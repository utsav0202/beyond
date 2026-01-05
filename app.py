import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy import or_, func
from datetime import datetime

from config import Config
from models import db, Employer, Candidate, Feedback
from forms import RegistrationForm, LoginForm, AddFeedbackForm, SearchForm

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    return Employer.query.get(int(user_id))


# Create instance directory (only for SQLite) and database
with app.app_context():
    # Only create instance directory if using SQLite (local development)
    database_url = os.environ.get('DATABASE_URL')
    if not database_url:
        os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)
    # Create all database tables
    db.create_all()


@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Employer registration"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        employer = Employer(
            username=form.username.data,
            email=form.email.data,
            company_name=form.company_name.data
        )
        employer.set_password(form.password.data)
        
        db.session.add(employer)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Employer login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        employer = Employer.query.filter_by(username=form.username.data).first()
        
        if employer and employer.check_password(form.password.data):
            login_user(employer)
            flash(f'Welcome back, {employer.username}!', 'success')
            
            # Redirect to next page or dashboard
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    """Employer logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    """Employer dashboard"""
    # Get statistics
    total_candidates = Candidate.query.count()
    my_feedback_count = Feedback.query.filter_by(employer_id=current_user.id).count()
    
    # Get recent feedback by this employer
    recent_feedback = Feedback.query.filter_by(employer_id=current_user.id)\
        .order_by(Feedback.created_at.desc())\
        .limit(5)\
        .all()
    
    return render_template('dashboard.html',
                         total_candidates=total_candidates,
                         my_feedback_count=my_feedback_count,
                         recent_feedback=recent_feedback)


@app.route('/add-feedback', methods=['GET', 'POST'])
@login_required
def add_feedback():
    """Add employee feedback"""
    form = AddFeedbackForm()
    
    if form.validate_on_submit():
        # Check if candidate exists by email
        candidate = Candidate.query.filter_by(email=form.candidate_email.data).first()
        
        if not candidate:
            # Create new candidate profile
            candidate = Candidate(
                full_name=form.candidate_name.data,
                email=form.candidate_email.data,
                phone=form.candidate_phone.data
            )
            db.session.add(candidate)
            db.session.flush()  # Get candidate ID
        else:
            # Update candidate info if provided and different
            if form.candidate_name.data and form.candidate_name.data != candidate.full_name:
                candidate.full_name = form.candidate_name.data
            if form.candidate_phone.data and form.candidate_phone.data != candidate.phone:
                candidate.phone = form.candidate_phone.data
            candidate.updated_at = datetime.utcnow()
        
        # Create feedback entry
        feedback = Feedback(
            candidate_id=candidate.id,
            employer_id=current_user.id,
            role=form.role.data,
            expertise=form.expertise.data,
            feedback_text=form.feedback_text.data,
            rating=int(form.rating.data),
            employment_start=form.employment_start.data,
            employment_end=form.employment_end.data
        )
        
        db.session.add(feedback)
        db.session.commit()
        
        flash(f'Feedback for {candidate.full_name} has been added successfully!', 'success')
        return redirect(url_for('candidate_profile', candidate_id=candidate.id))
    
    return render_template('add_feedback.html', form=form)


@app.route('/candidate/<int:candidate_id>')
@login_required
def candidate_profile(candidate_id):
    """View candidate profile with all feedback"""
    candidate = Candidate.query.get_or_404(candidate_id)
    
    # Get all feedback for this candidate
    feedbacks = Feedback.query.filter_by(candidate_id=candidate_id)\
        .order_by(Feedback.created_at.desc())\
        .all()
    
    # Calculate aggregate data
    avg_rating = candidate.get_average_rating()
    all_expertise = candidate.get_all_expertise()
    feedback_count = candidate.get_feedback_count()
    
    return render_template('candidate_profile.html',
                         candidate=candidate,
                         feedbacks=feedbacks,
                         avg_rating=avg_rating,
                         all_expertise=all_expertise,
                         feedback_count=feedback_count)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    """Search candidates"""
    form = SearchForm()
    results = []
    
    if form.validate_on_submit() or request.args.get('role') or request.args.get('expertise'):
        # Get search parameters
        role = form.role.data or request.args.get('role', '')
        expertise = form.expertise.data or request.args.get('expertise', '')
        min_rating = form.min_rating.data or request.args.get('min_rating', '')
        
        # Start with all candidates
        query = Candidate.query
        
        # Filter by role (search in feedback)
        if role:
            query = query.join(Feedback).filter(
                Feedback.role.ilike(f'%{role}%')
            )
        
        # Filter by expertise (search in feedback)
        if expertise:
            expertise_terms = [term.strip() for term in expertise.split(',')]
            expertise_filters = []
            for term in expertise_terms:
                expertise_filters.append(Feedback.expertise.ilike(f'%{term}%'))
            
            if not role:  # Only join if not already joined
                query = query.join(Feedback)
            query = query.filter(or_(*expertise_filters))
        
        # Get distinct candidates
        candidates = query.distinct().all()
        
        # Filter by minimum rating if specified
        if min_rating:
            min_rating_value = float(min_rating)
            candidates = [c for c in candidates if c.get_average_rating() >= min_rating_value]
        
        # Prepare results with summary data
        for candidate in candidates:
            results.append({
                'id': candidate.id,
                'name': candidate.full_name,
                'email': candidate.email,
                'avg_rating': round(candidate.get_average_rating(), 1),
                'expertise': candidate.get_all_expertise()[:5],  # Top 5 skills
                'feedback_count': candidate.get_feedback_count()
            })
        
        # Sort by average rating (descending)
        results.sort(key=lambda x: x['avg_rating'], reverse=True)
        
        if not results:
            flash('No candidates found matching your criteria.', 'info')
    
    return render_template('search.html', form=form, results=results)


@app.template_filter('star_rating')
def star_rating_filter(rating):
    """Template filter to display star rating"""
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    
    stars = '★' * full_stars
    if half_star:
        stars += '⯨'
    stars += '☆' * empty_stars
    
    return stars


@app.context_processor
def utility_processor():
    """Add utility functions to templates"""
    def format_date(date):
        if not date:
            return 'N/A'
        return date.strftime('%B %Y')
    
    return dict(format_date=format_date)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)


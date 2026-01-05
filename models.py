from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Employer(UserMixin, db.Model):
    """Employer/HR user model"""
    __tablename__ = 'employers'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationship to feedback
    feedbacks = db.relationship('Feedback', backref='employer', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash and set password"""
        # Use pbkdf2:sha256 instead of scrypt for Python 3.9 compatibility
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    
    def check_password(self, password):
        """Verify password"""
        try:
            return check_password_hash(self.password_hash, password)
        except AttributeError as e:
            # Handle case where scrypt is not available (Python < 3.11)
            if 'scrypt' in str(e):
                # If password hash uses scrypt, we need to rehash with pbkdf2
                # This happens when database was created with Python 3.11+ but running on 3.9
                raise ValueError(
                    "Password hash uses scrypt which is not available in Python 3.9. "
                    "Please delete instance/candidates.db and run 'python populate_test_data.py' to recreate the database."
                )
            raise
    
    def __repr__(self):
        return f'<Employer {self.username} - {self.company_name}>'


class Candidate(db.Model):
    """Candidate/Employee profile model"""
    __tablename__ = 'candidates'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relationship to feedback
    feedbacks = db.relationship('Feedback', backref='candidate', lazy='dynamic', cascade='all, delete-orphan')
    
    def get_average_rating(self):
        """Calculate average rating from all feedback"""
        feedbacks = self.feedbacks.all()
        if not feedbacks:
            return 0
        return sum(f.rating for f in feedbacks) / len(feedbacks)
    
    def get_all_expertise(self):
        """Get unique list of all expertise/skills from feedback"""
        expertise_set = set()
        for feedback in self.feedbacks.all():
            if feedback.expertise:
                skills = [skill.strip() for skill in feedback.expertise.split(',')]
                expertise_set.update(skills)
        return sorted(list(expertise_set))
    
    def get_feedback_count(self):
        """Get total number of feedback entries"""
        return self.feedbacks.count()
    
    def __repr__(self):
        return f'<Candidate {self.full_name} - {self.email}>'


class Feedback(db.Model):
    """Employment feedback model"""
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False, index=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'), nullable=False, index=True)
    
    # Feedback details
    role = db.Column(db.String(120), nullable=False, index=True)
    expertise = db.Column(db.Text, nullable=True)  # Comma-separated skills
    feedback_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 rating
    
    # Employment period
    employment_start = db.Column(db.Date, nullable=True)
    employment_end = db.Column(db.Date, nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    
    def get_expertise_list(self):
        """Get expertise as a list"""
        if not self.expertise:
            return []
        return [skill.strip() for skill in self.expertise.split(',')]
    
    def get_employment_duration(self):
        """Calculate employment duration in months"""
        if not self.employment_start or not self.employment_end:
            return None
        delta = self.employment_end - self.employment_start
        return round(delta.days / 30)
    
    def __repr__(self):
        return f'<Feedback for {self.candidate.full_name} by {self.employer.company_name}>'


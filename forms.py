from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Optional, NumberRange
from models import Employer, Candidate


class RegistrationForm(FlaskForm):
    """Employer registration form"""
    username = StringField('Username', 
                          validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', 
                       validators=[DataRequired(), Email()])
    company_name = StringField('Company Name', 
                              validators=[DataRequired(), Length(min=2, max=120)])
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        """Check if username already exists"""
        employer = Employer.query.filter_by(username=username.data).first()
        if employer:
            raise ValidationError('Username already taken. Please choose a different one.')
    
    def validate_email(self, email):
        """Check if email already exists"""
        employer = Employer.query.filter_by(email=email.data).first()
        if employer:
            raise ValidationError('Email already registered. Please use a different one.')


class LoginForm(FlaskForm):
    """Employer login form"""
    username = StringField('Username', 
                          validators=[DataRequired()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    submit = SubmitField('Login')


class AddFeedbackForm(FlaskForm):
    """Add employee feedback form"""
    candidate_email = StringField('Candidate Email', 
                                 validators=[DataRequired(), Email()],
                                 render_kw={"placeholder": "candidate@example.com"})
    candidate_name = StringField('Candidate Full Name', 
                                validators=[DataRequired(), Length(min=2, max=120)],
                                render_kw={"placeholder": "John Doe"})
    candidate_phone = StringField('Candidate Phone (Optional)', 
                                 validators=[Optional(), Length(max=20)],
                                 render_kw={"placeholder": "+1234567890"})
    
    role = StringField('Role/Position', 
                      validators=[DataRequired(), Length(min=2, max=120)],
                      render_kw={"placeholder": "Software Engineer"})
    
    expertise = StringField('Expertise/Skills', 
                           validators=[DataRequired()],
                           render_kw={"placeholder": "Python, Flask, SQL, Docker"})
    
    feedback_text = TextAreaField('Feedback', 
                                 validators=[DataRequired(), Length(min=10, max=2000)],
                                 render_kw={"rows": 5, "placeholder": "Provide detailed feedback about the candidate's performance, work ethic, and contributions..."})
    
    rating = SelectField('Rating', 
                        choices=[('5', '5 - Excellent'), 
                                ('4', '4 - Very Good'), 
                                ('3', '3 - Good'), 
                                ('2', '2 - Fair'), 
                                ('1', '1 - Poor')],
                        validators=[DataRequired()])
    
    employment_start = DateField('Employment Start Date', 
                                validators=[Optional()],
                                format='%Y-%m-%d')
    
    employment_end = DateField('Employment End Date', 
                              validators=[Optional()],
                              format='%Y-%m-%d')
    
    submit = SubmitField('Submit Feedback')
    
    def validate_employment_end(self, employment_end):
        """Ensure end date is after start date"""
        if employment_end.data and self.employment_start.data:
            if employment_end.data < self.employment_start.data:
                raise ValidationError('Employment end date must be after start date.')


class SearchForm(FlaskForm):
    """Search candidates form"""
    role = StringField('Job Role', 
                      validators=[Optional()],
                      render_kw={"placeholder": "e.g., Software Engineer, Manager"})
    
    expertise = StringField('Required Skills/Expertise', 
                           validators=[Optional()],
                           render_kw={"placeholder": "e.g., Python, Management, Sales"})
    
    min_rating = SelectField('Minimum Rating', 
                            choices=[('', 'Any Rating'),
                                   ('1', '1 Star or Above'),
                                   ('2', '2 Stars or Above'),
                                   ('3', '3 Stars or Above'),
                                   ('4', '4 Stars or Above'),
                                   ('5', '5 Stars Only')],
                            validators=[Optional()])
    
    submit = SubmitField('Search')


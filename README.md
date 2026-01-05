# Beyond - HR Candidate Reference System

Beyond is a web application that allows employers to share and access employment references for candidates, helping make better hiring decisions through transparent feedback from previous employers.

## Features

- **Employer Authentication**: Secure registration and login system for HR professionals
- **Add Employee Feedback**: Submit detailed feedback about past employees including role, expertise, ratings, and employment dates
- **Search Candidates**: Find candidates based on job requirements, skills, and minimum ratings
- **Candidate Profiles**: View comprehensive profiles with aggregated feedback from multiple employers
- **Dashboard**: Quick access to stats and recent activity

## Tech Stack

- **Backend**: Flask 3.0
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF with WTForms
- **Frontend**: Bootstrap 5 with Jinja2 templates

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd beyond
```

2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5001
```

## Usage

### For Employers

1. **Register**: Create an account with your company name, email, and credentials
2. **Login**: Access your dashboard
3. **Add Feedback**: Submit feedback for past employees (creates or updates candidate profiles)
4. **Search**: Find candidates by role, skills, or minimum rating
5. **View Profiles**: Access detailed candidate information with all employer feedback

### Database

The SQLite database is automatically created on first run in the `instance/` directory. It contains three main tables:
- **Employers**: Registered HR users/employers
- **Candidates**: Employee profiles (created when feedback is submitted)
- **Feedback**: Employment feedback entries linking employers to candidates

## Security Features

- Password hashing using Werkzeug
- CSRF protection on all forms
- Session-based authentication
- SQL injection prevention via SQLAlchemy ORM
- Secure session cookies

## Project Structure

```
beyond/
├── app.py                    # Main Flask application
├── models.py                 # Database models
├── forms.py                  # WTForms definitions
├── config.py                 # Configuration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_feedback.html
│   ├── candidate_profile.html
│   └── search.html
├── static/                  # Static assets
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── instance/                # Database storage
    └── candidates.db
```

## License

This project is for educational/demonstration purposes.


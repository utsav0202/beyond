# Beyond - Quick Start Guide

## Installation & Setup

### 1. Install Dependencies

Make sure you have Python 3.8+ installed, then install the required packages:

```bash
cd beyond
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5001`

The SQLite database will be automatically created in the `instance/` directory on first run.

## Usage Guide

### First Time Setup

1. **Open your browser** and navigate to `http://localhost:5001`

2. **Register** your company:
   - Click "Get Started" or "Register"
   - Fill in:
     - Company Name (e.g., "Tech Corp")
     - Username (e.g., "john_hr")
     - Email (e.g., "john@techcorp.com")
     - Password (min 6 characters)
   - Click "Register"

3. **Login** with your credentials

### Adding Employee Feedback

1. From the dashboard, click **"Add Employee Feedback"**

2. Fill in the candidate information:
   - **Email**: Used to identify or create the candidate profile (required)
   - **Full Name**: The candidate's name (required)
   - **Phone**: Optional contact number

3. Add employment details:
   - **Role/Position**: e.g., "Senior Software Engineer"
   - **Skills/Expertise**: e.g., "Python, Flask, Docker, AWS"
   - **Employment Dates**: Start and end dates (optional)

4. Provide your feedback:
   - **Rating**: 1-5 stars
   - **Feedback Text**: Detailed comments about their performance

5. Click **"Submit Feedback"**

**Note**: If the candidate email already exists, your feedback will be added to their existing profile. Otherwise, a new profile is created.

### Searching for Candidates

1. Click **"Search"** in the navigation menu

2. Use filters to find candidates:
   - **Job Role**: Search by position (e.g., "Engineer", "Manager")
   - **Required Skills**: Enter comma-separated skills (e.g., "Python, AWS")
   - **Minimum Rating**: Filter by star rating (1-5)

3. Click **"Search"**

4. Results show:
   - Candidate name and email
   - Average rating
   - Top 5 skills
   - Number of reviews

5. Click **"View Profile"** to see full details

### Viewing Candidate Profiles

Candidate profiles display:

- **Basic Information**: Name, email, phone
- **Aggregate Rating**: Average rating from all employers
- **Skills Summary**: All unique skills from feedback entries
- **Employer Feedback**: Detailed feedback from each employer including:
  - Company name
  - Role held
  - Employment period and duration
  - Skills used
  - Rating and detailed feedback
  - Date added

## Features Overview

### Dashboard
- View total candidates in system
- See your feedback count
- Quick access to add feedback and search
- Recent activity list

### Add Feedback
- Create or update candidate profiles
- Automatic profile detection by email
- Comprehensive feedback forms
- Date validation

### Search
- Multi-criteria search
- Role-based filtering
- Skill matching
- Minimum rating filter
- Sorted results by rating

### Candidate Profiles
- Aggregated ratings
- Complete skill inventory
- Multiple employer feedback
- Employment history
- Timeline of feedback

## Tips & Best Practices

1. **Be Honest**: Provide genuine, constructive feedback to help other employers make informed decisions

2. **Be Detailed**: Include specific examples of skills, projects, and contributions

3. **Use Complete Skills**: Enter full skill names (e.g., "Python" not "Py", "Machine Learning" not "ML")

4. **Verify Emails**: Double-check candidate email addresses to ensure feedback is added to the correct profile

5. **Add Dates**: Including employment dates helps provide context and validates the feedback timeline

## Database Location

The SQLite database is stored at:
```
beyond/instance/candidates.db
```

## Security Notes

- Passwords are hashed using Werkzeug's secure password hashing
- CSRF protection is enabled on all forms
- Session cookies are HTTP-only
- SQL injection prevention via SQLAlchemy ORM

## Troubleshooting

### Issue: Can't login
- Verify your username and password are correct
- Usernames are case-sensitive

### Issue: Candidate not found in search
- Check your search criteria
- Try broader search terms
- Remove minimum rating filter

### Issue: Database error
- Ensure the `instance/` directory exists
- Delete `instance/candidates.db` to recreate the database

## Project Structure

```
beyond/
├── app.py                    # Main Flask application with all routes
├── models.py                 # SQLAlchemy database models
├── forms.py                  # WTForms for all forms
├── config.py                 # Application configuration
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── QUICKSTART.md            # This file
├── .gitignore               # Git ignore patterns
├── templates/               # HTML templates
│   ├── base.html            # Base template with navbar
│   ├── index.html           # Landing page
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── dashboard.html       # Employer dashboard
│   ├── add_feedback.html    # Add feedback form
│   ├── candidate_profile.html # Candidate profile view
│   └── search.html          # Search page
├── static/                  # Static assets
│   ├── css/
│   │   └── style.css        # Custom styles
│   └── js/
│       └── main.js          # Frontend JavaScript
└── instance/                # Generated on first run
    └── candidates.db         # SQLite database
```

## Support

For issues or questions, please refer to the main README.md file.

---

**Beyond** - Reference checks reimagined for modern hiring


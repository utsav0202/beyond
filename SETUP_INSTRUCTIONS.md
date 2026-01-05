# Beyond - Setup Instructions for New Users

## Prerequisites

Before you begin, make sure you have:
- **Python 3.8 or higher** installed on your system
- **pip** (Python package manager) installed
- A web browser (Chrome, Firefox, Safari, etc.)

To check your Python version:
```bash
python --version
# or
python3 --version
```

## Installation Steps

### Step 1: Extract the ZIP file

Extract the `beyond.zip` file to a location of your choice. You should see a folder structure like this:

```
beyond/
├── app.py
├── models.py
├── forms.py
├── config.py
├── requirements.txt
├── instance/
│   └── candidates.db    (pre-populated database)
├── templates/
├── static/
└── ...
```

### Step 2: Open Terminal/Command Prompt

Navigate to the extracted `beyond` folder:

**On Mac/Linux:**
```bash
cd /path/to/beyond
```

**On Windows:**
```cmd
cd C:\path\to\beyond
```

### Step 3: Create Virtual Environment

Create a Python virtual environment to keep dependencies isolated:

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` appear at the beginning of your command prompt.

### Step 4: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install Flask and all other necessary libraries.

### Step 5: Run the Application

Start the Flask server:

```bash
python app.py
```

You should see output like:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
```

### Step 6: Access the Application

Open your web browser and go to:
```
http://127.0.0.1:5001
```
or
```
http://localhost:5001
```

You should see the Beyond landing page!

## 🔐 Login Credentials

The database comes pre-populated with 3 employer accounts and 22 candidate profiles.

### Account 1: TechCorp Industries
- **Username:** `techcorp_hr`
- **Password:** `password123`
- Candidates: 4 US employees + 5 Indian employees

### Account 2: Innovate Solutions
- **Username:** `innovate_hr`
- **Password:** `password123`
- Candidates: 4 US employees + 4 Indian employees

### Account 3: Global Enterprises Inc
- **Username:** `global_hr`
- **Password:** `password123`
- Candidates: 4 US employees + 4 Indian employees

## 📊 What's Included

The database includes:
- **3 Employer accounts** (different companies)
- **22 Unique candidates** (12 from USA, 10 from India)
- **31 Feedback entries** (some candidates have feedback from multiple employers)
- **Diverse roles:** Engineers, Managers, Designers, Data Scientists, etc.
- **Real-world data:** Ratings, employment dates, skills, detailed feedback

## 🎯 Features to Try

1. **Login** - Use any of the three accounts above
2. **Dashboard** - View statistics and recent activity
3. **Search Candidates** - Search by role, skills, or minimum rating
   - Try: "Developer", "Python", "Cloud", "Manager", etc.
4. **View Profiles** - Click on any candidate to see detailed feedback
5. **Add Feedback** - Submit feedback for new or existing candidates

## 🔧 Troubleshooting

### Port Already in Use

If you get an error that port 5001 is already in use, you can either:

1. **Kill the process using the port:**
   ```bash
   # On Mac/Linux
   lsof -ti:5001 | xargs kill -9
   
   # On Windows
   netstat -ano | findstr :5001
   taskkill /PID <PID_NUMBER> /F
   ```

2. **Run on a different port:**
   Edit `app.py` and change the last line to use a different port (e.g., 5002, 8000):
   ```python
   app.run(debug=True, host='0.0.0.0', port=5002)
   ```
   Then access at `http://127.0.0.1:5002`

### Module Not Found Error

If you get "ModuleNotFoundError", make sure:
1. Your virtual environment is activated (you see `(venv)` in your prompt)
2. You ran `pip install -r requirements.txt`
3. You're in the correct directory

### Database Issues

If you encounter database errors:
1. Make sure the `instance` folder exists
2. Delete `instance/candidates.db` and run `python app.py` again (will recreate empty DB)
3. Run `python populate_test_data.py` to repopulate with test data

## 📝 Notes

- **Database Location:** The SQLite database is in `instance/candidates.db`
- **Debug Mode:** The app runs in debug mode (auto-reload on code changes)
- **Security:** Change passwords before using in production
- **Stop Server:** Press `Ctrl+C` in the terminal to stop the server

## 🚀 Next Steps

Once you're logged in, you can:
- Explore existing candidate profiles
- Add feedback for new employees
- Search candidates based on your requirements
- See how multiple employers rated the same candidate

## 📞 Support

For issues or questions, refer to:
- `README.md` - Full project documentation
- `QUICKSTART.md` - Detailed usage guide
- `IMPLEMENTATION_SUMMARY.md` - Technical details

---

**Enjoy using Beyond!** 🎊


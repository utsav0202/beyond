# Deployment Guide: Beyond HR Candidate Reference System

This guide will walk you through deploying the Beyond app to Render's free tier.

## Prerequisites

- A GitHub account
- Your code pushed to a GitHub repository
- A Render account (sign up at https://render.com - it's free)

## Step 1: Prepare Your Code

1. **Ensure all changes are committed and pushed to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Verify your repository is accessible** on GitHub.

## Step 2: Create a Render Account

1. Go to https://render.com
2. Sign up using your GitHub account (recommended for easy integration)
3. Verify your email if prompted

## Step 3: Create PostgreSQL Database

1. In the Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure the database:
   - **Name**: `beyond-db` (or any name you prefer)
   - **Database**: `beyond` (or leave default)
   - **User**: Leave default
   - **Region**: Choose closest to your users
   - **PostgreSQL Version**: Latest (default)
   - **Plan**: **Free** (for free tier)
3. Click **"Create Database"**
4. **Important**: Wait for the database to be fully created (status shows "Available")
5. **Note the connection details** - you'll see:
   - Internal Database URL (for connecting from your web service)
   - External Database URL (for local connections if needed)

## Step 4: Create Web Service

1. In the Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository:
   - Click **"Connect account"** if not already connected
   - Authorize Render to access your repositories
   - Select your repository containing the Beyond app
3. Configure the web service:
   - **Name**: `beyond-app` (or any name you prefer)
   - **Region**: Choose same region as your database
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (if app is in root) or specify subdirectory
   - **Runtime**: **Python 3** (auto-detected)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (or leave empty - Procfile will be used)
   - **Plan**: **Free** (for free tier)

## Step 5: Configure Environment Variables

In your web service settings, go to **"Environment"** tab and add:

1. **SECRET_KEY**:
   - **Run this command on YOUR LOCAL COMPUTER** (in Terminal), NOT on Render:
     ```bash
     python3 -c "import secrets; print(secrets.token_hex(32))"
     ```
   - Copy the output (a long random string) and paste it as the value for `SECRET_KEY` in Render
   - **OR** use this pre-generated one: `16db08175609da7ae2292526ae1fc94b9f1e401869910ec5392f71afe5db9044`
   - This is critical for session security and CSRF protection

2. **DATABASE_URL**:
   - Go back to your PostgreSQL database dashboard
   - Copy the **Internal Database URL** (starts with `postgresql://`)
   - Paste it as the value for `DATABASE_URL` in your web service environment variables

## Step 6: Deploy

1. Click **"Create Web Service"** (or **"Save Changes"** if editing)
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Build your application
   - Start the web service
3. Watch the build logs - you should see:
   - Dependencies being installed
   - Database tables being created (from `db.create_all()`)
   - Application starting successfully

## Step 7: Verify Deployment

1. Once deployment completes, you'll see a URL like: `https://beyond-app.onrender.com`
2. Click the URL to open your app
3. **First visit may take 10-30 seconds** (free tier wakes up from sleep)
4. Test the application:
   - Register a new employer account
   - Login
   - Add feedback for a candidate
   - Search for candidates
   - Verify data persists after refresh

## Step 8: Update Your App (Future Deployments)

Whenever you push changes to GitHub:

1. **Commit and push your changes:**
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```

2. **Render automatically detects the push** and starts a new deployment
3. Monitor the deployment in Render dashboard
4. Your app updates automatically (usually takes 2-5 minutes)

## Troubleshooting

### Build Fails

- **Check build logs** in Render dashboard for error messages
- Common issues:
  - Missing dependencies in `requirements.txt`
  - Python version mismatch (check `runtime.txt`)
  - Syntax errors in code

### Database Connection Errors

- Verify `DATABASE_URL` is set correctly in environment variables
- Ensure database status is "Available" before deploying web service
- Check that you're using the **Internal Database URL** (not external)

### App Crashes on Startup

- Check **Runtime logs** in Render dashboard
- Common issues:
  - Missing environment variables (especially `SECRET_KEY`)
  - Database not accessible
  - Port binding issues (should use `gunicorn` via Procfile)

### Slow First Request

- This is normal on free tier - app sleeps after 15 minutes of inactivity
- First request wakes it up (10-30 seconds)
- Subsequent requests are fast
- Anyone visiting the URL automatically wakes it up

### Database Expires After 90 Days

- Free tier PostgreSQL expires after 90 days
- Options:
  1. Upgrade to paid tier ($7/month)
  2. Export data and recreate database
  3. Use external PostgreSQL service (some have free tiers)

## Environment Variables Reference

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `SECRET_KEY` | Yes | Flask secret key for sessions | Generated random string |
| `DATABASE_URL` | Yes | PostgreSQL connection string | Auto-provided by Render |

## Free Tier Limitations

- **Web Service**: Sleeps after 15 minutes of inactivity (wakes automatically on visit)
- **PostgreSQL**: Expires after 90 days (can be recreated)
- **Build Time**: Limited to 10 minutes
- **Bandwidth**: 100 GB/month

## Security Notes

- Never commit `.env` file or `SECRET_KEY` to GitHub
- Use environment variables for all secrets
- HTTPS is automatically enabled on Render
- Secure cookies are enabled in production (when `DATABASE_URL` is set)

## Support

- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com
- Flask Documentation: https://flask.palletsprojects.com

## Next Steps

After successful deployment:

1. Share your app URL with users
2. Monitor usage in Render dashboard
3. Set up custom domain (optional, requires paid tier)
4. Configure email notifications (if needed)
5. Set up database backups (recommended for production)


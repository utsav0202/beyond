# Push to GitHub - Quick Guide

Your code is committed and ready to push! Follow these steps:

## Option 1: Create New GitHub Repository (Recommended)

1. **Go to GitHub**: https://github.com/new
2. **Create a new repository**:
   - Repository name: `beyond` (or any name you prefer)
   - Description: "HR Candidate Reference System"
   - Choose **Public** or **Private**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click **"Create repository"**

3. **Copy the repository URL** (it will look like: `https://github.com/YOUR_USERNAME/beyond.git`)

4. **Run these commands** (replace YOUR_USERNAME with your GitHub username):
   ```bash
   cd /Users/utsav/git/beyond
   git remote add origin https://github.com/YOUR_USERNAME/beyond.git
   git branch -M main
   git push -u origin main
   ```

## Option 2: If You Already Have a GitHub Repository

If you already created a repository, just run:

```bash
cd /Users/utsav/git/beyond
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## After Pushing

Once your code is on GitHub, you can proceed with Render deployment following `DEPLOYMENT.md`.


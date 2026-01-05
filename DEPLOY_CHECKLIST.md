# Complete Deployment Checklist

## ✅ Step 1: Code Preparation (DONE)
- [x] All deployment files created (Procfile, runtime.txt, etc.)
- [x] Configuration updated for PostgreSQL
- [x] Requirements updated with production dependencies
- [x] Code committed to git

## 📤 Step 2: Push to GitHub

### Create GitHub Repository:
1. Go to: https://github.com/new
2. Repository name: `beyond` (or your choice)
3. Set to **Public** or **Private**
4. **DO NOT** check "Add a README file"
5. Click **"Create repository"**

### Push Your Code:
Run these commands (replace YOUR_USERNAME):

```bash
cd /Users/utsav/git/beyond
git remote add origin https://github.com/YOUR_USERNAME/beyond.git
git branch -M main
git push -u origin main
```

**Or if you prefer SSH:**
```bash
git remote add origin git@github.com:YOUR_USERNAME/beyond.git
git branch -M main
git push -u origin main
```

## 🚀 Step 3: Deploy to Render

### 3.1 Create Render Account
- Go to: https://render.com
- Sign up with GitHub (recommended for easy integration)
- Verify email if needed

### 3.2 Create PostgreSQL Database
1. Click **"New +"** → **"PostgreSQL"**
2. Settings:
   - **Name**: `beyond-db`
   - **Database**: `beyond`
   - **Region**: Choose closest to you
   - **Plan**: **Free**
3. Click **"Create Database"**
4. Wait for status: **"Available"** ✅
5. **Note**: The Internal Database URL will be auto-injected to your web service

### 3.3 Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect GitHub:
   - Click **"Connect account"** if needed
   - Authorize Render
   - Select your `beyond` repository
3. Configure:
   - **Name**: `beyond-app`
   - **Region**: Same as database
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Runtime**: Python 3 (auto-detected)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: (leave empty - Procfile handles this)
   - **Plan**: **Free**
4. **Environment Variables** (click "Advanced" → "Add Environment Variable"):
   
   **IMPORTANT**: Run the Python command on YOUR LOCAL MACHINE (in Terminal), NOT on Render!
   
   **Step 4a - Generate SECRET_KEY (Run this locally):**
   ```bash
   # Open Terminal on your Mac and run:
   cd /Users/utsav/git/beyond
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```
   Copy the output (it will be a long random string like: `16db08175609da7ae2292526ae1fc94b...`)
   
   **OR use this pre-generated one:**
   ```
   16db08175609da7ae2292526ae1fc94b9f1e401869910ec5392f71afe5db9044
   ```
   
   **Step 4b - Add to Render:**
   - In Render's "Environment Variables" section, click "Add Environment Variable"
   - **Key**: `SECRET_KEY`
   - **Value**: Paste the generated key (without the `SECRET_KEY=` prefix, just the value)
   - Click "Save"
   
   **Step 4c - Add DATABASE_URL:**
   - Go to your PostgreSQL service dashboard
   - Copy the **Internal Database URL** (starts with `postgresql://`)
   - Back in Web Service → Environment Variables
   - **Key**: `DATABASE_URL`
   - **Value**: Paste the Internal Database URL
   - Click "Save"
5. Click **"Create Web Service"**

### 3.4 Wait for Deployment
- Watch build logs
- Should see: "Build successful" ✅
- First deployment takes 3-5 minutes

### 3.5 Get Your URL
- Once deployed, you'll see: `https://beyond-app.onrender.com`
- First visit may take 10-30 seconds (waking up)
- Test registration, login, and features

## 🎉 Step 4: Verify Everything Works

Test these features:
- [ ] Landing page loads
- [ ] Can register new employer account
- [ ] Can login
- [ ] Can add feedback for candidate
- [ ] Can search candidates
- [ ] Data persists after refresh

## 📝 Quick Reference

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Update app later:**
```bash
git add .
git commit -m "Your changes"
git push origin main
# Render auto-deploys!
```

## 🆘 Need Help?

- See `DEPLOYMENT.md` for detailed troubleshooting
- Render Docs: https://render.com/docs
- Check Render dashboard logs if issues occur


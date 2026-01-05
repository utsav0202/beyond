# 🔑 How to Set SECRET_KEY on Render

## Step-by-Step Visual Guide

### Step 1: Generate SECRET_KEY (Run on YOUR Mac)

**Open Terminal on your Mac** and run:

```bash
cd /Users/utsav/git/beyond
python3 -c "import secrets; print(secrets.token_hex(32))"
```

**You'll see output like:**
```
fd32d72b9e4a89601e339bea6bb915288d2e4d67b839dd7e59bd13891e555f93
```

**Copy this entire string** (the long random text)

---

### Step 2: Add to Render Dashboard

1. **Go to Render Dashboard** → Your Web Service → **"Environment"** tab

2. **Click "Add Environment Variable"** button

3. **Fill in:**
   - **Key**: `SECRET_KEY` (exactly like this, all caps)
   - **Value**: Paste the string you copied (just the random text, nothing else)
   
   Example:
   ```
   Key:   SECRET_KEY
   Value: fd32d72b9e4a89601e339bea6bb915288d2e4d67b839dd7e59bd13891e555f93
   ```

4. **Click "Save"**

---

## Quick Option: Use Pre-Generated Key

If you don't want to run the command, you can use this one:

**Key**: `SECRET_KEY`  
**Value**: `16db08175609da7ae2292526ae1fc94b9f1e401869910ec5392f71afe5db9044`

---

## Important Notes

- ✅ Run the Python command **on your Mac** (Terminal app)
- ✅ Copy the output **before** going to Render dashboard
- ✅ Paste **only the value** (the random string), not "SECRET_KEY="
- ✅ Make sure there are no extra spaces or characters

---

## Visual Flow

```
Your Mac Terminal          →    Render Dashboard
─────────────────              ──────────────────
Run Python command    →    Paste into Environment Variables
Copy output          →    Key: SECRET_KEY
                         Value: [paste here]
```


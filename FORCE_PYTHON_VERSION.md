# 🔧 Force Python 3.11 on Render

## Problem

Render is using Python 3.13, but we need Python 3.11 for compatibility.

## Solution: Add Environment Variable

If `runtime.txt` isn't being respected, add this environment variable in Render:

1. **Go to Render Dashboard** → Your Web Service (`beyond-app`)
2. **Go to "Environment" tab**
3. **Add Environment Variable:**
   - **Key**: `PYTHON_VERSION`
   - **Value**: `3.11.9`
4. **Save Changes**
5. **Redeploy**

## Alternative: Update runtime.txt Format

Some Render setups need a different format. Try updating `runtime.txt` to:

```
python-3.11
```

Or:

```
3.11.9
```

## What We've Done

1. ✅ Updated `requirements.txt` to use `psycopg[binary]==3.1.18` (supports Python 3.13)
2. ✅ Updated `config.py` to use `postgresql+psycopg://` dialect (explicitly uses psycopg3)
3. ✅ Updated `runtime.txt` to `python-3.11.9`

## Next Steps

1. **Push changes to GitHub:**
   ```bash
   git push origin main
   ```

2. **If Render still uses Python 3.13:**
   - Add `PYTHON_VERSION=3.11.9` environment variable in Render dashboard
   - Or the psycopg3 fix should work with Python 3.13

3. **Wait for deployment** and check logs

## Why This Should Work

- `psycopg3` supports Python 3.13 ✅
- Explicit dialect `postgresql+psycopg://` forces SQLAlchemy to use psycopg3 ✅
- If Python 3.11 is used, even better ✅


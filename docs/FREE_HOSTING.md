# 🆓 FREE 24/7 Bot Hosting Guide

## Option 1: PythonAnywhere (FREE Forever) ⭐ RECOMMENDED

### Features:
- ✅ 100% FREE forever
- ✅ No credit card required
- ✅ Easy setup
- ✅ Runs 24/7
- ✅ 512MB RAM (enough for Telegram bot)

### Step-by-Step Setup:

#### 1. Create Account
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Click **"Pricing & signup"**
3. Choose **"Create a Beginner account"** (FREE)
4. Sign up with email

#### 2. Upload Your Bot

**Option A: From GitHub (Recommended)**
```bash
# Open a Bash console in PythonAnywhere
git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git
cd Anachak-Kasekor-Chatbot
```

**Option B: Upload Files**
- Use the "Files" tab to upload your files manually

#### 3. Install Dependencies
```bash
# In PythonAnywhere Bash console
cd Anachak-Kasekor-Chatbot
pip3 install --user -r requirements.txt
```

#### 4. Create .env File
```bash
nano .env
```

Add your bot token:
```env
MAIN_BOT_TOKEN=your_bot_token_here
```

Save: `Ctrl+X`, then `Y`, then `Enter`

#### 5. Create Always-On Task

1. Go to **"Tasks"** tab
2. Under **"Always-on tasks"** (if available) or **"Scheduled tasks"**
3. For free accounts, use **"Scheduled tasks"**:
   - Command: `/home/YOUR_USERNAME/Anachak-Kasekor-Chatbot/.local/bin/python3 /home/YOUR_USERNAME/Anachak-Kasekor-Chatbot/main_bot.py`
   - Time: Every hour (or as frequent as allowed)

**Note:** Free PythonAnywhere doesn't have "always-on" tasks, but you can use scheduled tasks that run every hour.

#### 6. Keep Bot Running (Workaround for Free Tier)

Create a wrapper script:
```bash
nano run_bot.sh
```

Add:
```bash
#!/bin/bash
cd /home/YOUR_USERNAME/Anachak-Kasekor-Chatbot
while true; do
    python3 main_bot.py
    sleep 5
done
```

Make it executable:
```bash
chmod +x run_bot.sh
```

Run in background:
```bash
nohup ./run_bot.sh > bot.log 2>&1 &
```

---

## Option 2: Replit (FREE with Always-On) ⭐ EASIEST

### Features:
- ✅ FREE tier available
- ✅ No credit card required
- ✅ Browser-based IDE
- ✅ Easy deployment
- ✅ Can run 24/7 with UptimeRobot trick

### Step-by-Step Setup:

#### 1. Create Replit Account
1. Go to [replit.com](https://replit.com)
2. Sign up (free)

#### 2. Import from GitHub
1. Click **"Create Repl"**
2. Choose **"Import from GitHub"**
3. Paste: `https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot`
4. Click **"Import from GitHub"**

#### 3. Add Secrets (Environment Variables)
1. Click **"Secrets"** (lock icon) in left sidebar
2. Add:
   - Key: `MAIN_BOT_TOKEN`
   - Value: Your bot token
3. Click **"Add new secret"**

#### 4. Modify main_bot.py for Replit

Add this at the top of `main_bot.py`:
```python
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

Then in your `main()` function, add before `application.run_polling()`:
```python
keep_alive()  # Add this line
application.run_polling(allowed_updates=Update.ALL_TYPES)
```

#### 5. Run the Bot
1. Click **"Run"** button
2. Your bot starts!

#### 6. Keep It Running 24/7 (Free Trick)

Use **UptimeRobot** to ping your Replit every 5 minutes:

1. Copy your Replit URL (e.g., `https://your-repl.username.repl.co`)
2. Go to [uptimerobot.com](https://uptimerobot.com)
3. Sign up (free)
4. Click **"Add New Monitor"**
5. Settings:
   - Monitor Type: HTTP(s)
   - Friendly Name: Anachak Bot
   - URL: Your Replit URL
   - Monitoring Interval: 5 minutes
6. Click **"Create Monitor"**

Now your bot runs 24/7 for FREE! 🎉

---

## Option 3: Glitch (FREE)

### Features:
- ✅ FREE
- ✅ No credit card
- ✅ Easy setup
- ✅ Similar to Replit

### Setup:
1. Go to [glitch.com](https://glitch.com)
2. Sign up
3. Click **"New Project"** → **"Import from GitHub"**
4. Paste your repo URL
5. Add `.env` file with your token
6. Use same UptimeRobot trick as Replit

---

## Option 4: Oracle Cloud (FREE Forever)

### Features:
- ✅ FREE forever (generous free tier)
- ✅ 4 ARM CPUs
- ✅ 24GB RAM
- ✅ Professional VPS
- ✅ No credit card required initially

### Setup:
1. Go to [oracle.com/cloud/free](https://www.oracle.com/cloud/free/)
2. Sign up for free tier
3. Create a VM instance (Ubuntu)
4. Follow VPS setup from DEPLOYMENT.md

---

## Option 5: Your Own Computer (Linux) - FREE

### Using systemd (Runs on boot)

Create service file:
```bash
sudo nano /etc/systemd/system/anachak-bot.service
```

Add:
```ini
[Unit]
Description=Anachak Kasekor Bot
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/Anachak-Kasekor-Chatbot
Environment="PATH=/home/YOUR_USERNAME/Anachak-Kasekor-Chatbot/.venv/bin"
ExecStart=/home/YOUR_USERNAME/Anachak-Kasekor-Chatbot/.venv/bin/python main_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable anachak-bot
sudo systemctl start anachak-bot
sudo systemctl status anachak-bot
```

Commands:
```bash
# Check status
sudo systemctl status anachak-bot

# View logs
sudo journalctl -u anachak-bot -f

# Restart
sudo systemctl restart anachak-bot

# Stop
sudo systemctl stop anachak-bot
```

---

## Option 6: Termux (Android Phone) - FREE

Run your bot on your Android phone!

### Setup:
1. Install **Termux** from F-Droid or Play Store
2. Open Termux and run:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install Python and Git
pkg install python git -y

# Clone your repository
git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git
cd Anachak-Kasekor-Chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env file
nano .env
# Add your bot token, save with Ctrl+X

# Run bot
python main_bot.py
```

### Keep Running in Background:
```bash
# Install termux-services
pkg install termux-services -y

# Run in background
nohup python main_bot.py > bot.log 2>&1 &

# Check if running
ps aux | grep python
```

**Tip:** Keep your phone plugged in and connected to WiFi!

---

## Comparison Table

| Platform | Cost | Difficulty | Uptime | Credit Card |
|----------|------|------------|--------|-------------|
| **Replit** | FREE | ⭐ Easy | 99%+ | No |
| **PythonAnywhere** | FREE | ⭐⭐ Medium | 95%+ | No |
| **Glitch** | FREE | ⭐ Easy | 99%+ | No |
| **Oracle Cloud** | FREE | ⭐⭐⭐ Hard | 99.9%+ | Yes (but free) |
| **Your Computer** | FREE | ⭐⭐ Medium | Depends | No |
| **Termux (Phone)** | FREE | ⭐⭐ Medium | Depends | No |

---

## My Recommendation:

### For Beginners: **Replit** ⭐
- Easiest setup
- Works immediately
- Free 24/7 with UptimeRobot

### For Long-term: **Oracle Cloud** ⭐⭐⭐
- Professional VPS
- Free forever
- Best performance

### For Testing: **Your Computer** ⭐⭐
- Quick setup
- Full control
- Good for development

---

## Need Help?

Choose the option that works best for you and follow the guide. All options are 100% FREE! 🎉

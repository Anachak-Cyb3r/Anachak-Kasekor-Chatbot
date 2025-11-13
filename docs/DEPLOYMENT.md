# 🚀 Deployment Guide

This guide shows you how to run your bot 24/7 like a server.

## Option 1: Deploy to Render.com (FREE) ⭐ Recommended

### Step 1: Prepare Your Repository

Create a `render.yaml` file in your project root:

```yaml
services:
  - type: web
    name: anachak-kasekor-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main_bot.py
    envVars:
      - key: MAIN_BOT_TOKEN
        sync: false
```

### Step 2: Deploy to Render

1. Go to [render.com](https://render.com) and sign up
2. Click **New +** → **Web Service**
3. Connect your GitHub account
4. Select your repository: `Anachak-Kasekor-Chatbot`
5. Configure:
   - **Name:** anachak-kasekor-bot
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main_bot.py`
6. Add Environment Variable:
   - **Key:** `MAIN_BOT_TOKEN`
   - **Value:** Your bot token
7. Click **Create Web Service**

Your bot will be live in 2-3 minutes! ✅

---

## Option 2: Deploy to Railway.app (FREE $5/month)

### Step 1: Create railway.json

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python main_bot.py",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Step 2: Deploy

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **New Project** → **Deploy from GitHub repo**
4. Select your repository
5. Add environment variables:
   - `MAIN_BOT_TOKEN` = your token
6. Deploy automatically starts!

---

## Option 3: VPS Deployment (DigitalOcean, Linode, etc.)

### Step 1: Create a VPS

1. Sign up for a VPS provider (e.g., DigitalOcean)
2. Create a new Droplet/Server:
   - **OS:** Ubuntu 22.04 LTS
   - **Plan:** Basic $4-6/month
   - **Region:** Closest to your users

### Step 2: Connect to Your Server

```bash
ssh root@your_server_ip
```

### Step 3: Install Dependencies

```bash
# Update system
apt update && apt upgrade -y

# Install Python and pip
apt install python3 python3-pip python3-venv git -y

# Install supervisor (to keep bot running)
apt install supervisor -y
```

### Step 4: Clone Your Repository

```bash
# Create app directory
mkdir -p /opt/bots
cd /opt/bots

# Clone your repository
git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git
cd Anachak-Kasekor-Chatbot

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 5: Create .env File

```bash
nano .env
```

Add your bot token:
```env
MAIN_BOT_TOKEN=your_bot_token_here
```

Save with `Ctrl+X`, then `Y`, then `Enter`.

### Step 6: Set Up Supervisor (Auto-restart)

Create supervisor config:
```bash
nano /etc/supervisor/conf.d/anachak-bot.conf
```

Add this configuration:
```ini
[program:anachak-bot]
directory=/opt/bots/Anachak-Kasekor-Chatbot
command=/opt/bots/Anachak-Kasekor-Chatbot/.venv/bin/python main_bot.py
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/anachak-bot.err.log
stdout_logfile=/var/log/anachak-bot.out.log
environment=PATH="/opt/bots/Anachak-Kasekor-Chatbot/.venv/bin"
```

### Step 7: Start the Bot

```bash
# Reload supervisor
supervisorctl reread
supervisorctl update

# Start the bot
supervisorctl start anachak-bot

# Check status
supervisorctl status anachak-bot
```

### Useful Commands

```bash
# Check bot status
supervisorctl status anachak-bot

# Stop bot
supervisorctl stop anachak-bot

# Restart bot
supervisorctl restart anachak-bot

# View logs
tail -f /var/log/anachak-bot.out.log

# View errors
tail -f /var/log/anachak-bot.err.log
```

---

## Option 4: Run on Your Local Computer (Linux/Mac)

### Using systemd (Linux)

Create a service file:
```bash
sudo nano /etc/systemd/system/anachak-bot.service
```

Add:
```ini
[Unit]
Description=Anachak Kasekor Telegram Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/Anachak-Kasekor-Chatbot
Environment="PATH=/path/to/Anachak-Kasekor-Chatbot/.venv/bin"
ExecStart=/path/to/Anachak-Kasekor-Chatbot/.venv/bin/python main_bot.py
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

### Using screen (Simple method)

```bash
# Install screen
sudo apt install screen -y

# Start a screen session
screen -S anachak-bot

# Run your bot
cd /path/to/Anachak-Kasekor-Chatbot
source .venv/bin/activate
python main_bot.py

# Detach from screen: Press Ctrl+A, then D

# Reattach to screen
screen -r anachak-bot

# List all screens
screen -ls
```

---

## Option 5: Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main_bot.py"]
```

### Create docker-compose.yml

```yaml
version: '3.8'

services:
  bot:
    build: .
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - ./img:/app/img
```

### Deploy

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## Comparison Table

| Option | Cost | Difficulty | Uptime | Best For |
|--------|------|------------|--------|----------|
| Render.com | Free | ⭐ Easy | 99%+ | Beginners |
| Railway.app | Free ($5 credit) | ⭐ Easy | 99%+ | Beginners |
| VPS | $4-6/month | ⭐⭐ Medium | 99.9%+ | Production |
| Local Computer | Free | ⭐⭐ Medium | Depends | Testing |
| Docker | Varies | ⭐⭐⭐ Hard | 99.9%+ | Advanced |

---

## Monitoring Your Bot

### Check if Bot is Running

Send `/start` to your bot on Telegram. If it responds, it's running!

### Set Up Uptime Monitoring (Free)

1. **UptimeRobot** - [uptimerobot.com](https://uptimerobot.com)
   - Free monitoring
   - Email alerts if bot goes down
   - 5-minute check intervals

2. **Better Uptime** - [betteruptime.com](https://betteruptime.com)
   - Free tier available
   - Status page
   - Incident management

---

## Troubleshooting

### Bot Stops Running
- Check logs for errors
- Verify bot token is correct
- Ensure server has internet connection
- Check if process is running: `ps aux | grep python`

### Bot Responds Slowly
- Check server resources (CPU, RAM)
- Verify internet speed
- Consider upgrading server plan

### Bot Doesn't Start After Reboot
- Ensure auto-start is enabled (systemd/supervisor)
- Check service status
- Review startup logs

---

## Updating Your Bot

### On Cloud Platforms (Render/Railway)
1. Push changes to GitHub
2. Platform auto-deploys new version

### On VPS
```bash
cd /opt/bots/Anachak-Kasekor-Chatbot
git pull origin main
pip install -r requirements.txt --upgrade
supervisorctl restart anachak-bot
```

---

## Security Best Practices

1. **Never commit .env file** - Already in .gitignore ✅
2. **Use environment variables** - For sensitive data
3. **Keep dependencies updated** - `pip install --upgrade`
4. **Enable firewall** - On VPS
5. **Use SSH keys** - Instead of passwords
6. **Regular backups** - Of your configuration

---

## Need Help?

- Check logs first
- Search GitHub issues
- Ask in community
- Contact Anachak Cyb3r Team

---

**Recommended:** Start with Render.com (free) for testing, then move to VPS for production! 🚀

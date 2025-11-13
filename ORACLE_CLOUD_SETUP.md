# 🌟 Oracle Cloud FREE Setup Guide (24/7 Forever)

This guide will help you run your bot 24/7 on Oracle Cloud's FREE tier.

## Why Oracle Cloud?
- ✅ **100% FREE Forever** (not a trial)
- ✅ 4 ARM CPUs + 24GB RAM
- ✅ Runs 24/7 even when your laptop is off
- ✅ Professional server
- ✅ No time limits

---

## Step 1: Create Oracle Cloud Account

1. Go to: https://www.oracle.com/cloud/free/
2. Click **"Start for free"**
3. Fill in your details:
   - Email address
   - Country
   - Name
4. Verify your email
5. Add payment method (for verification only - **you won't be charged**)
6. Complete registration

---

## Step 2: Create a Virtual Machine

### 2.1 Access the Console
1. Log in to Oracle Cloud
2. Click **"Create a VM instance"**

### 2.2 Configure Your VM
- **Name:** `anachak-kasekor-bot`
- **Compartment:** Keep default
- **Placement:** Keep default
- **Image:** Ubuntu 22.04 (Minimal)
- **Shape:** 
  - Click "Change Shape"
  - Select **"Ampere"** (ARM-based)
  - Choose **VM.Standard.A1.Flex**
  - Set: 2 OCPUs, 12 GB RAM (or use all 4 OCPUs, 24GB - it's FREE!)

### 2.3 Networking
- Keep default VCN settings
- **Assign a public IPv4 address:** ✅ YES

### 2.4 SSH Keys
- **Generate SSH key pair:** Click this
- **Download private key** - SAVE THIS FILE! (e.g., `ssh-key.key`)
- **Download public key** (optional)

### 2.5 Create
- Click **"Create"**
- Wait 2-3 minutes for provisioning

### 2.6 Note Your IP Address
- Once created, copy the **Public IP address** (e.g., `123.45.67.89`)

---

## Step 3: Connect to Your Server

### 3.1 On Linux/Mac:

Open terminal and run:

```bash
# Make the key file secure
chmod 400 ~/Downloads/ssh-key.key

# Connect to your server (replace with your IP)
ssh -i ~/Downloads/ssh-key.key ubuntu@YOUR_SERVER_IP
```

### 3.2 On Windows:

Use **PuTTY** or **Windows Terminal**:

```bash
ssh -i C:\Users\YourName\Downloads\ssh-key.key ubuntu@YOUR_SERVER_IP
```

---

## Step 4: Setup Your Bot (Automated)

Once connected to your server, run these commands:

```bash
# Download the setup script
wget https://raw.githubusercontent.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot/main/setup_oracle_server.sh

# Make it executable
chmod +x setup_oracle_server.sh

# Run the setup
./setup_oracle_server.sh
```

The script will:
1. Update the system
2. Install Python and dependencies
3. Clone your bot repository
4. Ask for your bot token
5. Set up automatic restart
6. Start your bot

**When prompted, enter your bot token:**
```
8394979757:AAFeQw7sLYF4wUvjjwzB_6taQ39Ube4jSOY
```

---

## Step 5: Verify Bot is Running

```bash
# Check bot status
sudo supervisorctl status anachak-bot

# View live logs
sudo tail -f /var/log/anachak-bot.out.log

# Should show: "🤖 Main Bot is running..."
```

---

## Step 6: Open Firewall (If Needed)

If your bot needs to receive webhooks (it doesn't for polling mode), open ports:

```bash
# Allow HTTP/HTTPS
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

---

## Managing Your Bot

### Check Status
```bash
sudo supervisorctl status anachak-bot
```

### View Logs
```bash
# Live logs
sudo tail -f /var/log/anachak-bot.out.log

# Error logs
sudo tail -f /var/log/anachak-bot.err.log
```

### Restart Bot
```bash
sudo supervisorctl restart anachak-bot
```

### Stop Bot
```bash
sudo supervisorctl stop anachak-bot
```

### Start Bot
```bash
sudo supervisorctl start anachak-bot
```

### Update Bot Code
```bash
cd /opt/bots/Anachak-Kasekor-Chatbot
sudo git pull origin main
sudo supervisorctl restart anachak-bot
```

---

## Troubleshooting

### Bot Not Starting?

Check logs:
```bash
sudo tail -50 /var/log/anachak-bot.err.log
```

### Connection Refused?

Check if SSH port is open in Oracle Cloud:
1. Go to Oracle Cloud Console
2. Navigate to your VM instance
3. Click on the subnet
4. Click on the Security List
5. Add Ingress Rule:
   - Source: 0.0.0.0/0
   - Destination Port: 22
   - Protocol: TCP

### Need to Change Bot Token?

```bash
sudo nano /opt/bots/Anachak-Kasekor-Chatbot/.env
# Edit the token
# Save: Ctrl+X, Y, Enter

sudo supervisorctl restart anachak-bot
```

---

## Cost Breakdown

| Resource | Cost |
|----------|------|
| VM (4 CPUs, 24GB RAM) | **FREE** |
| Storage (200GB) | **FREE** |
| Network Transfer (10TB) | **FREE** |
| Public IP | **FREE** |
| **Total** | **$0.00/month** |

**Forever!** No time limits, no trials. Oracle Cloud's Always Free tier is truly free.

---

## Benefits

✅ Your bot runs 24/7  
✅ Works even when your laptop is off  
✅ Professional server infrastructure  
✅ Automatic restart if it crashes  
✅ Free forever  
✅ Fast and reliable  

---

## Alternative: Quick Manual Setup

If the script doesn't work, here's the manual way:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install requirements
sudo apt install python3 python3-pip python3-venv git supervisor -y

# Clone repo
cd /opt
sudo git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git
cd Anachak-Kasekor-Chatbot

# Setup Python
sudo python3 -m venv .venv
sudo .venv/bin/pip install -r requirements.txt

# Create .env
sudo nano .env
# Add: MAIN_BOT_TOKEN=your_token_here
# Save: Ctrl+X, Y, Enter

# Create supervisor config
sudo nano /etc/supervisor/conf.d/anachak-bot.conf
```

Paste this:
```ini
[program:anachak-bot]
directory=/opt/Anachak-Kasekor-Chatbot
command=/opt/Anachak-Kasekor-Chatbot/.venv/bin/python main_bot.py
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/anachak-bot.err.log
stdout_logfile=/var/log/anachak-bot.out.log
```

Start it:
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start anachak-bot
```

---

## Need Help?

- Check logs first: `sudo tail -f /var/log/anachak-bot.out.log`
- Verify bot token is correct
- Ensure internet connection is working: `ping google.com`
- Check supervisor status: `sudo supervisorctl status`

---

**Your bot will now run 24/7 forever, completely FREE!** 🎉

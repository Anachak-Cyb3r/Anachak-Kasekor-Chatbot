# 🚀 Quick Start: Run Your Bot 24/7

## 🎯 Goal
Run your Anachak Kasekor Bot 24/7 even when your laptop is turned off.

---

## ✅ EASIEST Option: Oracle Cloud (FREE Forever)

### What You Get:
- ✅ FREE server (4 CPUs, 24GB RAM)
- ✅ Runs 24/7 forever
- ✅ No credit card charges
- ✅ Professional hosting

### Quick Steps:

#### 1. Sign Up (5 minutes)
- Go to: https://www.oracle.com/cloud/free/
- Click "Start for free"
- Complete registration

#### 2. Create Server (3 minutes)
- Click "Create a VM instance"
- Name: `anachak-bot`
- Image: Ubuntu 22.04
- Shape: Ampere (ARM) - 2-4 CPUs
- Download SSH key
- Click "Create"
- **Copy the Public IP address**

#### 3. Connect to Server
```bash
# On your computer terminal
chmod 400 ~/Downloads/ssh-key.key
ssh -i ~/Downloads/ssh-key.key ubuntu@YOUR_SERVER_IP
```

#### 4. Run Setup Script (Automated - 5 minutes)
```bash
# On the server, run:
wget https://raw.githubusercontent.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot/main/setup_oracle_server.sh
chmod +x setup_oracle_server.sh
./setup_oracle_server.sh
```

When asked, enter your bot token:
```
8394979757:AAFeQw7sLYF4wUvjjwzB_6taQ39Ube4jSOY
```

#### 5. Done! ✅
Your bot is now running 24/7!

Check it:
```bash
sudo supervisorctl status anachak-bot
```

---

## 📊 Useful Commands

### Check if bot is running:
```bash
sudo supervisorctl status anachak-bot
```

### View live logs:
```bash
sudo tail -f /var/log/anachak-bot.out.log
```

### Restart bot:
```bash
sudo supervisorctl restart anachak-bot
```

### Update bot code:
```bash
cd /opt/bots/Anachak-Kasekor-Chatbot
sudo git pull origin main
sudo supervisorctl restart anachak-bot
```

---

## 🆘 Troubleshooting

### Bot not responding?
```bash
# Check logs
sudo tail -50 /var/log/anachak-bot.err.log

# Restart
sudo supervisorctl restart anachak-bot
```

### Can't connect to server?
- Check if you're using the correct IP address
- Make sure SSH key file has correct permissions: `chmod 400 ssh-key.key`
- Verify the key file path is correct

### Need to change bot token?
```bash
sudo nano /opt/bots/Anachak-Kasekor-Chatbot/.env
# Edit the token
# Save: Ctrl+X, then Y, then Enter
sudo supervisorctl restart anachak-bot
```

---

## 💰 Cost: $0.00/month (Forever!)

Oracle Cloud's Always Free tier includes:
- 4 ARM CPUs
- 24 GB RAM
- 200 GB storage
- 10 TB network transfer/month

**No time limits. No trials. Actually FREE forever!**

---

## 📚 Full Documentation

For detailed instructions, see:
- **ORACLE_CLOUD_SETUP.md** - Complete setup guide
- **docs/DEPLOYMENT.md** - All deployment options
- **docs/FREE_HOSTING.md** - Other free hosting options

---

## ✨ What Happens Now?

✅ Your bot runs 24/7  
✅ Auto-restarts if it crashes  
✅ Works even when your laptop is off  
✅ Professional server infrastructure  
✅ Completely FREE  

**Test it:** Send `/start` to your bot on Telegram!

---

**Need help?** Check the logs or open an issue on GitHub!

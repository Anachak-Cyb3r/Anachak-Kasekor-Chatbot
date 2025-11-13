#!/bin/bash
# Setup script for Oracle Cloud server
# Run this script on your Oracle Cloud VM

echo "🚀 Setting up Anachak Kasekor Bot on Oracle Cloud..."

# Update system
echo "📦 Updating system..."
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
echo "🐍 Installing Python..."
sudo apt install python3 python3-pip python3-venv git supervisor -y

# Create app directory
echo "📁 Creating app directory..."
sudo mkdir -p /opt/bots
cd /opt/bots

# Clone repository
echo "📥 Cloning repository..."
sudo git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git
cd Anachak-Kasekor-Chatbot

# Create virtual environment
echo "🔧 Setting up virtual environment..."
sudo python3 -m venv .venv
sudo .venv/bin/pip install -r requirements.txt

# Create .env file
echo "🔐 Creating .env file..."
echo "Please enter your bot token:"
read BOT_TOKEN

sudo tee .env > /dev/null <<EOF
MAIN_BOT_TOKEN=$BOT_TOKEN
SOIL_BOT_USERNAME=detect_soil_bot
RICE_SEED_BOT_USERNAME=detect_rice_seed_bot
RICE_DISEASE_BOT_USERNAME=detect_leaf_of_rice_bot
WEATHER_BOT_USERNAME=detect_weather_bot
MARKET_BOT_USERNAME=cambomarket_bot
CHATBOT_USERNAME=cambochatAI_bot
EOF

# Create supervisor config
echo "⚙️ Setting up supervisor..."
sudo tee /etc/supervisor/conf.d/anachak-bot.conf > /dev/null <<EOF
[program:anachak-bot]
directory=/opt/bots/Anachak-Kasekor-Chatbot
command=/opt/bots/Anachak-Kasekor-Chatbot/.venv/bin/python main_bot.py
user=root
autostart=true
autorestart=true
stderr_logfile=/var/log/anachak-bot.err.log
stdout_logfile=/var/log/anachak-bot.out.log
environment=PATH="/opt/bots/Anachak-Kasekor-Chatbot/.venv/bin"
EOF

# Start the bot
echo "🚀 Starting the bot..."
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start anachak-bot

echo "✅ Bot is now running 24/7!"
echo "📊 Check status: sudo supervisorctl status anachak-bot"
echo "📝 View logs: sudo tail -f /var/log/anachak-bot.out.log"

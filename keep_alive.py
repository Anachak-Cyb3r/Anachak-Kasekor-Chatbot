"""
Keep alive module for Replit hosting
This creates a simple web server that can be pinged by UptimeRobot
to keep the bot running 24/7 on Replit's free tier
"""

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "🤖 Anachak Kasekor Bot is running! ✅"

@app.route('/status')
def status():
    return {
        "status": "online",
        "bot": "Anachak Kasekor Chatbot",
        "message": "Bot is active and running"
    }

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    """Start the web server in a separate thread"""
    t = Thread(target=run)
    t.daemon = True
    t.start()

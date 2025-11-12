# Telegram Bot Hub

A main Telegram bot that acts as a hub to redirect users to specialized child bots.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create your bots on Telegram:**
   - Open Telegram and search for @BotFather
   - Create your main bot: `/newbot`
   - Create child bots (Soil Detection, Market, etc.)
   - Save all bot tokens

3. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Add your main bot token
   - Add your child bot usernames (without @)

4. **Run the bot:**
   ```bash
   python main_bot.py
   ```

## How It Works

- Users start the main bot with `/start`
- They see a menu with buttons for different services
- Clicking a button redirects them to the specialized child bot
- "More Options" shows additional bots

## Customization

Edit `main_bot.py` to:
- Add more child bots
- Change button text and emojis
- Modify welcome messages
- Add more menu levels

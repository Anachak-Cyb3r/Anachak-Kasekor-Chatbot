# 📦 Installation Guide

This guide will walk you through setting up the Anachak Kasekor Chatbot on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Telegram Account** - To create and test your bot

## Step 1: Create Your Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the prompts to:
   - Choose a name for your bot (e.g., "Anachak Kasekor")
   - Choose a username (must end in 'bot', e.g., "anachak_kasekor_bot")
4. **Save the bot token** - You'll need this later
5. (Optional) Set bot profile picture with `/setuserpic`
6. (Optional) Set bot description with `/setdescription`

## Step 2: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git

# Navigate to the project directory
cd Anachak-Kasekor-Chatbot
```

## Step 3: Set Up Virtual Environment

### On Linux/macOS:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### On Windows:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt when activated.

## Step 4: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt
```

This will install:
- `python-telegram-bot==22.5` - Telegram Bot API wrapper
- `httpx` - HTTP client for async requests
- Other dependencies

## Step 5: Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env
```

Edit the `.env` file with your favorite text editor:

```bash
# On Linux/macOS
nano .env

# On Windows
notepad .env
```

Add your bot token:
```env
MAIN_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# Optional: Customize child bot usernames
SOIL_BOT_USERNAME=detect_soil_bot
RICE_SEED_BOT_USERNAME=detect_rice_seed_bot
RICE_DISEASE_BOT_USERNAME=detect_leaf_of_rice_bot
WEATHER_BOT_USERNAME=detect_weather_bot
MARKET_BOT_USERNAME=cambomarket_bot
CHATBOT_USERNAME=cambochatAI_bot
```

**⚠️ Important:** Never commit your `.env` file to Git! It's already in `.gitignore`.

## Step 6: Verify Installation

Check if everything is set up correctly:

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Verify .env file exists
ls -la .env  # Linux/macOS
dir .env     # Windows
```

## Step 7: Run the Bot

```bash
python main_bot.py
```

You should see:
```
🤖 Main Bot is running...
```

## Step 8: Test Your Bot

1. Open Telegram
2. Search for your bot username
3. Send `/start` command
4. You should see the language selection menu

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'telegram'"
**Solution:** Make sure your virtual environment is activated and dependencies are installed:
```bash
source .venv/bin/activate  # Activate venv
pip install -r requirements.txt
```

### Issue: "telegram.error.InvalidToken"
**Solution:** Check your `.env` file and ensure the bot token is correct (no extra spaces).

### Issue: Bot doesn't respond
**Solution:** 
- Verify the bot is running (check terminal)
- Ensure you're messaging the correct bot
- Check your internet connection
- Verify the token is valid in BotFather

### Issue: "AttributeError" with Python 3.13
**Solution:** Ensure you have `python-telegram-bot==22.5` or higher:
```bash
pip install --upgrade python-telegram-bot
```

## Next Steps

- Read the [Usage Guide](USAGE.md) to learn about bot features
- Check [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute
- Join our community and share feedback

## Updating the Bot

To get the latest changes:

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart the bot
python main_bot.py
```

---

Need help? Open an issue on [GitHub](https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot/issues).

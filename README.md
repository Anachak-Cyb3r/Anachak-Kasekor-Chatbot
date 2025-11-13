# 🤖 Anachak Kasekor Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-22.5-blue.svg)
![License](https://img.shields.io/badge/License-Anachak%20Cyb3r-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**An AI-powered Telegram assistant empowering Cambodian farmers with smart agricultural solutions**

[Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing) • [Team](#-contributors)

</div>

---

## 🌾 Overview

**Anachak Kasekor Chatbot** is an intelligent Telegram bot developed by the **Anachak Cyb3r Team** to revolutionize farming in Cambodia. Our mission is to provide farmers with accessible AI-powered tools that help them make informed decisions, increase crop yields, and solve agricultural challenges efficiently.

This bot serves as a central hub connecting farmers to specialized AI services including soil analysis, disease detection, weather forecasting, and agricultural marketplace access.

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| 🧪 **Soil Type Detection** | Analyzes soil composition and recommends suitable crops for optimal growth |
| 🌾 **Rice Seed Analysis** | Identifies rice seed varieties and quality assessment |
| 🦠 **Disease Detection** | Detects rice plant diseases early and provides treatment recommendations |
| 🌤️ **Weather Forecasting** | Real-time weather updates to help farmers plan their activities |
| 🛒 **Marketplace** | Platform for farmers to buy, sell, and promote agricultural products |
| 💬 **AI Agricultural Advisor** | 24/7 chatbot answering farming-related questions |

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot.git
   cd Anachak-Kasekor-Chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your bot token:
   ```env
   MAIN_BOT_TOKEN=your_telegram_bot_token_here
   ```

5. **Run the bot**
   ```bash
   python main_bot.py
   ```

---

## 📖 Usage

### Starting the Bot

1. Open Telegram and search for your bot
2. Send `/start` command
3. Select your preferred language (Khmer 🇰🇭 or English 🇬🇧)
4. Choose from the available services

### Available Commands

- `/start` - Initialize the bot and display main menu

### Bot Architecture

```
Main Bot (Hub)
    ├── Soil Detection Bot
    ├── Rice Seed Detection Bot
    ├── Rice Disease Detection Bot
    ├── Weather Forecasting Bot
    ├── Marketplace Bot
    └── AI Chatbot Advisor
```

---

## 🛠️ Technology Stack

- **Language:** Python 3.13
- **Framework:** python-telegram-bot 22.5
- **API:** Telegram Bot API
- **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
Anachak-Kasekor-Chatbot/
├── main_bot.py              # Main bot application
├── compress_image.py        # Image compression utility
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── img/                    # Image assets
    ├── intro.png
    └── intro_compressed.jpg
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Test your changes before submitting
- Update documentation as needed

---

## 🧠 Our Mission

To make farming **smarter, easier, and more sustainable** by combining **AI and agriculture** — building a better future for Cambodian farmers through accessible technology and innovation.

---

## 👨‍💻 Contributors

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/identicons/1.png" width="100px;" alt=""/>
      <br />
      <sub><b>Pring Rady</b></sub>
    </td>
    <td align="center">
      <img src="https://github.com/identicons/2.png" width="100px;" alt=""/>
      <br />
      <sub><b>Morn Chanthoung</b></sub>
    </td>
    <td align="center">
      <img src="https://github.com/identicons/3.png" width="100px;" alt=""/>
      <br />
      <sub><b>Mi Lyheng</b></sub>
    </td>
  </tr>
</table>

---

## 📞 Support

For support, questions, or feedback:
- Open an issue on GitHub
- Contact the Anachak Cyb3r Team

---

## 📜 License

This project is licensed under **Anachak Cyb3r**.  
All rights reserved © 2025.

---

## 🙏 Acknowledgments

- Thanks to all farmers who inspired this project
- Telegram Bot API for providing the platform
- The open-source community for their invaluable tools

---

<div align="center">

**Made with ❤️ by Anachak Cyb3r Team**

⭐ Star this repository if you find it helpful!

</div>

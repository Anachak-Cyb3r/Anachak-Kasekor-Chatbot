import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Bot tokens - replace with your actual tokens
MAIN_BOT_TOKEN = os.getenv('MAIN_BOT_TOKEN')

# Child bot usernames (without @)
SOIL_DETECTION_BOT = os.getenv('SOIL_BOT_USERNAME', 'detect_soil_bot')
RICE_SEED_BOT = os.getenv('RICE_SEED_BOT_USERNAME', 'detect_rice_seed_bot')
RICE_DISEASE_BOT = os.getenv('RICE_DISEASE_BOT_USERNAME', 'detect_leaf_of_rice_bot')
WEATHER_BOT = os.getenv('WEATHER_BOT_USERNAME', 'detect_weather_bot')
MARKET_BOT = os.getenv('MARKET_BOT_USERNAME', 'cambomarket_bot')
CHATBOT = os.getenv('CHATBOT_USERNAME', 'cambochatAI_bot')

# Load image once at startup for better performance
INTRO_IMAGE = None
try:
    with open('img/intro_compressed.jpg', 'rb') as f:
        INTRO_IMAGE = f.read()
except Exception as e:
    print(f"Warning: Could not load intro image: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send language selection when /start is used"""
    
    # Create language selection keyboard
    keyboard = [
        [InlineKeyboardButton("🇰🇭 ភាសាខ្មែរ", callback_data='lang_khmer')],
        [InlineKeyboardButton("🇬🇧 English", callback_data='lang_english')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Please select your language / សូមជ្រើសរើសភាសា:",
        reply_markup=reply_markup
    )

async def show_main_menu(query, language, user_name="", is_first_time=False):
    """Show main menu based on selected language"""
    
    # Get current date
    today = datetime.now().strftime("%d/%m/%Y")
    
    if language == 'khmer':
        welcome_message = (
            f"🙏 ជំរាបសួរ {user_name}\n"
            f"🌾 ស្វាគមន៍មកកាន់ អាណាចក្រកសិករ\n"
            f"🤖 AI សម្រាប់ជួយដល់ប្រជាកសិករ\n"
            f"📅 ថ្ងៃនេះ {today}\n"
            f"📌 សូមជ្រើសរើសមុខងារដែលអ្នកចង់ប្រើ៖"
        )
        
        keyboard = [
            [InlineKeyboardButton("🌱 វិភាគប្រភេទដី", url=f"https://t.me/{SOIL_DETECTION_BOT}"),
             InlineKeyboardButton("🌾 វិភាគគ្រាប់ស្រូវ", url=f"https://t.me/{RICE_SEED_BOT}")],
            [InlineKeyboardButton("🦠 វិភាគជំងឺស្រូវ", url=f"https://t.me/{RICE_DISEASE_BOT}"),
             InlineKeyboardButton("🌤️ ព្យាករណ៍អាកាសធាតុ", url=f"https://t.me/{WEATHER_BOT}")],
            [InlineKeyboardButton("🛒 ទីផ្សារ", url=f"https://t.me/{MARKET_BOT}"),
             InlineKeyboardButton("💬 ទីប្រឹក្សាកសិកម្ម", url=f"https://t.me/{CHATBOT}")],
            [InlineKeyboardButton("🔙 ប្តូរភាសា", callback_data='change_language')]
        ]
    else:  # English
        welcome_message = (
            f"👋 Hello {user_name}\n"
            f"🌾 Welcome to Anachak Kasekor\n"
            f"🤖 AI for supporting farmers\n"
            f"📅 Today: {today}\n"
            f"📌 Please choose a feature:"
        )
        
        keyboard = [
            [InlineKeyboardButton("🌱 Soil Type Detection", url=f"https://t.me/{SOIL_DETECTION_BOT}"),
             InlineKeyboardButton("🌾 Rice Seed Detection", url=f"https://t.me/{RICE_SEED_BOT}")],
            [InlineKeyboardButton("🦠 Rice Disease Detection", url=f"https://t.me/{RICE_DISEASE_BOT}"),
             InlineKeyboardButton("🌤️ Weather Forecasting", url=f"https://t.me/{WEATHER_BOT}")],
            [InlineKeyboardButton("🛒 Marketplace", url=f"https://t.me/{MARKET_BOT}"),
             InlineKeyboardButton("💬 Chat Bot", url=f"https://t.me/{CHATBOT}")],
            [InlineKeyboardButton("🔙 Change Language", callback_data='change_language')]
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # If first time (from language selection text), send photo with media edit
    if is_first_time:
        if INTRO_IMAGE:
            try:
                # Edit message media to add photo (using cached image)
                media = InputMediaPhoto(media=INTRO_IMAGE, caption=welcome_message)
                await query.edit_message_media(
                    media=media,
                    reply_markup=reply_markup
                )
            except Exception as e:
                print(f"Error editing media: {e}")
                # Fallback to editing text only
                try:
                    await query.edit_message_text(
                        welcome_message,
                        reply_markup=reply_markup
                    )
                except Exception as e2:
                    print(f"Error editing text: {e2}")
        else:
            # No image available, use text only
            try:
                await query.edit_message_text(
                    welcome_message,
                    reply_markup=reply_markup
                )
            except Exception as e:
                print(f"Error editing text: {e}")
    else:
        # Coming from change language button, edit the photo caption
        try:
            await query.edit_message_caption(
                caption=welcome_message,
                reply_markup=reply_markup
            )
        except Exception as e:
            print(f"Error editing caption: {e}")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button clicks"""
    query = update.callback_query
    
    # Get user's full name
    user = query.from_user
    user_name = user.full_name if user.full_name else user.first_name
    
    # Answer callback with cool animation text
    if query.data.startswith('lang_'):
        await query.answer("✨ Loading...", show_alert=False)
    elif query.data == 'change_language':
        await query.answer("🔄 Switching...", show_alert=False)
    else:
        await query.answer()
    
    # Language selection
    if query.data == 'lang_khmer':
        context.user_data['language'] = 'khmer'
        # Check if coming from change_language (has photo) or first time (text only)
        is_first_time = not query.message.photo
        await show_main_menu(query, 'khmer', user_name, is_first_time)
    
    elif query.data == 'lang_english':
        context.user_data['language'] = 'english'
        # Check if coming from change_language (has photo) or first time (text only)
        is_first_time = not query.message.photo
        await show_main_menu(query, 'english', user_name, is_first_time)
    
    # More options - Khmer
    elif query.data == 'more_options_khmer':
        keyboard = [
            [InlineKeyboardButton("📊 ការវិភាគ", url="https://t.me/your_analytics_bot")],
            [InlineKeyboardButton("💬 ជំនួយ", url="https://t.me/your_support_bot")],
            [InlineKeyboardButton("⬅️ ត្រឡប់ទៅម៉ឺនុយ", callback_data='back_to_menu_khmer')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "⚙️ ជម្រើសបន្ថែម:\n\nសូមជ្រើសរើសសេវាកម្ម:",
            reply_markup=reply_markup
        )
    
    # More options - English
    elif query.data == 'more_options_english':
        keyboard = [
            [InlineKeyboardButton("📊 Analytics Bot", url="https://t.me/your_analytics_bot")],
            [InlineKeyboardButton("💬 Support Bot", url="https://t.me/your_support_bot")],
            [InlineKeyboardButton("⬅️ Back to Main Menu", callback_data='back_to_menu_english')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "⚙️ More Options:\n\nSelect a service:",
            reply_markup=reply_markup
        )
    
    # Back to menu - Khmer
    elif query.data == 'back_to_menu_khmer':
        await show_main_menu(query, 'khmer', user_name, False)
    
    # Back to menu - English
    elif query.data == 'back_to_menu_english':
        await show_main_menu(query, 'english', user_name, False)
    
    # Change language - show language selection without deleting
    elif query.data == 'change_language':
        keyboard = [
            [InlineKeyboardButton("🇰🇭 ភាសាខ្មែរ", callback_data='lang_khmer')],
            [InlineKeyboardButton("🇬🇧 English", callback_data='lang_english')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Edit the caption to show language selection
        try:
            await query.edit_message_caption(
                caption="Please select your language / សូមជ្រើសរើសភាសា:",
                reply_markup=reply_markup
            )
        except Exception:
            # If editing caption fails, delete and send new message
            await query.message.delete()
            await query.message.reply_text(
                "Please select your language / សូមជ្រើសរើសភាសា:",
                reply_markup=reply_markup
            )

def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(MAIN_BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Start the bot
    print("🤖 Main Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

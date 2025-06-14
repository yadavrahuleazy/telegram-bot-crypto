from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

# ====== CONFIGURATION ======
TOKEN = '7988749647:AAGHOYfMTdza4Pj1_emDEhb8LX1IGKwtagU'
WEBHOOK_URL = 'https://telegram-bot-crypto.onrender.com/'  # 👈 Replace with your actual Render URL
CHANNEL_USERNAME = '@waytomillionaire32'  # 👈 Your Telegram channel
# ===========================

# Initialize Flask app
app = Flask(__name__)

# Initialize Bot
bot = Bot(token=TOKEN)

# Set up Dispatcher
dp = Dispatcher(bot=bot, update_queue=None, workers=4, use_context=True)

# ======= Command Handlers ========
def start(update, context):
    update.message.reply_text("🚀 Bot is working perfectly!")

def help_command(update, context):
    update.message.reply_text("🤖 Available commands:\n/start - Start the bot\n/help - Help info")

def handle_message(update, context):
    user_message = update.message.text
    update.message.reply_text(f"👋 You said: {user_message}")
# =================================

# Register handlers
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# === Webhook Route ===
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "ok"

# === Health Check Route ===
@app.route('/')
def index():
    return "Bot is live ✅"

# === Set webhook when app starts ===
@app.before_first_request
def setup_webhook():
    bot.delete_webhook()
    bot.set_webhook(url=WEBHOOK_URL + TOKEN)

# === Main ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))

from flask import Flask, request
import telegram
from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# === Configuration ===
TOKEN = '7988749647:AAGHOYfMTdza4Pj1_emDEhb8LX1IGKwtagU'  # 🔐 Replace with your bot token
URL = 'https://telegram-bot-crypto.onrender.com/'          # 🌐 Replace with your Render service URL
CHANNEL = '@waytomillionaire32'                            # 📢 Replace with your Telegram channel

# === Initialize App & Bot ===
app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)

# === Commands ===
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="🚀 Bot is working perfectly!")

def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="🤖 Available commands:\n/start - Start the bot\n/help - List commands")

def handle_message(update, context):
    user_message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"👋 You said: {user_message}")

# === Set Webhook ===
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook(f"{URL}{TOKEN}")
    return "Webhook set!" if s else "Webhook setup failed."

# === Main Webhook Route ===
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dp = Dispatcher(bot, None, workers=0, use_context=True)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    dp.process_update(update)
    return 'ok'

# === Root Route ===
@app.route('/')
def home():
    return '🤖 Crypto Bot is running!'

# === Run App (Only for local testing, not used in Render) ===
if __name__ == "__main__":
    app.run(debug=False)

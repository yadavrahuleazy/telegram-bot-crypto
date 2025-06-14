from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

# === Configuration ===
TOKEN = '7988749647:AAGHOYfMTdza4Pj1_emDEhb8LX1IGKwtagU'  # ✅ Your Bot Token
URL = 'https://telegram-bot-crypto.onrender.com/'         # ✅ Your Render Service URL
CHANNEL = '@waytomillionaire32'                            # ✅ Your Telegram Channel

# === Initialize App & Bot ===
app = Flask(__name__)
bot = Bot(token=TOKEN)

# === Commands ===
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🚀 Bot is working perfectly!")

def help_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
        text="🧾 Available commands:\n/start - Start the bot\n/help - List commands")

def handle_message(update, context):
    user_message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"👋 You said: {user_message}")

# === Set Webhook ===
@app.route(f"/setwebhook", methods=["GET", "POST"])
def set_webhook():
    success = bot.set_webhook(f"{URL}{TOKEN}")
    return "Webhook set!" if success else "Webhook setup failed."

# === Main Webhook Route ===
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp = Dispatcher(bot, None, workers=0, use_context=True)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    dp.process_update(update)
    return 'ok'

# === Root Route for health check ===
@app.route('/')
def home():
    return '✅ Crypto Bot is running on Render!'

# === Only for local testing ===
if __name__ == '__main__':
    app.run(debug=False)

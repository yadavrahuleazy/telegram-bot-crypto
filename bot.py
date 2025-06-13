import telebot
import os
from flask import Flask, request

# Bot token environment variable se le rahe hain
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Bot instance create
bot = telebot.TeleBot(BOT_TOKEN)

# Flask app banaya
app = Flask(__name__)

# Start command handle karna
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Bot is live and working 24x7 on Render!")

# Telegram ka webhook data handle karna
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# Root route check
@app.route("/", methods=["GET"])
def home():
    return "🔥 Crypto Bot is deployed and running!", 200

# Bot polling (Render ke liye optional hai — webhook zyada preferred)
if __name__ == "__main__":
    print("✅ Bot is running 24x7 via webhook...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


import os
from telegram.ext import Application, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

async def start(update, context):
    await update.message.reply_text("🚀 Bot is live and working 24x7!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot is running 24x7...")
    app.run_polling()

if __name__ == "__main__":
    main()

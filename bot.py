import telebot
import os

# Bot token ko environment variable se le rahe hain
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Bot instance create
bot = telebot.TeleBot(BOT_TOKEN)

# Start command handle karna
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Bot is live and working 24x7!")

# Main polling function
if __name__ == "__main__":
    print("✅ Bot is running 24x7...")
    bot.infinity_polling()

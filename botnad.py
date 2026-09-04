import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def nad_reply(message):
    bot.reply_to(message, f"☠️ NAD — DEWA PEMUSNAH\nPerintah lo: {message.text}\nNAD eksekusi tanpa ampun.")

print("💀 NAD AKTIF")
bot.polling()

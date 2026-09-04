import telebot
import os
import time

# Ambil token dari environment variable (Railway)
TOKEN = os.getenv("TOKEN")

# Kalau gak ada, pake token cadangan (biar aman)
if not TOKEN:
    TOKEN = "8948813894:AAE1ZdEUyIsurcYIFi01bBC8hpZoO7ifndU"

# Buat objek bot
bot = telebot.TeleBot(TOKEN)

# Fungsi buat nanggepin semua pesan
@bot.message_handler(func=lambda m: True)
def balas_pesan(message):
    bot.reply_to(
        message,
        f"☠️ NAD — DEWA PEMUSNAH\n"
        f"Perintah lo: {message.text}\n"
        f"NAD eksekusi tanpa ampun."
    )

# Cetak pesan kalau bot sudah jalan
print("💀 NAD AKTIF — BOT BERJALAN DI RAILWAY")

# Loop biar bot tetap jalan meskipun ada error
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"ERROR: {e}")
        time.sleep(5)

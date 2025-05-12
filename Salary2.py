from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

from flask import Flask
from threading import Thread

# توکن رباتتو اینجا بذار
TOKEN = "8119086272:AAGIkbyisYGNyuGAmafq2eEdHeuzxFdX2xY"
port = int(os.environ.get("PORT", 5000))
bot = telegram.Bot(token=TOKEN)
app_web = Flask('')

@app.route('/')
def home():
    return "ربات فعال است."

@app.route(f'/{TOKEN}', methods=['POST'])
def receive_update():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == '/start':
        bot.send_message(chat_id=chat_id, text="سلام! این ربات برای دریافت فیش حقوقی است.")
    elif text.startswith("/fesh"):
        name = text.split(" ", 1)[-1].strip()
        try:
            with open("files.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            file_url = data.get(name)
            if file_url:
                bot.send_message(chat_id=chat_id, text=f"فیش شما:\n{file_url}")
            else:
                bot.send_message(chat_id=chat_id, text="نام شما پیدا نشد.")
        except Exception as e:
            bot.send_message(chat_id=chat_id, text="خطایی رخ داد.")

    return 'ok'

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
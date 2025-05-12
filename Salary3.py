import os
import json
import telegram
from flask import Flask, request
from threading import Thread

# توکن ربات
TOKEN = "8119086272:AAGIkbyisYGNyuGAmafq2eEdHeuzxFdX2xY"

# ساخت نمونه بات
bot = telegram.Bot(token=TOKEN)

# ساخت اپ Flask
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "ربات فعال است."

@app_web.route(f'/{TOKEN}', methods=['POST'])
def receive_update():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="سلام! برای دریافت فیش حقوقی عبارت /fesh نام‌خود را بفرستید.")
    elif text.startswith("/fesh"):
        name = text.split(" ", 1)[-1].strip()
        try:
            with open("files.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            file_url = data.get(name)
            if file_url:
                bot.send_message(chat_id=chat_id, text=f"📄 فیش حقوقی شما:\n{file_url}")
            else:
                bot.send_message(chat_id=chat_id, text="❌ نام شما پیدا نشد.")
        except Exception as e:
            bot.send_message(chat_id=chat_id, text="⚠️ خطایی رخ داد.")

    return 'ok'

# اجرای اپ Flask در Thread جداگانه
def run():
    port = int(os.environ.get("PORT", 5000))
    app_web.run(host='0.0.0.0', port=port)

Thread(target=run).start()

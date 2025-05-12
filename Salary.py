from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

from flask import Flask
from threading import Thread

port = int(os.environ.get("PORT", 5000))
app_web = Flask('')

@app_web.route('/')
def home():
    return "ربات فیش حقوقی فعاله."

def run():
    app_web.run(host='0.0.0.0', port=port)

Thread(target=run).start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات فیش حقوقی خوش اومدی.")

# توکن رباتتو اینجا بذار
TOKEN = "8119086272:AAGIkbyisYGNyuGAmafq2eEdHeuzxFdX2xY"

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
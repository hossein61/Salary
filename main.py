import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread

# فایل JSON فیش‌ها
with open("Salaries.json", "r") as f:
    SALARY_FILES = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! لطفاً کد پرسنلی‌تان را وارد کنید:")

async def handle_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()
    if code in SALARY_FILES:
        link = SALARY_FILES[code]
        await update.message.reply_text(f"اینم فیش حقوقی شما:\n{link}")
    else:
        await update.message.reply_text("کد پرسنلی معتبر نیست یا فیش شما هنوز بارگذاری نشده.")

app = ApplicationBuilder().token("8119086272:AAGIkbyisYGNyuGAmafq2eEdHeuzxFdX2xY").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code))

app_web = Flask('')

@app_web.route('/')
def home():
    return "ربات فیش حقوقی فعاله."

def run():
    app_web.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
app.run_polling()


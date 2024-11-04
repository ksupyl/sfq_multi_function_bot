import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я многофункциональный бот. Вот что я умею:\n"
        "/study - Учебные задачи\n"
        "/schedule - Расписание и напоминания\n"
        "/finance - Финансовый анализ\n"
        "/quiz - Викторина\n"
        "Выбери команду, чтобы начать!"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
    

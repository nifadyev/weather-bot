from telegram.ext import ApplicationBuilder, CommandHandler

from config import TELEGRAM_BOT_TOKEN
from handlers import hello, help, now, start


def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("now", now))

    application.run_polling()


main()

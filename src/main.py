import logging

from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler

from config import TELEGRAM_BOT_TOKEN
from handlers import button_tap, enable_daily, help, menu, now, start

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    # print(Settings(_env_file='.env').dict())
    # application = ApplicationBuilder().token(str(Settings.bot_token)).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("now", now))
    application.add_handler(CommandHandler("enable_daily", enable_daily))
    application.add_handler(CommandHandler("menu", menu))

    application.add_handler(CallbackQueryHandler(button_tap))

    application.run_polling()


if __name__ == "__main__":
    main()

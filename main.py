import threading
import telebot

from config import TOKEN
from handlers import register_handlers
from sheduler import run_scheduler


def main():
    bot = telebot.TeleBot(TOKEN)

    register_handlers(bot)

    scheduler_thread = threading.Thread(
        target=run_scheduler,
        args=(bot,),
        daemon=True
    )
    scheduler_thread.start()

    print("Бот запущен")

    bot.infinity_polling()


if __name__ == "__main__":
    main()
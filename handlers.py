from telebot import types
from config import CHAT_ID
from parser import get_random_article
from sheduler import get_next_post_time

def register_handlers(bot):

    def main_keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(" Получить статью")
        markup.add(" Опубликовать в канал")
        return markup


    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(
            message.chat.id,
            "Привет! \n\nВыбери действие:",
            reply_markup=main_keyboard()
        )


    @bot.message_handler(func=lambda m: m.text == " Получить статью")
    def article_private(message):
        article = get_random_article()

        if not article:
            bot.send_message(message.chat.id, "Ошибка получения статьи")
            return

        title, url, source = article

        text = (
            f"<b>{title}</b>\n\n"
            f"🔗 {url}\n\n"
            f"<i>Источник: {source}</i>"
        )

        bot.send_message(message.chat.id, text, parse_mode="HTML")


    @bot.message_handler(func=lambda m: m.text == " Опубликовать в канал")
    def article_channel(message):
        article = get_random_article()

        if not article:
            bot.send_message(message.chat.id, "Ошибка получения статьи")
            return

        title, url, source = article

        text = (
            f"<b>{title}</b>\n\n"
            f"🔗 {url}\n\n"
            f"<i>Источник: {source}</i>"
        )

        bot.send_message(CHAT_ID, text, parse_mode="HTML")
        bot.send_message(message.chat.id, "Опубликовано в канал ")

    @bot.message_handler(commands=["nextpost"])
    def next_post(message):
        next_time = get_next_post_time()
        bot.send_message(message.chat.id, f"Следующий пост: {next_time}")
import time
import json
from datetime import datetime, timedelta

from config import CHAT_ID, POST_TIMES, POST_INTERVAL_DAYS
from parser import get_random_article

STATE_FILE = "last_post.json"


def load_last_post_time():
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            return datetime.fromisoformat(data["last_post"])
    except Exception:
        return None


def save_last_post_time(dt):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_post": dt.isoformat()}, f)


def send_scheduled_article(bot):
    article = get_random_article()

    if not article:
        print("Нет статьи")
        return

    title, url, source = article

    text = (
        f"<b>{title}</b>\n\n"
        f"🔗 {url}\n\n"
        f"<i>Источник: {source}</i>"
    )

    bot.send_message(CHAT_ID, text, parse_mode="HTML")
    print("Статья отправлена")


def run_scheduler(bot):
    last_post_time = load_last_post_time()

    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time in POST_TIMES:

            if last_post_time is None or now - last_post_time >= timedelta(days=POST_INTERVAL_DAYS):
                send_scheduled_article(bot)
                last_post_time = now
                save_last_post_time(now)
                time.sleep(61)

        time.sleep(15)

def get_next_post_time():
    from datetime import datetime, timedelta
    from config import POST_INTERVAL_DAYS

    last_post_time = load_last_post_time()

    if not last_post_time:
        return "Скоро (нет истории постов)"

    next_time = last_post_time + timedelta(days=POST_INTERVAL_DAYS)

    return next_time.strftime("%Y-%m-%d %H:%M")
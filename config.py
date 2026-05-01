import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URLS = [
    "https://habr.com/ru/flows/information_security/articles/",
    "https://habr.com/ru/flows/backend/articles/",
    "https://habr.com/ru/flows/admin/articles/"
]

POST_TIMES = ["18:00"]
POST_INTERVAL_DAYS = 3
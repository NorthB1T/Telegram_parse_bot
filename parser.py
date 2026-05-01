import random
import requests
from bs4 import BeautifulSoup
from config import URLS


def get_habr_articles():
    articles = []

    for url in URLS:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for article in soup.find_all("article"):
                title_tag = article.find("h2")

                if title_tag:
                    link_tag = title_tag.find("a")

                    if not link_tag:
                        continue

                    title = title_tag.text.strip()
                    link = link_tag["href"]

                    if link.startswith("/"):
                        link = "https://habr.com" + link

                    articles.append((title, link, "Habr"))

        except requests.RequestException as error:
            print(f"Ошибка запроса: {error}")

    return articles


def get_random_article():
    articles = get_habr_articles()

    if not articles:
        return None

    return random.choice(articles)
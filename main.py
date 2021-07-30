import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/all/'
HOST = 'https://habr.com'
result = []


def get_html(url):
    r = requests.get(url)
    return r


def check_keywords(text):
    for word in KEYWORDS:
        if text.find(word) != -1:
            return True
    return False


soup = BeautifulSoup(get_html(URL).text, 'html.parser')
items = soup.find_all('a', class_='tm-article-snippet__title-link')

for i, item in enumerate(items):
    print(f"Обрабатываем {i + 1} статью из {len(items)}")
    article_url = item.get('href')
    article_soup = BeautifulSoup(get_html(HOST + article_url).text, 'html.parser')
    article_text = article_soup.find('div', id='post-content-body').find('div').get_text(strip=True)
    if check_keywords(article_text):
        title = article_soup.find('h1').find('span').get_text(strip=True)
        date = article_soup.find('span', 'tm-article-snippet__datetime-published').find('time').get_text(strip=True)
        result.append({
            'дата': date,
            'заголовок': title,
            'ссылка': HOST + article_url
        })

pprint(result)

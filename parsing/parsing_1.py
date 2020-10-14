import requests
from bs4 import BeautifulSoup
import csv

CSV = 'anime.csv'
HOST = "https://animekisa.tv"
URL = "https://animekisa.tv/latest/1"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listAnimes')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_='title-box-2').get_text(strip=True),
                'link_product': HOST + item.find('a', class_='an').get('href'),
                'time': item.find('div', class_='centerv2').get_text(strip=True),
                'image': HOST + item.find('div', class_='image-box').find('img').get('src')
            }
        )
    return anime

def save_animes(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Name of anime', 'Link of anime', 'next episode', 'Image of anime'])
        for item in items:
            writer.writerow([item['title'], item['link_product'], item['time'], item['image']])


def parser():
    PAGENATION = input('type amount of pages, please: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(1, PAGENATION):
            print(f'parsed pages: {page=}')
            html = get_html(URL, params={'page': page})
            anime.extend(get_content(html.text))
            save_animes(anime, CSV)
        print('parsing end')
    else:
        print('Error in parser, baby')

parser()
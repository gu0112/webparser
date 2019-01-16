import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webserver.settings")

import django
django.setup()
from data.models import WebData

def parse_web():
    url = 'http://www.koreaherald.com'
    req = requests.get(url)

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select(
        'dd > a'
    )

    data = {}
    for title in titles:
        data[title.text] =title.get('href')
    print(data[title.text])
    return data

if __name__ == '__main__':
    web_data_dict = parse_web()
    url ='http://www.koreaherald.com'

    for t, l in web_data_dict.items():
        WebData(title=t, link=url+l).save()


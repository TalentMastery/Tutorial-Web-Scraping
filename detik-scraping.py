import os
import requests
import json
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_articel = soup.find(attrs={'class', 'grid-row list-content'})
titles = populer_articel.findAll(attrs={'class': 'media__title'})
images = populer_articel.findAll(attrs={'class':'media__image'})

for title in titles:
    print(title.text)

for image in images:
    print(image.find('a').find('img')['title'])


# print(link_articel)

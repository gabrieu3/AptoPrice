import requests
import re
import json
import time
from bs4 import BeautifulSoup
from src.dto.ApDto import ApDto
from random import randrange

class ApOlx:
    url = ''
    pages = ''
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/53.0.2785.143 Safari/537.36'}

    def __init__(self):
        self.pages = 101

    # Search Html page
    def get_page_html(self, url):
        print('get_page_html: ' + url)

        time.sleep(randrange(1, 3))
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200:
            return r.text
        else:
            return ''

    # Get Links from Html
    def get_links(self, html):

        links = []
        soup = BeautifulSoup(html, 'html.parser')
        t = soup.find("ul", {"id": "main-ad-list"})

        for item in t.findAll('li', attrs={'class': 'item'}):
            link = item.find('a', attrs={'class': 'OLXad-list-link'})
            try:
                link = re.sub(r"\s+", " ", link.get('href')).strip()
            except Exception as e:
                link = ''

            if link != '':
                links.append(link)

        return links

    # Get data from page
    def get_data(self, html):
        ap = ApDto(html)
        soup = BeautifulSoup(html, 'html.parser')
        obj = soup.find("script", {"id": "initial-data"})

        try:
            obj = json.loads(obj["data-json"])
        except Exception as e:
            obj = ''
        try:
            ap.set_id(obj["ad"]["listId"])
            ap.set_title(obj["ad"]["subject"])
            ap.set_description(obj["ad"]["body"])
            ap.set_price(obj["ad"]["priceValue"])
            ap.set_old_price(obj["ad"]["oldPrice"])
            ap.set_category(obj["ad"]["categoryName"])
            ap.set_url(obj["ad"]["friendlyUrl"])
            ap.set_seller(obj["ad"]["user"]["name"])
            ap.set_phone(obj["ad"]["phone"]["phone"])
            ap.set_image(obj["ad"]["images"])
            ap.set_city(obj["ad"]["location"]["municipality"])
            ap.set_uf(obj["ad"]["location"]["uf"])
            ap.set_cep(obj["ad"]["location"]["zipcode"])
            ap.set_neighbourhood(obj["ad"]["location"]["neighbourhood"])
            ap.set_address(obj["ad"]["location"]["address"])
            ap.set_date_insert(obj["ad"]["listTime"])
        except Exception as error:
            print(error)
            print('Obj: ' + obj)
        return ap


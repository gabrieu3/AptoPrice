import requests
import re
import json
import time
from bs4 import BeautifulSoup
from src.dto.ApDto import ApDto

class ApOlx:
    url = ''
    pages = ''
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/53.0.2785.143 Safari/537.36'}

    def __init__(self):
        self.pages = 100

    # Search Html page
    def get_page_html(self, url):
        time.sleep(5)
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

        ap.id = obj["ad"]["listId"]
        ap.title = obj["ad"]["subject"]
        ap.description = obj["ad"]["body"]
        ap.price = obj["ad"]["priceValue"]
        ap.old_price = obj["ad"]["oldPrice"]
        ap.category =obj["ad"]["categoryName"]
        ap.url = obj["ad"]["friendlyUrl"]
        ap.seller = obj["ad"]["user"]["name"]
        ap.phone = obj["ad"]["phone"]["phone"]
        ap.image = obj["ad"]["images"]
        ap.city = obj["ad"]["location"]["municipality"]
        ap.uf = obj["ad"]["location"]["uf"]
        ap.cep = obj["ad"]["location"]["zipcode"]
        ap.neighbourhood = obj["ad"]["location"]["neighbourhood"]
        ap.address = obj["ad"]["location"]["address"]
        ap.dateInsert = obj["ad"]["listTime"]

        return ap


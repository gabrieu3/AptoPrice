import re
import json
from bs4 import BeautifulSoup
from src.dto.ApDto import ApDto
from src.scrap.ApScrap import ApScrap


class ApOlx:

    def __init__(self):
        self.web = ApScrap(1, 2)
        self.url = r'https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/' \
                   r'joinville/imoveis/venda/apartamentos?o='

    # Get Links from Html
    def get_structure(self, html):

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
            ap.set_site('OLX')
        except Exception as error:
            print(error)
            print('Obj: ' + obj)
        return ap

    def get_dto_ap(self, link):
        html = self.web.get_page_html(link)
        return self.get_data(html)

    # Get Results from OLX website
    def get_aptos_olx(self):
        for i in range(self.web.first_page, self.web.last_page):
            html = self.web.get_page_html(self.url + str(i))
            links = self.get_structure(html)
            aptos = []
            for link in links:
                ap = self.get_dto_ap(link)
                ap.set_page(i)
                aptos.append(ap)
        return aptos




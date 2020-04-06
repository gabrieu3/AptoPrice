from bs4 import BeautifulSoup
from src.dto.ApDto import ApDto
from src.scrap.ApScrap import ApScrap
from datetime import date
import re

class ApImovelSc:

    def __init__(self):
        self.log = 0
        self.web = ApScrap(1, 78)
        self.url_main = r'https://www.imoveis-sc.com.br'
        self.url = r'https://www.imoveis-sc.com.br/joinville/comprar/apartamento?page=2'

    # Get Links from Html
    def get_structure(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        page_aptos = soup.find("div", {"class": "cards-list"})
        links = []
        for apto in page_aptos.findAll("article", {"class": "bloco"}):
            try:
                link = apto.find("a", {"class":"bt-conheca"}).get("href")
                link = link.replace(r'/Im%C3%B3veis%20para%20compra/','')
                links.append(self.url_main + link)
            except Exception as e:
                print(e)
                links = []
        return links

    #Register on Terminal
    def __log__(self, info):
        if self.log == 1:
            print(info)

    # Get data from page
    def get_data(self, html):
        ap = ApDto(html)
        soup = BeautifulSoup(html, 'html.parser')
        caracteristica = soup.find("ul", {"class": "caracteristicas"})
        valor = soup.find("span", {"class": "valor-padrao"})

        descricao = soup.find("p", {"class": "chamada-imovel"})

        try:
            code = 0
            for li in caracteristica.findAll("li"):
                if 'Código' in li.text:
                    code = li.find("span").text
            ap.set_id(code)
            self.__log__(code)
        except Exception as error:
            ap.set_id('')
            print(error)
        try:
            title = soup.find("h2", {"class": "tit-imovel"}).text
            ap.set_title(title)
            self.__log__(title)
        except Exception as error:
            ap.set_title('')
            print(error)
        try:
            description = soup.find("p", {"class": "chamada-imovel"}).text
            ap.set_description(description)
            self.__log__(description)
        except Exception as error:
            ap.set_description('')
            print(error)
        try:
            price = soup.find("span", {"class": "valor-atual"})
            if price is not None:
                price = price.find("strong", {"class": "valor"}).text
            else:
                price = soup.find("span", {"class": "valor-padrao"})
                price = price.find("strong", {"class": "valor"}).text

            ap.set_price(price)
            self.__log__(price)
        except Exception as error:
            ap.set_price('')
            print(error)
        try:
            price_old = soup.find("span", {"class": "valor-de"})
            if price_old is None:
                price_old = price
            else:
                price_old = price_old.find("strong", {"class": "valor"}).text
            ap.set_old_price(price_old)
            self.__log__(price_old)
        except Exception as error:
            ap.set_old_price('')
            print(error)
        try:
            category = soup.find("div", {"class": "informations"})
            category = category.find("strong").text
            ap.set_category(category)
            self.__log__(category)
        except Exception as error:
            ap.set_category('')
            print(error)
        try:
            link = soup.find("link", {"rel": "canonical"})
            link = link["href"].strip()
            ap.set_url(link)
            self.__log__(link)
        except Exception as error:
            ap.set_url('')
            print(error)
        try:
            seller = 0
            for li in caracteristica.findAll("li"):
                if '47' in li.text:
                    seller = li.text
            self.__log__(seller)
            ap.set_seller(seller)
        except Exception as error:
            ap.set_seller('')
            print(error)
        try:
            cell = re.search('\(?\d{2}\)?\s?\d{4,5}\-\d{4}',seller)
            cell = cell.group(0)
            ap.set_phone(cell)
            self.__log__(cell)
        except Exception as error:
            ap.set_phone('')
            print(error)
        try:
            photos = []
            for a in soup.findAll("a",{"class":"fancybox"}):
                photos.append(a["href"])
            ap.set_image(photos)
            self.__log__(photos)
        except Exception as error:
            ap.set_image('')
            print(error)
        try:
            city = soup.find("div", {"class": "informations"})
            for x in city.findAll("strong"):
                city = x.text
            ap.set_city(city)
            self.__log__(city)
        except Exception as error:
            ap.set_city('')
            print(error)
        try:
            ap.set_uf('SC')
        except Exception as error:
            ap.set_uf('')
            print(error)
        try:
            ap.set_cep('')
        except Exception as error:
            ap.set_cep('')
            print(error)
        try:
            neighborhood = soup.find("strong", {"class": "header-imovel"})
            neighborhood = neighborhood.find("span").text
            neighborhood = neighborhood[0:neighborhood.find("|")].strip()
            ap.set_neighbourhood(neighborhood)
            self.__log__(neighborhood)
        except Exception as error:
            ap.set_neighbourhood('')
            print(error)
        try:
            address = soup.find("strong", {"class": "header-imovel"}).find("span").text
            ap.set_address(address)
            self.__log__(address)
        except Exception as error:
            ap.set_address('')
            print(error)
        try:
            date_insert = date.today()
            ap.set_date_insert(date_insert)
            self.__log__(date_insert)
        except Exception as error:
            ap.set_date_insert('')
            print(error)
        try:
            ap.set_site('IMOVELWEB')
        except Exception as error:
            ap.set_site('')
            print(error)

        return ap

    def get_dto_ap(self, link):
        html = self.web.get_page_html(link)
        return self.get_data(html)

    # Get Results from website
    def get_aptos(self):
        aptos = []
        for i in range(self.web.first_page, self.web.last_page):
            html = self.web.get_page_html(self.url + str(i))
            links = self.get_structure(html)
            for link in links:
                ap = self.get_dto_ap(link)
                ap.set_page(i)
                aptos.append(ap)
        return aptos
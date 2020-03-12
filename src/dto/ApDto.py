import datetime
import re
import pandas as pd


class ApDto:

    def __init__(self, html):
        self.id = 0
        self.page = 0
        self.html = html
        self.cod = 0
        self.title = ''
        self.detail = ''
        self.category = ''
        self.region = ''
        self.price = 0
        self.old_price = 0
        self.seller = ''
        self.phone = ''
        self.email = ''
        self.date_insert = datetime.datetime.now()
        self.url = ''
        self.cep = 0
        self.city = ''
        self.neighbourhood = ''
        self.address = ''
        self.location = ''
        self.description = ''
        self.image = ''
        self.uf = ''

    def get_id(self):
        return self.id

    def set_id(self, id):
        try:
            if pd.isnull(id):
                self.id = '1'
            else:
                self.id = id
        except Exception as error:
            print('ID : <' + id + '> Error: ' + error)

    def set_cod(self, cod):
        if pd.isnull(cod):
            self.cod = 1
        else:
            self.cod = cod

    def set_page(self, page):
        if pd.isnull(page):
            self.page = 9999
        else:
            self.page = page

    def set_title(self, title):
        if pd.isnull(title):
            self.title = ''
        else:
            self.title = title.upper().strip()

    def set_detail(self, detail):
        if pd.isnull(detail):
            self.detail = ''
        else:
            self.detail = detail.upper().strip()

    def set_description(self, description):
        if pd.isnull(description):
            self.description = ''
        else:
            self.description = description.upper().strip()

    def set_price(self, price):
        if pd.isnull(price):
            self.price = ''
        else:
            self.price = price.upper().strip()

    def set_old_price(self, old_price):
        if pd.isnull(old_price):
            self.old_price = ''
        else:
            self.old_price = old_price.upper().strip()

    def set_category(self, category):
        if pd.isnull(category):
            self.category = ''
        else:
            self.category = category.upper().strip()

    def set_url(self, url):
        if pd.isnull(url):
            self.url = ''
        else:
            self.url = url.lower().strip()

    def set_seller(self, seller):
        if pd.isnull(seller):
            self.seller = ''
        else:
            self.seller = seller.upper().strip()

    def set_phone(self, phone):
        if pd.isnull(phone):
            self.phone = ''
        else:
            self.phone = phone

    def set_image(self, image):
        image = str(image)
        if pd.isnull(image):
            self.image = ''
        else:
            self.image = image

    def set_city(self, city):
        if pd.isnull(city):
            self.city = ''
        else:
            self.city = city.upper().strip()

    def set_uf(self, uf):
        if pd.isnull(uf):
            self.uf = ''
        else:
            self.uf = uf.upper().strip()

    def set_neighbourhood(self, neighbourhood):
        if pd.isnull(neighbourhood):
            self.neighbourhood = ''
        else:
            self.neighbourhood = neighbourhood.upper().strip()

    def set_cep(self, cep):
        if pd.isnull(cep):
            self.cep = 0
        else:
            self.cep = cep

    def set_address(self, address):
        if pd.isnull(address):
            self.address = 0
        else:
            self.address = address.upper().strip()

    def set_date_insert(self, date_insert):
        if pd.isnull(date_insert):
            self.date_insert = ''
        else:
            self.date_insert = date_insert

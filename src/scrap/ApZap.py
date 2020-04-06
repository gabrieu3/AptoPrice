import json
from bs4 import BeautifulSoup
from src.dto.ApDto import ApDto
from src.scrap.ApScrap import ApScrap


class ApZap:

    def __init__(self):
        self.web = ApScrap(1, 2)
        self.url = r'https://www.zapimoveis.com.br/venda/apartamentos/sc+joinville/?pagina=$page$&onde=' \
                   r',Santa%20Catarina,Joinville,,,,BR%3ESanta%20Catarina%3ENULL%3EJoinville,-26.283421,-48.845226' \
                   r'&transacao=Venda&tipoUnidade=Residencial,Apartamento&tipo=Im%C3%B3vel%20usado'

    # Get Links from Html
    def get_structure(self, html):

        soup = BeautifulSoup(html, 'html.parser')
        dic = {}
        apto_list = []
        for script in soup.findAll("script"):
            if -1 != script.text.find('window.__INITIAL_STATE__'):
                try:
                    obj = script.text.replace('window.__INITIAL_STATE__=','')
                    obj = obj.replace(';(function(){var s;(s=document.currentScript||document.scripts[document.scripts.'
                                      'length-1]).parentNode.removeChild(s);}());','')
                    dic = json.loads(obj)
                    apto_list = dic["results"]["listings"]
                except Exception as e:
                    print(e)
                    dic = {}
                    apto_list = []
        return apto_list

    # Get data from page
    def get_data(self, data):
        ap = ApDto(data)

        try:
            ap.set_id(data["listing"]["id"])
        except Exception as error:
            ap.set_id('')
            print(error)
        try:
            ap.set_title(data["listing"]["title"])
        except Exception as error:
            ap.set_title('')
            print(error)
        try:
            ap.set_description(data["listing"]["description"])
        except Exception as error:
            ap.set_description('')
            print(error)
        try:
            ap.set_price(data["listing"]["pricingInfo"]["price"])
        except Exception as error:
            ap.set_price('')
            print(error)
        try:
            ap.set_old_price(data["listing"]["pricingInfo"]["salePrice"])
        except Exception as error:
            ap.set_old_price('')
            print(error)
        try:
            ap.set_category(data["listing"]["unitTypes"][0])
        except Exception as error:
            ap.set_category('')
            print(error)
        try:
            ap.set_url(data["link"]["href"])
        except Exception as error:
            ap.set_url('')
            print(error)
        try:
            ap.set_seller(data["account"]["name"])
        except Exception as error:
            ap.set_seller('')
            print(error)
        try:
            ap.set_phone(data["account"]["phones"]["primary"])
        except Exception as error:
            ap.set_phone('')
            print(error)
        try:
            ap.set_image(data["listing"]["images"])
        except Exception as error:
            ap.set_image('')
            print(error)
        try:
            ap.set_city(data["listing"]["address"]["city"])
        except Exception as error:
            ap.set_city('')
            print(error)
        try:
            ap.set_uf(data["listing"]["address"]["state"])
        except Exception as error:
            ap.set_uf('')
            print(error)
        try:
            ap.set_cep(data["listing"]["address"]["zipCode"])
        except Exception as error:
            ap.set_cep('')
            print(error)
        try:
            ap.set_neighbourhood(data["listing"]["address"]["neighborhood"])
        except Exception as error:
            ap.set_neighbourhood('')
            print(error)
        try:
            ap.set_address(data["listing"]["address"]["street"])
        except Exception as error:
            ap.set_address('')
            print(error)
        try:
            ap.set_date_insert(data["listing"]["createdAt"])
        except Exception as error:
            ap.set_date_insert('')
            print(error)
        try:
            ap.set_site('ZAP')
        except Exception as error:
            ap.set_site('')
            print(error)

        return ap

    # Get Results from OLX website
    def get_aptos_zap(self):
        aptos = []
        for i in range(self.web.first_page, self.web.last_page):
            html = self.web.get_page_html(self.url.replace('$page$', str(i)))
            data_structure = self.get_structure(html)
            for apto in data_structure:
                ap = self.get_data(apto)
                ap.set_page(i)
                aptos.append(ap)
        return aptos


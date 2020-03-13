from src.scrap.ApZap import ApZap
from src.dao.ApDao import ApDao
import pandas as pd


class ApDcoZap:
    url = r'https://www.zapimoveis.com.br/venda/apartamentos/sc+joinville/?pagina=$page$' \
          r'&onde=,Santa%20Catarina,Joinville,,,,BR%3ESanta%20Catarina%3ENULL%3EJoinville,-26.283421,-48.845226' \
          r'&transacao=Venda&tipoUnidade=Residencial,Apartamento&tipo=Im%C3%B3vel%20usado'

    def __init__(self):
        self.oconn = ApZap()
        self.dao = ApDao()

    # Get Results from OLX website
    def get_results(self):
        html = self.oconn.get_page_html(self.url.replace('$page$','1'))
        self.oconn.get_dictionary(html)



    def get_dto_ap(self, link):
        html = self.oconn.get_page_html(link)
        return self.oconn.get_data(html)

    # Write results into a DB Mysql
    def write_results_db(self, aptos):
        for ap in aptos:
            self.dao.save(ap)

    # Write results into a sheet
    def write_results(self, aptos):

        apto_id = []
        apto_title = []
        apto_price = []
        apto_old_price = []
        apto_url = []
        apto_seller = []
        apto_phone = []
        apto_city = []
        apto_neighbourhood = []
        apto_address = []
        apto_date_insert = []

        for ap in aptos:
            apto_id.append(ap.id)
            apto_title.append(ap.title)
            apto_price.append(ap.price)
            apto_old_price.append(ap.old_price)
            apto_url.append(ap.url)
            apto_seller.append(ap.seller)
            apto_phone.append(ap.phone)
            apto_city.append(ap.id)
            apto_neighbourhood.append(ap.neighbourhood)
            apto_address.append(ap.address)
            apto_date_insert.append(ap.date_insert)

        df = pd.DataFrame({'id': apto_id,
                           'title': apto_title,
                           'price': apto_price,
                           'old_price': apto_old_price,
                           'url': apto_url,
                           'seller': apto_seller,
                           'phone': apto_phone,
                           'city': apto_city,
                           'neighbourhood': apto_neighbourhood,
                           'address': apto_address,
                           'dateInsert': apto_date_insert})
        df.to_csv('aptos_olx.csv', index=False, encoding='utf-8')
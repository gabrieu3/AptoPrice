from src.scrap.ApOlx import ApOlx
import pandas as pd


class ApDco:
    url = r'https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/joinville/imoveis' \
          r'/venda/apartamentos?o='

    def __init__(self):
        self.oconn = ApOlx()
        self.aptos = []

    # Get Results from OLX website
    def get_results(self):
        html = self.oconn.get_page_html(self.url + '1')
        links = self.oconn.get_links(html)

        for link in links:
            html = self.oconn.get_page_html(link)
            self.aptos.append(self.oconn.get_data(html))

        return self.aptos

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
        apto_dateInsert = []

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
            apto_dateInsert.append(ap.dateInsert)

        df = pd.DataFrame({'id': apto_id,
                           'title': apto_title,
                           'price': apto_price,
                           'old_price': apto_old_price,
                           'url': apto_url
                           'seller': apto_seller,
                           'phone': apto_phone,
                           'city': apto_city,
                           'neighbourhood': apto_neighbourhood,
                           'address': apto_address,
                           'dateInsert': apto_dateInsert})
        df.to_csv('aptos_olx.csv', index=False, encoding='utf-8')
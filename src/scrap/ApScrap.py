from src.scrap.Scrap import Scrap


class ApScrap:

    def __init__(self, first, last):
        self.first_page = first
        self.last_page = last
        self.web = Scrap()

    def set_first_page(self, first):
        self.first_page = first

    def set_last_page(self, last):
        self.last_page = last

    def get_page_html(self, url):
        return self.web.get_page_html(url)



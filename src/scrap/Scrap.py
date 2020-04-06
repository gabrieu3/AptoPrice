import requests
import time
from random import randrange


class Scrap:

    def __init__(self):
        self.url = ''
        self.pages = ''
        self.headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    def get_page_html(self, url):
        print('get_page_html: ' + url)
        self.url = url

        #self.__time__()
        r = requests.get(url, headers=self.headers)

        if r.status_code == 200:
            return r.text
        else:
            return ''

    def __time__(self):
        time.sleep(randrange(1, 2))
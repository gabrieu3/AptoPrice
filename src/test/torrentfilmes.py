import pandas as pd
import requests  # urlopen
from bs4 import BeautifulSoup
import re
import time
from random import randrange

v_title = []
v_link = []
v_nota = []

for page in range(1, 100):

    time.sleep(randrange(1, 3))

    url = 'https://torrentfilmes.net/page/' + str(page)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    print('Getting Url: ' + url)
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        t = soup.find("div", {"class": "listagem"})

        for li in t.findAll('div', attrs={'class': 'item'}):

            a = li.find('a')

            nota = li.find('div', attrs={'class': 'nota'})

            try:
                title = a['title']
            except Exception as e:
                title = ''

            try:
                link  = a['href']
            except Exception as e:
                link = ''

            try:
                nota = re.sub(r"\s+", " ", nota.get_text()).strip()
            except Exception as e:
                nota = ''

            if title != '':
                v_title.append(title)
                v_link.append(link)
                v_nota.append(nota)

    else:
        print(r.status_code)


df = pd.DataFrame({'Title': v_title, 'Link': v_link, 'Nota': v_nota})
#df.to_csv('filmes_olx.csv', index=False, encoding='utf-8')



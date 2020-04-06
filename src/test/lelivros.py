import pandas as pd
import requests  # urlopen
from bs4 import BeautifulSoup
import re
import time
from random import randrange

v_title = []
v_link = []
v_nota = []

for page in range(450, 644):

    time.sleep(randrange(1, 3))

    url = 'http://lelivros.love/page/' + str(page)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    print('Getting Url: ' + url)
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        for li in soup.findAll('li', attrs={'class': 'post-17105 product type-product status-publish has-post-thumbnail hentry first instock'}):

            a = li.find('a')
            img = a.find('img')
            h3 = a.find('h3')
            try:
                title = h3.text
            except Exception as e:
                title = ''

            try:
                link  = a['href']
            except Exception as e:
                link = ''

            try:
                link_img = '=image("' + img['src'] + '",3)'
            except Exception as e:
                link_img = ''

            if title != '':
                v_title.append(title)
                v_link.append(link)
                v_nota.append(link_img)

    else:
        print(r.status_code)


df = pd.DataFrame({'Title': v_title, 'Link': v_link, 'Link img': v_nota})
#df.to_csv('livros4.csv', index=False, encoding='utf-8')



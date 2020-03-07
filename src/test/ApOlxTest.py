from src.scrap.ApOlx import ApOlx

a = ApOlx()

url = 'https://sc.olx.com.br/norte-de-santa-catarina/regiao-de-joinville-e-norte-do-estado/joinville/imoveis' \
      '/venda/apartamentos?o=1'
for l in a.get_links(a.get_page_html(url)):
    print(l)


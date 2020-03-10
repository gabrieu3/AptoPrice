from src.db.Db import Db

b = Db()

a = b.connect();
query = 'insert into apto(id, title, description, price, old_price, category, url, seller, phone, ' \
        'image, city, uf, cep, neighbourhood, address, date_insert) ' \
        'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
ee = 557087775
args = (
    ee, 'EXCELENTE APARTAMENTO NO JARDIM IRIRIÚ | 02 DORMITÓRIOS | PORCELANATO E LAMINADO', '', 'R$ 185.328', '',
    '',
    'https://sc.olx.com.br/norte-de-santa-catarina/imoveis/excelente-apartamento-no-jardim-iririu-02-dormitorios-porcelanato-e-laminado-557087774',
    'Salazar Imï¿³veis', '4738010547.0', '', '557087774', '', 0, 'Jardim Iririú', '0', '2020-03-07T22:07:46.000Z')
try:
    cursor = a.cursor()
    cursor.execute(query, args)

    a.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    a.close()

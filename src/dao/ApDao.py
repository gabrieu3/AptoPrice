from src.dto.ApDto import ApDto
from src.db.Db import Db


class ApDao:

    def __init__(self):
        self.c = Db()

    def insert(self, apto):
        query = 'insert into apto(id, title, description, price, old_price, category, url, seller, phone, ' \
                'image, city, uf, cep, neighbourhood, address, date_insert, page) ' \
                'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args = (str(apto.id),str(apto.title),str(apto.description),str(apto.price),str(apto.old_price),str(apto.category),
                str(apto.url),str(apto.seller),str(apto.phone),str(apto.image),str(apto.city),str(apto.uf),
                str(apto.cep),str(apto.neighbourhood),str(apto.address),str(apto.date_insert),int(apto.page))
        print('INSERT: ' + str(args))
        conn = self.c.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(query, args)
            conn.commit()
        except Exception as error:
            print(cursor.statement)
            print(error)
        finally:
            cursor.close()
            conn.close()

    def update(self, apto):
        query = 'update apto set title = %s, description= %s, price= %s, old_price= %s, category= %s, ' \
                'url= %s, seller= %s, phone= %s, image= %s, city= %s, uf= %s, cep= %s, neighbourhood= %s,' \
                'address= %s, date_insert= %s, page = %s ' \
                'where id = %s'

        args = (str(apto.title),str(apto.description),str(apto.price),str(apto.old_price),str(apto.category),
                str(apto.url),str(apto.seller),str(apto.phone),str(apto.image),str(apto.city),str(apto.uf),
                str(apto.cep),str(apto.neighbourhood),str(apto.address),str(apto.date_insert),int(apto.page),str(apto.id))
        print('UPDATE: '+ str(args))
        conn = self.c.connect()
        cursor = conn.cursor()

        try:
            cursor.execute(query, args)

            conn.commit()
        except Exception as error:
            print(cursor.statement)
            print(error)
        finally:
            cursor.close()
            conn.close()

    def exists(self, apto):
        query = r"select ifnull(max('S'),'N')  from apto where id = '" + str(apto.id) + "'"
        result = 'N'

        conn = self.c.connect()
        cursor = conn.cursor()

        try:

            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as error:
            print(cursor.statement)
            print(error)
        finally:
            cursor.close()
            conn.close()

        return result[0][0]

    def save(self, apto):
        if self.exists(apto) == 'S':
            self.update(apto)
        else:
            self.insert(apto)

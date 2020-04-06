import mysql.connector
from mysql.connector import Error

class Db:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'dev'
        self.passwd = 'dev12345;'
        self.database = 'aptos'
        self.mydb = ''

    def connect(self):
        try:
            self.mydb = mysql.connector.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        except Error as error:
            print(error)

        return self.mydb


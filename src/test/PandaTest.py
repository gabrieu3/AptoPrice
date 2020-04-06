import pandas as pd
from src.dto.ApDto import ApDto
from src.dao.ApDao import ApDao
from numpy import *


df = pd.read_csv('aptos_olx.csv')
dao = ApDao()

for i in range(len(df['id'])):

    a = ApDto('html')
    a.set_id(df["id"][i])
    a.set_title(df["title"][i])
    a.set_price(df["price"][i])
    a.set_old_price(df["old_price"][i])
    a.set_url(df["url"][i])
    a.set_seller(df["seller"][i])
    a.set_phone(df["phone"][i])
    a.set_cep(df["cep"][i])
    a.set_neighbourhood(df["neighbourhood"][i])
    a.set_address(df["address"][i])
    a.set_date_insert(df["dateInsert"][i])
    dao.save(a)


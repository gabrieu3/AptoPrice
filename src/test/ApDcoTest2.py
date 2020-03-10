from src.dco.ApDco import ApDco
from src.dao.ApDao import ApDao

link = 'https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamentos-com-otimo-padrao-no-espinheiros-715173014'
dco = ApDco()
dao = ApDao()

dto = dco.get_dto_ap(link)
dao.save(dto)




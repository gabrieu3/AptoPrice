from src.dco.ApDco import ApDco
from src.dao.ApDao import ApDao

link = 'https://sc.olx.com.br/norte-de-santa-catarina/imoveis/apartamento-a-venda-com-2-dormitorios-em-adhemar-garcia-joinville-cod-v15078-716944544'
dco = ApDco()
dao = ApDao()

dto = dco.get_dto_ap(link)
dao.save(dto)




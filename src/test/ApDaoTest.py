from src.dao.ApDao import ApDao
from src.dto.ApDto import ApDto

a = ApDao()

b = ApDto('html')
b.id = 1
b.title = 'Primeiro'
c = ApDto('html')
c.id = 2
c.title = 'Segundo'

a.save(b)

a.save(c)
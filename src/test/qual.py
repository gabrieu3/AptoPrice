# coding=utf8
import re
#print(texto)

#p = re.compile('(a-zA-Z)*(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})(a-zA-Z)*')
#p = re.compile('\(\d{2}\)?\d{4,5}\-\d{4}')
#p = re.compile('\d\d')
#teste = p.search('aaaaa 56 aaaaa')
seller = 'Anagê Centro - Vendas: 47 3025-3000'
cell = re.search('\(?\d{2}\)?\s?\d{4,5}\-\d{4}',seller)

print(cell.group(0))


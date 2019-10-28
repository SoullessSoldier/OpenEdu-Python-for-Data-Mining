"""
9.JSON и визуализация геоданных
9.1. Документация к публичным API
В некоторых ситуациях сайты/сервисы предоставляют удобный набор данных
Один из примеров - сайт Портал открытых данных правительства Москвы
https://data.mos.ru/
Документация API:
https://apidata.mos.ru/Docs
В ответах API будут JSON
api_key=c25290a0b5f170f69d45a28665b43168
login=rossum
pass=python370
"""
from urllib.request import urlopen
url="https://apidata.mos.ru/v1/datasets?api_key=c25290a0b5f170f69d45a28665b43168&$skip=1&$top=1&$inlinecount=allpages"
res=urlopen(url).read().decode('utf8')
print(res)
'''
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way (некоторой линии,
возможно замкнутой) и не иметь собственных тегов.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента карты посчитайте,
сколько всего тегов node не содержат в себе ни одного тега tag (первое число в ответе),
а сколько содержит хотя бы один тег tag (второе число в ответе). Числа введите через пробел.
'''
from bs4 import BeautifulSoup as BS
file=open('input8-2.osm','r',encoding='utf8')
xml=file.read()
soup=BS(xml,'lxml')
cnt=0

nodes={}
for node in soup.find_all('node'):
    cnt=0

    for tag in node('tag'):
        cnt+=1
    nodes[node['id']]=cnt

file.close()
cnt_0=0
cnt_1=0
for k,v in nodes.items():
    if v==0:
        cnt_0+=1
    else:
        cnt_1+=1
print(cnt_0,cnt_1)#24305 884
#Анализ геоданных OpenStreeMaps
#считатем количество супермаркетов на куске экспортированной карты

from bs4 import BeautifulSoup as BS

xml=open('map8-1.osm','r',encoding='utf8').read()
soup=BS(xml,'lxml')
cnt=0
#print(soup)
#Перебратиь все ноды
for node in soup.find_all('node'):
    for tag in node('tag'):#Ищем ноды с тегами
        #К тегу можно обратиться как к словарю
        if tag['k']=='shop' and tag['v']=='supermarket':
            cnt+=1
print(cnt)
#В следующей лекции посчитаем количество супермаркетов каждой сети


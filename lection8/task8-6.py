'''
В OpenStreetMap XML встречаются теги way, которые соответствуют некоторым линиям и многоугольникам на карте.
Way состоит из списка нодов (точек), которые задаются тегами nd вложенными в тег way.
Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm определите id того way,
который содержит в себе наибольшее количество нодов. Если таких несколько - выведите тот id,
который встречается в файле раньше.
'''
from bs4 import BeautifulSoup as BS
file=open('input8-2.osm','r',encoding='utf8')
xml=file.read()
soup=BS(xml,'lxml')
cnt=0
total_count=0
nodes=[]
for node in soup.find_all('way'):
    cnt=0
    total_count+=1
    for tag in node('nd'):
        cnt+=1
    nodes.append([node['id'],cnt,total_count])

file.close()
#print(nodes)
print(sorted(nodes,key=lambda x:(-x[1],x[2]))[0])
print(sorted(nodes,key=lambda x:(-x[1],x[2]))[0][0])#227140108
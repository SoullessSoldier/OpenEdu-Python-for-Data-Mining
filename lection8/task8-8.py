'''
Вася, открывший заправку в прошлой задаче, разорился.
Конкуренция оказалась слишком большой.
Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке,
но и на каком-то контуре.
Определите, сколько заправок на самом деле (не только обозначенных node, но и way) есть на
фрагменте карты https://stepik.org/media/attachments/lesson/245681/map2.osm
'''
from bs4 import BeautifulSoup as BS
response=open('map2.osm','r',encoding='utf8')
xml=response.read()
response.close()
soup=BS(xml,'lxml')
names={}
for node in soup.find_all(['node','way']):#Можно передавать список тегов для поиска!!!
    flag=False
    name=''
    for tag in node('tag'):
        #if tag['k']=='shop' and tag['v']=='supermarket':
        if tag['k']=='amenity' and tag['v']=='fuel':

            flag=True
        if tag['k']=='name':
            name=tag['v']
    if flag:
        if name not in names:
            names[name]=0
        names[name]+=1
#print(names)
supermarkets=list(names.items())
sum=0
for now in sorted(supermarkets,key=lambda x:(-x[1],x[0])):
    print(*now)
    sum+=now[1]
print(f"Total fuels: {sum}")#27
"""
Используя модуль xmltodict определите, сколько точек (node) имеют тег с ключом shop для участка карты.

Обратите внимание, что в зависимости от количества тегов tag внутри тега node представление информации для тегов
будет либо словарем, либо списком словарей. Чтобы проверить, что объект является списком, можно воспользоваться
функцией isinstance:

if isinstance(tag, list):
    print('list')
elif isinstance(tag, dict):
    print('dict')

Не забудьте также, что node может и вовсе не иметь тегов tag внутри себя.
"""
import xmltodict
fin=open('map10-2.osm','r',encoding='utf8')
xml=fin.read()
fin.close()
dct=xmltodict.parse(xml)
spisok=[]
nodes_all={}
for node in dct['osm']['node']:
   flag=False
   nodes_all[node['@id']]=(node['@lat'],node['@lon'])
   if 'tag' in node  and isinstance(node['tag'],list):#если есть ключ tag  в словаре, описывающем одну точку node
        # На одиночных точках значением будет словарь со значением из одной строки, нам нужны точки с целым списком тегов tag
        #flag=False
        shop_name=''
        for tag in node['tag']:
            if tag['@k']=="shop":
                shop_name=tag['@v']
                flag=True#нашли дом!
   """Из вредности, вдруг есть ноды-словари с одним лищь тегом tag"""
   if 'tag' in node and isinstance(node['tag'], dict):
       if node['tag']['@k'] == "shop":
           shop_name = node['tag']['@v']
           flag = True  # нашли дом!

   if flag:
#        print(f"{street}, {housenumber}; latitude: {node['@lat']}, longitude: {node['@lon']}")
        spisok.append([shop_name,node['@lat'],node['@lon']])



print(len(spisok))

for i in spisok:
    print(i)

"""
10.3
Используя модуль xmltodict определите, координаты точек (node) имеющие тег с ключом shop для участка карты.
Выведите координаты в формате, пригодном для вставки в пример leaflet для отображения в виде маркеров,
в том порядке, в котором точки встречаются в исходном файле.

Если вы все делаете правильно, то первые строки в вашем ответе должны быть такими:

L.marker([55.6027557, 37.4934168]).addTo(mymap);
L.marker([55.6034066, 37.4899744]).addTo(mymap);
L.marker([55.6043511, 37.4885361]).addTo(mymap);
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



#print(len(spisok))

for i in spisok:
    print(f"L.marker([{i[1]}, {i[2]}]).addTo(mymap);")

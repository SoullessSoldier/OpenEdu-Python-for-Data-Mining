"""
9.7 Преобразование XML в словарь

"""
import xmltodict
fin=open("big-nikitskaya-street.osm","r",encoding="utf-8")
dct=xmltodict.parse(fin.read())
"""
#Смотрим, какие ключи есть в словаре
print(dct.keys())#'osm'
print(dct['osm'].keys())#'@version', '@generator', '@copyright', '@attribution', '@license', 'bounds', 'node', 'way', 'relation'
print(dct['osm']['node'])#выведется обрезанный список
print(dct['osm']['node'][0])#каждый нод - словарь
"""
spisok=[]
nodes_all={}
for node in dct['osm']['node']:
    #print(node)
    #print(f"latitude: {node['@lat']}, longitude: {node['@lon']}")
    """
    Попробуем поискать адрес в текущем представлении
    У нод есть тег - элемент словаря с ключом tag и значением - списком словарей (@k, @v)
    """
    flag=False
    nodes_all[node['@id']]=(node['@lat'],node['@lon'])
    if 'tag' in node  and isinstance(node['tag'],list):#если есть ключ tag  в словаре, описывающем одну точку node
        # На одиночных точках значением будет словарь со значением из одной строки, нам нужны точки с целым списокм тегов tag
        #flag=False
        street=''
        housenumber=''
        for tag in node['tag']:
            if tag['@k']=="addr:street":
                street=tag['@v']
            if tag['@k']=="addr:housenumber":
                housenumber=tag['@v']
                flag=True#нашли дом!
    if flag:
#        print(f"{street}, {housenumber}; latitude: {node['@lat']}, longitude: {node['@lon']}")
        spisok.append([street,housenumber,node['@lat'],node['@lon']])
for way in dct['osm']['way']:#а теперь тоже самое для "замкнутых ломаных" way
    """
    Здесь засада! Даже если брать координату пути по первой точке, то сначала надо обойти файл и занести координаты всех точек
    в словарь! Иначе в явном виде для way координат нет!
    Это сделано заполнением словаря nodes_all при обходе нод
    """
    #print(way)
    flag = False
    if 'tag' in way and isinstance(way['tag'], list):

        street=''
        housenumber=''
        nd_id=''
        #for nd in way['nd']:
        nd_id=way['nd'][len(way['nd'])//2]['@ref']#Типа берем среднюю точку из списка идетификаторов nd, образующих ломаную
        for tag in way['tag']:
            #if tag['@k']=="building":
            if tag['@k'] == "addr:street":
                street = tag['@v']
            if tag['@k'] == "addr:housenumber":
                housenumber = tag['@v']
                flag = True  # нашли дом!
    if flag:
        #print(f"way {street}, {housenumber}; latitude: {nodes_all[nd_id][0]}, longitude: {nodes_all[nd_id][1]}")
        spisok.append([street, housenumber, nodes_all[nd_id][0], nodes_all[nd_id][1]])
for i in sorted(spisok):
    print(i)
"""
Впереди нанесение маркеров по координатам на карту
"""

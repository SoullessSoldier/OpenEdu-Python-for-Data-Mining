"""
Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и последний node),
 среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.

Для каждого подходящего под условия way выведите две строки.
В первой укажите одно число - id этого way.
Во второй выведите список кортежей, содержащих координаты (широту и долготу) всех node, входящих в этот way.
Для этого удобно в первой (И ВТОРОЙ???) задаче к предыдущему видео (task8-11,task8-12.py) сохранить все координаты в словарь,
где ключом является id нода,
и совместить ее с последней задачей к предыдущему видео (task8-13.py).

Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

Если вы все делаете правильно, то ваш ответ должен начинаться со строк

28889642
[(55.5652795, 37.5695507), (55.5651145, 37.5702288), (55.5648475, 37.5700314), (55.5650147, 37.5693509), (55.5652795, 37.5695507)]
28911067
[(55.5683532, 37.5644676), (55.5682987, 37.5644271), (55.5679549, 37.5641683), (55.5679974, 37.5639919), (55.5683976, 37.5642929), (55.5686577, 37.5632112), (55.5687302, 37.5632692), (55.5687094, 37.5633574), (55.5687319, 37.5633741), (55.5686567, 37.5636906), (55.5686342, 37.5636738), (55.5685984, 37.5638247), (55.5686198, 37.5638406), (55.5684996, 37.5643462), (55.5684605, 37.5643171), (55.5684327, 37.5644347), (55.5683718, 37.5643896), (55.5683532, 37.5644676)]
"""
from bs4 import BeautifulSoup as BS
"""
from urllib.request import urlopen
url='https://stepik.org/media/attachments/lesson/266078/mapcity.osm'
response = urlopen(url)
xml = response.read().decode('utf8')
"""

xml=open('mapcity.osm','r',encoding='utf8').read()
soup = BS(xml, 'lxml')

nodes = {}#нам понадобятся все ноды
for node in soup.find_all('node'):

        lat=float(node['lat'])
        lon=float(node['lon'])
        id=node['id']
        nodes[id]=(lat,lon)

for way in soup.find_all('way'):

    for tag in way('tag'):
        if tag['k'] == 'building':
            # нам надо узнать все id нодов, входящих в этот way
            rnodes = []  # список нодов
            for nd in way('nd'):
                ref = nd['ref']
                rnodes.append(ref)
            if rnodes[0]==rnodes[len(rnodes)-1]:
                print(way['id'])
                temp_list1=[]
                for rnode in rnodes:
                    temp_list1.append(nodes[rnode])
                #temp_tuple=tuple(temp_list1)
                print(temp_list1)
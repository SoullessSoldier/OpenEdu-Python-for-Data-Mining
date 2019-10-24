"""
Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и последний node),
среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.

Для каждого подходящего под условия way выведите две строки. В первой укажите одно число - id этого way.
Во второй перечислите через пробел id (ref) всех nd, входящих в этот way в том же порядке, в котором они перечисляются в файле.

Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

Если вы все делаете правильно, то ваш ответ должен начинаться со строк

28889642
317555544 317555545 317555546 317555547 317555544
28911067
317558736 529559432 317558559 317558560 317558561 317558562 317558290 529559420 529559416 529559414 529559412 529559410 529559426 529559424 529559422 317558289 317558288 317558736
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
for way in soup.find_all('way'):
    flag = False  # вдруг "дорога" - не хайвей
    for tag in way('tag'):
        if tag['k'] == 'building':
            # нам надо узнать все id нодов, входящих в этот way
            rnodes = []  # список нодов
            for nd in way('nd'):
                ref = nd['ref']
                rnodes.append(ref)
            if rnodes[0]==rnodes[len(rnodes)-1]:
                print(way['id'])
                print(*rnodes)
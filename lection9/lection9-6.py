"""
Сопоставление данных из разных источников
работаем с файлом html.html, получаем файл html9-6.html
уберем L.circle и L.polygon
отцентрируем карту с Лондона на Москву:
было var mymap = L.map('mapid').setView([51.505, -0.09], 13);
и L.marker([51.5, -0.09]).addTo(mymap)
меняем координаты на (55.746439, 37.624054)
***
пометим дома на Большой Никитской, где отключают воду
см. 9-5
мы знаем адрес дома, но нам нужны географические координаты
выгружаем нужный кусок карты с openstreetmap
https://www.openstreetmap.org/export#map=16/55.7576/37.5991
big-nikitskaya-street.osm
интересуют ноды:
<node id="1684243150" lat="55.7568223" lon="37.6018195">
  <tag k="addr:housenumber" v="19/13"/>
  <tag k="addr:street" v="Большая Никитская улица"/>
либо адрес приписан к ломаной
<way>
  <tag k="addr:housenumber" v="6"/>
  <tag k="addr:street" v="Большая Никитская улица"/>
  <tag k="building" v="yes"/>
Надо вспомнить обработку XML
Есть способ - библиотека xmltodict

"""
import xmltodict
fin=open("big-nikitskaya-street.osm","r",encoding="utf-8")
dct=xmltodict.parse(fin.read())
#Смотрим, какие ключи есть в словаре
print(dct.keys())#'osm'
print(dct['osm'].keys())#'@version', '@generator', '@copyright', '@attribution', '@license', 'bounds', 'node', 'way', 'relation'
print(dct['osm']['node'])#выведется обрезанный список
print(dct['osm']['node'][0])#каждый нод - словарь
#Иногда такое превращение в список словарей удобнее, чем BeautifulSoup
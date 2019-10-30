"""
9.8 Автоматическое добавление маркеров на карту
вспомним про файл html9-6.html
В нем в скрипте проставляем маркеры, пока руками
L.marker([55.7572499, 37.6043881]).addTo(mymap)
		.bindPopup("<b>Большая Никитская улица</b><br />16 с8.").openPopup();
Это работает. осталось научиться генерировать это питоном
можно пока даже без popup
"""
import xmltodict

start="""
<!DOCTYPE html>
<html>
<head>

	<title>Quick Start - Leaflet</title>

	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<link rel="shortcut icon" type="image/x-icon" href="docs/images/favicon.ico" />

    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js" integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og==" crossorigin=""></script>



</head>
<body>



<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
	var mymap = L.map('mapid').setView([55.746439, 37.624054], 13);
	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox.streets'
	}).addTo(mymap);
"""
end="""
var popup = L.popup();
	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent("You clicked the map at " + e.latlng.toString())
			.openOn(mymap);
	}
	mymap.on('click', onMapClick);
</script>
</body>
</html>
"""


fin=open("big-nikitskaya-street.osm","r",encoding="utf-8")
fout=open('map9-8.html','w',encoding='utf-8')
print(start,file=fout
      )
dct=xmltodict.parse(fin.read())
spisok=[]
nodes_all={}
for node in dct['osm']['node']:
    flag=False
    nodes_all[node['@id']]=(node['@lat'],node['@lon'])
    if 'tag' in node  and isinstance(node['tag'],list):
        street=''
        housenumber=''
        for tag in node['tag']:
            if tag['@k']=="addr:street":
                street=tag['@v']
            if tag['@k']=="addr:housenumber":
                housenumber=tag['@v']
                flag=True#нашли дом!
    if flag:
        spisok.append([street,housenumber,node['@lat'],node['@lon']])
for way in dct['osm']['way']:#а теперь тоже самое для "замкнутых ломаных" way
    flag = False
    if 'tag' in way and isinstance(way['tag'], list):

        street=''
        housenumber=''
        nd_id=''
        #for nd in way['nd']:
        nd_id=way['nd'][len(way['nd'])//2]['@ref']
        for tag in way['tag']:
            #if tag['@k']=="building":
            if tag['@k'] == "addr:street":
                street = tag['@v']
            if tag['@k'] == "addr:housenumber":
                housenumber = tag['@v']
                flag = True  # нашли дом!
    if flag:
        spisok.append([street, housenumber, nodes_all[nd_id][0], nodes_all[nd_id][1]])
#spisok=[street,housenumber,latitude,longitude]
for i in spisok:
    lat=i[2]
    lon=i[3]
    print(f"L.marker([{lat}, {lon}]).addTo(mymap)",file=fout)
print(end,file=fout)
fout.close()
#Получится весьма кучно )))
"""
Идеал - 9.5+9.8:
ввести улицу, получить дома, получить их координаты, получить даты выключения воды и нанести дома на карту 
"""

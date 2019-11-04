"""
В этой задаче вам предстоит установить и проверить модуль xmltodict.
Для этого скачайте xml-файл, а затем запустите приведенную ниже программу в той же папке, куда сохранен файл:

"""
import xmltodict

fin = open('test10-1.xml', 'r', encoding='utf8')
xmltext = fin.read()
fin.close()
xml = xmltodict.parse(xmltext)
for plant in xml['CATALOG']['PLANT']:
    for key in plant:
        print(key, plant[key])
    print('---')
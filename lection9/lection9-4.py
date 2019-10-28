"""
9.4 Запись JSON
Хотим сохранить все данные в файл
JSON - удобный способ передавать данные из одного скрипта в другой

"""
from urllib.request import urlopen
import json
total=1000#68674
i=0
alllst=[]#пустой список для всего, что скачалось
while i<total:
    url="https://apidata.mos.ru/v1/datasets/1401/rows?api_key=c25290a0b5f170f69d45a28665b43168&$top=500&$skip="+str(i)
    response=urlopen(url)
    respdata = response.read().decode('utf-8')
    lst = json.loads(respdata)
    alllst.extend(lst)
    i += 500
    print(i)
print(len(alllst))
#Alllst хотим сохранить в Json-файл
fout=open("lection-9-4-out.json","w",encoding="utf-8")
json.dump(alllst,fout,ensure_ascii=False)
fout.close()
#теперь можно натравить скрипт на реальные 60к+ данных
#а скрипт 9-4-1 будет принимать запрос и выводить время отключения

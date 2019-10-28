"""
9.2. Работа с публичным API
Запрос https://apidata.mos.ru/v1/datasets/1401/rows?api_key=c25290a0b5f170f69d45a28665b43168
повисит и вернет ошибку HTTP 413 - request entity too large, мы хотим получить больше ограничение по серверу.
В документации https://apidata.mos.ru/Docs#datasetRows
при запросе датасетов с количеством записей более 10000шт., в ответе будет передан статус 413.
Получение таких датасетов возможно с применением описанных ниже параметров $top (максимальное допустимое значение - 500шт.)
и $skip. Для получения количества записей в датасете можно воспользоваться запросом /datasets/{id}/count.
В датасете 1401 68674 записи
top=100
https://apidata.mos.ru/v1/datasets/1401/rows?api_key=c25290a0b5f170f69d45a28665b43168&$top=100
выдаст первые 100 записей
$top=100&$skip=100
выдаст следующие 100
Задача - забирать данные в JSON и превращать их в питоновский список

"""
from urllib.request import urlopen
import json
total=1000#68674
i=0
while i<total:
    url="https://apidata.mos.ru/v1/datasets/1401/rows?api_key=c25290a0b5f170f69d45a28665b43168&$top=500&$skip="+str(i)
    response=urlopen(url)
    i+=500
    respdata=response.read().decode('utf-8')
    #Превращаем ответ в формате JSON в питоновский список
    lst=json.loads(respdata)
    print(lst)


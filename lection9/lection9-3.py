"""
9.3 Формат JSON
Разбор ответа
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
    #Надо вытащить адрес, начало отключения горячей воды и конец отключения
    lst=json.loads(respdata)
    """
    {'global_id': 864658342, 'Number': 1, 
    'Cells': {'global_id': 864658342, 'AddressClarification': None, 'AdmArea': 'Центральный административный округ', 
    'District': 'район Хамовники', 'Address': 'город Москва, Бутиковский переулок, дом 18', 
    'BuildingType': 'жилой дом', 'OutageBySections': 'нет', 
    'Periods': [{'OutageEndTime': None, 'OutageBegin': 'без отключения', 'OutageEnd': 'без отключения', 
    'OutageBeginTime': None, 'Porches': 'все подъезды'}], 'UserNumber': [], 'UNOM': '3030'}}
    """
    for now in lst:
        cells=now['Cells']
        #print(cells['Address'])
        """
        В Periods список словарей
        Понадеемся, что отключение в доме всего одно, будем брать нулевой элеемент списка периодов
        """
        periods=cells['Periods']
        period=periods[0]
        begin=period['OutageBegin']
        end=period['OutageEnd']
        print(cells['Address'],begin,end)
        """
        Данные успешно извлечены. Надо проверить, обязательно ли при их использовании ссылаться на сайт-источник
        Следующая задача - сохранить данные в файл и нанести места отключения горячей воды на карту.
        """

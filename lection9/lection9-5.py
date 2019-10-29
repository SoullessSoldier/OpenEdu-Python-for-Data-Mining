"""
9.5 Знакомство с визуализацией геоданных
"""
"""
Принимаем адрес и ищем вхождения его как подстроки, выводим время отключения
"""
import json
fin=open("lecton9-4-out.json","r",encoding="utf-8")#lection-9-4-out.json
text=fin.read()
lst=json.loads(text)
s=input("Введите адрес: ")
for now in lst:
    cells = now['Cells']
    """
    В Periods список словарей
    Понадеемся, что отключение в доме всего одно, будем брать нулевой элеемент списка периодов
    """
    periods = cells['Periods']
    period = periods[0]
    begin = period['OutageBegin']
    end = period['OutageEnd']
    address=cells['Address']
    if s in address:
        print(f"По адресу {address} отключение воды с {begin} по {end}")
    """
    Консольный ввод/вывод можно заменить на чат-бота
    """
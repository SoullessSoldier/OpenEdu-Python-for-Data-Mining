#Пример решения задачи на обработку веб-страниц
'''
Задача - насколько совпадают профили университетов через английскую википедию
Список всех университетов Москвы: https://en.wikipedia.org/wiki/Category:Universities_in_Moscow
попарно сравнить между собой и определить, кто с кем имеет больше общего
Анализ:
ищем внутри <h2>Pages in category "Universities in Moscow"</h2>
ссылки вида '/wiki/' без 'Category:' и кроме слова 'Moscow'
'''
def getlinks(url):
    url_base = "https://en.wikipedia.org/"
    response = urlopen(url_base+url)
    html = response.read().decode('utf-8')
    soup = BS(html, 'lxml')
    links=set()#множество, так как ссылки могут повторяться
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/wiki') and ':' not in s:
                links.add(s)
    return links

url="/wiki/Category:Universities_in_Moscow"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

#allunivs=getlinks(url)
allunivs=list(getlinks(url))[:10]#временно укоротим задачу
print(allunivs)
print(len(allunivs))
#Составим таблицу похожести университетов и выведем ее в HTML
#Для кажлой пары университетов найдем число страниц, по которым они пересекаются
#Число подстановок - N^2, 3600 раз будем загружать страницы университетов???
        #Лучше сразу для каждого университета выгрузим все ссылки
        #тогда число проходов будет всего N
linkunivs={}#Создадим словарь
for univ in allunivs:
    linkunivs[univ]=getlinks(univ)
    print(univ,len(linkunivs[univ]))


for univ1 in allunivs:
    for univ2 in allunivs:
        print(univ1,univ2,len(linkunivs[univ1]&linkunivs[univ2]))

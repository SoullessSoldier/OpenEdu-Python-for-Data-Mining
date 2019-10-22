#Обработка ссылок
'''
Далее попробуем находить кратчайший путь от одной ссылки до другой
Теория 6 рукопожатий
'''
'''
/wiki/ - 1 уровень ссылок
/wiki/* - 2 уровень ссылок
/wiki/*/* - 3 уровень ссылок
на каждом уровне некое множество ссылок, обработка может занять большое время
Будем шагать с 1 уровня вниз и с нижнего уровня вверх
научимся до одного и того же места доходить и с верха, и с низа 
напишем функцию, которая получая ссылку на страницу, выдает множество страниц, на которые ссылается эта страница
def getlinks(url)

'''

def getlinks(url):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    soup = BS(html, 'lxml')
    links=set()#множество, так как ссылки могут повторяться
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/wiki') and ':' not in s:
                links.add(s)
    return links

url="wiki/Higher_School_of_Economics"
url_base="https://en.wikipedia.org/"
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

links=getlinks(url_base+url)
#print(links)
#print(len(links))
#Теперь можно добыть все ссылки со 2го уровня
'''
for now in links:
    print(now)
    nowlinks=getlinks(url_base+now)
    print(len(nowlinks))
    
#процесс достаточно медленный
'''
#посчитаем сколько общих ссылок у 2 разных статей
links2=getlinks(url_base+'/wiki/Moscow_State_University')
print(len(links&links2))#просто пересечем множества
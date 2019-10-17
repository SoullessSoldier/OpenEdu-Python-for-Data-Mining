#Работа с тегами HTML
'''
Из лекции 7-3 надо отфильтровать все ненужное и получить ссыылки

'''
url="https://en.wikipedia.org/wiki/Higher_School_of_Economics"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

#Список служебных ссылок, которые нам не нужны
'''
Либо через список исключений
exceptions=set(['/wiki/Wikipedia:Citation_needed','/wiki/File:','/wiki/Special:',
                '/wiki/Wikipedia:','/wiki/Help:','/wiki/Portal:',
                '/wiki/Talk:','/wiki/Category:'])

for link in soup.find_all('a'):
    if link.has_attr('href'):
        s=link.get('href')
        if s.startswith('/wiki'):
            flag=True
            for now in exceptions:
                if s.startswith(now):
                    flag=False
            if flag:
                print(link.get('href'))
'''
'''
Либо просто предположив, что знак : в ссылках не встречается
'''
for link in soup.find_all('a'):
    if link.has_attr('href'):
        s=link.get('href')
        if s.startswith('/wiki') and ':' not in s:
            print(s)

'''
Далее попробуем находить кратчайший путь от одной ссылки до другой
Теория 6 рукопожатий
'''
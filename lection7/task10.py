'''
Мы сохранили статью с википедии, она доступна по ссылке https://stepik.org/media/attachments/lesson/258943/Moscow.html
Вам необходимо обработать ее с помощью BeautifulSoup и подсчитать все внутренние ссылки,
которые не содержат в себе двоеточия (не являются ссылкой на техническую статью в википедии) и не начинаются с символа #.
Под ссылкой понимается содержимое аттрибута href тега a. Ссылка называется внешней, если она ведет на другой сайт
(т.е. начинается с http:// или https://). Все остальные ссылки являются внутренними.
Вам могут быть полезны методы find_all для супа (он позволяет найти все теги на странице),
 метод has_attr для тега (проверяет есть ли такой атрибут у тега) и доступ к атрибуту тега по аналогии со словарем.
В качестве ответа выведите количество внутренних ссылок, удовлетворяющих условию.
'''
def getlinks(url):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    soup = BS(html, 'lxml')

    links=[]#надо все ссылки

    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and (':' not in s) and (not s.startswith('#')):
                links.append(s)
    return links

url="https://stepik.org/media/attachments/lesson/258943/Moscow.html"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

links=getlinks(url)
print(len(links))
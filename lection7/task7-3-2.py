'''
Мы сохранили статью с википедии, она доступна по ссылке https://stepik.org/media/attachments/lesson/258939/webpage.html

Вам необходимо обработать ее с помощью BeautifulSoup и вывести все внешние ссылки, которые есть на этой странице,
в том порядке как они встречались по одной в строке.

Под ссылкой понимается содержимое аттрибута href тега a.
Ссылка называется внешней, если она ведет на другой сайт (т.е. начинается с http:// или https://).

Вам могут быть полезны методы find_all для супа (он позволяет найти все теги на странице),
метод has_attr для тега (проверяет есть ли такой атрибут у тега) и доступ к атрибуту тега по аналогии со словарем.
'''
#url="input7-3-2.html"
url="https://stepik.org/media/attachments/lesson/258939/webpage.html"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

white_list=set(["http://","https://"])

for link in soup.find_all('a'):
    if link.has_attr('href'):
        s=link.get('href')
        for word in white_list:
            if s.startswith(word):
                print(link.get('href'))
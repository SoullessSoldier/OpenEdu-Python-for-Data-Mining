'''
В файле https://stepik.org/media/attachments/lesson/258944/New-York.html есть несколько таблиц,
у которых атрибут class равен wikitable collapsible collapsed.

Вам необходимо найти вторую (при нумерации с единицы) такую таблицу и
просто напечатать тег из BeautifiulSoup для этой таблицы (должен выводить html-код, начинающийся с тега <table>
и заканчивающийся </table>). Этот текст необходимо сдать в качестве ответа.

Для решения этой задачи полезно использовать аргумент attrs в методе find_all или другом аналогичном методе.
В качестве параметра attrs принимает словарь, где ключом является название атрибута, а значением - значение атрибута.
'''

url="https://stepik.org/media/attachments/lesson/258944/New-York.html"
#url='New-York.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

fout=open('out17.txt','w',encoding='utf8')

table= soup.find_all('table',attrs={"class": "wikitable collapsible collapsed"})[1]

print(table,file=fout)

fout.close()
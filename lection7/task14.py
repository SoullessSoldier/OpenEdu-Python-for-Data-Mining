'''
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица.
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму.
Для доступа к ячейкам используйте возможности BeautifulSoup.
'''
url="https://stepik.org/media/attachments/lesson/209723/3.html"
#url='input14.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')
links=[]
sum=0
for link in soup.find_all('td'):
    links.append(int(link.text.strip()))
for i in links:
    sum+=i
print(sum)


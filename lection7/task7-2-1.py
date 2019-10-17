'''import requests
from bs4 import BeautifulSoup as BS

page=requests.get('7-5.html')
res=BS(page.text,'lxml')
#print(res)
#list = res.find('div', class_='container')
list1=res.findAll('div', class_='course')
print(len(list1))'''


'''
Мы сохранили страницу с википедии про языки программирования и сохранили 
по адресу https://stepik.org/media/attachments/lesson/209717/1.html

Скачайте её с помощью скрипта на Питоне и посчитайте, какой язык упоминается 
чаще Python или C++ (ответ должен быть одной из этих двух строк). 
Необходимо просто подсчитать количество вхождений слова Python или C++ как подстроки.
'''

a=open('7-5.html','r',encoding='utf8')
cnt_python=0
cnt_cpp=0
for line in a:
    cnt_python+=line.count('Python')
    cnt_cpp+=line.count('C++')
print('Python') if cnt_cpp<cnt_python else print('C++')
a.close()
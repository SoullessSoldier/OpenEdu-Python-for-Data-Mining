'''
В файле https://stepik.org/media/attachments/lesson/258944/New-York.html есть несколько таблиц,
у которых атрибут class равен wikitable collapsible collapsed.

Вам необходимо найти вторую (при нумерации с единицы) такую таблицу и преобразовать ее в csv-таблицу.
В csv-таблице ячейки должны разделяться запятой, а строки не должны окружаться кавычками.

Например, для таблицы:

<table>
<tr><td>a</td><td>b</td></tr>
<tr><td colspan=2>c</td></tr>
</table>
ответ должен выглядеть так:

a,b
c
Обратите внимание, что в таблице может встречаться тег <tbody>, на который мы можем просто не обращать внимания.
Также там могут встречаться теги <th> (ячейка-заголовок), которые следует интерпретировать так же как теги <td>.
Для поиска нескольких тегов удобно пользоваться методом find_all,
которому в качестве параметра передается список строк с нужными названиями тегов.

Чтобы получить содержимое тега td (то что записано от открывающего до закрывающего тега),
достаточно написать td.text. Лучше удалить все пробельные символы в полученной строке с помощью метода strip().
'''

url="https://stepik.org/media/attachments/lesson/258944/New-York.html"
#url='New-York.html'
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html,'lxml')

fout=open('out18.csv','w',encoding='utf8')

table= soup.find_all('table',attrs={"class": "wikitable collapsible collapsed"})[1]
#Пишем th
print(table.find('th').text.strip(),file=fout)
rows=table.find_all('tr')
for row in rows:
    tds=row.find_all('td')
    str1=''
    for td in tds:
        #print(td)
        str1+=td.text+","

    print(str1[:-1],file=fout,end='')
print(file=fout)
fout.close()
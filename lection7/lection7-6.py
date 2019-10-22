#Пример решения задачи на обработку веб-страниц
#Собственно, красивый вывод в HTML
#По строкам и столбцам - университеты, на пересечении - количество общих ссылок
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
            if s.startswith('/wiki') and ':' not in s and (s!='/wiki/Moscow') and (s!='/wiki/Main_Page'):
                links.add(s)
    return links

url="/wiki/Category:Universities_in_Moscow"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

#allunivs=getlinks(url)
allunivs=list(getlinks(url))[:5]#временно укоротим задачу
#Отсортируем по алфавиту

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
    #print(univ,len(linkunivs[univ]))

fout=open('univs.html','w',encoding='utf8')
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <table border='1'>
        <tr>
''',file=fout)

allunivs=sorted(allunivs)

allunivs_shorted=allunivs.copy()
for i in range(0,len(allunivs_shorted)):
    allunivs_shorted[i]=allunivs_shorted[i][6:].replace('_',' ')

#print('','\t'.join(allunivs),sep='\t')
print('<td></td><td>','</td><td>'.join(allunivs_shorted),sep='\t',end='</td></tr>',file=fout)
for univ1 in allunivs:
    # ОТрежем лишнее '/wiki/' в строках с адресами, они уже не нужны, и заменим _ на пробелы
    print('<tr><td>',univ1[6:].replace('_',' '),'</td>',file=fout)
    #print(univ1,end='\t')
    for univ2 in allunivs:
        #print(len(linkunivs[univ1]&linkunivs[univ2]),end='\t')
        print('<td>',len(linkunivs[univ1] & linkunivs[univ2]), end='</td>',file=fout)
    #print()#для перевода строки
    print('</tr>',file=fout)
print('''
</table>
</body>
</html>
''',file=fout)
fout.close()
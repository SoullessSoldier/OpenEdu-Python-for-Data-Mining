'''
В этой задаче достаточно вам необходимо посчитать количество внутренних ссылок,
которые есть в обеих статьях: https://stepik.org/media/attachments/lesson/258943/Moscow.html
и https://stepik.org/media/attachments/lesson/258944/New-York.html

Обратите внимание, что если ссылка встречается в статье несколько раз, то учитывать ее нужно лишь однажды,
т.е. необходимо найти количество различных страниц википедии, на которых есть ссылка как из первой, так и из второй статьи.
'''
def getlinks(url):
    response = urlopen(url)
    html = response.read().decode('utf-8')
    soup = BS(html, 'lxml')

    links=set()#надо все ссылки

    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and (':' not in s) and (not s.startswith('#')):
                links.add(s)
    return links



from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
url1="https://stepik.org/media/attachments/lesson/258943/Moscow.html"
links1=getlinks(url1)
url2="https://stepik.org/media/attachments/lesson/258944/New-York.html"
links2=getlinks(url2)
print(len(links1&links2))
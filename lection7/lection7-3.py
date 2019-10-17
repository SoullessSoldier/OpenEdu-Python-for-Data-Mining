'''
на какие статьи ведут ссылки из википедии
https://ru.wikipedia.org/wiki/Высшая_школа_экономики
(интересны только внутренние ссылки <a href="/wiki/> (внутри википедии))
'''

#url="https://ru.wikipedia.org/wiki/Высшая_школа_экономики"
url="https://en.wikipedia.org/wiki/Higher_School_of_Economics"

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response=urlopen(url)
html=response.read().decode('utf-8')
soup=BS(html)
for link in soup.find_all('a'):
    print(link)


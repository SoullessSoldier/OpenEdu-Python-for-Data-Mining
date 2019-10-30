"""
Вам нужно научиться пользоваться функцией urlopen модуля urllib.requests

Откройте файл https://stepik.org/media/attachments/lesson/209717/1.html с помощью скрипта на питоне,
примените функцию urlopen, затем примените метод read, а затем метод decode со строкой параметром utf-8.
Напечатайте что получилось и сдайте в качестве ответа.
"""
from urllib.request import urlopen
print(urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8'))
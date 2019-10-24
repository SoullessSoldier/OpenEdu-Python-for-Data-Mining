a='''Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк. 
Выведите три найденных числа в формате, приведенном в примере. 
Словом считается последовательность больших и маленьких латинских букв (для проверки того, состоит ли строка только из латинских букв удобно пользоваться методом isalpha()). 
Все остальные символы считаются разделителями слов.
Разделителем слов стоит считать всё, что не является буквой, а не только пробелы.


Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258919/input.txt

Пример входного файла:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Пример ответа:

Input file contains:
108 letters 
20 words 
4 lines 
'''
import re
cnt_letters=0
cnt_words=0
cnt_rows=0

fin=open('input6-2-2.txt','r')
for line in fin:
    z=re.sub('[^a-zA-Z]',' ', line)
    s=z.split()
    cnt_rows+=1
    cnt_words+=len(s)
    for words in line:
        for j in words:
            if j.isalpha():
                cnt_letters+=1
            #elif j=='\'' or j=='-':
            #else:
                #cnt_words+=1
fin.close()
print('Input file contains:')
print(f'{cnt_letters} letters ')
print(f'{cnt_words} words ')
print(f'{cnt_rows} lines')
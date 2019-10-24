a='''
В качестве ответа введите все строки наибольшей длины из входного файла, не меняя их порядок.

В данной задаче удобно считать список строк входного файла целиком при помощи метода readlines().

Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258920/input.txt

Пример входного файла:

One
Twenty one
Two
Twenty two
Пример ответа:

Twenty one
Twenty two
'''
fin=open('input6-2-3.txt','r')
s=fin.readlines()
l=dict()
cnt=0
for line in s:
    l[cnt]=len(line)
    cnt+=1
fin.close()
final_dict = {k: v for k, v in l.items() if not v < max(l.values())}
for k,v in final_dict.items():
    print(s[k])
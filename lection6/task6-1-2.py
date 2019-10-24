'''Дан текст на языке племени Мумба-Юмба. Выведите все слова, встречающиеся в тексте, разделяя их пробелом.
Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в алфавитном порядке.
Подсказка. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей,
при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется в задаче,
а чтобы сделать то что нужно — вспомните про параметр key в сортировке.

В этой задачи нужно сдать только ответ для входного файла.
Ссылка на входной файл https://stepik.org/media/attachments/lesson/258916/input.txt
'''
fin=open("input6-1-2.txt",'r',encoding='utf8')

dct={}
lst=list()
for line in fin:
    s=line.split()
    lst+=s
    for word in s:
        if word in dct:
            dct[word]+=1
        else:
            dct[word]=1
fin.close()
file = open('1.txt','w')
#sorted_keys = sorted(dct, key=lambda x: int(dct[x]), reverse=True)
ss='''sorted_keys = sorted(dct, reverse=True)
dct1={}
for i in sorted_keys:
    s = str("{0};{1}\n").format(i, dct[i])
    file.writelines(s)
    dct1[dct[i]]=i
file.close()'''
lst=list()
for i in dct:
    lst.append([dct[i],i])
a=sorted(lst,reverse=True)#,key=lambda x: x[1])
b=sorted(a,key=lambda x: (-x[0],x[1]))
s=''
for i in b:
    #s = str("{0};{1}\n").format(i[0], i[1])
    s+=i[1]+' '
file.writelines(s)

file.close()
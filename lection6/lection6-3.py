#csv-файлы
#Файл для примера - test6-3-1.csv
#найдем медиану
fin=open('test6-3-1.csv','r',encoding='utf8')
vals=[]
for line in fin:
    now=line.split(',')
    print(now)
    vals.extend(list(map(int,now)))
fin.close()
print(vals)
vals.sort()
print("Median is: ",vals[len((vals))//2])
print("Mean is: ",sum(vals)/len(vals))

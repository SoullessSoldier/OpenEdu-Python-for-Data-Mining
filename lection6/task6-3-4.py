a='''Вася составил таблицу с ценами на продукты в разных магазинах. 
В первой строке таблицы (кроме первой ячейки) записаны названия продуктов. 
Во всех строках, начиная со второй, записана информация о ценах в магазине. 
В первой ячейки написано название магазина, а в ячейках, начиная со второй - цена на товар, название которого записано в первой строке соответствующего столбца.
Таблица задана как csv-файл, разделителем ячеек выступает точка с запятой, а строковые константы не окружаются кавычками.
Вася очень хочет поесть, но денег у него мало. Поэтому помогите ему определить самый дешевый продукт и в каком магазине он продается. 
Название продукта следует записать в первой строке, а название товара - во второй. 
Если несколько товаров стоят одинаково, то выведите то название, которое раньше в алфавитном порядке. 
Если этот товар продается в нескольких магазинах по одной минимальной цене, то выведите минимальное в алфавитном порядке название магазина.
Ссылка на csv-файл: https://stepik.org/media/attachments/lesson/258925/input.csv'''
fin=open('input6-3-4.csv','r',encoding='utf8')
goods=fin.readline().rstrip('\n').split(';')
l=[]
#print(shops)
for line in fin:
    s=line.rstrip('\n').split(';')
    shop=s[0]
    for i in range(1,len(s)):
        l.append([int(s[i]),goods[i],shop])
fin.close()
#for i in sorted(l,key=lambda x: (x[0],x[1],x[2]))[0]:
#    print(i)
for i in range(2):
    print(sorted(l,key=lambda x: (x[0],x[1],x[2]))[0][i+1])
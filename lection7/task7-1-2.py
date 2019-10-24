a='''
В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл, 
в котором будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10. 
'''
fout=open('task7-1-2.html','w')
s=['<html>\n','<body>\n','<table>\n']
fout.writelines(s)
s=[]
for i in range (1,11):
    s.append('<tr>\n')
    for j in range(1,11):
        s.append('<td>'+str(i*j)+'</td>\n')
    s.append('</tr>\n')
s.append('</table>\n</body>\n</html>')
fout.writelines(s)
fout.close()

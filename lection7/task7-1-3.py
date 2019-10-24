a='''
В этой задаче вам предстоит научиться создавать ссылки. 
Вам нужно сгенерировать html-код на питоне и сдать на проверку html-файл, в котором будет таблица размером 10 на 10, 
которая должна содержать таблицу умножения для чисел от 1 до 10. 
Каждое число в таблице должно быть ссылкой на страницу http://<это число>.ru. 
Например, число 12 должно быть ссылкой на страницу http://12.ru
'''
fout=open('task7-1-3.html','w')
s=['<html>\n','<body>\n','<table>\n']
fout.writelines(s)
s=[]
for i in range (1,11):
    s.append('<tr>\n')
    for j in range(1,11):
        s.append('<td><a href=\'http://'+str(i*j)+'.ru\'>'+str(i*j)+'</a></td>\n')
    s.append('</tr>\n')
s.append('</table>\n</body>\n</html>')
fout.writelines(s)
fout.close()

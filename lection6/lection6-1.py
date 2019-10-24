f_in=open("test2.txt",'r',encoding='utf8')
#1 вариант - обойти весь файл
cnt=0
for line in f_in:
    if 'abc' in line:
        cnt+=1
f_in.close()
print(cnt)
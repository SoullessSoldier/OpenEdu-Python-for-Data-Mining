"""
В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам.
Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W,
чтение R,
запуск X.
Вам требуется восстановить контроль над правами доступа к файлам
(ваша программа для каждого запроса должна будет возвращать OK, если над файлом выполняется допустимая операция,
или же Access denied, если операция недопустима.

В первой строке входного файла содержится число N (1  N  10000) —количество файлов содержащихся в данной файловой системе.

В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами.
Длина имени файла не превышает 15 символов.

Далее указано чиcло M (1  M  50000) — количество запросов к файлам.

В последних M строках указан запрос вида Операция Файл.
К одному и тому же файлу может быть применено любое количество запросов.
Операция чтения обозначается как read, записи - write, запуска - execute.

Для каждого из M запросов нужно вывести в отдельной строке Access denied или OK.

Sample Input:

4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
Sample Output:

OK
Access denied
Access denied
OK
OK
"""
N=int(input("Input N: "))
files_dict={}
for i in range(N):
    list1=input().split()
    files_dict[list1[0]]=list1[1:len(list1)]
#for i in files_dict.items():
#    print(i)
M=int(input("Input M: "))
for i in range(M):
    file_query=input().split()
    file=file_query[1]
    action=file_query[0]
    if action=="read":
        action="R"
        if action in files_dict[file]:
            print("OK")
        else:
            print("Access denied")
    elif action=="write":
        action="W"
        if action in files_dict[file]:
            print("OK")
        else:
            print("Access denied")
    elif action=="execute":
        action="X"
        if action in files_dict[file]:
            print("OK")
        else:
            print("Access denied")
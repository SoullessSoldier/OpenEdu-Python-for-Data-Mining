"""
Эта задача предназначена для того, чтобы проверить, что вам удалось установить интерпретатор Python и среду программирования.
Вам необходимо создать проект, скопировать приведённый ниже код (разбираться в нём не нужно),
запустить его и сдать вывод программы (число) в качестве ответа.

x = 2112
i = 0
ans = 0
while i < x:
    ans += sum(map(lambda x: x ** 2, [i // 10, i % 13]))
    i += 7
print(ans)
"""
x = 2112
i = 0
ans = 0
while i < x:
    ans += sum(map(lambda x: x ** 2, [i // 10, i % 13]))
    i += 7
print(ans)
#4462910
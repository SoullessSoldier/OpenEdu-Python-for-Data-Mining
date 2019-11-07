"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

Для каждого из запроса выведите название страны, в котором находится данный город.

Sample Input:

2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Odessa
3
Odessa
Moscow
Novgorod
Sample Output:

Ukraine
Russia
Russia
"""
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country

for i in range(int(input())):
    print(motherland[input()])
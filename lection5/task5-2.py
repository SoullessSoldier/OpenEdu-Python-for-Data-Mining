"""
В первой строке задаётся количество названий столиц - число N. В следующих N строках задаются названия столиц по одному в строке. Отсортируйте названия столиц в алфавитном порядке и выведите их по одному в строке.

Sample Input:

2
Moscow
Berlin
Sample Output:

Berlin
Moscow
"""
n=int(input())
a=[]
i=0
for i in range(n):
    a.append(input())
a.sort()
for i in a:
    print(i)
"""
В первой строке задаётся количество названий столиц и государств - число N. В следующих N строках задаются названия столиц и государств по одному в строке, слова разделяются одним пробелом. Отсортируйте названия столиц и государств по названию государства в алфавитном порядке и выведите их по одному в строке.

Sample Input:

2
Moscow Russia
Vienna Austria
Sample Output:

Vienna Austria
Moscow Russia
"""
def mykey(x):
    return x[1]
n=int(input())
a=[]
i=0
for i in range(n):
    a.append(input().split())
sortedlst=sorted(a,key=mykey)
for i in sortedlst:
    print(*i)
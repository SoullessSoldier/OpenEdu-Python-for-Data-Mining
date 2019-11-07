"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

Sample Input:

1 3 2
4 3 2
Sample Output:

2
"""
a=set(map(int,input().split()))
b=set(map(int,input().split()))
cnt=0
for i in a:
    if i in b:
        cnt+=1
print(cnt)
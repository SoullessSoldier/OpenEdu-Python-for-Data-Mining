"""
Даны два списка чисел. Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

Sample Input:

1 3 2
4 3 2
Sample Output:

2 3
"""
a1=set(map(int,input().split()))
a2=set(map(int,input().split()))
print(*sorted(a1&a2))
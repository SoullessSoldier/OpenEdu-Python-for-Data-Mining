"""
Определите количество четных элементов в последовательности, завершающейся числом 0.

Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит, а служит как признак ее окончания).

Sample Input:

2
1
4
0
Sample Output:

2
"""

cnt=-1
element=-1
while element!=0:
    element=int(input())
    if element%2==0:
        cnt+=1
print(cnt)
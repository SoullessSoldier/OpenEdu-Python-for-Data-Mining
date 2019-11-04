"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет - не выводите ничего. Если таких пар соседей несколько - выведите первую пару.

Sample Input:

-1 2 3 -1 -2
Sample Output:

2 3
"""
spisok=list(map(int,input().split()))
for i in range(0,len(spisok)-1):
    if spisok[i]*spisok[i+1]>0:
        print(spisok[i],spisok[i+1])
        break
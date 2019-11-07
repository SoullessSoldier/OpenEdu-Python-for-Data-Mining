"""
Дан список чисел. Определите, сколько в нем встречается различных чисел. Не забудьте, что функция len подходит и для множеств.

Sample Input:

1 2 3 2 1
Sample Output:

3
"""
myset=set(map(int,input().split()))
print(len(myset))
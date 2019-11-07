"""
Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO,
если не встречалось.

Sample Input:

1 2 3 2 3 4
Sample Output:

NO
NO
NO
YES
YES
NO
"""
numbers = list(map(int,input().split()))
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)

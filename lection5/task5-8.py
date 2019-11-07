"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.

В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков, упорядоченный по алфавиту.
Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков, упорядоченный по алфавиту.

Sample Input:

3
3
Russian
English
Japanese
2
Russian
English
1
English
Sample Output:

1
English
3
English
Japanese
Russian
"""
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')

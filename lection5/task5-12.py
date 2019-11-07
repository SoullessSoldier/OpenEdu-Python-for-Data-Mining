"""
Дана строка. Выведите слово, которое в этой строке встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом (алфавитном) порядке.

Sample Input:

apple orange banana banana orange
Sample Output:

banana
"""
counter = {}
line = input().split()
for word in line:
    counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
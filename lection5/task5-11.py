"""
На вход подается строка. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки. Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Sample Input:

one two one tho three
Sample Output:

0 0 1 0 0
"""
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
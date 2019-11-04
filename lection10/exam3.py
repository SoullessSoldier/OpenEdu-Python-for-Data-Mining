"""
Дана строка, в которой буква h встречается как минимум два раза.
Разверните последовательность символов, заключенную между первым и последнием появлением буквы h,
в противоположном порядке.
Sample Input:

In the hole in the ground there lived a hobbit
Sample Output:

In th a devil ereht dnuorg eht ni eloh ehobbit
"""
original=input()
pos1=original.find('h')
pos2=len(original)-original[::-1].find('h')
print(original[0:pos1+1] + original[pos1+1:pos2-1][::-1] + original[pos2-1:])
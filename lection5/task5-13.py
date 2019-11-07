"""
Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:

Пополнение счета клиента. Снятие денег со счета. Запрос остатка средств на счете. Перевод денег между счетами клиентов. Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая пробелов). Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия или перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом. Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.

Входной данные содержат количество и последовательность операций. Возможны следующие операции: DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет счета, то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента name. Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток средств на счету клиента name. TRANSFER name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у какого-либо клиента нет счета, то ему создается счет. INCOME p - начислить всем клиентам, у которых открыты счета, pот суммы счета. Проценты начисляются только клиентам с положительным остатком на счету, если у клиента остаток отрицательный, то его счет не меняется. После начисления процентов сумма на счету остается целой, то есть начисляется только целое число денежных единиц. Дробная часть начисленных процентов отбрасывается.

Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента. Если же у клиента с запрашиваемым именем не открыт счет в банке, выведите ERROR.

Sample Input:

7
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov

Sample Output:

105
-50
ERROR
"""
def deposit(name, sum):
    bank[name] = bank.get(name, 0) + int(sum)


def withdraw(name, sum):
    bank[name] = bank.get(name, 0) - int(sum)


def balance(name):
    if name not in bank:
        print('ERROR')
    else:
        print(bank[name])


def transfer(name_from, name_to, sum):
    withdraw(name_from, sum)
    deposit(name_to, sum)


def income(percent):
    for k, v in bank.items():
        if v > 0:
            bank[k] = int(v * ((int(percent) / 100) + 1))


bank = dict()

for i in range(int(input())):
    line = input().split()
    if 'BALANCE' in line:
        balance(line[1])
    elif 'DEPOSIT' in line:
        deposit(line[1], line[2])
    elif 'WITHDRAW' in line:
        withdraw(line[1], line[2])
    elif 'INCOME' in line:
        income(line[1])
    elif 'TRANSFER' in line:
        transfer(line[1], line[2], line[3])
    else:
        withdraw(line[1], line[3])
        deposit(line[2], line[3])
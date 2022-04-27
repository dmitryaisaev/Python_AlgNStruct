# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача
# решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому
# использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.

from collections import deque, ChainMap

alph16 = {x: y for x, y in zip('0123456789ABCDEF', range(16))}
alph10 = {x: y for x, y in zip(range(16),'0123456789ABCDEF')}
alph = ChainMap(alph10, alph16)

# перевод из 16-ричной в 10-чную
def HexToInt(nstr):
    dn = 0
    for i, item in enumerate(reversed(nstr)):
        dn += alph[item] * 16 ** i
    return dn

# перевод из 10-чной в 16-ричную
def IntToHex(numb):
    dq = deque()
    while numb > 0:
        dq.appendleft(alph[numb % 16])
        numb = numb // 16
    return list(dq)


# ввод данных и хранение в виде списка
lnum1 = list(input('Введите 1 число в шестнадцатеричном виде = ').upper())
lnum2 = list(input('Введите 2 число в шестнадцатеричном виде = ').upper())

# перевод ы 10-чную системц
num1 = HexToInt(lnum1)
num2 = HexToInt(lnum2)

#  получение результатов  и хранение в виде списка
lsum_ = IntToHex(num1 + num2)
lmul_ = IntToHex(num1 * num2)

# вывод на экран в виде списка
print(f'{lnum1} + {lnum2} = {lsum_}')
print(f'{lnum1} * {lnum2} = {lmul_}')

# вывод в виде строки
print(f'{"".join(lnum1)} + {"".join(lnum2)} = {"".join(lsum_)}')
print(f'{"".join(lnum1)} * {"".join(lnum2)} = {"".join(lmul_)}')
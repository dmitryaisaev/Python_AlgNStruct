# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
l1 = input('Введите первую букву = ')
l2 = input('Введите вторую букву = ')
letter_a = ord('a')
p1 = ord(l1) - letter_a + 1
p2 = ord(l2) - letter_a + 1
print(f'Номер первой буква = {p1}')
print(f'Номер второй буквы = {p2}')
d = p2 - p1 - 1
print(f'Количество букв между {l1} и {l2} = {d}')
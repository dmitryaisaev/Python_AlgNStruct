# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

a = int(input('Введите номер буквы в алфавите = '))
letter_a = ord('a')
n = chr(letter_a - 1 + a)
print(f'Буква под номерам {a} = {n}')
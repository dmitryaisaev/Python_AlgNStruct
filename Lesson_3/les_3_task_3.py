# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

a1 = [randint(0,20) for i in range(20)]
print(f'Исходный массив: {a1}')
max_el = a1[0]
max_i = []
min_el = a1[0]
min_i = []
for i in range(len(a1)):
    if max_el < a1[i]:
       max_el = a1[i]
       max_i.clear()
       max_i.append(i)
    elif max_el == a1[i]:
        max_i.append(i)
    if min_el > a1[i]:
        min_el = a1[i]
        min_i.clear()
        min_i.append(i)
    elif min_el == a1[i]:
        min_i.append(i)
for i in max_i:
    a1[i] = min_el
for i in min_i:
    a1[i] = max_el
print(f'Результ. массив: {a1}')
print(f'Минимальный элемент: {min_el}, Максимальный элемент: {max_el}')
print(f'Номера минимальных элементов: {min_i}, номера максимальных элементов: {max_i}')

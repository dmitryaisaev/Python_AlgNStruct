# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

def recurs_max(array, size):
    if size == 2:
        if array[0] > array[1]:
            return array[0]
        else:
            return  array[1]
    else:
        m = recurs_max(array, size - 1)
        if array[size - 1] > m:
            return array[size - 1]
        else:
            return m

a = [[randint(1,100) for _ in range(5)] for _ in range(3)]
for line in a:
    for item in line:
        print(f'{item:>4}', end = '')
    print()

r_min = a[0]
for i in range(1, len(a)):
    for j, item in enumerate(a[i]):
        if r_min[j] > item:
            r_min[j] = item

print('-' * len(r_min) * 5)
for el in r_min:
    print(f'{el:>4}', end = '')
print()

print(f'Макс среди минимальных элементов столбцов матрицы =  {recurs_max(r_min, len(r_min))}')

max_ = r_min[0]
for i in range(1, len(r_min)):
    if r_min[i] > max_:
        max_ = r_min[i]

print(max_)
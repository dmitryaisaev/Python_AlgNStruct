# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

c = 5
r = 4
matrix = []
for i in range(r):
    sum_lines = 0
    matrix.append([])
    for j in range(c - 1):
        matrix[i].append(int(input(f'Введите элемнт матрицы: строка {i + 1}, колонка {j + 1} = ')))
        sum_lines += matrix[i][j]
    matrix[i].append(sum_lines)
for line in matrix:
    for item in line:
        print(f'{item:>4}', end = '')
    print()
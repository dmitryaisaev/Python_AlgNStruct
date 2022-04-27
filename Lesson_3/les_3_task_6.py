# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

a1 = [randint(0,100) for i in range(10)]
print(a1)
max_el = a1[0]
min_el = a1[0]
i1 = 0
i2 = 0
for i in range(len(a1)):
    if max_el < a1[i]:
       max_el = a1[i]
       i1 = i
    if min_el > a1[i]:
        min_el = a1[i]
        i2 = i
print('Номера максимального и минимального элементов массива: ', i1, i2)
if i1 < i2:
    st = i1
    fn = i2
else:
    st = i2
    fn = i1
v_sum = 0
for i in range(st + 1, fn):
    v_sum += a1[i]
print('Сумма =', v_sum)
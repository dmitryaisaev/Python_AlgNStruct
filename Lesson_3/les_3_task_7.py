# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

a = [randint(1,20) for i in range(10)]
print(a)
m1 = a[0]
i1 = 0
for i in range(i1 + 1, len(a)):
    if m1 > a[i]:
        m1 = a[i]
        i1 = i
m2 = a[0]
i2 = 0
if i1 == 0:
    m2 = a[1]
    i2= 1
for i in range(i2 + 1, len(a)):
    if i != i1 and m2 > a[i]:
        m2 = a[i]
        i2 = i
print(m1, m2)
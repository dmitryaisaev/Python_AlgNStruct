# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

a1 = [randint(0,5) for i in range(20)]
print(a1)
cnt = {0:0}
for i in a1:
    cnt[i] = cnt.get(i, 0) + 1
print(cnt)
v_max = 0
k_max = []
for k, v in cnt.items():
    if v_max < v:
        v_max = v
        k_max.clear()
        k_max.append(k)
    elif v_max == v:
        k_max.append(k)
print(k_max)
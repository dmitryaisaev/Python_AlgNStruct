# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

lst_s = [i for i in range(2, 100)]
d_k = {i: 0 for i in range(2, 10)}
for i in lst_s:
    for j in d_k.keys():
        if i % j == 0:
            d_k[j] += 1
for k, v in d_k.items():
    print(f'Кратно {k}: {v}')
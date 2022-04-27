# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

from random import randint

a1 = [randint(-10,100) for i in range(20)]
print(a1)

v_neg_max = 0
i_neg_max = 0
for i in range(0, len(a1)):
    if a1[i] < 0:
        if v_neg_max == 0:
            v_neg_max = a1[i]
            i_neg_max = i
        if v_neg_max < a1[i]:
            v_neg_max = a1[i]
            i_neg_max = i
print(f'Максимальный отрицательный элемент {v_neg_max}, под номером {i_neg_max}')
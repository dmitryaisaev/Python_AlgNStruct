# задача 7 из урока 3
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
# код оформлен в функцию, на входе кол-во элементов массива
# предварительно удалены функции print()

from random import randint
import cProfile

def get_array(n):
   return([randint(-100, 100) for _ in range(n)])


# 1 вариант - через 2 цикла
def my_func1(SIZE):
    array = get_array(SIZE)
    m1 = array[0]
    i1 = 0
    for i in range(i1 + 1, SIZE):
        if m1 > array[i]:
            m1 = array[i]
            i1 = i
    m2 = array[0]
    i2 = 0
    if i1 == 0:
        m2 = array[1]
        i2= 1
    for i in range(i2 + 1, SIZE):
        if i != i1 and m2 > array[i]:
            m2 = array[i]
    return (m1, m2)

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func1(5)"
# 1000 loops, best of 5: 10.3 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func1(10)"
# 1000 loops, best of 5: 19.4 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func1(15)"
# 1000 loops, best of 5: 27.8 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func1(20)"
# 1000 loops, best of 5: 34.7 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func1(100)"
# 1000 loops, best of 5: 168 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func1(500)"
# 1000 loops, best of 5: 846 usec per loop

# cProfile.run('my_func1(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.293    0.293 <string>:1(<module>)
#         1    0.000    0.000    0.267    0.267 les_4_task_12.py:10(get_array)
#         1    0.039    0.039    0.267    0.267 les_4_task_12.py:11(<listcomp>)
#         1    0.025    0.025    0.292    0.292 les_4_task_12.py:15(my_func1)
#    100000    0.089    0.000    0.179    0.000 random.py:200(randrange)
#    100000    0.049    0.000    0.228    0.000 random.py:244(randint)
#    100000    0.064    0.000    0.090    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.293    0.293 {built-in method builtins.exec}
#    100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    127528    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}

# 2 вариант - за 1 проход
def my_func2(SIZE):
    array = get_array(SIZE)

    if array[0] > array[1]:
        min_idx_1 = 0
        min_idx_2 = 1
    else:
        min_idx_1 = 1
        min_idx_2 = 0

    for i in range(2, SIZE):
        if array[i] < array[min_idx_1]:
            spam = min_idx_1
            min_idx_1 = i
            if array[spam] < array[min_idx_2]:
                min_idx_2 = spam
        elif array[i] < array[min_idx_2]:
            min_idx_2 = i
    return(array[min_idx_1], array[min_idx_2])

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func2(5)"
# 1000 loops, best of 5: 9.82 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func2(10)"
# 1000 loops, best of 5: 18.6 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func2(15)"
# 1000 loops, best of 5: 27.2 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func2(20)"
# 1000 loops, best of 5: 34.7 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func2(100)"
# 1000 loops, best of 5: 168 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_12" "les_4_task_12.my_func2(500)"
# 1000 loops, best of 5: 843 usec per loop

# cProfile.run('my_func2(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.298    0.298 <string>:1(<module>)
#         1    0.000    0.000    0.269    0.269 les_4_task_12.py:10(get_array)
#         1    0.039    0.039    0.269    0.269 les_4_task_12.py:11(<listcomp>)
#         1    0.028    0.028    0.297    0.297 les_4_task_12.py:66(my_func2)
#    100000    0.090    0.000    0.181    0.000 random.py:200(randrange)
#    100000    0.049    0.000    0.230    0.000 random.py:244(randint)
#    100000    0.064    0.000    0.091    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.298    0.298 {built-in method builtins.exec}
#    100000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    127302    0.016    0.000    0.016    0.000 {method 'getrandbits' of '_random.Random' objects}


# Наблюдения и выводы:
# сложность у всех алгоритмов линейная
# по скорости практически одинаково
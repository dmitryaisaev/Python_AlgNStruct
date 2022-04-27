# задача 3 из урока 3
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# код оформлен в функцию, на входе кол-во элементов массива
# предварительно удалены функции print()

from random import randint
import cProfile

def get_array(n):
   return([randint(-100, 100) for _ in range(n)])


# ---------------------------------------------------------------------------------------------------------------------
# 1 вариант - в цикле за 1 проход
def my_func1(SIZE):
    array = get_array(SIZE)
    idx_min = 0
    idx_max = 0

    for i in range(SIZE):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return(array)

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func1(5)"
# 1000 loops, best of 5: 10.1 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func1(10)"
# 1000 loops, best of 5: 18.4 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func1(15)"
# 1000 loops, best of 5: 27.6 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func1(20)"
# 1000 loops, best of 5: 35.4 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func1(100)"
# 1000 loops, best of 5: 168 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func1(500)"
# 1000 loops, best of 5: 847 usec per loop

# cProfile.run('my_func1(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.011    0.011    2.951    2.951 <string>:1(<module>)
#         1    0.399    0.399    2.669    2.669 les_4_task_13.py:10(<listcomp>)
#         1    0.271    0.271    2.940    2.940 les_4_task_13.py:15(my_func1)
#         1    0.000    0.000    2.669    2.669 les_4_task_13.py:9(get_array)
#   1000000    0.865    0.000    1.761    0.000 random.py:200(randrange)
#   1000000    0.509    0.000    2.270    0.000 random.py:244(randint)
#   1000000    0.630    0.000    0.896    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    2.951    2.951 {built-in method builtins.exec}
#   1000000    0.105    0.000    0.105    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1272542    0.161    0.000    0.161    0.000 {method 'getrandbits' of '_random.Random' objects}



# ---------------------------------------------------------------------------------------------------------------------
# 2 вариант - использование фкнкций min() max()
def my_func2(SIZE):
    array = get_array(SIZE)
    min_num = min(array)
    max_num = max(array)

    idx_min = array.index(min_num)
    idx_max = array.index(max_num)

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return (array)

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func2(5)"
# 1000 loops, best of 5: 9.67 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func2(10)"
# 1000 loops, best of 5: 17.5 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func2(15)"
# 1000 loops, best of 5: 24.9 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func2(20)"
# 1000 loops, best of 5: 32.8 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func2(100)"
# 1000 loops, best of 5: 153 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func2(500)"
# 1000 loops, best of 5: 762 usec per loop

# cProfile.run('my_func2(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.011    0.011    2.705    2.705 <string>:1(<module>)
#         1    0.397    0.397    2.632    2.632 les_4_task_13.py:10(<listcomp>)
#         1    0.000    0.000    2.694    2.694 les_4_task_13.py:64(my_func2)
#         1    0.000    0.000    2.632    2.632 les_4_task_13.py:9(get_array)
#   1000000    0.867    0.000    1.760    0.000 random.py:200(randrange)
#   1000000    0.475    0.000    2.235    0.000 random.py:244(randint)
#   1000000    0.629    0.000    0.893    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    2.705    2.705 {built-in method builtins.exec}
#         1    0.031    0.031    0.031    0.031 {built-in method builtins.max}
#         1    0.031    0.031    0.031    0.031 {built-in method builtins.min}
#   1000000    0.104    0.000    0.104    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1274373    0.160    0.000    0.160    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# ---------------------------------------------------------------------------------------------------------------------
# 3 вариант - если использовать рекурсию для поиска мин/макс

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

def recurs_min(array, size):
    if size == 2:
        if array[0] < array[1]:
            return array[0]
        else:
            return  array[1]
    else:
        m = recurs_min(array, size - 1)
        if array[size - 1] < m:
            return array[size - 1]
        else:
            return m

def my_func3(SIZE):
    array = get_array(SIZE)
    lna = len(array)
    min_num = recurs_min(array, lna)
    max_num = recurs_max(array, lna)

    idx_min = array.index(min_num)
    idx_max = array.index(max_num)

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return (array)

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func3(5)"
# 1000 loops, best of 5: 11.9 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func3(10)"
# 1000 loops, best of 5: 22.6 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func3(15)"
# 1000 loops, best of 5: 33 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func3(20)"
# 1000 loops, best of 5: 44.4 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func3(100)"
# 1000 loops, best of 5: 211 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_13" "les_4_task_13.my_func3(500)"
# 1000 loops, best of 5: 1.09 msec per loop

# cProfile.run('my_func3(990)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 les_4_task_13.py:10(<listcomp>)
#     989/1    0.001    0.000    0.001    0.001 les_4_task_13.py:115(recurs_max)
#     989/1    0.002    0.000    0.002    0.002 les_4_task_13.py:128(recurs_min)
#         1    0.000    0.000    0.005    0.005 les_4_task_13.py:141(my_func3)
#         1    0.000    0.000    0.003    0.003 les_4_task_13.py:9(get_array)
#       990    0.001    0.000    0.002    0.000 random.py:200(randrange)
#       990    0.000    0.000    0.002    0.000 random.py:244(randint)
#       990    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       990    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1253    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# Наблюдения и выводы:
# сложность у всех алгоритмов линейная
# по времени выполнения алгоритм использующий встроенные функции min() и msx() уверенно обогнал других
# использование рекурсии оказался самым долгим
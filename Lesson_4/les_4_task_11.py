# задача 9 из урока 3
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# код оформлен в функцию, на входе кол-во элементов массива
# предварительно удалены функции print()

from random import randint
import cProfile

def get_array(n):
   return([[randint(1,100) for _ in range(n)] for _ in range(n)])

# 1 вариант - за 2 цикла и рекурсию
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

def my_func1(SIZE):
    matrix = get_array(SIZE)

    r_min = matrix[0]
    for i in range(1, SIZE):
        for j, item in enumerate(matrix[i]):
            if r_min[j] > item:
                r_min[j] = item
    return(recurs_max(r_min, len(r_min)))

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(5)"
# 1000 loops, best of 5: 45.1 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(10)"
# 1000 loops, best of 5: 163 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(15)"
# 1000 loops, best of 5: 354 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(20)"
# 1000 loops, best of 5: 621 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(25)"
# 1000 loops, best of 5: 943 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(30)"
# 1000 loops, best of 5: 1.35 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(35)"
# 1000 loops, best of 5: 1.83 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(40)"
# 1000 loops, best of 5: 2.4 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func1(100)"
# 1000 loops, best of 5: 14.9 msec per loop

# cProfile.run('my_func1(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.668    0.668 <string>:1(<module>)
#         1    0.001    0.001    0.640    0.640 les_4_task_11.py:10(<listcomp>)
#     499/1    0.003    0.000    0.003    0.003 les_4_task_11.py:13(recurs_max)
#         1    0.024    0.024    0.667    0.667 les_4_task_11.py:26(my_func1)
#         1    0.000    0.000    0.640    0.640 les_4_task_11.py:9(get_array)
#    250000    0.210    0.000    0.430    0.000 random.py:200(randrange)
#    250000    0.118    0.000    0.548    0.000 random.py:244(randint)
#    250000    0.155    0.000    0.220    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.668    0.668 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    250000    0.026    0.000    0.026    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    320538    0.040    0.000    0.040    0.000 {method 'getrandbits' of '_random.Random' objects}

# 2 вариант - за 2 вложенных цикла
def my_func2(SIZE):
    matrix = get_array(SIZE)

    max_ = matrix[0][0]
    for j in range(SIZE):
        min_ = matrix[0][j]
        for i in range(SIZE):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]
        if min_ > max_ :
            max_ = min_
    return(max_)

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(5)"
# 1000 loops, best of 5: 46.2 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(10)"
# 1000 loops, best of 5: 167 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(15)"
# 1000 loops, best of 5: 363 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(20)"
# 1000 loops, best of 5: 639 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(25)"
# 1000 loops, best of 5: 954 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(30)"
# 1000 loops, best of 5: 1.36 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(35)"
# 1000 loops, best of 5: 1.91 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(40)"
# 1000 loops, best of 5: 2.45 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func2(100)"
# 1000 loops, best of 5: 15.2 msec per loop

# cProfile.run('my_func2(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.668    0.668 <string>:1(<module>)
#         1    0.001    0.001    0.634    0.634 les_4_task_11.py:10(<listcomp>)
#         1    0.034    0.034    0.668    0.668 les_4_task_11.py:57(my_func2)
#         1    0.000    0.000    0.634    0.634 les_4_task_11.py:9(get_array)
#    250000    0.207    0.000    0.427    0.000 random.py:200(randrange)
#    250000    0.117    0.000    0.544    0.000 random.py:244(randint)
#    250000    0.155    0.000    0.220    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.668    0.668 {built-in method builtins.exec}
#    250000    0.025    0.000    0.025    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    320150    0.039    0.000    0.039    0.000 {method 'getrandbits' of '_random.Random' objects}

# 3 вариант - за 3 цикла
def my_func3(SIZE):
    matrix = get_array(SIZE)

    r_min = matrix[0]
    for i in range(1, SIZE):
        for j, item in enumerate(matrix[i]):
            if r_min[j] > item:
                r_min[j] = item
    max_ = r_min[0]
    for i in range(1, len(r_min)):
        if r_min[i] > max_:
            max_ = r_min[i]
    return(max_)

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(5)"
# 1000 loops, best of 5: 44.2 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(10)"
# 1000 loops, best of 5: 157 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(15)"
# 1000 loops, best of 5: 350 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(20)"
# 1000 loops, best of 5: 608 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(25)"
# 1000 loops, best of 5: 954 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(30)"
# 1000 loops, best of 5: 1.33 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(35)"
# 1000 loops, best of 5: 1.81 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(40)"
# 1000 loops, best of 5: 2.36 msec per loop

# python -m timeit -n 1000 -s "import les_4_task_11" "les_4_task_11.my_func3(100)"
# 1000 loops, best of 5: 14.4 msec per loop

# cProfile.run('my_func3(500)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.656    0.656 <string>:1(<module>)
#         1    0.001    0.001    0.632    0.632 les_4_task_11.py:10(<listcomp>)
#         1    0.023    0.023    0.655    0.655 les_4_task_11.py:117(my_func3)
#         1    0.000    0.000    0.632    0.632 les_4_task_11.py:9(get_array)
#    250000    0.211    0.000    0.427    0.000 random.py:200(randrange)
#    250000    0.115    0.000    0.542    0.000 random.py:244(randint)
#    250000    0.153    0.000    0.217    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.656    0.656 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#    250000    0.025    0.000    0.025    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    320150    0.039    0.000    0.039    0.000 {method 'getrandbits' of '_random.Random' objects}

# Наблюдения и выводы:
# самым быстрым оказался алгоритм №3 самым медленным алгоритм №2, алгоритм с рекурсией оказался посередине
# данная оценка получена ЭМИПИРИЧЕСКИ - путем замеров времени выполнения, почему так у меня объективного объяснения (аналитической оценке
# в видеоуроках не учили) возможно особенности обращения к памяти - в №2 выборка элементов массива по 2-м индексам matrix[i][j],
# алгоритм с рекурсией отработал быстро возможно из-за того что вызовы функций возможно кэшируются и быстрее отрабатывают
# исходя из замеров времени работы: время увеличиваетсмя не линейно, если постороить график зависимости времени выполнения
# от кол. входных данных то получится график похожий на параблолу - исходя из ЭМПИРИЧЕСКОЙ оценки сложность алгоритма квадратичная O(n^2)
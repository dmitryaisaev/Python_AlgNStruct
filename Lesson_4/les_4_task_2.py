import cProfile

# 1 Решето Эратосфена ==================================================================================================
def sieve(n):
    sv = [i for i in range(n)]
    sv[1] = 0

    for i in range(2, n):
        if sv[i] != 0:
            j = i * 2
            while j < n:
                sv[j] = 0
                j += i

    return([i for i in sv if i != 0])

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(10)"
# 1000 loops, best of 5: 4.08 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(20)"
# 1000 loops, best of 5: 7.74 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(30)"
# 1000 loops, best of 5: 11.4 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(40)"
# 1000 loops, best of 5: 15.5 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(50)"
# 1000 loops, best of 5: 18.9 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(100)"
# 1000 loops, best of 5: 37.2 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(150)"
# 1000 loops, best of 5: 56.3 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(200)"
# 1000 loops, best of 5: 76.2 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(250)"
# 1000 loops, best of 5: 97.5 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(300)"
# 1000 loops, best of 5: 121 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(350)"
# 1000 loops, best of 5: 144 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(400)"
# 1000 loops, best of 5: 170 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(450)"
# 1000 loops, best of 5: 193 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(500)"
# 1000 loops, best of 5: 215 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve(1000)"
# 1000 loops, best of 5: 463 usec per loop

cProfile.run('sieve(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.064    0.064 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 les_4_task_2.py:15(<listcomp>)
#         1    0.054    0.054    0.063    0.063 les_4_task_2.py:4(sieve)
#         1    0.005    0.005    0.005    0.005 les_4_task_2.py:5(<listcomp>)
#         1    0.000    0.000    0.064    0.064 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2 прстой алгоритм перебора ===========================================================================================
def prime(n):
    lst = []
    for i in range(2, n):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return (lst)

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(10)"
# 1000 loops, best of 5: 2.02 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(20)"
# 1000 loops, best of 5: 4.75 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(30)"
# 1000 loops, best of 5: 7.3 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(40)"
# 1000 loops, best of 5: 10.2 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(50)"
# 1000 loops, best of 5: 14 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(100)"
# 1000 loops, best of 5: 34.9 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(150)"
# 1000 loops, best of 5: 60.7 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(200)"
# 1000 loops, best of 5: 94.8 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(250)"
# 1000 loops, best of 5: 126 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(300)"
# 1000 loops, best of 5: 167 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(350)"
# 1000 loops, best of 5: 209 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(400)"
# 1000 loops, best of 5: 260 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(450)"
# 1000 loops, best of 5: 315 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(500)"
# 1000 loops, best of 5: 367 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.prime(1000)"
# 1000 loops, best of 5: 1.07 msec per loop

# cProfile.run('prime(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    6.763    6.763 <string>:1(<module>)
#         1    6.761    6.761    6.763    6.763 les_4_task_2.py:72(prime)
#         1    0.000    0.000    6.763    6.763 {built-in method builtins.exec}
#      9592    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# 3 Решето Эратосфена (с оптимизацией) =================================================================================
def sieve_o(n):
    sv = [i for i in range(n)]
    sv[1] = 0

    for i in range(2, n):
        if sv[i] != 0:
            j = i * i
            while j < n:
                sv[j] = 0
                j += i

    return([i for i in sv if i != 0])

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(50)"
# 1000 loops, best of 5: 15.7 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(100)"
# 1000 loops, best of 5: 32.3 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(150)"
# 1000 loops, best of 5: 47.6 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(200)"
# 1000 loops, best of 5: 63.8 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(250)"
# 1000 loops, best of 5: 82.1 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(300)"
# 1000 loops, best of 5: 101 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(350)"
# 1000 loops, best of 5: 120 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(400)"
# 1000 loops, best of 5: 142 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(450)"
# 1000 loops, best of 5: 160 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(500)"
# 1000 loops, best of 5: 180 usec per loop

# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.sieve_o(1000)"
# 1000 loops, best of 5: 384 usec per loop

# cProfile.run('sieve_o(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.051    0.051 <string>:1(<module>)
#         1    0.042    0.042    0.051    0.051 les_4_task_2.py:137(sieve_o)
#         1    0.005    0.005    0.005    0.005 les_4_task_2.py:138(<listcomp>)
#         1    0.004    0.004    0.004    0.004 les_4_task_2.py:148(<listcomp>)
#         1    0.000    0.000    0.051    0.051 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# Наблюдения и выводы:
# по времени выполнения ожидаемо выиграл 3 алгоритм оптимизированное решето
# исходя из замеров времени у простого алгоритма экспоненциальная сложность O(e^n) при увеличении входных данных время
# выполнения резко возрастает, для 1 000 000 прошло больше минуты я не стал ждать до конца
# 1 и 3 похожи на линейные, но в инете написано что у классического решета логарифмическая сложность O(n log(log(n)))

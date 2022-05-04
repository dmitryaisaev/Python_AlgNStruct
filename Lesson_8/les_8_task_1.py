size = int(input('Введите кол. человек = '))

graph = []

# заполнение графа
for i in range(size):
    graph.append([])
    for j in range(size):
        if i == j:
            graph[i].append(0)
        else:
            graph[i].append(1)

for el in graph:
    print(el)


# сумма рукопожатий
sum_n = 0
# признаки того что человек уже пожал руку
is_shake = [False for _ in range(size)]

# проходим по каждому человеку и тот пожимает руки всем
for i in range(size):
    is_shake[i] = True  # помечаем что i-й человк пожал руку всем
    for j in range(size):
        # если человек уже проходио по всем с рукопожатием (признак True) то пропускаем
        if not is_shake[j]:
            sum_n += 1
print(sum_n)
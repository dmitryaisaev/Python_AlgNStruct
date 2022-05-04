from random import randint
from collections import deque

def gen_graph(n):
    for i in range(n):
        k = 0
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = randint(0, 1)
            k += graph[i][j]
        # если вдруг получилась вершина ни с кем не связанная
        if k == 0:
            if i == 0:
                graph[i][1] = 1
            else:
                graph[i][0] = 1



vertex_count = int(input('Введите количество вершин = '))
graph = [[None for _ in range(vertex_count)] for _ in range(vertex_count)]

gen_graph(vertex_count)
for el in graph:
    print(el)

# пройденные
is_visited = [False for _ in range(vertex_count)]
# не пройденные
stack = []
# пройденные вершины
passed = []

def dfs(start_vertex):
    if not is_visited[start_vertex]:
        passed.append(start_vertex)

    # помечаем как посещенную
    is_visited[start_vertex] = True

    # проходим по всем смежным вершинам
    for i in range(vertex_count):
        if graph[start_vertex][i] == 1:
            if not is_visited[i]:
                stack.append(i) # есть смежная вершина и она не посещена - добавляем в стэк

    # if len(stack) > 0:
    #     print(stack)

    # если закончились все смежные вершины выходим
    if len(stack) == 0:
        return

    # берем из стэка вершину бобавленную последней и идем "в глубь"
    current = stack.pop()
    dfs(current)

dfs(int(input('Введите стартовую вершину = ')))
print(f'Список пройденных вершин: ', passed)


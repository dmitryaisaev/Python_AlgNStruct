from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijksra(graph, idxStart):
    length = len(graph)
    start = idxStart
    is_visited = [False] * length
    lstCost = [float('inf')] * length  # результирующий список
    lstParent = [-1] * length

    lstCost[idxStart] = 0     # итоговая стоимость
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[idxStart] = True

        for i, vertex in enumerate(graph[idxStart]):
            if vertex != 0 and not is_visited[i]:
                if lstCost[i] > vertex + lstCost[idxStart]:
                    lstCost[i] = vertex + lstCost[idxStart]
                    lstParent[i] = idxStart

        min_cost = float('inf')
        for i in range(length):
            if min_cost > lstCost[i] and not is_visited[i]:
                min_cost = lstCost[i]
                idxStart = i

    print(lstParent)

    cost = 0
    lstPath = [deque([i]) for i in range(length)]

    for i in range(length):
        if i == start:
            continue
        if lstParent[i] < 0:
            lstPath[i].clear()
            lstPath[i].appendleft(-1)
            continue
        n = i
        while lstParent[n] != start:
            lstPath[i].appendleft(lstParent[n])
            n = lstParent[n]
        lstPath[i].appendleft(start)

    for i, el in enumerate(lstPath):
        if -1 in el:
            print(f'{i}: Нет пути')
        else:
            print(f'{i}: ' + ' '.join(map(str, el)))

    return lstCost


s = int(input('От какой вершины идти: '))
print(dijksra(g, s))
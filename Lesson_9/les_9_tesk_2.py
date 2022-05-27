# 2. Закодируйте любую строку по алгоритму Хаффмана.

import collections
from binarytree import Node

codetab = {}

# функция обхода дерева
def search(search_tree: Node, path=''):
    if search_tree.left == None and search_tree.right == None:
        codetab[search_tree.value] = path
        return
    else:
        if search_tree.left != None:
            search(search_tree.left, path + '0')
        if search_tree.right != None:
            search(search_tree.right, path + '1')

# для вычисления частот используем каунтер
input_str = 'beep boop beer!' # проверочная строка
input_str = input('Введите строку ')
fr = collections.Counter(input_str)

print(fr)

deq_s = collections.deque()
deq_p = collections.deque()

for k, v in fr.most_common():
    deq_p.appendleft(v)
    deq_s.appendleft(k)

print(deq_p)
print(deq_s)

# цикл пока в очереди не останется 1 элемент
while len(deq_s) > 1:
    # создаем узел дерева = 1 приоритет + 2 приоритет
    c = Node(deq_p[0] + deq_p[1])
    # если в очереди узел то добавляем если нет то создаем узел и добавляем в новый узел слева
    if type(deq_s[0]) == Node:
        c.left = deq_s[0]
    else:
        c.left = Node(deq_s[0])
    # если в очереди узел то добавляем если нет то сощдаем узел и добавляем в новый узел справа
    if type(deq_s[1]) == Node:
        c.right = deq_s[1]
    else:
        c.right = Node(deq_s[1])
    # убираем левый и следующий элементы из очередей и приоритетов
    deq_s.popleft()
    deq_s.popleft()
    deq_p.popleft()
    deq_p.popleft()
    # теперь надо вставить узел в очеред на свое место по получившемуся приоритету
    if len(deq_p) == 0:
        deq_s.append(c)
        deq_p.append(c.value)
    else:
        for i in range(len(deq_p)):
            if deq_p[i] >= c.value:
                deq_s.insert(i, c)  # в очередь с символами вставляем узел
                deq_p.insert(i, c.value) # в очередь с приоритетами значение нового узла
                break
            if i == len(deq_p) - 1:
                deq_s.append(c)
                deq_p.append(c.value)

print(deq_s[0])

search(deq_s[0])

print('Кодовая таблица', codetab)

res = ''
for ch in input_str:
    res = res + codetab[ch]

print('Закодированная строка ', res)
print(len(res) // 8, ' байт против ', len(input_str) * 8)
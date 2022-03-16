"""
Номер посылки 66050325


-- ПРИНЦИП РАБОТЫ --

В представленной задаче, если счиать все дороги типа R -- дорогами одного направления,
а дороги типа B -- дорогами другого направления, то можно свести задачу к задаче нахождения петель в графе
Действительно, если из точки A в точку B можно доехать дорогами обоих типов, то в ориентированном графе
это будет означать наличие петли с вершинами A и B.

Тогда можно решить задачу методом обхода в глубину с покраской.

Если при проверке смежных по исходящим дугам вершин очередная вершина окажется серой — цикл есть,
то есть существует пара городов, между которыми есть дороги двух типов


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

В процессе поиска мы проходим по всем вершинам ∣V∣, перебирая все ребра ∣E∣, итоговая сложность O(∣E∣+ ∣V∣)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ

Нам необходимо хранить массив цветов -- O(V) дополнительной памяти
"""

import sys
from collections import defaultdict
from typing import List, Dict

WHITE = -1
GREY = 0
BLACK = 1


def is_loop_DFS(start_vertex: int, color: List[int], graph: Dict[int, List[int]]) -> bool:
    """
    Поиск петель в графе

    :param start_vertex: вершина начала обхода
    :param color: массив цветов
    :param graph: массив вершин
    :return: результата работа алгоритма: True, если петель нет,
             в противном случае False
    """
    stack = [start_vertex, ]

    while len(stack) > 0:
        v = stack.pop()
        if color[v] == WHITE:
            color[v] = GREY
            stack.append(v)
            if v in graph:
                for w in graph[v]:
                    if color[w] == WHITE:
                        stack.append(w)
                    elif color[w] == GREY:
                        return False

        elif color[v] == GREY:
            color[v] = BLACK

    return True


def dfs(graph: Dict[int, List[int]], m: int):
    """
    Поиск петель во всех компонентах связанности

    :param graph: словарь, описывающий ребра графа
    :param m: количество вершин
    :return:
    """
    color = [WHITE] * (m + 1)

    for v in range(1, m + 1):
        if color[v] == WHITE:
            result = is_loop_DFS(v, color, graph)
            if not result:
                return False

    return True


def main():
    # количество городов
    n = int(sys.stdin.readline().rstrip())

    # словарь вершина - смежные вершины
    graph = defaultdict(list)
    for i in range(1, n):

        for j, rb in enumerate(list(sys.stdin.readline().rstrip())):
            k = i + j + 1
            if rb == 'R':
                graph[i].append(k)
            else:
                graph[k].append(i)

    if dfs(graph, n):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

"""
Номер посылки 66050312


-- ПРИНЦИП РАБОТЫ --

Я реализовал сортировку построение максимального остовного дерева при помощи алгоритма Прима.
За счет взятия весов ребер с отрицательным знаком, ищется максимальное остовное дерево

Алгоритм Прима можно описать следующим образом:
Берется любая из вершин графа -- по умолчанию первая -- и находятся все исходящие из нее ребра.
Из этих ребер выбирается ребро с наименьшим весом, и в остов добавляется ребро и вершина6 в которую ребро входило.
Добавим ко множеству потенциально добавляемых рёбер все, которые исходят из новой вершины и входят в вершины,
ещё не включённые в остов.
Повторяем, пока в остовном дереве не будет n вершин и n-1 ребер.
Каждый раз при добавлении ребра, подсчитываем его вес и добавляем к общей сумме


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Мы храним все ребра в куче с поддержанием минимума.
Если вместе с ребром в подграф добавляется новая вершина, то это ребро добавляется в остов. Если ребро соединяет две вершины,
уже присутствующее в подмножестве остова, мы отбрасываем его из дальнейшего рассмотрения и из кучи в том числе.
Благодаря приоритетной очереди сложность алгоритма Прима
O(∣E∣ log∣V∣), где ∣E∣ — количество рёбер в графе, а ∣V∣ — количество вершин.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ

Нам необходимо хранить массив вершин ∣V∣ и ребер ∣E∣ остова, пространственная сложность O(∣E∣ + ∣V∣)
"""

import heapq
import sys
from collections import defaultdict


class Graph:

    def __init__(self, vertex_count: int, init_vertex: int = 1):
        """
        инициализация

        :param vertex_count: количетсво вершин в графе
        :param init_vertex: вершина, с которой начнем поиск минимального остовного дерева
        """

        self.vertex_count = vertex_count
        self.added = set()  # Множество вершин, уже добавленных в остов.
        self.not_added = [1]*(vertex_count+1)  # Множество вершины, ещё не добавленных в остов.
        self.edges = list()  # Массив рёбер, исходящих из остовного дерева.
        self.all_edges = defaultdict(list)
        self.init_vertex = init_vertex

    def add_edge(self, i: int, j: int, weight: int):
        """
        Добавление неориентированного ребра графа

        :param i: первая вершина
        :param j: вторая вершина
        :param weight: вес ребра
        """
        if i != j:
            self.all_edges[i].append((j, weight))
            self.all_edges[j].append((i, weight))

    def add_vertex(self, v):
        """
        Добавляет все рёбра, которые инцидентны v, но их конец ещё не в остове.

        :param v: номер вершины
        """
        self.added.add(v)
        self.not_added[v] = 0

        for (end, weight) in self.all_edges.get(v, []):
            if self.not_added[end] != 0:
                heapq.heappush(self.edges, (weight, (v, end)))

    def find_min_spanning_tree_weight(self) -> int:
        """
        Строит минимальное остовное дерево, подсчитывает и выдает суммарный вес его ребер
        Если построить минимальное остовное дерево невозможно, возбуждается исключение
        """

        sum_weight = 0

        self.add_vertex(self.init_vertex)

        while len(self.added) < self.vertex_count and len(self.edges) > 0:
            weight, (_, end) = heapq.heappop(self.edges)

            if self.not_added[end] > 0:
                sum_weight += weight
                self.add_vertex(end)

        if len(self.added) < self.vertex_count:
            raise Exception('Oops! I did it again')

        return sum_weight


def main():

    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    graph = Graph(n)

    for _ in range(m):
        i, j, w = map(int, sys.stdin.readline().rstrip().split())

        # чтобы найти макимаьное остовное дерево, добавляем вес ребра с отрицательным знаком
        graph.add_edge(i, j, -w)

    try:
        max_spanning_tree_weight = graph.find_min_spanning_tree_weight()
        print(-max_spanning_tree_weight)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

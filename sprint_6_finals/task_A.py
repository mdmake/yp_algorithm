import sys
import heapq

minimum_spanning_tree = []  # Рёбра, составляющие MST.

added = set()  # Множество вершин, уже добавленных в остов.
not_added = set()  # Множество вершины, ещё не добавленных в остов.
edges = list()  # Массив рёбер, исходящих из остовного дерева.
all_edges = dict()
# vertices = set()
weight = dict()


def add_vertex(v):
    global edges
    global added
    global not_added

    added.add(v)
    not_added.remove(v)
    # Добавляем все рёбра, которые инцидентны v, но их конец ещё не в остове.
    #
    # Вершины not_added стоит хранить в таком контейнере,
    # чтобы проверка (end in not_added) выполнялась эффективно.
    #
    # Для этого подойдёт, например, хеш-таблица.
    # Также в некоторых языках программирования имеется контейнер set.

    for (end, w) in all_edges.get(v, []):
        if end in not_added:
            heapq.heappush(edges, (w, (v, end)))

    # edges += [(i, j) for (i, j) in all_edges if i == v and j in not_added]
    # edges += graph.edges.filter(start == v, end in not_added)


def extract_minimum(egs: list):
    #me = max(egs, key=lambda item: weight[frozenset(item)])
    w, me = heapq.heappop(egs)
    #egs.remove(me)
    return w, me


def find_MST():
    summ = 0
    #global minimum_spanning_tree

    # not_added = vertices

    # Берём первую попавшуюся вершину.
    v = 1
    add_vertex(v)

    # пока not_added не пуст и edges не пуст:
    while len(not_added) > 0 and len(edges) > 0:
        # Подразумеваем, что extract_minimum извлекает минимальное ребро
        # из массива рёбер и больше данного ребра в массива не будет.
        w, (begin, end) = extract_minimum(edges)


        if end in not_added:
            # если e.end in not_added, то:
            summ += w
            #minimum_spanning_tree.append(end)
            add_vertex(end)

    if len(not_added) > 0:
        # если not_added не пуст, то
        # raise Exception("Исходный граф несвязный")
        print('Oops! I did it again')
    # верни ошибку "Исходный граф несвязный"
    else:
        print(-summ)
        #return minimum_spanning_tree


def main():
    # количество вершин, количество ребер
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    # словарь вершина - смежные вершины

    for _ in range(m):
        i, j, L = map(int, sys.stdin.readline().rstrip().split())

        # веса ребер
        if i != j:

            if i not in all_edges.keys():
                all_edges[i] = [(j, -L), ]
            else:
                all_edges[i].append((j, -L))

            if j not in all_edges.keys():
                all_edges[j] = [(i, -L), ]
            else:
                all_edges[j].append((i, -L))



    # MainDFS(s, n, graph)
    for i in range(1, n + 1):
        # vertices.append(i)
        not_added.add(i)

    find_MST()
    # print(minimum_spanning_tree)


if __name__ == '__main__':
    main()

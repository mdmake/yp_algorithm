import sys

dist = []
previous = []
weight_ = []
vertices = []
visited = []
graph = dict()
edge = dict()


def weight(u, v):
    return edge.get(frozenset((u, v)), float('inf'))


def relax(u, v):
    # Проверяем, не получился ли путь короче найденного ранее.
    if dist[v] > dist[u] + weight(u, v):
        dist[v] = dist[u] + weight(u, v)
        previous[v] = u


def get_min_dist_not_visited_vertex():
    # Находим ещё непосещённую вершину с минимальным расстоянием от s.
    current_minimum = float('inf')
    current_minimum_vertex = None

    for v in vertices:
        # для каждой вершины v из graph.vertices:
        if not visited[v] and (dist[v] <= current_minimum):
            # если (не visited[v]) И (dist[v] < current_minimum), то
            current_minimum = dist[v]
            current_minimum_vertex = v
    return current_minimum_vertex


def Dijkstra(graph, s):
    for v in vertices:
        dist[v] = float('inf')  # Задаём расстояние по умолчанию.
        previous[v] = None  # Задаём предшественника для восстановления SPT.
        visited[v] = False  # Список статусов посещённости вершин.

    dist[s] = 0  # Расстояние от вершины до самой себя 0.

    while True:
        # пока существуют непосещённые вершины с расстоянием не равным бесконечности:
        u = get_min_dist_not_visited_vertex()
        if u is None:
            break

        visited[u] = True
        # из множества рёбер графа выбираем те, которые исходят из вершины u
        neighbours = graph.get(u, [])

        for v in neighbours:
            relax(u, v)


def main():
    # количество вершин, количество ребер
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    # словарь вершина - смежные вершины

    for _ in range(m):
        i, j, L = (int(item) for item in sys.stdin.readline().rstrip().split())
        pair = frozenset((i, j))

        # веса ребер
        if pair not in edge:
            edge[pair] = L
        else:
            if L<edge[pair]:
                edge[pair] = L

        # направление связей
        if i not in graph:
            graph[i] = []
        if j not in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)

    # MainDFS(s, n, graph)
    for i in range(1, n + 1):
        vertices.append(i)

    for i in range(0, n + 1):
        previous.append(None)
        weight_.append(float('inf'))
        visited.append(False)
        dist.append(float('inf'))

    for v in vertices:
        Dijkstra(graph, v)
        print(*[x if x < float('inf') else -1 for x in dist[1:]])


if __name__ == '__main__':
    main()

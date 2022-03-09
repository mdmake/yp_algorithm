import sys


def DFS(v, color, vertex: dict):  # v - номер вершины
    color[v] = 'gray'  # Вершина посещена, но ещё не обработана.
    # для каждого исходящего ребра (v,w):
    print(v, end=' ')
    if v in vertex:
        for w in sorted(vertex[v]):
            if color[w] == 'white':  # Если вершина не посещена, то
                DFS(w, color, vertex)  # запустим обход от найденной смежной вершины.
    color[v] = 'black'  # Теперь вершина обработана.


def MainDFS(s, m, graph):
    color = ['white'] * (m+1)

    # для каждого i от 0 до |V| - 1:

    DFS(s, color, graph)

    # for v in range(1, m + 1):
    #     if v in graph:
    #         if color[v] == 'white':
    #             DFS(v, color, graph)  # Запускаем обход, стартуя с i-й вершины.


def main():
    # количество вершин, количество ребер
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    # словарь вершина - смежные вершины
    graph = dict()
    for _ in range(m):
        i, j = (int(item) for item in sys.stdin.readline().rstrip().split())
        if i not in graph:
            graph[i] = []
        if j not in graph:
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)


    for k in graph:
        graph[k] = sorted(graph[k])

    # стартовая вершина
    s = int(sys.stdin.readline().rstrip())

    MainDFS(s, n, graph)


if __name__ == '__main__':
    main()

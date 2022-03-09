import sys


def DFS(start_vertex: int, color, vertex: dict):

    stack = []
    stack.append(start_vertex)

    while len(stack) > 0:
        # Получаем из стека очередную вершину.
        # Это может быть как новая вершина, так и уже посещённая однажды.
        v = stack.pop()
        if color[v] == 'white':
            print(v, end=' ')
            # Красим вершину в серый. И сразу кладём её обратно в стек:
            # это позволит алгоритму позднее вспомнить обратный путь по графу.
            color[v] = 'gray'
            stack.append(v)
            # Теперь добавляем в стек все непосещённые соседние вершины,
            # вместо вызова рекурсии
            # для каждого исходящего ребра (v,w):
            if v in vertex:
                for w in sorted(vertex[v], reverse=True):
                    # возьмём вершину w
                    if color[w] == 'white':
                        stack.append(w)
        elif color[v] == 'gray':
            # Серую вершину мы могли получить из стека только на обратном пути.
            # Следовательно, её следует перекрасить в чёрный.
            color[v] = 'black'


def DFS_REC(v, color, vertex: dict):  # v - номер вершины
    color[v] = 'gray'  # Вершина посещена, но ещё не обработана.
    # для каждого исходящего ребра (v,w):
    print(v, end=' ')
    if v in vertex:
        for w in sorted(vertex[v]):
            if color[w] == 'white':  # Если вершина не посещена, то
                DFS(w, color, vertex)  # запустим обход от найденной смежной вершины.
    color[v] = 'black'  # Теперь вершина обработана.


def MainDFS(s, m, graph):
    color = ['white'] * (m + 1)

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

import sys



def DFS(v, color, vertex: dict, entry, leave, time):  # v - номер вершины
    time += 1
    entry[v] = time
    color[v] = 'gray'  # Вершина посещена, но ещё не обработана.
    # для каждого исходящего ребра (v,w):
    #print(v, end=' ')
    if v in vertex:
        for w in sorted(vertex[v]):
            if color[w] == 'white':  # Если вершина не посещена, то
               time = DFS(w, color, vertex, entry, leave, time)  # запустим обход от найденной смежной вершины.

    time += 1  # Перед выходом из вершины время снова обновляется.
    leave[v] = time  # Запишем время выхода.
    color[v] = 'black'  # Теперь вершина обработана.
    return time


def MainDFS(s, m, graph):
    color = ['white'] * (m + 1)
    time = -1
    entry = [None] * (m + 1)
    leave = [None] * (m + 1)

    # для каждого i от 0 до |V| - 1:

    DFS(s, color, graph, entry, leave, time)

    for i in range(1, m+1):
        print(entry[i], leave[i])


def main():
    # количество вершин, количество ребер
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    # словарь вершина - смежные вершины
    graph = dict()
    for _ in range(m):
        i, j = (int(item) for item in sys.stdin.readline().rstrip().split())
        if i not in graph:
            graph[i] = []
        graph[i].append(j)

    for k in graph:
        graph[k] = sorted(graph[k])

    # стартовая вершина
    s = 1

    MainDFS(s, n, graph)


if __name__ == '__main__':
    main()

import sys


def TopSort(v, color, graph, order):
    color[v] = 'gray'
    for w in graph.get(v, []):
        if color[w] == 'white':
            TopSort(w, color, graph, order)
    color[v] = 'black'
    order.append(v)  # Кладём обработанную вершину в стек.


def MainTopSort(n, graph, income):
    order = []
    color = ['white'] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 'white':
            TopSort(i, color, graph, order)

    print(*order[::-1])


def main():
    # количество вершин, количество ребер
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    # словарь вершина - смежные вершины
    graph = dict()
    income = set()
    for _ in range(m):

        i, j = (int(item) for item in sys.stdin.readline().rstrip().split())
        if i not in graph:
            graph[i] = []
        graph[i].append(j)
        income.add(j)

    # for k in graph:
    #     graph[k] = sorted(graph[k])

    MainTopSort(n, graph, income)
    # MainDFS(n, graph, income)


if __name__ == '__main__':
    main()

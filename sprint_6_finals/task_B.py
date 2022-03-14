import sys


def DFS(start_vertex: int, color, vertex: dict, colorComponent):
    stack = []
    stack.append(start_vertex)

    while len(stack) > 0:
        # Получаем из стека очередную вершину.
        # Это может быть как новая вершина, так и уже посещённая однажды.
        v = stack.pop()


        if color[v] == -1:
            # print(v, end=' ')
            # Красим вершину в серый. И сразу кладём её обратно в стек:
            # это позволит алгоритму позднее вспомнить обратный путь по графу.
            color[v] = 0
            stack.append(v)
            # Теперь добавляем в стек все непосещённые соседние вершины,
            # вместо вызова рекурсии
            # для каждого исходящего ребра (v,w):
            if v in vertex:
                for w in sorted(vertex[v], reverse=True):
                    # возьмём вершину w
                    if color[w] == -1:
                        stack.append(w)
                    elif color[w] == 0:
                        return False


        elif color[v] == 0:
            # Серую вершину мы могли получить из стека только на обратном пути.
            # Следовательно, её следует перекрасить в чёрный.
            color[v] = colorComponent

    return True


def MainDFS(m, graph):
    color = [-1] * (m + 1)

    # для каждого i от 0 до |V| - 1:

    component_count = 0
    rez = True
    for v in range(1, m + 1):
        if color[v] == -1:
            component_count += 1
            rez &= DFS(v, color, graph, component_count)  # Запускаем обход, стартуя с i-й вершины.


    if rez:
        print('YES')
    else:
        print('NO')


    # result = [list() for _ in range(component_count)]
    #
    # for i, item in enumerate(color[1:]):
    #     result[item - 1].append(i + 1)
    #
    # print(component_count)
    # for i in range(component_count):
    #     print(*result[i])


def main():
    # количество городов
    n = int(sys.stdin.readline().rstrip())

    # словарь вершина - смежные вершины
    graph = dict()
    for i in range(1, n):

        for j, rb in enumerate(list(sys.stdin.readline().rstrip())):
            k = i+j+1
            if rb == 'R':
                if i in graph:
                    graph[i].append(k)
                else:
                    graph[i] = [k, ]

            else:
                if k in graph:
                    graph[k].append(i)
                else:
                    graph[k] = [i, ]

    # for k in graph:
    #     graph[k] = sorted(graph[k])

    MainDFS(n, graph)


if __name__ == '__main__':
    main()

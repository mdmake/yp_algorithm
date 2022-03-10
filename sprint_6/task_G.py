import sys
from collections import deque

# Длины массивов равны числу вершин|V|.


def BFS(s, vertexes, color, distance, previous):
    # Создадим очередь вершин и положим туда стартовую вершину.
    planned = deque()
    planned.append(s)
    color[s] = 'gray'
    #print(s, end=' ')
    distance[s] = 0
    while len(planned)>0:
    # пока очередь planned не пуста:
        u = planned.popleft()  # Возьмём вершину из очереди.
        for v in vertexes.get(u, []):
        #для каждого ребра (u,v), исходящего из u:
            #возьмём вершину v
            if color[v] == 'white': # Серые и чёрные вершины уже
                                    # либо в очереди, либо обработаны.
                distance[v] = distance[u] + 1
                previous[v] = u
                # print(v, end=' ')
                color[v] = 'gray'
                planned.append(v) # Запланируем посещение вершины.
        color[u] = 'black' # Теперь вершина считается обработанной.

def ShortestPath(v, previous): # Кратчайший путь от s до v.
    # Класть вершины будем в стек, тогда
    # стартовая вершина окажется наверху стека
    # и порядок следования от s до v будет соответствовать
    # порядку извлечения вершин из стека.
    path = []
    current_vertex = v
    while current_vertex != None: # Предшественник вершины s равен None.
        path.append(current_vertex)
        current_vertex = previous[current_vertex]
    return path




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

    color = ['white'] * (n+1)
    previous = [None] * (n+1)
    distance = [None] * (n+1)

    BFS(s, graph, color, distance, previous)
    print(max(distance[1:]))

if __name__ == '__main__':
    main()

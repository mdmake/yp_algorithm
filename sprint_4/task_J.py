import sys


def effective_solution_3Sum(A, x):
    history = set()
    n = len(x)
    if n < 3:
        return set()

    triples = set()
    for i in range(n):
        for j in range(i + 1, n):
            target = A - x[i] - x[j]
            if target in history:
                triples.add((target, x[i], x[j]))
        history.add(x[i])
    return triples


def effective_solution_4Sum(A, x):
    lrez = list()
    storage = set()
    n = len(x)
    for i in range(3, n):
        target = A - x[i]
        rez3 = effective_solution_3Sum(target, x[:i])
        for item in rez3:
            tr = (*item, x[i])
            if tr not in storage:
                lrez.append(tr)
            storage.add((*item, x[i]))

    return lrez


def effective_solution(A, x):
    n = len(x)
    x.sort()
    pair = dict()
    for i in range(n):
        for j in range(i + 1, n):
            summ = x[i] + x[j]
            if summ not in pair:
                pair[summ] = [(i, j), ]
            else:
                pair[summ].append((i, j))

    storage = set()
    for i in range(2, n):
        for j in range(i + 1, n):
            target = A - x[i] - x[j]
            if target in pair:
                for (i_0, j_0) in pair[target]:
                    if j_0 < i:
                        storage.add((x[i_0], x[j_0], x[i], x[j]))

    return storage


def main():
    n = sys.stdin.readline().rstrip()
    A = int(sys.stdin.readline().rstrip())
    data = [int(item) for item in sys.stdin.readline().rstrip().split()]
    data.sort()
    rez = effective_solution(A, data)
    rez = list(rez)
    print(len(rez))
    rez.sort()
    for item in rez:
        print(*item)


if __name__ == '__main__':
    main()

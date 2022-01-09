import sys


def non_effective_solution(A, x):
    history = set()
    n = len(x)
    x.sort()
    quadros = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                target = A - x[i] - x[j] - x[k]
                if target in history:
                    quadros.add((target, x[i], x[j], x[k]))
        history.add(x[i])
    return quadros


def effective_solution(A, x):

    n = len(x)
    x.sort()
    pair = dict()
    for i in range(n):
        for j in range(i + 1, n):
            summ = x[i] + x[j]
            if summ not in pair:
                pair[summ] = {(i, j), }
            else:
                pair[summ].add((i, j))

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

    rez = effective_solution(A, data)
    print(len(rez))
    rez = list(rez)
    rez.sort()
    for item in rez:
        print(*item)


if __name__ == '__main__':
    main()

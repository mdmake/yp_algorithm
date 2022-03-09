import sys


def main():
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    result = dict()
    for _ in range(m):
        i, j = (int(item) for item in sys.stdin.readline().rstrip().split())
        if i not in result:
            result[i] = []
        result[i].append(j)

    for k in range(1, max(result.keys()) + 1):
        if k in result:
            print(len(result[k]), *sorted(result[k]))
        else:
            print(0)


if __name__ == '__main__':
    main()

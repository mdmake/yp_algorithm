import sys


def main():
    n, m = (int(item) for item in sys.stdin.readline().rstrip().split())

    result = [[0]*n for _ in range(n)]
    for _ in range(m):
        i, j = (int(item) for item in sys.stdin.readline().rstrip().split())
        result[i-1][j-1] = 1

    for row in range(n):
        print(*result[row])


if __name__ == '__main__':
    main()

import sys
from collections import defaultdict

'''
10
8 5 5 8 6 9 8 2 4 7
8
9 8 1 1 1 5 10 8

5
'''


def calcSortNum(data):
    k = defaultdict(int)
    for number in data:
        k[number] += 1

    return k


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    children = [int(item) for item in sys.stdin.readline().rstrip().split()]
    m = int(sys.stdin.readline().rstrip())
    cookies =  [int(item) for item in sys.stdin.readline().rstrip().split()]

    children.sort(reverse=True)
    cookies.sort(reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if children[i] > cookies[j]:
            i = i + 1
        else:
            i += 1
            j += 1
    print(j)


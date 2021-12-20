import sys
from random import randint
'''
10
8 5 5 8 6 9 8 2 4 7
8
9 8 1 1 1 5 10 8

5
'''

def partition(array, pivot):

    left = []
    center = []
    right = []

    for item in array:
        if item < pivot:
            right.append(item)
        elif item == pivot:
            center.append(item)
        else:
            left.append(item)

    return left, center, right


def quicksortReverse(array):
    if len(array) < 2:  # базовый случай,
        return array       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[randint(0, len(array)-1)]
        left, center, right = partition(array, pivot)
        return quicksortReverse(left) + center + quicksortReverse(right)


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    children = [int(item) for item in sys.stdin.readline().rstrip().split()]
    m = int(sys.stdin.readline().rstrip())
    cookies = [int(item) for item in sys.stdin.readline().rstrip().split()]

    children = quicksortReverse(children)
    cookies = quicksortReverse(cookies)

    i = 0
    j = 0
    while i < n and j < m:
        if children[i] > cookies[j]:
            i = i + 1
        else:
            i += 1
            j += 1
    print(j)

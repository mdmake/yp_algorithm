import sys
from random import randint


def countingSortID(array):
    counted_values = [0] * (max(array) + 1)
    for value in array:
        counted_values[value] += 1

    edList = []

    for i in range(len(counted_values)):
        if counted_values[i] != 0:
            edList.append((counted_values[i], i))

    return edList


def partition(array, pivot):
    left = []
    center = []
    right = []

    for item in array:
        if item[0] < pivot:
            right.append(item)
        elif item[0] == pivot:
            center.append(item)
        else:
            left.append(item)

    return left, center, right


def quicksortReverse(array):
    if len(array) < 2:  # базовый случай,
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        pivot = array[randint(0, len(array) - 1)][0]
        left, center, right = partition(array, pivot)
        return quicksortReverse(left) + center + quicksortReverse(right)


if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    ids = list(map(int, sys.stdin.readline().rstrip().split()))
    k = int(sys.stdin.readline().rstrip())

    ids = countingSortID(ids)
    ids = quicksortReverse(ids)
    ids.sort(key=lambda x: x[0], reverse=True)
    print(" ".join([str(ids[i][1]) for i in range(k)]))

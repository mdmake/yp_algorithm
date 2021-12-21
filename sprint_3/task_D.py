import sys

'''
10
8 5 5 8 6 9 8 2 4 7
8
9 8 1 1 1 5 10 8

5
'''


def countingSort(array):
    counted_values = [0] * (max(array)+1)
    for value in array:
        counted_values[value] += 1

    index = len(array)-1
    for value in range(0, len(counted_values)):
        for amount in range(1, counted_values[value]+1):
            array[index] = value
            index -= 1

    return array


def main():
    n = int(sys.stdin.readline().rstrip())
    children = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    cookies = list(map(int, sys.stdin.readline().rstrip().split()))

    children = countingSort(children)
    cookies = countingSort(cookies)

    i = 0
    j = 0
    while i < n and j < m:
        if children[i] > cookies[j]:
            i = i + 1
        else:
            i += 1
            j += 1
    print(j)


if __name__ == '__main__':
    main()

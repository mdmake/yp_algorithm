import sys


def countingSortAndSum(array, k):
    counted_values = [0] * (max(array)+1)
    for value in array:
        counted_values[value] += 1

    index = 0
    summa = 0
    for value in range(0, len(counted_values)):
        for amount in range(1, counted_values[value]+1):
            summa += value
            if summa > k:
                return index
            index += 1

    return len(array)


def main():
    n, k = list(map(int, sys.stdin.readline().rstrip().split()))
    district = list(map(int, sys.stdin.readline().rstrip().split()))

    return countingSortAndSum(district, k)


if __name__ == '__main__':
    print(main())

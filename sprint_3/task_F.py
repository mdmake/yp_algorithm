import sys


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
    lines = list(map(int, sys.stdin.readline().rstrip().split()))

    lines = countingSort(lines)

    for i in range(0, n-2):
        prePerimetr = lines[i+1] + lines[i+2]
        if lines[i] < lines[i+1] + lines[i+2]:
            return lines[i] + prePerimetr

    return -1


if __name__ == '__main__':
    print(main())

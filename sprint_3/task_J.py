def bubbleSortPass(data, n):
    rez = False
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            data[i], data[i + 1] = data[i + 1], data[i]
            rez = True

    return rez


import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    r = bubbleSortPass(data, n)
    print(*data)
    while r:
        r = bubbleSortPass(data, n)
        if r:
            print(*data)
import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    prices = list(map(int, sys.stdin.readline().rstrip().split()))

    ac = 0
    diff = 0
    mem_pr = float('inf')  # цена на момент покупки
    for i in range(n - 1):

        if ac == 1:
            # ловим пик
            if prices[i] > mem_pr and prices[i + 1] < prices[i]:
                ac = 0
                diff += prices[i]
                continue

        if ac == 0:
            # ищем покупку -- если на следующем шаге цена выше -- покупаем сейчас
            if prices[i] < prices[i + 1]:
                mem_pr = prices[i]
                diff -= prices[i]
                ac = 1
                continue

    if ac == 1:
        diff += prices[-1]

    print(diff)


if __name__ == '__main__':
    main()

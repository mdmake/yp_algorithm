import sys


def main():
    m = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    piles = []
    for i in range(n):
        piles.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

    piles = sorted(piles, key=lambda item: item[0], reverse=True)

    price = 0

    for (worth, volume) in piles:
        if volume < m:
            price += volume*worth
            m -= volume
        else:
            price += m * worth
            break

    print(price)


if __name__ == '__main__':
    main()

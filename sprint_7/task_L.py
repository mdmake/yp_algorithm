import sys


def main():
    # количество слитков, вместимость рюкзака

    n, M = (map(int, sys.stdin.readline().rstrip().split()))

    weight = list(map(int, sys.stdin.readline().rstrip().split()))

    dp0 = [0] * (M + 1)
    dp1 = [0] * (M + 1)

    for i in range(n):
        for j in range(M + 1):
            if j - weight[i] >= 0:
                dp1[j] = max(dp0[j], weight[i] + dp0[j - weight[i]])
            else:
                dp1[j] = dp0[j]

        dp0 = [item for item in dp1]

    print(dp1[-1])


if __name__ == '__main__':
    main()

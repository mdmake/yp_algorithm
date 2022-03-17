import sys


def main():
    # количество слитков, вместимость рюкзака

    n, M = (map(int, sys.stdin.readline().rstrip().split()))

    weight = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [[0] * (M + 1) for _ in range(n)]

    for i in range(n):
        for j in range(M + 1):
            if j - weight[i] >= 0:
                dp[i][j] = max(dp[i - 1][j], weight[i] + dp[i - 1][j - weight[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[-1][-1])


if __name__ == '__main__':
    main()

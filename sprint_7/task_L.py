import sys



def main():
    # количество слитков, вместимость рюкзака

    n, M = (map(int, sys.stdin.readline().rstrip().split()))

    weight = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [0] * (M + 1)

    # https: // www.youtube.com / watch?v = T4bY72lCQac & list = PLqM7alHXFySGMu2CSdW_6d2u1o6WFTIO -
    # https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    for i in range(n):
        for j in range(M, weight[i]-1, -1):
            if j - weight[i] >= 0:
                dp[j] = max(dp[j], weight[i] + dp[j - weight[i]])

    print(dp[-1])


if __name__ == '__main__':
    main()

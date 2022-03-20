import sys


def main():

    n = int(sys.stdin.readline().rstrip())

    weight = sorted((map(int, sys.stdin.readline().rstrip().split())))

    s = sum(weight)

    if s % 2 != 0 or n < 2:
        print(False)
        return
    else:
        M = s//2


    dp = [False] * (M + 1)

    # https: // www.youtube.com / watch?v = T4bY72lCQac & list = PLqM7alHXFySGMu2CSdW_6d2u1o6WFTIO -
    # https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    for i in range(n):
        for j in range(M, weight[i]-1, -1):
            # if j - weight[i] >= 0:
            #     dp[j] = max(dp[j], weight[i] + dp[j - weight[i]])
            if dp[j - weight[i]] or (weight[i] == j):
                dp[j] = True

    print(dp[-1])
    # if dp[-1] == M:
    #     print(True)
    # else:
    #     print(False)


if __name__ == '__main__':
    main()

import sys

# https://www.youtube.com/watch?v=-yiKNcjcK0Y

def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    b = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])

    i = n
    j = m
    i_idx = []
    j_idx = []

    while i != 0 and j != 0:
        if a[i - 1] == b[j - 1]:
            i_idx.append(i)
            j_idx.append(j)
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1

    print(*i_idx[::-1])
    print(*j_idx[::-1])


if __name__ == '__main__':
    main()

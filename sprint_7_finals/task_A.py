import sys


def main():
    # по вертикали
    s1 = list(sys.stdin.readline().rstrip())
    # по горизонтали
    s2 = list(sys.stdin.readline().rstrip())

    # строки
    m = len(s1) + 1
    # столбцы
    n = len(s2) + 1

    dp = [[0] * n for _ in range(m)]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + 1

    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + 1
        for j in range(1, n):
            p1 = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

            if s1[i-1] != s2[j-1]:
                p2 = dp[i - 1][j - 1] + 1
            else:
                p2 = dp[i - 1][j - 1]
            dp[i][j] = min(p1, p2)

    print(dp[m-1][n-1])


if __name__ == '__main__':
    main()

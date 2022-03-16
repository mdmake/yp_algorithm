import sys




def main():
    # строки, столбцы
    n, m = (map(int, sys.stdin.readline().rstrip().split()))

    points = []
    dp = [[0]*m for _ in range(n)]

    for _ in range(n):
        points.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    dp[n-1][0] = points[n-1][0]

    for i in range(n-1, -1,  -1):
        for j in range(0, m):

            if i == n-1 and j == 0:
                continue

            if i < n-1 and j > 0:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + points[i][j]
            elif j == 0:
                dp[i][j] = dp[i + 1][j] + points[i][j]
            else:
                dp[i][j] = dp[i][j - 1] + points[i][j]


    print(dp[0][m-1])

if __name__ == '__main__':
    main()




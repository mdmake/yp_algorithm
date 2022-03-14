import sys


def main():
    # ступеньки, количество прыжков
    n, k = (map(int, sys.stdin.readline().rstrip().split()))

    dp = [0] * (n + 3)

    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    if k > 1:
        dp[3] = 2
    else:
        dp[3] = 1

    mm = 10 ** 9 + 7

    for i in range(4, n + 1):

        dp[i] = sum(dp[max((1, i - k), ):i]) % mm
        # print(i, dp[max((1, i-k),):i])
        if i <= k + 1:
            dp[i] += 1

    print(dp[n])


if __name__ == '__main__':
    main()

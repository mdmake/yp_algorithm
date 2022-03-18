# https://www.youtube.com/watch?v=t2DpD9GnhfU

import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    r = list(map(int, sys.stdin.readline().rstrip().split()))

    dp = [0] * (n)
    p = [0] * (n)

    for i in range(n):
        for j in range(0, i):
            if r[i] > r[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    p[i] = j
                else:
                    p[i] = i

    mdp = max(dp)
    idx = dp.index(mdp)
    rez = [idx + 1, ]
    current = r[idx]
    current_idx = idx

    for i in range(current_idx - 1, -1, -1):
        if current > r[i] and dp[idx] - dp[i] == 1:
            rez.append(i + 1)
            current = r[i]
            idx = i

    print(mdp + 1)
    print(*rez[::-1])


if __name__ == '__main__':
    main()

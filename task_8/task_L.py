import sys


def prefix_function(s):
    # Функция возвращает массив длины |s|
    pi = [None] * len(s)
    pi[0] = 0

    for i in range(1, len(s)):
        k = pi[i - 1]
        while (k > 0) and (s[k] != s[i]):
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        pi[i] = k
    return pi


def main():
    s = sys.stdin.readline().rstrip()
    result = prefix_function(s)
    print(*result)


if __name__ == '__main__':
    main()

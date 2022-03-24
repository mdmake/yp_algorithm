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
    text = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    r = s + '#' + text

    rez = prefix_function(r)
    #print(*rez)

    k = 0
    new_text = ''
    for i, v in enumerate(rez[len(s)+1:]):
        if v == len(s):
            new_text += text[k:i-len(s)+1] + t
            k = i+1

    new_text += text[k:]
    print(new_text)



if __name__ == '__main__':
    main()

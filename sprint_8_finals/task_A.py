import sys


def unpack(s: str, i):
    rez = ''

    while i < len(s):

        if s[i].isalpha():
            rez += s[i]
        elif s[i].isdigit():
            m = int(s[i])
            r, i = unpack(s, i + 1)
            rez += m * r
        elif s[i] == '[':
            pass
        elif s[i] == ']':
            return rez, i,

        i += 1

    return rez, i


def main():
    n = int(sys.stdin.readline().rstrip())

    data = []
    for i in range(n):
        s, _ = unpack(sys.stdin.readline().rstrip(), 0)

        data.append(s)

    smax = max(data)
    smin = min(data)

    prefix = ''
    for s1, s2 in zip(smin, smax):
        if s1 == s2:
            prefix += s1
        else:
            return prefix

    return prefix


if __name__ == '__main__':
    print(main())

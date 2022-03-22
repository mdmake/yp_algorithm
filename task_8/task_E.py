import sys


def main():
    s = sys.stdin.readline().rstrip()
    count = int(sys.stdin.readline().rstrip())

    t = {}
    for i in range(count):
        item = sys.stdin.readline().rstrip().split()
        t[int(item[1])] = item[0]

    s1 = ''
    idx = 0
    for k in sorted(t.keys()):
        s1 += s[idx:k] + t[k]
        idx = int(k)

    s1 = s1 + s[idx:]

    print(s1)


if __name__ == '__main__':
    main()

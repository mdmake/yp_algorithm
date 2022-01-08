import sys


def main():
    a = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()

    if len(s) < 1:
        print(0)
        return
    rez = ord(s[0])
    for i in range(1, len(s)):
        rez = (rez * a + ord(s[i])) % m
    print(rez % m)


if __name__ == '__main__':
    main()

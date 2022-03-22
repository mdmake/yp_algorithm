import sys


def main():
    s = sys.stdin.readline().rstrip().split()
    print(*s[::-1])


if __name__ == '__main__':
    main()

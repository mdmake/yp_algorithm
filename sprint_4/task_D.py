import sys

def main():
    n = int(sys.stdin.readline().rstrip())

    names = set()
    for i in range(n):
        name = sys.stdin.readline().rstrip()
        if name not in names:
            names.add(name)
            print(name)


if __name__ == '__main__':
    main()

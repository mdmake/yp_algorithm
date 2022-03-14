import sys


def main():
    n = int(sys.stdin.readline().rstrip())

    dairy = []
    for i in range(n):
        dairy.append(tuple(sys.stdin.readline().rstrip().split()))

    dairy = sorted(dairy, key=lambda item: (float(item[1]), float(item[0])))

    end = '0'
    result = []

    for pair in dairy:
        if float(end) <= float(pair[0]):
            result.append(pair)
            end = pair[1]

    print(len(result))
    for pair in result:
        print(*pair)


if __name__ == '__main__':
    main()

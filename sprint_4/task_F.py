import sys


def myHash(s):

    # решение в лоб
    return sum([ord(item)**5 for item in s])


def main():
    n = int(sys.stdin.readline().rstrip())
    words = sys.stdin.readline().rstrip().split()

    length = dict()
    for i, word in enumerate(words):
        h = myHash(word)
        if h in length.keys():
            length[h].append(i)
        else:
            length[h] = [i,]

    for v in length.values():
        print(*v)


if __name__ == '__main__':
    main()

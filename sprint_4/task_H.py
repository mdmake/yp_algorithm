import sys


def myHash(s):

    hashTable = dict()

    hashSum = 0
    for i, char in enumerate(s):
        if char not in hashTable:
            hashTable[char] = i

        hashSum += hashTable[char]*i
    return hashSum


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    if myHash(s1) == myHash(s2):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
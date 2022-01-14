import sys


def main():
    memo = dict()
    maxLen = 0
    position = 0
    data = sys.stdin.readline().rstrip()
    i = 0
    for char in data:
        if char not in memo or  memo[char] < position:
            memo[char] = i
        else:
            length = i-position
            position = memo[char] + 1
            if maxLen < length:
                maxLen = length
            memo[char] = i

        i += 1

    length = i - position
    if maxLen < length:
        maxLen = length

    print(maxLen)


if __name__ == "__main__":
    main()
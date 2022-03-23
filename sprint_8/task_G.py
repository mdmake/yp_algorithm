import sys


def find(text, pattern, start=0):
    offset = len(pattern)
    if len(text) < len(pattern):
        return -1

    for pos in range(start, len(text) - len(pattern) + 1):
        if text[pos:pos + offset] == pattern:
            return pos

    return -1


def find_with_constant(text, pattern, start=0):
    offset = len(pattern)
    if len(text) < len(pattern):
        return -1

    for pos in range(start, len(text) - len(pattern) + 1):
        delta = text[pos] - pattern[0]
        new_pattern = list(map(lambda x: x + delta, pattern))
        if text[pos:pos + offset] == new_pattern:
            return pos

    return -1


def findall(text, pattern):
    pos = 0
    result = []
    while pos < len(text):
        pos = find_with_constant(text, pattern, start=pos)
        if pos == -1:
            return result
        result.append(pos+1)
        pos += 1

    return result


def main():
    n = int(sys.stdin.readline().rstrip())
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split()))

    print(*findall(s, p))


if __name__ == '__main__':
    main()

import string
import sys


def main():
    even = tuple(a for i, a in enumerate(list(string.ascii_lowercase)) if i % 2 == 1)

    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] not in even:
            i += 1
            continue

        if s2[j] not in even:
            j += 1
            continue

        # print(s1[i], s2[j])
        if s1[i] < s2[j]:
            return -1
        elif s1[i] > s2[j]:
            return 1
        else:
            i += 1
            j += 1

    if i < len(s1):
        if len(set(s1[i]) & set(even)) > 0:
            return 1

    if j < len(s2):
        if len(set(s2[j]) & set(even)) > 0:
            return -1

    return 0


if __name__ == '__main__':
    print(main())

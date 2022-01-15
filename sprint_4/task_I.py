import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    team_1 = sys.stdin.readline().rstrip().strip().split()
    m = int(sys.stdin.readline().rstrip())
    team_2 = sys.stdin.readline().rstrip().strip().split()

    maxLen = 0
    length = 0

    for k in range(len(team_1)):
        i = k
        j = 0
        while j < len(team_2):
            if i < len(team_1) and team_1[i] == team_2[j]:
                i += 1
                length += 1
            else:
                if maxLen < length:
                    maxLen = length
                length = 0
                i = k
            j += 1

    if maxLen < length:
        maxLen = length
    print(maxLen)


if __name__ == "__main__":
    main()


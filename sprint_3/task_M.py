import sys
def main(n, m, part1, part2, ):
    if part1[-1] < part2[0]:
        if (n + m) % 2 == 1:
            mid = (n + m) // 2

            if mid < n:
                return part1[mid]
            else:
                return part2[mid - n]

        else:
            mid1 = (n + m) // 2
            mid2 = mid1 - 1

            if mid1 < n:
                v1 = part1[mid1]
            else:
                v1 = part2[mid1 - n]

            if mid2 < n:
                v2 = part1[mid2]
            else:
                v2 = part2[mid2 - n]
            return (v1 + v2) / 2



    else:
        i, j = 0, 0
        rezult = []
        while i < n and j < m:

            if part1[i] < part2[j]:
                rezult.append(part1[i])

                if (i + j) == (n + m) // 2:
                    if (n + m) % 2 == 1:
                        return rezult[-1]
                    else:
                        return (rezult[-1] + rezult[-2]) / 2

                i += 1
            else:
                rezult.append(part2[j])

                if (i + j) == (n + m) // 2:
                    if (n + m) % 2 == 1:
                        return rezult[-1]
                    else:
                        return (rezult[-1] + rezult[-2]) / 2

                j += 1

        while i < n:
            rezult.append(part1[i])
            if (i + j) == (n + m) // 2:
                if (n + m) % 2 == 1:
                    return rezult[-1]
                else:
                    return (rezult[-1] + rezult[-2]) / 2

            i += 1

        while j < m:
            rezult.append(part2[j])

            if (i + j) == (n + m) // 2:
                if (n + m) % 2 == 1:
                    return rezult[-1]
                else:
                    return (rezult[-1] + rezult[-2]) / 2
            j += 1

        return 0


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    part1 = list(map(int, sys.stdin.readline().rstrip().split()))
    part2 = list(map(int, sys.stdin.readline().rstrip().split()))

    #n = 8
    #m = 10
    #part1 = [0, 0, 0, 1, 3, 3, 5, 10]
    #part2 = [4, 4, 5, 7, 7, 7, 8, 9, 9, 10]
    r = main(n, m, part1, part2)
    print(r)

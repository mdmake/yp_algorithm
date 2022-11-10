import sys

def findMedianSortedArrays(A, B):

    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2  # отступ за индексацию с 0

        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    part1 = list(map(int, sys.stdin.readline().rstrip().split()))
    part2 = list(map(int, sys.stdin.readline().rstrip().split()))

    print(findMedianSortedArrays(part1, part2))


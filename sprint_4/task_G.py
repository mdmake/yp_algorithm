import sys


def maxLengthSubarraySumToZero(A, n):

    H = dict()
    sum = 0
    maxLen = 0
    for i in range(n):
        sum = sum + 1 if A[i] > 0 else sum - 1
        if sum == 0:
            if maxLen < i:
                maxLen = i+1
        elif sum in H.keys():
            if maxLen < i-H[sum]:
                maxLen = i-H[sum]
        else:
            H[sum] = i

    return maxLen




def main():

    n = int(sys.stdin.readline().rstrip())
    data = [int(item) for item in sys.stdin.readline().rstrip().split()]

    rez = maxLengthSubarraySumToZero(data, n)

    print(rez)


if __name__ == '__main__':
    main()

import sys


def maxLengthSubarrayWithEqualCount01(A, n):

    H = dict()
    sum = 0
    maxLen = 0
    for i in range(n):
        # если 1 -- увеличиваем сумму, если 0 -- уменьшаем
        sum = sum + 1 if A[i] > 0 else sum - 1

        # если сумма нулевая, то смотрим на длину
        # если нет, то ищем нет ли такой же суммы ранеее -- если есть,
        # значит пространство между этими суммами нулевое.
        # Если ни то ни другое -- просто запоминаем эту сумму
        # то есть -- нулевую сумму проверяем на длину, для ненулевой ищем былали такая раньше,
        # и если нет -- запоминаем, если да -- смотрим расстояние до нее и сравниваем с максимумом
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

    rez = maxLengthSubarrayWithEqualCount01(data, n)

    print(rez)


if __name__ == '__main__':
    main()

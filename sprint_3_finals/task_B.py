import sys
from random import randint


def comparator(item1, item2):
    # сравниваем количество задач
    if item1[1] > item2[1]:
        return True
    elif item1[1] == item2[1]:
        # смотрим у кого меньше штраф
        if item1[2] < item2[2]:
            return True
        elif item1[2] == item2[2]:
            # выбираем лексикографический порядок
            if item1[0] < item2[0]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def comaratorInt(a,b):
    if a>b:
        return True
    else:
        return False

def partition(array, pivot, left, right):

    i = left
    j = right

    while i < j:
        if comparator(pivot, array[i]):
            i += 1
            continue
        if comparator(array[j], pivot):
            j -= 1
            continue

        array[i], array[j] = array[j], array[i]

    return array.index(pivot)

def quicksort(array, left, right):
    if left >= right:  # базовый случай,
        return  # массивы с 0 или 1 элементами фактически отсортированы
    # elif (left+1) >= right:
    #     return
    else:  # рекурсивный случай

        pivot = array[randint(left, right)]
        index = partition(array, pivot, left, right)

        r = index+1
        if r > right:
            r = right
        if r > (len(array)-1):
            r = (len(array)-1)

        l = index - 1
        if l < 0:
            l = 0
        if l < left:
            l = left

        quicksort(array, left, l)
        quicksort(array, r, right)


def main():
    n = int(sys.stdin.readline().rstrip())

    data = []
    for i in range(n):
        strData = sys.stdin.readline().rstrip().split()
        data.append((strData[0], int(strData[1]), int(strData[2])))

    quicksort(data, 0, len(data) - 1)

    for item in data[::-1]:
        print(item[0])

def test():
    d = [4, 8, 9, 20, 1, 5, 3, 10, 6, 7]
    quicksort(d, 0, len(d)-1)
    print(d)


if __name__ == "__main__":
    # print(comparator(('timofey', 4, 80), ('gena', 6, 1000)))
    main()
    # test()




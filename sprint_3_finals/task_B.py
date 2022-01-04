"""
Номер посылки 63282997

-- ПРИНЦИП РАБОТЫ --
Я реализовал эффективную быструю сортировку без использования дополнительной памяти.
Выбирается опорный элемент, и для этого элемента переупорядачивается массив таким образом,
что бы слева от опорного находились все элементы меньше опорного, а справа -- больше.
Далее сортировка рекурсивно вызывается для правого и левого подмассивов.

Принцип переупорядочивания элементов основан на приеме 'двух указателей'.
Правый (right) и левый (left) указатели изначально указывают на правый и левый концы отрезка.
Далее будем двигать левый указатель вправо до тех пор, пока он указывает на элемент, меньший опорного.
Аналогично двигаем правый указатель влево, пока он стоит на элементе, превосходящем опорный.
В итоге окажется, что что левее от left все элементы точно принадлежат первой группе, а правее от right — второй.
Далее элементы нарушающие порядок меняются местами
Процедура повторяется, пока указатели не столкнутся.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
На каждом шаге мы получаем массив упорядоченный относительно опорного элемента.
Опорный элемент разбивает массив на подмассивы.
Рекурсивно вызывая функцию сортировки для правого и левого подмассивов, пока их длина
не достигнет 0 или 1, мы получаем упорядоченный на каждом своем подмассиве массив.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В худшем случае, когда мы каждый раз будем выбирать
опорный элемента, делящий массив на подмассивы длины 0 и n-1 мы получим глубину рекурсии
O(n) и на каждом шаге будем выполнять O(n) операций по сравнению. Итого, сложность O(n^2)
В среднем случае, когда мы будем делить массив поплам глубина рекурсии будет состовлять O(log n),
на каждом уровне рекурсии мы буем проделывать O(n) операций, итого O(n log n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Массив содержит n элементов. Используется дополнительная память в виде затрат на вызов рекурсии,
пространственная сложность O(1).
"""

import sys
from random import randint
from typing import Tuple, List


def comparator(item1: Tuple[str, int, int], item2: Tuple[str, int, int]) -> bool:
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

    return False


def partition(array: List[Tuple[str, int, int]], pivot: Tuple[str, int, int], left: int, right: int):
    while left < right:
        while comparator(pivot, array[left]):
            left += 1
        while comparator(array[right], pivot):
            right -= 1
        if left >= right:
            return right
        array[left], array[right] = array[right], array[left]

    return right


def quicksort(array: List[Tuple[str, int, int]], left: int, right: int):
    if left >= right or right < 0 or left > (len(array) - 1):
        return

    pivot = array[randint(left, right)]
    index = partition(array, pivot, left, right)

    quicksort(array, left, index - 1)
    quicksort(array, index + 1, right)


def main():
    n = int(sys.stdin.readline().rstrip())

    data = []
    for i in range(n):
        strData = sys.stdin.readline().rstrip().split()
        data.append((strData[0], int(strData[1]), int(strData[2])))

    quicksort(data, 0, len(data) - 1)

    for item in data[::-1]:
        print(item[0])


if __name__ == "__main__":
    main()

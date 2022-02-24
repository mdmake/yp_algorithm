"""
Номер посылки 65482923


-- ПРИНЦИП РАБОТЫ --
Я реализовал сортировку кучей (max-heap), принцип работы сортировки:
    - считывается массив элементов, который необходимо отсортировать
    - элементы по одному вставляются в кучу (с созранением ее свойств). В результате
        работы алгоритма построения кучи, на вершине кучи находится максимальный элемент массива
    - извлекается элемент с максимальным приоритетом (первый), после чего куча перестраивается
    - процесс продолжается, пока из кучи не извлекутся все элементы

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Корректность алгоритма строится на том, что на вершине кучи (max-heap)
находится максимальный по приоритету элемент. После извлечения максимального элемента и
перестроения кучи, на вершине оказывается следующий по приоритету.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Создание кучи -- O(1) -- выделяем место под n элементов
Вставка n  элементов -- O(log1)+O(log2)+...+O(logn). Оценивая сверху, получаем O(n log n)
Извлечение элемента -- не более чем O(n log n)
Итоговая сложность -- O(1) + O(n log n) + O(n log n) ~ O(n log n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
Для писанной реализации алгоритма пирамидальной сортировки нужно выделить память под массив из
n элементов. То есть требуется O(n) дополнительной памяти.
"""


import sys
from typing import Tuple


def comparator(a: Tuple[str, int, int], b: Tuple[str, int, int]) -> bool:
    """
    Реализет сранение двух элементов
    Каждый элемент -- запись о участнике соревнования.
    Запись каждого из участников состоит из логина, количества решенных задач и штрафа.
    Сравнение реализованно следующим образом: при сравнении двух участников выше
    будет идти тот, у которого решено больше задач.
    При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
    Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше
    в алфавитном (лексикографическом) порядке.
    :param a: Первый участник
    :param b: Второй участник
    :return: Возвращает True, если первый элемент больше второго
    """
    if a[1] < b[1]:
        return False
    # при равенстве решенных задач смотрим на штрафы
    elif a[1] == b[1]:
        if a[2] > b[2]:
            return False
        elif a[2] == b[2]:
            # при равенстве штрафов смотрим на логины
            if a[0] > b[0]:
                return False
    return True


class Heap:

    def __init__(self, source, comparator):
        """
        :param source: массив исходных данных, из которых строится куча
        :param comparator: функция, определяющая отношение неравенства
                           на множестве исходных элементов
        """
        self.size = 0
        self.heap = [0] * (len(source) + 1)

        self.compare = comparator

        self.heap[0] = -1
        for key in source:
            self.heap_add(key)

    def heap_add(self, item):
        """
        Добавление элемента в кучу
        :param item: добавляемый элемент
        """

        self.size += 1
        self.heap[self.size] = item
        self.sift_up(self.size)

    def sift_up(self, idx):
        """
        Просеивание вверх
        :param idx: индекс 'просеиваемого' элемента
        """
        while idx > 1:

            parent_index = idx // 2
            if self.compare(self.heap[idx], self.heap[parent_index]):
                self.heap[parent_index], self.heap[idx] = self.heap[idx], self.heap[parent_index]
                idx = parent_index
            else:
                return

        return

    def sift_down(self, idx):
        """
        Просеивание вниз
        :param idx: индекс 'просеиваемого' элемента
        """
        while True:
            left = 2 * idx
            right = 2 * idx + 1

            if self.size < left:
                return

            if (right <= self.size) and self.compare(self.heap[right], self.heap[left]):
                index_largest = right
            else:
                index_largest = left

            if self.compare(self.heap[index_largest], self.heap[idx]):
                self.heap[idx], self.heap[index_largest] = self.heap[index_largest], self.heap[idx]
                idx = index_largest
            else:
                return

    def get_max_priority(self):
        """
        Изымает из кучи максимальный элемент и восстанавливает кучу
        :return: Возвращает максимальный элемент кучи
        """
        max_priority = self.heap[1]
        self.heap[1] = self.heap[self.size]

        self.size -= 1
        self.sift_down(1)
        return max_priority

    def heapsort(self):
        """
        Рализует пирамидалную сортировку элементов кучи
        :return: отсортированный массив элементов кучи
        """
        sorted_array = [0] * self.size
        i = 0
        while self.size > 0:
            sorted_array[i] = self.get_max_priority()
            i += 1

        return sorted_array


def main():
    arraySize = int(sys.stdin.readline().rstrip())

    data = []
    for _ in range(arraySize):
        row = sys.stdin.readline().rstrip().split()
        data.append((row[0], int(row[1]), int(row[2])))

    heap = Heap(data, comparator)
    result = heap.heapsort()

    for name, *_ in result:
        print(name)


def test():
    arr = [
        ('alla', 4, 100),
        ('gena', 6, 1000),
        ('gosha', 2, 90),
        ('rita', 2, 90),
        ('timofey', 4, 80), ]

    heap = Heap(arr, comparator)
    result = heap.heapsort()

    print(result)


if __name__ == '__main__':
    main()

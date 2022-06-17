"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.


Формат ввода

В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.
Формат вывода

Напечатайте нужные числа в возрастающем порядке через пробел.
"""

import sys


def find_neibour(n: int, m: int, data: list, x: int, y: int) -> list:
    neibhor = []

    if x > 0:
        neibhor.append(data[x - 1][y])
    if x < n - 1:
        neibhor.append(data[x + 1][y])

    if y > 0:
        neibhor.append(data[x][y - 1])
    if y < m - 1:
        neibhor.append(data[x][y + 1])

    return neibhor


def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    data = []

    for _ in range(n):
        data.append(sys.stdin.readline().rstrip().split())

    point_x = int(sys.stdin.readline().rstrip())
    point_y = int(sys.stdin.readline().rstrip())

    result = [int(item) for item in find_neibour(n, m, data, point_x, point_y)]
    result.sort()

    print(*result)


if __name__ == "__main__":
    main()



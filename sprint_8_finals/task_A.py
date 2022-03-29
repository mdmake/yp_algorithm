"""
Номер посылки 66577520


-- ПРИНЦИП РАБОТЫ --
Я реализовал расчет поиск максимального общего префикса у n строк
Строки поступают в запакованном виде, необходимо их распаковать, найти минимальный и максимальный элемент,
и найти у них общий префикс.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Распаковка требует от нас пройтись по каждому элементу строки и обработать его - O(n)
Нахождение максимальной и мимнималоьной строки -- 2*O(n)
Посимвольное сравнение двух массивов занимает O(k), где k -- длина наименьшей строки
Итого 2O(2*n + k + n) ~ O(n)


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
Алгоритму требуется дополнительная память для хранения максимальной и минимальной строк -- O(1)
"""

import sys


def unpack(s: str) -> str:
    """
    Производит распаковку рекурсивно заданной строки вида 3[a]2[r2[t]]

    :param s: запакованная строка
    :return: распакованную строку
    """

    multiplyer = []
    characters = []
    result = []
    for char in s:
        if char.isdigit():
            multiplyer.append(int(char))
        elif char == '[':
            characters.append([])
        elif char == ']':
            intermediate = ''.join(characters.pop()) * multiplyer.pop()
            if len(characters) > 0:
                characters[-1].append(intermediate)
            else:
                result.append(intermediate)
        elif len(characters) == 0:
            result.append(char)
        else:
            characters[-1].append(char)

    return ''.join(result)


def find_common_prefix(s1: str, s2: str) -> str:
    """
    Ищет наибольший общий префикс у двух строк

    :param s1: первая строка
    :param s2: вторая строка
    :return: префикс
    """

    prefix = ''
    for s1, s2 in zip(s1, s2):
        if s1 == s2:
            prefix += s1
        else:
            return prefix

    return prefix


def main():
    n = int(sys.stdin.readline().rstrip())

    min_str = ''
    max_str = ''
    for i in range(n):
        s = unpack(sys.stdin.readline().rstrip())
        if max_str == '':
            max_str = s
        if min_str == '':
            min_str = s

        if s > max_str:
            max_str = s

        if s < min_str:
            min_str = s

    result = find_common_prefix(max_str, min_str)

    print(result)


if __name__ == '__main__':
    main()

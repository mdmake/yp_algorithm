"""
Номер посылки 66483466


-- ПРИНЦИП РАБОТЫ --
Я реализовал расчет поиск максимального общего префикса у n строк
Строки поступают в запакованном виде, необходимо их распаковать, отсортировать,
и найти общий префикс у максимальной и минимальной строк.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Распаковка требует от нас пройтись по каждому элементу строки и обработать его - O(n)
Встроенная сортировка Python -- timesort -- O(n log n)
Посимвольное сравнение двух массивов занимает O(k), где k -- длина наименьшей строки
Итого O(n log n + k + n) ~ O(n log n)


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
Алгоритму timesort требуется O(n) дополнительного места
"""

import sys
from typing import List, Tuple


def unpack(s: str, i: int) -> Tuple[str, int]:
    """
    Производит распаковку текущего уровня вложенности рекурсивно заданной строки вида 3[a]2[r2[t]]

    :param s: запакованная строка
    :param i: номер символа строки, с которого мы ее обрабатываем
    :return: распакованную часть строки и позицию, на которой заканчивается уровень вложенности
    """
    rez = ''

    while i < len(s):

        if s[i].isalpha():
            rez += s[i]
        elif s[i].isdigit():
            m = int(s[i])
            r, i = unpack(s, i + 1)
            rez += m * r
        elif s[i] == '[':
            pass
        elif s[i] == ']':
            return rez, i,

        i += 1

    return rez, i


def find_common_prefix(strings: List[str]) -> str:
    """
    Ищет наибольший общий префикс у массива строк

    :param strings: массив строк
    :return: префикс
    """
    if len(strings) < 1:
        return ''
    elif len(strings) == 1:
        return strings[0]

    strings.sort()

    prefix = ''
    for s1, s2 in zip(strings[0], strings[-1]):
        if s1 == s2:
            prefix += s1
        else:
            return prefix

    return prefix


def main():
    n = int(sys.stdin.readline().rstrip())

    data = []
    for i in range(n):
        s, _ = unpack(sys.stdin.readline().rstrip(), 0)
        data.append(s)

    result = find_common_prefix(data)

    print(result)


if __name__ == '__main__':
    main()

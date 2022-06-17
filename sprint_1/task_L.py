"""
Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную букву.
Формат ввода

На вход подаются строки s и t, разделённые переносом строки. Длины строк не превосходят 1000 символов. Строки не бывают пустыми.
Формат вывода

Выведите лишнюю букву.
"""

import sys


def main():
    first = sorted(sys.stdin.readline().rstrip())
    second = sorted(sys.stdin.readline().rstrip())

    for i in range(len(first)):
        if second[i] != first[i]:
            return second[i]
    return second[-1]


if __name__ == '__main__':
    print(main())

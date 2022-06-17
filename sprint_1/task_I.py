"""
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.
Формат ввода

На вход подаётся целое число в диапазоне от 1 до 10000.
Формат вывода

Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.

"""
import sys


def if_4_degree(number: int) -> bool:
    if number == 1:
        return True

    s = str(bin(number))[3:]
    if len(s) % 2 == 0 and set(s) == set("0"):
        return True

    return False


def main():
    number = int(sys.stdin.readline().rstrip())
    print(if_4_degree(number))


if __name__ == "__main__":
    main()

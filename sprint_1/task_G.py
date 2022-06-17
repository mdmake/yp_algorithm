"""
Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. Но, кажется, она получилась не очень оптимальной.
Попробуйте написать более эффективную программу.
Не используйте встроенные средства языка по переводу чисел в бинарное представление.
"""
import sys


def to_bin(number: int) -> str:
    rezult = ""
    while number >= 2:
        rezult += str(number % 2)
        number = number // 2

    rezult += str(number)
    return rezult[::-1]


def main():
    number = int(sys.stdin.readline().rstrip())

    print(to_bin(number))


if __name__ == "__main__":
    main()

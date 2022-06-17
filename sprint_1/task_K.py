"""
Вася просил Аллу помочь решить задачу. На этот раз по информатике.
Для неотрицательного целого числа X списочная форма –— это массив его цифр слева направо. К примеру,
для 1231 списочная форма будет [1,2,3,1]. На вход подается количество цифр числа Х,
списочная форма неотрицательного числа Х и неотрицательное число K. Числа К и Х не превосходят 10000.
Нужно вернуть списочную форму числа X + K.
Формат ввода

В первой строке — длина списочной формы числа X. На следующей строке — сама списочная форма с цифрами записанными через пробел.
В последней строке записано число K, 0 ≤ K ≤ 10000.
"""
import sys


def create_number_from_list(numbers: list) -> int:
    result = 0
    for i in range(len(numbers) - 1, -1, -1):
        result += int(numbers[len(numbers) - i - 1]) * 10 ** i

    return result


def main():
    _ = sys.stdin.readline()
    listnum = sys.stdin.readline().rstrip().split()

    num = int(sys.stdin.readline().rstrip())

    print(*str(num + create_number_from_list(listnum)))


if __name__ == "__main__":
    main()

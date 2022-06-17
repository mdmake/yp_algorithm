"""
Вася делает тест по математике: вычисляет значение функций в различных точках. Стоит отличная погода, и друзья зовут Васю гулять. Но мальчик решил сначала закончить тест и только после этого идти к друзьям. К сожалению, Вася пока не умеет программировать. Зато вы умеете. Помогите Васе написать код функции, вычисляющей y = ax2 + bx + c. Напишите программу, которая будет по коэффициентам a, b, c и числу x выводить значение функции в точке x.
Формат ввода

На вход через пробел подаются числа a, x, b, c. В конце ввода находится перенос строки.
Формат вывода

Выведите одно число — значение функции в точке x.
"""

import sys


def main():
    data = sys.stdin.readline().rstrip().split()
    num = [int(item) for item in data]

    return num[0] * num[1] ** 2 + num[2] * num[1] + num[3] * num[1]


if __name__ == '__main__':
    result = main()
    print(result)

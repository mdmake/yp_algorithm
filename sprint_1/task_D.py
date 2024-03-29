"""
Метеорологическая служба вашего города решила исследовать погоду новым способом.
Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней, в которые температура строго больше, чем в
день до (если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов, то
хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.
Заметим, что если число показаний n=1, то единственный день будет хаотичным.


Формат ввода

В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105. Во второй строке даны n
целых чисел –— значения температуры в каждый из n дней. Значения температуры не превосходят 273 по модулю.
Формат вывода

Выведите единственное число — хаотичность за данный период.

Ввод
7
-1 -10 -8 0 2 0 5

Вывод
3

"""
import sys


def chaotic_weather(data: list) -> int:
    new_data = [-274, ] + data + [-274, ]
    counter = 0
    for i in range(1, len(data) + 1):
        if new_data[i - 1] < new_data[i] > new_data[i + 1]:
            counter += 1

    return counter


def main():
    _ = sys.stdin.readline()

    data = [int(item) for item in sys.stdin.readline().rstrip().split()]

    result = chaotic_weather(data)

    print(result)


if __name__ == "__main__":
    main()

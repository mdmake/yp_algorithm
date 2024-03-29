"""
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового.
После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб
по цветам. Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового.
Помогите Рите справиться с этой задачей.
Примечание: попробуйте решить задачу за один проход по массиву!
Формат ввода

В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000.
Во второй строке даётся массив, в котором указан цвет для каждого предмета.
Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.
Формат вывода

Нужно вывести в строку через пробел цвета предметов в правильном порядке.
Пример 1

Ввод Скопировать ввод	Вывод Скопировать вывод
7
0 2 1 2 0 0 1

0 0 0 1 1 2 2
"""


import sys


def calcSort(data: list[str]) -> list[int]:
	k = [0] * 3
	for item in data:
		if item == '0':
			k[0] += 1
		elif item == '1':
			k[1] += 1
		else:
			k[2] += 1

	result = [0] * k[0] + [1] * k[1] + [2] * k[2]
	return result


def calcSortNum(data: list[int]) -> list[int]:
	k = [0] * 3
	for number in data:
		k[number] += 1

	result = [0] * k[0] + [1] * k[1] + [2] * k[2]
	return result


if __name__ == "__main__":
	n = sys.stdin.readline().rstrip()
	data = sys.stdin.readline().rstrip().split()
	print(*calcSort(data))

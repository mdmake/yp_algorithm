"""
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного участка
клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой.
Для ландшафтных работ было нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок или его часть могли быть
обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными
садовниками, сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
Нужно определить границы будущих клумб.
Пример 1:
Два отрезка [7, 8] сливаются в один, но потом их
накрывает отрезок [6, 10]. Таким образом, имеем две клумбы с координатами [2,3] и [6,10].
Пример 2
Отрезки [2,3], [3, 4] и [3,4] сольются в один отрезок [2,4]. Отрезок [5,6] ни с кем не объединяется, добавляем его в ответ.

Формат ввода

В первой строке задано количество садовников n. Число садовников не превосходит 100 000.
В следующих n строках через пробел записаны координаты клумб в формате: start end, где start —– координата начала, end —– координата конца. Оба числа целые, неотрицательные и не превосходят 107. start строго меньше, чем end.
Формат вывода

Нужно вывести координаты каждой из получившихся клумб в отдельных строках. Данные должны выводится в отсортированном порядке —– сначала клумбы с меньшими координатами, затем —– с бОльшими.
Пример 1

Ввод Скопировать ввод	Вывод Скопировать вывод
4
7 8
7 8
2 3
6 10
2 3
6 10
"""

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())

    array = []
    for i in range(n):
        array.append([i] + [int(item) for item in sys.stdin.readline().rstrip().split()])

    array.sort(key=lambda x: [x[1], x[0]])

    array = [item[1:] for item in array]

    newarray = [array[0]]
    for i in range(n - 1):
        if newarray[-1][1] < array[i + 1][0]:
            newarray.append(array[i + 1])
        elif newarray[-1][1] < array[i + 1][1]:
            newarray[-1][1] = array[i + 1][1]

    for item in newarray:
        print(*item)

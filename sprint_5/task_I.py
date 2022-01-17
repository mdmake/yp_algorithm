import sys
# выбрали один элемент
# -- если элементы упорядоченны -- получаем один вариант -- NO
# -- если нет, то:
# -- если root и два чисал -> 5

# если 4:
# 1: граница (1, 4) -> 5 + 5
# 2: если внутренность 2 or 3: -> 2 + 2

# количество цифр больше, количество цифр меньше
# 0, 1 -> 1
# 2 ->  2
# 3 -> 5
# 4 -> 14

memory = {0: 1, 1: 1, 2: 2}


def generateTree(data):
    l = len(data)
    if l in memory:
        return memory[l]

    result = 0
    for pivot in data:
        left = frozenset(item for item in data if item < pivot)
        right = frozenset(item for item in data if item > pivot)

        countLeft = generateTree(left)
        countRight = generateTree(right)

        result += countLeft * countRight

    memory[l] = result
    return result


def main():
    n = int(sys.stdin.readline().rstrip())

    return generateTree(list(range(n)))


if __name__ == '__main__':
    print(main())

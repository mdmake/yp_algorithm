"""
Номер посылки


-- ПРИНЦИП РАБОТЫ --
Я реализовал двустороннюю очередь на кольцевом буфере фиксированного размера
с двумя указателями на голову и хвост очереди.
Указатель 'head' -- индекс, по которому нужно извлекать элемент, если очередь не пустая
Указатель 'tail' — индекс, по которому нужно добавлять элемент, если в очереди есть место

Реализованы методы push_back(x), push_front(x), pop_back(), pop_front().

 - push_back(x) – добавляет элемент в конец дека.
    Если в деке уже находится максимальное число элементов, выводит «error», в противном случае None.
 - push_front(value) – добавляет элемент в начало дека.
    Если в деке уже находится максимальное число элементов, выводит «error», в противном случае None.
 - pop_front() – выводит первый элемент дека и удалить его. Если дек был пуст, то выводит «error».
 - pop_back() – выводит последний элемент дека и удалить его. Если дек был пуст, то выводит «error».

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
 Алгоритм функционирует по аналогии с очередью на кольцевом буфере, но с возможностью двигать не только хвост очереди,
 но и голову. Вычисление длинны очереди на каждой операции добавления-удаления элементов позволяет
  контролировать длину очереди, не допуская перезатирания элеметов (перехлеста головы и хвоста)

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Очередь имееет фиксированную длину, выделение места стоит O(1)
Добавление в хвост и голову очереди стоит O(1),
потому что отсутствует выделение памяти, происходит присваивание элементу в ячейку уже созданного массива

Извлечение из очереди стоит в худшем случае O(1), когда выходной стек не пуст.
Итого, каждая операция стоит не более O(1), итоговая временная сложность -- O(1).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Если очередь содержит n элементов. Добавление и удаление элеметов не изменяет размер массива.
Соответственно пространственная сложность O(n).
"""

import sys


class Deque:
    def __init__(self, max_length):
        self.items = [0] * max_length
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    # add in tail
    def push_back(self, x):
        if self.size >= self.max_length:
            return 'error'
        self.items[self.tail] = x
        self.tail = (self.tail + 1) % self.max_length
        self.size += 1

    # remove from tail
    def pop_back(self):
        if self.size == 0:
            return 'error'
        index = (self.tail - 1) % self.max_length
        element = self.items[index]
        self.tail = index
        self.size -= 1
        return element

    # add to head
    def push_front(self, x):
        if self.size >= self.max_length:
            return 'error'
        index = (self.head - 1) % self.max_length
        self.items[index] = x
        self.head = index
        self.size += 1

    # remove front head
    def pop_front(self):
        if self.size == 0:
            return 'error'
        element = self.items[self.head]
        self.head = (self.head + 1) % self.max_length
        self.size -= 1
        return element


if __name__ == '__main__':
    count_command = int(sys.stdin.readline().rstrip())
    maxsize = int(sys.stdin.readline().rstrip())

    stack = Deque(maxsize)
    for i in range(count_command):
        command = sys.stdin.readline().rstrip().split()
        if 'push_back' in command:
            result = stack.push_back(int(command[1]))
        elif 'pop_back' in command:
            result = stack.pop_back()
        elif 'push_front' in command:
            result = stack.push_front(int(command[1]))
        else:
            result = stack.pop_front()

        if result is not None:
            print(result)

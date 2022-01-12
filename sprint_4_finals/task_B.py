"""
Номер посылки 63668784

-- ПРИНЦИП РАБОТЫ --
Я реализовал хэш таблицу с механизмом разрешения коллизий с помощью метода цепочек


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Количество элементов не может превышать 10^5,
Для того что бы поддерживать коэффициент заполнения на уровне alpha = 2/3
выберем в качестве количества корзин ближайшее простое число к 10^5/alpha, то есть 150001
Оптимальнее было бы использовать коэффициент заполнения 1/3, но в этом случае решение
не проходит по объему используемой памяти


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В моем алгоритме используется разрешение коллизий с помощью метода цепочек, наиболее затратная
операция -- поиск элемента в цепочке, в худшем случае O(n), в среднем -- O(1)
В этой задаче средняя временная сложность достигается за счет выбора количества корзин.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дополнительная память не используется, пространственная сложность O(1)
"""

import sys
from typing import Union


class Node:
    def __init__(self, key: int, value: int, next: Union[None, 'Node'] = None):
        self.key = key
        self.value = value
        self.next = next


class MyList:
    def __init__(self):
        self.head = None

    def find(self, key) -> Union[None, 'Node']:

        node = self.head
        while node is not None:
            if node.key == key:
                return node
            node = node.next
        return None

    def add(self, key: int, value: int):
        node = self.find(key)
        if node is None:
            buffer = self.head
            self.head = Node(key, value, buffer)
        else:
            node.value = value

    def delete(self, key: int) -> Union[None, int]:
        node = self.head

        prev = None
        while node is not None:
            if node.key == key:

                if prev is None:
                    self.head = node.next
                else:
                    prev.next = node.next
                return node.value
            prev = node
            node = node.next

        return None

    def get(self, key: int) -> Union[None, int]:
        node = self.find(key)

        if node is None:
            return None

        return node.value


class MyHashTable:
    def __init__(self, M: int):
        self.M = M
        self.data = [MyList() for _ in range(M)]

    def get(self, key: int) -> Union[None, int]:
        return self.data[self.simpleHash(key)].get(key)

    def put(self, key: int, value: int):
        self.data[self.simpleHash(key)].add(key, value)

    def delete(self, key: int) -> Union[None, int]:
        return self.data[self.simpleHash(key)].delete(key)

    def simpleHash(self, x: int) -> int:
        return x % self.M


def main():

    M = 150001

    count = int(sys.stdin.readline().rstrip())

    hashTable = MyHashTable(M)
    for i in range(count):
        command = sys.stdin.readline().rstrip().split()

        if command[0] == 'get':
            print(hashTable.get(int(command[1])))
        elif command[0] == 'put':
            hashTable.put(int(command[1]), int(command[2]))
        else:
            print(hashTable.delete(int(command[1])))


if __name__ == '__main__':
    main()

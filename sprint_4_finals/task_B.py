import sys


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyList:
    def __init__(self):
        self.head = None

    def find(self, key):

        node = self.head
        while node is not None:
            if node.key == key:
                return node
            node = node.next
        return None

    def add(self, key, value):
        node = self.find(key)
        if node is None:
            buffer = self.head
            self.head = Node(key, value, buffer)
        else:
            node.value = value

    def delete(self, key):
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

    def get(self, key):
        node = self.find(key)

        if node is None:
            return None

        return node.value


class MyHashTable:
    def __init__(self, M):
        self.M = M
        self.data = [MyList() for _ in range(M)]

    def get(self, key):
        return self.data[self.h(key)].get(key)

    def put(self, key, value):
        self.data[self.h(key)].add(key, value)

    def delete(self, key):
        return self.data[self.h(key)].delete(key)

    def h(self, x):
        return x % self.M


def main():
    M = 2  # количество корзин == максимальное число запросов * 3

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

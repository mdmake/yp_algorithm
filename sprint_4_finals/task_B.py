import sys


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyList:
    def __init__(self):
        self.head = None

    def find(self, key):
        node = self.head
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        return prev, node

    def add(self, key, value):

        prev, node = self.find(key)
        if prev is None:
            self.head = Node(key, value)
        elif node is None:
            prev.next = Node(key, value)
        else:
            node.value = value

    def delete(self, key):
        prev, node = self.find(key)

        if node is None:
            return None
        elif prev is None:
            self.head = node.next
            return node.value

        prev.next = node.next
        return node.value

    def get(self, key):
        prev, node = self.find(key)

        if node is None:
            if prev is None:
                return None
            else:
                return prev.value

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
            print(command, hashTable.get(int(command[1])))
        elif command[0] == 'put':
            hashTable.put(int(command[1]), int(command[2]))
            print(command)
        elif command[0] == 'delete':
            print(command, hashTable.delete(int(command[1])))
        else:
            pass



if __name__ == '__main__':
    main()

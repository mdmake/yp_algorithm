import sys


class MyQueueSized:
    def __init__(self, max_size):
        self.data = [None] * max_size

        self.head = 0
        self.tail = 0

        self.max_size = max_size
        self._size = 0

    def push(self, value):
        if self._size < self.max_size:
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self._size += 1
        else:
            print('error')

    def pop(self):
        if self._size == 0:
            return None

        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.max_size

        self._size -= 1

        return value

    def peek(self):
        if self.size == 0:
            return None
        return self.data[self.head]

    def size(self):
        return self._size


if __name__ == '__main__':
    count_command = int(sys.stdin.readline().rstrip())

    size = int(sys.stdin.readline().rstrip())

    queue = MyQueueSized(size)
    for i in range(count_command):
        command = sys.stdin.readline().rstrip().split()
        if 'push' in command:
            queue.push(int(command[1]))
        elif 'pop' in command:
            print(queue.pop())
        elif 'peek' in command:
            print(queue.peek())
        else:
            print(queue.size())

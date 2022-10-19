# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

def solution(node, elem):
    current = node
    pos = 0
    while current:
        if current.value == elem:
            return pos

        current = current.next_item
        pos += 1

    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node3")
    print(idx)
    assert idx == 2


if __name__ == '__main__':
    test()
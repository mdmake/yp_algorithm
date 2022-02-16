# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def getH(node):
    if node is None:
        return 0
    elif node.right is not None or node.left is not None:
        return 1 + max(getH(node.right), getH(node.left))

    else:
        return 1


def solution(root) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    return getH(root)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3
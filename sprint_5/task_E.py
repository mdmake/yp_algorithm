import sys
from typing import Optional, Tuple


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def checkSearchTree(node):
    if node is None:
        return True, None

    right, maxRightVal = checkSearchTree(node.right)
    left, maxLeftVal = checkSearchTree(node.left)

    if not (right and left):
        return False, None

    result = True
    maxValue = node.value

    if maxLeftVal is not None:
        result = result and maxLeftVal < node.value
        maxValue = max((maxValue, maxLeftVal))

    if maxRightVal is not None:
        result = result and node.value < maxRightVal
        maxValue = max((maxValue, maxRightVal))

    return result, maxValue



def solution(root) -> bool:
    result, _ = checkSearchTree(root)
    return result


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    print('case 1' * 10)
    assert solution(node5)
    node2.value = 5
    print('case 2' * 10)

    assert not solution(node5)


if __name__ == '__main__':
    test()

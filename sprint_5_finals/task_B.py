from typing import Tuple, Optional

#Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def getRightNode(node: 'Node') -> Tuple[Optional['Node'], Optional['Node']]:
    currentNode = node
    parent = None

    while currentNode.right is not None:
        parent = currentNode
        currentNode = currentNode.right

    return parent, currentNode


def getRightNodeOfLeftSubtree(node: 'Node') -> Tuple[Optional['Node'], Optional['Node']]:
    if node.left is None:
        return None, None,

    parent, fundedNode = getRightNode(node.left)

    if parent is None:
        parent = node

    return parent, fundedNode


def findNodeByKey(root, key):
    if root.value is None:
        return None, None
    if root.value == key:
        return None, root

    node = root
    parent = None
    while node.value is not None:

        if node.value == key:
            return parent, node

        if key > node.value:
            if node.right is None:
                return None, None
            parent = node
            node = node.right

        else:
            if node.left is None:
                return None, None
            parent = node
            node = node.left

    return None, None


def setNodeAsNewChild(parent: 'Node', oldChild: 'Node', newChild: Optional['Node']):
    if parent.left == oldChild:
        parent.left = newChild
    else:
        parent.right = newChild


def remove(root, key):
    # Для простоты повествования мы всегда будем брать самую правую вершину в левом поддереве.
    # При желании вы сможете адаптировать алгоритм, считая, что берётся самая левая
    # вершина в правом поддереве.
    if root is None:
        return root

    parentD, D = findNodeByKey(root, key)

    if D is None:
        return root

    # Если удаляемый нод -- лист

    if D.left is None and D.right is None:
        if parentD is None:
            return None
        else:
            setNodeAsNewChild(parentD, D, None)
            return root

    # если D не лист
    if D.right is None:
        if parentD is None:
            return D.left
        else:
            setNodeAsNewChild(parentD, D, D.left)
            return root

    elif D.left is None:
        if parentD is None:
            return D.right
        else:
            setNodeAsNewChild(parentD, D, D.right)
            return root
    else:
        parentP, P = getRightNodeOfLeftSubtree(D)
        setNodeAsNewChild(parentP, P, P.left)

        P.right = D.right
        P.left = D.left

        if parentD is not None:
            setNodeAsNewChild(parentD, D, P)
            return root
        else:
            return P


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()

# Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value

## ============================================================================================================

def getRight(node):
    if node.right is None:
        return node
    return getRight(node.right)


def getLeft(node):
    if node.left is None:
        return node
    return getLeft(node.left)


# берем самую левую вершину поддерева
def getRightNodeLS(node):
    if node.left is None:
        return None
    return getRight(node.left)


# берем самую правую вершину поддерева
def getLeftNodeRS(node):
    if node.right is None:
        return None
    return getLeft(node.right)


def findNodeByKey(root, key):
    if root is None:
        return None

    if key == root.value:
        return root
    elif key > root.value:
        return findNodeByKey(root.right, key)
    else:  # key< root.value
        return findNodeByKey(root.left, key)


## ============================================================================================================

# getRightNodeOfLeftSubtree


def getRightNodeIter(node):
    currentNode = node
    parent = None

    while currentNode.right is not None:
        parent = currentNode
        currentNode = currentNode.right

    return parent, currentNode


def getLeftNodeIter(node):
    currentNode = node
    parent = None

    while currentNode.left is not None:
        parent = currentNode
        currentNode = currentNode.left

    return parent, currentNode


def getLeftNodeRSIter(node):
    if node.right is None:
        return None, None

    parent, node = getLeftNodeIter(node.right)

    return parent, node


def getRightNodeLSIter(node):
    if node.left is None:
        return None, None,

    parent, findedNode = getRightNodeIter(node.left)

    if parent is None:
        parent = node

    return parent, findedNode


def findNodeByKeyIter(root, key):
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


def remove(root, key):
    # Для простоты повествования мы всегда будем брать самую правую вершину в левом поддереве.
    # При желании вы сможете адаптировать алгоритм, считая, что берётся самая левая
    # вершина в правом поддереве.
    if root is None:
        return root

    parentD, D = findNodeByKeyIter(root, key)

    if D is None:
        return root

    # Если удаляемый нод -- лист

    if D.left is None and D.right is None:
        if parentD is None:
            return None
        else:
            if parentD.right == D:
                parentD.right = None
            else:
                parentD.left = None

            return root

    # если D не лист
    # ищем нод на замену -- самая левая вершина в правом поддереве
    # те P.right = None

    if D.right is None:
        if parentD is None:
            return D.left
        else:
            if parentD.right == D:
                parentD.right = D.left
            else:
                parentD.left = D.left
            return root
    elif D.left is None:
        if parentD is None:
            return D.right
        else:
            if parentD.right == D:
                parentD.right = D.right
            else:
                parentD.left = D.right
            return root

    parentP, P = getRightNodeLSIter(D)

    # если справа есть поддерево и мы нашли замещающий нод
    # аккуратно заменяющий выдираем нод из дерева
    # если нод на замену -- лист

    if parentP.right == P:
        parentP.right = P.left
    else:
        parentP.left = P.left

    P.right = D.right
    P.left = D.left

    if parentD is not None:
        if parentD.right == D:
            parentD.right = P
        else:
            parentD.left = P

        return root
    else:
        return P


def test():
    # node1 = Node(None, None, 2)
    # node2 = Node(node1, None, 3)
    # node3 = Node(None, node2, 1)
    # node4 = Node(None, None, 6)
    # node5 = Node(node4, None, 8)
    # node6 = Node(node5, None, 10)
    # node7 = Node(node3, node6, 5)

    # # правая =============================================================================================
    # node1 = Node(None, None, 5)
    # node2 = Node(None, node1, 3)
    # node3 = Node(None, node2, 1)
    # newHead = remove(node3, 3)
    # assert newHead.value == 1
    # assert newHead.right.value == 5
    #
    #
    # node1 = Node(None, None, 5)
    # node2 = Node(None, node1, 3)
    # node3 = Node(None, node2, 1)
    # newHead = remove(node3, 1)
    # assert newHead is node2
    # #assert newHead.value == 1
    # assert newHead.right.value == 5
    #
    #
    # node1 = Node(None, None, 5)
    # node2 = Node(None, node1, 3)
    # node3 = Node(None, node2, 1)
    # newHead = remove(node3, 5)
    # assert newHead is node3
    # assert newHead.right.value == 3
    # assert newHead.right.right == None
    #
    # # левая =============================================================================================
    #
    # node1 = Node(None, None, 1)
    # node2 = Node(node1, None,  3)
    # node3 = Node(node2, None, 5)
    # newHead = remove(node3, 1)
    # assert newHead is node3
    # assert newHead.left.value == 3
    # assert newHead.left.left == None
    # assert newHead.left.right == None
    #
    #
    # node1 = Node(None, None, 1)
    # node2 = Node(node1, None,  3)
    # node3 = Node(node2, None, 5)
    # newHead = remove(node3, 3)
    # assert newHead is node3
    # assert newHead.left is node1
    # assert newHead.left.left == None
    #
    #
    # node1 = Node(None, None, 1)
    # node2 = Node(node1, None,  3)
    # node3 = Node(node2, None, 5)
    # newHead = remove(node3, 5)
    # assert newHead is node2
    # assert newHead.left is node1
    # assert newHead.left.value == 1
    # assert newHead.left.left == None

    # empty
    # node1 = Node(None, None, 1)
    # # node2 = Node(node1, None,  3)
    # # node3 = Node(node2, None, 5)
    # newHead = remove(node1, 5)
    # assert newHead is node1
    # assert newHead.left is None
    # assert newHead.left is None

    # ===========================================================================================
    # full tree P.parent == D
    node7 = Node(None, None, 7)
    node3 = Node(None, None, 3)
    node1 = Node(None, None, 1)

    # left
    node6 = Node(None, node7, 6)
    node2 = Node(node1, node3, 2)
    # root
    node4 = Node(node2, node6, 4)

    newHead = remove(node4, 4)
    assert newHead is node3
    assert newHead.right is node6
    assert newHead.left is node2
    # ===========================================================================================

    # ===========================================================================================
    # full tree P.parent == D
    node7 = Node(None, None, 7)
    node3 = Node(None, None, 3)
    node1 = Node(None, None, 1)

    # left
    node6 = Node(None, node7, 6)
    node2 = Node(node1, node3, 2)
    # root
    node4 = Node(node2, node6, 4)

    newHead = remove(node4, 6)
    assert newHead is node4
    assert newHead.right is node7
    # ===========================================================================================

    # ===========================================================================================
    # full tree P.parent == D
    node7 = Node(None, None, 7)
    node5 = Node(None, None, 5)
    node3 = Node(None, None, 3)
    node1 = Node(None, None, 1)

    # left
    node6 = Node(node5, node7, 6)
    node2 = Node(node1, node3, 2)
    # root
    node4 = Node(node2, node6, 4)

    newHead = remove(node4, 6)
    assert newHead is node4
    assert newHead.right is node5
    # ===========================================================================================

    # ===========================================================================================
    # full tree
    node7 = Node(None, None, 7)
    node5 = Node(None, None, 5)
    node3 = Node(None, None, 3)
    node1 = Node(None, None, 1)
    node9 = Node(None, None, 9)
    node11 = Node(None, None, 11)
    node13 = Node(None, None, 13)
    node15 = Node(None, None, 15)

    # right
    node14 = Node(node13, node15, 14)
    node10 = Node(node9, node11, 10)
    node12 = Node(node10, node14, 12)
    # left
    node6 = Node(node5, node7, 6)
    node2 = Node(node1, node3, 2)
    node4 = Node(node2, node6, 4)

    # root
    node8 = Node(node4, node12, 8)

    newHead = remove(node8, 12)
    assert newHead is node8
    assert newHead.right is node11
    assert node10.right is None
    # assert newHead.left.value == 1
    # assert newHead.left.left == None
    # ===========================================================================================

    # node4 = Node(None, None, 6)
    # node5 = Node(node4, None, 8)
    # node6 = Node(node5, None, 10)
    # node7 = Node(node3, node6, 5)

    # assert newHead.right is node5
    # assert newHead.right.value == 8

    #                 node7(5)
    #                /         \
    #           node3(1)            node6(10)
    #                 \             /
    #                node2(3)   node5(8)
    #               /           /
    #           node1(2)    node4(6)


if __name__ == '__main__':
    test()



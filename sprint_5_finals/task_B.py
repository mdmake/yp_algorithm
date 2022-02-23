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

    while currentNode.left is None:
        parent = currentNode
        currentNode = currentNode.right

    return parent, currentNode


def getLeftNodeIter(node):
    currentNode = node
    parent = None

    while currentNode.left is None:
        parent = currentNode
        currentNode = currentNode.left

    return parent, currentNode


def getLeftNodeRSIter(node):
    if node.right is None:
        return None, None

    parent, node = getLeftNodeIter(node.right)

    return parent, node


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

    parentD, D = findNodeByKeyIter(root, key)

    if D is None:
        pass
        # мы не нашли нод, кторый нужно удалять

    if parentD is None and D is not None:
        pass
        # удаляем единственный нод

    if D.left is None and D.right is None:
        if parentD.right == D:
            parentD.right = None
        else:
            parentD.left = None

        return root


    if D.left is not None:
        # ищем нод на замену
        paretnP, P = getLeftNodeRSIter(D)

        # аккуратно заменяющий выдираем нод из дерева
        if P.left is None and P.right is None:
            # нод на замену -- лист

            if paretnP.right == P:
                paretnP.right = None
            else:
                paretnP.left = None
        else:

            if paretnP.right == P:
                paretnP.right = P.left
            else:
                paretnP.left = P.left

        if parentD is not None:
            if parentD.right == P:
                parentD.right = P
            else:
                parentD.left = P

        P.right = D.right
        P.left = D.left


    if D != root:
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



"""
Номер посылки 65484165


-- ПРИНЦИП РАБОТЫ --
Я реализовал алгоритм удаления узла из бинарного дерева поиска дерева по ключу
Удаление узла работает в несколько этапов:
 - происходит поиск узла по ключу
 - происходит поиск замещающего узла
 - замещающий узел удаляется со своего места и вставляеся вместо удаляемого


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Происходит поиск узда по ключу, если узел не найден -- дерево остается неизменным.
В противном случае,мы начинаем искать замещающий узел потомках удаляемого.
Новый узел должен быть больше всех элементов в правом поддреве и меньше всех элементов в левом поддереве.
Этому условию соответствует самый правый узе левого поддерева  и самый левый узел правого поддерева
В моей реализации используется самая правую вершину в левом поддереве.
В результате такоей подстановки корректность сруктурв бинарного дерева поиска сохранется.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Поиск элемента в дереве - O(h), где h-высота дерева.
В бинарном дереве из n элементов средняя сложность поиска элемента O (log n)

PS Когда я писал про худшую сложность поиска элемента O(n), я имел ввиду, что в худшем случае бинарное
дерево будет представялть собой односвязанный список (наприме вариант, когда у кажого нода есть
только правый сосед) В этом случае поиск последнего элемента в цепочке будет занимать n сравнений - O(n)

Поиск замещающего элемента --- O(h_1), где h_1-высота левого поддерева, в среднем O(log n)

В худшем случае - O(n)
Итого, временная сложность в среднем O(log n), в худшем случае - O(n),

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
Дополнительное место не используется
"""

from typing import Tuple, Optional


# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def getRightNode(node: 'Node') -> Tuple[Optional['Node'], Optional['Node']]:
    """
    Ищет самый правый узел дерева, возвращает узел, и его родителя
    :param node: корень дерева, в котором происходит поиск
    :return: родитель, самый правый узел
    """
    currentNode = node
    parent = None

    while currentNode.right is not None:
        parent = currentNode
        currentNode = currentNode.right

    return parent, currentNode


def getRightNodeOfLeftSubtree(node: 'Node') -> Tuple[Optional['Node'], Optional['Node']]:
    """
    Ищет самый правый узел левого поддерева и его родителя
    :param node: корень дерева
    :return: родитель, самый правый узел левого поддерева
    """
    if node.left is None:
        return None, None,

    parent, fundedNode = getRightNode(node.left)

    if parent is None:
        parent = node

    return parent, fundedNode


def findNodeByKey(root, key):
    """
    Ищет в дереве узел, значение которого соответствует ключу. Если такого узла нет, возвращется None
    :param root: корень дерева, в котром происхдит поиск
    :param key: ключ по которому происхоит поиск
    :return: родитель найденного узла, найденный узел
    """
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
    """
    Проверяет, является ли потомок правым или левым потомком своего родителя, и заменяется новым значением.
    :param parent: родитель
    :param oldChild: потомок
    :param newChild: новый потомок
    """
    if parent.left == oldChild:
        parent.left = newChild
    else:
        parent.right = newChild


def remove(root, key):
    """
    Удаляет по ключу узел из дерева
    :param root: корень дерева, из котрого мы удаляем узел
    :param key: ключ, по которому ищется удаляемый узел
    :return: корень получившегося дерева
    """
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

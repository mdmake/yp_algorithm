# from node import Node

#Comment it before submitting
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value



def insert(root, key):
    node = insert_node(root, key)
    return root

def insert_node(root, key):

    if key < root.value:
        if root.left is None:
            root.left = Node(None, None, key)
            #return root.left
        else:
            insert_node(root.left, key)
    else:# key >= root.value:
        if root.right is None:
            root.right = Node(None, None, key)
            #return root.right
        else:
            insert_node(root.right, key)



#
# def insert(root, key):
#     #  Your code
#     #  “ヽ(´▽｀)ノ”
#     pass


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
#Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left



def getEven(node):
    if node is None:
        return 0, True
    elif node.right is not None or node.left is not None:

        rl, re = getEven(node.right)
        ll, le = getEven(node.left)
        return 1 + max(rl, ll),  re and le and abs(rl-ll) < 2

    else:
        return 1, True



def solution(root):
    #  Your code
    #  “ヽ(´▽｀)ノ”
    _, balansed = getEven(root)

    return balansed



def test():
    node0 = Node(6)
    node1 = Node(1, node0, None)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)


    assert solution(node5)



if __name__ == '__main__':
    test()
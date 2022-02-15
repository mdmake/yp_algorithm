
class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def findNode(root, l):
    node = root
    path = [root, ]

    while True:

        if node.value == l:
            pass


def print_LMR(vertex):
  if vertex.left != None:
      print_LMR(vertex.left)
  print(vertex.value, end=' ')
  if vertex.right != None:
      print_LMR(vertex.right)


def print_LMR_check(vertex, dset, L, R):

  if vertex.left != None:
      print_LMR_check(vertex.left, dset, L, R)

  if vertex in dset and R > vertex.value >= L:
    print(vertex.value, end=' ')
  elif L < vertex.value < R:
    print(vertex.value, end=' ')
  else:
    return

  if vertex.right != None:
      print_LMR_check(vertex.right,  dset, L, R)




def print_RML(vertex):
    if vertex.right != None:
        print_RML(vertex.right)
    print(vertex.value, end=' ')
    if vertex.left != None:
        print_RML(vertex.left)



st = list()

def findNode(node, value):


    if node is None or node.value is None:
        print(None)
        return None

    if node.value >= value:
        st.append(node)
    print(node.value)

    if node.value < value:

        result = findNode(node.right, value)
    else:
        result = findNode(node.left, value)

    # если решение не найдено в левом или правом поддереве:
    if result is None:
        if node.value is None:
            return None
        else:
            if node.value < value:
                return None
            return node, node.value
    else:
        return result




def print_range(node, l, r):
    #  Your code

    if node is None:
        return

    if node.value < l:
        print_range(node.right, l, r)
    elif node.value > r:
        print_range(node.left, l, r)
    else:
        print_range(node.left, l, r)
        print(node.value)
        print_range(node.right, l, r)





def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node31 = Node(None, None, 8)

    node4 = Node(node31, node3, 8)

    node5 = Node(node4, None, 9)
    node11 = Node(None, None, 11)
    node6 = Node(node5, node11, 10)
    node7 = Node(node2, node6, 5)

    # print_LMR(node7)
    # print()
    # print_RML(node7)
    # print()
    # print_range(node7, 2, 8)

    print_range(node7, 2, 8)


    # print(node, v)
    # for item in st:
    #     print(item)







if __name__ == '__main__':
    test()

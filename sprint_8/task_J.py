import sys
from collections import defaultdict


# 0: {b: 5, c: 9, a: 1}
class Tree:
    def __init__(self):
        self.root = Node(0, '')
        self.maxn = 1
        self.nd = {0: self.root, }


class Node:
    def __init__(self, num, letter):
        self.num = num
        self.letter = letter
        self.is_final = False
        self.edge = defaultdict(dict)


def is_pattern_in_tree(tree, pattern):
    current_node = tree.root
    for i in range(0, len(pattern)):
        symbol = pattern[i]
        if symbol in current_node.edge.keys():
            current_node = tree.nd[current_node.edge[symbol]]
        else:
            return False

    return True


def add_string(tree, string: str):
    current_node = tree.root

    for i in range(0, len(string)):
        symbol = string[i]  # На каждом шаге работаем с одним символом.

        if symbol not in current_node.edge.keys():
            current_node.edge[symbol] = tree.maxn
            tree.nd[tree.maxn] = Node(tree.maxn, symbol)
            current_node = tree.nd[tree.maxn]
            tree.maxn += 1

        else:
            current_node = tree.nd[current_node.edge[symbol]]

        # Сдвинуться на следующий символ.
    return tree


def returnName(tree, root):

    current_node = root

    string = []

    for k, v in current_node.edge.items:
        string.append(k + returnName(tree, tree.nd[v]))

    return string



def add_ac(tree, pattern):

    current_node = tree.root

    for i in range(0, len(pattern)):
        current_node = tree.nd[current_node.edge[pattern[i]]]

    start_node = current_node

    return returnName(tree, start_node)








def main():
    n = int(sys.stdin.readline().rstrip())
    classes = defaultdict(list)

    for i in range(n):
        s = sys.stdin.readline().rstrip()
        k = ''.join(c for c in s if c.isupper())
        classes[k].append(s)

    m = int(sys.stdin.readline().rstrip())
    patterns = []
    for i in range(m):
        patterns.append(sys.stdin.readline().rstrip())

    tree = Tree()

    for k in classes.keys():
        add_string(tree, k)

    for pattern in patterns:
        if is_pattern_in_tree(tree, pattern):
            rez = add_ac(tree, pattern)
            print(rez)
        else:
            print('')



if __name__ == '__main__':
    main()

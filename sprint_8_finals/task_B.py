"""
Номер посылки 66484531


-- ПРИНЦИП РАБОТЫ --
Создаем префиксное дерево, в терминальных узлах будем хранить длину добавленного слова
Префиксное дерево хранит максимальное количество нодов
Потом строим динамику, в каждом элементе массива dp будем хранить, можно ли создать строку с s[:i] из
слов шпаргалки

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Создание бора из n строк -- O(L), где L -- суммарная длина строк
Ребра хранятся в хэш-таблице, доступ к ребру -- O(1)
Для перебора по префиксному дереву в динамике -- сложность O(m*n), где m - длина шпаргалки, n -- количество строк
Итого O(m*n + L) Так как суммарная длина строк пропорциональна их количеству k, можно сказать
что итоговая сложность -- O(m*n + k*n) = O((m+k)*n)


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
Требуется дополнительное место для хранения списка ребер -> O(n⋅∣Σ∣), и для хранения массива нодов, O(n)
Итого -- O(n⋅∣Σ∣)
"""

import sys


class Trie:
    def __init__(self):
        # указатель на корень
        self.root = Node()

        # хеш с нодами по номеру
        self.nd = {0: self.root, }

    @property
    def maxN(self):
        return len(self.nd)

    def add_node(self):
        self.nd[self.maxN] = Node()
        return self.nd[self.maxN - 1]


class Node:
    def __init__(self):
        self.is_final = False
        self.edge = dict()
        self.word_length = 0


def add_pattern_to_tree(trie: 'Trie', string: str) -> 'Trie':
    """
    Добавляет строку в бор

    :param trie: бор
    :param string: строка, которую добавляем
    :return: обновленный бор
    """
    current_node = trie.root

    for i in range(0, len(string)):
        symbol = string[i]

        if symbol not in current_node.edge.keys():
            current_node.edge[symbol] = trie.maxN
            current_node = trie.add_node()
        else:
            current_node = trie.nd[current_node.edge[symbol]]

    current_node.word_length = len(string)
    current_node.is_final = True
    return trie


def is_splitting_possible(tree: 'Trie', s: str) -> bool:
    """
    Вычисляет, можно ли разбить строку на слова из словаря

    :param tree: бор
    :param s: строка
    :return: True, если можно, False  в противном случае
    """
    dp = [False] * (len(s) + 1)
    dp[0] = True

    node = tree.root
    for i in range(len(dp)):
        offset = 0
        while i + offset < len(dp):
            if node.is_final and dp[i + offset - node.word_length]:
                dp[i + offset] = True
            if i + offset == len(s) or not node.edge.get(s[i + offset], False):
                node = tree.root
                break
            node = tree.nd[node.edge[s[i + offset]]]
            offset += 1

    return dp[-1]


def main():
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    tree = Trie()
    for _ in range(n):
        add_pattern_to_tree(tree, sys.stdin.readline().rstrip())

    result = is_splitting_possible(tree, s)

    if result:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

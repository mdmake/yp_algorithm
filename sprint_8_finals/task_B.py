import sys
from collections import defaultdict


class Tree:
    def __init__(self):
        # указатель на корень
        self.root = Node(0, '')

        # количество нодов
        self.maxn = 1

        # хеш с нодами по номеру
        self.nd = {0: self.root, }


class Node:
    def __init__(self, num, letter):
        self.num = num
        self.letter = letter
        self.is_final = False
        self.edge = defaultdict(dict)
        self.word = None


def add_pattern_to_tree(tree, string: str):
    current_node = tree.root

    for i in range(0, len(string)):
        symbol = string[i]

        if symbol not in current_node.edge.keys():
            current_node.edge[symbol] = tree.maxn
            tree.nd[tree.maxn] = Node(tree.maxn, symbol)
            current_node = tree.nd[tree.maxn]
            tree.maxn += 1

        else:
            current_node = tree.nd[current_node.edge[symbol]]

    current_node.word = string
    current_node.is_final = True
    return tree


def find_any(tree, text):
    # построить префиксное дерево trie по набору шаблонов patterns
    finding = []
    for pos in range(0, len(text)):  # Перебираем стартовые позиции.
        # Начинаем с корня бора.
        current_node = tree.root
        # Перебираем символы шаблона, начиная со стартовой позиции.
        offset = 0
        mismatch_not_found = True  # Расхождений с шаблоном пока не найдено.
        while mismatch_not_found and (pos + offset) < len(text):
            symbol = text[pos + offset]
            if symbol in current_node.edge.keys():

                # Сдвинуться на следующий символ.
                current_node = tree.nd[current_node.edge[symbol]]
                if current_node.is_final:
                    # return pos, current_node.word
                    finding.append((pos, current_node.word))
                    mismatch_not_found = False

                offset += 1

            else:  # Подходящее ребро отсутствует.
                # Найдено разночтение, мы должны завершить сканирование шаблона
                #   на текущей стартовой позиции. Внутренний цикл прервётся.
                # Работа на этом не заканчивается:
                #   будет взята следующая стартовая позиция.
                mismatch_not_found = False
    # Ни на одной стартовой позиции мы не дошли до терминального узла,
    #   значит, шаблон не найден.
    return finding


def main():
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    patterns = []
    tree = Tree()
    for _ in range(n):
        patterns.append(sys.stdin.readline().rstrip())
        add_pattern_to_tree(tree, patterns[-1])

    # pos_word = find_any(tree, s)
    # print(pos_word)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    node = tree.root
    for i in range(len(dp)):
        offset = 0
        while i + offset < len(dp):
            if node.is_final and dp[i + offset - len(node.word)]:
                dp[i + offset] = True
            if (i + offset == len(s) or not node.edge.get(s[i + offset], False)):
                node = tree.root
                break
            node = tree.nd[node.edge[s[i + offset]]]
            offset += 1

    if dp[-1]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

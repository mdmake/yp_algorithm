# A. Генератор скобок

import sys


def generateBracketSequence(data, openBracket, closeBracket):
    if openBracket + closeBracket == 0:
        print(data)
        return

    if openBracket == 0:
        generateBracketSequence(data + ')', openBracket, closeBracket - 1)
    elif closeBracket == 0 or openBracket >= closeBracket:
        generateBracketSequence(data + '(', openBracket - 1, closeBracket)
    else:
        generateBracketSequence(data + '(', openBracket - 1, closeBracket)
        generateBracketSequence(data + ')', openBracket, closeBracket - 1)


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    generateBracketSequence('', n, n)

"""
Формат ввода

В первой строке записана строка s.
Во второй —- строка t.
Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки могут быть пустыми.
Формат вывода

Выведите True, если s является подпоследовательностью t, иначе —– False.
Пример 1

Ввод Скопировать ввод	Вывод Скопировать вывод
abc
ahbgdcu
True

"""


import sys


def subSequence(s, t):
    i = 0
    j = 0
    l_s = len(s)
    l_t = len(t)

    if l_s == 0:
        return True

    if l_s > l_t:
        return False

    while i < l_s and j < l_t:
        if s[i] == t[j]:
            i += 1
        j += 1
        if i == l_s:
            return True

    if i == l_s:
        return True
    else:
        return False


if __name__ == '__main__':
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    print(subSequence(s, t))
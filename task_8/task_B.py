import sys


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    n = len(s1)
    m = len(s2)

    if abs(n - m) > 1:
        print('FAIL')
        return

    i = 0
    j = 0
    counter = 0
    while i < n and j < n:
        if s1[i] != s2[j]:
            # замена
            if len(s1[i + 1:]) == len(s2[j + 1:]):
                counter += 1
            # удаление
            elif len(s1[i + 1:]) > len(s2[j + 1:]):
                counter += 1
                i += 1
            # вставка
            else:
                counter += 1
                j += 1

        i += 1
        j += 1

        if counter >= 2:
            print('FAIL')
            return

    print('OK')


if __name__ == '__main__':
    main()

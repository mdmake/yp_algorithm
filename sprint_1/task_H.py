"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе. Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.
Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.
Формат ввода

Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.
Формат вывода

Одно число в двоичной системе счисления.

"""

import sys

def bin_summ_cool():
    # Python program to add two binary numbers.

    # Driver code
    # Declaring the variables
    a = "1101"
    b = "100"
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    # Initialize the result
    result = ''

    # Initialize the carry
    carry = 0

    # Traverse the string
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        # Compute the carry.
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    print(result.zfill(max_len))



def bin_summ(a: str, b: str) -> str:
    if len(a) > len(b):
        s, l = b, a
    else:
        s, l = a, b

    s = "0" * (len(l) - len(s) + 1) + s
    l = "0" + l

    rez = ""
    prev = 0
    for lb, sb, in zip(l[::-1], s[::-1]):
        current_sum = prev + int(lb) + int(sb)
        rez += str(current_sum % 2)
        prev = current_sum // 2

    rez = rez[::-1]
    return rez if rez[0] == "1" else rez[1:]


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    print(bin_summ(a, b))


if __name__ == "__main__":
    main()

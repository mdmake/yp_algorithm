"""
Помогите Васе понять, будет ли фраза палиндромом‎. Учитываются только буквы и цифры, заглавные
и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.
Формат ввода

В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит
20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

"""
import sys


def is_palyndrom(data: str) -> bool:
    i = 0
    j = len(data) - 1
    while i < j:
        if not data[i].isalnum():
            i += 1
            continue
        if not data[j].isalnum():
            j -= 1
            continue
        if data[i] != data[j]:
            return False

        i += 1
        j -= 1

    return True


def main():
    _ = sys.stdin.readline()
    data = sys.stdin.readline().lower()

    print(is_palyndrom(data))


if __name__ == "__main__":
    main()

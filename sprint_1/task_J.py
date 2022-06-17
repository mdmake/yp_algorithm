"""
Основная теорема арифметики говорит: любое число раскладывается на произведение простых множителей единственным образом,
с точностью до их перестановки. Например:
Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.
Напишите программу, которая производит факторизацию переданного числа.
Формат ввода

В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.
Формат вывода

Выведите в порядке неубывания простые множители, на которые раскладывается число n.
"""
import sys


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


def factoristaion(number):
    primes, _ = get_least_primes_linear(number)

    deliteli = []
    for i, prime in enumerate(primes):
        while number % prime == 0:
            number = number // prime
            deliteli.append(prime)

    return deliteli


def main():
    number = int(sys.stdin.readline().rstrip())

    print(*factoristaion(number))


if __name__ == "__main__":
    main()

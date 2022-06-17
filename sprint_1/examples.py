import sys


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False

    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n, num):
                numbers[j] = False

    return numbers

def eratosthenes_2(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False

    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n, num):
                numbers[j] = False

    return numbers


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


def main():
    n = int(sys.stdin.readline().rstrip())
    result = eratosthenes_2(n)
    print(result)
    result = get_least_primes_linear(n)
    print(*result)


if __name__ == "__main__":
    main()

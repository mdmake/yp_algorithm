import sys

# https://stackoverflow.com/questions/14133806/why-is-powa-d-n-so-much-faster-than-ad-n
# кратко: pow(a, r-l+1, m) в 5 раз быстрее (a ** (r-l+1) % m
def gornerHash(s, a, m):

    if len(s) < 1:
        return 0

    rez = ord(s[0])

    for i in range(1, len(s)):
        rez = (rez * a + ord(s[i])) % m

    return rez % m


def gornerHashList(s, a, m):

    if len(s) < 1:
        return 0

    rez = [0, ord(s[0]), ]

    for i in range(1, len(s)):
        rez.append((rez[-1] * a + ord(s[i])) % m)

    return rez


def main():
    a = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    hashes = gornerHashList(s, a, m)

    for i in range(n):
        l, r = (int(item) for item in sys.stdin.readline().rstrip().split())

        hash_r_l = hashes[r] - (hashes[l-1] * pow(a, r-l+1, m))

        print(hash_r_l % m)


if __name__ == '__main__':
    main()


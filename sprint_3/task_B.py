import sys

keys = {
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def combination(key, sequence, data):
    if len(key) == 0:
        return sequence

    rez = ''
    for item in data[key[0]]:
        rez += ' ' + combination(key[1:], sequence + item, data)
    return rez[1:]


if __name__ == '__main__':
    keySequence = [int(item) for item in list(sys.stdin.readline().rstrip())]
    print(combination(keySequence, '', keys))
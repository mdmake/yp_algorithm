import sys


# если левый больше чем правый -- возвращаем True
def more(n1, n2):

    for i, j in zip(list(n1), list(n2)):
        if i < j:
            return 0
        elif i > j:
            return 1

    if len(n1) == len(n2):
        return 1
    if len(n1) > len(n2):
        secondPart = n1[len(n2):]
        return more(secondPart, n2)

    elif len(n1) < len(n2):
        secondPart = n2[len(n1):]
        return more(n1, secondPart)

    return 0



def wiseSort(data):
    for i in range(1, len(data)):
        itemToInsert = data[i]

        j = i

        while j > 0:
            rez = more(itemToInsert, data[j-1])
            if rez == 0:
                break
            elif rez == 1:
                data[j] = data[j - 1]
                j -= 1
            else:
                secondPart = itemToInsert[len(data[j-1]):]
                if len(secondPart) == 0:
                    data[j] = data[j - 1]
                    j -= 1
                else:
                    data[j] = data[j - 1]
                    j -= 1

        data[j] = itemToInsert


if __name__ == "__main__":

    n = sys.stdin.readline().rstrip()
    data = sys.stdin.readline().rstrip().split()
    #data = ['83', '8', '9', '6', '63', '6']
    wiseSort(data)

    print(''.join(data))
    #print(data)
import sys


def main():
    databaseDocumentCount = int(sys.stdin.readline().rstrip())

    databaseIndex = []
    # Для каждого документа в БД составляем словарь {слово: количество упоминаний в документе}
    for i in range(databaseDocumentCount):
        countDict = dict()
        for word in sys.stdin.readline().rstrip().split():
            if word not in countDict:
                countDict[word] = 1
            else:
                countDict[word] += 1

        databaseIndex.append(countDict)


    requestCount = int(sys.stdin.readline().rstrip())
    # для каждого запроса
    for i in range(requestCount):
        request = set(sys.stdin.readline().rstrip().split())
        # Для каждого запроса считаем релевантность текстов в БД
        rez = []
        for i, index in enumerate(databaseIndex):
            rez.append([i, 0])
            for word in request:
                rez[-1][1] += index.get(word, 0)

        rez.sort(key=lambda x: x[1], reverse=True)

        print(*[item[0]+1 for item in rez[:5] if item[1] > 0])

if __name__ == '__main__':
    main()

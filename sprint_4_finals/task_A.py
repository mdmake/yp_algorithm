import sys


def main():
    databaseDocumentCount = int(sys.stdin.readline().rstrip())

    db = []
    for i in range(databaseDocumentCount):
        db.append(sys.stdin.readline().rstrip().split())

    mdict = dict()
    for i, record in enumerate(db):
        for word in record:
            if word not in mdict:
                mdict[word] = {i: 0 for i in range(databaseDocumentCount)}
            mdict[word][i] += 1


    requestCount = int(sys.stdin.readline().rstrip())
    # для каждого запроса

    for i in range(requestCount):
        rez = [[i, 0] for i in range(databaseDocumentCount)]

        request = set(sys.stdin.readline().rstrip().split())
        # Для каждого запроса считаем релевантность текстов в БД
        for word in request:
            if word in mdict:
                for i in range(databaseDocumentCount):
                    rez[i][1] += mdict[word][i]


        rez.sort(key=lambda x: x[1], reverse=True)

        print(*[item[0]+1 for item in rez[:5] if item[1] > 0])

if __name__ == '__main__':
    main()

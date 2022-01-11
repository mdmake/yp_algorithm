import sys

def main():
    databaseDocumentCount = int(sys.stdin.readline().rstrip())

    mdict = dict()
    for i in range(databaseDocumentCount):
        record = sys.stdin.readline().rstrip().split()
        for word in record:
            if word not in mdict:
                mdict[word] = {i: record.count(word)}
            mdict[word][i] = record.count(word)

    requestCount = int(sys.stdin.readline().rstrip())

    #dbrequest = dict()
    dbwordrequest = dict()
    for _ in range(requestCount):

        request = frozenset(sys.stdin.readline().rstrip().split())

        #if request not in dbrequest:
            # этот запрос еще никогда не обрабатывался
            # готовим структуру для релевантности
        rez = {i: 0 for i in range(databaseDocumentCount)}
        for word in request:
            # если слово вообще есть в текстах
            if word in mdict:
                # смотрим для каждого слова
                # 1-- мы еще никогда не искали это слово по всем текстам
                # 2 -- уже искали и запомнили

                # заполняем словарик
                if word not in dbwordrequest:
                    dbwordrequest[word] = dict()
                    if word in mdict:
                        for k in mdict[word]:
                            dbwordrequest[word][k] = mdict[word][k]
                #  берем данные из словарика
                for k in dbwordrequest[word]:
                    rez[k] += dbwordrequest[word][k]

        print(*[ky+1 for ky in sorted(rez, key=rez.get, reverse=True)[:5] if rez[ky] > 0])


if __name__ == '__main__':
    main()

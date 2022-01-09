import sys


def main():
    databaseDocumentCount = int(sys.stdin.readline().rstrip())

    databaseDocuments = []
    for i in range(databaseDocumentCount):
        databaseDocuments.append([item for item in sys.stdin.readline().rstrip().split()])

    databaseIndex = []
    for sentence in databaseDocuments:
        databaseIndex.append({word: sentence.count(word) for word in sentence})

    requestCount = int(sys.stdin.readline().rstrip())
    requests = []
    for i in range(requestCount):
        requests.append({item for item in sys.stdin.readline().rstrip().split()})

    for request in requests:
        rez = dict()
        for i, index in enumerate(databaseIndex):
            s = sum([index.get(word, 0) for word in request])
            if s in rez:
                rez[s].append(i+1)
            else:
                rez[s] = [i+1, ]


        rezForPrint = []
        for k in sorted(rez.keys(), reverse=True):
            if k > 0:
                for item in rez[k]:
                    rezForPrint.append(item)

        print(*rezForPrint[:5])

if __name__ == '__main__':
    main()
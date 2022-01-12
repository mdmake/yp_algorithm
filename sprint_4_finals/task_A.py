"""
Номер посылки 63668674

-- ПРИНЦИП РАБОТЫ --
Я реализовал поисковую систему (трепещи, Google), которая:
 - считывает n документов
 - строит по этим документам поисковый индекс
 - считывает m запросов
 - вычисляет релевантность каждого документа для каждого запроса
 - выводит порядковые номера 5 документов с максимальной релеавтностью для каждого запроса

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
В качестве поискового индекса строится словарь -- хеш-массив вида
{
    слово_1 : {документ_1: число_вхождений_слова_1_в_документ_1, документ_2: число_вхождений_слова_1_в_документ_2, ...}
    слово_2 : {документ_1: число_вхождений_слова_2_в_документ_1, документ_2: число_вхождений_слова_2_в_документ_2, ...}
    ...
    слово_k : {документ_1: число_вхождений_слова_k_в_документ_1, документ_2: число_вхождений_слова_2_в_документ_2, ...}
}
где каждому слову соответствует количество вхождений этого слова в каждый из документов.
В целях экономии места если слово_k не входит в документ_l, запись документ_l: 0 по ключу 'слово_k' не создается

Далее происходит считывание n запросов. Для каждого уникального слова в запросе считается релевантность
по всем документам, полученные значения хешируются, для того, чтобы при появлении этого-же слова в
новом запросе расчет не происходил заново.
Далее высчитывается суммарная релевантность документов по всем словам запроса и
выводятся порядковые номера документов с самой высокой релевантностью.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Записываем в словарь каждое слово каждого документа -- O(k*m), ,
где
m -- количество документов,
к -- количество слов в самом длинном документе
Проходим по каждому слову каждого запроса, по каждому слову в документах  -- O(p*n*k),
где
p -- количество слов в запросе,
n -- количество запросов
Количество слов в документах конечно, количество слов в запросах конечно.
Итоговая сложность -- O(k*m + p*n*k) ~ O(N)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Используется дополнительная память для хранения:
 - хэш-массив индекса занимает O(k*m), где m -- количество документов, к -- количество слов в самом длинном документе
 - хеш-массив посчитаной релевантность для слов в запросе занимает до O(p*n), где p -- количество слов в запросе, n -- количество запросов
Итого O(k*m + p*n)
Количество слов в документах конечно, количество слов в запросах конечно.
Итоговая сложность линейн зависит от количества документов и количества запроов ~ O(N)
"""

import sys
from typing import List, Dict, FrozenSet


def createIndex(count: int) -> Dict[str, Dict[int, int]]:
    index = dict()
    for i in range(count):
        record = sys.stdin.readline().rstrip().split()
        for word in record:
            if word not in index:
                index[word] = {i: record.count(word)}
            index[word][i] = record.count(word)
    return index


def processRequest(
    request: FrozenSet[str],
    index: Dict[str, Dict[int, int]],
    documentCount: int,
    requestsWordHash: Dict[str, Dict[int, int]],
) -> List[int]:

    rez = {i: 0 for i in range(documentCount)}
    for word in request:
        # если слово вообще есть в текстах
        if word in index:

            # если мы еще никогда не искали это слово по всем текстам
            # то заполняем словарик
            if word not in requestsWordHash:
                requestsWordHash[word] = dict()
                if word in index:
                    for k in index[word]:
                        requestsWordHash[word][k] = index[word][k]

            #  берем данные из словарика
            for k in requestsWordHash[word]:
                rez[k] += requestsWordHash[word][k]

    return [
        item + 1 for item in sorted(rez, key=rez.get, reverse=True)[:5] if rez[item] > 0
    ]


def main():
    databaseDocumentCount = int(sys.stdin.readline().rstrip())

    index = createIndex(databaseDocumentCount)

    requestCount = int(sys.stdin.readline().rstrip())
    dbWordsRequest = dict()

    for _ in range(requestCount):
        request = frozenset(sys.stdin.readline().rstrip().split())

        result = processRequest(request, index, databaseDocumentCount, dbWordsRequest)
        print(*result)


if __name__ == "__main__":
    main()

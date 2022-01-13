"""
Номер посылки 63767478

-- UPDATE --
Узким место в программе является массива релеавтностей запроса каждому из документов.
Вместо того чтобы сортировать весь массив со сложностью O(n logn) можно возмользоваться алгоритмом
quickselect, который позволяет найти 5-ый минимальный/максимальный элемент со средней сложностью O(n)
После применения алгоритма к массиву, достаточно будет будет необходимо отсортировать оставшиеся 4 элемента
так как quickselect гарантирует что элементы справа больше чем 5-ый, но не гарантирует что он идет по порядку,
сложность -- О(1)
Для реализации алгоритма я использовал https://en.wikipedia.org/wiki/Quickselect
и https://www.geeksforgeeks.org/quickselect-algorithm/


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

import random
import sys
from typing import Tuple, List


def comparator(a: Tuple[int], b: Tuple[int]) -> bool:
    if a[1] > b[1]:
        return True
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return True
    return False


def partition(data: List[Tuple[int]], left: int, right: int) -> int:
    pivotIndex = random.randint(left, right)
    pivot = data[pivotIndex]
    data[right], data[pivotIndex] = data[pivotIndex], data[right]
    i = left - 1
    for j in range(left, right):
        if comparator(data[j], pivot):
            i += 1
            # if j > i:
            # print(f'swap A[{i}] and A[{j}]')
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[right] = data[right], data[i + 1]
    return i + 1


def quickSelectKMaxSublist(data: List[Tuple[int]], K: int, left: int, right: int) -> List[Tuple[int]]:

    if K > right-1:
        return data

    while left < right:
        pivotIndex = partition(data, left, right)

        if K == pivotIndex:
            return data[:K + 1]
        if K < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1

    return data[:K + 1]


def main():
    databaseDocumentCount = int(sys.stdin.readline().rstrip())

    index = dict()
    for i in range(databaseDocumentCount):
        record = sys.stdin.readline().rstrip().split()

        for word in record:
            buffer = index.get(word, {})
            buffer[i] = buffer.get(i, 0) + 1
            index[word] = buffer

    requestCount = int(sys.stdin.readline().rstrip())

    requestCach = {}
    for _ in range(requestCount):

        request = frozenset(sys.stdin.readline().rstrip().split())

        if request not in requestCach:
            result = {}
            for word in request:
                for document, count in index.get(word, {}).items():
                    result[document] = count + result.get(document, 0)

            resultList = list(result.items())
            kSorted = quickSelectKMaxSublist(resultList, 4, 0, len(resultList) - 1)
            finalResult = [item[0] + 1 for item in sorted(kSorted[:5], key=lambda x: (-x[1], x[0]))]
            requestCach[request] = finalResult
        else:
            finalResult = requestCach[request]


        print(*finalResult)


if __name__ == "__main__":
    main()

import sys

# Тимофей решил сортировать таблицу результатов следующим образом:
# при сравнении двух участников выше будет идти тот, у которого решено больше задач.
# При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
# Если же и штрафы совпадают, то первым будет тот,
# у которого логин идёт раньше в алфавитном (лексикографическом) порядке.
# alla 4 100
# логин задачи штрафы
# comparatorAMoreThenB
def comparator(a, b)->bool:
    if a[1]<b[1]:
        return False
    # при равенстве решенных задач смотрим на штрафы
    elif a[1] == b[1]:
        if a[2] > b[2]:
            return True
        elif a[2] == b[2]:
            # при равенстве штрафов смотрим на логины
            if a[0] > b[0]:
                return False
    return True

def sift_down(heap, idx):
    # получли левого и правого потомков
    left = 2 * idx
    right = 2 * idx + 1

    size = len(heap) - 1  # size = 6

    if size < left:
        return idx

    if (right <= size) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    else:
        return idx


def sift_up(heap, idx):
    if idx == 1:
        return idx

    parent_index = idx // 2
    if heap[parent_index] < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)
    else:
        return idx

def heap_add(heap, key):
    size = len(heap) - 1

    index = size + 1
    heap.append(key)
    sift_up(heap, index)


def heap_get_max_priority(heap):
    size = len(heap) - 1

    result = heap[1]
    heap[1] = heap[size]
    heap = heap[:-1]
    # heap.size -= 1
    sift_down(heap, 1)
    return heap, result



def heapsort(array):
#   # Создадим пустую бинарную кучу.
    heap = [-1, ]
#
#   # Вставим в неё по одному все элементы массива, сохраняя свойства кучи.
#   для каждого элемента item из массива array:
    for item in array:
        heap_add(heap, item)   # псевдокод для heap_add можно посмотреть в прошлом уроке
#
#   # Будем извлекать из неё наиболее приоритетные элементы, удаляя их из кучи.
    sorted_array = [0]*len(heap)
    i = 0
#   до тех пор, пока куча не пуста:
    while len(heap) > 1:
        heap, sorted_array[i] = heap_get_max_priority(heap)

#     # псевдокод для heap_get_max_priority можно посмотреть в прошлом уроке
        i += 1

    return sorted_array



def main():
    n = int(sys.stdin.readline().rstrip())

    data = []
    for _ in range(n):
        row = sys.stdin.readline().rstrip().split()
        data.append((row[0], int(row[1]), int(row[2])))

    print(data)




def test():
    arr = [3, 5, 1, 6, 9, 2,  -3, 11, 26, 7]
    d = heapsort(arr)
    print(d)


if __name__ == '__main__':
    #main()
    test()

def sift_down_recursive(heap, idx):
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


def sift_down(heap, idx):
    size = len(heap) - 1  # size = 6

    while True:
        left = 2 * idx
        right = 2 * idx + 1

        if size < left:
            return idx

        if (right <= size) and (heap[left] < heap[right]):
            index_largest = right
        else:
            index_largest = left

        if heap[idx] < heap[index_largest]:
            heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
            idx = index_largest
        else:
            return idx


def test():
    sample = [-1, 9, 6, 8, 3, 4, 7]
    sample2 = [-1, 9, 6, 8, 3, 4, 7]

    # idx, newel = 2, 5
    # sample[idx] = 5

    print(sample)
    rez = sift_down(sample, 1)
    # rez2 = sift_down_iter(sample2, 1)
    print('1: ', rez)
    # print('2: ', rez2)
    # assert rez == 1
    print(sample)


if __name__ == '__main__':
    test()

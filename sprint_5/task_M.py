def sift_up_recursive(heap, idx):

    if idx == 1:
        return idx

    parent_index = idx // 2
    if heap[parent_index] < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)
    else:
        return idx


def sift_up(heap, idx):

    while idx > 1:

        parent_index = idx // 2
        if heap[parent_index] < heap[idx]:
            heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
            idx = parent_index
        else:
            return idx

    return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1






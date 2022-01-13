import random

def comparator(a,b):
    pass

def partition(data, left, right, pivotIndex):
    pivotValue = data[pivotIndex]
    data[pivotIndex], data[right] = data[right], data[pivotIndex]  # Move pivot to end
    storeIndex = left
    for i in range(left, right):
        if data[i] < pivotValue:
            data[storeIndex], data[i] = data[i], data[storeIndex]
            storeIndex += 1
    data[right], data[storeIndex] = data[storeIndex], data[right]  # Move pivot to its final place
    return storeIndex

# Returns the k-th smallest element of list within left..right inclusive
# (i.e. left <= k <= right).
def select(data, left, right, k):
    if left == right:  # If the data contains only one element,
        return data[left]  # return that element
    pivotIndex = left + random.randint(a=0, b=right - left)  # select a pivotIndex between left and right,
    # e.g., left + floor(rand() % (right − left + 1))
    pivotIndex = partition(data, left, right, pivotIndex)
    # The pivot is in its final sorted position
    if k == pivotIndex:
        return data[k]
    elif k < pivotIndex:
        return select(data, left, pivotIndex - 1, k)
    else:
        return select(data, pivotIndex + 1, right, k)


def main():
    data = [5, 4, 7, 8, 3, 1,  9, 2, 6]
    print(select(data, 0, len(data)-1, 0))
    print(data)
    print('===')


if __name__ == "__main__":
    main()
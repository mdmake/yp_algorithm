import random


def comparator_less(a, b):
    if a[1] > b[1]:
        return True
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return True
    return False


def partition(data, left, right):
    # This gets an index, not a value:
    pivotindex = random.randint(left, right)  # allow right to be selected
    pivot = data[pivotindex]  # this is the pivot value
    # move the value out of the way
    data[right], data[pivotindex] = data[pivotindex], data[right]
    i = left - 1
    for j in range(left, right):
        #if data[j] < pivot:
        if comparator_less(data[j], pivot):
            i += 1
            if j > i:
                print(f'swap A[{i}] and A[{j}]')
                data[i], data[j] = data[j], data[i]
    data[i+1], data[right] = data[right], data[i+1]
    return i + 1

def quickselect(data, K, left, right):

    while left < right:
        if left == right:
            return data[left]
        pivotIndex = partition(data, left, right)
        if K == pivotIndex:
            return data[pivotIndex]  # this is the element you want to return
        if K < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1
    return data[left]

from math import exp, sqrt, log2
# left is the left index for the interval
# right is the right index for the interval
# k is the desired index value, where array[k] is the (k+1)th smallest element when left = 0

def sign(x):
    if x>0:
        return 1
    return -1

def select(array, left, right, k):
    while right > left:
        # Use select recursively to sample a smaller set of size s
        # the arbitrary constants 600 and 0.5 are used in the original
        # version to minimize execution time.
        if right - left > 600:
            n = right - left + 1
            i = k - left + 1
            z = log2(n)
            s = 0.5 * exp(2 * z/3)
            sd = 0.5 * sqrt(z * s * (n - s)/n) * sign(i - n/2)
            newLeft = max(left, k - i * s/n + sd)
            newRight = min(right, k + (n - i) * s/n + sd)
            select(array, newLeft, newRight, k)
        # partition the elements between left and right around t
        t = array[k] 
        i = left
        j = right
        array[left], array[k] = array[k], array[left]
        if array[right] > t:
            array[right], array[left] = array[left], array[right]
        while i < j:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1
            while array[i] < t:
                i = i + 1
            while array[j] > t:
                j = j - 1
        if array[left] == t:
            array[left], array[j] = array[j], array[left]
        else:
            j = j + 1
            array[right], array[j] = array[j], array[right]
        # Adjust left and right towards the boundaries of the subset
        # containing the (k - left + 1)th smallest element.
        if j <= k:
            left = j + 1
        if k <= j:
            right = j - 1


def bubblesort(data):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def max5(elements):
    for i in range(min(5, len(elements))):
        for j in range(i, len(elements)):
            #if key(elements[i]) < key(elements[j]):
            if comparator_less(elements[j], elements[i]):
                elements[i], elements[j] = elements[j], elements[i]

    return elements[:5]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]


def main():
    #data = [5, 4, 7, 8, 3, 1,  9, 2, 6]
    data = [[0, 3], [1, 3], [2, 3], [3, 4], [4, 4], [5, 3]]
    #prep = [0, 0, 0, 8, 3, 1,  9, 9, 6]
    #data  = [[0, 0], [1, 0], [2, 1], [3, 0], [4, 0], [5, 1], [6, 1], [7, 0], [8, 1], [9, 0]]

    #data = [[i, 20] for i in range(20)]
    #data = [i for i in range(10)]


    print(data)
    #print(select_test(data, 0, len(data) - 1,  4))
    print(max5(data))
    #print(quickselect(data, 4, 0, len(data) - 1))
    print('====================')
    print(data)
    print(data[:5])
    print(*[item[0] + 1 for item in sorted(data[:5], key=lambda x: (-x[1], x[0])) if item[1] > 0])



if __name__ == "__main__":
    main()

    # #data = [9, 2, 4, 1, 6, 3]
    # data = [[i, 10] for i in range(60)]
    # print(data)
    # pivot = 5
    # print(pivot, data[pivot])
    # partition_test(data, 0, len(data) - 1, pivot)
    # # kmax = 4
    # # print(select_test(data, 0, len(data) - 1, kmax))
    # print(data)

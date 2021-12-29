def binary_search(arr, x, left, right):
    while left <= right:
        if right <= left:
            if arr[right] == x:
                return right
            else:
                return -1

        # промежуток не пуст
        mid = (left + right) // 2
        if x <= arr[mid]:
            right = mid
        else:
            left = mid + 1


def broken_search_test(nums, target) -> int:
    j = len(nums) - 1
    i = 0
    mid = (j - i + 1) // 2

    if (nums[j] < target or target < nums[i]) and nums[i] <= nums[j]:
        return -1

    if nums[i] <= target <= nums[j]:
        return binary_search(nums, target, i, j)

    if nums[i] <= target:
        if nums[i] < nums[mid] <= target:
            rez = broken_search(nums[mid:], target)
            return mid + rez if rez >= 0 else rez
        else:
            return broken_search(nums[i:mid], target)

    if target <= nums[j]:
        if target < nums[mid] < nums[j]:
            return broken_search(nums[i:mid], target)
        else:
            rez = broken_search(nums[mid:], target)
            return mid + rez if rez >= 0 else rez


def broken_search(nums, target) -> int:
    j = len(nums) - 1
    i = 0

    while i <= j:
        mid = i + (j - i + 1) // 2

        if (nums[j] < target or target < nums[i]) and nums[i] <= nums[j]:
            return -1

        if nums[i] <= target <= nums[j]:
            return binary_search(nums, target, i, j)

        if nums[i] <= target:
            if nums[i] <= nums[mid] < target:
                i = mid
                continue
            else:
                j = mid - 1
                continue

        if target <= nums[j]:
            if target < nums[mid] <= nums[j]:
                j = mid - 1
                continue

            else:
                i = mid
                continue

    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    for i, item in enumerate(arr):
        rez = broken_search(arr, item)
        print(rez)
        assert rez == i


if __name__ == '__main__':
    test()

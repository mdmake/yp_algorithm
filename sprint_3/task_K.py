def merge(arr, lf, mid, rg):
    # Your code
    # “ヽ(´▽｀)ノ”

    l = lf
    r = mid
    result = []

    while l < mid and r < rg:
        if arr[l] <= arr[r]:
            result.append(arr[l])
            l += 1
        else:
            result.append(arr[r])
            r += 1

    while l < mid:
        result.append(arr[l])
        l += 1

    while r < rg:
        result.append(arr[r])
        r += 1

    arr[lf:rg] = result
    return arr


def merge_sort(arr, lf, rg):
    if lf+1 >= rg:
        return

    merge_sort(arr, lf, (rg-lf)//2 + lf)
    merge_sort(arr, (rg-lf)//2 + lf, rg)

    merge(arr, lf, ((rg - lf) // 2) + lf, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]

    print(b)
    print(expected)
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    print(expected)
    print(c)
    assert c == expected


if __name__ == '__main__':
    test()

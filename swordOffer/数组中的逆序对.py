# !/usr/bin/python3


def inversePairs(data):
    if not data:
        return 0
    temp = [i for i in data]
    return mergeSort(temp, data, 0, len(data) - 1) % 1000000007


def mergeSort(temp, data, low, high):
    if low >= high:
        temp[low] = data[low]
        return 0
    mid = (low + high) // 2
    left = mergeSort(data, temp, low, mid)
    right = mergeSort(data, temp, mid + 1, high)

    count = 0
    i = low
    j = mid + 1
    index = low
    while i <= mid and j <= high:
        if data[i] <= data[j]:
            temp[index] = data[i]
            i += 1
        else:
            temp[index] = data[j]
            count += mid - i + 1
            j += 1
        index += 1
    while i <= mid:
        temp[index] = data[i]
        i += 1
        index += 1
    while j <= high:
        temp[index] = data[j]
        j += 1
        index += 1
    return count + left + right


# 思路二
def inverp(data):
    """
    先将原数组排序，取出最小的它在原数组中的位置表示前面有多少个比它大的，然后删除它
    :param data: list
    :return: int
    """
    import copy
    count = 0
    copy = copy.copy(data)
    copy.sort()
    for i in range(len(copy)):
        count += data.index(copy[i])
        data.remove(copy[i])
    return count%1000000007


if __name__ == '__main__':
    nums = [1, 3, 7,2, 5, 6, 4]
    print(inverp(nums))

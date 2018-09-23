# !/usr/bin/python3

"""
一个长度为 n-1 的递增排序数组中所有数字是唯一的，每个数字都在 0~n-1 中，只有一个不在，求出这个数字
"""


def get_missing_number(numbers):
    if not numbers:
        return -1
    left, right = 0, len(numbers) -1
    while left<= right:
        mid = (left+right) //2
        if numbers[mid] != mid:
            if mid == 0 or numbers[mid-1] == mid-1:
                return mid
            right = mid-1
        else:
            left = mid + 1

    if left == len(numbers):
        return len(numbers)

    return -1

"""
数组中数值和下标相等的元素
"""


def get_number(numbers):
    if not numbers:
        return -1
    left, right = 0, len(numbers) -1
    while left <= right:
        mid = (left+right) //2
        if numbers[mid] == mid:
            return mid
        elif numbers[mid] > mid:
            right = mid- 1
        else:
            left = mid + 1



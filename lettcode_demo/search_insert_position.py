# !/usr/bin/python3

"""

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
"""


def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return len([x for x in nums if x < target])


def searchInsert(nums, target):
    import bisect
    a = bisect.bisect(nums, target)
    return a

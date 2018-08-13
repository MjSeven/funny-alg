# !/usr/bin/python3
"""
输入一个整形数组，，数组中有正数也有负数，数组中的一个或多个组成一个子数组，求所有子数组的最大值
时间复杂度：O(n)
"""


def findMaxSumOfSubarray(nums):
    """
    :param nums:list
    :return: int
    """
    if not nums:
        return
    length = len(nums)
    cursum = 0
    maxsum = float('-inf')
    start, end = 0, 0
    for i in range(length):
        if cursum <= 0:
            cursum = nums[i]
            start = i
        else:
            cursum += nums[i]
        if cursum > maxsum:
            end = i
            maxsum = cursum

    return maxsum


if __name__ == '__main__':
    nums = [1, -2, 3, 10, -4, 7, 2, -5]
    print(findMaxSumOfSubarray(nums))

# !/usr/bin/python3

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
"""


def canJump(nums):
    """
    思路：
        贪心算法
    :type nums: List[int]
    :rtype: bool
    """
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i + n)
    return True


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(canJump(nums))

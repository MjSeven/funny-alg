# !/usr/bin/python3

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
"""
def threeSumClosest(nums, target):
    """
    思路：
        双指针法，要先排序，然后一个在前，一个在后，遍历整个数组，比较和 target 的值
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    import sys
    result, diff = 0, sys.maxsize
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            hold_diff = abs(total - target)

            if not hold_diff:
                return total
            if hold_diff < diff:
                diff = hold_diff
                result = total
            if total < target:
                left += 1
            else:
                right -= 1
    return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    print(threeSumClosest(nums, 1))


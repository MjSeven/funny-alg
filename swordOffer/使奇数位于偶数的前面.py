# !/usr/bin/python3
"""
输入一个整数数组，使该数组中所有奇数位于数组的前半部分，偶数位于后半部分
"""

def solution(nums, length):
    if not nums or length <= 0:
        return

    left, right = 0, length -1
    while left < right:
        while left < right and nums[left] &1 == 1:
            # 说明遇到的都是奇数
            left += 1
        while left < right and nums[right] &1 == 0:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

"""
注意这里一个用法：
    n & 1 == 0 的话说明这个数是偶数
    n & 1 == 1 的话说明这个数是奇数
"""

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    solution(nums, len(nums))

    print(nums)


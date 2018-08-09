# !/usr/bin/python3
"""
一个有序数组的开始若干个元素移动到数组的末尾。求其最小元素。
如 [3, 4, 5, 1, 2] 为 [1, 2, 3, 4, 5] 的一个旋转。
"""

def Min(nums, length):
    if not nums or length <= 0:
        return
    start, end = 0, length -1
    while nums[start] >= nums[end]:
        if end - start == 1:
            mid = end
            break
        mid = (start + end) // 2
        if nums[start] == nums[end] == nums[mid]:
            return min(nums[start: end+1])
        if nums[mid] >= nums[start]:
            start = mid
        elif nums[mid] <= nums[end]:
            end = mid
    return nums[mid]


if __name__ == '__main__':
    nums = [3, 4, 5, 6, 1, 2]
    nums1 = [1, 0, 1, 1, 1]
    print(Min(nums, len(nums)))
    print(Min(nums1, len(nums1)))


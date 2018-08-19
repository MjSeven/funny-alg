# !/usr/bin/python3

"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。
"""


def fourSum(self, nums, target):
    def findNsum(nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results

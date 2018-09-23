"""
找到一个数组中出现次数大于 n/3 的数
n 为数组长度
"""
import collections
collections.Counter


def majorityelement(nums):
    from collections import Counter
    ctr = Counter()
    for n in nums:
        ctr[n] += 1
        if len(ctr) == 3:
            ctr -= Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums) / 3]


if __name__ == '__main__':
    a = [1, 1, 1, 3, 3, 2, 2, 2]
    print(majorityelement(a))

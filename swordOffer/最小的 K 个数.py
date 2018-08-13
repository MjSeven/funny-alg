# !/usr/bin/python3
"""
输入 n 个整数，找出其中最小的 k 个数
"""


def getLeatestNumbers(numbers, k):
    """
    :param numbers: list
    :param k: int
    :return: list
    """
    if not numbers or k <= 0:
        return []
    import heapq
    heap = []
    length = len(numbers)
    if length < k:
        return []
    for ele in numbers:
        ele = -ele
        if len(heap) < k:
            heapq.heappush(heap, ele)
        else:
            heapq.heappushpop(heap, ele)
    heap = [-i for i in heap]
    return sorted(heap)



if __name__ == '__main__':
    nums = [4, 5, 1, 6, 2, 7, 3 ,8]
    print(getLeatestNumbers(nums, 4))

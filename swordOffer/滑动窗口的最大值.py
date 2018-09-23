from collections import deque


def max_slidewindow(nums, k):
    if not nums or k <= 0:
        return
    if k == 1:
        return nums

    qmax = deque([])
    qmax.append(0)
    res = []
    for x, y in enumerate(nums[1:], 1):
        if nums[qmax[-1]] <= y:
            for i in range(len(qmax)-1, -1, -1):
                if nums[qmax[i]] > y:
                    break
                else:
                    qmax.pop()
        qmax.append(x)
        if qmax[0] <= x-k:
            qmax.popleft()
        if x >= k-1:
            res.append(nums[qmax[0]])
    return res

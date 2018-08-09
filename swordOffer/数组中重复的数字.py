def duplicate(nums, length):
    """
    找出数组中重复的数字：
        在一个长度为 n 的数组中，数字都在 0 ~ n-1 之间，有些数字是重复的，请输出任意一个
        例如 [2， 3， 1， 0， 2， 5， 3] 输出 2 或3 都可
    :param nums: list
    :param length: int
    :return: int
    """
    if not nums or length <= 0:
        return
    for i in range(length):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            # 注意与下面一种方式的区别，下面一种方式并不能正确交换结果
            # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            # temp = nums[nums[i]]
            # nums[nums[i]] = nums[i]
            # nums[i] = temp
    return


def CountRange(nums, length, start, end):
    if not nums:
        return 0
    count = 0
    for i in range(length):
        if start <= nums[i] <= end:
            count += 1
    return count


def getDuplication(nums, length):
    """
    不修改数组找出重复的数字
        利用二分查找的思想
    :param nums: list
    :param length: int
    :return: int
    """
    if not nums or length <= 0:
        return

    start, end = 1, length-1
    while end >= start:
        mid = start + ((end-start)>>1)
        count = CountRange(nums, length, start, mid)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > mid-start + 1:
            end = mid
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate(nums, len(nums)))
    nums = [2, 3, 5, 4, 3, 2, 6, 7]
    print(getDuplication(nums, len(nums)))


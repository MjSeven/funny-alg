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


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate(nums, len(nums)))


# !/usr/bin/python3

"""
数组中有一个数字的出现次数超过数组长度的一半，请找出这个数字
"""


def moreThanHalf(numbers):
    """
    :param numbers: list
    :return: None or int
    """
    if not numbers:
        return
    length = len(numbers)
    res = numbers[0]
    times = 1
    for i in range(1, length):
        if times == 0:
            res = numbers[i]
        elif numbers[i] == res:
            times += 1
        else:
            times -= 1
    real_times = numbers.count(res)
    if real_times < length/2:
        res = None
    return res


if __name__ == '__main__':
    nums = [1, 2, 3,2, 2,2,2 ,5,4,2]
    print(moreThanHalf(nums))

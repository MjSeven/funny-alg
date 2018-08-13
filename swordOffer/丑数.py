# !/usr/bin/python3
"""
只包含因子 2 3 5 的数称为丑数
习惯上 1 为第一个丑数
"""


def getUglyNumber_Solution(index):
    if index <= 0:
        return 0
    if index == 1:
        return 1
    numbers = [1]
    i2, i3, i5 = 0, 0, 0
    for k in range(index - 1):
        n2 = numbers[i2] * 2
        n3 = numbers[i3] * 3
        n5 = numbers[i5] * 5
        min_ = min(n2, n3, n5)
        numbers.append(min_)
        if n2 == min_:
            i2 += 1
        if n3 == min_:
            i3 += 1
        if n5 == min_:
            i5 += 1
    return min_
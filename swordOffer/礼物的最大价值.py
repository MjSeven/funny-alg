# !/usr/bin/python3
"""
在一个 m*n 的棋盘上，每一格中都有一个礼物，现在可以从棋盘的左上角开始，，每次只能向下或向右移动
直到棋盘的右下角。计算能拿到最大的礼物价值
"""


def getMaxValue(values):
    if not values:
        return 0
    rows = len(values)
    cols = len(values[0])
    maxvalues = []
    for i in range(rows):
        for j in range(cols):
            left, up = 0, 0
            if i > 0:
                up = maxvalues[i]
            if j > 0:
                left = maxvalues[j-1]

            maxvalues[i] = max(left, up) + values[i][j]

    return maxvalues[-1]


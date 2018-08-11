# !/usr/bin/python3
"""
有一个矩阵：
1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16
按照1 2 3 4 8 12 167 15 14 13 9 5 6 ...顺序打印
"""

def printMatrix(matrix):
    ret = []
    while matrix:
        ret += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        if matrix:
            ret += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))

    return ret

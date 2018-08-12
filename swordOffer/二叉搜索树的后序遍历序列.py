# !/usr/bin/python3
"""
判断一个数组是不是二叉搜索树的后序遍历
"""

def verifySquenceOfBST(sequence):
    if not sequence:
        return False
    if len(sequence) == 1:
        return True
    length = len(sequence)
    root = sequence[-1]
    i = 0
    while sequence[i] < root:
        i = i + 1
    k = i
    for j in range(i, length - 1):
        if sequence[j] < root:
            return False
    left_s = sequence[:k]
    right_s = sequence[k:length - 1]

    leftIs = True
    rightIs = True

    if len(left_s) > 0:
        leftIs = verifySquenceOfBST(sequence=left_s)
    if len(right_s) > 0:
        rightIs = verifySquenceOfBST(sequence=right_s)

    return leftIs and rightIs


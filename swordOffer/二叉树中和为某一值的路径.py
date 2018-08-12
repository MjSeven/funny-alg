# !/usr/bin/python3

class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findPath(root, expectNumber):
    if not root:
        return []
    if root and root.left and not root.right and root.val == expectNumber:
        return [[root.val]]

    res = []
    left = findPath(root.left, expectNumber-root.val)
    right = findPath(root.right, expectNumber-root.val)
    for i in left+right:
        res.append([root.val] + i)

    return res




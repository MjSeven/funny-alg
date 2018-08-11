# !/usr/bin/python3
"""
判断一颗二叉树是不是对称的
如果和它的镜像一样，则其是对称的，否则不是
"""

class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetrical(root):
    def isSame(p1, p2):
        if not p1 and not p2:
            return True
        if not p1 or not p2:
            return False
        if p1.val != p2.val:
            return False

        return isSame(p1.left, p2.right) and isSame(p1.right, p2.left)

    return isSame(root, root)


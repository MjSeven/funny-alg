# !/usr/bin/python3
"""
输入一颗二叉树，输出它的镜像，即左右节点互换
"""

class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mirrorRecursively(pNode):
    if not pNode:
        return
    if not pNode.left and not pNode.right:
        return
    pNode.left, pNode.right = pNode.right, pNode.left
    if pNode.left:
        mirrorRecursively(pNode.left)
    if pNode.right:
        mirrorRecursively(pNode.right)

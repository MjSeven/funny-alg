# !/usr/bin/python3
"""
从上到下打印二叉树，同一层的节点从左至右
"""


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def PrintFromToptoBottom(pRoot):
    if not pRoot:
        return

    d = []
    d.append(pRoot)
    while len(d):
        pNode = d.pop(0)
        print(pNode.val)
        if pNode.left:
            d.append(pNode.left)
        if pNode.right:
            d.append(pNode.right)

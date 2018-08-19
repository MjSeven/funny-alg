"""
二叉搜索树与双向链表转换
"""


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def convert(pRootOfTree):
    if not pRootOfTree:
        return
    if not pRootOfTree.left and not pRootOfTree.right:
        return
    # 处理左子树
    convert(pRootOfTree.left)
    left = pRootOfTree.left

    # 连接跟与左子树最大节点
    if left:
        while left.right:
            left = left.right
        pRootOfTree.left, left.right = left, pRootOfTree

    # 处理右子树
    convert(pRootOfTree.right)
    right = pRootOfTree.right

    # 连接根与右子树的最小节点
    if right:
        while (right.left):
            right = right.left
        pRootOfTree.right, right.left = right, pRootOfTree

    while (pRootOfTree.left):
        pRootOfTree = pRootOfTree.left
    return pRootOfTree


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(14)
    convert(root)

class Solution:
    def NodeList(self, pRootOfTree):
        if not pRootOfTree:
            return []
        return self.NodeList(pRootOfTree.left) + [pRootOfTree] + self.NodeList(pRootOfTree.right)

    def convert(self, pRootOfTree):
        res = self.NodeList(pRootOfTree)
        if len(res) == 0:
            return None
        if len(res) == 1:
            return pRootOfTree
        res[0].left = None
        res[0].right = res[1]
        res[-1].left = res[-2]
        res[-1].right = None
        for i in range(1, len(res) - 1):
            res[i].left = res[i - 1]
            res[i].right = res[i + 1]
        return res[0]

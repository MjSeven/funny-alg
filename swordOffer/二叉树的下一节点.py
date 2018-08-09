# !/usr/bin/python3
"""
给定一个二叉树和其中的一个节点，找出中序遍历的下一个节点
树的节点有一个指向父亲的指针以及左右孩子的指针
"""
"""
class BinaryTreeNode():
    def __init__(self, left, right, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
"""


def getNext(pNode):
    if not pNode:
        return

    pNext = None
    if pNode.right:
        # 当有右子树的时候，那么下一节点是右子树的最左节点
        pRigth = pNode.right
        while pRigth.left:
            pRigth = pRigth.left

        pNext = pRigth
    elif pNode.parent:
        # 没有右子树，那么考虑父节点
            # 如果是父节点的左子节点，那么父节点即为下一节点
            # 如果是父节点的右节点，那么一层一层往上，直到节点是父节点的左子节点为止
        pCurrent = pNode
        pParent = pNode.parent
        while pParent and pCurrent == pParent.right:
            pCurrent = pParent
            pParent = pParent.parent
        pNext = pParent

    return pNext




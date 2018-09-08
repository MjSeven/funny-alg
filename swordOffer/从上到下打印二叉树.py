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

def Print(pRoot):
    if not pRoot:
        return []
    res = []
    tmp = [pRoot]
    while tmp:
        size = len(tmp)
        row = []
        for i in tmp:
            row.append(i.val)
        res.append(row)
        for i in range(size):
            node = tmp.pop(0)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
    return res



if __name__ == '__main__':
    node = BinaryTreeNode(1)
    node.left = BinaryTreeNode(2)
    node.right = BinaryTreeNode(3)
    node.left.left = BinaryTreeNode(4)
    node.left.right = BinaryTreeNode(5)
    node.right.left = BinaryTreeNode(6)
    node.right.right = BinaryTreeNode(7)
    #PrintFromToptoBottom(node)
    res = Print(node)
    print(res)

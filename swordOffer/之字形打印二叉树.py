# !/usr/bin/python3


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def printBin(self, pRoot):
    if not pRoot:
        return []
    from collections import deque
    res, tmp = [], []
    last = pRoot
    q = deque([pRoot])
    left_to_right = True
    while q:
        t = q.popleft()
        tmp.append(t.val)
        if t.left:
            q.append(t.left)
        if t.right:
            q.append(t.right)
        if t == last:
            res.append(tmp if left_to_right else tmp[::-1])
            left_to_right = not left_to_right
            tmp = []
            if q:
                last = q[-1]
    return res
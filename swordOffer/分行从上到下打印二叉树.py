# !/usr/bin/python3


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def Print(root):
    if not root:
        return
    s = []
    s.append(root)
    nextlevel, toBeprint = 0, 1
    while len(s):
        pNode = s.pop(0)
        print(pNode.val)
        toBeprint -= 1
        if pNode.left:
            nextlevel += 1
        if pNode.right:
            nextlevel += 1

        if toBeprint == 0:
            print()
            nextlevel, toBeprint = toBeprint, nextlevel

def Print(pRoot):
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

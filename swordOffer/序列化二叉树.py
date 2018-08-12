# !/usr/bin/python3


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = -1
    def serialize(self, root):
        if not root:
            return "#"
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def deserializer(self, s):
        self.flag += 1

        l = s.split(',')
        if self.flag >= len(s):
            return None
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.deserializer(s)
            root.right = self.deserializer(s)
        return root

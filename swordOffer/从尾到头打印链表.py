# !/usr/bin/python3
"""
class ListNode:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
"""

def PrintNode(pHead):
    # 基于栈实现
    pNode = pHead
    nodes = []
    while pNode:
        nodes.append(pNode)
        pNode = pNode.next
    while len(nodes):
        pNode = nodes.pop()
        print(pNode.value)


def PrintNode(pHead):
    # 基于递归实现
    if pHead:
        if pHead.next:
            PrintNode(pHead.next)
    print(pHead.value)
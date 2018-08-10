# !/usr/bin/python3
"""
单链表反转问题
"""
class ListNode:
    def __init__(self, value, next):
        self.val = value
        self.next = next


def ReverseListNode(pHead):
    pNode = pHead
    pPrev, pReverse = None, None
    while pNode:
        pNext = pNode.next
        if not pNext:
            pReverse = pNode

        pNode.next = pPrev
        pPrev = pNode
        pNode = pNext

    return pReverse

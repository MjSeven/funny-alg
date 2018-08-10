# !/usr/bin/python3
"""
合并两个排序的链表，合并之后仍然有序
"""

class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def merge(pHead1, pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    pNew = ListNode(0)
    p = pNew
    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            pNew.next = pHead1
            pHead1 = pHead1.next
        else:
            pNew.next = pHead2
            pHead2 = pHead2.next
        pNew = pNew.next
    if pHead1:
        pNew.next = pHead1
    if pHead2:
        pNew.next = pHead2

    return p.next




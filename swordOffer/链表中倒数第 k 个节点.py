# !/usr/bin/python3
"""
输入一个链表，输出该链表中倒数第 k 个节点
尾部节点是倒数第 1 个
"""
class ListNode:
    def __init__(self, value, next):
        self.val = value
        self.next = next

"""
第一个指针先开始走 k-1 步，然后第二个指针从头开始
若第二个指针走到末尾了，那么第二个指针就是倒数第 k 个节点
"""

def findKthToTail(pHead, k):
    """
    :param pHead: ListNode
    :param k: int
    :return: ListNode
    """
    if not pHead or k <= 0:
        return None

    pAhead = pHead
    for i in range(k-1):
        if pAhead.next:
            pAhead = pAhead.next
        else:
            return None

    pBehind = pHead
    while pAhead.next:
        pAhead = pAhead.next
        pBehind = pBehind.next

    return pBehind




# !/usr/bin/python3
"""
在 O(1) 时间内删除链表节点
"""
class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

    def __eq__(self, other):
        if self.val == other.val and self.next == other.next:
            return True
        return False


def deleteNode(pHead, pToBedeleted):
    """
    主要分为三种情况：
        尾节点：直接将倒数第一个节点的 next 赋值为 None 即可
        不是尾节点：将要删除节点的变为下一节点即可
        头节点：都赋值为空即可
    :param pHead: ListNode
    :param pToBedeleted: ListNode
    :return:
    """
    if not pHead or not pToBedeleted:
        return

    if pToBedeleted.next:
        pNext = pToBedeleted.next
        pToBedeleted.val = pNext.val
        pToBedeleted.next = pNext.next
    #elif pHead.val == pToBedeleted.val and pHead.next == pToBedeleted.next:
    elif pHead == pToBedeleted:
        pToBedeleted = None
        pHead = None
    else:
        pNode = pHead
        while pNode.next != pToBedeleted:
            pNode = pNode.next
        pNode.next = None


a = ListNode(1)
b = ListNode(1)
print(a == b)


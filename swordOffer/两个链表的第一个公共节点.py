# !/usr/bin/python3

"""
思路：
    1 蛮力法：
        遍历第一个链表，每到一个节点就遍历第二个链表，看是否与之相同 时间复杂度O(mn)
    2 借助栈
        将两个链表分别放到不同的栈中，由于栈顶存放的是链表的尾节点，
        而如果链表存在公共节点，尾节点一定相同，只需找到最后一个相同的尾节点即可‘
        时间复杂度 O(m+n)
    3 遍历法
        先在较长的链表上走几步，然后两个链表一同前进，每次判断是否相同即可
         时间复杂度 O(m+n)
"""

class ListNode:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next


def getListNodeLength(pHead):
    if not pHead:
        return 0
    pNode = pHead
    length = 0
    while pNode:
        length += 1
        pNode = pNode.next
    return length


def findfirstCommonNode(pHead1, pHead2):
    length1 = getListNodeLength(pHead1)
    length2 = getListNodeLength(pHead2)

    pHeadLong = pHead1 if length1 > length2 else pHead2
    pHeadShort = pHead2 if length1 > length2 else pHead1

    for i in range(abs(length1-length2)):
        pHeadLong = pHeadLong.next

    while pHeadLong and pHeadShort and pHeadLong != pHeadShort:
        pHeadLong = pHeadLong.next
        pHeadShort = pHeadShort.next

    firstCommonNode = pHeadLong
    return firstCommonNode







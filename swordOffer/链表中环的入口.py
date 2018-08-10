# !/usr/bin/python3
"""
一个链表包含环，如何找出环的入口节点
"""
class ListNode:
    def __init__(self, value, next):
        self.val = value
        self.next = next

    def __eq__(self, other):
        if self.val == other.val and self.next == other.next:
            return True
        return False

"""
思路：
    先确定链表存在环，然后任意找出环中的一个节点
    然后确定环中节点个数 k ，最后两个指针，第一个先走 k 步，第二个开始从头走，相遇的点即位入口节点
"""
def mettingNode(pHead):
    # 确定链表存在环，而且找到环中的一个节点
    if not pHead:
        return None
    pSlow = pHead.next
    pFast = pHead.next
    while pSlow and pFast:
        if pSlow == pFast:
            return pSlow

        pSlow = pSlow.next
        if pFast:
            pFast = pFast.next
    return None


def entryNode(pHead):
    meetNode = mettingNode(pHead)
    if not meetNode:
        return None

    loop = 1
    pNode = pHead
    if pNode.next != meetNode:
        loop += 1
        pNode = pNode.next

    pNode = pHead
    for i in range(loop):
        pNode = pNode.next

    pNode2 = pHead
    while pNode != pNode2:
        pNode = pNode.next
        pNode2 = pNode2.next

    return pNode

"""
思路二：遍历链表，将当前节点放入一个列表中，遍历到下一个节点时判断其是否在列表中就行了
    不过这种方法在链表很长时很消耗额外空间。O(n)
"""
def EntryNodeLoop(pHead):
    tempList= []
    p = pHead
    while p:
        if p in tempList:
            return p
        tempList.append(p)
        p = p.next


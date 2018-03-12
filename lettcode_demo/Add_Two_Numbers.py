# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0   # 进位符
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next    # 这一步一定要仔细理解为什么会这样返回

    
# 链表构造
idx = ListNode(3)
n = idx
n.next = ListNode(4)
n = n.next
n.next = ListNode(5)
n = n.next
print(idx.val,idx.next.val,idx.next.next.val)
    

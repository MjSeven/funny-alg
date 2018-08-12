# !/usr/bin/python3
"""
两个整数序列，一个表示栈的压入顺序，另一个表示栈的弹出序列，判断弹出序列是否正确
"""

from collections import UserList

def isPopOrder(pushV, popV):
    stack = []
    while popV:
        if pushV and popV[0] == pushV[0]:
            popV.pop(0)
            pushV.pop(0)
        elif stack and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
        elif pushV:
            stack.append(pushV.pop(0))
        else:
            return False
    return True


if __name__ == '__main__':
    push = [1,2,3,4,5]
    pop = [1, 2, 3, 4, 5]
    print(isPopOrder(push, pop))

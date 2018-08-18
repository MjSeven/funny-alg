# !/usr/bin/python3

class Solution:
    """
    两个栈实现队列
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()


class Solution:
    """
    两个队列实现栈
    """
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, val):
        self.queue1.append(val)

    def pop(self):
        if len(self.queue1) == 0:
            # return None
            raise IndexError
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2 ,self.queue1
        return self.queue2.pop()


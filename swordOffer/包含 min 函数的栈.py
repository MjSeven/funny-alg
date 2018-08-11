# !/usr/bin/python3

"""
实现栈的数据结构，包含 min 函数，使得 min，push，pop 函数时间复杂度都是 O(1)
"""


class Stack:
    def __init__(self):
        self.m_data = []
        self.m_min = []

    def push(self,value):
        self.m_data.append(value)
        if len(self.m_min) == 0 or value < self.m_min[-1]:
            self.m_min.append(value)
        else:
            self.m_min.append(self.m_min[-1])

    def pop(self):
        if self.m_data and self.m_min:
            self.m_data.pop()
            self.m_min.pop()

    def top(self):
        if self.m_data:
            return self.m_data[-1]


    def min(self):
        if self.m_min:
            return self.m_min[-1]
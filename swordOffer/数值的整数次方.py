# !/usr/bin/python3
"""
实现函数 求取一个数的 n 次方
类似于 Python 中的 2**3 = 8
"""
"""
公式：

a^n = a^(n/2) * a^(n/2)  --> 若 n 为偶数
a^n = a^((n-1)/2) * a^((n-1)/2) * a  --> 若 n 为奇数
"""

def Power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = Power(base, exponent>>1)
    result *= base
    if exponent & 1 == 1:
        result *= base

    return result

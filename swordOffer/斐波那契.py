# !/usr/bin/python3

def fibonacci(n):
    if n < 2:
        return n
    one, two, fibN = 1, 0, 0
    for i in range(n):
        fibN = one + two
        two, one = one, fibN

    return fibN

def fib(n):
    index, a, b = 0, 0, 1
    while index < n:
        yield b
        a, b = b, a+b
        index += 1

# 类似的还有青蛙跳台阶问题：
    # 一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级台阶，求青蛙要跳上 n 级的台阶总共有多少种跳法？
    # 或者青蛙一次可以跳上 1 级，也可以 2 级，也可以 。。。 n 级，那么总共有 f(n) = 2^(n-1) 种方法

if __name__ == '__main__':
    print(fibonacci(5))
    print(list(fib(5)))

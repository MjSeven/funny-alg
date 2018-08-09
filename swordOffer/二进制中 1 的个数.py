# !/usr/bin/python3

def NumberOf1(n):
    count = 0
    while n:
        count += 1
        n = (n-1) & n
    return count

# 判断一个数是不是 2 的整数次方
# (n-1)&n


if __name__ == '__main__':
    print(NumberOf1(10))

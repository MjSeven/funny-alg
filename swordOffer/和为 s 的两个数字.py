"""
一个递增排序的数组和一个数字 s
在数组中查找两个数，是他们和为 s
"""


def find_numbers_sum(numbers, s):
    if not numbers:
        return []
    ahead, behind = len(numbers)-1, 0
    while ahead > behind:
        cursum = numbers[ahead] + numbers[behind]
        if cursum == s:
            print(numbers[ahead], numbers[behind])
            break
        elif cursum > s:
            ahead -= 1
        else:
            behind += 1

a = [1,2,3,4,5,6]
find_numbers_sum(a, 11)

"""
和为 s 的连续正数序列
"""

def fund_continuous_seq(s):
    if s<3:
        return
    small, big = 1, 2
    mid = (s+1) //2
    cursum = small + big
    while small < mid:
        if cursum == s:
            print(range(small, big+1))
        while cursum > s and small < mid:
            cursum -= small
            small += 1
            if cursum == s:
                print(range(small, big + 1))

        big += 1
        cursum += big

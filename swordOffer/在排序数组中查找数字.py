# !/usr/bin/python3

"""
统计一个数字在排序数组中出现的次数。
注意： 排序
"""


def get_numberof_k(data, k):
    if not data:
        return
    number = 0
    first = get_first_k(data, k)
    last = get_last_k(data, k)
    if first > -1 and last > -1:
        number = last - first +1

    return number


def get_first_k(data, k):
    if not data:
        return
    start, end = 0, len(data)-1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] ==k:
            if  mid == 0 or data[mid-1]!= k:
                return mid
            else:
                end = mid -  1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def get_last_k(data, k):
    if not data:
        return
    start, end = 0, len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == k:
            if mid == len(data)-1 or data[mid + 1] != k  :
                return mid
            else:
                start = mid + 1
        elif data[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# def get_first_k(data, k):
#     if not data:
#         return
#     start, end = 0, len(data)-1
#     mid = (start+end)//2
#     if data[mid] ==k:
#         if mid > 0 and data[mid-1]!= k or mid==0:
#             return mid
#         else:
#             end = mid -  1
#     elif data[mid] > k:
#         end = mid - 1
#     else:
#         start = mid + 1
#
#     return get_first_k(data, k)
#
#
# def get_last_k(data, k):
#     if not data:
#         return
#     start, end = 0, len(data) - 1
#     mid = (start + end) // 2
#     if data[mid] == k:
#         if mid > 0 and data[mid + 1] != k or mid == len(data)-1:
#             return mid
#         else:
#             start = mid + 1
#     elif data[mid] < k:
#         start = mid + 1
#     else:
#         end = mid - 1
#
#     return get_last_k(data, k)


if __name__ == '__main__':
    a = [1,2,3,3,3,3,4,5]
    print(get_numberof_k(a, 3))
    a = [3,3,3,3]
    print(get_numberof_k(a, 3))
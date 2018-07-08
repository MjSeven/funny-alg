#! /usr/bin/env python
# _*_ coding:utf-8 _*_

# 插入排序
def insert_sort(alist):
    # 直接插入
    count = len(alist)
    for i in range(1, count):
        key = alist[i]
        j = i - 1
        while j >= 0:
            if alist[j] > key:
                alist[j], alist[j + 1] = key, alist[j]
            j -= 1

def main():
    alist= [54,26,93,17,77,31,44,55,20]
    print(insert_sort(alist))

if __name__ == '__main__':
    main()

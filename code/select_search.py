#!/usr/bin/env python 
#coding:utf-8

def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in xrange(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newarr = []
    for i in xrange(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

# 另一种写法
def select_sort(list_test):
    for i in range(0, len(list_test)):
        min_d = i       # 0 1
        for j in range(i + 1, len(list_test)):      # 1 ~ len(list_test)
            if list_test[j] < list_test[min_d]:
                min_d = j
        # 一轮过后选出最小的一个数放在第一个位置
        list_test[i], list_test[min_d] = list_test[min_d], list_test[i]
        
def main():
    alist= [54,26,93,17,77,31,44,55,20]
    print(select_sort(alist))

if __name__ == '__main__':
    main()

#!/usr/bin/env python
#coding:utf-8

def binary_search(alist, item):
    low = 0
    high = len(alist) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = alist[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def main():
    a = [1, 3, 5, 7, 9]
    print(binary_search(a,9))
    print(binary_search(a,5))
    print(binary_search(a, -1))

if __name__ == '__main__':
    main()

#!/usr/bin/env python
#coding:utf-8

def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[0]

    less = [i for i in array[1:] if i < pivot]
    great = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(great)

def quick_sort2(alist, left, right):
    if left >= right:
        return
    low, high = left, right
    key = alist[low]
    while left < right:
        while left < right and alist[right] > key:
            right -= 1
        alist[left] = alist[right]
        
        while left < right and alist[left] <= key:
            left += 1
        alist[right] = alist[left]
    alist[right] = key
    
    quick_sort(alist, low, left-1)
    quick_sort(alist, left+1, high)
   
def quick_sort3(array, l, r):
    if l <= r:
        q = partition(array, l, r)
        quick_sort(array, l, q-1)
        quick_sort(array, 1+1, r)
        
def partition(arr, l, r):
    x = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
     arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def main():
    alist= [54,26,93,17,77,31,44,55,20]
    print(quick_sort(alist))

if __name__ == '__main__':
    main()

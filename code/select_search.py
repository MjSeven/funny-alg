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
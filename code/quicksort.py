#!/usr/bin/env python
#coding:utf-8

def quicksort(array):
    if len(array) < 2:
        return array

    pivot = array[0]

    less = [i for i in array[1:] if i < pivot]
    great = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(great)

#a = [10,2,89,3,56,34,23,67,23,1,345,3623462,23,154,43]
#print quicksort(a)



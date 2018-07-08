#! /usr/bin/env python
# _*_ coding:utf-8 _*_

def shell_sort(L):
    step = len(L)//2
    while step > 0:
        for i in range(step,len(L)):            #在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while(i >= step and L[i] < L[i-step]):      #这里可以调整step从小到大或者从大到小排列
                L[i],L[i-step] = L[i-step],L[i]
                i -= step
                # print L
        step /= 2
    print L

# 增量的选择方式是希尔排序的独特特征
def main():
    alist= [54,26,93,17,77,31,44,55,20]
    print(shell_sort(alist))

if __name__ == '__main__':
    main()
    

def Shell_sort(L):
# 引用至：https://www.cnblogs.com/xubing-613/p/7286203.html
    step = len(L)/2
    while step > 0:
        for i in range(step,len(L)):            #在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while(i >= step and L[i] < L[i-step]):      #这里可以调整step从小到大或者从大到小排列
                L[i],L[i-step] = L[i-step],L[i]
                i -= step
                # print L
        step /= 2
    print L

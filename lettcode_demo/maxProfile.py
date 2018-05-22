# _*_ coding:utf-8 _*_
# 一个数组，求出最大差异值，但是前面的值要小于后面的
# 例如 [9, 11, 8, 5, 7, 12, 16, 14] 最大差异值是 11，就是 5 和 16，但是要保证 5 < 16
# 思路：在扫描到数组的第 i 个数字时，记住之前的 i - 1 个数字的最小值，就能在当前位置得到最大差异值

def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        min = prices[0]
        maxdiff = prices[1] - min
        for i in range(2,length):
            if prices[i-1] < min:
                min = prices[i-1]
            curdiff = prices[i] - min
            maxdiff = max(maxdiff, curdiff)
        if maxdiff <= 0:
            return 0
        return maxdiff

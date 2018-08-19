"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


def max_area(height):
    """
    思路：
        两线段之间的区域总会受限于较短的那条
        移动较长的只会让面积越来越小，移动较短的那条会让面积可能变大
    :param height: List[int]
    :return: int
    """
    length = len(height)
    l, r = 0, length-1
    max_water = 0
    while l < r:
        max_water = max(max_water, min(height[l], height[r])*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_water

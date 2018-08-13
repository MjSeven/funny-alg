# !/usr/bin/python3

"""
从字符串中找出最长的不包含重复字符的子字符串
"""


def longestSubstring(s):
    used = {}
    long, start = 0, 0
    for i, c in enumerate(s):
        if c in used and start < used[c]:
            start += 1
        else:
            long = max(long, i-start+1)
        used[c] = i

    return long


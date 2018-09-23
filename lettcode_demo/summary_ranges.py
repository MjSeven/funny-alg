"""
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
"""


def summary_ranges(nums):
    ranges, r = [], []
    for n in nums:
        if n - 1 not in r:
            r = []
            # ranges += r,
            ranges.append(r)
        r[1:] = n,
    print(ranges)
    return ['-'.join(map(str, r)) for r in ranges]


if __name__ == '__main__':
    a = [0, 1, 2, 4, 5, 7]
    print(summary_ranges(a))

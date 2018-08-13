# !/usr/bin/python3


def findfirstchar(s):
    if not s:
        return -1
    count = {}
    order = []
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
            order.append(i)
    for i in order:
        if count[s[i]] == 1:
            return i

    """
    # 直接输出字符
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            order.append(i)
    for i in order:
        if count[i] == 1:
            return i

    """


if __name__ == '__main__':
    s = 'google'
    print(findfirstchar(s))

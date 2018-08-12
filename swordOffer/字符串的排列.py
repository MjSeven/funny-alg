# !/usr/bin/python3
from itertools import permutations

def permutation(ss):
    if not ss:
        return []
    a = map(''.join, permutations(ss))
    return sorted(list(set(a)))


def permutation1(ss):
    if not ss:
        return []
    res = []
    helper(ss, res, '')
    return sorted(list(set(res)))


def helper(ss, res, path):
    if not ss:
        res.append(path)
    else:
        for i in range(len(ss)):
            helper(ss[:i] + ss[i + 1:], res, path + ss[i])

"""
C++ 语言
void Permutation(char* pStr)
{
    if(pStr == nullptr)
        return
    Permutation(pStr, pStr);
}
void Permutation(char* pStr, char* pBegin)
{
    if(*pStr == '\0')
        print('%s\n', pStr);
    else:
    {
        for(char* pCh = pBegin; *pCh != '\0'; ++pCh)
        {
            char temp = *pCh;
            *pCh = *pBegin;
            *pBegin = temp;
            
            Permutation(pStr, pBegin + 1);
            
            temp = *pCh;
            *pCh = *pBegin;
            *pBegin = temp;
        }
    }
}
"""

if __name__ == '__main__':
    s = 'abc'
    res = permutation1(s)
    print(res)

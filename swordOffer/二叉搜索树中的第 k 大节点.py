# !/usr/bin/python3

"""
二叉搜索树中中序遍历是按照从小到大的顺序来排列的
"""

def get_kth_number(pRoot, k):
    if not pRoot or k <= 0:
        return None
    def core(pRoot, k):
        if pRoot.left:
            target = core(pRoot.left, k)
        if not target:
            if k == 1:
                target = pRoot
            k -= 1
        if pRoot.right:
            target = core(pRoot.right, k)

        return target

    return core(pRoot, pRoot, k)


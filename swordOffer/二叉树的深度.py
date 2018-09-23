# !/usr/bin/python3

def get_depth(pRoot):
    """
    二叉树的深度
    """
    if not pRoot:
        return 0
    left = get_depth(pRoot.left)
    right = get_depth(pRoot.right)

    return left+1 if left>right else right+1


def is_balanced(pRoot):
    """
    判断是否是平衡二叉树
    :param pRoot: BinaryTreeNode
    :return: True or False
    """
    if not pRoot:
        return True
    depth = 0
    def core(pRoot, depth):
        if not pRoot:
            depth = 0
            return True
        left, right = 0, 0
        if core(pRoot.left, left) and core(pRoot.right, right):
            diff = abs(left - right)
            if diff <= 1:
                depth = max(left, right) +1
                return True
    return core(pRoot, depth)


def isbalanced_solution(proot):
    if not proot:
        return True
    if abs(get_depth(proot.left) - get_depth(proot.right)) > 1:
        return  False

    return  isbalanced_solution(proot.left) and isbalanced_solution(proot.right)

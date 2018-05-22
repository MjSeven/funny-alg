# _*_coding:utf-8
# 1. 机器人从 M * N 的网格左上角开始，要到右下角，问总共有多少条路径？
# 2. 在网格中加入了障碍物，用 1 表示，其余用 0 表示，同样问有多少条路径？

# 1. 解决办法：到达某一点的路径数等于到达它上一点的路径数与它左边的路径数之和。
#             即起点到达 (i, j) 点的路径 = 起点到 (i - 1, j) + 起点到 (i, j-1) 的路径。
# 2. 解决办法：如果是 1 ，直接本条路径为 0 。否则加之前一个格子的路径


def uniquePathsWithObstacles(obstacleGrid):
    """
    :info: has obstacles
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if obstacleGrid[0][0] == 1: return 0
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])): 
            if obstacleGrid[i][j] == 1 or i == j == 0:
                obstacleGrid[i][j] -= 1
            else:
                add1 = obstacleGrid[i - 1][j] if i > 0 else 0
                add2 = obstacleGrid[i][j - 1] if j > 0 else 0
                obstacleGrid[i][j] += add1 + add2
    return abs(obstacleGrid[-1][-1])


def uniquePaths(m, n):
    """
    :info: has no obstacles
    :type m: int
    :type n: int
    :rtype: int
    """
    aux = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            aux[i][j] = aux[i][j-1] + aux[i-1][j]
        print aux
    return aux[-1][-1]

def uniquePaths1(m, n):
    """
    :info: has no obstacles use one array
    :type m: int
    :type n: int
    :rtype: int
    """
    row_state = [1] * n
    for _ in range(1, m):
        col_state = 1
        for j in range(1, n):
            row_state[j] += col_state
            col_state = row_state[j]
            
    return row_state[-1]


def main():
    test = [[0,0,0],[0,1,0],[0,0,0]]
    print uniquePaths1(7, 3)
    #print uniquePathsWithObstacles(test)
    #print test

if __name__ == '__main__':
    main()
    

# !/usr/bin/python3

def find(matrix, rows, columns, num):
    """
    在一个二维数组中查找，每一行从左至右递增，每一列从上到下递增
        思路：从右上角开始查找
    :param matrix: list
    :param rows: int
    :param columns: int
    :param num: int
    :return: True or Flase
    """
    if matrix and rows > 0 and columns > 0:
        row, column = 0, columns - 1
        while row < rows and column >= 0:
            if matrix[row][column] == num:
                return True
            elif matrix[row][column] > num:
                column -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    matrix = [[1,2,8,9], [2,4,9,12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(find(matrix, len(matrix), len(matrix[0]), 56))

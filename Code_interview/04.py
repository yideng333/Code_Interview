'''
二维数组中查找
'''


def find_matrix(matrix, element):
    row = 0
    col = len(matrix[0])-1

    while row < len(matrix) and col < len(matrix[0]):
        if matrix[row][col] == element:
            return (row, col)
        elif matrix[row][col] > element:
            col = col - 1
        else:
            row = row + 1

    return False


if __name__ == '__main__':
    test_case_1 = [[1, 2, 8, 9],
                   [2, 4, 9, 12],
                   [4, 7, 10, 13],
                   [6, 8, 11, 15]]

    rlt = find_matrix(test_case_1, 6)
    print(rlt)

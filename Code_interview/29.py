'''
顺时针打印矩阵
'''


def print_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    # print(rows, columns)

    row = 0
    col = 0

    while row * 2 < rows and col * 2 < columns:
        print_core(matrix, row, col, rows, columns)
        row += 1
        col += 1


def print_core(matrix, row, col, rows, columns):
    for i in range(col, columns-col):
        print(matrix[row][i])

    for i in range(row+1, rows-row):
        print(matrix[i][columns-col-1])

    # 需要对行数进行限制，防止只有一行时重复打印的情况
    if row+1 < rows-row:
        for i in range(columns-col-2, col-1, -1):
            print(matrix[rows-row-1][i])

    # 需要对列数进行限制，防止只有一列时重复打印的情况
    if col + 1 < columns-col:
        for i in range(rows-row-2, row, -1):
            print(matrix[i][col])


if __name__ == '__main__':
    test_case = [[1,2,3,1],
                 [5,6,7,1],
                 [9,10,11,1],
                 [12,13,14,1],
                 [15,16,17,1]
                 ]

    print_matrix(test_case)

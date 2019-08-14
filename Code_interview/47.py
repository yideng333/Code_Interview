'''
礼物的最大价值
'''


def get_max_value(matrix):
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    print(rows, cols)

    # value_matrix = [[0 for i in range(cols)] for j in range(rows)]
    value_matrix = [0 for i in range(cols)]
    print(value_matrix)

    for row in range(rows):
        for col in range(cols):
            if row > 0:
                # up = value_matrix[row-1][col]
                up = value_matrix[col]
            else:
                up = 0

            if col > 0:
                # left = value_matrix[row][col-1]
                left = value_matrix[col-1]
            else:
                left = 0

            # value_matrix[row][col] = max(up, left) + matrix[row][col]
            value_matrix[col] = max(up, left) + matrix[row][col]

    print(value_matrix)
    # return value_matrix[rows-1][cols-1]
    return value_matrix[cols-1]


if __name__ == '__main__':
    test = [[1, 10, 3, 8],
            [12, 2, 9, 6],
            [5, 7, 4, 11],
            [3, 7, 16, 5]]

    rlt = get_max_value(test)
    print(rlt)

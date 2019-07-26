'''
矩阵中的路径
'''


def find_path(matrix, string):
    row_nubmer = len(matrix)
    col_number = len(matrix[0])
    print(row_nubmer, col_number)

    visited = [[0 for i in range(col_number)] for j in range(row_nubmer)]
    k = 0
    for row in range(row_nubmer):
        for col in range(col_number):
            print(matrix[row][col])
            if (help_find(matrix, row_nubmer, col_number, row, col, string, k, visited)):
                return True

    return False


def help_find(matrix, rows, cols, row, col, string, k, visited):
    if k == len(string):
        return True

    if row >=0 and row < rows and col >=0 and col < cols \
            and visited[row][col] == 0 and matrix[row][col] == string[k]:
        visited[row][col] = 1
        k += 1
        has_path = help_find(matrix, rows, cols, row, col-1, string, k,  visited) or \
                   help_find(matrix, rows, cols, row-1, col, string, k,  visited) or \
                   help_find(matrix, rows, cols, row, col+1, string, k,  visited) or \
                   help_find(matrix, rows, cols, row+1, col, string, k, visited)
        if not has_path:
            k -= 1
            visited[row][col] = 0
            return False
        return True

    else:
        return False


if __name__ == '__main__':
    test_case_1 = [['a', 'b', 't', 'g'],
                   ['c', 'f', 'c', 's'],
                   ['j', 'd', 'e', 'h']]

    string = 'acfa'
    rlt = find_path(test_case_1, string)
    print(rlt)

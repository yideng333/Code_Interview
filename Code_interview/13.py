'''
机器人的运动范围
'''


def robot_move(threhold, rows, cols):

    visited = [[0 for i in range(cols)] for j in range(rows)]
    # print(visited)

    count = move_help(0, 0, rows, cols, visited, threhold)

    return count


def move_help(row, col, rows, cols, visited, threhold):
    count = 0
    if check(row, col, rows, cols, threhold, visited):
        # count += 1
        visited[row][col] = 1
        print(row, col)
        count = 1 + move_help(row-1, col, rows, cols, visited, threhold) + \
                move_help(row, col-1, rows, cols, visited, threhold) + \
                move_help(row+1, col, rows, cols, visited, threhold) + \
                move_help(row, col+1, rows, cols, visited, threhold)

    return count


def check(row, col, rows, cols, threhold, visited):
    if row >=0 and row < rows and col >=0 and col < cols and \
            get_sum(row) + get_sum(col) <= threhold and visited[row][col] == 0:
        return True
    else:
        return False


def get_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10

    return sum


if __name__ == '__main__':
    rlt = robot_move(18, 20, 20)
    print(rlt)

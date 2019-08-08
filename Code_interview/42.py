'''
连续子数组的最大和
'''


def get_max_sum(array):
    max_sum = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            # print(array[i:j+1])
            if sum(array[i:j+1]) > max_sum:
                max_sum = sum(array[i:j+1])
    print(max_sum)


def get_max_sum_2(array):

    cur_sum = 0
    total_sum = 0
    for i in range(len(array)):
        if cur_sum <= 0:
            cur_sum = array[i]
        else:
            cur_sum += array[i]

        if cur_sum > total_sum:
            total_sum = cur_sum

    print(total_sum)
    return total_sum


def get_max_sum_3(array):
    cur_sum = array[0]
    total_sum = array[0]

    for i in array[1:]:
        cur_sum = max(i, cur_sum + i)
        total_sum = max(total_sum, cur_sum)

    print(total_sum)


if __name__ == '__main__':
    test = [1, -2, 3, 10, -4, 7, 2, -5]
    get_max_sum_3(test)

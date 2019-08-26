'''
股票的最大利润
'''


def max_diff(array):
    if len(array) < 2:
        return 0

    min_number = array[0]
    max_money = array[1] - array[0]

    i = 1
    while i <= len(array)-1:
        if array[i] - min_number > max_money:
            max_money = array[i] - min_number

        if array[i] < min_number:
            min_number = array[i]

        i += 1

    return max_money


if __name__ == '__main__':
    test = [1, 2, 4, 7, 11, 16]
    rlt = max_diff(test)
    print(rlt)

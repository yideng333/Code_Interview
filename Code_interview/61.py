'''
扑克牌中的顺子
'''


def is_continues(array):
    array.sort()
    print(array)

    zero_cnt = 0
    gap_cnt = 0
    i = len(array) -1

    while i >= 0:
        if array[i] == 0:
            zero_cnt += 1
        if array[i] != 0 and array[i-1] != 0 and i - 1 >= 0 and array[i] - array[i-1] > 1:
            gap_cnt += (array[i] - array[i-1] -1)

        i -= 1

    print(zero_cnt, gap_cnt)

    if gap_cnt > zero_cnt:
        return False
    else:
        return True


if __name__ == '__main__':
    test = [1, 3, 0, 7, 0 ]
    rlt = is_continues(test)
    print(rlt)

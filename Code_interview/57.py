'''
和为S的数字
'''


def get_sum(array, number):
    if not array or number < 0:
        return -1

    first = 0
    end = len(array) - 1

    while first <= end:
        if array[first] + array[end] == number:
            return array[first], array[end]
        elif array[first] + array[end] > number:
            end -= 1
        else:
            first += 1

    return -1


def find_senquence(number):
    small = 1
    big = 2
    mid = (1+ number) >> 1
    print(mid)
    while small < mid:
        cnt = get_cnt(small, big)

        if cnt == number:
            print(small, big)

        if cnt > number:
            small += 1
        else:
            big += 1


def get_cnt(start, end):
    cnt = 0
    for i in range(start, end+1):
        cnt += i

    # print(cnt)
    return cnt


if __name__ == '__main__':
    # test1 = [1,2,4,7,11,15]
    # rlt = get_sum(test1, 17)
    # print(rlt)
    find_senquence(14)

'''
数组中出现次数超过一半的数字
'''


def count_number(array):
    number = array[0]
    count = 1

    for i in range(1, len(array)):

        if count == 0:
            number = array[i]
            count = 1
        elif array[i] == number:
            count += 1
        else:
            count -= 1

    return number


def partition(array, length, start, end):
    pivot = array[start]
    mark = start
    for i in range(start + 1, end):
        if array[i] < pivot:
            mark += 1
            array[i], array[mark] = array[mark], array[i]

    array[start], array[mark] = array[mark], array[start]

    return mark


def more_than_half(array):
    length = len(array)
    mid = length >> 1
    start = 0
    end = length

    index = partition(array, length, start, end)
    while index != mid:
        if index > mid:
            index = partition(array, length, start, index+1)
        else:
            index = partition(array, length, index+1, end)

    result = array[mid]
    print(index, mid, result)
    return result


if __name__ == '__main__':
    test1 = [2,4,2,4,4,2,2,4,4]
    test2 = [2,1,3,2,2,5,4,2]
    # rlt = count_number(test)
    rlt = more_than_half(test2)
    # print(rlt)
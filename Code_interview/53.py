'''
在排序数组中查找数字
'''


def find_first_k(array, number):
    start = 0
    end = len(array)

    while start <= end:
        mid = (end + start) >> 1
        # print(mid)
        if array[mid] == number:
            if mid == 0 or (mid > 0 and array[mid - 1] != number):
                return mid
            else:
                end = mid - 1
        elif array[mid] < number:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def find_last_k(array, number):
    start = 0
    end = len(array)

    while start <= end:
        mid = (end + start) >> 1
        # print(mid)
        if array[mid] == number:
            if mid == len(array) -1 or (mid < len(array)-1 and array[mid + 1] != number):
                return mid
            else:
                start = mid + 1
        elif array[mid] < number:
            start = mid + 1
        else:
            end = mid - 1

    return -1


'''
数字在排序数组中出现的次数
'''
def find_number(array, number):
    if not array:
        return -1

    first_index = find_first_k(array, number)
    last_index = find_last_k(array, number)
    print(first_index, last_index)

    if first_index != -1 and last_index != -1:
        return last_index - first_index + 1

    else:
        return -1


'''
0～n-1中缺失的数字
'''
def find_missing_number(array, length):
    if not array or length <= 0:
        return -1
    start = 0
    end = length

    while start <= end:
        mid = (start + end) >> 1

        if array[mid] != mid:
            if mid == 0 or array[mid-1] == mid - 1:
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1

    if start == length:
        return length

    return -1

'''
数组中数值和下标相等的元素
'''
def find_equal_number(array):
    if not array:
        return -1
    start = 0
    end = len(array)

    while start <= end:
        mid = (start + end) >> 1
        if mid == array[mid]:
            return mid
        elif mid > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == '__main__':
    # test1 = [1, 2, 2, 3, 3, 3, 4, 5]
    # rlt = find_number(test1, 2)
    # print(rlt)

    # test2 = [0,1,2,3,4,6]
    # rlt = find_missing_number(test2, 7)
    # print(rlt)

    test3 = [-1, 0, 1, 2, 5 ]
    rlt = find_equal_number(test3)
    print(rlt)

'''
数组使奇数位于偶数前面
'''


def reorder(array):
    if not array:
        return None

    start = 0
    end = len(array) -1

    while start <= end:

        # 前面的指针找偶数
        while array[start] & 0x1 != 0:
            start += 1

        # 后面的指针找奇数
        while array[end] & 0x1 != 1:
            end -= 1

        # if start > end:
        #     return array
        if start < end:
            array[start], array[end] = array[end], array[start]

    return array


if __name__ == '__main__':
    test_case_1 = [7,2,4,1,3,6,8,9]
    rlt = reorder(test_case_1)
    print(rlt)
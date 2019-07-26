'''
旋转数组最小数字
'''


def min_number(array):
    start = 0
    end = len(array)-1
    mid = start

    # 如果数组本身就是递增的，直接返回
    while array[start] >= array[end]:
        if end-start == 1:
            return array[end]

        mid = (end + start) // 2

        # 首尾中间三个数相等，只能顺序查找
        if array[start] == array[end] and array[mid] == array[start]:
            min = array[start]
            for i in range(start + 1, end):
                if array[i] < min:
                    min = array[i]
            return min

        if array[mid] >= array[start]:
            start = mid
        elif array[mid] <= array[start]:
            end = mid

    return array[mid]


if __name__ == '__main__':
    test_case_1 = [4,5,6,1,2,3]
    test_case_2 = [1,2,3,4,5,6]
    test_case_3 = [1,0,1,1,1,1]
    rlt = min_number(test_case_1)
    print(rlt)

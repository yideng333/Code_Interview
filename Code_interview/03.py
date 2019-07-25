'''
数组中重复的数字
'''


def find_duplication_1(array):
    if not array:
        return False

    d = {}
    for i in array:
        if d.get(i, 0) > 0:
            return True
        else:
            if d.get(i):
                d[i] += 1
            else:
                d[i] = 1
    return False


def find_duplication_2(array):
    if not array:
        return False

    for i in range(len(array)):
        while i != array[i]:
            # print(array)
            if array[i] == array[array[i]]:
                return True
            else:
                temp = array[array[i]]
                array[array[i]] = array[i]
                array[i] = temp
    return False


if __name__ == '__main__':
    test_case_1 = [2,3,1,0,2,5,3]
    test_case_2 = [2,4,6,0,1,3,6]
    test_case_3 = [2,3,5,4,3,2,6,7]
    # rlt = find_duplication_1(test_case_2)
    rlt = find_duplication_2(test_case_2)
    print(rlt)


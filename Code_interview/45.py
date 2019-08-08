'''
把数组排成最小的数
'''
from functools import cmp_to_key


def cmp(a,b):
    if a+b>b+a:
        return 1
    if a+b<b+a:
        return -1
    else:
        return 0


def PrintMinNumber(numbers):
    if not numbers:
        return ""
    number = list(map(str,numbers))
    number.sort(key=cmp_to_key(cmp))
    return "".join(number).lstrip('0') or '0'


def print_min_number(array):
    if not array:
        return

    array = list(map(str, array))

    for i in range(len(array)):
        sorted = False
        for j in range(len(array) -1):
            if cmp(array[j], array[j+1]) == 1:
                array[j], array[j + 1] = array[j+1], array[j]
                sorted = True
        if not sorted:
            break
    print(array)


if __name__ == '__main__':
    test = [3, 32, 321]
    # print(PrintMinNumber(test))
    print_min_number(test)

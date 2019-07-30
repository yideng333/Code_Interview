'''
打印从1到最大的n位数
'''


def print_max_n(n):
    number = ['0' for i in range(n)]
    print_help(0, n, number)


def print_help(begin, length, number):
    if begin == length:
        # print(number)
        print_with_nozero(number)
        return

    for i in range(10):
        number[begin] = str(i)
        print_help(begin+1, length, number)


def print_with_nozero(number):
    number_string = ''.join(number)
    number_string = number_string.lstrip('0')
    print(number_string)


if __name__ == '__main__':
    rlt = print_max_n(4)
    # print(rlt)

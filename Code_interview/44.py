'''
数字序列中某一位的数字
'''


def digit_at_x(n):
    digit_string = [i for i in range(n)]
    digit_string = ''.join(list(map(str, digit_string)))
    print(digit_string[n])
    return digit_string[n]


def digit_at_x_new(index):
    digits = 1

    while True:
        number = count_number(digits)
        if index < number * digits:
            return get_digit(index, digits)

        index -= number * digits
        digits += 1


# m位的数字总共有多少位
def count_number(digits):
    if digits == 1:
        return 10

    count = pow(10, digits-1)

    return count * 9


def get_digit(index, digits):
    print(index)
    number = begin_number(digits) + index // digits
    print(number)
    index_right = digits - index % digits
    print(index_right)
    for i in range(1, index_right):
        number = number // 10

    print(number % 10)
    return number % 10


def begin_number(index):
    if index == 1:
        return 0

    return pow(10, index - 1)


if __name__ == '__main__':
    # digit_at_x(1001)
    digit_at_x_new(1001)
    # print(count_number(3))

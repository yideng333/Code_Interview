'''
数值的整数次方
'''


def power_of_n(n, exp):
    if exp == 0:
        return 1

    if exp == 1:
        return n

    # exp >>1 右移1位等于除以2
    result = power_of_n(n, exp >> 1)
    result *= result
    if exp & 0x1 == 1:
        result *= n

    return result


if __name__ == '__main__':
    rlt = power_of_n(2, 10)
    print(rlt)

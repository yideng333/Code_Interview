'''
不用加减乘除做加法
'''


def get_sum(num1, num2):
    while num2 != 0:
        res = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = res
        num2 = carry
    return num1


if __name__ == '__main__':
    rlt = get_sum(5,17)
    print(rlt)
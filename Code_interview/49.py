'''
丑数
'''


def is_ugly_number(number):

    while number % 2 == 0:
        number = number // 2

    while number % 3 == 0:
        number = number // 3

    while number % 5 == 0:
        number = number // 5

    if number == 1:
        return True
    else:
        return False


def get_ugly_number(index):
    number = [0 for i in range(index)]
    number[0] = 1
    ugly_2 = ugly_3 = ugly_5 = 0

    i = 1
    while i < index:
        next_ugly = min(number[ugly_2]*2, number[ugly_3]*3, number[ugly_5]*5)
        number[i] = next_ugly

        while number[ugly_2]*2 <= next_ugly:
            ugly_2 += 1
        while number[ugly_3]*3 <= next_ugly:
            ugly_3 += 1
        while number[ugly_5]*5 <= next_ugly:
            ugly_5 += 1

        i += 1

    # print(number)
    return number[-1]


if __name__ == '__main__':
    # print(is_ugly_number(14))
    rlt = get_ugly_number(1500)
    print(rlt)
'''
数组中数字出现的次数
'''


'''
数组中只出现1次的两个数字
'''
def get_one_number(array):
    if not array:
        return -1

    temp = array[0]
    for i in range(1, len(array)):
        temp = temp ^ array[i]

    print(temp)

    index = 0
    while (temp & 1) == 0:
        temp = temp >> 1
        index += 1

    print(index)

    number1 = 0
    number2 = 0
    for number in array:
        if is_bit(number, index):
            number1 ^= number
        else:
            number2 ^= number

    print(number1, number2)


def is_bit(number, index):
    number = number >> index
    if number & 1 == 1:
        return True
    else:
        return False


'''
数组中唯一只出现一次的数字
'''
def get_number(array):
    if not array:
        return -1

    bit_array = [0 for i in range(32)]

    for i in array:
        # print(i)
        bit_mask = 1
        for j in range(32)[::-1]:

            bit = i & bit_mask
            if bit != 0:
                bit_array[j] += 1
            bit_mask = bit_mask << 1

    # print(bit_array)

    number = 0
    for i in range(32):
        number = number << 1
        number += bit_array[i] % 3

    print(number)


if __name__ == '__main__':
    # test1 = [2,4,3,6,3,2,5,5]
    # get_one_number(test1)

    test2 = [2,6,2,2,4,4,4]
    get_number(test2)

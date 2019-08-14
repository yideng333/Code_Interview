'''
把数字翻译成字符串
'''


# 递归解法
def translation(number):

    if len(number) <= 1:
        return 1

    if number[0] != '0' and number[0:2] and int(number[0:2]) < 26:
        cnt = translation(number[1:]) + translation(number[2:])
    else:
        cnt = translation(number[1:])

    return cnt


# DP
def translation_new(number):
    i = len(number)
    cnt_list = [0 for i in range(len(number) + 1)]
    cnt_list[i] = 1
    i -= 1
    cnt_list[i] = 1
    i -= 1
    while i >= 0:
        digit1 = int(number[i])
        digit2 = int(number[i+1])

        # print(digit1, digit2)
        if 10 <= digit1 * 10 + digit2 <= 25:
            count = cnt_list[i + 1] + cnt_list[i + 2]
        else:
            count = cnt_list[i+1]

        cnt_list[i] = count
        # print(cnt_list)
        i -= 1

    return cnt_list[0]


if __name__ == '__main__':
    # rlt = translation(str(2258))
    rlt = translation_new(str(12258))
    print(rlt)
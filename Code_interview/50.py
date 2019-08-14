'''
第一个只出现一次的字符
'''


def first_not_repeting_char(string):
    d = {}
    for i in string:
        if d.get(i) is None:
            d[i] = 1
        else:
            d[i] += 1

    for i in string:
        if d.get(i) == 1:
            return i


if __name__ == '__main__':
    test = 'abaccdeff'
    rlt =first_not_repeting_char(test)
    print(rlt)

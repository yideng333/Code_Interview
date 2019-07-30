'''
表示数值的字符串
'''
import re


def check(string):
    if not string:
        return False

    patten = re.compile(r'^[+|-]?\d+\.?\d+$|^[+|-]?\d+[e|E]?[+|-]?\d+$')

    m = patten.match(string)
    print(m)
    # print(string)
    if m:
        print(m.group(0))
        return True
    else:
        return False


if __name__ == '__main__':
    test_case_1 = '0.034'
    rlt = check(test_case_1)
    print(rlt)
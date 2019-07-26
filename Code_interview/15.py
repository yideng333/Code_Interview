'''
二进制中1的个数
'''

def number_of_one_v1(n):
    count = 0
    flag = 1

    while(flag < n):
        print(flag)
        if n & flag:
            count += 1

        flag = flag << 1

    return count


def number_of_one_v2(n):
    count = 0
    while(n):
        count += 1
        # 去掉最低位的1
        n = (n-1) & n

    return count


if __name__ == '__main__':
    rlt = number_of_one_v2(10)
    print(rlt)

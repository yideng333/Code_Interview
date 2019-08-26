'''
圆圈中最后剩下的数字
'''


def last_remaining(n, m):
    if m < 1 or n < 1:
        return -1

    last = 0

    i = 2
    while i <= n:
        last = (last + m) % i
        i += 1

    return last


if __name__ == '__main__':
    rlt = last_remaining(5, 3)
    print(rlt)

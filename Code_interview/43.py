'''
1~n整数中1出现的次数
'''


def get_number_of_one(n):
    cnt = 0
    for i in range(1, n+1):
       cnt += number_of_one(i)

    print(cnt)
    return cnt


def number_of_one(n):
    cnt = 0
    while n:
        if n % 10 == 1:
            cnt += 1
        n = n // 10

    return cnt


if __name__ == '__main__':
    get_number_of_one(100)
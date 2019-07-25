'''
斐波那契数列
'''


def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_new(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    temp = 0
    i = 2
    while i <= n:
        temp = a + b
        a = b
        b = temp
        i += 1

    return temp


if __name__ == '__main__':
    rlt = fib_new(10)
    print(rlt)

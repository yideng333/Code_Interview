'''
剪绳子
f(n) = max(f(i) * f(n-i))
'''


# 递归解法
def cut_role_recursive(n):
    if n < 2:
        return 0
    if n < 3:
        return 1
    if n < 4:
        return 2

    return help_cut(n)


def help_cut(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    max = 0
    for i in range(1, n//2 + 1):
        number = help_cut(i) * help_cut(n - i)
        if number > max:
            max = number

    return max


# 动态规划
def cut_role_dp(n):
    if n < 2:
        return 0
    if n < 3:
        return 1
    if n < 4:
        return 2

    product = [0] * (n+1)
    product[0] = 0
    product[1] = 1
    product[2] = 2
    product[3] = 3

    for i in range(4, n + 1):
        max = 0
        for j in range(1, i //2 +1):
            number = product[j] * product[i-j]
            if number > max:
                max = number
        product[i] = max

    print(product)

    return product[n]


if __name__ == '__main__':
    # rlt = cut_role_recursive(8)
    rlt = cut_role_dp(8)
    print(rlt)

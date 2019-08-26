'''
n个骰子的点数
'''


def print_probability(n):
    dp = [[0 for i in range(6 * n)] for i in range(n)]

    for i in range(6):
        dp[0][i] = 1

    print(dp)

    for i in range(1, n):  # 1，相当于2个骰子。
        for j in range(i, 6 * (i + 1)):  # [0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
            dp[i][j] = dp[i - 1][j - 6] + dp[i - 1][j - 5] + dp[i - 1][j - 4] + \
                       dp[i - 1][j - 3] + dp[i - 1][j - 2] + dp[i - 1][j - 1]

    print(dp)
    cnt_sum = 6 ** n
    count = [i / cnt_sum for i in dp[n - 1]] # 算得骰子投出每一个点数的频数。再除以总的排列数即可得到频率
    return count


if __name__ == '__main__':
    rlt = print_probability(2)
    print(rlt)

'''
字符串的排列组合
'''


# 排列
def permutation(string, start, length):
    if not string:
        return

    if start == length:
        print(''.join(string))
        return
    else:
        for i in range(start, length):
            string[i], string[start] = string[start], string[i]
            permutation(string, start+1, length)
            string[i], string[start] = string[start], string[i]


# 组合
def combination(list, size):
    if size == 0 or not list:
        return [[]]
    else:
        result = []
        for i in range(0, (len(list) - size) + 1):
            # 从i处截断
            pick = list[i:i+1]
            rest = list[i+1:]
            # 截断位置后的list继续组合
            for j in combination(rest, size - 1):
                print(pick, j)
                result.append(pick + j)
            # print(result)
        return result


if __name__ == '__main__':
    string = 'abcd'
    permutation(list(string), 0, len(string))
    # print(combination(list(string), 3))
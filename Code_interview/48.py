'''
最长不含重复字符的子字符串
'''


def get_substring(string):
    position = {}

    max_length = [0 for i in range(len(string))]

    for i in range(len(string)):
        if position.get(string[i]) is None:
            if i > 0:
                max_length[i] = max_length[i-1] + 1
            else:
                max_length[i] = 1
        else:
            d = i - position.get(string[i])
            if d <= max_length[i-1]:
                max_length[i] = d
            else:
                max_length[i] = max_length[i-1] + 1

        position[string[i]] = i

    print(max_length)
    print(position)
    return max_length[-1]


if __name__ == '__main__':
    test = 'arabcacfr'
    rlt = get_substring(test)
    print(rlt)

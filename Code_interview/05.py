'''
字符串替换空格
'''


# 算法复杂度O(n)实现方式
def replace_space(string):
    string = list(string)
    length = len(string)
    space_nubmer = 0
    for i in string:
        if i == ' ':
            space_nubmer += 1
    print(space_nubmer)

    for i in range(space_nubmer * 2):
        string.append(' ')

    new_length = length + space_nubmer * 2 - 1
    print(new_length)
    length -= 1

    print(string)
    while length >= 0:
        if string[length] != ' ':
            string[new_length] = string[length]
            length -= 1
            new_length -= 1
        else:
            string[new_length] = '0'
            new_length -= 1
            string[new_length] = '2'
            new_length -= 1
            string[new_length] = '%'
            new_length -= 1
            length -= 1

    print(string)
    return ''.join(string)


if __name__ == '__main__':
    test_case_1 = 'my happy world'
    print(test_case_1.replace(' ', '%20'))
    rlt = replace_space(test_case_1)
    print(rlt)

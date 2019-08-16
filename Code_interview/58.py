'''
翻转字符串
'''


def get_reverse(string):
    if not string:
        return ''

    string = reverse_core(string)
    string = string.split(' ')
    print(string)

    new_string = []
    for s in string:
        new_string.append(reverse_core(s))

    return ' '.join(new_string)


def reverse_core(string):
    s_list = list(string)
    s_list = s_list[::-1]
    return ''.join(s_list)


if __name__ == '__main__':
    test = 'i am a student'
    rlt = get_reverse(test)
    print(rlt)
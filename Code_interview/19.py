'''
正则表达式匹配
'''


def match(string, patten):
    if not string or not patten:
        return False

    return match_help(string, patten, 0, 0)


def match_help(string, patten, s, p):
    if s == len(string)-1 and p == len(patten) -1:
        return True

    if s != len(string)-1 and p == len(patten) -1:
        return False

    if patten[p+1] == '*':
        if string[s] == patten[p] or patten[p] == '.':
            return match_help(string, patten, s+1, p+2) or \
                    match_help(string, patten, s +1, p) or \
                    match_help(string, patten, s, p + 2)
        else:
            return match_help(string, patten, s, p + 2)

    if string[s] == patten[p] or patten[p] == '.':
        return match_help(string, patten, s +1, p +1)

    return False


if __name__ == '__main__':
    rlt = match('abc', 'ac*bc')
    print(rlt)

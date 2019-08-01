'''
栈的压入弹出序列
'''


def is_order(push_order, pop_order):
    if not push_order or not pop_order or len(pop_order) != len(push_order):
        return False

    stack = []

    i = 0
    j = 0
    while i < len(push_order):
        stack.append(push_order[i])
        while j < len(pop_order):
            if len(stack) > 0 and stack[-1] == pop_order[j]:
                stack.pop()
                j += 1
            else:
                break
        i += 1

    print(stack)

    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    push_order = [1,2,3,4,5]
    pop_order = [4,3,5,1,2]
    rlt = is_order(push_order, pop_order)
    print(rlt)

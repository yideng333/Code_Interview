'''
二叉搜索树的后序遍历序列
'''


def is_post_order(array, start, end):
    if not array:
        return False

    node_val = array[end]

    i = start
    while i < end:
        if array[i] > node_val:
            break
        i += 1

    j = i
    while j < end:
        if array[j] < node_val:
            return False
        j += 1

    left = True
    if i > start:
        left = is_post_order(array, start, i-1)

    right = True
    if i < end:
        right = is_post_order(array, i, end-1)

    return left and right


if __name__ == '__main__':
    test_case_1 = [5,7,6,9,11,10,8]
    test_case_2 = [7,4,6,5]
    rlt = is_post_order(test_case_2, 0, len(test_case_2)-1)
    print(rlt)
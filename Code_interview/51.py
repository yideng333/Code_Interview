'''
数组中的逆序对
'''

cnt = 0


def get_reverse_number(array):
    if len(array) == 1:
        return array

    mid = len(array) >> 1

    left = get_reverse_number(array[:mid])
    right = get_reverse_number(array[mid:])

    return merge(left, right)


def merge(left, right):
    global cnt
    i = 0
    j = 0

    m_array = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            m_array.append(left[i])
            i += 1

        elif right[j] < left[i]:
            cnt += len(left) - i
            m_array.append(right[j])
            j += 1

    m_array += left[i:]
    m_array += right[j:]

    return m_array


if __name__ == '__main__':
    test = [6, 5, 4, 3, 2, 1]
    print(get_reverse_number(test))
    print(cnt)

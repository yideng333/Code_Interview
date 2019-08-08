'''
最小的k个数
'''


def partition(array, length, start, end):
    pivot = array[start]
    mark = start
    for i in range(start + 1, end):
        if array[i] < pivot:
            mark += 1
            array[i], array[mark] = array[mark], array[i]

    array[start], array[mark] = array[mark], array[start]

    return mark


def most_k_small(array, k):
    length = len(array)
    start = 0
    end = length

    index = partition(array, length, start, end)
    while index != k-1:
        if index > k-1:
            index = partition(array, length, start, index+1)
        else:
            index = partition(array, length, index+1, end)

    result = [array[i] for i in range(k)]
    return result


def most_k_small_2(array, k):
    result = []
    for i in array:
        if len(result) < k:
            result.append(i)
        else:
            max_index = result.index(max(result))
            if i < max(result):
                result[max_index] = i

    return result


if __name__ == '__main__':
    test1 = [2,4,2,4,4,2,2,4,4]
    test2 = [2,1,3,2,2,5,4,2]
    test3 = [6,8,9,7,2,3,4,1]
    # rlt = count_number(test)
    rlt = most_k_small_2(test3, 4)
    print(rlt)

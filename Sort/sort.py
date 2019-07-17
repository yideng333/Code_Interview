'''
排序算法实现
'''


# 冒泡排序
def bubble_sort(array):
    length = len(array)
    for i in range(length):
        sorted = True
        for j in range(length-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
                sorted = False

        if sorted:
            # 这一轮没有做过交换，说明已经排完序了就直接退出
            break
        # print(array)

    return array


# 选择排序
def select_sort(array):
    for i in range(len(array)):
        max_index = i
        # 找出最小元素的下标
        for j in range(i+1, len(array)):
            if array[j] < array[max_index]:
                max_index = j

        # 交换max_index和i位置上的值
        array[max_index], array[i] = array[i], array[max_index]
        print(array)

    return array


# 插入排序
def insert_sort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i-1
        # 从i-1的位置向前找到插入点
        while j >= 0 and array[j] > value:
            # if array[j] < value:
            array[j+1] = array[j]
            # else:
            #     break
            j -= 1
        # 插入元素
        array[j+1] = value
        print(array)
    return array


# 希尔排序 (插入排序的升级版)
def shell_sort(array):
    def insert(array, gap):
        for i in range(gap, len(array)):
            j = i - gap
            value = array[i]
            while j >= 0 and array[j] > value:
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = value

    gap = 1
    while gap < len(array):
        gap = gap * 3 + 1
    while gap > 0:
        print(gap)
        # 每次按区间进行插入排序
        insert(array, gap)
        gap = gap // 3
    return array


# 归并排序
def merge_sort(array):
    def merge(l_array, r_array):
        i = 0
        j = 0
        m_array = []
        while i < len(l_array) and j < len(r_array):
            if l_array[i] < r_array[j]:
                m_array.append(l_array[i])
                i += 1

            elif r_array[j] <= l_array[i]:
                m_array.append(r_array[j])
                j += 1
        m_array += l_array[i:]
        m_array += r_array[j:]

        return m_array

    # print(array)
    length = len(array)
    if length == 1:
        return array

    mid = length // 2
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


# 快速排序
def quick_sort(array, start_index, end_index):
    if end_index <= start_index:
        return

    mark = start_index
    # 取基准值
    pivot = array[start_index]
    i = start_index + 1
    while i <= end_index:
        # 小于基准值，则mark+1，交换位置
        if array[i] < pivot:
            mark += 1
            array[mark], array[i] = array[i], array[mark]
        i += 1

    # 基准值与mark交换位置， mark中就是基准值的位置
    array[start_index], array[mark] = array[mark], array[start_index]
    # print(array)

    # 基准值左右两部分递归排序
    quick_sort(array, start_index, mark - 1)
    quick_sort(array, mark + 1,  end_index)

    return array


# 堆排序
def heap_sort(array):
    # 下沉指定元素
    def shift_down(array, index, length):
        left_child = 2 * index + 1  # 左子节点下标
        right_child = 2 * index + 2  # 右子节点下标
        present = index  # 要调整的节点下标

        # 下沉左边
        if left_child < length and array[left_child] > array[present]:
            present = left_child

        # 下沉右边
        if right_child < length and array[right_child] > array[present]:
            present = right_child

        # 如果下标不相等 证明调换过了
        if present != index:
            array[index], array[present] = array[present], array[index]
            # 继续下沉
            shift_down(array, present, length)

    length = len(array)
    # 构建大顶堆
    i = length // 2
    while i >= 0:
        shift_down(array, i, length)
        i -= 1

    print(array)

    i = length - 1
    while i > 0:
        # 将堆顶元素交换到最后
        array[0], array[i] = array[i], array[0]
        length -= 1
        shift_down(array, 0, length)
        i -= 1
    return array


# 计数排序
def count_sort(array):
    max_number = array[0]
    for i in range(1, len(array)):
        if array[i] > max_number:
            max_number = array[i]

    help_list = [0] * max_number

    for i in range(len(array)):
        help_list[array[i]-1] += 1
    print(help_list)
    k = 0
    for i in range(len(help_list)):
        if help_list[i] > 0:
            array[k] = i+1
            k += 1
    return array


if __name__ == '__main__':
    l1 = [11, 8, 9, 2, 5, 6, 1, 7]

    # l2 = bubble_sort(l1)
    # l2 = select_sort(l1)
    # l2 = insert_sort(l1)
    # l2 = shell_sort(l1)
    # l2 = merge_sort(l1)
    # l2 = quick_sort(l1, 0, len(l1)-1)
    # l2 = heap_sort(l1)
    l2 = count_sort(l1)
    print(l2)

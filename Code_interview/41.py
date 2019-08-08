'''
数据流中的中位数
'''
import heapq


# 使用两个大小堆实现
def get_midden(array):
    min_list = []
    max_list = []

    i = 0
    while i < len(array):
        insert(array[i], min_list, max_list)
        i += 1

    if len(min_list) + len(max_list) & 1 == 1:
        midden = min_list[0]
    else:
        midden = ((max_list[0] * -1) + min_list[0]) / 2
    print(max_list)
    print(min_list)
    print(midden)
    return midden


def insert(number, min_list, max_list):

    # 总长度为偶数
    if len(min_list) + len(max_list) & 1 == 0:
        # 如果该数小于最大堆中的最大数，那么需要交换取出最大数
        if len(max_list) > 0 and number < max_list[0] * -1:
            heapq.heappush(max_list, number * -1)
            number = heapq.heappop(max_list) * -1

        # 将元素插入最小堆
        heapq.heappush(min_list, number)

    else:
        # 如果该数大于最小堆中的最小数，那么需要交换取出最小数
        if len(min_list) > 0 and number > min_list[0]:
            heapq.heappush(min_list, number)
            number = heapq.heappop(min_list)
        # 将元素插入最大堆
        heapq.heappush(max_list, number * -1)


if __name__ == '__main__':
    test1 = [2,4,2,4,4,2,2,4,4]
    test2 = [2,1,3,6,2,5,4,2,8]
    get_midden(test2)

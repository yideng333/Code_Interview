'''
队列的最大值
'''
from collections import deque


def slide_window(array, size):
    queue = deque()
    res = []

    i = 0
    while i < size:
        queue.append(array[i])
        i += 1

    res.append(max(queue))

    for i in range(size, len(array)):
        # print(array[i])
        queue.popleft()
        queue.append(array[i])
        res.append(max(queue))
    print(res)
    return res


def max_slide_window(array, size):
    queue = deque()
    res = []

    for index, val in enumerate(array):
        if len(queue) > 0 and index - queue[0] >= size:
            queue.popleft()

        while len(queue) > 0 and array[queue[-1]] < val:
            queue.pop()

        queue.append(index)

        if index + 1 >= size:
            res.append(array[queue[0]])

    print(res)


if __name__ == '__main__':
    test = [2,3,4,2,6,3,5,1]
    # slide_window(test, 2)
    max_slide_window(test, 3)

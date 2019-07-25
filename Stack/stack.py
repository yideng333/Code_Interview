import logging
'''
栈相关操作
'''


# 使用数组实现栈
class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            logging.error('stack is empty')

    def push(self, x):
        self.stack.append(x)

    def peak(self):
        if self.stack:
            return self.stack[-1]
        else:
            logging.error('stack is empty')

    def length(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 使用链表实现栈
class Stack_new(object):
    def __init__(self):
        self.next = None

    def push(self, x):
        temp = Node(x)
        temp.next = self.next
        self.next = temp

    def pop(self):
        if self.next is not None:
            temp = self.next.next
            self.next = temp
        else:
            raise LookupError('stack is empty!')

    def peak(self):
        if self.next is not None:
            return self.next.val
        else:
            raise LookupError('stack is empty!')

    def length(self):
        i = 0
        cur = self.next
        while cur is not None:
            cur = cur.next
            i += 1
        return i


# 用两个队列实现栈
class stack_by_2_queues(object):
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        if len(self.queue2) == 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            raise LookupError('stack is empty!')

        if len(self.queue2) == 0:
            for i in range(len(self.queue1)-1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            for i in range(len(self.queue2)-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)


if __name__ == '__main__':
    stack1 = stack_by_2_queues()
    stack1.push(7)
    stack1.push(8)
    stack1.push(9)
    # print(stack1.length())
    # print(stack1.peak())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    stack1.push(10)
    stack1.push(1)
    print(stack1.pop())
    print(stack1.pop())
    # print(stack1.length())
    # print(stack1.peak())

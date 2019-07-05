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


if __name__ == '__main__':
    stack1 = Stack_new()
    stack1.push(7)
    stack1.push(8)
    stack1.push(9)
    print(stack1.length())
    print(stack1.peak())
    stack1.pop()
    print(stack1.length())
    print(stack1.peak())

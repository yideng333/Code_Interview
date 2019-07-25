'''
队列相关操作
'''


class Head(object):
    def __init__(self):
        self.left = None
        self.right = None


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 使用链表实现队列
class Queue(object):
    def __init__(self):
        self.head = Head()

    def enqueue(self, x):
        node = Node(x)
        p = self.head
        # 队列中已经有元素了
        if p.right:
            temp = p.right
            p.right = node
            temp.next = node
        else:
            p.right = node
            p.left = node

    def dequeue(self):
        p = self.head
        # 只有一个元素
        if p.left and (p.left == p.right):
            temp = p.left
            p.left = None
            p.right = None
            return temp.val
        elif p.left and (p.left != p.right):
            temp = p.left
            p.left = temp.next
            return temp.val

        else:
            raise LookupError('queue is empty!')

    def is_empty(self):
        if self.head.left:
            return False
        else:
            return True

    def top(self):
        # 查询目前队列中最早入队的元素
        if self.head.left:
            return self.head.left.val
        else:
            raise LookupError('queue is empty!')


# 用两个栈实现队列
class Queue_by_2_stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        # 如果stack2为空, 将stack1的元素挪到stack2中
        if not self.stack2:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            raise LookupError('queue is empty!')

        return self.stack2.pop()


if __name__ == '__main__':
    queue1 = Queue_by_2_stacks()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(5)
    # print(queue1.top())
    print(queue1.dequeue())
    print(queue1.dequeue())
    queue1.enqueue(3)
    queue1.enqueue(8)
    print(queue1.dequeue())
    print(queue1.dequeue())
    queue1.enqueue(9)
    print(queue1.dequeue())
    print(queue1.dequeue())
    # print(queue1.dequeue())
    # print(queue1.top())

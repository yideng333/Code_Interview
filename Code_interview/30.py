'''
包含min函数的栈
'''


class MinStack():
    def __init__(self):
        self.m_data = []
        self.m_min = []

    def push(self, x):
        self.m_data.append(x)

        if not self.m_min:
            self.m_min.append(x)
        else:
            if x <= self.m_min[-1]:
                self.m_min.append(x)

    def pop(self):
        if len(self.m_data) == 0:
            raise LookupError('stack is empty!')
        val = self.m_data.pop()
        if val == self.m_min[-1]:
            self.m_min.pop()

        return val

    def min(self):
        if len(self.m_min) == 0:
            raise LookupError('stack is empty!')
        return self.m_min[-1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(5)
    stack.push(6)
    print(stack.min())
    print(stack.pop())
    print(stack.min())
    print(stack.pop())
    print(stack.min())
    print(stack.pop())
    print(stack.pop())
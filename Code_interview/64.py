'''
求1+2+...+n
'''

all_sum = 0


def get_sum(n):
    global all_sum
    all_sum += n
    n -= 1
    return n > 0 and get_sum(n)


if __name__ == '__main__':
    get_sum(5)
    print(all_sum)
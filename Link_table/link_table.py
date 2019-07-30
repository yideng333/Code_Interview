import copy
'''
链表相关操作(带头节点)
'''


# 定义链表结构体
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 构建一个长度为l的链表
def generate_LNode(l):
    # 头节点
    head = Node(None)
    cur = head
    for i in range(l):
        temp = Node(i)
        cur.next = temp
        cur = temp
    return head


# 根据列表中的元素构建链表
def generate_LNode_from_list(array):
    # 头节点
    head = Node(None)
    cur = head
    for i in array:
        temp = Node(i)
        cur.next = temp
        cur = temp
    return head


# 顺序打印元素
def print_LNode(head):
    cur = head
    templist = []
    while cur:
        templist.append(str(cur.val))
        cur = cur.next
    print('-->'.join(templist))


# 逆序打印元素(递归)
def recursive_reverse_print_LNode(head):
    if not head:
        return
    recursive_reverse_print_LNode(head.next)
    print(head.val)


# 逆序打印元素
def reverse_print_LNode(head):
    cur = head
    stack = []
    res = []
    while cur:
        stack.append(cur.val)
        cur = cur.next
    for i in range(len(stack) - 1, -1, -1):
        res.append(str(stack[i]))
    print('-->'.join(res))


# 链表逆序(插入法)
def reverse_LNode(head):
    cur = head.next.next
    next = None
    head.next.next =None
    while cur:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next
    return head


# 链表逆序(递归法)
def recursive_reverse_LNode(head):
    def recursive_part(head):
        if not head.next:
            return head
        cur = head
        new_head = recursive_part(cur.next)
        head.next.next = cur
        cur.next = None
        return new_head

    if not head or not head.next:
        return None
    # 从头节点的下一个节点开始
    new_head = recursive_part(head.next)
    head.next = new_head
    return head


# 合并两个有序链表
def merge_two_LNode(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.val <= head2.val:
        head1.next = merge_two_LNode(head1.next, head2)
        return head1
    else:
        head2.next = merge_two_LNode(head1, head2.next)
        return head2


# 找到倒数第K个元素
def find_last_k_element(head, k):
    if not head or not head.next:
        return
    fast = head.next
    slow = head.next

    # 快指针先走k步
    i = 0
    while i < k:
        fast = fast.next
        i += 1

    # 快慢指针同时走，快指针走到链表底时，慢指针就是倒数第k个元素
    while fast is not None:
        slow = slow.next
        fast = fast.next

    print(slow.val)


# 找到链表中点
def find_middle(head):
    if not head or not head.next:
        return head

    fast = head.next
    slow = head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


# 链表插入排序
def insertionSortList(head):
    dummy = Node(-1)
    cur = dummy
    # p = copy.deepcopy(head)
    p = head
    while p is not None:
        # 找到插入点
        while cur.next is not None and cur.next.val < p.val:
            cur = cur.next
        # 插入元素
        next = p.next
        p.next = cur.next
        cur.next = p
        p = next
        # 指针归位
        cur = dummy

    return dummy.next


# 链表归并排序
def mergeSortList(head):
    def findmiddle(head):
        if not head:
            return head

        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def merge(lhead, rhead):
        dummy = Node(-1)
        cur = dummy

        while lhead and rhead:
            if lhead.val < rhead.val:
                cur.next = lhead
                lhead = lhead.next
            else:
                cur.next = rhead
                rhead = rhead.next
            cur = cur.next

        if lhead:
            cur.next = lhead
        if rhead:
            cur.next = rhead
        return dummy.next

    if not head or not head.next:
        return head

    middle = findmiddle(head)
    rhead = middle.next
    middle.next = None

    return merge(mergeSortList(head), mergeSortList(rhead))


if __name__ == '__main__':
    head1 = generate_LNode(8)
    # print_LNode(head1)
    # middle_head = findmiddle(head1.next)
    # print(middle_head.val)
    # print_LNode(middle_head)

    # head2 = generate_LNode(10)
    # print_LNode(head1)
    # print_LNode(head2)
    # head3 = merge_two_LNode(head1.next, head2.next)
    # print_LNode(head3)
    # head.next = head.next.next
    # print_LNode(head)

    new_head = reverse_LNode(head1)
    print_LNode(new_head)

    new_head1 = mergeSortList(new_head.next)
    # new_head1 = insertionSortList(new_head.next)
    print_LNode(new_head1)
    # print_LNode(head1)

    # print_LNode(head1)
    # find_last_k_element(head1, 3)

    # reverse_print_LNode(head)
    # head_new = copy.deepcopy(head)
    # new_head = reverse_LNode(head)
    # print_LNode(new_head)
    # new_head = recursive_reverse_LNode(head)
    # print_LNode(new_head)

    # recursive_reverse_print_LNode(head)

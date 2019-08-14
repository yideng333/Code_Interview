'''
两个链表的第一个公共节点
'''
from Link_table.link_table import generate_LNode_from_list, print_LNode


def first_common_node(head1, head2):
    l1 = get_length(head1)
    l2 = get_length(head2)

    if l2 > l1:
        head_long = head2
        head_short = head1
    else:
        head_long = head1
        head_short = head2

    for i in range(abs(l2-l1)):
        head_long = head_long.next

    while head_long is not None and head_short is not None and head_long.val != head_short.val:
        head_long = head_long.next
        head_short = head_short.next

    return head_long


def get_length(head):
    length = 0
    cur = head
    while cur:
        cur = cur.next
        length += 1

    return length


if __name__ == '__main__':
    head1 = generate_LNode_from_list([1, 2, 3, 4, 5, 6, 7])
    print_LNode(head1)
    head2 = generate_LNode_from_list([8, 9, 6, 7])
    print_LNode(head2)

    rlt = first_common_node(head1, head2)
    print(rlt.val)

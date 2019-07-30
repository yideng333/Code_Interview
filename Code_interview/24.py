'''
反转链表
'''
from Link_table.link_table import generate_LNode_from_list, print_LNode


def reverse_list(head):
    cur = head.next
    pre = None

    while cur:
        # print(cur.val)
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    head.next = pre
    return head


if __name__ == '__main__':
    head1 = generate_LNode_from_list([1, 4, 5, 7, 2, 9, 12])
    print_LNode(head1)
    head2 = reverse_list(head1)
    print_LNode(head2)

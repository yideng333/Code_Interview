'''
合并有序链表
'''
from Link_table.link_table import generate_LNode_from_list, print_LNode


def merge_two_list(head1, head2):
    if not head1:
        return head2
    elif not head2:
        return head1

    if head1.val <= head2.val:
        head1.next = merge_two_list(head1.next, head2)
        return head1
    else:
        head2.next = merge_two_list(head1, head2.next)
        return head2


if __name__ == '__main__':
    head1 = generate_LNode_from_list([1, 4, 5, 7, 9, 12])
    print_LNode(head1)
    head2 = generate_LNode_from_list([2, 3, 6, 10, 13])
    print_LNode(head2)

    head3 = merge_two_list(head1.next, head2.next)
    print_LNode(head1)
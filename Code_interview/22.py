'''
链表中倒数第K个节点
'''
from Link_table.link_table import generate_LNode_from_list, print_LNode


def find_k_node(head, k):
    if not head or k == 0:
        return

    length = 0
    fast = head
    while fast:
        fast = fast.next
        length += 1

    print(length)
    if length < k:
        return

    fast = head
    i = 0
    while i < k:
        fast = fast.next
        i += 1

    slow = head
    while fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == '__main__':
    head1 = generate_LNode_from_list([1, 4, 5, 7, 9, 12])
    print_LNode(head1)

    node = find_k_node(head1, 6)
    if node:
        print(node.val)

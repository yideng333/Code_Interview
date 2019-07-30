'''
链表中环的入口
'''
from Link_table.link_table import generate_LNode_from_list, print_LNode


def make_circle(head, n):
    cur = head
    circle_node = None
    while cur.next is not None:
        if cur.val == n:
            circle_node = cur
        cur = cur.next

    cur.next = circle_node
    return head


def meeting_node(head):
    if not head.next or not head.next.next:
        return None
    slow = head.next
    fast = head.next.next

    while fast and slow:
        if fast == slow:
            return fast
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

    return None


def find_meeting_node(head):
    m_node = meeting_node(head)
    if not m_node:
        return None

    cur = m_node.next
    node_number = 1
    while cur != m_node:
        cur = cur.next
        node_number += 1

    print('circle length:', node_number)

    p_cur = head
    p_next = m_node

    while p_cur != p_next:
        p_cur = p_cur.next
        p_next = p_next.next

    print('circle meeting node:', p_cur.val)
    return p_cur


if __name__ == '__main__':
    # head1 = generate_LNode(10)
    head1 = generate_LNode_from_list([1,4,5,7,2,9,12])
    print_LNode(head1)
    head1 = make_circle(head1, 4)
    # node = meeting_node(head1)
    # print(node.val)
    find_meeting_node(head1)
    # print_LNode(head1)

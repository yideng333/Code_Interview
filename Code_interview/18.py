'''
删除链表的节点
'''
from Link_table.link_table import generate_LNode_from_list, print_LNode


def delete_node(head, node):
    if not head or not node:
        return

    # 删除的节点不是最后一个
    if node.next is not None:
        next = node.next
        node.val = next.val
        node.next = next.next
        next.next = None

    # 只有一个节点
    elif head == node:
        return None

    # 删除尾节点
    else:
        cur = head
        while cur.next != node:
            cur = cur.next
        cur.next = None

    return head


def get_node(head, val):
    cur = head
    while cur:
        if cur.val == val:
            return cur
        cur = cur.next


if __name__ == '__main__':
    head1 = generate_LNode_from_list([1, 4, 5, 7, 9, 12])
    print_LNode(head1)

    node = get_node(head1, 1)
    print(node.val)

    head1 = delete_node(head1, node)
    print_LNode(head1)

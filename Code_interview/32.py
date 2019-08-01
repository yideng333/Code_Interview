'''
从上到下打印二叉树
'''
from Tree.binary_tree import BinaryTree
import pprint
pp = pprint.PrettyPrinter(indent=2)


def print_level(root):
    if not root:
        return

    queue = []
    queue.append(root)

    while queue:
        r = queue.pop(0)
        print(r.val)
        if r.left:
            queue.append(r.left)
        if r.right:
            queue.append(r.right)


def print_level_2(root):
    if not root:
        return

    queue = []
    queue.append(root)

    print()
    # level_number = 1
    print_number = 1
    next_level_number = 0
    while queue:
        r = queue.pop(0)
        print(r.val)
        print_number -= 1

        if r.left:
            queue.append(r.left)
            next_level_number += 1
        if r.right:
            queue.append(r.right)
            next_level_number += 1

        if print_number == 0:
            print('-----')
            print_number = next_level_number
            next_level_number = 0


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_node_by_list([5,2,1,12,6,8,13,15,20,23])
    pp.pprint(tree1.get_dict_form())

    print_level_2(tree1.root)

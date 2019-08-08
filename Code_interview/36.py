'''
二叉搜索树与双向链表
'''
from Tree.binary_tree import BinaryTree
import pprint
pp = pprint.PrettyPrinter(indent=2)


def transform(root, last_node):
    if root is None:
        return

    if root.left:
        last_node = transform(root.left, last_node)

    root.left = last_node

    if last_node is not None:
        last_node.right = root

    last_node = root

    if root.right:
        last_node = transform(root.right, last_node)

    return last_node


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_rank_node_by_list([10,6,14,4,8,12,16])
    pp.pprint(tree1.get_dict_form())

    last_node = transform(tree1.root, None)
    new_root = last_node
    while (new_root and new_root.left):
        print(new_root.val)
        new_root = new_root.left


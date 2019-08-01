'''
二叉树镜像
'''
from Tree.binary_tree import BinaryTree
import pprint
pp = pprint.PrettyPrinter(indent=2)
from copy import deepcopy


def get_mirror_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left

    get_mirror_tree(root.left)
    get_mirror_tree(root.right)

    return root


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_node_by_list([5,2,1,12,6,8,13,15,20,23])
    pp.pprint(tree1.get_dict_form())

    tree2 = BinaryTree()
    tree2.root = get_mirror_tree(deepcopy(tree1.root))
    pp.pprint(tree2.get_dict_form())

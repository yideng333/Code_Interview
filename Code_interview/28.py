'''
对称二叉树
'''
from Tree.binary_tree import BinaryTree
import pprint
pp = pprint.PrettyPrinter(indent=2)
# from copy import deepcopy


def is_symmetrical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val == root2.val:
        return is_symmetrical(root1.left, root2.right) and is_symmetrical(root1.right, root2.left)
    else:
        return False


if __name__ == '__main__':
    tree1 = BinaryTree()
    test_case1 = [8,6,6,5,7,7,5]
    test_case2 = [7,7,7,7,7,7,7]
    tree1.add_node_by_list(test_case1)
    pp.pprint(tree1.get_dict_form())

    rlt = is_symmetrical(tree1.root, tree1.root)
    print(rlt)
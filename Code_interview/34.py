'''
二叉树和为某一值的路径
'''
from Tree.binary_tree import BinaryTree
import pprint
pp = pprint.PrettyPrinter(indent=2)


def get_sum_path(root, number, path):
    # print(path)
    if root is None:
        return

    if root.val == number:
        path.append(root.val)
        for i in path:
            print(i)
        print('--------')

    if root.left:
        get_sum_path(root.left, number-root.val, path + [root.val])

    if root.right:
        get_sum_path(root.right, number-root.val, path + [root.val])


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_node_by_list([10, 5, 2, 4, 7, 10])
    pp.pprint(tree1.get_dict_form())

    get_sum_path(tree1.root, 22, [])


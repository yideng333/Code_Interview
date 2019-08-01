'''
树的子结构
'''
from Tree.binary_tree import BinaryTree
import pprint
pp = pprint.PrettyPrinter(indent=2)


def has_sub_tree(root1, root2):
    result = False
    if root1 and root2:
        # 节点值相等，开始比较
        if root1.val == root2.val:
            result = compare(root1, root2)

        if not result:
            # 比较左边节点
            result = has_sub_tree(root1.left, root2)

        if not result:
            # 比较右边节点
            result = has_sub_tree(root1.right, root2)

    return result


def compare(root1, root2):
    # root2已经匹配完了
    if root2 is None:
        return True

    # root1已经匹配完了
    if root1 is None:
        return False

    if root1.val == root2.val:
        return compare(root1.left, root2.left) and compare(root1.right, root2.right)
    else:
        return False


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_node_by_list([5,2,1,12,6,8,13,15,20,23])
    # pp.pprint(tree1.get_dict_form())

    tree2 = BinaryTree()
    tree2.add_node_by_list([12,15,20])
    # pp.pprint(tree2.get_dict_form())

    rlt = has_sub_tree(tree1.root, tree2.root)
    print(rlt)

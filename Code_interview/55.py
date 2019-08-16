'''
二叉树的深度
'''
from Tree.binary_tree import BinaryTree


def get_depth(root):
    if not root:
        return 0

    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)

    return max(left_depth, right_depth) + 1

'''
平衡的二叉树
'''
def is_balanced_tree(root):
    if not root:
        return True

    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)

    if abs(left_depth - right_depth) > 1:
        return False

    return is_balanced_tree(root.left) and is_balanced_tree(root.right)


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_rank_node_by_list([5,3,7,2,4])
    rlt = get_depth(tree1.root)
    print(rlt)
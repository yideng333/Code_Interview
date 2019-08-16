'''
二叉搜索树的第k大节点
'''
from Tree.binary_tree import BinaryTree
import copy


cnt = 0
def get_top_K_node(root, k):
    global cnt
    if not root:
        return None

    if root.left:
        target = get_top_K_node(root.left, k)
    else:
        target = None

    if target is None:
        cnt += 1
        if cnt == k:
            # print(root.val)
            target = root

    if target is None and root.right:
        target = get_top_K_node(root.right, k)

    return target


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_node_by_list([5,3,7,2,4,6,8])
    print('----')
    r1 = get_top_K_node(tree1.root, 4)
    print(r1.val)
    print(r1.dict_form())
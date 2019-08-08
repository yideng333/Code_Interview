'''
序列化二叉树
'''
from Tree.binary_tree import BinaryTree, Node
import pprint
pp = pprint.PrettyPrinter(indent=2)


def serialize(root, array):
    if root is None:
        array.append('$')
        return array

    array.append(root.val)
    array = serialize(root.left, array)
    array = serialize(root.right, array)
    return array


def de_serialize(root, array):
    number = array.pop(0)
    if number != '$':
        root = Node(number)

        root.left = de_serialize(root.left, array)
        root.right = de_serialize(root.right, array)

    return root


if __name__ == '__main__':
    tree1 = BinaryTree()
    tree1.add_node_by_list([10,6,14,4,8,12])
    pp.pprint(tree1.get_dict_form())

    array = serialize(tree1.root, [])

    print(array)
    array = [10, 6, 4, '$', '$', '$', 14, 12, '$', '$', '$']
    tree2 = BinaryTree()
    tree2.root = de_serialize(tree2.root, array)
    pp.pprint(tree2.get_dict_form())

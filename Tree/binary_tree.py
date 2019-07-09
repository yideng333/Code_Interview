'''
二叉树相关操作
'''
import pprint
pp = pprint.PrettyPrinter(indent=2)


# 定义节点
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dict_form(self):
        dict_set = {
            "val": self.val,
            "left": self.left,
            "right": self.right,
        }
        return dict_set


# 定义二叉树
class BinaryTree(object):

    def __init__(self):
        self.root = None

    # 按照顺序增加节点(非递归)
    def add_node(self, x):
        # 根节点为空
        if self.root is None:
            self.root = Node(x)
        else:
            # 声明一个队列
            queue = list()
            queue.append(self.root)
            while queue:
                root = queue.pop(0)
                if root.left is None:
                    root.left = Node(x)
                    return
                elif root.right is None:
                    root.right = Node(x)
                    return
                else:
                    queue.append(root.left)
                    queue.append(root.right)

    # 按照顺序增加节点(递归)
    def add_node_recursive(self, node, x):
        # 根节点为空
        if self.root is None:
            self.root = Node(x)
            return self.root
        else:
            # 左节点为空
            if node.left is None:
                node.left = Node(x)
                return self.root
            # 右节点为空
            if node.right is None:
                node.right = Node(x)
                return self.root

            if node.left.left is None or node.left.right is None:
                # 左节点的子节点有一个为空
                self.add_node_recursive(node.left, x)
            elif node.right.left is None or node.right.right is None:
                # 右节点的子节点有一个为空
                self.add_node_recursive(node.right, x)
            else:
                # 左右两个节点的子节点都满了，默认从左边节点开始遍历
                self.add_node_recursive(node.left, x)

    # 增加二叉搜索树的节点
    def add_rank_node(self, node, x):
        # 根节点为空
        if self.root is None:
            self.root = Node(x)
            return self.root
        else:
            if x == node.val:
                print('node {} already exisit'.format(x))
                return self.root
            if x < node.val:
                if node.left is None:
                    node.left = Node(x)
                    return self.root
                else:
                    self.add_rank_node(node.left, x)
            if x >= node.val:
                if node.right is None:
                    node.right = Node(x)
                    return self.root
                else:
                    self.add_rank_node(node.right, x)

    def add_rank_node_by_list(self, elements_list):
        for element in elements_list:
            print(element)
            self.add_rank_node(self.root, element)

    def add_node_by_list(self, elements_list, type='normal'):
        for element in elements_list:
            if type == 'normal':
                self.add_node(element)
            elif type == 'recursive':
                self.add_node_recursive(self.root, element)
            else:
                print('type is not exist')

    def get_dict_form(self):
        # 根节点为空
        if self.root is None:
            return {}
        else:
            node_queue = list()
            dict_queue = list()
            node_queue.append(self.root)
            dict_pack = self.root.dict_form()
            dict_queue.append(dict_pack)
            while node_queue:
                root = node_queue.pop(0)
                dict_root = dict_queue.pop(0)
                if root.left is not None:
                    node_queue.append(root.left)
                    dict_root['left'] = root.left.dict_form()
                    dict_queue.append(dict_root['left'])
                if root.right is not None:
                    node_queue.append(root.right)
                    dict_root['right'] = root.right.dict_form()
                    dict_queue.append(dict_root['right'])
            return dict_pack

    def pre_order_recursive(self, node):
        if node is None:
            return node
        print(node.val)
        self.pre_order_recursive(node.left)
        self.pre_order_recursive(node.right)

    def pre_order_nonrecursive(self):
        if self.root is None:
            return

        # 声明一个栈
        stack = list()
        node = self.root
        while node or stack:
            while node:
                print(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

    def mid_order_recursive(self, node):
        if node is None:
            return node
        self.mid_order_recursive(node.left)
        print(node.val)
        self.mid_order_recursive(node.right)

    def mid_order_nonrecursive(self):
        if self.root is None:
            return

        # 声明一个栈
        stack = list()
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            print(node.val)
            node = node.right

    def post_order_recursive(self, node):
        if node is None:
            return node
        self.post_order_recursive(node.left)
        self.post_order_recursive(node.right)
        print(node.val)

    # 后序遍历为前序的镜像
    def post_order_nonrecursive(self):
        if self.root is None:
            return

        # 声明一个栈
        stack = list()
        output_stack = list()
        node = self.root
        while node or stack:
            while node:
                output_stack.append(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left

        while output_stack:
            print(output_stack.pop())

    # 最大层数
    def depth(self, node):
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    tree = BinaryTree()

    element_list = [5, 2, 1, 12, 6, 8, 13, 15, 20, 23]
    tree.add_node_by_list(element_list, 'normal')
    # tree.add_rank_node_by_list(element_list)
    print(tree.get_dict_form())
    pp.pprint(tree.get_dict_form())

    # 前序遍历
    # tree.pre_order_recursive(tree.root)
    # tree.pre_order_nonrecursive()

    # 中序遍历
    # tree.mid_order_recursive(tree.root)
    # tree.mid_order_nonrecursive()

    # 后序遍历
    # tree.post_order_recursive(tree.root)
    # tree.post_order_nonrecursive()

    # 最大深度
    depth = tree.depth(tree.root)
    print(depth)

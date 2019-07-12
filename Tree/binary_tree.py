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
        self.ans = []

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

    # 层次遍历
    def level_order(self):
        res = []
        # 根节点为空
        if self.root is None:
            return res
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                q = queue.pop(0)
                print(q.val)
                if q.left:
                   queue.append(q.left)
                if q.right:
                    queue.append(q.right)

    # 打印每层元素 (层次遍历)
    def print_level_order(self):
        res = []
        # 根节点为空
        if self.root is None:
            return res
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                res.append([node.val for node in queue])
                new_queue = []
                for q in queue:
                    if q.left:
                        new_queue.append(q.left)
                    if q.right:
                        new_queue.append(q.right)
                queue = new_queue

        return res

    # 最大层数
    def depth(self, node):
        if node is None:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        return max(left_depth, right_depth) + 1

    def list_to_tree(self, node, elements_list):
        start = 0
        end = len(elements_list) - 1
        mid = (end - start) // 2
        # print(elements_list)
        if node is None:
            node = Node(elements_list[mid])

        if len(elements_list) > 1:
            if start < mid:
                node.left = self.list_to_tree(node.left, elements_list[start:mid])
            if mid < end:
                node.right = self.list_to_tree(node.right, elements_list[mid+1:])
            return node
        else:
            return node

    # 路径之和
    def path_sum(self, node, num):
        if node is None:
            return False

        if not node.left and not node.right:
            return node.val == num

        left = self.path_sum(node.left, num-node.val)
        right = self.path_sum(node.right, num-node.val)
        return left or right

    # 路径之和，返回路径
    def path_sum_2(self, node, num, path):
        if node is None:
            return
        # 节点是叶子节点且值满足条件
        # if not node.left and not node.right and node.val == num:
        #     self.ans.append(path + [node.val])

        # 任意节点的值满足条件
        if node.val == num:
            self.ans.append(path + [node.val])

        # if node.left:
        self.path_sum_2(node.left, num-node.val, path + [node.val])
        # if node.right:
        self.path_sum_2(node.right, num-node.val, path + [node.val])

    # 路径之和(任意起点和终点)
    def path_sum_3(self, node, num, path):
        if node is None:
            return

        self.path_sum_2(node, num, path)
        self.path_sum_3(node.left, num, path)
        self.path_sum_3(node.right, num, path)

    # 根据前序和中序顺序构造二叉树
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = Node(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root
        return None


if __name__ == '__main__':
    tree = BinaryTree()

    # element_list = [5, 2, 1, 12, 6, 8, 13, 15, 20, 23]
    # tree.add_node_by_list(element_list, 'normal')
    # # tree.add_rank_node_by_list(element_list)
    # print(tree.get_dict_form())
    # pp.pprint(tree.get_dict_form())

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
    # depth = tree.depth(tree.root)
    # print(depth)

    # 层序遍历
    # tree.level_order()

    # 按层打印
    # res = tree.print_level_order()
    # print(res)

    # 根据中序遍历序列构造二叉树
    # element_list = [5, 2, 4, 7, 8, 9, 10, 13]
    # tree.root = tree.list_to_tree(tree.root, element_list)
    # tree.root = tree.list_to_tree_new(element_list, 0, len(element_list))
    # print('-' * 20)
    # print(res)

    # 路径之和
    # print(tree.path_sum(tree.root, 39))

    # 路径之和3
    # tree.path_sum_3(tree.root, 13, [])
    # print(tree.ans)

    # 根据前序和中序顺序构造二叉树
    # preorder = [3, 9, 20, 15, 7]
    # inorder = [9, 3, 15, 20, 7]
    # tree.root = tree.buildTree(preorder, inorder)
    # res = tree.print_level_order()
    # print('-' * 20)
    # print(res)

from binary_search.BinaryTree import BinaryTree
from binary_search.Node import Node


class AVLTree(BinaryTree):
    def _insert(self, node, value):
        if value <= node.value:
            if node.left_node is None:
                node.left_node = Node(value, parent=node)
                self.update_balance(node.left_node)
            else:
                self._insert(node.left_node, value)
        else:
            if node.right_node is None:
                node.right_node = Node(value, parent=node)
                self.update_balance(node.right_node)
            else:
                self._insert(node.right_node, value)

    def update_balance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return

        if node.parent is not None:
            if node.is_left_child():
                node.parent.balanceFactor += 1
            elif node.is_right_child():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balanceFactor > 0:
            if node.left_node.balanceFactor < 0:
                self.rotate_left(node.left_node)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
        elif node.balanceFactor < 0:
            if node.right_node.balanceFactor > 0:
                self.rotate_right(node.right_node)
                self.rotate_left(node)
            else:
                self.rotate_left(node)

    def rotate_left(self, node):
        new_root = node.right_node
        node.right_node = new_root.left_node

        if new_root.left_node is not None:
            new_root.left_node.parent = node

        new_root.parent = node.parent

        if node.parent is None:
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_node = new_root
            else:
                node.parent.right_node = new_root

        new_root.left_node = node
        node.parent = new_root

        node.balanceFactor = node.balanceFactor + 1 - min(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor + 1 + max(node.balanceFactor, 0)

    def rotate_right(self, node):
        new_root = node.left_node
        node.left_node = new_root.right_node

        if new_root.right_node is not None:
            new_root.right_node.parent = node

        new_root.parent = node.parent

        if node.parent is None:
            self.root = new_root
        else:
            if node.is_left_child():
                node.parent.left_node = new_root
            else:
                node.parent.right_node = new_root

        new_root.right_node = node
        node.parent = new_root

        node.balanceFactor = node.balanceFactor - 1 - max(new_root.balanceFactor, 0)
        new_root.balanceFactor = new_root.balanceFactor - 1 + min(node.balanceFactor, 0)

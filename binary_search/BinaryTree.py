from binary_search.Node import Node


class BinaryTree(object):
    def __init__(self, *args):
        self.__root = None
        self.size = 0

        if args is not None:
            for i in args:
                self.insert(i)

    def length(self):
        return self.size

    def breadth_first(self):
        current_level = [self.__root]
        while current_level:
            next_level = list()
            print([e.value for e in current_level])
            for n in current_level:
                if n.left_node:
                    next_level.append(n.left_node)
                if n.right_node:
                    next_level.append(n.right_node)
            print("-----")
            current_level = next_level
        print('\n')

    def min(self):
        return self.__root.min()

    def max(self):
        node = self.__root

        while node.right_node is not None:
            node = node.right_node

        return node.value

    def insert(self, value):
        if self.__root is None:
            self.__root = Node(value)
        else:
            self._insert(self.__root, value)

        self.size += 1

    def _insert(self, node, value):
        if value <= node.value:
            if node.left_node is None:
                node.left_node = Node(value, parent=node)
            else:
                self._insert(node.left_node, value)
        else:
            if node.right_node is None:
                node.right_node = Node(value, parent=node)
            else:
                self._insert(node.right_node, value)

    def _get(self, node, value):
        if not node:
            return None
        elif node.value == value:
            return node
        elif node.value < value:
            return self._get(node.right_node, value)
        else:
            return self._get(node.left_node, value)

    def contains(self, value):
        if self._get(self.__root, value):
            return True
        return False

    def delete(self, value):
        if self.size > 1:
            node = self._get(self.__root, value)
            if node:
                self._remove(node)
                self.size -= 1
            else:
                raise KeyError('Error, value not in tree')
        elif self.size == 1 and self.__root.value == value:
            self.__root = None
            self.size = 1
        else:
            raise KeyError('Error, value not in tree')

    def _remove(self, node):
        if node.is_leaf():  # node has no child
            if node == node.parent.left_node:
                node.parent.left_node = None
            else:
                node.parent.right_node = None

        elif node.has_both_children():
            succ = node.find_successor()
            succ.splice_out()
            node.value = succ.value

        else:  # node has only one child
            if node.has_left_child():  # node has only a left child
                if node.is_left_child():
                    node.left_node.parent = node.parent
                    node.parent.left_node = node.left_node
                elif node.is_right_child():
                    node.left_node.parent = node.parent
                    node.parent.right_node = node.left_node
                else:  # node is root
                    node.replace_node(node.left_node.value, node.left_node.left_node, node.left_node.right_node)
            else:  # node has only a right child
                if node.is_left_child():
                    node.right_node.parent = node.parent
                    node.parent.left_node = node.right_node
                elif node.is_right_node():
                    node.right_node.parent = node.parent
                    node.parent.right_node = node.right_node
                else:  # node is root
                    node.replace_node(node.right_node.value, node.right_node.left_node, node.right_node.right_node)

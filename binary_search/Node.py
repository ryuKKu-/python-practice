class Node(object):
    def __init__(self, value=None, left_node=None, right_node=None, parent=None):
        self.__value = value
        self.__left_node = left_node
        self.__right_node = right_node
        self.__parent = parent
        self.balanceFactor = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left_node(self):
        return self.__left_node

    @left_node.setter
    def left_node(self, node):
        self.__left_node = node

    @property
    def right_node(self):
        return self.__right_node

    @right_node.setter
    def right_node(self, node):
        self.__right_node = node

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, node):
        self.__parent = node

    def __str__(self):
        return "value : " + str(self.value) + ", parent : " + (str(self.parent.value) if self.parent else 'None')

    def is_leaf(self):
        return self.left_node is None and self.right_node is None

    def has_left_child(self):
        return self.left_node

    def has_right_child(self):
        return self.right_node

    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()

    def has_any_children(self):
        return self.has_left_child() or self.has_right_child()

    def is_left_child(self):
        return self.parent and self.parent.left_node == self

    def is_right_child(self):
        return self.parent and self.parent.right_node == self

    def replace_node(self, value, left_child, right_child):
        self.value = value
        self.left_node = left_child
        self.right_node = right_child

        if self.has_left_child():
            self.left_node.parent = self

        if self.has_right_child():
            self.right_node.parent = self

    def find_min(self):
        node = self
        while node.left_node is not None:
            node = node.left_node

        return node

    def find_successor(self):
        succ = None

        if self.has_right_child():
            succ = self.right_node.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_node = None
                    succ = self.parent.find_successor()
                    self.parent.right_node = self
        return succ

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_node = None
            else:
                self.parent.right_node = None

        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_node = self.left_node
                else:
                    self.parent.right_node = self.left_node
                self.left_node.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_node = self.right_node
                else:
                    self.parent.right_node = self.right_node
                self.right_node.parent = self.parent

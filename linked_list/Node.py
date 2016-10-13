class Node(object):
    def __init__(self, value=None, next_node=None):
        self.__value = value
        self.__next = next_node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, x):
        self.__value = x

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, node):
        self.__next = node

    def __str__(self):
        return str(self.__value)

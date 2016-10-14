from linked_list.Node import Node


class LinkedList(object):
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.next_node
        return output

    def __len__(self):
        if not self.head:
            return 0
        else:
            current = self.head
            count = 0
            while current:
                count += 1
                current = current.next_node
            return count

    def is_empty(self):
        return self.head is None

    def push_front(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node

    def push_back(self, value):
        if not self.head:
            self.push_front(value)
        else:
            node = Node(value)
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = node

    def pop_front(self):
        if not self.head:
            raise IndexError("Unable to pop from empty list")
        else:
            head = self.head
            self.head = self.head.next_node
            return "Pop front : %s" % str(head)

    def pop_back(self):
        if not self.head:
            raise IndexError("Unable to pop back from empty list")
        else:
            tail = self.head
            while tail.next_node.next_node:
                tail = tail.next_node
            value = tail.next_node.value
            tail.next_node = None
            return "Pop back : %s" % str(value)

    def front(self):
        if self.head:
            return self.head.value
        else:
            return None

    def back(self):
        if self.head:
            current = self.head
            for _ in range(0, len(self) - 1):
                current = current.next_node
            return current.value
        else:
            return None

    def value_at(self, idx):
        if self.head:
            if idx >= len(self):
                raise IndexError("Index %d is out of boundaries" % idx)
            else:
                current = self.head
                for _ in range(0, idx):
                    current = current.next_node
                return current.value
        else:
            raise IndexError("No value was inserted in the linked list")

    def insert_at(self, idx, value):
        if self.head:
            if idx > len(self):
                raise IndexError("Index %d is out of boundaries" % idx)
            else:
                if idx == 0:
                    self.push_front(value)
                elif idx == len(self):
                    self.push_back(value)
                else:
                    current = self.head
                    for i in range(0, idx-1):
                        current = current.next_node
                    temp = current.next_node
                    node = Node(value, temp)
                    current.next_node = node
        else:
            raise IndexError("No value was inserted in the linked list")

    def reverse(self):
        if self.head.next_node:
            temp = self.head
            self.head = None
            while temp:
                self.push_front(temp.value)
                temp = temp.next_node

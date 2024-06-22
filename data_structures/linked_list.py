class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if not prev_node:
            print("Previous node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next
        current = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("")

llist = LinkedList()
llist.insert_at_beginning(4)
llist.insert_at_beginning(41)
llist.insert_at_end(5)
print(llist.search(41).data)
llist.print_list()
"""Плюсом зв'язкових списків є можливість додавання елементів в  початок списку  О(1), в кінці списку О(n), пошук та видалення елементів О(n)"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node doesn't exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node

    def insert_before(self,next_node, data):
        if not next_node:
            return
        new_node = Node(data)
        new_node.prev = next_node.prev
        next_node.prev = new_node
        new_node.next = next_node
        if new_node.prev:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def search(self, target_data):
        current = self.head
        while current:
            if current.data == target_data:
                return current
            current = current.next
        return None

    def search_from_tail(self, target_data):
        current = self.tail
        while current:
            if current.data == target_data:
                return current
            current = current.prev
        return None

    def remove(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                current_node.prev = None
                current_node.next = None
                return True
            current_node = current_node.next
        return False





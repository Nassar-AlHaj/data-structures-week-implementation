class Node:
    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.next = nxt


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_first(self, elem):
        node = Node(elem, None, self.head)
        if self.is_empty():
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.size += 1

    def add_last(self, elem):
        node = Node(elem, self.tail, None)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        return data

    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def peek_first(self):
        return None if self.is_empty() else self.head.data

    def peek_last(self):
        return None if self.is_empty() else self.tail.data

    def __len__(self):
        return self.size

    def __iter__(self):
        trav = self.head
        while trav:
            yield trav.data
            trav = trav.next

    def __str__(self):
        vals = []
        trav = self.head
        while trav:
            vals.append(str(trav.data))
            trav = trav.next
        return "[ " + ", ".join(vals) + " ]"

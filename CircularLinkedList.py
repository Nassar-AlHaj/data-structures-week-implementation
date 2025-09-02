class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.head = self.tail = node
            self.tail.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.size -= 1
        return data

    def peek(self):
        return None if self.is_empty() else self.head.data

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.is_empty():
            return
        trav = self.head
        first_pass = True
        while trav and (first_pass or trav != self.head):
            yield trav.data
            trav = trav.next
            first_pass = False

    def __str__(self):
        if self.is_empty():
            return "[]"
        vals = []
        trav = self.head
        first_pass = True
        while trav and (first_pass or trav != self.head):
            vals.append(str(trav.data))
            trav = trav.next
            first_pass = False
        return "[ " + ", ".join(vals) + " ]"

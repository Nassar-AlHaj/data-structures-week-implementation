class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem)
        else:
            self.tail.next = Node(elem)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem)
        else:
            self.head = Node(elem, self.head)
        self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return data

    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Empty list")
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            trav = self.head
            while trav.next != self.tail:
                trav = trav.next
            self.tail = trav
            self.tail.next = None
        self.size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_first()
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        data = prev.next.data
        prev.next = prev.next.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1
        return data

    def index_of(self, obj):
        index = 0
        trav = self.head
        while trav:
            if trav.data == obj:
                return index
            trav = trav.next
            index += 1
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

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

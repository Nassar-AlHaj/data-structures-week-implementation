class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


class LinkedListStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, elem):
        self.top = Node(elem, self.top)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def __len__(self):
        return self.size

    def __str__(self):
        vals = []
        trav = self.top
        while trav:
            vals.append(str(trav.data))
            trav = trav.next
        return "[ " + ", ".join(vals) + " ]"

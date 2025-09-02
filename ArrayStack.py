class ArrayStack:
    def __init__(self, capacity=10):
        self.arr = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, elem):
        if self.size == len(self.arr):
            raise RuntimeError("Stack is full")
        self.arr[self.size] = elem
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        self.size -= 1
        elem = self.arr[self.size]
        self.arr[self.size] = None
        return elem

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.arr[self.size - 1]

    def __len__(self):
        return self.size

    def __str__(self):
        return "[ " + ", ".join(str(self.arr[i]) for i in range(self.size)) + " ]"

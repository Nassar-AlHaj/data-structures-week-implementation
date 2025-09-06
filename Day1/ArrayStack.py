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


def test_array_stack():
    print("Testing ArrayStack...")
    
    stack = ArrayStack(5)
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"After pushing 10, 20, 30: {stack}")
    print(f"Size: {len(stack)}")
    
    print(f"Top element (peek): {stack.peek()}")
    print(f"Stack after peek: {stack}")
    
    popped = stack.pop()
    print(f"Popped element: {popped}")
    print(f"Stack after pop: {stack}")
    
    stack.push(40)
    stack.push(50)
    print(f"After pushing 40, 50: {stack}")
    
    try:
        stack.push(60)
        stack.push(70)
    except RuntimeError as e:
        print(f"Expected error when stack is full: {e}")
    
    print("Popping all elements:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}, Stack: {stack}")
    
    try:
        stack.peek()
    except IndexError as e:
        print(f"Expected error when peeking empty stack: {e}")
    
    try:
        stack.pop()
    except IndexError as e:
        print(f"Expected error when popping empty stack: {e}")
    
    print("ArrayStack tests completed successfully!\n")


if __name__ == "__main__":
    test_array_stack()

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


def test_linked_list_stack():
    print("Testing LinkedListStack...")
    
    stack = LinkedListStack()
    print(f"Empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    print(f"Size: {len(stack)}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"After pushing 10, 20, 30: {stack}")
    print(f"Size: {len(stack)}")
    
    print(f"Top element (peek): {stack.peek()}")
    print(f"Stack after peek: {stack}")
    print(f"Size after peek: {len(stack)}")
    
    popped = stack.pop()
    print(f"Popped element: {popped}")
    print(f"Stack after pop: {stack}")
    print(f"Size after pop: {len(stack)}")
    
    stack.push(40)
    stack.push(50)
    print(f"After pushing 40, 50: {stack}")
    
    print("Popping all elements:")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped}, Stack: {stack}, Size: {len(stack)}")
    
    print(f"Final empty stack: {stack}")
    print(f"Is empty: {stack.is_empty()}")
    
    try:
        stack.peek()
    except IndexError as e:
        print(f"Expected error when peeking empty stack: {e}")
    
    try:
        stack.pop()
    except IndexError as e:
        print(f"Expected error when popping empty stack: {e}")
    
    stack.push(100)
    print(f"Single element stack: {stack}")
    print(f"Peek single element: {stack.peek()}")
    popped = stack.pop()
    print(f"Popped single element: {popped}")
    print(f"Stack after popping single element: {stack}")
    
    print("Testing with many elements...")
    for i in range(1000):
        stack.push(i)
    print(f"Stack with 1000 elements - Size: {len(stack)}")
    print(f"Top element: {stack.peek()}")
    
    print("First 10 popped elements:", end=" ")
    for _ in range(10):
        print(stack.pop(), end=" ")
    print()
    print(f"Size after popping 10 elements: {len(stack)}")
    
    print("LinkedListStack tests completed successfully!\n")


if __name__ == "__main__":
    test_linked_list_stack()

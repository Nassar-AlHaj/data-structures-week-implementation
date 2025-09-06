class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

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
        values = []
        trav = self.head
        first_pass = True
        while trav and (first_pass or trav != self.head):
            values.append(str(trav.data))
            trav = trav.next
            first_pass = False
        return "[ " + ", ".join(values) + " ]"

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

    def add_first(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.head = self.tail = node
            self.tail.next = self.head
        else:
            node.next = self.head
            self.head = node
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
            self.tail.next = self.head
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

    def peek(self):
        return None if self.is_empty() else self.head.data

    def peek_last(self):
        return None if self.is_empty() else self.tail.data

    def contains(self, elem):
        if self.is_empty():
            return False
        trav = self.head
        first_pass = True
        while trav and (first_pass or trav != self.head):
            if trav.data == elem:
                return True
            trav = trav.next
            first_pass = False
        return False

    def index_of(self, elem):
        if self.is_empty():
            return -1
        index, trav, first_pass = 0, self.head, True
        while trav and (first_pass or trav != self.head):
            if trav.data == elem:
                return index
            trav = trav.next
            index += 1
            first_pass = False
        return -1

    def rotate(self, steps=1):
        if self.is_empty() or self.size == 1:
            return
        steps = steps % self.size
        if steps == 0:
            return
        for _ in range(steps):
            self.head = self.head.next
            self.tail = self.tail.next

    def clear(self):
        self.head = self.tail = None
        self.size = 0


# Test Functions
def test_circular_linked_list():
    print("Testing CircularLinkedList...")

    cll = CircularLinkedList()
    print(f"Empty list: {cll}")
    print(f"Is empty: {cll.is_empty()}")
    print(f"Size: {len(cll)}")

    # Add elements
    cll.add(10)
    cll.add(20)
    cll.add(30)
    print(f"After adding 10, 20, 30: {cll}")

    cll.add_first(5)
    print(f"After adding 5 at beginning: {cll}")
    print(f"Size: {len(cll)}")

    # Peek
    print(f"First element (peek): {cll.peek()}")
    print(f"Last element (peek): {cll.peek_last()}")

    # Search
    print(f"Contains 20: {cll.contains(20)}")
    print(f"Contains 99: {cll.contains(99)}")
    print(f"Index of 20: {cll.index_of(20)}")
    print(f"Index of 99: {cll.index_of(99)}")

    # Remove
    first = cll.remove_first()
    print(f"Removed first: {first}, List: {cll}")

    last = cll.remove_last()
    print(f"Removed last: {last}, List: {cll}")

    cll.add(40)
    cll.add(50)
    print(f"After adding 40, 50: {cll}")

    removed = cll.remove_at(1)
    print(f"Removed element at index 1: {removed}, List: {cll}")

    # Rotate
    print(f"List before rotate: {cll}")
    cll.rotate(1)
    print(f"List after rotate(1): {cll}")
    cll.rotate(2)
    print(f"List after rotate(2): {cll}")

    # Iteration
    print("Iteration over list:")
    for elem in cll:
        print(f"  {elem}")

    # Clear
    cll.clear()
    print(f"List after clear: {cll}")
    print(f"Is empty: {cll.is_empty()}")

    # Error handling
    try:
        cll.remove_first()
    except RuntimeError as e:
        print(f"Expected error removing from empty list: {e}")

    try:
        cll.remove_at(0)
    except IndexError as e:
        print(f"Expected error with invalid index: {e}")

    print("CircularLinkedList tests completed successfully!\n")


# Run tests when file is executed directly
if __name__ == "__main__":
    test_circular_linked_list()

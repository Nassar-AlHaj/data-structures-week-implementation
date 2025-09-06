class Node:
    def __init__(self, data, prev=None, nxt=None):
        self.data = data
        self.prev = prev
        self.next = nxt

    def __str__(self):
        return str(self.data)


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

    def add(self, elem):
        self.add_last(elem)

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

    def contains(self, elem):
        trav = self.head
        while trav:
            if trav.data == elem:
                return True
            trav = trav.next
        return False

    def index_of(self, elem):
        index = 0
        trav = self.head
        while trav:
            if trav.data == elem:
                return index
            trav = trav.next
            index += 1
        return -1

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_first()
        if index == self.size - 1:
            return self.remove_last()
        trav = self.head
        for _ in range(index):
            trav = trav.next
        trav.prev.next = trav.next
        trav.next.prev = trav.prev
        self.size -= 1
        return trav.data

    def reverse(self):
        if self.is_empty() or self.size == 1:
            return
        self.head, self.tail = self.tail, self.head
        trav = self.head
        while trav:
            trav.prev, trav.next = trav.next, trav.prev
            trav = trav.next

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        trav = self.head
        while trav:
            yield trav.data
            trav = trav.next

    def reverse_iter(self):
        trav = self.tail
        while trav:
            yield trav.data
            trav = trav.prev

    def __str__(self):
        vals = []
        trav = self.head
        while trav:
            vals.append(str(trav.data))
            trav = trav.next
        return "[ " + ", ".join(vals) + " ]"


def test_doubly_linked_list():
    print("Testing DoublyLinkedList...")

    dll = DoublyLinkedList()
    print(f"Empty list: {dll}")
    print(f"Is empty: {dll.is_empty()}")
    print(f"Size: {len(dll)}")

    dll.add_first(20)
    dll.add_first(10)
    print(f"After adding 20, 10 at beginning: {dll}")

    dll.add_last(30)
    dll.add_last(40)
    print(f"After adding 30, 40 at end: {dll}")
    print(f"Size: {len(dll)}")

    print(f"First element (peek): {dll.peek_first()}")
    print(f"Last element (peek): {dll.peek_last()}")

    print(f"Contains 30: {dll.contains(30)}")
    print(f"Contains 99: {dll.contains(99)}")
    print(f"Index of 30: {dll.index_of(30)}")
    print(f"Index of 99: {dll.index_of(99)}")

    first = dll.remove_first()
    print(f"Removed first: {first}, List: {dll}")

    last = dll.remove_last()
    print(f"Removed last: {last}, List: {dll}")

    dll.add(50)
    dll.add(60)
    print(f"After adding 50, 60: {dll}")

    removed = dll.remove_at(1)
    print(f"Removed element at index 1: {removed}, List: {dll}")

    dll.add_first(5)
    dll.add_last(70)
    print(f"Final list: {dll}")

    print("Forward iteration:")
    for elem in dll:
        print(f"  {elem}")

    print("Backward iteration:")
    for elem in dll.reverse_iter():
        print(f"  {elem}")

    print(f"List before reverse: {dll}")
    dll.reverse()
    print(f"List after reverse: {dll}")

    dll.clear()
    print(f"List after clear: {dll}")
    print(f"Is empty: {dll.is_empty()}")

    try:
        dll.remove_first()
    except RuntimeError as e:
        print(f"Expected error removing from empty list: {e}")

    try:
        dll.remove_at(0)
    except IndexError as e:
        print(f"Expected error with invalid index: {e}")

    dll.add_first(100)
    print(f"Single element list: {dll}")
    dll.reverse()
    print(f"Reverse single element: {dll}")
    removed = dll.remove_last()
    print(f"Removed from single element list: {removed}")
    print(f"List after removal: {dll}")

    print("DoublyLinkedList tests completed successfully!\n")


if __name__ == "__main__":
    test_doubly_linked_list()

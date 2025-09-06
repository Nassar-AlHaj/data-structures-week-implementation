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

    def __len__(self):
        return self.size

    def __str__(self):
        vals = []
        trav = self.head
        while trav:
            vals.append(str(trav.data))
            trav = trav.next
        return "[ " + ", ".join(vals) + " ]"


def test_singly_linked_list():
    print("Testing SinglyLinkedList...")

    ll = SinglyLinkedList()
    print(f"Empty list: {ll}")
    print(f"Is empty: {ll.is_empty()}")
    print(f"Size: {len(ll)}")

    ll.add(10)
    ll.add(20)
    ll.add(30)
    print(f"After adding 10,20,30: {ll}")

    ll.add_first(5)
    print(f"After adding 5 at beginning: {ll}")

    print(f"First element: {ll.peek_first()}")
    print(f"Last element: {ll.peek_last()}")

    print(f"Index of 20: {ll.index_of(20)}")
    print(f"Contains 30: {ll.contains(30)}")
    print(f"Contains 99: {ll.contains(99)}")

    first = ll.remove_first()
    print(f"Removed first: {first}, List: {ll}")

    last = ll.remove_last()
    print(f"Removed last: {last}, List: {ll}")

    removed = ll.remove_at(0)
    print(f"Removed at index 0: {removed}, List: {ll}")

    ll.add(40)
    ll.add(50)
    ll.add(60)
    print(f"After adding 40,50,60: {ll}")

    print("Iterating through list:")
    for elem in ll:
        print(f"  {elem}")

    ll.clear()
    print(f"After clear: {ll}, Is empty: {ll.is_empty()}")

    try:
        ll.peek_first()
    except RuntimeError as e:
        print(f"Expected error: {e}")

    try:
        ll.remove_at(0)
    except IndexError as e:
        print(f"Expected error: {e}")

    ll.add(100)
    print(f"Single element list: {ll}")
    removed = ll.remove_last()
    print(f"Removed last: {removed}, List: {ll}")

    print("SinglyLinkedList tests completed successfully!\n")


if __name__ == "__main__":
    test_singly_linked_list()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def offer(self, elem):
        node = Node(elem)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def enqueue(self, elem):
        self.offer(elem)

    def poll(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return data

    def dequeue(self):
        return self.poll()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def front_element(self):
        return self.peek()

    def rear_element(self):
        return None if self.is_empty() else self.rear.data

    def contains(self, elem):
        trav = self.front
        while trav:
            if trav.data == elem:
                return True
            trav = trav.next
        return False

    def to_list(self):
        result = []
        trav = self.front
        while trav:
            result.append(trav.data)
            trav = trav.next
        return result

    def clear(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        trav = self.front
        while trav:
            yield trav.data
            trav = trav.next

    def __str__(self):
        vals = []
        trav = self.front
        while trav:
            vals.append(str(trav.data))
            trav = trav.next
        return "[ " + ", ".join(vals) + " ]"

    def __bool__(self):
        return not self.is_empty()


def test_linked_list_queue():
    print("Testing LinkedListQueue...")

    queue = LinkedListQueue()
    print(f"Empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Size: {len(queue)}")
    print(f"Boolean value: {bool(queue)}")

    queue.offer(10)
    queue.offer(20)
    queue.offer(30)
    print(f"After offering 10, 20, 30: {queue}")
    print(f"Size: {len(queue)}")

    print(f"Front element (peek): {queue.peek()}")
    print(f"Rear element: {queue.rear_element()}")

    polled = queue.poll()
    print(f"Polled element: {polled}")
    print(f"Queue after poll: {queue}")

    queue.enqueue(40)
    queue.enqueue(50)
    print(f"After enqueuing 40, 50: {queue}")

    dequeued = queue.dequeue()
    print(f"Dequeued element: {dequeued}")
    print(f"Queue after dequeue: {queue}")

    print(f"Contains 30: {queue.contains(30)}")
    print(f"Contains 99: {queue.contains(99)}")

    print(f"Queue as list: {queue.to_list()}")

    print("Iterating through queue:")
    for elem in queue:
        print(f"  {elem}")

    queue.offer(60)
    queue.offer(70)
    print(f"Queue with more elements: {queue}")
    print(f"Front: {queue.front_element()}, Rear: {queue.rear_element()}")

    print("Processing all elements (FIFO order):")
    processed_elements = []
    while not queue.is_empty():
        elem = queue.poll()
        processed_elements.append(elem)
        print(f"  Processed: {elem}, Queue: {queue}, Size: {len(queue)}")
    print(f"Elements processed in order: {processed_elements}")

    print(f"Final empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Boolean value: {bool(queue)}")

    try:
        queue.peek()
    except IndexError as e:
        print(f"Expected error when peeking empty queue: {e}")

    try:
        queue.poll()
    except IndexError as e:
        print(f"Expected error when polling empty queue: {e}")

    queue.offer(100)
    print(f"Single element queue: {queue}")
    print(f"Front: {queue.front_element()}, Rear: {queue.rear_element()}")
    polled = queue.poll()
    print(f"Polled from single element queue: {polled}")
    print(f"Queue after polling single element: {queue}")

    queue.clear()
    print("LinkedListQueue tests completed successfully!\n")


if __name__ == "__main__":
    test_linked_list_queue()

class QueueArray:
    def __init__(self, capacity=10):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def offer(self, elem):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.data[self.rear] = elem
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def poll(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elem = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return elem

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return "[]"
        vals = []
        idx = self.front
        for _ in range(self.size):
            vals.append(str(self.data[idx]))
            idx = (idx + 1) % self.capacity
        return "[ " + ", ".join(vals) + " ]"


def test_queue_array():
    print("Testing QueueArray...")
    
    queue = QueueArray(5)
    print(f"Empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    print(f"Is full: {queue.is_full()}")
    print(f"Size: {len(queue)}")
    
    queue.offer(10)
    queue.offer(20)
    queue.offer(30)
    print(f"After offering 10, 20, 30: {queue}")
    print(f"Size: {len(queue)}")
    
    print(f"Front element (peek): {queue.peek()}")
    print(f"Queue after peek: {queue}")
    
    polled = queue.poll()
    print(f"Polled element: {polled}")
    print(f"Queue after poll: {queue}")
    print(f"Size after poll: {len(queue)}")
    
    queue.offer(40)
    queue.offer(50)
    queue.offer(60)
    print(f"Queue at capacity: {queue}")
    print(f"Is full: {queue.is_full()}")
    
    polled = queue.poll()
    print(f"Polled: {polled}, Queue: {queue}")
    queue.offer(70)
    print(f"After offering 70: {queue}")
    
    try:
        queue.offer(80)
    except OverflowError as e:
        print(f"Expected error when queue is full: {e}")
    
    print("Polling all elements:")
    while not queue.is_empty():
        polled = queue.poll()
        print(f"Polled: {polled}, Queue: {queue}, Size: {len(queue)}")
    
    print(f"Final empty queue: {queue}")
    print(f"Is empty: {queue.is_empty()}")
    
    try:
        queue.peek()
    except IndexError as e:
        print(f"Expected error when peeking empty queue: {e}")
    
    try:
        queue.poll()
    except IndexError as e:
        print(f"Expected error when polling empty queue: {e}")
    
    try:
        invalid_queue = QueueArray(0)
    except ValueError as e:
        print(f"Expected error with zero capacity: {e}")
    
    try:
        invalid_queue = QueueArray(-5)
    except ValueError as e:
        print(f"Expected error with negative capacity: {e}")
    
    print("\nTesting extensive circular buffer operations...")
    test_queue = QueueArray(3)
    
    for cycle in range(3):
        print(f"Cycle {cycle + 1}:")
        for i in range(3):
            test_queue.offer(f"Item{cycle}-{i}")
        print(f"  Filled: {test_queue}")
        
        while not test_queue.is_empty():
            item = test_queue.poll()
            print(f"  Polled: {item}, Queue: {test_queue}")
    
    print("QueueArray tests completed successfully!\n")


if __name__ == "__main__":
    test_queue_array()

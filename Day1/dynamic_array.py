class MyDynamicArray:
    def __init__(self, capacity=16):
        if capacity < 0:
            raise ValueError(f"Illegal Capacity: {capacity}")
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * capacity

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        return self.arr[index]

    def set(self, index, elem):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        self.arr[index] = elem

    def clear(self):
        for i in range(self.length):
            self.arr[i] = None
        self.length = 0

    def add(self, elem):
        if self.length + 1 >= self.capacity:
            self.capacity = 2 * self.capacity if self.capacity > 0 else 1
            new_arr = [None] * self.capacity
            for i in range(self.length):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.length] = elem
        self.length += 1

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        data = self.arr[index]
        new_arr = [None] * (self.length - 1)
        for i in range(self.length):
            if i < index:
                new_arr[i] = self.arr[i]
            elif i > index:
                new_arr[i - 1] = self.arr[i]
        self.arr = new_arr
        self.length -= 1
        self.capacity = self.length
        return data

    def remove(self, obj):
        index = self.index_of(obj)
        if index == -1:
            return False
        self.remove_at(index)
        return True

    def index_of(self, obj):
        for i in range(self.length):
            if self.arr[i] == obj:
                return i
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

    def __iter__(self):
        for i in range(self.length):
            yield self.arr[i]

    def __str__(self):
        if self.length == 0:
            return "[]"
        return "[" + ", ".join(str(self.arr[i]) for i in range(self.length)) + "]"


def test_dynamic_array():
    print("Testing MyDynamicArray...")
    
    arr = MyDynamicArray(2)
    print(f"Empty array: {arr}")
    print(f"Is empty: {arr.is_empty()}")
    print(f"Size: {arr.size()}")
    
    arr.add(1)
    arr.add(2)
    arr.add(3)
    arr.add(4)
    print(f"After adding 1,2,3,4: {arr}")
    print(f"Size: {arr.size()}, Capacity: {arr.capacity}")
    
    print(f"Element at index 0: {arr.get(0)}")
    print(f"Element at index 2: {arr.get(2)}")
    
    arr.set(1, 10)
    print(f"After setting index 1 to 10: {arr}")
    
    print(f"Index of 10: {arr.index_of(10)}")
    print(f"Contains 3: {arr.contains(3)}")
    print(f"Contains 99: {arr.contains(99)}")
    
    removed = arr.remove_at(1)
    print(f"Removed element at index 1: {removed}")
    print(f"Array after removal: {arr}")
    
    success = arr.remove(3)
    print(f"Removed element 3: {success}")
    print(f"Array after removing 3: {arr}")
    
    print("Iterating through array:")
    for elem in arr:
        print(f"  {elem}")
    
    arr.clear()
    print(f"Array after clear: {arr}")
    print(f"Is empty: {arr.is_empty()}")
    
    try:
        arr.get(0)
    except IndexError as e:
        print(f"Expected error accessing empty array: {e}")
    
    try:
        MyDynamicArray(-1)
    except ValueError as e:
        print(f"Expected error with negative capacity: {e}")
    
    print("MyDynamicArray tests completed successfully!\n")


if __name__ == "__main__":
    test_dynamic_array()

import unittest
from typing import Any, Optional, List


class MinHeap:
    def __init__(self):
        self.heap: List[Any] = []

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def get_min(self) -> Optional[Any]:
        return None if self.is_empty() else self.heap[0]

    def insert(self, value: Any) -> None:
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self) -> Optional[Any]:
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return root

    def _bubble_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _bubble_down(self, index: int) -> None:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._bubble_down(smallest)

    def build_heap(self, arr: List[Any]) -> None:
        self.heap = arr.copy()
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._bubble_down(i)

    def heap_sort(self) -> List[Any]:
        sorted_arr = []
        while not self.is_empty():
            sorted_arr.append(self.extract_min())
        return sorted_arr

    def __str__(self) -> str:
        return f"MinHeap: {self.heap}"


# ==================== UNIT TESTS ====================

class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MinHeap()

    def test_empty_heap(self):
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertIsNone(self.heap.get_min())
        self.assertIsNone(self.heap.extract_min())

    def test_single_element(self):
        self.heap.insert(5)
        self.assertEqual(self.heap.get_min(), 5)
        self.assertEqual(self.heap.extract_min(), 5)
        self.assertTrue(self.heap.is_empty())

    def test_multiple_insertions(self):
        values = [10, 5, 15, 2, 8, 12, 20]
        for value in values:
            self.heap.insert(value)
        self.assertEqual(self.heap.get_min(), 2)

    def test_extract_min_order(self):
        values = [10, 5, 15, 2, 8, 12, 20, 1, 25]
        for value in values:
            self.heap.insert(value)
        extracted = [self.heap.extract_min() for _ in range(len(values))]
        self.assertEqual(extracted, sorted(values))

    def test_build_heap_from_array(self):
        arr = [10, 5, 15, 2, 8, 12, 20]
        self.heap.build_heap(arr)
        self.assertEqual(self.heap.get_min(), min(arr))
        extracted = [self.heap.extract_min() for _ in range(len(arr))]
        self.assertEqual(extracted, sorted(arr))

    def test_heap_sort(self):
        values = [64, 34, 25, 12, 22, 11, 90]
        for value in values:
            self.heap.insert(value)
        sorted_result = self.heap.heap_sort()
        self.assertEqual(sorted_result, sorted(values))
        self.assertTrue(self.heap.is_empty())

    def test_duplicate_values(self):
        values = [5, 3, 5, 1, 3, 1, 5]
        for value in values:
            self.heap.insert(value)
        extracted = [self.heap.extract_min() for _ in range(len(values))]
        self.assertEqual(extracted, sorted(values))

    def test_mixed_data_types(self):
        string_heap = MinHeap()
        strings = ["zebra", "apple", "banana", "cherry"]
        for s in strings:
            string_heap.insert(s)
        self.assertEqual(string_heap.get_min(), "apple")
        extracted = [string_heap.extract_min() for _ in range(len(strings))]
        self.assertEqual(extracted, sorted(strings))

    def test_large_heap(self):
        import random
        values = [random.randint(1, 1000) for _ in range(100)]
        for value in values:
            self.heap.insert(value)
        self.assertEqual(self.heap.get_min(), min(values))
        extracted = [self.heap.extract_min() for _ in range(10)]
        self.assertEqual(extracted, sorted(extracted))


if __name__ == '__main__':
    print("Running Min Heap Tests...")
    print("=" * 25)
    unittest.main(verbosity=2)

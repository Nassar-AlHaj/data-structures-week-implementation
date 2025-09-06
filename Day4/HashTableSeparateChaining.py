import unittest
from typing import Any, List, Optional, Iterator


class HashTableSeparateChaining:
    def __init__(self, capacity: int = 3, load_factor: float = 0.75):
        if capacity <= 0 or load_factor <= 0 or load_factor == float("inf"):
            raise ValueError("Illegal capacity or load factor")
        self.capacity = capacity
        self.load_factor = load_factor
        self.size_ = 0
        self.buckets = [[] for _ in range(capacity)]
        self.mod_count = 0

    def clear(self) -> None:
        self.size_ = 0
        self.buckets = [[] for _ in range(self.capacity)]
        self.mod_count += 1

    def size(self) -> int:
        return self.size_

    def is_empty(self) -> bool:
        return self.size_ == 0

    def hash(self, key: Any) -> int:
        return (hash(key) & 0x7FFFFFFF) % self.capacity

    def put(self, key: Any, value: Any) -> Optional[Any]:
        if key is None:
            raise ValueError("Null key")
        if self.size_ >= self.capacity * self.load_factor:
            self.resize()
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                old_val = v
                bucket[i] = (key, value)
                return old_val
        bucket.append((key, value))
        self.size_ += 1
        self.mod_count += 1
        return None

    def add(self, key: Any, value: Any) -> Optional[Any]:
        return self.put(key, value)

    def get(self, key: Any) -> Optional[Any]:
        if key is None:
            return None
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for (k, v) in bucket:
            if k == key:
                return v
        return None

    def has_key(self, key: Any) -> bool:
        return self.contains_key(key)

    def contains_key(self, key: Any) -> bool:
        if key is None:
            return False
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for (k, _) in bucket:
            if k == key:
                return True
        return False

    def remove(self, key: Any) -> Optional[Any]:
        if key is None:
            return None
        bucket_index = self.hash(key)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size_ -= 1
                self.mod_count += 1
                return v
        return None

    def keys(self) -> List[Any]:
        ks = []
        for bucket in self.buckets:
            for (k, _) in bucket:
                ks.append(k)
        return ks

    def values(self) -> List[Any]:
        vals = []
        for bucket in self.buckets:
            for (_, v) in bucket:
                vals.append(v)
        return vals

    def resize(self) -> None:
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size_ = 0
        for bucket in old_buckets:
            for (k, v) in bucket:
                self.put(k, v)

    def __iter__(self) -> Iterator[Any]:
        expected_mod_count = self.mod_count
        for bucket in self.buckets:
            for (k, _) in bucket:
                if expected_mod_count != self.mod_count:
                    raise RuntimeError("Concurrent modification")
                yield k

    def __str__(self) -> str:
        items = []
        for bucket in self.buckets:
            for (k, v) in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"


# ==================== UNIT TESTS ====================

class TestHashTableSeparateChaining(unittest.TestCase):
    def setUp(self):
        self.ht = HashTableSeparateChaining()

    def test_empty_hash_table(self):
        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)
        self.assertIsNone(self.ht.get("key"))
        self.assertFalse(self.ht.contains_key("key"))
        self.assertEqual(self.ht.keys(), [])
        self.assertEqual(self.ht.values(), [])

    def test_basic_operations(self):
        self.assertIsNone(self.ht.put("key1", "value1"))
        self.assertIsNone(self.ht.put("key2", "value2"))
        self.assertEqual(self.ht.size(), 2)
        self.assertFalse(self.ht.is_empty())
        self.assertEqual(self.ht.get("key1"), "value1")
        self.assertEqual(self.ht.get("key2"), "value2")
        self.assertIsNone(self.ht.get("nonexistent"))
        self.assertTrue(self.ht.contains_key("key1"))
        self.assertTrue(self.ht.contains_key("key2"))
        self.assertFalse(self.ht.contains_key("nonexistent"))

    def test_update_existing_key(self):
        self.ht.put("key", "value1")
        old_value = self.ht.put("key", "value2")
        self.assertEqual(old_value, "value1")
        self.assertEqual(self.ht.get("key"), "value2")
        self.assertEqual(self.ht.size(), 1)

    def test_remove_operations(self):
        self.ht.put("key1", "value1")
        self.ht.put("key2", "value2")
        self.ht.put("key3", "value3")
        removed_value = self.ht.remove("key2")
        self.assertEqual(removed_value, "value2")
        self.assertEqual(self.ht.size(), 2)
        self.assertFalse(self.ht.contains_key("key2"))
        self.assertIsNone(self.ht.remove("nonexistent"))
        self.assertEqual(self.ht.size(), 2)

    def test_keys_and_values(self):
        data = {"a": 1, "b": 2, "c": 3}
        for k, v in data.items():
            self.ht.put(k, v)
        keys = self.ht.keys()
        values = self.ht.values()
        self.assertEqual(len(keys), 3)
        self.assertEqual(len(values), 3)
        self.assertEqual(set(keys), set(data.keys()))
        self.assertEqual(set(values), set(data.values()))

    def test_collision_handling(self):
        small_ht = HashTableSeparateChaining(capacity=2)
        items = [("key1", "val1"), ("key2", "val2"), ("key3", "val3"), ("key4", "val4")]
        for k, v in items:
            small_ht.put(k, v)
        for k, v in items:
            self.assertEqual(small_ht.get(k), v)
        self.assertEqual(small_ht.size(), 4)

    def test_resize_functionality(self):
        initial_capacity = self.ht.capacity
        for i in range(10):
            self.ht.put(f"key{i}", f"value{i}")
        self.assertGreater(self.ht.capacity, initial_capacity)
        for i in range(10):
            self.assertEqual(self.ht.get(f"key{i}"), f"value{i}")

    def test_clear_operation(self):
        for i in range(5):
            self.ht.put(f"key{i}", f"value{i}")
        self.ht.clear()
        self.assertTrue(self.ht.is_empty())
        self.assertEqual(self.ht.size(), 0)
        self.assertEqual(self.ht.keys(), [])

    def test_null_key_handling(self):
        with self.assertRaises(ValueError):
            self.ht.put(None, "value")
        self.assertIsNone(self.ht.get(None))
        self.assertFalse(self.ht.contains_key(None))
        self.assertIsNone(self.ht.remove(None))

    def test_iterator(self):
        data = {"a": 1, "b": 2, "c": 3}
        for k, v in data.items():
            self.ht.put(k, v)
        iterated_keys = list(self.ht)
        self.assertEqual(len(iterated_keys), 3)
        self.assertEqual(set(iterated_keys), set(data.keys()))


if __name__ == '__main__':
    print("Running Hash Table Tests...")
    print("=" * 30)
    unittest.main(verbosity=2)

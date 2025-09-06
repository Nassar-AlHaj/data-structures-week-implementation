import unittest
from typing import Optional

class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.count = 0
        self.is_word_ending = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('\0')

    def insert(self, key: str, num_inserts: int = 1) -> bool:
        if key is None:
            raise ValueError("Null key not permitted")
        if num_inserts <= 0:
            raise ValueError("Number of inserts must be positive")
        node = self.root
        created_new_node = False
        is_prefix = False
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
                created_new_node = True
            else:
                if node.children[ch].is_word_ending:
                    is_prefix = True
            node = node.children[ch]
            node.count += num_inserts
        if node != self.root:
            node.is_word_ending = True
        return is_prefix or not created_new_node

    def delete(self, key: str, num_deletions: int = 1) -> bool:
        if not self.contains(key):
            return False
        if num_deletions <= 0:
            raise ValueError("Number of deletions must be positive")
        node = self.root
        for ch in key:
            current = node.children[ch]
            current.count -= num_deletions
            if current.count <= 0:
                del node.children[ch]
                return True
            node = current
        return True

    def contains(self, key: str) -> bool:
        return self.count(key) > 0

    def count(self, key: str) -> int:
        if key is None:
            raise ValueError("Null key not permitted")
        node = self.root
        for ch in key:
            if node is None or ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count if node and node.is_word_ending else 0

    def starts_with(self, prefix: str) -> bool:
        if prefix is None:
            raise ValueError("Null prefix not permitted")
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def clear(self):
        self.root.children = {}

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_basic_operations(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.contains("hello"))
        self.assertEqual(self.trie.count("hello"), 1)
        self.assertFalse(self.trie.contains("world"))
        self.assertEqual(self.trie.count("world"), 0)

    def test_multiple_insertions(self):
        words = ["hello", "help", "world", "word"]
        for word in words:
            self.trie.insert(word)
        for word in words:
            self.assertTrue(self.trie.contains(word))

    def test_counting(self):
        self.trie.insert("test", 3)
        self.assertEqual(self.trie.count("test"), 3)
        self.trie.insert("test", 2)
        self.assertEqual(self.trie.count("test"), 5)

    def test_deletion(self):
        self.trie.insert("test", 3)
        self.assertTrue(self.trie.delete("test", 1))
        self.assertEqual(self.trie.count("test"), 2)
        self.assertTrue(self.trie.delete("test", 2))
        self.assertFalse(self.trie.contains("test"))
        self.assertFalse(self.trie.delete("nonexistent"))

    def test_prefix_operations(self):
        words = ["car", "card", "care", "cat"]
        for word in words:
            self.trie.insert(word)
        self.assertTrue(self.trie.starts_with("car"))
        self.assertTrue(self.trie.starts_with("ca"))
        self.assertFalse(self.trie.starts_with("dog"))

    def test_overlapping_words(self):
        self.trie.insert("test")
        self.trie.insert("testing")
        self.assertTrue(self.trie.contains("test"))
        self.assertTrue(self.trie.contains("testing"))
        self.assertFalse(self.trie.contains("tes"))

    def test_clear(self):
        self.trie.insert("hello")
        self.trie.insert("world")
        self.trie.clear()
        self.assertFalse(self.trie.contains("hello"))
        self.assertFalse(self.trie.contains("world"))

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            self.trie.insert(None)
        with self.assertRaises(ValueError):
            self.trie.count(None)
        with self.assertRaises(ValueError):
            self.trie.insert("test", 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

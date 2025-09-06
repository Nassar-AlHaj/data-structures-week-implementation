import unittest

class UnionFind:
    """
    Union-Find (Disjoint Set Union) with path compression and union by size
    """
    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Size must be positive")
        self.size = self.num_components = size
        self.sz = [1] * size
        self.id = list(range(size))

    def find(self, p: int) -> int:
        if not (0 <= p < self.size):
            raise ValueError(f"Element {p} out of bounds")
        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:
            next_p = self.id[p]
            self.id[p] = root
            p = next_p
        return root

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def component_size(self, p: int) -> int:
        return self.sz[self.find(p)]

    def components(self) -> int:
        return self.num_components

    def unify(self, p: int, q: int) -> bool:
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2:
            return False
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
        self.num_components -= 1
        return True


class TestUnionFind(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFind(10)

    def test_initialization(self):
        self.assertEqual(self.uf.components(), 10)
        self.assertEqual(self.uf.component_size(0), 1)
        for i in range(10):
            for j in range(i + 1, 10):
                self.assertFalse(self.uf.connected(i, j))

    def test_basic_union(self):
        self.assertTrue(self.uf.unify(0, 1))
        self.assertTrue(self.uf.connected(0, 1))
        self.assertEqual(self.uf.components(), 9)
        self.assertEqual(self.uf.component_size(0), 2)
        self.assertEqual(self.uf.component_size(1), 2)

    def test_redundant_union(self):
        self.uf.unify(0, 1)
        self.assertFalse(self.uf.unify(0, 1))
        self.assertEqual(self.uf.components(), 9)

    def test_chain_unions(self):
        for i in range(4):
            self.uf.unify(i, i + 1)
        for i in range(5):
            for j in range(i + 1, 5):
                self.assertTrue(self.uf.connected(i, j))
        self.assertEqual(self.uf.components(), 6)
        self.assertEqual(self.uf.component_size(0), 5)

    def test_multiple_components(self):
        self.uf.unify(0, 1)
        self.uf.unify(1, 2)
        self.uf.unify(3, 4)
        self.uf.unify(4, 5)
        self.assertTrue(self.uf.connected(0, 2))
        self.assertTrue(self.uf.connected(3, 5))
        self.assertFalse(self.uf.connected(0, 3))
        self.assertFalse(self.uf.connected(2, 4))
        self.assertEqual(self.uf.components(), 6)

    def test_path_compression(self):
        for i in range(9):
            self.uf.unify(i, i + 1)
        root = self.uf.find(0)
        for i in range(10):
            self.assertEqual(self.uf.find(i), root)

    def test_union_by_size(self):
        self.uf.unify(0, 1)
        self.uf.unify(2, 3)
        self.uf.unify(3, 4)
        components_before = self.uf.components()
        self.uf.unify(0, 2)
        self.assertEqual(self.uf.components(), components_before - 1)
        self.assertEqual(self.uf.component_size(0), 5)

    def test_large_dataset(self):
        large_uf = UnionFind(1000)
        for i in range(10):
            for j in range(1, 100):
                large_uf.unify(i * 100, i * 100 + j)
        self.assertEqual(large_uf.components(), 10)
        for i in range(10):
            self.assertEqual(large_uf.component_size(i * 100), 100)

    def test_error_handling(self):
        with self.assertRaises(ValueError):
            UnionFind(0)
        with self.assertRaises(ValueError):
            UnionFind(-1)
        with self.assertRaises(ValueError):
            self.uf.find(-1)
        with self.assertRaises(ValueError):
            self.uf.find(10)

    def test_single_element(self):
        single_uf = UnionFind(1)
        self.assertEqual(single_uf.components(), 1)
        self.assertEqual(single_uf.component_size(0), 1)
        self.assertEqual(single_uf.find(0), 0)
        self.assertFalse(single_uf.unify(0, 0))


if __name__ == '__main__':
    unittest.main(verbosity=2)

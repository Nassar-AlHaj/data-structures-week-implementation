import unittest
from collections import deque
from typing import List


class Graph:
    """
    Undirected graph with BFS and DFS using adjacency list
    """
    def __init__(self, vertices: int):
        if vertices <= 0:
            raise ValueError("Number of vertices must be positive")
        self.v = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int) -> None:
        if not (0 <= u < self.v and 0 <= v < self.v):
            raise ValueError(f"Vertices must be in range [0, {self.v-1}]")
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def bfs(self, start: int) -> List[int]:
        if not (0 <= start < self.v):
            raise ValueError(f"Start vertex must be in range [0, {self.v-1}]")
        visited = [False] * self.v
        order = []
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in sorted(self.adj[node]):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return order

    def dfs(self, start: int) -> List[int]:
        if not (0 <= start < self.v):
            raise ValueError(f"Start vertex must be in range [0, {self.v-1}]")
        visited = [False] * self.v
        order = []
        self._dfs_util(start, visited, order)
        return order

    def _dfs_util(self, node: int, visited: List[bool], order: List[int]) -> None:
        visited[node] = True
        order.append(node)
        for neighbor in sorted(self.adj[node]):
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited, order)

    def is_connected(self) -> bool:
        if self.v == 0:
            return True
        return len(self.bfs(0)) == self.v

    def __str__(self) -> str:
        return "\n".join(f"{i}: {self.adj[i]}" for i in range(self.v))


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(5)

    def test_graph_initialization(self):
        self.assertEqual(self.graph.v, 5)
        self.assertEqual(len(self.graph.adj), 5)
        for adj_list in self.graph.adj:
            self.assertEqual(len(adj_list), 0)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Graph(0)
        with self.assertRaises(ValueError):
            Graph(-1)

    def test_add_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.assertIn(1, self.graph.adj[0])
        self.assertIn(0, self.graph.adj[1])
        self.assertIn(2, self.graph.adj[1])
        self.assertIn(1, self.graph.adj[2])

    def test_add_duplicate_edge(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 1)
        self.assertEqual(self.graph.adj[0].count(1), 1)
        self.assertEqual(self.graph.adj[1].count(0), 1)

    def test_add_invalid_edge(self):
        with self.assertRaises(ValueError):
            self.graph.add_edge(-1, 0)
        with self.assertRaises(ValueError):
            self.graph.add_edge(0, 5)

    def test_bfs_simple_path(self):
        for i in range(4):
            self.graph.add_edge(i, i + 1)
        self.assertEqual(self.graph.bfs(0), [0, 1, 2, 3, 4])

    def test_bfs_star_graph(self):
        for i in range(1, 5):
            self.graph.add_edge(0, i)
        self.assertEqual(self.graph.bfs(0), [0, 1, 2, 3, 4])

    def test_dfs_simple_path(self):
        for i in range(4):
            self.graph.add_edge(i, i + 1)
        self.assertEqual(self.graph.dfs(0), [0, 1, 2, 3, 4])

    def test_bfs_disconnected_component(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 4)
        self.assertEqual(set(self.graph.bfs(0)), {0, 1})
        self.assertEqual(set(self.graph.bfs(2)), {2, 3, 4})

    def test_dfs_disconnected_component(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 4)
        self.assertEqual(set(self.graph.dfs(0)), {0, 1})
        self.assertEqual(set(self.graph.dfs(2)), {2, 3, 4})

    def test_single_vertex_traversal(self):
        single_graph = Graph(1)
        self.assertEqual(single_graph.bfs(0), [0])
        self.assertEqual(single_graph.dfs(0), [0])

    def test_invalid_start_vertex(self):
        with self.assertRaises(ValueError):
            self.graph.bfs(-1)
        with self.assertRaises(ValueError):
            self.graph.bfs(5)
        with self.assertRaises(ValueError):
            self.graph.dfs(-1)
        with self.assertRaises(ValueError):
            self.graph.dfs(5)

    def test_is_connected(self):
        single_graph = Graph(1)
        self.assertTrue(single_graph.is_connected())
        self.graph.add_edge(0, 1)
        self.graph.add_edge(2, 3)
        self.assertFalse(self.graph.is_connected())
        self.graph.add_edge(1, 2)
        self.graph.add_edge(3, 4)
        self.assertTrue(self.graph.is_connected())

    def test_complex_graph_traversal(self):
        edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
        for u, v in edges:
            self.graph.add_edge(u, v)
        bfs_result = self.graph.bfs(0)
        dfs_result = self.graph.dfs(0)
        self.assertEqual(bfs_result[0], 0)
        self.assertEqual(dfs_result[0], 0)
        self.assertEqual(set(bfs_result), set(range(5)))
        self.assertEqual(set(dfs_result), set(range(5)))


if __name__ == '__main__':
    unittest.main(verbosity=2)

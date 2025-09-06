import unittest
from collections import defaultdict, deque
from typing import List, Any, Set


class Graph:
    def __init__(self, directed: bool = False):
        self.adj_list = defaultdict(list)
        self.directed = directed

    def add_vertex(self, v: Any) -> None:
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u: Any, v: Any) -> None:
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def get_vertices(self) -> List[Any]:
        return list(self.adj_list.keys())

    def get_neighbors(self, v: Any) -> List[Any]:
        return self.adj_list[v]

    def has_vertex(self, v: Any) -> bool:
        return v in self.adj_list

    def has_edge(self, u: Any, v: Any) -> bool:
        return v in self.adj_list[u]

    def bfs(self, start: Any) -> List[Any]:
        if start not in self.adj_list:
            return []
        visited: Set[Any] = set([start])
        order: List[Any] = []
        q = deque([start])
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return order

    def dfs(self, start: Any) -> List[Any]:
        if start not in self.adj_list:
            return []
        visited: Set[Any] = set()
        order: List[Any] = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, node: Any, visited: Set[Any], order: List[Any]) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, order)

    def __str__(self) -> str:
        return "\n".join([f"{v}: {neighbors}" for v, neighbors in self.adj_list.items()])


# ==================== UNIT TESTS ====================

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.undirected_graph = Graph(directed=False)
        self.directed_graph = Graph(directed=True)

    def test_empty_graph(self):
        self.assertEqual(self.undirected_graph.get_vertices(), [])
        self.assertFalse(self.undirected_graph.has_vertex('A'))
        self.assertEqual(self.undirected_graph.bfs('A'), [])
        self.assertEqual(self.undirected_graph.dfs('A'), [])

    def test_add_vertex(self):
        self.undirected_graph.add_vertex('A')
        self.undirected_graph.add_vertex('B')
        self.assertTrue(self.undirected_graph.has_vertex('A'))
        self.assertTrue(self.undirected_graph.has_vertex('B'))
        self.assertEqual(len(self.undirected_graph.get_vertices()), 2)

    def test_undirected_graph_edges(self):
        self.undirected_graph.add_vertex('A')
        self.undirected_graph.add_vertex('B')
        self.undirected_graph.add_vertex('C')
        self.undirected_graph.add_edge('A', 'B')
        self.undirected_graph.add_edge('B', 'C')
        self.assertTrue(self.undirected_graph.has_edge('A', 'B'))
        self.assertTrue(self.undirected_graph.has_edge('B', 'A'))
        self.assertTrue(self.undirected_graph.has_edge('B', 'C'))
        self.assertTrue(self.undirected_graph.has_edge('C', 'B'))
        self.assertFalse(self.undirected_graph.has_edge('A', 'C'))
        self.assertEqual(set(self.undirected_graph.get_neighbors('B')), {'A', 'C'})

    def test_directed_graph_edges(self):
        self.directed_graph.add_vertex('A')
        self.directed_graph.add_vertex('B')
        self.directed_graph.add_vertex('C')
        self.directed_graph.add_edge('A', 'B')
        self.directed_graph.add_edge('B', 'C')
        self.assertTrue(self.directed_graph.has_edge('A', 'B'))
        self.assertFalse(self.directed_graph.has_edge('B', 'A'))
        self.assertTrue(self.directed_graph.has_edge('B', 'C'))
        self.assertFalse(self.directed_graph.has_edge('C', 'B'))
        self.assertEqual(self.directed_graph.get_neighbors('A'), ['B'])
        self.assertEqual(self.directed_graph.get_neighbors('C'), [])

    def test_bfs_traversal(self):
        graph = Graph(directed=False)
        edges = [('A', 'B'), ('B', 'C'), ('A', 'D'), ('D', 'E'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
        for u, v in edges:
            graph.add_edge(u, v)
        bfs_result = graph.bfs('A')
        self.assertEqual(bfs_result[0], 'A')
        self.assertIn('B', bfs_result[:3])
        self.assertIn('D', bfs_result[:3])

    def test_dfs_traversal(self):
        graph = Graph(directed=False)
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        dfs_result = graph.dfs('A')
        self.assertEqual(dfs_result[0], 'A')
        self.assertEqual(len(dfs_result), 3)
        self.assertIn('B', dfs_result)
        self.assertIn('C', dfs_result)

    def test_traversal_with_cycles(self):
        graph = Graph(directed=False)
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')
        bfs_result = graph.bfs('A')
        dfs_result = graph.dfs('A')
        self.assertEqual(len(bfs_result), 3)
        self.assertEqual(len(dfs_result), 3)
        self.assertEqual(set(bfs_result), {'A', 'B', 'C'})
        self.assertEqual(set(dfs_result), {'A', 'B', 'C'})


if __name__ == '__main__':
    print("Running Graph Tests...")
    print("=" * 25)
    unittest.main(verbosity=2)

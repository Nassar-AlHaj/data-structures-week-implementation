import unittest
from typing import Optional, List, Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None


class BinaryTree:
    def __init__(self, root_value: Optional[Any] = None):
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def height(self, node: Optional[Node] = None) -> int:

         if node is None:
          node = self.root
          if node is None:  # empty tree
            return -1
         if node.left is None and node.right is None:
          return 0
         return 1 + max(
           self.height(node.left) if node.left else -1,
           self.height(node.right) if node.right else -1
    )

    def size(self, node: Optional[Node] = None) -> int:
     if node is None:
        node = self.root
        if node is None:  # empty tree
            return 0
     return 1 + (self.size(node.left) if node.left else 0) + (self.size(node.right) if node.right else 0)


    def preorder_traversal(self, node: Optional[Node] = None) -> List[Any]:
        result = []
        if node is None:
            node = self.root
        self._preorder(node, result)
        return result

    def _preorder(self, node: Optional[Node], result: List[Any]) -> None:
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def inorder_traversal(self, node: Optional[Node] = None) -> List[Any]:
        result = []
        if node is None:
            node = self.root
        self._inorder(node, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[Any]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def postorder_traversal(self, node: Optional[Node] = None) -> List[Any]:
        result = []
        if node is None:
            node = self.root
        self._postorder(node, result)
        return result

    def _postorder(self, node: Optional[Node], result: List[Any]) -> None:
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def level_order_traversal(self) -> List[Any]:
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()

    def test_empty_tree(self):
        self.assertTrue(self.bt.is_empty())
        self.assertEqual(self.bt.height(), -1)
        self.assertEqual(self.bt.size(), 0)
        self.assertEqual(self.bt.preorder_traversal(), [])
        self.assertEqual(self.bt.inorder_traversal(), [])
        self.assertEqual(self.bt.postorder_traversal(), [])
        self.assertEqual(self.bt.level_order_traversal(), [])

    def test_single_node_tree(self):
        bt = BinaryTree(1)
        self.assertFalse(bt.is_empty())
        self.assertEqual(bt.height(), 0)
        self.assertEqual(bt.size(), 1)
        self.assertEqual(bt.preorder_traversal(), [1])
        self.assertEqual(bt.inorder_traversal(), [1])
        self.assertEqual(bt.postorder_traversal(), [1])
        self.assertEqual(bt.level_order_traversal(), [1])

    def test_manual_tree_construction(self):
        bt = BinaryTree(1)
        bt.root.left = Node(2)
        bt.root.right = Node(3)
        bt.root.left.left = Node(4)
        bt.root.left.right = Node(5)

        self.assertEqual(bt.height(), 2)
        self.assertEqual(bt.size(), 5)
        self.assertEqual(bt.preorder_traversal(), [1, 2, 4, 5, 3])
        self.assertEqual(bt.inorder_traversal(), [4, 2, 5, 1, 3])
        self.assertEqual(bt.postorder_traversal(), [4, 5, 2, 3, 1])
        self.assertEqual(bt.level_order_traversal(), [1, 2, 3, 4, 5])

    def test_traversal_with_specific_node(self):
        bt = BinaryTree(1)
        bt.root.left = Node(2)
        bt.root.right = Node(3)
        bt.root.left.left = Node(4)
        bt.root.left.right = Node(5)
        bt.root.right.left = Node(6)
        bt.root.right.right = Node(7)

        left_subtree = bt.root.left
        self.assertEqual(bt.preorder_traversal(left_subtree), [2, 4, 5])
        self.assertEqual(bt.inorder_traversal(left_subtree), [4, 2, 5])
        self.assertEqual(bt.postorder_traversal(left_subtree), [4, 5, 2])

    def test_height_and_size_calculations(self):
        bt = BinaryTree()
        self.assertEqual(bt.height(), -1)
        self.assertEqual(bt.size(), 0)

        bt.root = Node(1)
        self.assertEqual(bt.height(), 0)
        self.assertEqual(bt.size(), 1)

        bt.root.left = Node(2)
        self.assertEqual(bt.height(), 1)
        self.assertEqual(bt.size(), 2)

        bt.root.right = Node(3)
        self.assertEqual(bt.height(), 1)
        self.assertEqual(bt.size(), 3)

        bt.root.left.left = Node(4)
        bt.root.left.right = Node(5)
        self.assertEqual(bt.height(), 2)
        self.assertEqual(bt.size(), 5)


def run_tests():
    print("Running Binary Tree Tests...")
    print("=" * 40)
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_tests()

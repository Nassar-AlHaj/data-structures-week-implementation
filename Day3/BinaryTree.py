import unittest
from typing import Optional, List, Any


class Node:
    """Node class for Binary Tree"""
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None


class BinaryTree:
    """
    Binary Tree implementation with traversal algorithms
    
    Time Complexities:
    - Traversal: O(n)
    - Height: O(n)
    - Size: O(n)
    
    Space Complexity: O(n) for storage, O(h) for recursion stack
    """
    
    def __init__(self, root_value: Optional[Any] = None):
        """Initialize binary tree with optional root value"""
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None
    
    def is_empty(self) -> bool:
        """Check if tree is empty"""
        return self.root is None
    
    def height(self) -> int:
        """Calculate height of tree (-1 for empty tree)"""
        return self._height_helper(self.root)
    
    def _height_helper(self, node: Optional[Node]) -> int:
        """Helper method to calculate height recursively"""
        if node is None:
            return -1
        
        return 1 + max(self._height_helper(node.left), self._height_helper(node.right))
    
    def size(self) -> int:
        """Count total number of nodes in tree"""
        return self._size_helper(self.root)
    
    def _size_helper(self, node: Optional[Node]) -> int:
        """Helper method to count nodes recursively"""
        if node is None:
            return 0
        
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)
    
    def preorder_traversal(self) -> List[Any]:
        """Preorder traversal: Root -> Left -> Right"""
        result = []
        self.preorder(self.root, result)
        return result
    
    def preorder(self, node: Optional[Node], result: List[Any]) -> None:
        """Helper method for preorder traversal"""
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
    
    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal: Left -> Root -> Right"""
        result = []
        self.inorder(self.root, result)
        return result
    
    def inorder(self, node: Optional[Node], result: List[Any]) -> None:
        """Helper method for inorder traversal"""
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
    
    def postorder_traversal(self) -> List[Any]:
        """Postorder traversal: Left -> Right -> Root"""
        result = []
        self.postorder(self.root, result)
        return result
    
    def postorder(self, node: Optional[Node], result: List[Any]) -> None:
        """Helper method for postorder traversal"""
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)


# ==================== UNIT TESTS ====================

class TestBinaryTree(unittest.TestCase):
    """Test cases for Binary Tree"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.bt = BinaryTree()
    
    def test_empty_tree(self):
        """Test operations on empty tree"""
        self.assertTrue(self.bt.is_empty())
        self.assertEqual(self.bt.height(), -1)
        self.assertEqual(self.bt.size(), 0)
        self.assertEqual(self.bt.preorder_traversal(), [])
        self.assertEqual(self.bt.inorder_traversal(), [])
        self.assertEqual(self.bt.postorder_traversal(), [])
    
    def test_single_node_tree(self):
        """Test tree with single node"""
        bt = BinaryTree(1)
        self.assertFalse(bt.is_empty())
        self.assertEqual(bt.height(), 0)
        self.assertEqual(bt.size(), 1)
        self.assertEqual(bt.preorder_traversal(), [1])
        self.assertEqual(bt.inorder_traversal(), [1])
        self.assertEqual(bt.postorder_traversal(), [1])
    
    def test_manual_tree_construction(self):
        """Test manually constructed tree"""
        # Create tree:    1
        #               /   \
        #              2     3
        #             / \
        #            4   5
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
    
    def test_traversal_algorithms(self):
        """Test all traversal algorithms"""
        # Create tree:     A
        #               /     \
        #              B       C
        #             / \     /
        #            D   E   F
        bt = BinaryTree('A')
        bt.root.left = Node('B')
        bt.root.right = Node('C')
        bt.root.left.left = Node('D')
        bt.root.left.right = Node('E')
        bt.root.right.left = Node('F')
        
        # Test different traversal orders
        self.assertEqual(bt.preorder_traversal(), ['A', 'B', 'D', 'E', 'C', 'F'])
        self.assertEqual(bt.inorder_traversal(), ['D', 'B', 'E', 'A', 'F', 'C'])
        self.assertEqual(bt.postorder_traversal(), ['D', 'E', 'B', 'F', 'C', 'A'])


# ==================== HOW TO RUN TESTS ====================

if __name__ == '__main__':
    print("Running Binary Tree Tests...")
    print("=" * 30)
    unittest.main(verbosity=2)
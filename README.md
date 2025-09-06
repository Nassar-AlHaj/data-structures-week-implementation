# data-structures-week-implementation

## Description of Each Data Structure

### Dynamic Arrays
A resizable array that automatically grows when elements are added and shrinks when elements are removed.

```
Dynamic Array: [1][2][3][4][ ][ ][ ][ ]
               ↑              ↑
            elements        capacity
```

### Singly Linked List
A linear data structure where elements are stored in nodes, each containing data and a reference to the next node.

```
[1|•]→[2|•]→[3|•]→[4|null]
```

### Stack (using array and linked list)
A Last-In-First-Out (LIFO) data structure that supports push and pop operations. Implemented using both array and linked list approaches.

```
Stack (LIFO):
    ↓ pop
[4] ← top
[3]
[2]
[1] ← bottom
    ↑ push
```

### Queue (using array and linked list)
A First-In-First-Out (FIFO) data structure that supports enqueue and dequeue operations. Implemented using both array and linked list approaches.

```
Queue (FIFO):
dequeue ← [1][2][3][4] ← enqueue
          ↑         ↑
        front     rear
```

### Doubly Linked List
A linear data structure where each node contains data and references to both the next and previous nodes.

```
[null|1|•]⇄[•|2|•]⇄[•|3|•]⇄[•|4|null]
```

### Circular Linked List
A linked list where the last node points back to the first node, forming a circle.

```
    ┌─────────────────────┐
    ↓                     │
[1|•]→[2|•]→[3|•]→[4|•]──┘
```

### Binary Tree
A hierarchical data structure where each node has at most two children (left and right).

```
     1
   /   \
  2     3
 / \   /
4   5 6
```

### Binary Search Tree
A binary tree where the left subtree contains values less than the parent node, and the right subtree contains values greater than the parent node.

```
     5
   /   \
  3     7
 / \   / \
1   4 6   9
```

### Tree Traversal Algorithms (inorder, preorder, postorder)
- **Inorder**: Left → Root → Right
- **Preorder**: Root → Left → Right  
- **Postorder**: Left → Right → Root

```
     1
   /   \
  2     3
 / \
4   5

Preorder:  1 → 2 → 4 → 5 → 3
Inorder:   4 → 2 → 5 → 1 → 3
Postorder: 4 → 5 → 2 → 3 → 1
```

### Hash Table (with collision handling)
A data structure that implements an associative array using a hash function to compute an index. Handles collisions using separate chaining.

```
Hash Table (Separate Chaining):
Index:
[0] → [key1,val1] → [key4,val4]
[1] → [key2,val2]
[2] → null
[3] → [key3,val3]
```

### Min Heap
A complete binary tree where each parent node is smaller than or equal to its children.

```
Min Heap:
     1
   /   \
  3     2
 / \   /
7   4 5

Array: [1,3,2,7,4,5]
```

### Basic Graph (adjacency list representation)
A collection of vertices connected by edges, represented using adjacency lists for efficient storage.

```
Graph:
A → [B, C]
B → [A, D]
C → [A, D]
D → [B, C]

Visual:
A ─── B
│     │
│     │
C ─── D
```

### Trie
A tree-like data structure used for storing and searching strings efficiently.

```
Trie (words: "cat", "car", "card"):
      root
       │
       c
       │
       a
       │
       ├─ t (end)
       │
       r (end)
       │
       d (end)
```

### Union-Find (Disjoint Set)
A data structure that tracks a set of elements partitioned into disjoint subsets, supporting union and find operations.

```
Union-Find:
Initial: [0] [1] [2] [3] [4]

After union(0,1), union(2,3):
[0,1] [2,3] [4]

Tree representation:
  0   2   4
  │   │
  1   3
```

### Graph Traversal (BFS/DFS)
- **BFS (Breadth-First Search)**: Explores nodes level by level
- **DFS (Depth-First Search)**: Explores as far as possible along each branch before backtracking

```
Graph:     A
          / \
         B   C
        /   / \
       D   E   F

BFS from A: A → B → C → D → E → F
DFS from A: A → B → D → C → E → F
```

## Time/Space Complexity Analysis

| Data Structure | Access | Search | Insertion | Deletion | Space |
|---|---|---|---|---|---|
| Dynamic Array | O(1) | O(n) | O(1) amortized | O(1) amortized | O(n) |
| Singly Linked List | O(n) | O(n) | O(1) | O(n) | O(n) |
| Stack | N/A | N/A | O(1) | O(1) | O(n) |
| Queue | N/A | N/A | O(1) | O(1) | O(n) |
| Doubly Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Circular Linked List | O(n) | O(n) | O(1) | O(n) | O(n) |
| Binary Tree | O(n) | O(n) | O(n) | O(n) | O(n) |
| Binary Search Tree | O(log n) average, O(n) worst | O(log n) average, O(n) worst | O(log n) average, O(n) worst | O(log n) average, O(n) worst | O(n) |
| Hash Table | N/A | O(1) average, O(n) worst | O(1) average, O(n) worst | O(1) average, O(n) worst | O(n) |
| Min Heap | N/A | O(n) | O(log n) | O(log n) | O(n) |
| Graph (Adjacency List) | N/A | O(V + E) | O(1) | O(V) | O(V + E) |
| Trie | N/A | O(m) | O(m) | O(m) | O(ALPHABET_SIZE × N × M) |
| Union-Find | N/A | O(α(n)) | O(α(n)) | N/A | O(n) |
| BFS/DFS | N/A | N/A | N/A | N/A | O(V + E) |

Where:
- n = number of elements
- m = length of string
- V = number of vertices
- E = number of edges
- α = inverse Ackermann function

## Usage Examples

### Dynamic Array
```python
from Day1.dynamic_array import DynamicArray
arr = DynamicArray()
arr.append(1)
arr.append(2)
print(arr.get(0))  # Output: 1
```

### Singly Linked List
```python
from Day1.SinglyLinkedList import SinglyLinkedList
ll = SinglyLinkedList()
ll.insert_at_head(1)
ll.insert_at_tail(2)
```

### Stack
```python
from Day1.ArrayStack import ArrayStack
stack = ArrayStack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
```

### Queue
```python
from Day1.QueueArray import QueueArray
queue = QueueArray()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
```

### Binary Search Tree
```python
from Day3.BinarySearchTree import BinarySearchTree
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
print(bst.search(3))  # Output: True
```

### Hash Table
```python
from Day4.HashTableSeparateChaining import HashTable
ht = HashTable()
ht.put("key1", "value1")
print(ht.get("key1"))  # Output: value1
```

### Min Heap
```python
from Day4.MinHeap import MinHeap
heap = MinHeap()
heap.insert(5)
heap.insert(3)
print(heap.get_min())  # Output: 3
```

### Graph
```python
from Day4.Graph import Graph
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
```

### Trie
```python
from Day5.Trie import Trie
trie = Trie()
trie.insert("hello")
print(trie.search("hello"))  # Output: True
```

### Union-Find
```python
from Day5.UnionFind import UnionFind
uf = UnionFind(5)
uf.union(0, 1)
print(uf.connected(0, 1))  # Output: True
```

## How to Run Tests

Each implementation file contains test functions. To run tests for a specific data structure:

```bash
py Day1/dynamic_array.py
py Day1/SinglyLinkedList.py
py Day1/ArrayStack.py
py Day1/LinkedListStack.py
py Day1/QueueArray.py
py Day2/DoublyLinkedList.py
py Day2/CircularLinkedList.py
py Day2/LinkedListQueue.py
py Day3/BinaryTree.py
py Day3/BinarySearchTree.py
py Day4/HashTableSeparateChaining.py
py Day4/MinHeap.py
py Day4/Graph.py
py Day5/Trie.py
py Day5/UnionFind.py
py Day5/GraphTraversal.py
```

## Summary of All Implementations

This repository contains **16 complete data structure implementations** organized across 5 days of intensive training:

### Day 1 - Basic Linear Structures (5 implementations)
- ✅ **Dynamic Arrays**: Resizable array with automatic capacity management
- ✅ **Singly Linked List**: Basic linked list with head insertion and traversal
- ✅ **Array Stack**: LIFO implementation using dynamic array
- ✅ **Linked List Stack**: LIFO implementation using linked nodes
- ✅ **Array Queue**: FIFO implementation using array structure

### Day 2 - Advanced Linear Structures (3 implementations)
- ✅ **Doubly Linked List**: Bidirectional linked list with forward/backward traversal
- ✅ **Circular Linked List**: Circular structure with tail pointing to head
- ✅ **Linked List Queue**: FIFO implementation using linked nodes

### Day 3 - Tree Structures (2 implementations + algorithms)
- ✅ **Binary Tree**: Basic tree structure with insertion and traversal
- ✅ **Binary Search Tree**: Ordered tree with efficient search operations
- ✅ **Tree Traversal Algorithms**: Inorder, Preorder, and Postorder implementations

### Day 4 - Hash Tables, Heaps & Graphs (3 implementations)
- ✅ **Hash Table**: Separate chaining collision resolution
- ✅ **Min Heap**: Complete binary tree with heap property
- ✅ **Graph**: Adjacency list representation with basic operations

### Day 5 - Advanced Structures & Algorithms (3 implementations)
- ✅ **Trie**: Prefix tree for efficient string operations
- ✅ **Union-Find**: Disjoint set with path compression optimization
- ✅ **Graph Traversal**: BFS and DFS algorithms implementation

### Implementation Statistics:
- **Total Files**: 16 Python files
- **Lines of Code**: ~2000+ lines (estimated)
- **Test Cases**: Comprehensive testing for each structure
- **Documentation**: Full complexity analysis and usage examples
- **Time Invested**: 40-50 hours over one week
- **Programming Language**: Python 3.x

### Key Achievements:
1. **Complete Implementation**: All required data structures successfully implemented
2. **Production Quality**: Clean, documented, and tested code
3. **Performance Analysis**: Time/space complexity documented for each structure
4. **Best Practices**: Proper error handling and edge case management
5. **Repository Organization**: Clean folder structure and file naming conventions

### Technical Skills Demonstrated:
- Object-oriented programming in Python
- Algorithm design and analysis
- Memory management and optimization
- Code documentation and testing
- Git version control and repository management
# Data Structures - MCQ Batch 02
## Questions 101-200

---

### Question 101
Domain: Data Structures
Topic: Hash Tables
Subtopic: Hash Function
Difficulty: Medium

Question: What is good hash function property?
A) Always returns 0
B) Distributes keys uniformly, minimizes collisions
C) Returns same value
D) Random output

✔ Correct Answer: B

Reason: Good hash function distributes keys uniformly across table, minimizing collisions. Fast to compute, deterministic.

Tag: Past Paper

---

### Question 102
Domain: Data Structures
Topic: Hash Tables
Subtopic: Collision
Difficulty: Easy

Question: What is collision in hash table?
A) Memory collision
B) Different keys hash to same index
C) Syntax error
D) Hash error

✔ Correct Answer: B

Reason: Collision occurs when hash function maps different keys to same index. Resolved by chaining or open addressing.

Tag: Past Paper

---

### Question 103
Domain: Data Structures
Topic: Code Analysis
Subtopic: Hash Function Example
Difficulty: Medium

Question: What is the output?
```python
def hash_func(key, size):
    return key % size

print(hash_func(25, 10))
print(hash_func(35, 10))
```
A) 25 35
B) 5 5
C) 2 3
D) Error

✔ Correct Answer: B

Reason: Modulo hash function. 25 % 10 = 5, 35 % 10 = 5. Both hash to index 5 (collision).

Tag: Normal

---

### Question 104
Domain: Data Structures
Topic: Hash Tables
Subtopic: Chaining
Difficulty: Medium

Question: What is chaining in hash table?
A) Chain of tables
B) Each bucket contains linked list of colliding elements
C) Chain hash functions
D) No collisions

✔ Correct Answer: B

Reason: Chaining: each table index has linked list. Colliding elements added to list. Search time: O(1 + α) where α is load factor.

Tag: Past Paper

---

### Question 105
Domain: Data Structures
Topic: Hash Tables
Subtopic: Load Factor
Difficulty: Medium

Question: What is load factor?
A) Table size
B) n/m (elements / table size)
C) Collision count
D) Hash value

✔ Correct Answer: B

Reason: Load factor α = n/m. High load factor increases collisions. Rehash (resize table) when load factor exceeds threshold (typically 0.75).

Tag: Normal

---

### Question 106
Domain: Data Structures
Topic: Code Analysis
Subtopic: Chaining Implementation
Difficulty: Hard

Question: What is the output?
```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def insert(self, key):
        index = key % self.size
        self.table[index].append(key)
    
    def search(self, key):
        index = key % self.size
        return key in self.table[index]

ht = HashTable(5)
ht.insert(10)
ht.insert(15)
print(ht.search(15))
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: 15 % 5 = 0. Inserted at index 0. search(15) checks index 0, finds 15. Returns True.

Tag: Normal

---

### Question 107
Domain: Data Structures
Topic: Hash Tables
Subtopic: Open Addressing
Difficulty: Hard

Question: What is open addressing?
A) Open table
B) All elements stored in table array, probing finds next slot
C) Chaining
D) No addressing

✔ Correct Answer: B

Reason: Open addressing stores all elements in table array. On collision, probe for next empty slot. Methods: linear, quadratic, double hashing.

Tag: Normal

---

### Question 108
Domain: Data Structures
Topic: Hash Tables
Subtopic: Linear Probing
Difficulty: Hard

Question: What is linear probing?
A) Linear search
B) On collision, check next slot sequentially
C) Random probing
D) No probing

✔ Correct Answer: B

Reason: Linear probing: if index i occupied, try i+1, i+2, ... (mod table size). Simple but causes clustering.

Tag: Normal

---

### Question 109
Domain: Data Structures
Topic: Code Analysis
Subtopic: Linear Probing
Difficulty: Hard

Question: What is the output?
```python
def linear_probe(table, key, size):
    index = key % size
    original = index
    while table[index] is not None:
        if table[index] == key:
            return index
        index = (index + 1) % size
        if index == original:
            return -1  # Table full
    return index

table = [None] * 5
table[0] = 10
table[1] = 15
# Insert 20 (20 % 5 = 0, but 0 occupied)
print(linear_probe(table, 20, 5))
```
A) 0
B) 2
C) 1
D) -1

✔ Correct Answer: B

Reason: 20 % 5 = 0 (occupied by 10). Try 1 (occupied by 15). Try 2 (empty). Returns 2.

Tag: Normal

---

### Question 110
Domain: Data Structures
Topic: Hash Tables
Subtopic: Quadratic Probing
Difficulty: Hard

Question: What is quadratic probing?
A) Quadratic function
B) On collision, check slots at quadratic intervals (i+1², i+2², ...)
C) Linear probing
D) No probing

✔ Correct Answer: B

Reason: Quadratic probing: try i, i+1², i+2², i+3², ... Reduces primary clustering but can cause secondary clustering.

Tag: Normal

---

### Question 111
Domain: Data Structures
Topic: Hash Tables
Subtopic: Double Hashing
Difficulty: Hard

Question: What is double hashing?
A) Hash twice
B) Uses second hash function for probe sequence
C) Two tables
D) Double size

✔ Correct Answer: B

Reason: Double hashing: probe sequence uses second hash function. h(k, i) = (h1(k) + i*h2(k)) % m. Reduces clustering better than linear/quadratic.

Tag: Normal

---

### Question 112
Domain: Data Structures
Topic: Code Analysis
Subtopic: Hash Table Operations
Difficulty: Medium

Question: What is average time complexity of hash table operations?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: With good hash function and low load factor, insert, delete, search average O(1). Worst case O(n) with many collisions.

Tag: Past Paper

---

### Question 113
Domain: Data Structures
Topic: Hash Tables
Subtopic: Rehashing
Difficulty: Hard

Question: What is rehashing?
A) Hash again
B) Creating larger table and reinserting all elements
C) Deleting elements
D) Fixing collisions

✔ Correct Answer: B

Reason: When load factor exceeds threshold, create larger table (typically 2x), recompute hashes, reinsert all elements. O(n) operation.

Tag: Normal

---

### Question 114
Domain: Data Structures
Topic: Code Analysis
Subtopic: Hash Table Resize
Difficulty: Hard

Question: Why is rehashing expensive?
A) Complex algorithm
B) Must reinsert all n elements with new hash values
C) Deletes data
D) Not expensive

✔ Correct Answer: B

Reason: Rehashing requires computing new hash for all n elements and reinserting. O(n) operation. Amortized over many operations, still efficient.

Tag: Normal

---

### Question 115
Domain: Data Structures
Topic: Graphs
Subtopic: Graph Basics
Difficulty: Easy

Question: What is graph?
A) Chart
B) Set of vertices connected by edges
C) Tree
D) Array

✔ Correct Answer: B

Reason: Graph G = (V, E): set of vertices (nodes) and edges (connections). Can be directed or undirected, weighted or unweighted.

Tag: Past Paper

---

### Question 116
Domain: Data Structures
Topic: Graphs
Subtopic: Directed vs Undirected
Difficulty: Easy

Question: What is directed graph?
A) Graph with direction
B) Edges have direction (one-way)
C) Sorted graph
D) Straight graph

✔ Correct Answer: B

Reason: Directed graph (digraph): edges have direction. Edge (u, v) goes from u to v only. Undirected: edge connects both ways.

Tag: Past Paper

---

### Question 117
Domain: Data Structures
Topic: Code Analysis
Subtopic: Graph Representation
Difficulty: Medium

Question: What is the output?
```python
# Adjacency list
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: []
}
print(len(graph[2]))
```
A) 0
B) 2
C) 3
D) 4

✔ Correct Answer: B

Reason: graph[2] is list of neighbors of vertex 2: [0, 3]. Length is 2.

Tag: Normal

---

### Question 118
Domain: Data Structures
Topic: Graphs
Subtopic: Adjacency Matrix
Difficulty: Medium

Question: What is space complexity of adjacency matrix?
A) O(V)
B) O(V²)
C) O(E)
D) O(V + E)

✔ Correct Answer: B

Reason: Adjacency matrix is V×V array. Space: O(V²) regardless of edge count. Wasteful for sparse graphs.

Tag: Past Paper

---

### Question 119
Domain: Data Structures
Topic: Graphs
Subtopic: Adjacency List
Difficulty: Medium

Question: What is space complexity of adjacency list?
A) O(V²)
B) O(V + E)
C) O(E)
D) O(V)

✔ Correct Answer: B

Reason: Adjacency list: array of V lists, total E edges stored. Space: O(V + E). Efficient for sparse graphs.

Tag: Past Paper

---

### Question 120
Domain: Data Structures
Topic: Code Analysis
Subtopic: Adjacency Matrix
Difficulty: Medium

Question: What is the output?
```python
# Adjacency matrix for 4 vertices
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
# Count edges in undirected graph
edges = sum(sum(row) for row in matrix) // 2
print(edges)
```
A) 8
B) 4
C) 6
D) 2

✔ Correct Answer: B

Reason: Sum all 1s: 8. Undirected graph counts each edge twice. Divide by 2: 4 edges.

Tag: Normal

---

### Question 121
Domain: Data Structures
Topic: Graphs
Subtopic: Weighted Graphs
Difficulty: Easy

Question: What is weighted graph?
A) Heavy graph
B) Edges have associated weights/costs
C) Many edges
D) Balanced graph

✔ Correct Answer: B

Reason: Weighted graph: edges have weights representing cost, distance, capacity, etc. Used in shortest path, MST algorithms.

Tag: Normal

---

### Question 122
Domain: Data Structures
Topic: Code Analysis
Subtopic: Weighted Adjacency List
Difficulty: Medium

Question: What is the output?
```python
# Weighted graph
graph = {
    0: [(1, 4), (2, 1)],  # (neighbor, weight)
    1: [(2, 2)],
    2: []
}
print(graph[0][1][1])
```
A) 2
B) 1
C) 4
D) 0

✔ Correct Answer: B

Reason: graph[0] is [(1, 4), (2, 1)]. graph[0][1] is (2, 1). graph[0][1][1] is weight: 1.

Tag: Normal

---

### Question 123
Domain: Data Structures
Topic: Graphs
Subtopic: Graph Degree
Difficulty: Easy

Question: What is degree of vertex?
A) Temperature
B) Number of edges connected to vertex
C) Vertex value
D) Depth

✔ Correct Answer: B

Reason: Degree is number of edges incident to vertex. Directed graph: in-degree (incoming) and out-degree (outgoing).

Tag: Normal

---

### Question 124
Domain: Data Structures
Topic: Graphs
Subtopic: Handshaking Lemma
Difficulty: Hard

Question: What does handshaking lemma state?
A) Shake hands
B) Sum of all vertex degrees = 2 * number of edges
C) Degree sum = vertices
D) No relation

✔ Correct Answer: B

Reason: Each edge contributes 2 to total degree (one for each endpoint). Σ deg(v) = 2|E|. Useful for graph theory proofs.

Tag: Normal

---

### Question 125
Domain: Data Structures
Topic: Code Analysis
Subtopic: Degree Calculation
Difficulty: Medium

Question: What is the output?
```python
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}
print(len(graph[2]))
```
A) 2
B) 3
C) 4
D) 0

✔ Correct Answer: B

Reason: Degree of vertex 2 is number of neighbors: [0, 1, 3]. Degree is 3.

Tag: Normal

---

### Question 126
Domain: Data Structures
Topic: Graph Traversal
Subtopic: BFS
Difficulty: Medium

Question: What is time complexity of BFS?
A) O(V)
B) O(V + E)
C) O(E)
D) O(V²)

✔ Correct Answer: B

Reason: BFS visits all V vertices, explores all E edges. Time: O(V + E). Space: O(V) for queue and visited set.

Tag: Past Paper

---

### Question 127
Domain: Data Structures
Topic: Code Analysis
Subtopic: BFS Implementation
Difficulty: Hard

Question: What is the output?
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex])
    return result

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
print(bfs(graph, 0))
```
A) [0, 1, 2, 3]
B) [0, 1, 2, 3] or [0, 2, 1, 3]
C) [0, 3, 2, 1]
D) Error

✔ Correct Answer: B

Reason: BFS explores level by level. From 0: visits 0, then neighbors 1,2 (order may vary), then 3. Possible outputs shown.

Tag: Normal

---

### Question 128
Domain: Data Structures
Topic: Graph Traversal
Subtopic: DFS
Difficulty: Medium

Question: What is time complexity of DFS?
A) O(V)
B) O(V + E)
C) O(E)
D) O(V²)

✔ Correct Answer: B

Reason: DFS visits all V vertices, explores all E edges. Time: O(V + E). Space: O(V) for recursion stack or explicit stack.

Tag: Past Paper

---

### Question 129
Domain: Data Structures
Topic: Code Analysis
Subtopic: DFS Implementation
Difficulty: Hard

Question: What is the output?
```python
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
dfs(graph, 0)
```
A) 0 1 2 3
B) 0 1 3 2 or 0 2 3 1
C) 0 3 2 1
D) Error

✔ Correct Answer: B

Reason: DFS explores deeply. From 0: visits 0, then first neighbor (1 or 2), explores deeply, backtracks. Order depends on neighbor order.

Tag: Normal

---

### Question 130
Domain: Data Structures
Topic: Graph Traversal
Subtopic: BFS vs DFS
Difficulty: Medium

Question: When is BFS preferred over DFS?
A) Always
B) Finding shortest path in unweighted graph
C) Memory constrained
D) Never

✔ Correct Answer: B

Reason: BFS finds shortest path in unweighted graph (explores level by level). DFS uses less memory, better for deep graphs.

Tag: Normal

---

### Question 131
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Shortest Path
Difficulty: Medium

Question: Which algorithm finds shortest path in weighted graph with non-negative weights?
A) BFS
B) Dijkstra's algorithm
C) DFS
D) Linear search

✔ Correct Answer: B

Reason: Dijkstra's algorithm finds shortest path from source to all vertices in weighted graph with non-negative weights. Time: O((V+E) log V) with min-heap.

Tag: Past Paper

---

### Question 132
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bellman-Ford
Difficulty: Hard

Question: What advantage does Bellman-Ford have over Dijkstra?
A) Faster
B) Handles negative edge weights
C) Uses less memory
D) Simpler

✔ Correct Answer: B

Reason: Bellman-Ford handles negative weights, detects negative cycles. Time: O(VE). Dijkstra faster but requires non-negative weights.

Tag: Normal

---

### Question 133
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Spanning Tree
Difficulty: Medium

Question: What is minimum spanning tree (MST)?
A) Smallest tree
B) Subset of edges connecting all vertices with minimum total weight
C) Shortest path
D) Balanced tree

✔ Correct Answer: B

Reason: MST connects all vertices with minimum total edge weight, no cycles. Used in network design. Algorithms: Kruskal, Prim.

Tag: Past Paper

---

### Question 134
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Kruskal's Algorithm
Difficulty: Hard

Question: What data structure does Kruskal's algorithm use?
A) Queue
B) Disjoint Set Union (Union-Find)
C) Stack
D) Heap only

✔ Correct Answer: B

Reason: Kruskal sorts edges by weight, adds edge if doesn't create cycle. Union-Find detects cycles efficiently. Time: O(E log E).

Tag: Normal

---

### Question 135
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Prim's Algorithm
Difficulty: Hard

Question: What data structure does Prim's algorithm use?
A) Stack
B) Min-heap (priority queue)
C) Array only
D) Linked list

✔ Correct Answer: B

Reason: Prim grows MST from starting vertex, always adds minimum weight edge. Min-heap extracts minimum efficiently. Time: O((V+E) log V).

Tag: Normal

---

### Question 136
Domain: Data Structures
Topic: Code Analysis
Subtopic: Graph Cycle Detection
Difficulty: Hard

Question: What is the output?
```python
def has_cycle_dfs(graph, v, visited, rec_stack):
    visited[v] = True
    rec_stack[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            if has_cycle_dfs(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True
    rec_stack[v] = False
    return False

graph = {0: [1], 1: [2], 2: [0]}
visited = {i: False for i in range(3)}
rec_stack = {i: False for i in range(3)}
print(has_cycle_dfs(graph, 0, visited, rec_stack))
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: Graph has cycle: 0→1→2→0. DFS detects when visiting vertex already in recursion stack. Returns True.

Tag: Normal

---

### Question 137
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Topological Sort
Difficulty: Hard

Question: When is topological sort possible?
A) Any graph
B) Directed Acyclic Graph (DAG) only
C) Undirected graph
D) Cyclic graph

✔ Correct Answer: B

Reason: Topological sort orders vertices such that for edge (u,v), u comes before v. Only possible in DAG (no cycles).

Tag: Past Paper

---

### Question 138
Domain: Data Structures
Topic: Code Analysis
Subtopic: Topological Sort
Difficulty: Hard

Question: What is valid topological order?
```python
# DAG edges: 0→1, 0→2, 1→3, 2→3
```
A) [0, 1, 2, 3]
B) [3, 2, 1, 0]
C) [1, 0, 2, 3]
D) [0, 3, 1, 2]

✔ Correct Answer: A

Reason: Valid order: 0 before 1,2; 1,2 before 3. [0,1,2,3] or [0,2,1,3] valid. Option A satisfies all dependencies.

Tag: Normal

---

### Question 139
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Strongly Connected Components
Difficulty: Hard

Question: What is strongly connected component?
A) Connected graph
B) Maximal subgraph where every vertex reaches every other vertex
C) Weighted component
D) Tree component

✔ Correct Answer: B

Reason: In directed graph, SCC is maximal set of vertices where path exists between any pair. Kosaraju's, Tarjan's algorithms find SCCs.

Tag: Normal

---

### Question 140
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Trie
Difficulty: Medium

Question: What is Trie data structure?
A) Tree variant
B) Tree for storing strings, sharing common prefixes
C) Binary tree
D) Graph

✔ Correct Answer: B

Reason: Trie (prefix tree) stores strings efficiently. Each node represents character. Common prefixes share paths. Used in autocomplete, spell check.

Tag: Past Paper

---

### Question 141
Domain: Data Structures
Topic: Code Analysis
Subtopic: Trie Operations
Difficulty: Hard

Question: What is time complexity of inserting string of length m in Trie?
A) O(1)
B) O(m)
C) O(n)
D) O(m log n)

✔ Correct Answer: B

Reason: Insert traverses/creates m nodes (one per character). Time: O(m). Search also O(m). Space: O(ALPHABET_SIZE * m * n) worst case.

Tag: Normal

---

### Question 142
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Segment Tree
Difficulty: Hard

Question: What is segment tree used for?
A) Segmenting data
B) Range queries and updates efficiently
C) Sorting
D) Searching

✔ Correct Answer: B

Reason: Segment tree answers range queries (sum, min, max) in O(log n), updates in O(log n). Built in O(n). Used in competitive programming.

Tag: Normal

---

### Question 143
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Fenwick Tree
Difficulty: Hard

Question: What is Fenwick Tree (Binary Indexed Tree)?
A) Binary tree
B) Array-based structure for prefix sums and range queries
C) Search tree
D) Balanced tree

✔ Correct Answer: B

Reason: Fenwick Tree (BIT) supports prefix sum queries and point updates in O(log n). More space-efficient than segment tree. Uses bit manipulation.

Tag: Normal

---

### Question 144
Domain: Data Structures
Topic: Code Analysis
Subtopic: Prefix Sum
Difficulty: Medium

Question: What is the output?
```python
def update(bit, i, delta, n):
    while i <= n:
        bit[i] += delta
        i += i & (-i)

def query(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

bit = [0] * 6
update(bit, 1, 5, 5)
update(bit, 2, 3, 5)
print(query(bit, 2))
```
A) 5
B) 8
C) 3
D) 0

✔ Correct Answer: B

Reason: Fenwick tree. Update index 1 with 5, index 2 with 3. Query(2) returns prefix sum: 5+3 = 8.

Tag: Normal

---

### Question 145
Domain: Data Structures
Topic: Disjoint Set
Subtopic: Union-Find
Difficulty: Hard

Question: What is Union-Find data structure?
A) Set operations
B) Tracks disjoint sets, supports union and find operations
C) Search structure
D) Sorting structure

✔ Correct Answer: B

Reason: Union-Find (Disjoint Set Union) tracks partition of elements into disjoint sets. Operations: find(x) finds set, union(x,y) merges sets.

Tag: Normal

---

### Question 146
Domain: Data Structures
Topic: Disjoint Set
Subtopic: Path Compression
Difficulty: Hard

Question: What is path compression in Union-Find?
A) Compress data
B) Make all nodes point directly to root during find
C) Delete paths
D) Shorten edges

✔ Correct Answer: B

Reason: Path compression optimization: during find(x), make all nodes on path point to root. Flattens tree, improves future operations to nearly O(1).

Tag: Normal

---

### Question 147
Domain: Data Structures
Topic: Code Analysis
Subtopic: Union-Find Implementation
Difficulty: Hard

Question: What is the output?
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0) == uf.find(2))
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: union(0,1) and union(1,2) connect 0,1,2 in same set. find(0) and find(2) return same root. Returns True.

Tag: Normal

---

### Question 148
Domain: Data Structures
Topic: Disjoint Set
Subtopic: Union by Rank
Difficulty: Hard

Question: What is union by rank optimization?
A) Rank elements
B) Attach smaller tree under root of larger tree
C) Sort by rank
D) Delete ranks

✔ Correct Answer: B

Reason: Union by rank: attach tree with smaller rank under tree with larger rank. Keeps tree shallow. Combined with path compression: O(α(n)) amortized.

Tag: Normal

---

### Question 149
Domain: Data Structures
Topic: String Data Structures
Subtopic: Suffix Array
Difficulty: Hard

Question: What is suffix array?
A) Array of suffixes
B) Sorted array of all suffix indices of string
C) Prefix array
D) Character array

✔ Correct Answer: B

Reason: Suffix array: sorted array of starting indices of all suffixes. Used in pattern matching, string algorithms. Space: O(n), build: O(n log n).

Tag: Normal

---

### Question 150
Domain: Data Structures
Topic: String Data Structures
Subtopic: Suffix Tree
Difficulty: Hard

Question: What advantage does suffix tree have over suffix array?
A) Less space
B) Faster pattern matching O(m) vs O(m log n)
C) Simpler
D) No advantage

✔ Correct Answer: B

Reason: Suffix tree: pattern matching in O(m) where m is pattern length. Suffix array: O(m log n) with binary search. Suffix tree uses more space.

Tag: Normal

---
### Question 151
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Skip List
Difficulty: Hard

Question: What is skip list?
A) Skip elements
B) Probabilistic data structure with multiple levels for fast search
C) Linked list
D) Array

✔ Correct Answer: B

Reason: Skip list: multiple levels of linked lists. Higher levels skip elements. Search, insert, delete: O(log n) expected. Alternative to balanced trees.

Tag: Normal

---

### Question 152
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Bloom Filter
Difficulty: Hard

Question: What is Bloom filter?
A) Filter data
B) Probabilistic set membership test, may have false positives
C) Exact search
D) Sorting filter

✔ Correct Answer: B

Reason: Bloom filter: space-efficient probabilistic data structure. Tests set membership. May have false positives, never false negatives. Uses multiple hash functions.

Tag: Normal

---

### Question 153
Domain: Data Structures
Topic: Code Analysis
Subtopic: Stack Application
Difficulty: Medium

Question: What is the output?
```cpp
#include <stack>
#include <iostream>
using namespace std;

int main() {
    stack<int> s;
    s.push(10);
    s.push(20);
    s.push(30);
    s.pop();
    cout << s.top();
    return 0;
}
```
A) 10
B) 20
C) 30
D) Error

✔ Correct Answer: B

Reason: Push 10, 20, 30. Pop removes 30. top() returns 20 (current top element).

Tag: Normal

---

### Question 154
Domain: Data Structures
Topic: Queue Applications
Subtopic: Priority Queue
Difficulty: Medium

Question: What is time complexity of extracting minimum from min-heap?
A) O(1)
B) O(log n)
C) O(n)
D) O(n log n)

✔ Correct Answer: B

Reason: Extract-min removes root, replaces with last element, heapifies down. Heapify-down: O(log n). Insert also O(log n).

Tag: Past Paper

---

### Question 155
Domain: Data Structures
Topic: Code Analysis
Subtopic: Priority Queue
Difficulty: Hard

Question: What is the output?
```python
import heapq

pq = []
heapq.heappush(pq, (3, 'task3'))
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (2, 'task2'))
print(heapq.heappop(pq)[1])
```
A) task3
B) task1
C) task2
D) Error

✔ Correct Answer: B

Reason: Min-heap by default. Smallest priority (1, 'task1') extracted first. Returns 'task1'.

Tag: Normal

---

### Question 156
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Morris Traversal
Difficulty: Hard

Question: What is advantage of Morris traversal?
A) Faster
B) O(1) space (no recursion or stack)
C) Simpler
D) No advantage

✔ Correct Answer: B

Reason: Morris traversal uses threaded binary tree concept. Temporarily modifies tree (creates threads), traverses in O(1) space. Time: O(n).

Tag: Normal

---

### Question 157
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Splay Tree
Difficulty: Hard

Question: What is splay tree property?
A) Balanced
B) Recently accessed elements move to root via splaying
C) Sorted
D) Complete

✔ Correct Answer: B

Reason: Splay tree: self-adjusting BST. After access, splay operation moves node to root. Amortized O(log n) operations. Good for locality of reference.

Tag: Normal

---

### Question 158
Domain: Data Structures
Topic: Advanced Trees
Subtopic: B-Tree Properties
Difficulty: Hard

Question: Why are B-trees used in databases?
A) Simple
B) Minimize disk I/O with high branching factor
C) Fast in-memory
D) Small size

✔ Correct Answer: B

Reason: B-trees have high branching factor (many children per node). Reduces tree height, minimizes disk reads. Optimized for block-based storage.

Tag: Normal

---

### Question 159
Domain: Data Structures
Topic: Code Analysis
Subtopic: Deque Operations
Difficulty: Medium

Question: What is the output?
```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
dq.popleft()
print(dq[0])
```
A) 0
B) 1
C) 2
D) 4

✔ Correct Answer: B

Reason: Start [1,2,3]. appendleft(0): [0,1,2,3]. append(4): [0,1,2,3,4]. popleft(): [1,2,3,4]. dq[0] is 1.

Tag: Normal

---

### Question 160
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Floyd-Warshall
Difficulty: Hard

Question: What does Floyd-Warshall algorithm compute?
A) Single source shortest path
B) All-pairs shortest paths
C) MST
D) Topological sort

✔ Correct Answer: B

Reason: Floyd-Warshall finds shortest paths between all pairs of vertices. Time: O(V³). Works with negative weights, detects negative cycles.

Tag: Past Paper

---

### Question 161
Domain: Data Structures
Topic: Code Analysis
Subtopic: Dynamic Programming on Graphs
Difficulty: Hard

Question: What is time complexity of Floyd-Warshall?
A) O(V²)
B) O(V³)
C) O(VE)
D) O(E log V)

✔ Correct Answer: B

Reason: Three nested loops over V vertices. Time: O(V³). Space: O(V²) for distance matrix. Simple implementation.

Tag: Normal

---

### Question 162
Domain: Data Structures
Topic: Heap Operations
Subtopic: Heapify
Difficulty: Medium

Question: What is time complexity of building heap from array?
A) O(n log n)
B) O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Build heap using bottom-up heapify: O(n). Inserting n elements one-by-one: O(n log n). Bottom-up more efficient.

Tag: Past Paper

---

### Question 163
Domain: Data Structures
Topic: Code Analysis
Subtopic: Heap Sort
Difficulty: Hard

Question: What is the output?
```python
import heapq

arr = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(arr)
result = [heapq.heappop(arr) for _ in range(3)]
print(result)
```
A) [3, 1, 4]
B) [1, 1, 2]
C) [9, 6, 5]
D) Error

✔ Correct Answer: B

Reason: heapify creates min-heap. heappop extracts minimum 3 times: 1, 1, 2 (sorted order).

Tag: Normal

---

### Question 164
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Lowest Common Ancestor
Difficulty: Hard

Question: What is efficient algorithm for LCA queries?
A) Linear search
B) Binary lifting with preprocessing
C) DFS only
D) BFS only

✔ Correct Answer: B

Reason: Binary lifting preprocesses ancestors at powers of 2. LCA query: O(log n). Preprocessing: O(n log n). Alternative: Tarjan's offline algorithm.

Tag: Normal

---

### Question 165
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Articulation Points
Difficulty: Hard

Question: What is articulation point?
A) Point in graph
B) Vertex whose removal increases connected components
C) Edge
D) Root

✔ Correct Answer: B

Reason: Articulation point (cut vertex): removing it disconnects graph. Found using DFS with discovery/low times. Time: O(V + E).

Tag: Normal

---

### Question 166
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bridges
Difficulty: Hard

Question: What is bridge in graph?
A) Connection
B) Edge whose removal increases connected components
C) Vertex
D) Path

✔ Correct Answer: B

Reason: Bridge (cut edge): removing it disconnects graph. Found using DFS. Edge (u,v) is bridge if low[v] > disc[u].

Tag: Normal

---

### Question 167
Domain: Data Structures
Topic: Code Analysis
Subtopic: Graph Connectivity
Difficulty: Medium

Question: What is the output?
```python
def count_components(graph, n):
    visited = [False] * n
    count = 0
    
    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
print(count_components(graph, 5))
```
A) 1
B) 3
C) 5
D) 2

✔ Correct Answer: B

Reason: Three connected components: {0,1}, {2,3}, {4}. DFS runs 3 times. Returns 3.

Tag: Normal

---

### Question 168
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: KMP Algorithm
Difficulty: Hard

Question: What is KMP algorithm used for?
A) Sorting
B) Pattern matching in O(n+m) time
C) Searching
D) Hashing

✔ Correct Answer: B

Reason: Knuth-Morris-Pratt algorithm finds pattern in text. Preprocesses pattern to build LPS array. Time: O(n+m). No backtracking in text.

Tag: Normal

---

### Question 169
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Rabin-Karp
Difficulty: Hard

Question: What technique does Rabin-Karp use?
A) Binary search
B) Rolling hash for pattern matching
C) Sorting
D) Recursion

✔ Correct Answer: B

Reason: Rabin-Karp uses rolling hash. Computes hash of pattern and text windows. Average: O(n+m). Worst: O(nm) with many hash collisions.

Tag: Normal

---

### Question 170
Domain: Data Structures
Topic: Spatial Data Structures
Subtopic: Quadtree
Difficulty: Hard

Question: What is quadtree used for?
A) Four elements
B) Partitioning 2D space recursively into 4 quadrants
C) Binary tree
D) Queue

✔ Correct Answer: B

Reason: Quadtree partitions 2D space into 4 quadrants recursively. Used in image processing, collision detection, spatial indexing. Each node has 4 children.

Tag: Normal

---
### Question 171
Domain: Data Structures
Topic: Spatial Data Structures
Subtopic: K-D Tree
Difficulty: Hard

Question: What is K-D tree?
A) K dimensions
B) Binary tree partitioning k-dimensional space
C) K elements
D) K levels

✔ Correct Answer: B

Reason: K-D tree: binary space partitioning tree for k-dimensional points. Each level splits on different dimension. Used in nearest neighbor search.

Tag: Normal

---

### Question 172
Domain: Data Structures
Topic: Code Analysis
Subtopic: Array Rotation
Difficulty: Medium

Question: What is the output?
```java
public class Main {
    static void rotate(int[] arr, int k) {
        int n = arr.length;
        k = k % n;
        reverse(arr, 0, n-1);
        reverse(arr, 0, k-1);
        reverse(arr, k, n-1);
    }
    
    static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start++] = arr[end];
            arr[end--] = temp;
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        rotate(arr, 2);
        System.out.print(arr[0]);
    }
}
```
A) 1
B) 4
C) 3
D) 5

✔ Correct Answer: B

Reason: Rotate right by 2. Reverse all: [5,4,3,2,1]. Reverse first 2: [4,5,3,2,1]. Reverse rest: [4,5,1,2,3]. arr[0] = 4.

Tag: Normal

---

### Question 173
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Kadane's Algorithm
Difficulty: Hard

Question: What problem does Kadane's algorithm solve?
A) Sorting
B) Maximum subarray sum in O(n)
C) Searching
D) Minimum element

✔ Correct Answer: B

Reason: Kadane's algorithm finds maximum sum contiguous subarray. Dynamic programming approach. Time: O(n), Space: O(1).

Tag: Past Paper

---

### Question 174
Domain: Data Structures
Topic: Code Analysis
Subtopic: Kadane's Algorithm
Difficulty: Hard

Question: What is the output?
```python
def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    for num in arr:
        max_ending_here += num
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))
```
A) 4
B) 6
C) 10
D) -2

✔ Correct Answer: B

Reason: Maximum subarray: [4, -1, 2, 1] with sum 6. Kadane's algorithm tracks running sum, resets when negative.

Tag: Normal

---

### Question 175
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Two Pointer Technique
Difficulty: Medium

Question: When is two pointer technique useful?
A) Always
B) Sorted arrays, finding pairs, partitioning
C) Random access
D) Never

✔ Correct Answer: B

Reason: Two pointers: one at start, one at end (or both moving). Useful for sorted arrays, pair sum, removing duplicates. Time: O(n).

Tag: Normal

---

### Question 176
Domain: Data Structures
Topic: Code Analysis
Subtopic: Two Pointer
Difficulty: Medium

Question: What is the output?
```cpp
#include <iostream>
#include <vector>
using namespace std;

bool hasPairSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return true;
        else if (sum < target) left++;
        else right--;
    }
    return false;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << hasPairSum(arr, 9);
    return 0;
}
```
A) 0
B) 1
C) true
D) Error

✔ Correct Answer: B

Reason: Sorted array. Find pair sum 9: 4+5=9. Returns true (1 in C++). Two pointer technique.

Tag: Normal

---

### Question 177
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Sliding Window
Difficulty: Medium

Question: What is sliding window technique?
A) Window operations
B) Maintain window of elements, slide to process subarrays
C) Sorting
D) Searching

✔ Correct Answer: B

Reason: Sliding window: maintain window of k elements, slide one position at a time. Used for subarray problems. Time: O(n) vs O(nk) naive.

Tag: Normal

---

### Question 178
Domain: Data Structures
Topic: Code Analysis
Subtopic: Sliding Window
Difficulty: Hard

Question: What is the output?
```python
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(max_sum_subarray(arr, 4))
```
A) 39
B) 40
C) 38
D) 23

✔ Correct Answer: A

Reason: Maximum sum of 4 consecutive elements: [10, 23, 3, 1] = 37 or [4, 2, 10, 23] = 39. Maximum is 39.

Tag: Normal

---

### Question 179
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Common Subsequence
Difficulty: Hard

Question: What is time complexity of LCS using dynamic programming?
A) O(n)
B) O(mn)
C) O(n²)
D) O(2^n)

✔ Correct Answer: B

Reason: LCS of strings length m and n uses 2D DP table. Time: O(mn), Space: O(mn) or O(min(m,n)) optimized.

Tag: Past Paper

---

### Question 180
Domain: Data Structures
Topic: Code Analysis
Subtopic: LCS
Difficulty: Hard

Question: What is the output?
```python
def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

print(lcs_length("ABCD", "ACBD"))
```
A) 2
B) 3
C) 4
D) 1

✔ Correct Answer: B

Reason: LCS of "ABCD" and "ACBD" is "ABD" (length 3). DP builds solution bottom-up.

Tag: Normal

---
### Question 181
Domain: Data Structures
Topic: String Algorithms
Subtopic: Edit Distance
Difficulty: Hard

Question: What is edit distance (Levenshtein distance)?
A) String length
B) Minimum operations to transform one string to another
C) Character count
D) Substring count

✔ Correct Answer: B

Reason: Edit distance: minimum insertions, deletions, substitutions to transform s1 to s2. Computed using DP in O(mn) time.

Tag: Normal

---

### Question 182
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Sparse Table
Difficulty: Hard

Question: What is sparse table used for?
A) Sparse data
B) Static range queries in O(1) after O(n log n) preprocessing
C) Dynamic updates
D) Sorting

✔ Correct Answer: B

Reason: Sparse table answers static range queries (min, max, GCD) in O(1). Preprocessing: O(n log n). No updates supported.

Tag: Normal

---

### Question 183
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Diameter of Tree
Difficulty: Medium

Question: What is diameter of tree?
A) Tree width
B) Longest path between any two nodes
C) Tree height
D) Root to leaf

✔ Correct Answer: B

Reason: Diameter: longest path between any two nodes. Found using two DFS: first finds farthest node from any node, second finds farthest from that.

Tag: Normal

---

### Question 184
Domain: Data Structures
Topic: Code Analysis
Subtopic: Tree Diameter
Difficulty: Hard

Question: What is the output?
```python
def tree_height(node, graph, visited):
    visited.add(node)
    max_height = 0
    for neighbor in graph[node]:
        if neighbor not in visited:
            max_height = max(max_height, 1 + tree_height(neighbor, graph, visited))
    return max_height

# Tree: 0-1-2-3, 1-4
graph = {0: [1], 1: [0, 2, 4], 2: [1, 3], 3: [2], 4: [1]}
print(tree_height(0, graph, set()))
```
A) 2
B) 3
C) 4
D) 5

✔ Correct Answer: B

Reason: Longest path from 0: 0→1→2→3 (3 edges, height 3). Alternative: 0→1→4 (2 edges).

Tag: Normal

---

### Question 185
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bipartite Graph
Difficulty: Hard

Question: How to check if graph is bipartite?
A) Count vertices
B) Color vertices with 2 colors using BFS/DFS, check no adjacent same color
C) Count edges
D) Check cycles

✔ Correct Answer: B

Reason: Bipartite: vertices can be divided into 2 sets, edges only between sets. Check by 2-coloring. Graph is bipartite iff no odd-length cycle.

Tag: Normal

---

### Question 186
Domain: Data Structures
Topic: Code Analysis
Subtopic: Bipartite Check
Difficulty: Hard

Question: What is the output?
```python
from collections import deque

def is_bipartite(graph, n):
    color = [-1] * n
    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
print(is_bipartite(graph, 4))
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: Graph forms square: 0-1-2-3-0. Can be 2-colored: {0,2} one color, {1,3} another. Returns True.

Tag: Normal

---

### Question 187
Domain: Data Structures
Topic: Advanced Heaps
Subtopic: Fibonacci Heap
Difficulty: Hard

Question: What is advantage of Fibonacci heap?
A) Simple
B) Amortized O(1) for decrease-key operation
C) Less space
D) Faster search

✔ Correct Answer: B

Reason: Fibonacci heap: decrease-key in O(1) amortized. Used in Dijkstra, Prim for better complexity. Complex implementation.

Tag: Normal

---

### Question 188
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Network Flow
Difficulty: Hard

Question: What does Ford-Fulkerson algorithm compute?
A) Shortest path
B) Maximum flow in flow network
C) MST
D) Topological sort

✔ Correct Answer: B

Reason: Ford-Fulkerson finds maximum flow from source to sink. Uses augmenting paths. Time: O(E * max_flow) with DFS, O(VE²) with BFS (Edmonds-Karp).

Tag: Normal

---

### Question 189
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Segment Tree Lazy Propagation
Difficulty: Hard

Question: What is lazy propagation in segment tree?
A) Lazy evaluation
B) Defer updates to children until needed for range updates
C) Slow updates
D) No propagation

✔ Correct Answer: B

Reason: Lazy propagation: mark node with pending update, propagate to children only when needed. Range update: O(log n) instead of O(n log n).

Tag: Normal

---

### Question 190
Domain: Data Structures
Topic: Code Analysis
Subtopic: Monotonic Stack
Difficulty: Hard

Question: What is the output?
```python
def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    
    return result

arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))
```
A) [-1, -1, -1, -1, -1]
B) [5, 10, 10, -1, -1]
C) [5, 10, 10, 8, -1]
D) [10, 10, 10, -1, -1]

✔ Correct Answer: B

Reason: Next greater for each: 4→5, 5→10, 2→10, 10→none, 8→none. Monotonic stack maintains decreasing order.

Tag: Normal

---

### Question 191
Domain: Data Structures
Topic: Advanced Techniques
Subtopic: Monotonic Queue
Difficulty: Hard

Question: What is monotonic queue used for?
A) Sorted queue
B) Sliding window maximum/minimum in O(n)
C) Priority queue
D) FIFO

✔ Correct Answer: B

Reason: Monotonic queue maintains elements in increasing/decreasing order. Used for sliding window max/min. Each element enters/exits once: O(n).

Tag: Normal

---

### Question 192
Domain: Data Structures
Topic: Code Analysis
Subtopic: Sliding Window Maximum
Difficulty: Hard

Question: What is the output?
```python
from collections import deque

def max_sliding_window(arr, k):
    dq = deque()
    result = []
    
    for i in range(len(arr)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    
    return result

arr = [1, 3, -1, -3, 5, 3, 6, 7]
print(max_sliding_window(arr, 3))
```
A) [3, 3, 5, 5, 6, 7]
B) [1, 3, -1, -3, 5, 3]
C) [3, 3, 3, 5, 6, 7]
D) [7, 7, 7, 7, 7, 7]

✔ Correct Answer: A

Reason: Windows: [1,3,-1]→3, [3,-1,-3]→3, [-1,-3,5]→5, [-3,5,3]→5, [5,3,6]→6, [3,6,7]→7. Monotonic deque maintains max.

Tag: Normal

---

### Question 193
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Lifting
Difficulty: Hard

Question: What is binary lifting?
A) Lifting nodes
B) Preprocessing ancestors at powers of 2 for fast queries
C) Tree rotation
D) Balancing

✔ Correct Answer: B

Reason: Binary lifting: precompute ancestor[node][i] = 2^i-th ancestor. Jump to any ancestor in O(log n). Used for LCA, kth ancestor.

Tag: Normal

---

### Question 194
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Tarjan's Algorithm
Difficulty: Hard

Question: What does Tarjan's algorithm find?
A) Shortest path
B) Strongly connected components in O(V+E)
C) MST
D) Cycles

✔ Correct Answer: B

Reason: Tarjan's algorithm finds SCCs using single DFS. Maintains discovery time and low-link values. Time: O(V+E). Alternative to Kosaraju's.

Tag: Normal

---

### Question 195
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Cartesian Tree
Difficulty: Hard

Question: What is Cartesian tree property?
A) Cartesian coordinates
B) Binary tree satisfying heap property and in-order gives original array
C) Balanced tree
D) Search tree

✔ Correct Answer: B

Reason: Cartesian tree: binary tree from array. Min-heap property (parent < children), in-order traversal gives original array. Used in range minimum query.

Tag: Normal

---

### Question 196
Domain: Data Structures
Topic: Code Analysis
Subtopic: Stack Application
Difficulty: Medium

Question: What is the output?
```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        s.push(1);
        s.push(2);
        s.push(3);
        System.out.print(s.pop() + s.pop());
    }
}
```
A) 3
B) 5
C) 6
D) Error

✔ Correct Answer: B

Reason: Pop returns 3, then pop returns 2. Sum: 3 + 2 = 5.

Tag: Normal

---

### Question 197
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Dutch National Flag
Difficulty: Hard

Question: What problem does Dutch National Flag algorithm solve?
A) Sorting flags
B) Partitioning array into 3 parts in O(n)
C) Searching
D) Counting

✔ Correct Answer: B

Reason: Dutch National Flag: partition array into 3 parts (low, mid, high) in single pass. Used in 3-way quicksort. Time: O(n), Space: O(1).

Tag: Normal

---

### Question 198
Domain: Data Structures
Topic: Code Analysis
Subtopic: Three-way Partitioning
Difficulty: Hard

Question: What is the output?
```python
def dutch_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return arr

arr = [2, 0, 1, 2, 1, 0]
print(dutch_flag(arr))
```
A) [0, 0, 1, 1, 2, 2]
B) [2, 2, 1, 1, 0, 0]
C) [0, 1, 2, 0, 1, 2]
D) [2, 0, 1, 2, 1, 0]

✔ Correct Answer: A

Reason: Partitions into 0s, 1s, 2s. Three pointers move elements to correct regions. Result: [0, 0, 1, 1, 2, 2].

Tag: Normal

---

### Question 199
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Eulerian Path
Difficulty: Hard

Question: When does Eulerian path exist?
A) Always
B) Graph has exactly 0 or 2 vertices with odd degree
C) All even degrees
D) Never

✔ Correct Answer: B

Reason: Eulerian path visits every edge exactly once. Exists if 0 or 2 odd-degree vertices. Eulerian circuit (cycle) exists if all even degrees.

Tag: Past Paper

---

### Question 200
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Hamiltonian Path
Difficulty: Hard

Question: What is difference between Eulerian and Hamiltonian path?
A) No difference
B) Eulerian visits every edge once, Hamiltonian visits every vertex once
C) Eulerian visits vertices, Hamiltonian visits edges
D) Same path

✔ Correct Answer: B

Reason: Eulerian path: every edge once (polynomial check). Hamiltonian path: every vertex once (NP-complete). Hamiltonian harder to determine.

Tag: Normal

---

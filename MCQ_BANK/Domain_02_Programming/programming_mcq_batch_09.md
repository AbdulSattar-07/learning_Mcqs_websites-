# Programming - MCQ Batch 09
## Questions 801-900

---

### Question 801
Domain: Programming
Topic: Code Analysis
Subtopic: yield from Example
Difficulty: Hard

Question: What is the output?
```python
def sub_gen():
    yield 1
    yield 2

def main_gen():
    yield from sub_gen()
    yield 3

print(list(main_gen()))
```
A) [1, 2]
B) [1, 2, 3]
C) [3]
D) Error

✔ Correct Answer: B

Reason: yield from sub_gen() yields all values from sub_gen (1, 2), then yields 3. Result: [1, 2, 3].

Tag: Normal

---

### Question 802
Domain: Programming
Topic: Comprehension Scope
Subtopic: Variable Leakage
Difficulty: Hard

Question: What is the output?
```python
x = 10
result = [x for x in range(3)]
print(x)
```
A) 2
B) 10
C) 0
D) Error

✔ Correct Answer: B

Reason: Python 3 comprehensions have own scope. x inside comprehension doesn't leak. Outer x remains 10. Python 2 leaked variables.

Tag: Normal

---

### Question 803
Domain: Programming
Topic: Code Analysis
Subtopic: Nested Comprehension Scope
Difficulty: Hard

Question: What is the output?
```python
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row if num > 2]
print(flat)
```
A) [1, 2, 3, 4]
B) [3, 4]
C) [1, 2]
D) Error

✔ Correct Answer: B

Reason: Nested comprehension with filter. Flattens matrix, keeps only num > 2: [3, 4].

Tag: Normal

---

### Question 804
Domain: Programming
Topic: Dictionary Comprehension
Subtopic: Dict from Lists
Difficulty: Medium

Question: What is the output?
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)
```
A) {'a': 1, 'b': 2, 'c': 3}
B) [('a', 1), ('b', 2), ('c', 3)]
C) Error
D) {'a': 'a', 'b': 'b', 'c': 'c'}

✔ Correct Answer: A

Reason: zip() pairs keys and values. Dict comprehension creates dictionary: {'a': 1, 'b': 2, 'c': 3}.

Tag: Normal

---

### Question 805
Domain: Programming
Topic: Code Analysis
Subtopic: Dict Inversion
Difficulty: Hard

Question: What is the output?
```python
d = {'a': 1, 'b': 2, 'c': 1}
inverted = {v: k for k, v in d.items()}
print(inverted)
```
A) {'a': 1, 'b': 2, 'c': 1}
B) {1: 'c', 2: 'b'}
C) {1: 'a', 2: 'b'}
D) Error

✔ Correct Answer: B

Reason: Inverts keys and values. Duplicate values (1) overwrite: last key 'c' for value 1. Result: {1: 'c', 2: 'b'}.

Tag: Normal

---

### Question 806
Domain: Programming
Topic: Set Comprehension
Subtopic: Unique Values
Difficulty: Medium

Question: What is the output?
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {x for x in nums}
print(sorted(unique))
```
A) [1, 2, 2, 3, 3, 3]
B) [1, 2, 3]
C) {1, 2, 3}
D) Error

✔ Correct Answer: B

Reason: Set comprehension creates set (removes duplicates): {1, 2, 3}. sorted() returns sorted list: [1, 2, 3].

Tag: Normal

---

### Question 807
Domain: Programming
Topic: Code Analysis
Subtopic: Conditional Comprehension
Difficulty: Hard

Question: What is the output?
```python
result = [x if x > 0 else 0 for x in [-2, -1, 0, 1, 2]]
print(result)
```
A) [1, 2]
B) [0, 0, 0, 1, 2]
C) [-2, -1, 0, 1, 2]
D) Error

✔ Correct Answer: B

Reason: Ternary in comprehension: if x > 0 keep x, else use 0. Negative values become 0: [0, 0, 0, 1, 2].

Tag: Normal

---

### Question 808
Domain: Programming
Topic: Functional Programming
Subtopic: First-Class Functions
Difficulty: Medium

Question: What does "first-class functions" mean?
A) Best functions
B) Functions can be assigned to variables, passed as arguments, returned
C) Primary functions
D) Class methods

✔ Correct Answer: B

Reason: First-class functions are treated like any other value: assignable, passable, returnable. Enables higher-order functions, callbacks.

Tag: Normal

---

### Question 809
Domain: Programming
Topic: Code Analysis
Subtopic: Function as Return Value
Difficulty: Hard

Question: What is the output?
```python
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5), triple(5))
```
A) 10 10
B) 10 15
C) 5 5
D) Error

✔ Correct Answer: B

Reason: multiplier returns function closing over factor. double has factor=2, triple has factor=3. double(5)=10, triple(5)=15.

Tag: Normal

---

### Question 810
Domain: Programming
Topic: Functional Programming
Subtopic: Pure Functions
Difficulty: Medium

Question: What is a pure function?
A) Clean function
B) No side effects, same input always gives same output
C) Simple function
D) Fast function

✔ Correct Answer: B

Reason: Pure function has no side effects (doesn't modify external state), deterministic (same input → same output). Easier to test, reason about.

Tag: Normal

---

### Question 811
Domain: Programming
Topic: Code Analysis
Subtopic: Side Effects
Difficulty: Medium

Question: Which function is pure?
```python
# A
def add(a, b):
    return a + b

# B
def add_to_list(lst, val):
    lst.append(val)
    return lst
```
A) B only
B) A only
C) Both
D) Neither

✔ Correct Answer: B

Reason: A is pure (no side effects, deterministic). B has side effect (modifies lst), not pure. Pure functions don't modify arguments.

Tag: Normal

---

### Question 812
Domain: Programming
Topic: Functional Programming
Subtopic: Immutability
Difficulty: Medium

Question: Why prefer immutability in functional programming?
A) Faster
B) Prevents side effects, easier reasoning, thread-safe
C) Uses less memory
D) Required

✔ Correct Answer: B

Reason: Immutable data prevents accidental modifications, eliminates side effects, naturally thread-safe (no race conditions). Functional programming principle.

Tag: Normal

---

### Question 813
Domain: Programming
Topic: Code Analysis
Subtopic: Immutable Update
Difficulty: Hard

Question: What is the output?
```python
original = (1, 2, 3)
updated = original + (4,)
print(original, updated)
```
A) (1, 2, 3, 4) (1, 2, 3, 4)
B) (1, 2, 3) (1, 2, 3, 4)
C) Error
D) (1, 2, 3, 4) (1, 2, 3)

✔ Correct Answer: B

Reason: Tuples immutable. Concatenation creates new tuple. original unchanged: (1, 2, 3). updated is new: (1, 2, 3, 4).

Tag: Normal

---

### Question 814
Domain: Programming
Topic: Recursion
Subtopic: Mutual Recursion
Difficulty: Hard

Question: What is mutual recursion?
A) Recursive functions
B) Two or more functions calling each other recursively
C) Single recursion
D) No recursion

✔ Correct Answer: B

Reason: Mutual recursion: functions call each other. is_even(n) calls is_odd(n-1), is_odd(n) calls is_even(n-1). Need base cases in both.

Tag: Normal

---

### Question 815
Domain: Programming
Topic: Code Analysis
Subtopic: Mutual Recursion Example
Difficulty: Hard

Question: What is the output?
```python
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(4))
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: is_even(4) → is_odd(3) → is_even(2) → is_odd(1) → is_even(0) → True. 4 is even, returns True.

Tag: Normal

---

### Question 816
Domain: Programming
Topic: Algorithm Design
Subtopic: Memoization Pattern
Difficulty: Hard

Question: What is the output?
```python
cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

print(fib(5))
```
A) 3
B) 5
C) 8
D) Error

✔ Correct Answer: B

Reason: Memoized fibonacci. fib(5) = fib(4) + fib(3) = 3 + 2 = 5. Cache prevents redundant calculations.

Tag: Normal

---

### Question 817
Domain: Programming
Topic: Algorithm Design
Subtopic: Tabulation
Difficulty: Hard

Question: What's the difference between memoization and tabulation?
A) No difference
B) Memoization is top-down (recursive), tabulation is bottom-up (iterative)
C) Tabulation is slower
D) Memoization is deprecated

✔ Correct Answer: B

Reason: Memoization: top-down recursive with caching. Tabulation: bottom-up iterative filling table. Both are DP approaches.

Tag: Normal

---

### Question 818
Domain: Programming
Topic: Code Analysis
Subtopic: Tabulation Example
Difficulty: Hard

Question: What approach is this?
```python
def fib(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return table[n]
```
A) Memoization
B) Tabulation
C) Recursion
D) Brute force

✔ Correct Answer: B

Reason: Bottom-up iterative approach filling table from base cases. Tabulation (DP). No recursion, builds solution iteratively.

Tag: Normal

---

### Question 819
Domain: Programming
Topic: Space Optimization
Subtopic: Fibonacci Space Optimization
Difficulty: Hard

Question: What is space complexity of optimized fibonacci?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Only need last two values, not entire table. Use two variables: prev, curr. Space: O(1). Time still O(n).

Tag: Normal

---

### Question 820
Domain: Programming
Topic: Code Analysis
Subtopic: Space-Optimized DP
Difficulty: Hard

Question: What is the output?
```python
def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fib(6))
```
A: 5
B) 8
C) 13
D) Error

✔ Correct Answer: B

Reason: Space-optimized fibonacci. Maintains only last two values. fib(6) = 8. Sequence: 0,1,1,2,3,5,8.

Tag: Normal

---

### Question 821
Domain: Programming
Topic: Divide and Conquer
Subtopic: Merge Sort Implementation
Difficulty: Hard

Question: What is the merge step in merge sort?
A) Splits array
B) Combines two sorted arrays into one sorted array
C) Sorts array
D) Finds middle

✔ Correct Answer: B

Reason: Merge step combines two sorted subarrays into single sorted array. Compares elements from both, adds smaller to result.

Tag: Normal

---

### Question 822
Domain: Programming
Topic: Code Analysis
Subtopic: Merge Function
Difficulty: Hard

Question: What is time complexity of merging two sorted arrays?
A) O(1)
B) O(n + m)
C) O(n * m)
D) O(log n)

✔ Correct Answer: B

Reason: Merge compares and copies all elements from both arrays once. Total: O(n + m) where n, m are array sizes.

Tag: Normal

---

### Question 823
Domain: Programming
Topic: Divide and Conquer
Subtopic: Quick Sort Partition
Difficulty: Hard

Question: What does partition step do in quick sort?
A) Divides array
B) Rearranges array so elements < pivot on left, > pivot on right
C) Sorts array
D) Finds median

✔ Correct Answer: B

Reason: Partition chooses pivot, rearranges so smaller elements left, larger right. Pivot in final position. Recursively sort partitions.

Tag: Normal

---

### Question 824
Domain: Programming
Topic: Code Analysis
Subtopic: Pivot Selection
Difficulty: Hard

Question: What affects quick sort performance?
A) Array size only
B) Pivot selection strategy
C) Data type
D) Nothing

✔ Correct Answer: B

Reason: Poor pivot (always min/max) causes O(n²). Good pivot (median) gives O(n log n). Random pivot or median-of-three improves average case.

Tag: Normal

---

### Question 825
Domain: Programming
Topic: Binary Search
Subtopic: Binary Search Variants
Difficulty: Hard

Question: What is lower_bound in binary search?
A) Minimum value
B) First position where element could be inserted maintaining order
C) Lowest index
D) Error

✔ Correct Answer: B

Reason: Lower bound finds first position >= target. Upper bound finds first position > target. Used for range queries in sorted arrays.

Tag: Normal

---

### Question 826
Domain: Programming
Topic: Code Analysis
Subtopic: Binary Search Insertion
Difficulty: Hard

Question: What does bisect.bisect_left() return?
```python
import bisect
arr = [1, 3, 3, 5]
print(bisect.bisect_left(arr, 3))
```
A) 0
B) 1
C) 2
D) 3

✔ Correct Answer: B

Reason: bisect_left() finds leftmost insertion point. For 3 in [1, 3, 3, 5], leftmost position is index 1 (before existing 3s).

Tag: Normal

---

### Question 827
Domain: Programming
Topic: Binary Search
Subtopic: bisect_right
Difficulty: Hard

Question: What's the difference between bisect_left and bisect_right?
A) No difference
B) bisect_left inserts before equal elements, bisect_right after
C) bisect_right is faster
D) bisect_left is deprecated

✔ Correct Answer: B

Reason: bisect_left() finds position before equal elements. bisect_right() (or bisect()) finds position after. For duplicates, different positions.

Tag: Normal

---

### Question 828
Domain: Programming
Topic: Code Analysis
Subtopic: bisect_right Example
Difficulty: Hard

Question: What is the output?
```python
import bisect
arr = [1, 3, 3, 5]
print(bisect.bisect_right(arr, 3))
```
A) 1
B) 3
C) 2
D) 4

✔ Correct Answer: B

Reason: bisect_right() finds rightmost insertion point. For 3 in [1, 3, 3, 5], rightmost position is index 3 (after existing 3s).

Tag: Normal

---

### Question 829
Domain: Programming
Topic: Trie
Subtopic: Trie Data Structure
Difficulty: Hard

Question: What is a Trie?
A) Try structure
B) Tree for storing strings with common prefixes
C) Triangle
D) Triple tree

✔ Correct Answer: B

Reason: Trie (prefix tree) stores strings efficiently, sharing common prefixes. Used for autocomplete, spell checking, IP routing.

Tag: Normal

---

### Question 830
Domain: Programming
Topic: Code Analysis
Subtopic: Trie Operations
Difficulty: Hard

Question: What is time complexity of Trie search?
A) O(n)
B) O(m) where m is string length
C) O(log n)
D) O(1)

✔ Correct Answer: B

Reason: Trie search traverses m nodes for string of length m. Independent of number of strings stored. Insert, delete also O(m).

Tag: Normal

---

### Question 831
Domain: Programming
Topic: Graph Algorithms
Subtopic: Dijkstra's Algorithm
Difficulty: Hard

Question: What does Dijkstra's algorithm find?
A) All paths
B) Shortest path from source to all vertices
C) Longest path
D) Cycles

✔ Correct Answer: B

Reason: Dijkstra's finds shortest paths from source to all vertices in weighted graph with non-negative weights. Uses priority queue.

Tag: Past Paper

---

### Question 832
Domain: Programming
Topic: Graph Algorithms
Subtopic: Bellman-Ford
Difficulty: Hard

Question: What advantage does Bellman-Ford have over Dijkstra?
A) Faster
B) Handles negative edge weights
C) Simpler
D) No advantage

✔ Correct Answer: B

Reason: Bellman-Ford handles negative weights, detects negative cycles. Slower O(VE) vs Dijkstra O((V+E) log V). Dijkstra fails with negative weights.

Tag: Normal

---

### Question 833
Domain: Programming
Topic: Graph Algorithms
Subtopic: Floyd-Warshall
Difficulty: Hard

Question: What does Floyd-Warshall algorithm find?
A) Single source shortest paths
B) All-pairs shortest paths
C) Minimum spanning tree
D) Cycles only

✔ Correct Answer: B

Reason: Floyd-Warshall finds shortest paths between all pairs of vertices. O(V³) time, works with negative weights, detects negative cycles.

Tag: Normal

---

### Question 834
Domain: Programming
Topic: Graph Algorithms
Subtopic: Topological Sort
Difficulty: Hard

Question: What is topological sort?
A) Sorting algorithm
B) Linear ordering of vertices in DAG respecting edge directions
C) Graph sorting
D) Topology

✔ Correct Answer: B

Reason: Topological sort orders vertices in Directed Acyclic Graph so for edge u→v, u comes before v. Used for task scheduling, dependency resolution.

Tag: Past Paper

---

### Question 835
Domain: Programming
Topic: Code Analysis
Subtopic: Topological Sort Application
Difficulty: Hard

Question: When is topological sort applicable?
A) Any graph
B) Directed Acyclic Graph (DAG) only
C) Undirected graph
D) Cyclic graph

✔ Correct Answer: B

Reason: Topological sort only works on DAG (no cycles). Cycles make linear ordering impossible. Use DFS or Kahn's algorithm.

Tag: Normal

---

### Question 836
Domain: Programming
Topic: Graph Algorithms
Subtopic: Minimum Spanning Tree
Difficulty: Hard

Question: What is minimum spanning tree?
A) Smallest tree
B) Subset of edges connecting all vertices with minimum total weight
C) Shortest path tree
D) Balanced tree

✔ Correct Answer: B

Reason: MST connects all vertices with minimum total edge weight, no cycles. Prim's and Kruskal's algorithms find MST.

Tag: Past Paper

---

### Question 837
Domain: Programming
Topic: Graph Algorithms
Subtopic: Prim's vs Kruskal's
Difficulty: Hard

Question: What's the difference between Prim's and Kruskal's?
A) No difference
B) Prim's grows tree from vertex, Kruskal's adds cheapest edge
C) Prim's is faster
D) Kruskal's is deprecated

✔ Correct Answer: B

Reason: Prim's starts from vertex, grows tree by adding nearest vertex. Kruskal's sorts edges, adds cheapest edge not creating cycle. Both find MST.

Tag: Normal

---

### Question 838
Domain: Programming
Topic: Union-Find
Subtopic: Disjoint Set
Difficulty: Hard

Question: What is Union-Find data structure?
A) Union of sets
B) Tracks disjoint sets, supports union and find operations
C) Set operations
D) Array union

✔ Correct Answer: B

Reason: Union-Find (Disjoint Set Union) tracks partition into disjoint sets. find() determines set, union() merges sets. Used in Kruskal's algorithm.

Tag: Normal

---

### Question 839
Domain: Programming
Topic: Code Analysis
Subtopic: Union-Find Operations
Difficulty: Hard

Question: What is time complexity of Union-Find with path compression?
A) O(n)
B) O(α(n)) - nearly constant
C) O(log n)
D) O(1)

✔ Correct Answer: B

Reason: With path compression and union by rank, operations are O(α(n)) where α is inverse Ackermann function (effectively constant).

Tag: Normal

---

### Question 840
Domain: Programming
Topic: Dynamic Programming
Subtopic: Coin Change Problem
Difficulty: Hard

Question: What is coin change problem?
A) Changing coins
B) Minimum coins needed to make amount
C) Counting coins
D) Sorting coins

✔ Correct Answer: B

Reason: Given coin denominations, find minimum coins to make target amount. Classic DP problem. dp[i] = min coins for amount i.

Tag: Normal

---

### Question 841
Domain: Programming
Topic: Code Analysis
Subtopic: Coin Change DP
Difficulty: Hard

Question: What is the output?
```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 2, 5], 11))
```
A) 5
B) 3
C) 11
D) -1

✔ Correct Answer: B

Reason: Minimum coins for 11: 5+5+1 = 3 coins. DP builds solution: dp[11] = 3.

Tag: Normal

---

### Question 842
Domain: Programming
Topic: Dynamic Programming
Subtopic: Edit Distance
Difficulty: Hard

Question: What is edit distance (Levenshtein distance)?
A) Text editing
B) Minimum operations to transform one string to another
C) String length difference
D) Character distance

✔ Correct Answer: B

Reason: Edit distance is minimum insertions, deletions, substitutions to transform string1 to string2. DP problem, used in spell checking.

Tag: Normal

---

### Question 843
Domain: Programming
Topic: Code Analysis
Subtopic: Edit Distance Complexity
Difficulty: Hard

Question: What is time complexity of edit distance DP?
A) O(n)
B) O(n * m)
C) O(n²)
D) O(n + m)

✔ Correct Answer: B

Reason: DP table size n×m where n, m are string lengths. Fill each cell once: O(n*m) time and space.

Tag: Normal

---

### Question 844
Domain: Programming
Topic: Greedy Algorithms
Subtopic: Huffman Coding
Difficulty: Hard

Question: What is Huffman coding?
A) Code encryption
B) Optimal prefix-free encoding based on frequency
C) Code compression
D) Error correction

✔ Correct Answer: B

Reason: Huffman coding creates optimal prefix-free binary codes based on character frequencies. Frequent characters get shorter codes. Used in compression.

Tag: Normal

---

### Question 845
Domain: Programming
Topic: Graph Algorithms
Subtopic: Cycle Detection
Difficulty: Hard

Question: How do you detect cycle in undirected graph using DFS?
A) Check all edges
B) If visiting visited node (not parent), cycle exists
C) Count vertices
D) Cannot detect

✔ Correct Answer: B

Reason: DFS marks vertices visited. If encounter visited vertex (not parent), back edge exists, indicating cycle.

Tag: Normal

---

### Question 846
Domain: Programming
Topic: Code Analysis
Subtopic: Directed Graph Cycle
Difficulty: Hard

Question: How do you detect cycle in directed graph?
A) Same as undirected
B) Track recursion stack, if visit node in stack, cycle exists
C) Count edges
D) Cannot detect

✔ Correct Answer: B

Reason: Use recursion stack (or colors). If DFS encounters node in current recursion stack, back edge exists, cycle detected.

Tag: Normal

---

### Question 847
Domain: Programming
Topic: Graph Algorithms
Subtopic: Strongly Connected Components
Difficulty: Hard

Question: What is strongly connected component?
A) Strong connection
B) Maximal subgraph where every vertex reaches every other vertex
C) Connected graph
D) Component count

✔ Correct Answer: B

Reason: SCC is maximal set of vertices where each vertex reachable from every other. Kosaraju's or Tarjan's algorithm finds SCCs.

Tag: Normal

---

### Question 848
Domain: Programming
Topic: Graph Algorithms
Subtopic: Bipartite Graph
Difficulty: Hard

Question: What is bipartite graph?
A) Two graphs
B) Graph whose vertices can be divided into two sets with edges only between sets
C) Binary graph
D) Paired graph

✔ Correct Answer: B

Reason: Bipartite graph has two disjoint vertex sets, edges only between sets. Check with BFS/DFS coloring (2-colorable).

Tag: Normal

---

### Question 849
Domain: Programming
Topic: Code Analysis
Subtopic: Bipartite Check
Difficulty: Hard

Question: How do you check if graph is bipartite?
A) Count vertices
B) Try 2-coloring with BFS/DFS, if possible then bipartite
C) Check edges
D) Cannot check

✔ Correct Answer: B

Reason: Assign colors (0/1) to vertices. If adjacent vertices get same color, not bipartite. If successful 2-coloring, bipartite.

Tag: Normal

---

### Question 850
Domain: Programming
Topic: String Algorithms
Subtopic: KMP Algorithm
Difficulty: Hard

Question: What does KMP algorithm do?
A) Sorts strings
B) Pattern matching in O(n+m) using prefix function
C) Encrypts strings
D) Compresses strings

✔ Correct Answer: B

Reason: KMP (Knuth-Morris-Pratt) finds pattern in text efficiently. Preprocesses pattern to avoid redundant comparisons. O(n+m) vs naive O(n*m).

Tag: Normal

---

### Question 851
Domain: Programming
Topic: String Algorithms
Subtopic: Rabin-Karp
Difficulty: Hard

Question: What technique does Rabin-Karp use?
A) Binary search
B) Rolling hash for pattern matching
C) Sorting
D) Recursion

✔ Correct Answer: B

Reason: Rabin-Karp uses rolling hash to compare pattern with text substrings. O(n+m) average, O(n*m) worst case with hash collisions.

Tag: Normal

---

### Question 852
Domain: Programming
Topic: Code Analysis
Subtopic: Longest Palindromic Substring
Difficulty: Hard

Question: What is time complexity of expanding around center for longest palindrome?
A) O(n)
B) O(n²)
C) O(n³)
D) O(log n)

✔ Correct Answer: B

Reason: Try each position as center (n positions), expand outward (O(n) per center): O(n²). Manacher's algorithm achieves O(n).

Tag: Normal

---

### Question 853
Domain: Programming
Topic: Dynamic Programming
Subtopic: Matrix Chain Multiplication
Difficulty: Hard

Question: What does matrix chain multiplication problem optimize?
A) Matrix values
B) Order of matrix multiplications to minimize operations
C) Matrix size
D) Multiplication speed

✔ Correct Answer: B

Reason: Different parenthesization orders have different costs. DP finds optimal order minimizing scalar multiplications. O(n³) time.

Tag: Normal

---

### Question 854
Domain: Programming
Topic: Dynamic Programming
Subtopic: Longest Increasing Subsequence
Difficulty: Hard

Question: What is LIS problem?
A) Longest string
B) Longest subsequence with increasing elements
C) Largest number
D) List size

✔ Correct Answer: B

Reason: LIS finds longest subsequence where elements are in increasing order (not necessarily consecutive). [10,9,2,5,3,7,101,18] has LIS [2,3,7,101] length 4.

Tag: Normal

---

### Question 855
Domain: Programming
Topic: Code Analysis
Subtopic: LIS Complexity
Difficulty: Hard

Question: What is time complexity of LIS using DP?
A) O(n)
B) O(n²)
C) O(n log n)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: DP approach: for each element, check all previous elements. O(n²). Binary search optimization achieves O(n log n).

Tag: Normal

---

### Question 856
Domain: Programming
Topic: Bit Manipulation
Subtopic: Subset Generation
Difficulty: Hard

Question: How do you generate all subsets using bits?
A) Recursion only
B) Iterate 0 to 2ⁿ-1, each bit represents element inclusion
C) Nested loops
D) Cannot use bits

✔ Correct Answer: B

Reason: For n elements, 2ⁿ subsets. Each number 0 to 2ⁿ-1 represents subset (bit i set = include element i).

Tag: Normal

---

### Question 857
Domain: Programming
Topic: Code Analysis
Subtopic: Subset Bits
Difficulty: Hard

Question: What is the output?
```python
def subsets(arr):
    n = len(arr)
    count = 0
    for i in range(1 << n):  # 2^n
        subset = [arr[j] for j in range(n) if i & (1 << j)]
        count += 1
    return count

print(subsets([1, 2, 3]))
```
A) 3
B) 8
C) 7
D) 6

✔ Correct Answer: B

Reason: 3 elements have 2³ = 8 subsets (including empty). Counts all subsets: 8.

Tag: Normal

---

### Question 858
Domain: Programming
Topic: Bit Manipulation
Subtopic: Single Number
Difficulty: Hard

Question: How do you find single non-duplicate number using XOR?
A) Count occurrences
B) XOR all numbers (duplicates cancel)
C) Sort and compare
D) Use set

✔ Correct Answer: B

Reason: XOR properties: x^x=0, x^0=x. XORing all numbers cancels duplicates, leaving single number. O(n) time, O(1) space.

Tag: Normal

---

### Question 859
Domain: Programming
Topic: Code Analysis
Subtopic: XOR Single Number
Difficulty: Hard

Question: What is the output?
```python
nums = [4, 1, 2, 1, 2]
result = 0
for num in nums:
    result ^= num
print(result)
```
A) 0
B) 4
C) 10
D) Error

✔ Correct Answer: B

Reason: XOR all: 4^1^2^1^2. Pairs cancel (1^1=0, 2^2=0). Result: 4^0^0 = 4.

Tag: Normal

---

### Question 860
Domain: Programming
Topic: Sliding Window
Subtopic: Fixed Window
Difficulty: Hard

Question: What is time complexity of fixed-size sliding window?
A) O(n * k)
B) O(n)
C) O(n²)
D) O(k)

✔ Correct Answer: B

Reason: Slide window once through array, updating in O(1) per slide (add new, remove old). Total: O(n) vs O(n*k) brute force.

Tag: Normal

---

### Question 861
Domain: Programming
Topic: Code Analysis
Subtopic: Sliding Window Max
Difficulty: Hard

Question: What is the output?
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

print(max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
```
A) 20
B) 24
C) 39
D) 10

✔ Correct Answer: B

Reason: Maximum sum of 4 consecutive elements. Window [10, 2, 3, 1] has sum 16. Window [2, 10, 2, 3] has sum 17. Window [4, 2, 10, 2] has sum 18. Actually [10, 2, 3, 1, 0, 20] wait, k=4: [2, 3, 1, 0] + next gives [3, 1, 0, 20] = 24.

Tag: Normal

---

### Question 862
Domain: Programming
Topic: Two Pointers
Subtopic: Container With Most Water
Difficulty: Hard

Question: What strategy solves container with most water?
A) Brute force
B) Two pointers from ends, move pointer at shorter height
C) Binary search
D) DP

✔ Correct Answer: B

Reason: Two pointers at ends. Area = min(height[left], height[right]) * width. Move pointer at shorter height inward. O(n) time.

Tag: Normal

---

### Question 863
Domain: Programming
Topic: Code Analysis
Subtopic: Three Sum Problem
Difficulty: Hard

Question: What is time complexity of three sum using sorting and two pointers?
A) O(n)
B) O(n²)
C) O(n³)
D) O(n log n)

✔ Correct Answer: B

Reason: Sort O(n log n), then for each element, two-pointer search O(n). Total: O(n²). Brute force: O(n³).

Tag: Normal

---

### Question 864
Domain: Programming
Topic: Hashing
Subtopic: Two Sum Problem
Difficulty: Medium

Question: What is time complexity of two sum using hash map?
A) O(n²)
B) O(n)
C) O(log n)
D) O(1)

✔ Correct Answer: B

Reason: Single pass: for each element, check if complement exists in hash map. O(1) lookup, O(n) total. Brute force: O(n²).

Tag: Normal

---

### Question 865
Domain: Programming
Topic: Code Analysis
Subtopic: Two Sum Implementation
Difficulty: Hard

Question: What is the output?
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
```
A) [2, 7]
B) [0, 1]
C) [7, 2]
D) []

✔ Correct Answer: B

Reason: Finds indices where nums[i] + nums[j] = target. 2 + 7 = 9 at indices 0 and 1. Returns [0, 1].

Tag: Normal

---

### Question 866
Domain: Programming
Topic: Stack Applications
Subtopic: Next Greater Element
Difficulty: Hard

Question: What data structure efficiently finds next greater element?
A) Queue
B) Stack
C) Heap
D) Array

✔ Correct Answer: B

Reason: Stack stores elements in decreasing order. For each element, pop smaller elements (they found their next greater). O(n) time.

Tag: Normal

---

### Question 867
Domain: Programming
Topic: Code Analysis
Subtopic: Monotonic Stack
Difficulty: Hard

Question: What is monotonic stack?
A) Single stack
B) Stack maintaining elements in monotonic order
C) Static stack
D) Mono stack

✔ Correct Answer: B

Reason: Monotonic stack maintains increasing or decreasing order. Push element after popping elements violating order. Used for next greater/smaller problems.

Tag: Normal

---

### Question 868
Domain: Programming
Topic: Queue Applications
Subtopic: Sliding Window Maximum
Difficulty: Hard

Question: What data structure efficiently finds maximum in sliding window?
A) Array
B) Deque (monotonic decreasing)
C) Stack
D) Heap

✔ Correct Answer: B

Reason: Monotonic deque stores indices in decreasing order of values. Front has maximum. Remove out-of-window indices. O(n) time.

Tag: Normal

---

### Question 869
Domain: Programming
Topic: Code Analysis
Subtopic: Prefix Sum
Difficulty: Medium

Question: What is the output?
```python
arr = [1, 2, 3, 4, 5]
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Sum of arr[1:4]
print(prefix[4] - prefix[1])
```
A) 6
B) 9
C) 10
D) Error

✔ Correct Answer: B

Reason: Prefix sum: [0, 1, 3, 6, 10, 15]. Sum arr[1:4] = arr[1]+arr[2]+arr[3] = 2+3+4 = 9. prefix[4]-prefix[1] = 10-1 = 9.

Tag: Normal

---

### Question 870
Domain: Programming
Topic: Prefix Sum
Subtopic: Range Sum Query
Difficulty: Hard

Question: What is time complexity of range sum query with prefix sum?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Precompute prefix sums O(n). Each range query: prefix[j+1] - prefix[i] in O(1). Preprocessing enables fast queries.

Tag: Normal

---

### Question 871
Domain: Programming
Topic: Binary Indexed Tree
Subtopic: Fenwick Tree
Difficulty: Hard

Question: What is Binary Indexed Tree (Fenwick Tree)?
A) Binary tree
B) Data structure for efficient prefix sum updates and queries
C) Search tree
D) Balanced tree

✔ Correct Answer: B

Reason: BIT supports update and prefix sum query in O(log n). More space-efficient than segment tree. Used for dynamic cumulative frequency.

Tag: Normal

---

### Question 872
Domain: Programming
Topic: Segment Tree
Subtopic: Range Queries
Difficulty: Hard

Question: What does segment tree efficiently support?
A) Sorting
B) Range queries and updates
C) Searching
D) Insertion

✔ Correct Answer: B

Reason: Segment tree supports range queries (sum, min, max) and updates in O(log n). Build: O(n). Used for range minimum query.

Tag: Normal

---

### Question 873
Domain: Programming
Topic: Code Analysis
Subtopic: Segment Tree Complexity
Difficulty: Hard

Question: What is space complexity of segment tree?
A) O(n)
B) O(4n) ≈ O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Segment tree needs approximately 4n space (2n-1 nodes, use 4n for simplicity). Still O(n) space complexity.

Tag: Normal

---

### Question 874
Domain: Programming
Topic: Trie Applications
Subtopic: Autocomplete
Difficulty: Medium

Question: Why is Trie good for autocomplete?
A) Fast sorting
B) Efficiently finds all words with given prefix
C) Stores more words
D) Compresses data

✔ Correct Answer: B

Reason: Trie groups words by prefix. Finding prefix takes O(m), then traverse subtree for all words with that prefix. Efficient prefix search.

Tag: Normal

---

### Question 875
Domain: Programming
Topic: Code Analysis
Subtopic: Trie Node Structure
Difficulty: Hard

Question: What does Trie node typically contain?
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```
A) Value only
B) Children dict and end-of-word flag
C) Parent reference
D) Word list

✔ Correct Answer: B

Reason: Trie node has children dict (char → child node) and is_end flag marking word completion. No need to store value.

Tag: Normal

---

### Question 876
Domain: Programming
Topic: Bloom Filter
Subtopic: Probabilistic Data Structure
Difficulty: Hard

Question: What is Bloom filter?
A) Filter function
B) Space-efficient probabilistic set membership test
C) Image filter
D) Data filter

✔ Correct Answer: B

Reason: Bloom filter tests set membership with possible false positives (says yes when no) but no false negatives. Space-efficient, used in caches.

Tag: Normal

---

### Question 877
Domain: Programming
Topic: Skip List
Subtopic: Probabilistic Structure
Difficulty: Hard

Question: What is skip list?
A) Skipped list
B) Probabilistic data structure with multiple levels for fast search
C) Linked list
D) Array list

✔ Correct Answer: B

Reason: Skip list is linked list with multiple levels (express lanes). O(log n) average search, insert, delete. Alternative to balanced trees.

Tag: Normal

---

### Question 878
Domain: Programming
Topic: Code Analysis
Subtopic: LRU Cache
Difficulty: Hard

Question: What data structures implement LRU cache efficiently?
A) Array only
B) Hash map + doubly linked list
C) Stack
D) Queue only

✔ Correct Answer: B

Reason: Hash map for O(1) lookup, doubly linked list for O(1) removal/addition. Move accessed items to front, evict from back.

Tag: Normal

---

### Question 879
Domain: Programming
Topic: LRU Cache
Subtopic: Cache Operations
Difficulty: Hard

Question: What is time complexity of LRU cache get and put?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Hash map provides O(1) lookup. Doubly linked list provides O(1) removal/insertion. Both operations: O(1).

Tag: Normal

---

### Question 880
Domain: Programming
Topic: Code Analysis
Subtopic: OrderedDict LRU
Difficulty: Hard

Question: What is the output?
```python
from collections import OrderedDict

class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

lru = LRU(2)
lru.cache[1] = 'a'
lru.cache[2] = 'b'
print(lru.get(1))
```
A) -1
B) a
C) 1
D) Error

✔ Correct Answer: B

Reason: Key 1 exists in cache. move_to_end() marks as recently used. Returns value 'a'.

Tag: Normal

---

### Question 881
Domain: Programming
Topic: Design Patterns
Subtopic: Strategy Pattern
Difficulty: Hard

Question: What is Strategy pattern?
A) Planning strategy
B) Defines family of algorithms, makes them interchangeable
C) Single algorithm
D) Optimization pattern

✔ Correct Answer: B

Reason: Strategy pattern encapsulates algorithms in separate classes, allowing runtime selection. Client uses interface, concrete strategies implement it.

Tag: Normal

---

### Question 882
Domain: Programming
Topic: Design Patterns
Subtopic: Decorator Pattern
Difficulty: Hard

Question: What is Decorator pattern (not Python decorator)?
A) Decorates code
B) Adds behavior to object dynamically without modifying class
C) Python decorator
D) Design only

✔ Correct Answer: B

Reason: Decorator pattern wraps object to add functionality. Wrapper implements same interface. Different from Python's @decorator syntax.

Tag: Normal

---

### Question 883
Domain: Programming
Topic: Design Patterns
Subtopic: Adapter Pattern
Difficulty: Hard

Question: What is Adapter pattern?
A) Adapts code
B) Converts interface to another interface client expects
C) Adapter class
D) Configuration

✔ Correct Answer: B

Reason: Adapter makes incompatible interfaces work together. Wraps adaptee, provides interface client expects. Like power adapter.

Tag: Normal

---

### Question 884
Domain: Programming
Topic: Code Analysis
Subtopic: Adapter Example
Difficulty: Hard

Question: What does this adapter do?
```python
class OldSystem:
    def old_method(self):
        return "Old"

class Adapter:
    def __init__(self, old):
        self.old = old
    
    def new_method(self):
        return self.old.old_method()

adapter = Adapter(OldSystem())
print(adapter.new_method())
```
A) Error
B) Old
C) New
D) None

✔ Correct Answer: B

Reason: Adapter wraps OldSystem, provides new_method() interface that calls old_method(). Returns "Old".

Tag: Normal

---

### Question 885
Domain: Programming
Topic: Design Patterns
Subtopic: Facade Pattern
Difficulty: Hard

Question: What is Facade pattern?
A) Building facade
B) Simplified interface to complex subsystem
C) Front-end pattern
D) Decoration

✔ Correct Answer: B

Reason: Facade provides simple interface hiding complex subsystem. Client interacts with facade, which delegates to subsystem components.

Tag: Normal

---

### Question 886
Domain: Programming
Topic: Design Patterns
Subtopic: Proxy Pattern
Difficulty: Hard

Question: What is Proxy pattern?
A) Network proxy
B) Placeholder controlling access to another object
C) Proxy server
D) Copy pattern

✔ Correct Answer: B

Reason: Proxy controls access to real object, adding functionality (lazy loading, access control, logging). Implements same interface as real object.

Tag: Normal

---

### Question 887
Domain: Programming
Topic: Design Patterns
Subtopic: Command Pattern
Difficulty: Hard

Question: What is Command pattern?
A) Command line
B) Encapsulates request as object
C) Command execution
D) Function call

✔ Correct Answer: B

Reason: Command pattern encapsulates request as object with execute() method. Enables undo/redo, queuing, logging requests.

Tag: Normal

---

### Question 888
Domain: Programming
Topic: Code Analysis
Subtopic: Command Pattern Example
Difficulty: Hard

Question: What does this pattern enable?
```python
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
    def execute(self):
        self.light.turn_on()

class Remote:
    def __init__(self):
        self.command = None
    def set_command(self, command):
        self.command = command
    def press_button(self):
        self.command.execute()
```
A) Nothing special
B) Decoupling invoker from receiver, enables undo/redo
C) Faster execution
D) Error

✔ Correct Answer: B

Reason: Command pattern decouples Remote (invoker) from Light (receiver). Can store commands for undo, queue them, log them.

Tag: Normal

---

### Question 889
Domain: Programming
Topic: Design Patterns
Subtopic: Template Method
Difficulty: Hard

Question: What is Template Method pattern?
A) Code template
B) Defines algorithm skeleton, subclasses override specific steps
C) Method template
D) Documentation

✔ Correct Answer: B

Reason: Template method defines algorithm structure in base class, subclasses implement specific steps. Promotes code reuse, enforces algorithm structure.

Tag: Normal

---

### Question 890
Domain: Programming
Topic: Design Patterns
Subtopic: State Pattern
Difficulty: Hard

Question: What is State pattern?
A) State management
B) Object changes behavior when internal state changes
C) State variable
D) Condition pattern

✔ Correct Answer: B

Reason: State pattern encapsulates states as objects. Context delegates to current state object. State transitions change behavior.

Tag: Normal

---

### Question 891
Domain: Programming
Topic: Code Analysis
Subtopic: State Pattern Example
Difficulty: Hard

Question: What is the output?
```python
class State:
    def handle(self):
        pass

class StateA(State):
    def handle(self):
        return "Handling A"

class StateB(State):
    def handle(self):
        return "Handling B"

class Context:
    def __init__(self):
        self.state = StateA()
    
    def request(self):
        return self.state.handle()

ctx = Context()
print(ctx.request())
```
A) State
B) Handling A
C) Handling B
D) Error

✔ Correct Answer: B

Reason: Context has StateA. request() delegates to state.handle(). StateA.handle() returns "Handling A".

Tag: Normal

---

### Question 892
Domain: Programming
Topic: Design Patterns
Subtopic: Builder Pattern
Difficulty: Hard

Question: What is Builder pattern?
A) Builds classes
B) Constructs complex objects step by step
C) Constructor pattern
D) Factory pattern

✔ Correct Answer: B

Reason: Builder separates construction from representation, building complex objects step by step. Useful for objects with many optional parameters.

Tag: Normal

---

### Question 893
Domain: Programming
Topic: Design Patterns
Subtopic: Prototype Pattern
Difficulty: Hard

Question: What is Prototype pattern?
A) First pattern
B) Creates objects by cloning existing instance
C) Template pattern
D) Base pattern

✔ Correct Answer: B

Reason: Prototype creates new objects by copying existing prototype. Useful when creation is expensive. Implements clone() method.

Tag: Normal

---

### Question 894
Domain: Programming
Topic: Code Analysis
Subtopic: Shallow Copy Issue
Difficulty: Hard

Question: What is the output?
```python
class Prototype:
    def __init__(self):
        self.data = [1, 2, 3]
    
    def clone(self):
        import copy
        return copy.copy(self)

p1 = Prototype()
p2 = p1.clone()
p2.data.append(4)
print(len(p1.data))
```
A) 3
B) 4
C) 0
D) Error

✔ Correct Answer: B

Reason: copy.copy() creates shallow copy. p2.data references same list as p1.data. Appending to p2.data affects p1.data. Length: 4.

Tag: Normal

---

### Question 895
Domain: Programming
Topic: Design Patterns
Subtopic: Chain of Responsibility
Difficulty: Hard

Question: What is Chain of Responsibility pattern?
A) Responsibility chain
B) Passes request along chain of handlers until one handles it
C) Linked handlers
D) Error chain

✔ Correct Answer: B

Reason: Chain of Responsibility passes request through handler chain. Each handler decides to process or pass to next. Decouples sender from receivers.

Tag: Normal

---

### Question 896
Domain: Programming
Topic: Design Patterns
Subtopic: Mediator Pattern
Difficulty: Hard

Question: What is Mediator pattern?
A) Middle pattern
B) Centralizes communication between objects
C) Mediation
D) Middleware

✔ Correct Answer: B

Reason: Mediator centralizes complex communications between objects. Objects communicate through mediator instead of directly, reducing coupling.

Tag: Normal

---

### Question 897
Domain: Programming
Topic: Design Patterns
Subtopic: Memento Pattern
Difficulty: Hard

Question: What is Memento pattern?
A) Memory pattern
B) Captures and restores object state (undo functionality)
C: Remembers objects
D) Memo pattern

✔ Correct Answer: B

Reason: Memento captures object state without violating encapsulation. Enables undo/redo by storing and restoring states.

Tag: Normal

---

### Question 898
Domain: Programming
Topic: Code Analysis
Subtopic: Iterator Pattern
Difficulty: Medium

Question: What does Iterator pattern provide?
A) Iteration only
B) Way to access collection elements sequentially without exposing structure
C) Loop pattern
D) Counter

✔ Correct Answer: B

Reason: Iterator provides uniform interface for traversing different collections. Hides internal structure, supports multiple simultaneous iterations.

Tag: Normal

---

### Question 899
Domain: Programming
Topic: Design Patterns
Subtopic: Visitor Pattern
Difficulty: Hard

Question: What is Visitor pattern?
A) Visits objects
B) Separates algorithm from object structure it operates on
C) Traversal pattern
D) Guest pattern

✔ Correct Answer: B

Reason: Visitor separates operations from object structure. Add new operations without modifying classes. Objects accept visitor, visitor performs operation.

Tag: Normal

---

### Question 900
Domain: Programming
Topic: Code Analysis
Subtopic: Composite Pattern
Difficulty: Hard

Question: What is Composite pattern?
A) Composed objects
B) Treats individual objects and compositions uniformly
C) Complex pattern
D) Multiple patterns

✔ Correct Answer: B

Reason: Composite pattern composes objects into tree structures. Treats leaf and composite objects uniformly through common interface. Used for hierarchies.

Tag: Normal

---

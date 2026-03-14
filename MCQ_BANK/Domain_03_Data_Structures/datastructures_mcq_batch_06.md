# Data Structures - MCQ Batch 06
## Questions 501-600

---

### Question 501
Domain: Data Structures
Topic: Backtracking
Subtopic: Subset Generation
Difficulty: Medium

Question: What is the time complexity of generating all subsets using backtracking?
A) O(n)
B) O(n²)
C) O(2ⁿ)
D) O(n!)

✔ Correct Answer: C

Reason: Each element has 2 choices (include/exclude), generating 2ⁿ subsets. Each subset takes O(n) to process, total O(n*2ⁿ).

Tag: Normal

---

### Question 502
Domain: Data Structures
Topic: Backtracking
Subtopic: Permutations
Difficulty: Hard

Question: What is the time complexity of generating all permutations?
A) O(n)
B) O(n²)
C) O(2ⁿ)
D) O(n!)

✔ Correct Answer: D

Reason: n! permutations exist for n elements. Generating each takes O(n) time, total O(n*n!) complexity.

Tag: Past Paper

---

### Question 503
Domain: Data Structures
Topic: Code Analysis
Subtopic: Permutation Generation
Difficulty: Hard

Question: [Missing question - Please review]

```python
def permute(nums):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return
        
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    
    backtrack([], nums)
    return result

nums = [1, 2, 3]
print(len(permute(nums)))
```
What is the output?
A) 3
B) 6
C) 9
D) 27

✔ Correct Answer: B

Reason: 3 elements have 3! = 6 permutations: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

Tag: Normal

---

### Question 504
Domain: Data Structures
Topic: Backtracking
Subtopic: Combination Sum
Difficulty: Hard

Question: In combination sum problem with unlimited element reuse, what is the key difference from subset sum?
A) No difference
B) Same element can be used multiple times
C) Only works with positive numbers
D) Requires sorting

✔ Correct Answer: B

Reason: Combination sum allows unlimited reuse of elements, while subset sum uses each element at most once. Backtracking explores with repetition.

Tag: Normal

---

### Question 505
Domain: Data Structures
Topic: Backtracking
Subtopic: Palindrome Partitioning
Difficulty: Hard

Question: What is the worst-case time complexity of finding all palindrome partitions?
A) O(n)
B) O(n²)
C) O(n * 2ⁿ)
D) O(n!)

✔ Correct Answer: C

Reason: 2ⁿ possible partitions exist. Checking each partition for palindromes takes O(n), giving O(n*2ⁿ) worst case.

Tag: Normal

---

### Question 506
Domain: Data Structures
Topic: Code Analysis
Subtopic: Rat in Maze
Difficulty: Medium

Question: [Missing question - Please review]

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool solveMaze(vector<vector<int>>& maze, int x, int y, vector<vector<int>>& sol) {
    int n = maze.size();
    
    if(x == n-1 && y == n-1 && maze[x][y] == 1) {
        sol[x][y] = 1;
        return true;
    }
    
    if(x >= 0 && x < n && y >= 0 && y < n && maze[x][y] == 1) {
        sol[x][y] = 1;
        
        if(solveMaze(maze, x+1, y, sol)) return true;
        if(solveMaze(maze, x, y+1, sol)) return true;
        
        sol[x][y] = 0;
        return false;
    }
    
    return false;
}

// What technique is this?
```
What algorithm is used?
A) Dynamic programming
B) Backtracking
C) Greedy
D) Divide and conquer

✔ Correct Answer: B

Reason: Rat in maze uses backtracking: try path, if blocked backtrack (sol[x][y]=0) and try alternative route.

Tag: Normal

---

### Question 507
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Topological Sort Applications
Difficulty: Hard

Question: Which problem can be solved using topological sort?
A) Shortest path
B) Course scheduling with prerequisites
C) Maximum flow
D) Minimum spanning tree

✔ Correct Answer: B

Reason: Course scheduling is classic topological sort application: courses are nodes, prerequisites are edges. Topo sort gives valid order.

Tag: Normal

---

### Question 508
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Alien Dictionary
Difficulty: Hard

Question: How does alien dictionary problem use topological sort?
A) Sorts characters
B) Builds graph from character order, then topological sort
C) Counts frequencies
D) Uses hash table

✔ Correct Answer: B

Reason: Compare adjacent words to derive character ordering (edges), build directed graph, then topological sort gives alien alphabet order.

Tag: Normal

---

### Question 509
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Catalan Numbers
Difficulty: Hard

Question: What is the nth Catalan number's formula?
A) n!
B) 2ⁿ
C) C(2n,n)/(n+1)
D) n²

✔ Correct Answer: C

Reason: nth Catalan number = C(2n,n)/(n+1) = (2n)!/(n+1)!n!. Counts binary trees, parenthesizations, paths, etc.

Tag: Normal

---

### Question 510
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Catalan Applications
Difficulty: Hard

Question: Which problem is NOT solved by Catalan numbers?
A) Number of BSTs with n nodes
B) Valid parentheses combinations
C) Shortest path in graph
D) Number of ways to triangulate polygon

✔ Correct Answer: C

Reason: Catalan numbers count BSTs, parenthesizations, polygon triangulations, mountain ranges, but not shortest paths.

Tag: Normal

---

### Question 511
Domain: Data Structures
Topic: Code Analysis
Subtopic: Catalan Number
Difficulty: Medium

Question: [Missing question - Please review]

```python
def catalan(n):
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]
    
    return dp[n]

print(catalan(4))
```
What is the output?
A) 4
B) 14
C) 16
D) 24

✔ Correct Answer: B

Reason: 4th Catalan number is 14. Counts 14 different BSTs with 4 nodes, 14 valid parenthesizations with 4 pairs, etc.

Tag: Normal

---

### Question 512
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Spiral Traversal
Difficulty: Medium

Question: What is the time complexity of spiral matrix traversal?
A) O(1)
B) O(n)
C) O(m*n)
D) O(m²*n²)

✔ Correct Answer: C

Reason: Must visit each element exactly once in m×n matrix, giving O(m*n) time complexity with O(1) extra space.

Tag: Normal

---

### Question 513
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Rotate Matrix
Difficulty: Medium

Question: How to rotate n×n matrix 90 degrees clockwise in-place?
A) Create new matrix
B) Transpose then reverse each row
C) Reverse then transpose
D) Cannot be done in-place

✔ Correct Answer: B

Reason: Transpose matrix (swap across diagonal), then reverse each row. Achieves 90° clockwise rotation in O(n²) time, O(1) space.

Tag: Normal

---

### Question 514
Domain: Data Structures
Topic: Code Analysis
Subtopic: Matrix Rotation
Difficulty: Hard

Question: [Missing question - Please review]
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]

✔ Correct Answer: A
Reason: [Reason needs review]
Tag: Normal

---
### Question 515
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Spiral Traversal
Difficulty: Medium

Question: What is the time complexity of spiral matrix traversal?
A) O(1)
B) O(m*n) where m and n are dimensions
C) O(m+n)
D) O(log n)

✔ Correct Answer: B

Reason: Spiral traversal visits each element exactly once in an m×n matrix, resulting in O(m*n) time complexity.

Tag: Normal

---

### Question 516
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: XOR Properties
Difficulty: Medium

Question: What is the result of a XOR a?
A) a
B) 0
C) 1
D) 2a

✔ Correct Answer: B

Reason: XOR of a number with itself is always 0 because all bits cancel out. This property is useful for finding unique elements.

Tag: Past Paper

---

### Question 517
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Set Bit
Difficulty: Easy

Question: How do you set the nth bit of a number x?
A) x & (1 << n)
B) x | (1 << n)
C) x ^ (1 << n)
D) x >> n

✔ Correct Answer: B

Reason: OR operation with (1 << n) sets the nth bit to 1 without affecting other bits. AND checks bit, XOR toggles bit.

Tag: Normal

---

### Question 518
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Clear Bit
Difficulty: Medium

Question: How do you clear the nth bit of a number x?
A) x & ~(1 << n)
B) x | (1 << n)
C) x ^ (1 << n)
D) x << n

✔ Correct Answer: A

Reason: AND with complement of (1 << n) clears the nth bit to 0. The ~ operator creates a mask with all bits 1 except nth bit.

Tag: Normal

---

### Question 519
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Count Set Bits
Difficulty: Medium

Question: What is Brian Kernighan's algorithm used for?
A) Sorting
B) Counting set bits efficiently
C) Searching
D) Hashing

✔ Correct Answer: B

Reason: Brian Kernighan's algorithm counts set bits by repeatedly clearing the rightmost set bit (n & (n-1)), running in O(number of set bits).

Tag: Normal

---

### Question 520
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Power of Two
Difficulty: Easy

Question: How to check if a number n is a power of 2?
A) n % 2 == 0
B) (n & (n-1)) == 0 and n != 0
C) n / 2 == integer
D) n > 0

✔ Correct Answer: B

Reason: Powers of 2 have only one set bit. n & (n-1) clears the rightmost bit, resulting in 0 only for powers of 2 (excluding 0).

Tag: Past Paper

---

### Question 521
Domain: Data Structures
Topic: String Algorithms
Subtopic: Palindrome Check
Difficulty: Easy

Question: What is the time complexity of checking if a string is a palindrome?
A) O(1)
B) O(n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: Checking palindrome requires comparing characters from both ends moving inward, visiting each character once, resulting in O(n) time.

Tag: Normal

---

### Question 522
Domain: Data Structures
Topic: String Algorithms
Subtopic: Anagram Detection
Difficulty: Medium

Question: What is an efficient way to check if two strings are anagrams?
A) Sort both and compare
B) Count character frequencies
C) Both A and B
D) Nested loops

✔ Correct Answer: C

Reason: Both sorting (O(n log n)) and frequency counting (O(n)) work. Frequency counting is faster but sorting is simpler to implement.

Tag: Normal

---

### Question 523
Domain: Data Structures
Topic: String Algorithms
Subtopic: String Matching
Difficulty: Medium

Question: What is the time complexity of naive string matching?
A) O(n)
B) O(m+n)
C) O(m*n) where m is pattern, n is text length
D) O(log n)

✔ Correct Answer: C

Reason: Naive string matching checks pattern at each position in text, resulting in O((n-m+1)*m) ≈ O(m*n) worst case.

Tag: Normal

---

### Question 524
Domain: Data Structures
Topic: String Algorithms
Subtopic: KMP Algorithm
Difficulty: Hard

Question: What is the time complexity of KMP string matching?
A) O(m*n)
B) O(m+n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: KMP (Knuth-Morris-Pratt) uses LPS array to avoid re-checking matched characters, achieving O(m+n) time where m is pattern, n is text length.

Tag: Past Paper

---

### Question 525
Domain: Data Structures
Topic: String Algorithms
Subtopic: Rabin-Karp
Difficulty: Hard

Question: What technique does Rabin-Karp algorithm use?
A) Dynamic programming
B) Rolling hash
C) Divide and conquer
D) Greedy approach

✔ Correct Answer: B

Reason: Rabin-Karp uses rolling hash to efficiently compute hash values for all substrings, achieving O(m+n) average case for string matching.

Tag: Normal

---

### Question 526
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Trie Operations
Difficulty: Medium

Question: What is the time complexity of inserting a word of length k in a Trie?
A) O(1)
B) O(k)
C) O(n)
D) O(k²)

✔ Correct Answer: B

Reason: Inserting a word requires traversing or creating k nodes (one per character), resulting in O(k) time complexity.

Tag: Normal

---

### Question 527
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Trie Space
Difficulty: Hard

Question: What is a disadvantage of Trie data structure?
A) Slow search
B) High space complexity
C) Cannot store strings
D) Slow insertion

✔ Correct Answer: B

Reason: Tries can consume significant memory as each node may have many child pointers (26 for lowercase English), though compressed tries reduce this.

Tag: Normal

---

### Question 528
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Suffix Tree
Difficulty: Hard

Question: What is a suffix tree used for?
A) Tree traversal
B) Efficient pattern matching and substring operations
C) Sorting
D) Hashing

✔ Correct Answer: B

Reason: Suffix tree stores all suffixes of a string, enabling O(m) pattern matching and various string operations like longest repeated substring.

Tag: Normal

---

### Question 529
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Segment Tree Height
Difficulty: Hard

Question: What is the height of a segment tree for array of size n?
A) O(n)
B) O(log n)
C) O(√n)
D) O(1)

✔ Correct Answer: B

Reason: Segment tree is a balanced binary tree with height O(log n), requiring 4n space for array of size n.

Tag: Normal

---

### Question 530
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Fenwick Tree
Difficulty: Hard

Question: What is another name for Fenwick Tree?
A) AVL Tree
B) Binary Indexed Tree (BIT)
C) Red-Black Tree
D) B-Tree

✔ Correct Answer: B

Reason: Fenwick Tree is also called Binary Indexed Tree (BIT), providing efficient range sum queries and updates in O(log n).

Tag: Normal

---

### Question 531
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Topological Sort
Difficulty: Medium

Question: Topological sort is possible only for which type of graph?
A) Undirected graph
B) Directed Acyclic Graph (DAG)
C) Cyclic graph
D) Complete graph

✔ Correct Answer: B

Reason: Topological sort orders vertices such that for every edge u→v, u comes before v, only possible in DAGs (no cycles).

Tag: Past Paper

---

### Question 536
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Kahn's Algorithm
Difficulty: Hard

Question: What does Kahn's algorithm use for topological sorting?
A) DFS
B) BFS with in-degree tracking
C) Dijkstra's approach
D) Greedy method

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Kahn's algorithm uses BFS, repeatedly removing vertices with in-degree 0 and updating neighbors' in-degrees, detecting cycles if not all vertices processed.

Tag: Normal

---

### Question 533
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Strongly Connected Components
Difficulty: Hard

Question: What algorithm finds strongly connected components?
A) BFS
B) Kosaraju's or Tarjan's algorithm
C) Dijkstra's algorithm
D) Prim's algorithm

✔ Correct Answer: B

Reason: Kosaraju's algorithm uses two DFS passes, Tarjan's uses single DFS with low-link values, both finding SCCs in O(V+E) time.

Tag: Normal

---

### Question 534
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Articulation Points
Difficulty: Hard

Question: What is an articulation point in a graph?
A) Starting point
B) Vertex whose removal increases connected components
C) Ending point
D) Highest degree vertex

✔ Correct Answer: B

Reason: Articulation point (cut vertex) is a vertex whose removal disconnects the graph or increases the number of connected components.

Tag: Normal

---

### Question 535
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bridge
Difficulty: Hard

Question: What is a bridge in graph theory?
A) Physical bridge
B) Edge whose removal increases connected components
C) Shortest edge
D) Longest edge

✔ Correct Answer: B

Reason: A bridge (cut edge) is an edge whose removal disconnects the graph or increases connected components, critical for network reliability.

Tag: Normal

---

### Question 536
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Optimal Substructure
Difficulty: Medium

Question: What is optimal substructure property?
A) Best structure
B) Optimal solution contains optimal solutions to subproblems
C) Largest structure
D) Fastest structure

✔ Correct Answer: B

Reason: Optimal substructure means optimal solution can be constructed from optimal solutions of subproblems, essential for dynamic programming.

Tag: Normal

---

### Question 537
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Overlapping Subproblems
Difficulty: Medium

Question: What characterizes overlapping subproblems?
A) No repetition
B) Same subproblems solved multiple times
C) Unique subproblems
D) No subproblems

✔ Correct Answer: B

Reason: Overlapping subproblems occur when same subproblems are solved repeatedly. DP stores results (memoization) to avoid recomputation.

Tag: Normal

---

### Question 538
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Memoization vs Tabulation
Difficulty: Medium

Question: How does memoization differ from tabulation?
A) Same thing
B) Memoization is top-down, tabulation is bottom-up
C) Memoization is slower
D) Tabulation uses recursion

✔ Correct Answer: B

Reason: Memoization uses recursion with caching (top-down), tabulation uses iteration filling table (bottom-up). Both solve DP problems.

Tag: Normal

---

### Question 539
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Fibonacci DP
Difficulty: Easy

Question: What is the time complexity of Fibonacci using DP?
A) O(2ⁿ)
B) O(n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: DP computes each Fibonacci number once and stores it, reducing exponential O(2ⁿ) recursive solution to linear O(n).

Tag: Past Paper

---

### Question 540
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Common Subsequence
Difficulty: Hard

Question: What is the time complexity of LCS using DP?
A) O(n)
B) O(m*n) where m, n are string lengths
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: LCS DP solution fills an m×n table where each cell depends on three neighbors, resulting in O(m*n) time and space.

Tag: Normal

---

### Question 541
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Knapsack Problem
Difficulty: Hard

Question: What is the time complexity of 0/1 Knapsack using DP?
A) O(n)
B) O(n*W) where n is items, W is capacity
C) O(n²)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: 0/1 Knapsack DP fills a table of size n×W, where each cell is computed in O(1), resulting in O(n*W) pseudo-polynomial time.

Tag: Normal

---

### Question 542
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Coin Change
Difficulty: Medium

Question: What type of problem is coin change?
A) Greedy only
B) Dynamic programming (unbounded knapsack variant)
C) Divide and conquer
D) Backtracking

✔ Correct Answer: B

Reason: Coin change is a DP problem (unbounded knapsack variant) where each coin can be used unlimited times to make target amount.

Tag: Normal

---

### Question 543
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Edit Distance
Difficulty: Hard

Question: What does edit distance (Levenshtein distance) measure?
A) String length
B) Minimum operations to transform one string to another
C) String similarity only
D) Character count

✔ Correct Answer: B

Reason: Edit distance counts minimum insertions, deletions, and substitutions needed to transform one string into another, useful for spell checking.

Tag: Normal

---

### Question 544
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Matrix Chain Multiplication
Difficulty: Hard

Question: What does matrix chain multiplication DP optimize?
A) Matrix values
B) Order of multiplication to minimize operations
C) Matrix size
D) Storage space

✔ Correct Answer: B

Reason: Matrix chain multiplication finds optimal parenthesization order to minimize scalar multiplications, as matrix multiplication is associative but not commutative.

Tag: Normal

---

### Question 545
Domain: Data Structures
Topic: Greedy Algorithms
Subtopic: Activity Selection
Difficulty: Medium

Question: What greedy choice does activity selection make?
A) Longest activity
B) Activity finishing earliest
C) Activity starting earliest
D) Random activity

✔ Correct Answer: B

Reason: Activity selection greedily selects activity finishing earliest, leaving maximum time for remaining activities, proving optimal solution.

Tag: Normal

---

### Question 546
Domain: Data Structures
Topic: Greedy Algorithms
Subtopic: Huffman Coding
Difficulty: Hard

Question: What does Huffman coding optimize?
A) Encryption
B) Variable-length encoding minimizing average code length
C) Fixed-length encoding
D) Decoding speed

✔ Correct Answer: B

Reason: Huffman coding assigns shorter codes to frequent characters and longer codes to rare ones, minimizing average code length for compression.

Tag: Normal

---

### Question 547
Domain: Data Structures
Topic: Greedy Algorithms
Subtopic: Fractional Knapsack
Difficulty: Medium

Question: How does fractional knapsack differ from 0/1 knapsack?
A) Same problem
B) Can take fractions of items, solvable by greedy
C) Harder problem
D) No difference

✔ Correct Answer: B

Reason: Fractional knapsack allows taking fractions of items, solvable optimally by greedy (highest value/weight ratio). 0/1 requires DP.

Tag: Normal

---

### Question 548
Domain: Data Structures
Topic: Divide and Conquer
Subtopic: Merge Sort
Difficulty: Easy

Question: What is the time complexity of merge sort?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: Merge sort divides array in half (log n levels) and merges in O(n) at each level, resulting in O(n log n) in all cases.

Tag: Past Paper

---

### Question 549
Domain: Data Structures
Topic: Divide and Conquer
Subtopic: Quick Sort
Difficulty: Medium

Question: What is the worst-case time complexity of quick sort?
A) O(n log n)
B) O(n²)
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Quick sort worst case O(n²) occurs with poor pivot selection (already sorted array). Average case is O(n log n) with good pivot.

Tag: Normal

---

### Question 550
Domain: Data Structures
Topic: Divide and Conquer
Subtopic: Binary Search
Difficulty: Easy

Question: What is required for binary search to work?
A) Unsorted array
B) Sorted array
C) Linked list
D) Tree structure

✔ Correct Answer: B

Reason: Binary search requires sorted array to eliminate half the search space each iteration, achieving O(log n) time complexity.

Tag: Past Paper

---


### Question 551
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Stability
Difficulty: Medium

Question: Which sorting algorithm is stable?
A) Quick sort
B) Merge sort
C) Heap sort
D) Selection sort

✔ Correct Answer: B

Reason: Stable sorts maintain relative order of equal elements. Merge sort is stable, while quick sort, heap sort, and selection sort are typically unstable.

Tag: Normal

---

### Question 552
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: In-Place Sorting
Difficulty: Easy

Question: Which sorting algorithm is NOT in-place?
A) Bubble sort
B) Merge sort
C) Selection sort
D) Insertion sort

✔ Correct Answer: B

Reason: Merge sort requires O(n) extra space for merging. Bubble, selection, and insertion sorts are in-place using O(1) extra space.

Tag: Normal

---

### Question 553
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Counting Sort
Difficulty: Medium

Question: When is counting sort efficient?
A) Always
B) When range of input is small compared to n
C) For large ranges
D) Never

✔ Correct Answer: B

Reason: Counting sort is O(n+k) where k is range. Efficient when k is O(n), but impractical for large ranges requiring excessive space.

Tag: Normal

---

### Question 554
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Radix Sort
Difficulty: Hard

Question: What is the time complexity of radix sort?
A) O(n log n)
B) O(d*n) where d is number of digits
C) O(n²)
D) O(n)

✔ Correct Answer: B

Reason: Radix sort processes d digits, using counting sort for each digit in O(n), resulting in O(d*n) time complexity.

Tag: Normal

---

### Question 555
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Bucket Sort
Difficulty: Hard

Question: When does bucket sort perform well?
A) Random data
B) Uniformly distributed data
C) Sorted data
D) Reverse sorted data

✔ Correct Answer: B

Reason: Bucket sort performs well (O(n)) when data is uniformly distributed across buckets. Skewed distribution degrades to O(n²).

Tag: Normal

---

### Question 556
Domain: Data Structures
Topic: Hashing
Subtopic: Collision Resolution
Difficulty: Medium

Question: What is chaining in hash tables?
A) Linking tables
B) Storing colliding elements in linked list at same index
C) Rehashing
D) Linear probing

✔ Correct Answer: B

Reason: Chaining handles collisions by maintaining a linked list at each hash table index, storing all elements that hash to same location.

Tag: Normal

---

### Question 557
Domain: Data Structures
Topic: Hashing
Subtopic: Open Addressing
Difficulty: Medium

Question: What is open addressing?
A) Open hash table
B) Finding alternative location for colliding element
C) Using linked lists
D) External storage

✔ Correct Answer: B

Reason: Open addressing resolves collisions by probing for alternative locations within the hash table (linear, quadratic, double hashing).

Tag: Normal

---

### Question 558
Domain: Data Structures
Topic: Hashing
Subtopic: Linear Probing
Difficulty: Medium

Question: What is primary clustering in linear probing?
A) Good clustering
B) Consecutive occupied slots forming clusters
C) Random distribution
D) No clustering

✔ Correct Answer: B

Reason: Linear probing causes primary clustering where consecutive occupied slots form long clusters, increasing search time for nearby hash values.

Tag: Normal

---

### Question 559
Domain: Data Structures
Topic: Hashing
Subtopic: Quadratic Probing
Difficulty: Hard

Question: How does quadratic probing reduce clustering?
A) Random probing
B) Uses quadratic function for probe sequence
C) Linear probing
D) No reduction

✔ Correct Answer: B

Reason: Quadratic probing uses i² for probe sequence, reducing primary clustering but can cause secondary clustering and may not probe all slots.

Tag: Normal

---

### Question 560
Domain: Data Structures
Topic: Hashing
Subtopic: Double Hashing
Difficulty: Hard

Question: What makes double hashing effective?
A) Single hash function
B) Uses two hash functions for probe sequence
C) Triple hashing
D) No hashing

✔ Correct Answer: B

Reason: Double hashing uses second hash function for probe interval, providing better distribution and eliminating clustering if functions are independent.

Tag: Normal

---

### Question 561
Domain: Data Structures
Topic: Hashing
Subtopic: Load Factor
Difficulty: Medium

Question: What is load factor in hash tables?
A) Weight capacity
B) Ratio of elements to table size (n/m)
C) Hash function speed
D) Collision count

✔ Correct Answer: B

Reason: Load factor α = n/m (elements/size) indicates how full the table is. Higher load factor increases collisions, requiring rehashing.

Tag: Normal

---

### Question 562
Domain: Data Structures
Topic: Hashing
Subtopic: Rehashing
Difficulty: Medium

Question: When is rehashing typically performed?
A) After every insertion
B) When load factor exceeds threshold (e.g., 0.75)
C) Never
D) Randomly

✔ Correct Answer: B

Reason: Rehashing creates larger table and reinserts all elements when load factor exceeds threshold, maintaining O(1) average operations.

Tag: Normal

---

### Question 563
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Bloom Filter
Difficulty: Hard

Question: What does a Bloom filter guarantee?
A) No false positives or negatives
B) No false negatives, but possible false positives
C) No false positives, but possible false negatives
D) Both false positives and negatives

✔ Correct Answer: B

Reason: Bloom filter never has false negatives (if says no, definitely not present) but can have false positives (if says yes, might not be present).

Tag: Normal

---

### Question 564
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Skip List
Difficulty: Hard

Question: What is the average time complexity of search in skip list?
A) O(n)
B) O(log n)
C) O(1)
D) O(n log n)

✔ Correct Answer: B

Reason: Skip list uses multiple levels of linked lists with probabilistic balancing, achieving O(log n) average search, insert, delete operations.

Tag: Normal

---

### Question 565
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Disjoint Set
Difficulty: Hard

Question: What is the time complexity of union-find with path compression and union by rank?
A) O(n)
B) O(α(n)) - inverse Ackermann, nearly constant
C) O(log n)
D) O(1)

✔ Correct Answer: B

Reason: With both optimizations, union-find operations are O(α(n)) where α is inverse Ackermann function, effectively constant for practical values.

Tag: Normal

---

### Question 566
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Spanning Tree
Difficulty: Medium

Question: What is a minimum spanning tree?
A) Smallest tree
B) Tree connecting all vertices with minimum total edge weight
C) Shortest path tree
D) Balanced tree

✔ Correct Answer: B

Reason: MST is a subset of edges forming a tree that connects all vertices with minimum total edge weight, used in network design.

Tag: Past Paper

---

### Question 567
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Prim's Algorithm
Difficulty: Medium

Question: What data structure makes Prim's algorithm efficient?
A) Stack
B) Min heap (priority queue)
C) Queue
D) Array only

✔ Correct Answer: B

Reason: Prim's algorithm uses min heap to efficiently select minimum weight edge, achieving O(E log V) with binary heap or O(E + V log V) with Fibonacci heap.

Tag: Normal

---

### Question 568
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Kruskal's Algorithm
Difficulty: Hard

Question: What data structure does Kruskal's algorithm use?
A) Stack
B) Disjoint set (union-find)
C) Queue
D) Heap only

✔ Correct Answer: B

Reason: Kruskal's sorts edges and uses union-find to detect cycles, adding edges if they don't create cycle, achieving O(E log E) time.

Tag: Normal

---

### Question 569
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Shortest Path
Difficulty: Easy

Question: Which algorithm finds shortest path from single source to all vertices?
A) BFS (unweighted)
B) Dijkstra's algorithm (non-negative weights)
C) Both A and B
D) DFS

✔ Correct Answer: C

Reason: BFS finds shortest path in unweighted graphs. Dijkstra's handles non-negative weighted graphs. Both solve single-source shortest path.

Tag: Normal

---

### Question 570
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bellman-Ford
Difficulty: Hard

Question: What advantage does Bellman-Ford have over Dijkstra's?
A) Faster
B) Handles negative edge weights
C) Simpler
D) Uses less space

✔ Correct Answer: B

Reason: Bellman-Ford handles negative edge weights and detects negative cycles, though slower O(VE) compared to Dijkstra's O(E log V).

Tag: Normal

---


### Question 571
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Floyd-Warshall
Difficulty: Hard

Question: What does Floyd-Warshall algorithm find?
A) Single source shortest path
B) All-pairs shortest paths
C) MST
D) Topological sort

✔ Correct Answer: B

Reason: Floyd-Warshall finds shortest paths between all pairs of vertices in O(V³) time, using dynamic programming approach.

Tag: Normal

---

### Question 572
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: A* Algorithm
Difficulty: Hard

Question: What does A* algorithm use for pathfinding?
A) BFS only
B) Heuristic function with actual cost
C) DFS only
D) Random search

✔ Correct Answer: B

Reason: A* uses f(n) = g(n) + h(n) where g is actual cost and h is heuristic estimate, finding optimal path efficiently with admissible heuristic.

Tag: Normal

---

### Question 573
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Cycle Detection
Difficulty: Medium

Question: How to detect cycle in undirected graph using DFS?
A) Check all edges
B) If back edge to visited non-parent node found
C) Count vertices
D) Random check

✔ Correct Answer: B

Reason: In undirected graph DFS, cycle exists if we encounter a visited vertex that's not the parent of current vertex (back edge).

Tag: Normal

---

### Question 574
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Directed Graph Cycle
Difficulty: Hard

Question: How to detect cycle in directed graph?
A) BFS only
B) DFS with recursion stack tracking
C) Count edges
D) Topological sort only

✔ Correct Answer: B

Reason: Track vertices in current recursion stack during DFS. If we reach a vertex already in stack, cycle exists (back edge in directed graph).

Tag: Normal

---

### Question 575
Domain: Data Structures
Topic: Backtracking
Subtopic: N-Queens
Difficulty: Hard

Question: What is the time complexity of N-Queens problem?
A) O(n²)
B) O(n!)
C) O(2ⁿ)
D) O(n log n)

✔ Correct Answer: B

Reason: N-Queens explores permutations of queen placements with pruning, resulting in O(n!) time complexity in worst case.

Tag: Normal

---

### Question 576
Domain: Data Structures
Topic: Backtracking
Subtopic: Sudoku Solver
Difficulty: Hard

Question: What technique does backtracking use?
A) Greedy choice
B) Try possibilities, backtrack on failure
C) Dynamic programming
D) Divide and conquer

✔ Correct Answer: B

Reason: Backtracking tries possibilities recursively, backtracking when constraints are violated, exploring solution space systematically.

Tag: Normal

---

### Question 577
Domain: Data Structures
Topic: Backtracking
Subtopic: Subset Sum
Difficulty: Medium

Question: What is the time complexity of subset sum using backtracking?
A) O(n)
B) O(2ⁿ)
C) O(n²)
D) O(n log n)

✔ Correct Answer: B

Reason: Backtracking explores all subsets (include/exclude each element), resulting in O(2ⁿ) time. DP can solve in pseudo-polynomial time.

Tag: Normal

---

### Question 578
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Sliding Window
Difficulty: Medium

Question: When is sliding window technique applicable?
A) Random problems
B) Contiguous subarray/substring problems
C) Graph problems
D) Tree problems

✔ Correct Answer: B

Reason: Sliding window efficiently solves problems involving contiguous subarrays/substrings by maintaining a window and sliding it, reducing time complexity.

Tag: Normal

---

### Question 579
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Two Pointers
Difficulty: Easy

Question: What is the two-pointer technique?
A) Using two variables
B) Two pointers moving through data structure
C) Two arrays
D) Two loops

✔ Correct Answer: B

Reason: Two-pointer technique uses two pointers moving through array/list (same/opposite directions) to solve problems efficiently, often reducing O(n²) to O(n).

Tag: Normal

---

### Question 580
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Fast and Slow Pointers
Difficulty: Medium

Question: What is Floyd's cycle detection algorithm also called?
A) Rabbit algorithm
B) Tortoise and hare algorithm
C) Fast algorithm
D) Slow algorithm

✔ Correct Answer: B

Reason: Floyd's algorithm uses fast (2x speed) and slow (1x speed) pointers. If cycle exists, fast pointer eventually meets slow pointer.

Tag: Normal

---

### Question 581
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Lowest Common Ancestor
Difficulty: Hard

Question: What is the time complexity of LCA in binary tree?
A) O(1)
B) O(h) where h is height
C) O(n)
D) O(log n) always

✔ Correct Answer: B

Reason: Finding LCA requires traversing from root to nodes, taking O(h) time where h is tree height (O(log n) balanced, O(n) skewed).

Tag: Normal

---

### Question 582
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Diameter of Tree
Difficulty: Hard

Question: What is the diameter of a tree?
A) Tree width
B) Longest path between any two nodes
C) Tree height
D) Number of nodes

✔ Correct Answer: B

Reason: Diameter is the length of longest path between any two nodes in tree, found using DFS/BFS in O(n) time.

Tag: Normal

---

### Question 583
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Serialize/Deserialize
Difficulty: Hard

Question: What is tree serialization?
A) Making tree serial
B) Converting tree to string/array representation
C) Sorting tree
D) Deleting tree

✔ Correct Answer: B

Reason: Serialization converts tree to linear format (string/array) for storage/transmission, deserializing reconstructs tree from representation.

Tag: Normal

---

### Question 584
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Kadane's Algorithm
Difficulty: Medium

Question: What problem does Kadane's algorithm solve?
A) Sorting
B) Maximum subarray sum
C) Searching
D) Merging

✔ Correct Answer: B

Reason: Kadane's algorithm finds maximum sum of contiguous subarray in O(n) time using dynamic programming approach.

Tag: Past Paper

---

### Question 585
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Dutch National Flag
Difficulty: Hard

Question: What does Dutch National Flag algorithm do?
A) Sort completely
B) Partition array into three parts
C) Binary partition
D) Find median

✔ Correct Answer: B

Reason: Dutch National Flag algorithm partitions array into three parts (low, mid, high values) in single pass O(n), useful for 3-way partitioning.

Tag: Normal

---

### Question 586
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Moore's Voting
Difficulty: Hard

Question: What does Boyer-Moore majority vote algorithm find?
A) All elements
B) Element appearing more than n/2 times
C) Minimum element
D) Maximum element

✔ Correct Answer: B

Reason: Boyer-Moore voting algorithm finds majority element (>n/2 occurrences) in O(n) time and O(1) space using candidate and count.

Tag: Normal

---

### Question 587
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Palindromic Substring
Difficulty: Hard

Question: What is the time complexity of Manacher's algorithm?
A) O(n²)
B) O(n)
C) O(n log n)
D) O(n³)

✔ Correct Answer: B

Reason: Manacher's algorithm finds longest palindromic substring in O(n) time using previously computed palindrome information.

Tag: Normal

---

### Question 588
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Reservoir Sampling
Difficulty: Hard

Question: What is reservoir sampling used for?
A) Water sampling
B) Random sampling from stream of unknown size
C) Sorting
D) Searching

✔ Correct Answer: B

Reason: Reservoir sampling selects k random items from stream of unknown/large size in single pass with uniform probability.

Tag: Normal

---

### Question 589
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Fisher-Yates Shuffle
Difficulty: Medium

Question: What does Fisher-Yates algorithm do?
A) Sort array
B) Randomly shuffle array with uniform distribution
C) Search array
D) Reverse array

✔ Correct Answer: B

Reason: Fisher-Yates shuffle randomly permutes array in O(n) time, ensuring each permutation has equal probability.

Tag: Normal

---

### Question 590
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Morris Traversal
Difficulty: Hard

Question: What is special about Morris traversal?
A) Uses recursion
B) Inorder traversal in O(1) space
C) Uses stack
D) Requires extra tree

✔ Correct Answer: B

Reason: Morris traversal performs inorder traversal without recursion or stack using threaded binary tree concept, achieving O(1) space.

Tag: Normal

---

### Question 591
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: LRU Cache
Difficulty: Hard

Question: What data structures implement LRU cache efficiently?
A) Array only
B) Hash map + doubly linked list
C) Stack
D) Queue only

✔ Correct Answer: B

Reason: Hash map provides O(1) lookup, doubly linked list maintains access order for O(1) eviction, together implementing O(1) LRU cache operations.

Tag: Normal

---

### Question 592
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: LFU Cache
Difficulty: Hard

Question: What does LFU cache track?
A) Recent access
B) Access frequency
C) Item size
D) Creation time

✔ Correct Answer: B

Reason: LFU (Least Frequently Used) cache tracks access frequency, evicting least frequently used items, requiring frequency counters and ordering.

Tag: Normal

---

### Question 593
Domain: Data Structures
Topic: String Algorithms
Subtopic: Z-Algorithm
Difficulty: Hard

Question: What does Z-algorithm compute?
A) String length
B) Length of longest substring starting from each position matching prefix
C) Character count
D) Hash value

✔ Correct Answer: B

Reason: Z-algorithm computes Z-array where Z[i] is length of longest substring starting at i matching prefix, useful for pattern matching in O(n).

Tag: Normal

---

### Question 594
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Monotonic Stack
Difficulty: Hard

Question: When is monotonic stack useful?
A) Random problems
B) Finding next greater/smaller element
C) Sorting
D) Searching

✔ Correct Answer: B

Reason: Monotonic stack maintains elements in increasing/decreasing order, efficiently solving next greater/smaller element problems in O(n).

Tag: Normal

---

### Question 595
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Monotonic Queue
Difficulty: Hard

Question: What problem does monotonic queue solve efficiently?
A) Sorting
B) Sliding window maximum/minimum
C) Searching
D) Hashing

✔ Correct Answer: B

Reason: Monotonic deque maintains elements in order within sliding window, finding max/min in O(1) per window, total O(n) for all windows.

Tag: Normal

---

### Question 596
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Lifting
Difficulty: Hard

Question: What is binary lifting used for?
A) Lifting trees
B) Finding kth ancestor in O(log n)
C) Tree traversal
D) Tree sorting

✔ Correct Answer: B

Reason: Binary lifting preprocesses tree to find kth ancestor in O(log n) using sparse table of 2^i ancestors, with O(n log n) preprocessing.

Tag: Normal

---

### Question 597
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Heavy-Light Decomposition
Difficulty: Hard

Question: What does heavy-light decomposition enable?
A) Tree compression
B) Path queries in O(log² n)
C) Tree sorting
D) Tree deletion

✔ Correct Answer: B

Reason: Heavy-light decomposition partitions tree into heavy and light paths, enabling path queries and updates in O(log² n) with segment trees.

Tag: Normal

---

### Question 598
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Centroid Decomposition
Difficulty: Hard

Question: What is centroid decomposition used for?
A) Finding center
B) Divide and conquer on trees
C) Tree balancing
D) Tree traversal

✔ Correct Answer: B

Reason: Centroid decomposition recursively decomposes tree by removing centroids, enabling efficient divide-and-conquer solutions for tree problems.

Tag: Normal

---

### Question 599
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Ternary Search
Difficulty: Hard

Question: When is ternary search applicable?
A) Any function
B) Unimodal functions (single peak/valley)
C) Multimodal functions
D) Random functions

✔ Correct Answer: B

Reason: Ternary search finds maximum/minimum of unimodal function by dividing into three parts, converging in O(log n) iterations.

Tag: Normal

---

### Question 600
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Meet in the Middle
Difficulty: Hard

Question: What does meet in the middle technique do?
A) Find middle element
B) Split problem into two halves, solve separately and combine
C) Sort middle elements
D) Delete middle

✔ Correct Answer: B

Reason: Meet in the middle splits search space into two halves, solving each in O(2^(n/2)) and combining, reducing O(2^n) to O(2^(n/2)).

Tag: Normal

---

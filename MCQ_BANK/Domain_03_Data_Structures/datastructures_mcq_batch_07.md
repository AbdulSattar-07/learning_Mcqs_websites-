# Data Structures - MCQ Batch 07
## Questions 601-700

---

### Question 601
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Prefix Sum
Difficulty: Easy

Question: What is the time complexity of range sum query using prefix sum?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: After O(n) preprocessing to build prefix sum array, each range sum query is answered in O(1) using prefixSum[r] - prefixSum[l-1].

Tag: Normal

---

### Question 602
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Difference Array
Difficulty: Medium

Question: What is difference array used for?
A) Finding differences
B) Efficient range updates
C) Sorting
D) Searching

✔ Correct Answer: B

Reason: Difference array enables O(1) range updates and O(n) final array construction, useful when multiple range updates are needed.

Tag: Normal

---

### Question 603
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Euler Tour
Difficulty: Hard

Question: What does Euler tour of tree provide?
A) Tree traversal
B) Flattening tree to array for range queries
C) Tree sorting
D) Tree deletion

✔ Correct Answer: B

Reason: Euler tour flattens tree into array where subtree becomes contiguous range, enabling segment tree queries on tree paths/subtrees.

Tag: Normal

---

### Question 604
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bipartite Graph
Difficulty: Medium

Question: How to check if a graph is bipartite?
A) Count vertices
B) 2-color using BFS/DFS
C) Check edges
D) Random check

✔ Correct Answer: B

Reason: Try to 2-color graph using BFS/DFS. If successful (no adjacent vertices have same color), graph is bipartite.

Tag: Normal

---

### Question 605
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Maximum Bipartite Matching
Difficulty: Hard

Question: What algorithm solves maximum bipartite matching?
A) BFS only
B) Hungarian algorithm or Ford-Fulkerson
C) DFS only
D) Dijkstra's

✔ Correct Answer: B

Reason: Maximum bipartite matching can be solved using Hungarian algorithm O(n³) or reducing to max flow problem with Ford-Fulkerson.

Tag: Normal

---

### Question 606
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Network Flow
Difficulty: Hard

Question: What does Ford-Fulkerson algorithm find?
A) Shortest path
B) Maximum flow in network
C) MST
D) Topological order

✔ Correct Answer: B

Reason: Ford-Fulkerson finds maximum flow from source to sink in flow network by repeatedly finding augmenting paths.

Tag: Normal

---

### Question 607
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Min Cut
Difficulty: Hard

Question: What is the relationship between max flow and min cut?
A) Unrelated
B) Max flow value equals min cut capacity
C) Max flow > min cut
D) Max flow < min cut

✔ Correct Answer: B

Reason: Max-flow min-cut theorem states maximum flow value equals minimum cut capacity, fundamental result in network flow theory.

Tag: Normal

---

### Question 608
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Binary Search Variants
Difficulty: Medium

Question: What is binary search on answer?
A) Searching for answer
B) Binary search on solution space to find optimal value
C) Regular binary search
D) Random search

✔ Correct Answer: B

Reason: Binary search on answer applies binary search to solution space when answer is monotonic, finding optimal value efficiently.

Tag: Normal

---

### Question 609
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Matrix Exponentiation
Difficulty: Hard

Question: What is the time complexity of computing A^n using matrix exponentiation?
A) O(n)
B) O(log n) matrix multiplications
C) O(n²)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: Matrix exponentiation uses binary exponentiation, computing A^n in O(log n) matrix multiplications, each taking O(d³) for d×d matrix.

Tag: Normal

---

### Question 610
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Fibonacci Fast
Difficulty: Hard

Question: How can Fibonacci be computed in O(log n)?
A) Recursion
B) Matrix exponentiation
C) Iteration only
D) Impossible

✔ Correct Answer: B

Reason: Using matrix [[1,1],[1,0]]^n and matrix exponentiation, Fibonacci can be computed in O(log n) time.

Tag: Normal

---

### Question 611
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Common Prefix
Difficulty: Easy

Question: What is the time complexity of finding LCP of n strings?
A) O(1)
B) O(n*m) where m is min string length
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Finding longest common prefix requires comparing characters across all n strings up to minimum length m, resulting in O(n*m).

Tag: Normal

---

### Question 612
Domain: Data Structures
Topic: String Algorithms
Subtopic: String Rotation
Difficulty: Easy

Question: How to check if string s2 is rotation of s1?
A) Sort both
B) Check if s2 is substring of s1+s1
C) Compare lengths only
D) Reverse and compare

✔ Correct Answer: B

Reason: If s2 is rotation of s1, then s2 will be substring of s1+s1. For example, "waterbottle" is in "erbottlewat" + "erbottlewat".

Tag: Normal

---

### Question 613
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Trapping Rain Water
Difficulty: Hard

Question: What approach solves trapping rain water efficiently?
A) Brute force only
B) Two pointers or precomputed max heights
C) Sorting
D) Hashing

✔ Correct Answer: B

Reason: Two-pointer approach or precomputing left/right max heights solves in O(n) time, calculating water trapped based on min of max heights.

Tag: Normal

---

### Question 614
Domain: Data Structures
Topic: Stack Applications
Subtopic: Stock Span
Difficulty: Medium

Question: What does stock span problem find?
A) Stock prices
B) Number of consecutive days with price ≤ current
C) Maximum price
D) Minimum price

✔ Correct Answer: B

Reason: Stock span finds consecutive previous days with price ≤ current day, efficiently solved using monotonic stack in O(n).

Tag: Normal

---

### Question 615
Domain: Data Structures
Topic: Stack Applications
Subtopic: Largest Rectangle
Difficulty: Hard

Question: How to find largest rectangle in histogram?
A) Brute force only
B) Stack-based approach in O(n)
C) Sorting
D) Binary search

✔ Correct Answer: B

Reason: Using stack to track increasing heights and calculating area when smaller height encountered solves in O(n) time.

Tag: Normal

---

### Question 616
Domain: Data Structures
Topic: Queue Applications
Subtopic: Sliding Window Maximum
Difficulty: Hard

Question: What data structure efficiently finds sliding window maximum?
A) Simple queue
B) Monotonic deque
C) Stack
D) Array

✔ Correct Answer: B

Reason: Monotonic deque maintains elements in decreasing order, providing O(1) max access and O(n) total time for all windows.

Tag: Normal

---

### Question 617
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Vertical Order Traversal
Difficulty: Medium

Question: What additional information is needed for vertical order traversal?
A) Only level
B) Horizontal distance from root
C) Node value
D) Parent pointer

✔ Correct Answer: B

Reason: Vertical order traversal groups nodes by horizontal distance from root, using map to store nodes at each distance level.

Tag: Normal

---

### Question 618
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Boundary Traversal
Difficulty: Medium

Question: What does boundary traversal of binary tree include?
A) All nodes
B) Left boundary, leaves, right boundary (excluding root duplicates)
C) Root only
D) Leaves only

✔ Correct Answer: B

Reason: Boundary traversal prints left boundary (top-down), all leaves (left-right), and right boundary (bottom-up), forming tree perimeter.

Tag: Normal

---

### Question 619
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Diagonal Traversal
Difficulty: Medium

Question: What are diagonals in binary tree?
A) Physical diagonals
B) Nodes where right child is same diagonal, left child is next
C) All nodes at same level
D) Random grouping

✔ Correct Answer: B

Reason: In diagonal traversal, right children stay on same diagonal while left children move to next diagonal, grouping nodes diagonally.

Tag: Normal

---

### Question 620
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Eulerian Path
Difficulty: Hard

Question: When does an Eulerian path exist in undirected graph?
A) Always
B) Exactly 0 or 2 vertices with odd degree
C) All even degrees
D) Never

✔ Correct Answer: B

Reason: Eulerian path (visiting each edge exactly once) exists if graph has exactly 0 (Eulerian circuit) or 2 vertices with odd degree.

Tag: Normal

---


### Question 621
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Hamiltonian Path
Difficulty: Hard

Question: What is the difference between Eulerian and Hamiltonian path?
A) Same thing
B) Eulerian visits each edge once, Hamiltonian visits each vertex once
C) Eulerian is faster
D) No difference

✔ Correct Answer: B

Reason: Eulerian path visits each edge exactly once, Hamiltonian path visits each vertex exactly once. Hamiltonian is NP-complete.

Tag: Normal

---

### Question 622
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Graph Coloring
Difficulty: Hard

Question: What is chromatic number of a graph?
A) Number of colors
B) Minimum colors needed to color vertices with no adjacent same color
C) Maximum colors
D) Average colors

✔ Correct Answer: B

Reason: Chromatic number is minimum colors needed for proper vertex coloring where no adjacent vertices share color. Finding it is NP-complete.

Tag: Normal

---

### Question 623
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bipartite Matching
Difficulty: Hard

Question: What is the chromatic number of a bipartite graph?
A) 1
B) 2
C) 3
D) Depends on size

✔ Correct Answer: B

Reason: Bipartite graphs can be 2-colored by definition (two independent sets), so chromatic number is always 2 (or 1 if no edges).

Tag: Normal

---

### Question 624
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Sparse Table
Difficulty: Hard

Question: What queries does sparse table answer efficiently?
A) Update queries
B) Range minimum/maximum queries (immutable)
C) Insert queries
D) Delete queries

✔ Correct Answer: B

Reason: Sparse table answers range min/max queries in O(1) after O(n log n) preprocessing, but doesn't support updates (immutable data).

Tag: Normal

---

### Question 625
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Square Root Decomposition
Difficulty: Hard

Question: What is the time complexity of range query using sqrt decomposition?
A) O(1)
B) O(√n)
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Dividing array into √n blocks, range queries process at most 2 partial blocks and √n complete blocks, resulting in O(√n).

Tag: Normal

---

### Question 626
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Mo's Algorithm
Difficulty: Hard

Question: What type of queries does Mo's algorithm handle?
A) Online queries
B) Offline range queries
C) Update queries
D) Insert queries

✔ Correct Answer: B

Reason: Mo's algorithm efficiently answers offline range queries by reordering them and maintaining answer while sliding window, achieving O(n√n).

Tag: Normal

---

### Question 627
Domain: Data Structures
Topic: String Algorithms
Subtopic: Suffix Array
Difficulty: Hard

Question: What is a suffix array?
A) Array of suffixes
B) Sorted array of suffix starting positions
C) Array of prefixes
D) Random array

✔ Correct Answer: B

Reason: Suffix array stores starting positions of all suffixes in sorted order, enabling efficient pattern matching and string operations.

Tag: Normal

---

### Question 628
Domain: Data Structures
Topic: String Algorithms
Subtopic: LCP Array
Difficulty: Hard

Question: What does LCP array store?
A) Longest common prefix
B) Length of longest common prefix between consecutive suffixes in suffix array
C) All prefixes
D) Character positions

✔ Correct Answer: B

Reason: LCP array stores longest common prefix length between consecutive suffixes in sorted suffix array, useful for various string problems.

Tag: Normal

---

### Question 629
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Convex Hull
Difficulty: Hard

Question: What does Graham scan algorithm find?
A) Graph scan
B) Convex hull of points in O(n log n)
C) Shortest path
D) Maximum distance

✔ Correct Answer: B

Reason: Graham scan finds convex hull by sorting points by polar angle and using stack to maintain hull vertices in O(n log n).

Tag: Normal

---

### Question 630
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Line Sweep
Difficulty: Hard

Question: What is line sweep algorithm technique?
A) Drawing lines
B) Processing events in sorted order (sweep line across plane)
C) Random processing
D) Parallel processing

✔ Correct Answer: B

Reason: Line sweep processes geometric events in sorted order as imaginary line sweeps across plane, solving intersection and interval problems efficiently.

Tag: Normal

---

### Question 631
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Cartesian Tree
Difficulty: Hard

Question: What property does Cartesian tree satisfy?
A) BST property only
B) Heap property for values, BST property for indices
C) AVL property
D) No special property

✔ Correct Answer: B

Reason: Cartesian tree satisfies min/max heap property for values and BST property for array indices, useful for range minimum queries.

Tag: Normal

---

### Question 632
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Treap
Difficulty: Hard

Question: What does Treap combine?
A) Tree and heap
B) BST (by key) and heap (by random priority)
C) Tree and map
D) Heap and array

✔ Correct Answer: B

Reason: Treap combines BST property for keys and heap property for random priorities, achieving expected O(log n) operations through randomization.

Tag: Normal

---

### Question 633
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Splay Tree
Difficulty: Hard

Question: What is special about splay trees?
A) Always balanced
B) Self-adjusting, recently accessed nodes move to root
C) Fixed structure
D) No rotations

✔ Correct Answer: B

Reason: Splay trees move accessed nodes to root via rotations (splaying), achieving O(log n) amortized time and good cache performance.

Tag: Normal

---

### Question 634
Domain: Data Structures
Topic: Advanced Trees
Subtopic: B-Tree Order
Difficulty: Hard

Question: In a B-tree of order m, what is the maximum number of children per node?
A) m-1
B) m
C) 2m
D) m+1

✔ Correct Answer: B

Reason: B-tree of order m has maximum m children per node and m-1 keys. Minimum children is ⌈m/2⌉ (except root).

Tag: Normal

---

### Question 635
Domain: Data Structures
Topic: Advanced Trees
Subtopic: B+ Tree
Difficulty: Hard

Question: How does B+ tree differ from B-tree?
A) Same structure
B) All data in leaf nodes, internal nodes only for routing
C) B+ is smaller
D) B+ is faster always

✔ Correct Answer: B

Reason: B+ tree stores all data in leaf nodes (linked for range queries), internal nodes only store keys for routing, optimizing range scans.

Tag: Normal

---

### Question 636
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Interval Scheduling
Difficulty: Medium

Question: What greedy choice solves interval scheduling?
A) Longest interval
B) Earliest finish time
C) Earliest start time
D) Random selection

✔ Correct Answer: B

Reason: Selecting interval with earliest finish time greedily maximizes remaining time for other intervals, proving optimal for interval scheduling.

Tag: Normal

---

### Question 637
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Interval Partitioning
Difficulty: Hard

Question: What does interval partitioning minimize?
A) Interval count
B) Number of resources needed for overlapping intervals
C) Interval length
D) Start times

✔ Correct Answer: B

Reason: Interval partitioning finds minimum resources (classrooms, processors) needed when intervals overlap, equal to maximum overlap depth.

Tag: Normal

---

### Question 638
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Path Sum
Difficulty: Medium

Question: How to find all root-to-leaf paths with given sum?
A) BFS only
B) DFS with backtracking
C) Level order
D) Inorder traversal

✔ Correct Answer: B

Reason: DFS with backtracking explores all root-to-leaf paths, tracking current sum and storing paths that match target sum.

Tag: Normal

---

### Question 639
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Maximum Path Sum
Difficulty: Hard

Question: What is the approach for maximum path sum in binary tree?
A) Simple traversal
B) Recursively compute max path through each node
C) Level order
D) Sorting

✔ Correct Answer: B

Reason: For each node, compute maximum path sum passing through it (left + node + right), tracking global maximum across all nodes.

Tag: Normal

---

### Question 640
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Traveling Salesman
Difficulty: Hard

Question: What is the time complexity of TSP using dynamic programming?
A) O(n²)
B) O(n² * 2ⁿ)
C) O(n!)
D) O(n log n)

✔ Correct Answer: B

Reason: TSP using DP with bitmask (Held-Karp algorithm) has O(n² * 2ⁿ) time complexity, better than brute force O(n!) but still exponential.

Tag: Normal

---

### Question 641
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Bitmasking DP
Difficulty: Hard

Question: When is bitmasking useful in DP?
A) Large state spaces
B) Small state spaces representable as bits
C) Continuous values
D) Never

✔ Correct Answer: B

Reason: Bitmasking represents state as bits (subsets, visited nodes) when state space is small (≤20 elements), enabling compact DP solutions.

Tag: Normal

---

### Question 642
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Digit DP
Difficulty: Hard

Question: What problems does digit DP solve?
A) Arithmetic
B) Counting numbers with digit constraints
C) Sorting digits
D) Finding digits

✔ Correct Answer: B

Reason: Digit DP counts numbers in range satisfying digit constraints (sum, pattern) by processing digits left-to-right with state tracking.

Tag: Normal

---

### Question 643
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Partition Problem
Difficulty: Hard

Question: What does partition problem ask?
A) Partition array randomly
B) Can array be partitioned into two equal sum subsets
C) Find maximum partition
D) Count partitions

✔ Correct Answer: B

Reason: Partition problem asks if array can be divided into two subsets with equal sum, solvable using subset sum DP in O(n*sum).

Tag: Normal

---

### Question 644
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Palindrome Partitioning
Difficulty: Hard

Question: What does palindrome partitioning find?
A) All palindromes
B) Minimum cuts to partition string into palindromes
C) Longest palindrome
D) Palindrome count

✔ Correct Answer: B

Reason: Palindrome partitioning finds minimum cuts needed to partition string such that each substring is palindrome, using DP in O(n²).

Tag: Normal

---

### Question 645
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Egg Dropping
Difficulty: Hard

Question: What does egg dropping problem optimize?
A) Egg count
B) Minimum trials to find critical floor in worst case
C) Floor count
D) Breaking eggs

✔ Correct Answer: B

Reason: Egg dropping finds minimum trials needed to determine critical floor in worst case, using DP with states (eggs, floors).

Tag: Normal

---


### Question 646
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Catalan Numbers
Difficulty: Hard

Question: What problems involve Catalan numbers?
A) Prime numbers
B) Number of BSTs, valid parentheses, paths in grid
C) Fibonacci variants
D) Sorting problems

✔ Correct Answer: B

Reason: Catalan numbers count BSTs with n nodes, valid parentheses combinations, paths in grid not crossing diagonal, and many combinatorial structures.

Tag: Normal

---

### Question 647
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: BST from Traversals
Difficulty: Hard

Question: Which traversals uniquely determine a binary tree?
A) Inorder only
B) Inorder + (Preorder or Postorder)
C) Preorder only
D) Any single traversal

✔ Correct Answer: B

Reason: Inorder with preorder or postorder uniquely determines binary tree. Inorder alone or preorder alone is insufficient.

Tag: Normal

---

### Question 648
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Majority Element
Difficulty: Medium

Question: What is a majority element?
A) Largest element
B) Element appearing more than n/2 times
C) Most frequent element
D) Median element

✔ Correct Answer: B

Reason: Majority element appears more than ⌊n/2⌋ times. Boyer-Moore voting algorithm finds it in O(n) time and O(1) space.

Tag: Normal

---

### Question 649
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Missing Number
Difficulty: Easy

Question: How to find missing number in array [0,n] with one missing?
A) Sort and search
B) Sum formula or XOR
C) Linear search
D) Binary search

✔ Correct Answer: B

Reason: Expected sum - actual sum gives missing number. Alternatively, XOR all numbers and array elements cancels out all except missing.

Tag: Normal

---

### Question 650
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Duplicate Detection
Difficulty: Easy

Question: How to find duplicate in array of n+1 elements from [1,n]?
A) Sort
B) Floyd's cycle detection or sum/XOR
C) Hash map only
D) Linear search

✔ Correct Answer: B

Reason: Floyd's cycle detection treats array as linked list (value as next index) finding cycle in O(n) time, O(1) space. Sum/XOR also work.

Tag: Normal

---

### Question 651
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Rotate Matrix
Difficulty: Medium

Question: How to rotate n×n matrix 90° clockwise in-place?
A) Create new matrix
B) Transpose then reverse each row
C) Reverse then transpose
D) Cannot do in-place

✔ Correct Answer: B

Reason: Transpose matrix (swap [i][j] with [j][i]) then reverse each row achieves 90° clockwise rotation in-place in O(n²).

Tag: Normal

---

### Question 652
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Set Matrix Zeroes
Difficulty: Medium

Question: How to set entire row/column to zero if element is zero, using O(1) space?
A) Impossible
B) Use first row and column as markers
C) Create new matrix
D) Use hash map

✔ Correct Answer: B

Reason: Use first row and column to mark which rows/columns to zero, with separate variables for first row/column themselves.

Tag: Normal

---

### Question 653
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Reverse in Groups
Difficulty: Hard

Question: What is the time complexity of reversing linked list in groups of k?
A) O(n²)
B) O(n)
C) O(n*k)
D) O(k)

✔ Correct Answer: B

Reason: Each node is visited constant times during reversal process, resulting in O(n) time complexity regardless of group size k.

Tag: Normal

---

### Question 654
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Palindrome Check
Difficulty: Medium

Question: How to check if linked list is palindrome in O(n) time, O(1) space?
A) Use array
B) Find middle, reverse second half, compare
C) Use stack
D) Impossible

✔ Correct Answer: B

Reason: Find middle using slow/fast pointers, reverse second half, compare with first half, achieving O(n) time and O(1) space.

Tag: Normal

---

### Question 655
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Merge K Sorted Lists
Difficulty: Hard

Question: What is the time complexity of merging k sorted lists with n total elements?
A) O(n)
B) O(n log k)
C) O(n*k)
D) O(n²)

✔ Correct Answer: B

Reason: Using min heap of size k to track smallest elements from each list, each of n elements is inserted/extracted in O(log k).

Tag: Normal

---

### Question 656
Domain: Data Structures
Topic: Stack Applications
Subtopic: Min Stack
Difficulty: Medium

Question: How to implement stack with O(1) getMin operation?
A) Sort stack
B) Maintain auxiliary stack tracking minimums
C) Linear search
D) Impossible

✔ Correct Answer: B

Reason: Maintain auxiliary stack where top always contains minimum of elements below in main stack, both push/pop/getMin in O(1).

Tag: Normal

---

### Question 657
Domain: Data Structures
Topic: Queue Applications
Subtopic: Queue using Stacks
Difficulty: Medium

Question: How to implement queue using two stacks?
A) One stack only
B) One for enqueue, one for dequeue with transfer
C) Three stacks
D) Impossible

✔ Correct Answer: B

Reason: Use one stack for enqueue, transfer to second stack for dequeue when needed, achieving amortized O(1) for both operations.

Tag: Normal

---

### Question 658
Domain: Data Structures
Topic: Stack Applications
Subtopic: Stack using Queues
Difficulty: Medium

Question: How to implement stack using two queues?
A) One queue only
B) Transfer elements between queues to maintain LIFO
C) Three queues
D) Impossible

✔ Correct Answer: B

Reason: Transfer n-1 elements to second queue on pop, making last element accessible, or use single queue with rotation, achieving O(n) pop.

Tag: Normal

---

### Question 659
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Flatten Binary Tree
Difficulty: Medium

Question: How to flatten binary tree to linked list in-place?
A) Create new list
B) Morris traversal or reverse postorder with pointer manipulation
C) Level order
D) Impossible in-place

✔ Correct Answer: B

Reason: Reverse postorder (right, left, root) with pointer manipulation or Morris traversal flattens tree to right-skewed linked list in-place.

Tag: Normal

---

### Question 660
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Construct Tree
Difficulty: Hard

Question: Can you construct unique binary tree from preorder and postorder only?
A) Yes, always
B) No, need inorder with one of them
C) Yes, if full binary tree
D) Never possible

✔ Correct Answer: C

Reason: Preorder and postorder alone don't uniquely determine tree, except for full binary trees where each node has 0 or 2 children.

Tag: Normal

---

### Question 661
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Clone Graph
Difficulty: Medium

Question: What approach clones a graph?
A) Copy nodes only
B) DFS/BFS with hash map tracking old-to-new node mapping
C) Copy edges only
D) Simple copy

✔ Correct Answer: B

Reason: Use DFS/BFS with hash map to track cloned nodes, creating new nodes and edges while avoiding infinite loops in cyclic graphs.

Tag: Normal

---

### Question 662
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Word Ladder
Difficulty: Hard

Question: What algorithm solves word ladder problem?
A) DFS
B) BFS for shortest transformation sequence
C) Binary search
D) Sorting

✔ Correct Answer: B

Reason: BFS finds shortest transformation sequence from start to end word, treating words as graph vertices with edges between one-letter-different words.

Tag: Normal

---

### Question 663
Domain: Data Structures
Topic: String Algorithms
Subtopic: Group Anagrams
Difficulty: Medium

Question: How to efficiently group anagrams?
A) Compare all pairs
B) Use sorted string or character count as hash key
C) Random grouping
D) Length-based grouping

✔ Correct Answer: B

Reason: Use sorted string or character count tuple as hash key to group anagrams in O(n*k log k) where n is words, k is max length.

Tag: Normal

---

### Question 664
Domain: Data Structures
Topic: String Algorithms
Subtopic: Valid Parentheses
Difficulty: Easy

Question: What data structure checks valid parentheses?
A) Queue
B) Stack
C) Array
D) Tree

✔ Correct Answer: B

Reason: Stack matches opening brackets with closing brackets, pushing opening and popping on closing, valid if stack empty at end.

Tag: Past Paper

---

### Question 665
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Valid Parentheses
Difficulty: Hard

Question: How to find longest valid parentheses substring?
A) Simple counting
B) Stack or DP tracking valid lengths
C) Sorting
D) Hashing

✔ Correct Answer: B

Reason: Stack stores indices to track valid parentheses spans, or DP tracks valid lengths, both solving in O(n) time.

Tag: Normal

---


### Question 666
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Product Except Self
Difficulty: Medium

Question: How to compute product of array except self without division?
A) Nested loops
B) Left and right product arrays
C) Sorting
D) Impossible

✔ Correct Answer: B

Reason: Compute left products and right products separately, then multiply for each position, achieving O(n) time without division.

Tag: Normal

---

### Question 667
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Container With Most Water
Difficulty: Medium

Question: What approach solves container with most water?
A) Brute force only
B) Two pointers from ends
C) Sorting
D) Binary search

✔ Correct Answer: B

Reason: Two pointers from ends, moving pointer at shorter height inward, finds maximum area in O(n) time.

Tag: Normal

---

### Question 668
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Three Sum
Difficulty: Medium

Question: What is the time complexity of three sum problem?
A) O(n)
B) O(n²)
C) O(n³)
D) O(n log n)

✔ Correct Answer: B

Reason: Sort array O(n log n), then for each element use two pointers to find pairs, resulting in O(n²) total time.

Tag: Normal

---

### Question 669
Domain: Data Structures
Topic: String Algorithms
Subtopic: Minimum Window Substring
Difficulty: Hard

Question: What technique solves minimum window substring?
A) Brute force
B) Sliding window with character frequency
C) Sorting
D) Binary search

✔ Correct Answer: B

Reason: Sliding window with two pointers and character frequency map finds minimum window containing all target characters in O(n).

Tag: Normal

---

### Question 670
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Substring Without Repeating
Difficulty: Medium

Question: How to find longest substring without repeating characters?
A) Brute force
B) Sliding window with hash set
C) Sorting
D) Binary search

✔ Correct Answer: B

Reason: Sliding window with hash set tracks characters in current window, expanding right and contracting left on duplicates, O(n) time.

Tag: Normal

---

### Question 671
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Validate BST
Difficulty: Medium

Question: What is correct way to validate BST?
A) Check each node with children only
B) Check each node is within valid range from ancestors
C) Inorder only
D) Level order

✔ Correct Answer: B

Reason: Each node must be within range defined by ancestors (left subtree < node < right subtree), not just comparing with immediate children.

Tag: Normal

---

### Question 672
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Recover BST
Difficulty: Hard

Question: If two nodes are swapped in BST, how to find them?
A) Rebuild tree
B) Inorder traversal finds two violations
C) Level order
D) Preorder traversal

✔ Correct Answer: B

Reason: Inorder traversal of BST should be sorted. Two swapped nodes create violations where current < previous, identifying the swapped nodes.

Tag: Normal

---

### Question 673
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Course Schedule
Difficulty: Medium

Question: What does course schedule problem check?
A) Schedule optimization
B) If courses can be completed (cycle detection in DAG)
C) Minimum courses
D) Maximum courses

✔ Correct Answer: B

Reason: Course schedule checks if prerequisite graph is DAG (no cycles) using topological sort or DFS cycle detection.

Tag: Normal

---

### Question 674
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Alien Dictionary
Difficulty: Hard

Question: What does alien dictionary problem find?
A) Alien words
B) Character order from sorted alien words
C) Word count
D) Dictionary size

✔ Correct Answer: B

Reason: Build graph from character order constraints in sorted words, then topological sort gives character order, detecting invalid input if cycle exists.

Tag: Normal

---

### Question 675
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Increasing Subsequence
Difficulty: Hard

Question: What is the optimal time complexity for LIS?
A) O(n²)
B) O(n log n) using binary search
C) O(n)
D) O(n³)

✔ Correct Answer: B

Reason: DP with binary search maintains array of smallest tail elements for each length, achieving O(n log n) instead of O(n²) DP.

Tag: Normal

---

### Question 676
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Russian Doll Envelopes
Difficulty: Hard

Question: How is Russian doll envelopes related to LIS?
A) Unrelated
B) 2D LIS problem after sorting
C) Simple LIS
D) Reverse LIS

✔ Correct Answer: B

Reason: Sort by width ascending and height descending, then find LIS on heights, handling 2D nesting constraint in O(n log n).

Tag: Normal

---

### Question 677
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Merge Intervals
Difficulty: Medium

Question: What is the approach for merging overlapping intervals?
A) Random merging
B) Sort by start time, then merge overlapping
C) No sorting needed
D) Binary search

✔ Correct Answer: B

Reason: Sort intervals by start time O(n log n), then linearly merge overlapping intervals by comparing end times, total O(n log n).

Tag: Normal

---

### Question 678
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Insert Interval
Difficulty: Medium

Question: How to insert interval into sorted non-overlapping intervals?
A) Insert and resort
B) Find position, merge overlapping intervals
C) Append at end
D) Random insertion

✔ Correct Answer: B

Reason: Find insertion position, merge with overlapping intervals, maintaining sorted order in O(n) time without full resort.

Tag: Normal

---

### Question 679
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Kth Smallest in BST
Difficulty: Medium

Question: How to find kth smallest element in BST?
A) Level order
B) Inorder traversal (iterative or recursive)
C) Preorder
D) Postorder

✔ Correct Answer: B

Reason: Inorder traversal of BST visits nodes in sorted order, kth visited node is kth smallest, O(h+k) time where h is height.

Tag: Normal

---

### Question 680
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: BST Iterator
Difficulty: Hard

Question: How to implement BST iterator with O(h) space?
A) Store all nodes
B) Use stack for controlled inorder traversal
C) Use queue
D) Use array

✔ Correct Answer: B

Reason: Stack stores path to current node, pushing left children and popping for next, achieving O(h) space and amortized O(1) next operation.

Tag: Normal

---

### Question 681
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Median of Two Sorted Arrays
Difficulty: Hard

Question: What is the optimal time complexity for median of two sorted arrays?
A) O(m+n)
B) O(log(min(m,n)))
C) O(m*n)
D) O(n)

✔ Correct Answer: B

Reason: Binary search on smaller array to partition both arrays such that left half ≤ right half, finding median in O(log(min(m,n))).

Tag: Normal

---

### Question 682
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Kth Largest Element
Difficulty: Medium

Question: What is the average time complexity of quickselect?
A) O(n²)
B) O(n)
C) O(n log n)
D) O(log n)

✔ Correct Answer: B

Reason: Quickselect uses partitioning like quicksort but recurses only on relevant side, achieving O(n) average, O(n²) worst case.

Tag: Normal

---

### Question 683
Domain: Data Structures
Topic: Heap Applications
Subtopic: Top K Elements
Difficulty: Medium

Question: How to find top k elements efficiently?
A) Sort completely
B) Min heap of size k
C) Max heap of size n
D) Array scan

✔ Correct Answer: B

Reason: Maintain min heap of size k, replacing minimum if larger element found, achieving O(n log k) time instead of O(n log n) sorting.

Tag: Normal

---

### Question 684
Domain: Data Structures
Topic: Heap Applications
Subtopic: Kth Largest in Stream
Difficulty: Medium

Question: What data structure maintains kth largest in stream?
A) Array
B) Min heap of size k
C) Max heap
D) Stack

✔ Correct Answer: B

Reason: Min heap of size k maintains k largest elements, with root being kth largest, allowing O(log k) insertion and O(1) kth largest access.

Tag: Normal

---

### Question 685
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Median in Stream
Difficulty: Hard

Question: How to maintain median in data stream?
A) Sort on each insertion
B) Two heaps (max heap for lower half, min heap for upper half)
C) Single heap
D) Array

✔ Correct Answer: B

Reason: Max heap stores lower half, min heap stores upper half, balancing sizes to keep median at heap tops, O(log n) insertion, O(1) median.

Tag: Normal

---

### Question 686
Domain: Data Structures
Topic: Trie Applications
Subtopic: Word Search II
Difficulty: Hard

Question: How does Trie optimize word search in grid?
A) No optimization
B) Prunes search space by checking valid prefixes
C) Sorts words
D) Random search

✔ Correct Answer: B

Reason: Trie enables checking if current path forms valid prefix, pruning DFS early if no words start with current prefix.

Tag: Normal

---

### Question 687
Domain: Data Structures
Topic: Trie Applications
Subtopic: Autocomplete
Difficulty: Medium

Question: How does Trie enable autocomplete?
A) Stores all words
B) Finds all words with given prefix efficiently
C) Random suggestions
D) Sorting

✔ Correct Answer: B

Reason: Navigate to prefix node in O(k), then DFS from there to collect all words with that prefix, efficient for autocomplete suggestions.

Tag: Normal

---

### Question 688
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Longest Consecutive Sequence
Difficulty: Medium

Question: How to find longest consecutive sequence in O(n)?
A) Sort first
B) Hash set with sequence building
C) Binary search
D) Nested loops

✔ Correct Answer: B

Reason: Use hash set for O(1) lookup, for each sequence start (no num-1 exists), count consecutive numbers, achieving O(n) time.

Tag: Normal

---

### Question 689
Domain: Data Structures
Topic: Matrix Algorithms
Subtopic: Search 2D Matrix
Difficulty: Medium

Question: How to search in row-wise and column-wise sorted matrix?
A) Linear search
B) Start from top-right or bottom-left corner
C) Binary search each row
D) Random search

✔ Correct Answer: B

Reason: Starting from top-right, move left if target smaller, down if larger, eliminating row or column each step, O(m+n) time.

Tag: Normal

---

### Question 690
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Skyline Problem
Difficulty: Hard

Question: What approach solves skyline problem?
A) Simple scan
B) Sweep line with priority queue
C) Sorting only
D) Random

✔ Correct Answer: B

Reason: Process building start/end events in sorted order, using priority queue to track active buildings and detect height changes.

Tag: Normal

---

### Question 691
Domain: Data Structures
Topic: String Algorithms
Subtopic: Decode Ways
Difficulty: Medium

Question: What technique solves decode ways problem?
A) Greedy
B) Dynamic programming
C) Backtracking only
D) Sorting

✔ Correct Answer: B

Reason: DP counts ways to decode string where dp[i] depends on single digit (dp[i-1]) and two digits (dp[i-2]) being valid.

Tag: Normal

---

### Question 692
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Unique Paths
Difficulty: Medium

Question: How many unique paths in m×n grid from top-left to bottom-right?
A) m+n
B) C(m+n-2, m-1) or DP
C) m*n
D) m^n

✔ Correct Answer: B

Reason: Combinatorial formula C(m+n-2, m-1) or DP with dp[i][j] = dp[i-1][j] + dp[i][j-1] computes unique paths.

Tag: Normal

---

### Question 693
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Path Sum
Difficulty: Easy

Question: How to find minimum path sum in grid?
A) Greedy
B) DP with dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
C) BFS
D) DFS

✔ Correct Answer: B

Reason: DP builds minimum path sum to each cell from top-left, choosing minimum of top or left neighbor, O(m*n) time.

Tag: Normal

---

### Question 694
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Number of Islands
Difficulty: Medium

Question: How to count islands in binary matrix?
A) Count 1s
B) DFS/BFS from each unvisited land cell
C) Count rows
D) Count columns

✔ Correct Answer: B

Reason: For each unvisited land cell, perform DFS/BFS to mark entire island, incrementing count, O(m*n) time.

Tag: Normal

---

### Question 695
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Surrounded Regions
Difficulty: Hard

Question: How to capture surrounded regions?
A) Capture all
B) DFS/BFS from border, mark non-captured, flip rest
C) Random capture
D) Capture none

✔ Correct Answer: B

Reason: DFS/BFS from border marks regions connected to border as non-captured, then flip remaining regions, O(m*n) time.

Tag: Normal

---

### Question 696
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Populating Next Right Pointers
Difficulty: Medium

Question: How to populate next right pointers in perfect binary tree?
A) Level order with queue
B) Use parent's next pointer (O(1) space)
C) DFS
D) Impossible

✔ Correct Answer: B

Reason: For perfect binary tree, use parent's next pointer to connect children without queue, achieving O(1) space instead of O(n).

Tag: Normal

---

### Question 697
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Word Break
Difficulty: Hard

Question: What approach solves word break problem?
A) Greedy
B) DP with dp[i] = any(dp[j] and s[j:i] in dict)
C) Backtracking only
D) Sorting

✔ Correct Answer: B

Reason: DP checks if string[0:i] can be segmented by trying all positions j where string[0:j] is valid and string[j:i] is in dictionary.

Tag: Normal

---

### Question 698
Domain: Data Structures
Topic: String Algorithms
Subtopic: Regular Expression Matching
Difficulty: Hard

Question: What technique solves regex matching with . and *?
A) Simple comparison
B) Dynamic programming or recursion with memoization
C) Greedy
D) Sorting

✔ Correct Answer: B

Reason: DP handles . (any char) and * (zero or more) by checking character matches and star patterns, O(m*n) time for pattern m and text n.

Tag: Normal

---

### Question 699
Domain: Data Structures
Topic: String Algorithms
Subtopic: Wildcard Matching
Difficulty: Hard

Question: How does wildcard matching differ from regex?
A) Same thing
B) Uses ? (single char) and * (any sequence)
C) Simpler always
D) No difference

✔ Correct Answer: B

Reason: Wildcard uses ? for single character and * for any sequence (including empty), solved with DP similar to regex but different rules.

Tag: Normal

---

### Question 700
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Expression Evaluation
Difficulty: Hard

Question: How to evaluate postfix expression?
A) Two stacks
B) Single stack
C) Queue
D) Recursion

✔ Correct Answer: B

Reason: Single stack pushes operands, pops two operands on operator, computes and pushes result, evaluating postfix in O(n) with O(n) space.

Tag: Normal

---

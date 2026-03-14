# Data Structures - MCQ Batch 08
## Questions 701-800

---

### Question 701
Domain: Data Structures
Topic: Stack Applications
Subtopic: Infix to Postfix
Difficulty: Medium

Question: What data structure converts infix to postfix?
A: Queue
B: Stack for operators
C: Array
D: Tree

✔ Correct Answer: B

Reason: Stack maintains operators based on precedence, outputting higher precedence operators before lower ones, converting infix to postfix.

Tag: Normal

---

### Question 702
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Next Permutation
Difficulty: Hard

Question: How to find next lexicographic permutation?
A: Generate all permutations
B: Find rightmost ascending pair, swap and reverse suffix
C: Sort
D: Random

✔ Correct Answer: B

Reason: Find rightmost i where a[i] < a[i+1], swap a[i] with smallest larger element in suffix, reverse suffix, O(n) time.

Tag: Normal

---

### Question 703
Domain: Data Structures
Topic: String Algorithms
Subtopic: Implement strStr
Difficulty: Medium

Question: What is the most efficient algorithm for substring search?
A: Naive O(m*n)
B: KMP O(m+n)
C: Brute force
D: Sorting

✔ Correct Answer: B

Reason: KMP algorithm with LPS array achieves O(m+n) time complexity, most efficient for substring search compared to naive O(m*n).

Tag: Normal

---

### Question 704
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Rotate Array
Difficulty: Easy

Question: How to rotate array right by k positions in O(1) space?
A: Use extra array
B: Reverse entire, reverse first k, reverse remaining
C: Shift one by one
D: Impossible

✔ Correct Answer: B

Reason: Three reversals achieve rotation: reverse all, reverse [0:k-1], reverse [k:n-1], O(n) time and O(1) space.

Tag: Normal

---

### Question 705
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Add Two Numbers
Difficulty: Medium

Question: How to add two numbers represented as linked lists?
A: Convert to integers
B: Traverse both lists with carry tracking
C: Reverse and add
D: Use array

✔ Correct Answer: B

Reason: Traverse both lists simultaneously, adding digits with carry, creating result list, handling different lengths and final carry.

Tag: Normal

---

### Question 706
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Zigzag Level Order
Difficulty: Medium

Question: How to implement zigzag level order traversal?
A: Use two stacks alternating direction
B: Single queue with reverse
C: Recursion only
D: DFS

✔ Correct Answer: A

Reason: Two stacks alternate left-to-right and right-to-left traversal at each level, achieving zigzag pattern efficiently.

Tag: Normal

---

### Question 707
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Coin Change
Difficulty: Medium

Question: What approach solves minimum coins for amount?
A: Greedy always works
B: DP with dp[i] = min coins for amount i
C: Backtracking only
D: Sorting

✔ Correct Answer: B

Reason: DP builds solution: dp[i] = min(dp[i-coin]+1) for all coins, handles cases where greedy fails.

Tag: Normal

---

### Question 708
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Course Schedule
Difficulty: Medium

Question: How to detect if courses can be completed with prerequisites?
A: Check for cycle in directed graph using DFS
B: Sort courses
C: Count edges
D: BFS only

✔ Correct Answer: A

Reason: Prerequisites form directed graph, cycle detection using DFS with visited/visiting states determines if all courses completable.

Tag: Normal

---

### Question 709
Domain: Data Structures
Topic: Heap Applications
Subtopic: Kth Largest Element
Difficulty: Medium

Question: Most efficient way to find kth largest element?
A: Sort array O(n log n)
B: Min heap of size k, O(n log k)
C: Linear scan
D: Binary search

✔ Correct Answer: B

Reason: Maintain min heap of k largest elements, root is kth largest, O(n log k) time better than sorting for small k.

Tag: Normal

---

### Question 710
Domain: Data Structures
Topic: String Manipulation
Subtopic: Longest Palindromic Substring
Difficulty: Medium

Question: What technique finds longest palindromic substring efficiently?
A: Check all substrings O(n³)
B: Expand around centers O(n²)
C: Greedy
D: Sorting

✔ Correct Answer: B

Reason: Expand around each possible center (2n-1 centers including between chars), O(n²) time, better than naive O(n³).

Tag: Normal

---

### Question 711
Domain: Data Structures
Topic: Array Techniques
Subtopic: Container With Most Water
Difficulty: Medium

Question: How to find maximum water container area?
A: Check all pairs O(n²)
B: Two pointers from ends, move smaller height
C: Sort heights
D: Stack

✔ Correct Answer: B

Reason: Two pointers start at ends, area = min(height) * width, move pointer with smaller height inward, O(n) time.

Tag: Normal

---

### Question 712
Domain: Data Structures
Topic: Backtracking
Subtopic: Generate Parentheses
Difficulty: Medium

Question: How to generate all valid n pairs of parentheses?
A: Generate all permutations and filter
B: Backtrack with open/close count constraints
C: Dynamic programming
D: Greedy

✔ Correct Answer: B

Reason: Backtrack adding '(' if open < n, adding ')' if close < open, ensures valid combinations without generating invalid ones.

Tag: Normal

---

### Question 713
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Lowest Common Ancestor
Difficulty: Medium

Question: How to find LCA in binary tree?
A: Store all ancestors in array
B: Recursive: if p and q in different subtrees, root is LCA
C: Level order traversal
D: Inorder traversal

✔ Correct Answer: B

Reason: Recursively check if p and q in different subtrees of current node, if yes current is LCA, else recurse to subtree containing both.

Tag: Normal

---

### Question 714
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Merge Intervals
Difficulty: Medium

Question: How to merge overlapping intervals?
A: Sort by start, merge if overlap
B: Check all pairs
C: Use heap
D: Dynamic programming

✔ Correct Answer: A

Reason: Sort intervals by start time, iterate merging current with previous if overlap (current.start <= prev.end), O(n log n).

Tag: Normal

---

### Question 715
Domain: Data Structures
Topic: Graph Traversal
Subtopic: Number of Islands
Difficulty: Medium

Question: How to count islands in 2D grid?
A: Count all 1s
B: DFS/BFS from each unvisited land cell, mark visited
C: Union-find only
D: Greedy

✔ Correct Answer: B

Reason: Iterate grid, when finding unvisited land, DFS/BFS to mark entire island, increment count, O(m*n) time.

Tag: Normal

---

### Question 716
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Unique Paths
Difficulty: Medium

Question: How many unique paths in m×n grid from top-left to bottom-right?
A: 2^(m+n)
B: dp[i][j] = dp[i-1][j] + dp[i][j-1]
C: m + n
D: m * n

✔ Correct Answer: B

Reason: DP approach: paths to cell = paths from above + paths from left, base case dp[0][0]=1, O(m*n) time and space.

Tag: Normal

---

### Question 717
Domain: Data Structures
Topic: String Algorithms
Subtopic: Group Anagrams
Difficulty: Medium

Question: How to group anagrams efficiently?
A: Compare each pair O(n²)
B: Use sorted string as hash key
C: Count characters for each
D: Random grouping

✔ Correct Answer: B

Reason: Sort each string as key in hashmap, anagrams have same sorted form, group by key, O(n*k log k) where k is max string length.

Tag: Normal

---

### Question 718
Domain: Data Structures
Topic: Tree Construction
Subtopic: Build Tree from Traversals
Difficulty: Hard

Question: Can you uniquely construct binary tree from preorder and postorder only?
A: Yes, always
B: No, need inorder with one of them
C: Yes, if tree is full binary tree
D: Yes, with level order

✔ Correct Answer: C

Reason: Preorder and postorder alone insufficient for general trees, but can construct full binary trees where every node has 0 or 2 children.

Tag: Normal

---

### Question 719
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Jump Game
Difficulty: Medium

Question: How to determine if can reach last index jumping max arr[i] steps?
A: Try all paths
B: Greedy: track max reachable index
C: BFS all positions
D: Dynamic programming only

✔ Correct Answer: B

Reason: Greedy approach: iterate updating max reachable, if current index > max reachable return false, O(n) time O(1) space.

Tag: Normal

---

### Question 720
Domain: Data Structures
Topic: Linked List Manipulation
Subtopic: Merge K Sorted Lists
Difficulty: Hard

Question: Most efficient way to merge k sorted linked lists?
A: Merge two at a time sequentially
B: Use min heap with k elements
C: Merge all into array and sort
D: Recursion only

✔ Correct Answer: B

Reason: Min heap of size k maintains smallest elements from each list, extract min and add next from that list, O(n log k) time.

Tag: Normal

---

### Question 721
Domain: Data Structures
Topic: Binary Search
Subtopic: Search in Rotated Array
Difficulty: Medium

Question: How to search in rotated sorted array?
A: Linear search O(n)
B: Modified binary search checking which half is sorted
C: Sort first
D: Two pointers

✔ Correct Answer: B

Reason: Binary search modified: determine which half is sorted, check if target in sorted half, adjust search space accordingly, O(log n).

Tag: Normal

---

### Question 722
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Word Break
Difficulty: Medium

Question: How to check if string can be segmented into dictionary words?
A: Try all combinations
B: DP: dp[i] = true if s[0:i] can be segmented
C: Greedy matching
D: Sort and search

✔ Correct Answer: B

Reason: DP approach: dp[i] true if any dp[j] true and s[j:i] in dictionary for j<i, O(n²*m) where m is dict lookup time.

Tag: Normal

---

### Question 723
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Serialize Binary Tree
Difficulty: Hard

Question: How to serialize and deserialize binary tree?
A: Level order with null markers
B: Inorder only
C: Preorder only
D: Count nodes

✔ Correct Answer: A

Reason: Level order traversal with null markers for missing children preserves structure, can reconstruct tree uniquely from serialized form.

Tag: Normal

---

### Question 724
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Clone Graph
Difficulty: Medium

Question: How to deep clone an undirected graph?
A: Copy nodes only
B: DFS/BFS with hashmap mapping old to new nodes
C: Copy edges only
D: Serialize and parse

✔ Correct Answer: B

Reason: Use hashmap to track cloned nodes, DFS/BFS creating new nodes and edges, prevents infinite loops and duplicate nodes.

Tag: Normal

---

### Question 725
Domain: Data Structures
Topic: Sliding Window
Subtopic: Longest Substring Without Repeating
Difficulty: Medium

Question: How to find longest substring without repeating characters?
A: Check all substrings O(n³)
B: Sliding window with hashset, expand/contract
C: Sort characters
D: Two passes

✔ Correct Answer: B

Reason: Sliding window with hashset, expand right adding chars, contract left when duplicate found, track max length, O(n) time.

Tag: Normal

---

### Question 726
Domain: Data Structures
Topic: Array Partitioning
Subtopic: Partition Labels
Difficulty: Medium

Question: How to partition string into max parts where each letter appears in only one part?
A: Split randomly
B: Track last occurrence of each char, extend partition to max last occurrence
C: Sort characters
D: Use stack

✔ Correct Answer: B

Reason: Record last occurrence of each character, iterate extending current partition end to max last occurrence seen, create partition when reaching end.

Tag: Normal

---

### Question 727
Domain: Data Structures
Topic: Tree Modification
Subtopic: Flatten Binary Tree
Difficulty: Medium

Question: How to flatten binary tree to linked list in-place?
A: Use extra array
B: Morris traversal or reverse preorder with right pointer
C: Level order
D: Inorder only

✔ Correct Answer: B

Reason: Reverse preorder (right, left, root) maintaining previous node, link current.right to previous, set left to null, O(n) time O(1) space.

Tag: Normal

---

### Question 728
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Decode Ways
Difficulty: Medium

Question: How many ways to decode numeric string where A=1, B=2, ..., Z=26?
A: Count digits
B: DP: dp[i] = dp[i-1] + dp[i-2] if valid two-digit
C: Greedy
D: Factorial

✔ Correct Answer: B

Reason: DP similar to Fibonacci: dp[i] counts ways, add dp[i-1] if single digit valid, add dp[i-2] if two digits valid (10-26).

Tag: Normal

---

### Question 729
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Single Number II
Difficulty: Medium

Question: Find element appearing once when others appear three times?
A: Use hashmap
B: Bit manipulation with ones and twos variables
C: Sort and compare
D: XOR

✔ Correct Answer: B

Reason: Track bits appearing once (ones) and twice (twos), when bit appears third time clear from both, remaining in ones is answer.

Tag: Normal

---

### Question 730
Domain: Data Structures
Topic: Stack Applications
Subtopic: Largest Rectangle in Histogram
Difficulty: Hard

Question: How to find largest rectangle area in histogram?
A: Check all pairs O(n²)
B: Stack maintaining increasing heights, calculate area on pop
C: Divide and conquer only
D: Greedy

✔ Correct Answer: B

Reason: Stack stores indices of increasing heights, when smaller height found, pop and calculate area with popped as smallest height, O(n) time.

Tag: Normal

---

### Question 731
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Word Ladder
Difficulty: Hard

Question: Shortest transformation sequence from beginWord to endWord changing one letter at a time?
A: DFS all paths
B: BFS treating words as graph nodes
C: Greedy character matching
D: Sort words

✔ Correct Answer: B

Reason: BFS on word graph where edge exists if words differ by one character, finds shortest path, O(M²*N) where M is word length, N is word count.

Tag: Normal

---

### Question 732
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Product Except Self
Difficulty: Medium

Question: How to compute product of array except self without division?
A: Nested loops O(n²)
B: Left and right product arrays
C: Use division
D: Impossible

✔ Correct Answer: B

Reason: Compute left products, then right products in reverse, result[i] = left[i] * right[i], O(n) time and space.

Tag: Normal

---

### Question 733
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Tree Maximum Path Sum
Difficulty: Hard

Question: How to find maximum path sum in binary tree?
A: Sum all nodes
B: Recursively compute max gain from each subtree, update global max
C: Level order sum
D: Preorder sum

✔ Correct Answer: B

Reason: For each node, max gain = node.val + max(0, left_gain, right_gain), path through node = node.val + left_gain + right_gain, track global max.

Tag: Normal

---

### Question 734
Domain: Data Structures
Topic: String Algorithms
Subtopic: Minimum Window Substring
Difficulty: Hard

Question: Find minimum window in s containing all characters of t?
A: Check all substrings
B: Sliding window with character frequency maps
C: Sort both strings
D: Greedy

✔ Correct Answer: B

Reason: Sliding window: expand right until valid, contract left while valid tracking minimum, use frequency maps to check validity, O(m+n).

Tag: Normal

---

### Question 735
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Copy List with Random Pointer
Difficulty: Medium

Question: How to deep copy linked list with random pointers?
A: Copy nodes only
B: Hashmap old to new nodes, two passes
C: Single pass impossible
D: Ignore random pointers

✔ Correct Answer: B

Reason: First pass creates nodes in hashmap, second pass sets next and random pointers using hashmap, handles cycles and complex references.

Tag: Normal

---

### Question 736
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Edit Distance
Difficulty: Hard

Question: Minimum operations to convert string s to t (insert/delete/replace)?
A: Count different characters
B: DP: dp[i][j] = min ops for s[0:i] to t[0:j]
C: Greedy replacement
D: Sort and compare

✔ Correct Answer: B

Reason: DP: if chars match dp[i][j]=dp[i-1][j-1], else min(insert: dp[i][j-1], delete: dp[i-1][j], replace: dp[i-1][j-1]) + 1.

Tag: Normal

---

### Question 737
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Next Permutation
Difficulty: Medium

Question: What happens when finding next permutation of largest permutation?
A: Return same
B: Return smallest permutation (reverse array)
C: Return error
D: Return empty

✔ Correct Answer: B

Reason: When array is in descending order (largest permutation), next permutation wraps to smallest (ascending order), reverse entire array.

Tag: Normal

---

### Question 738
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Binary Tree Right Side View
Difficulty: Medium

Question: How to get right side view of binary tree?
A: Traverse right subtree only
B: Level order, take last node of each level
C: Preorder traversal
D: Inorder traversal

✔ Correct Answer: B

Reason: Level order traversal, rightmost node at each level is visible from right side, O(n) time.

Tag: Normal

---

### Question 739
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Pacific Atlantic Water Flow
Difficulty: Medium

Question: Find cells where water can flow to both Pacific and Atlantic oceans?
A: Check each cell individually
B: DFS from ocean borders inward, find intersection
C: BFS from center
D: Greedy

✔ Correct Answer: B

Reason: DFS from Pacific borders marking reachable cells, DFS from Atlantic borders, intersection is answer, O(m*n) time.

Tag: Normal

---

### Question 740
Domain: Data Structures
Topic: Heap Applications
Subtopic: Find Median from Data Stream
Difficulty: Hard

Question: How to maintain median as numbers are added?
A: Sort after each insertion
B: Two heaps: max heap for lower half, min heap for upper half
C: Single array
D: Binary search tree

✔ Correct Answer: B

Reason: Max heap stores lower half, min heap stores upper half, balance sizes, median is heap tops, O(log n) insertion, O(1) median retrieval.

Tag: Normal

---

### Question 741
Domain: Data Structures
Topic: Trie Applications
Subtopic: Word Search II
Difficulty: Hard

Question: Find all words from dictionary in 2D board?
A: Search each word separately
B: Build trie of dictionary, DFS board with trie traversal
C: Check all paths
D: Sort board

✔ Correct Answer: B

Reason: Trie enables simultaneous search for all words, DFS board following trie paths, prune branches not in trie, much faster than individual searches.

Tag: Normal

---

### Question 742
Domain: Data Structures
Topic: Array Techniques
Subtopic: Trapping Rain Water
Difficulty: Hard

Question: How to calculate trapped rainwater in elevation map?
A: Simulate water filling
B: For each position, water = min(max_left, max_right) - height
C: Sort heights
D: Greedy

✔ Correct Answer: B

Reason: Water at position i trapped between max heights on left and right, compute left_max and right_max arrays, O(n) time and space.

Tag: Normal

---

### Question 743
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Increasing Subsequence
Difficulty: Medium

Question: Most efficient algorithm for LIS length?
A: DP O(n²)
B: Binary search with patience sorting O(n log n)
C: Greedy O(n)
D: Backtracking

✔ Correct Answer: B

Reason: Maintain array of smallest tail elements for increasing subsequences of each length, binary search to place elements, O(n log n).

Tag: Normal

---

### Question 744
Domain: Data Structures
Topic: String Manipulation
Subtopic: Valid Parentheses
Difficulty: Easy

Question: How to check if parentheses string is valid?
A: Count opening and closing
B: Stack: push opening, pop on closing, match types
C: Recursion
D: Two pointers

✔ Correct Answer: B

Reason: Stack tracks opening brackets, on closing bracket pop and verify match, valid if stack empty at end, O(n) time.

Tag: Normal

---

### Question 745
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Alien Dictionary
Difficulty: Hard

Question: How to derive alien language character order from sorted words?
A: Compare all word pairs
B: Build graph from adjacent word pairs, topological sort
C: Count character frequency
D: Alphabetical order

✔ Correct Answer: B

Reason: Compare adjacent words to find character ordering (edges in graph), topological sort gives valid character order, detect cycles for invalid input.

Tag: Normal

---

### Question 746
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Kth Smallest in BST
Difficulty: Medium

Question: How to find kth smallest element in BST?
A: Inorder traversal, return kth element
B: Level order traversal
C: Preorder traversal
D: Count all nodes

✔ Correct Answer: A

Reason: Inorder traversal of BST visits nodes in ascending order, return kth visited node, O(k) time with early termination.

Tag: Normal

---

### Question 747
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Find Peak Element
Difficulty: Medium

Question: How to find peak element in O(log n)?
A: Linear scan
B: Binary search: if mid > mid+1, peak in left half
C: Sort array
D: Two pointers

✔ Correct Answer: B

Reason: Binary search: if arr[mid] > arr[mid+1], peak exists in left half including mid, else in right half, O(log n) time.

Tag: Normal

---

### Question 748
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: House Robber
Difficulty: Easy

Question: Maximum money robbing houses without robbing adjacent ones?
A: Rob all houses
B: DP: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
C: Rob every other house
D: Greedy largest values

✔ Correct Answer: B

Reason: DP choice at each house: skip it (dp[i-1]) or rob it (dp[i-2] + nums[i]), take maximum, O(n) time.

Tag: Normal

---

### Question 749
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Common Subsequence
Difficulty: Medium

Question: How to find LCS length of two strings?
A: Check all subsequences
B: DP: dp[i][j] = LCS of s1[0:i] and s2[0:j]
C: Greedy matching
D: Sort and compare

✔ Correct Answer: B

Reason: DP: if chars match dp[i][j]=dp[i-1][j-1]+1, else max(dp[i-1][j], dp[i][j-1]), O(m*n) time and space.

Tag: Normal

---

### Question 750
Domain: Data Structures
Topic: Graph Traversal
Subtopic: Surrounded Regions
Difficulty: Medium

Question: How to capture surrounded regions in board?
A: Check each region separately
B: DFS from borders marking non-captured, flip remaining
C: BFS from center
D: Count regions

✔ Correct Answer: B

Reason: DFS from border 'O's marking them safe, flip all unmarked 'O's to 'X' (they're surrounded), restore marked ones, O(m*n).

Tag: Normal

---

### Question 751
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Sort List
Difficulty: Medium

Question: How to sort linked list in O(n log n) time O(1) space?
A: Convert to array and sort
B: Merge sort with slow/fast pointers to find middle
C: Bubble sort
D: Insertion sort

✔ Correct Answer: B

Reason: Merge sort on linked list: find middle with slow/fast pointers, recursively sort halves, merge sorted halves, O(n log n) time O(1) space.

Tag: Normal

---

### Question 752
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Maximum Product Subarray
Difficulty: Medium

Question: How to find maximum product of contiguous subarray?
A: Check all subarrays
B: Track both max and min products (negatives can flip)
C: Greedy largest values
D: Sort array

✔ Correct Answer: B

Reason: Track max and min products at each position (negative * min becomes max), update both considering current element, O(n) time O(1) space.

Tag: Normal

---

### Question 753
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Count Complete Tree Nodes
Difficulty: Medium

Question: How to count nodes in complete binary tree better than O(n)?
A: Traverse all nodes
B: Check if perfect tree, else recurse on subtrees, O(log²n)
C: Level order count
D: Impossible

✔ Correct Answer: B

Reason: Check left and right heights, if equal tree is perfect (2^h - 1 nodes), else recurse on subtrees, O(log²n) time.

Tag: Normal

---

### Question 754
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Majority Element II
Difficulty: Medium

Question: Find all elements appearing more than n/3 times?
A: Hashmap counting
B: Boyer-Moore voting with two candidates
C: Sort and count
D: Nested loops

✔ Correct Answer: B

Reason: At most 2 elements can appear > n/3 times, Boyer-Moore with two candidates and counters, verify candidates in second pass, O(n) time O(1) space.

Tag: Normal

---

### Question 755
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Evaluate Division
Difficulty: Medium

Question: Given equations a/b=k, how to evaluate queries?
A: Solve algebraically
B: Build weighted graph, DFS/BFS to find path product
C: Store all ratios
D: Matrix multiplication

✔ Correct Answer: B

Reason: Graph where edge a→b has weight k, b→a has weight 1/k, query a/c is path product from a to c using DFS/BFS.

Tag: Normal

---
### Question 756
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Interleaving String
Difficulty: Hard

Question: Check if s3 is interleaving of s1 and s2?
A: Try all combinations
B: DP: dp[i][j] = true if s3[0:i+j] is interleaving of s1[0:i] and s2[0:j]
C: Merge and compare
D: Greedy matching

✔ Correct Answer: B

Reason: DP: dp[i][j] true if (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1]), O(m*n) time.

Tag: Normal

---

### Question 757
Domain: Data Structures
Topic: Tree Construction
Subtopic: Construct from Inorder and Postorder
Difficulty: Medium

Question: How to build binary tree from inorder and postorder?
A: Random construction
B: Last postorder element is root, find in inorder to split subtrees
C: First postorder is root
D: Impossible

✔ Correct Answer: B

Reason: Last postorder element is root, find it in inorder to determine left/right subtrees, recursively build subtrees, O(n) with hashmap.

Tag: Normal

---

### Question 758
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Bitwise AND of Range
Difficulty: Medium

Question: Bitwise AND of all numbers in range [m,n]?
A: Iterate and AND all
B: Find common prefix of m and n in binary
C: AND m and n only
D: XOR operation

✔ Correct Answer: B

Reason: Numbers in range differ in lower bits, AND makes them 0, result is common binary prefix of m and n, right shift until equal.

Tag: Normal

---

### Question 759
Domain: Data Structures
Topic: Stack Applications
Subtopic: Basic Calculator
Difficulty: Hard

Question: How to implement calculator with +, -, (, )?
A: Evaluate left to right
B: Stack for numbers and operators, handle precedence and parentheses
C: Convert to postfix first
D: Recursion only

✔ Correct Answer: B

Reason: Stack maintains numbers and signs, on '(' push current result and sign, on ')' pop and apply, handle signs properly, O(n) time.

Tag: Normal

---

### Question 760
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Gas Station
Difficulty: Medium

Question: Find starting gas station to complete circular route?
A: Try each station
B: Track total and current surplus, start where current goes negative
C: Greedy largest gas
D: Binary search

✔ Correct Answer: B

Reason: If total gas >= total cost, solution exists, track current surplus, when negative reset start to next station, O(n) time.

Tag: Normal

---

### Question 761
Domain: Data Structures
Topic: String Algorithms
Subtopic: Palindrome Partitioning
Difficulty: Medium

Question: How to partition string into all palindromic substrings?
A: Check all partitions
B: Backtrack with palindrome checking, build partitions
C: Greedy longest palindromes
D: Dynamic programming only

✔ Correct Answer: B

Reason: Backtracking: try each position as partition point, check if prefix is palindrome, recurse on suffix, collect all valid partitions.

Tag: Normal

---

### Question 762
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Network Delay Time
Difficulty: Medium

Question: Minimum time for signal to reach all nodes from source?
A: BFS unweighted
B: Dijkstra's algorithm for shortest paths
C: DFS
D: Count edges

✔ Correct Answer: B

Reason: Weighted graph shortest path problem, Dijkstra finds shortest time to each node, answer is maximum of these times, O(E log V).

Tag: Normal

---

### Question 763
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Vertical Order Traversal
Difficulty: Hard

Question: How to perform vertical order traversal of binary tree?
A: Inorder traversal
B: Assign column indices, use hashmap, sort by column then row then value
C: Level order only
D: Preorder traversal

✔ Correct Answer: B

Reason: Assign column index (left child: col-1, right: col+1), track row, group by column in hashmap, sort appropriately, O(n log n).

Tag: Normal

---

### Question 764
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Burst Balloons
Difficulty: Hard

Question: Maximum coins from bursting balloons where coins = nums[i-1]*nums[i]*nums[i+1]?
A: Greedy burst smallest
B: DP: dp[i][j] = max coins bursting balloons between i and j, try each as last
C: Burst randomly
D: Sort and burst

✔ Correct Answer: B

Reason: DP thinking backwards: for range [i,j], try each k as last balloon burst, dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]).

Tag: Normal

---

### Question 765
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Reorder List
Difficulty: Medium

Question: Reorder list L0→L1→...→Ln to L0→Ln→L1→Ln-1→...?
A: Use extra array
B: Find middle, reverse second half, merge alternately
C: Recursion only
D: Swap adjacent

✔ Correct Answer: B

Reason: Find middle with slow/fast pointers, reverse second half, merge two halves alternately, O(n) time O(1) space.

Tag: Normal

---

### Question 766
Domain: Data Structures
Topic: Array Techniques
Subtopic: Sliding Window Maximum
Difficulty: Hard

Question: Maximum of each sliding window of size k?
A: Max of each window O(n*k)
B: Deque maintaining decreasing elements
C: Heap for each window
D: Sort each window

✔ Correct Answer: B

Reason: Deque stores indices of decreasing elements, front is max, remove out-of-window and smaller elements, O(n) time.

Tag: Normal

---

### Question 767
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Redundant Connection
Difficulty: Medium

Question: Find edge that creates cycle in undirected graph?
A: DFS from each edge
B: Union-Find, return edge that connects already connected nodes
C: BFS
D: Count degrees

✔ Correct Answer: B

Reason: Union-Find tracks connected components, when adding edge between nodes already in same component, that edge creates cycle, O(n*α(n)).

Tag: Normal

---

### Question 768
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Tree Cameras
Difficulty: Hard

Question: Minimum cameras to monitor all nodes (camera covers node, parent, children)?
A: Place on all nodes
B: Greedy post-order: place camera when child uncovered
C: Place on leaves
D: Random placement

✔ Correct Answer: B

Reason: Post-order traversal with states (covered, has camera, not covered), place camera when child not covered, greedy optimal.

Tag: Normal

---

### Question 769
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Regular Expression Matching
Difficulty: Hard

Question: Implement regex matching with . and * operators?
A: String comparison
B: DP: dp[i][j] = match of s[0:i] and p[0:j]
C: Greedy matching
D: Backtracking only

✔ Correct Answer: B

Reason: DP handles . (any char) and * (zero or more of previous), dp[i][j] considers char match and * cases, O(m*n) time.

Tag: Normal

---

### Question 770
Domain: Data Structures
Topic: Array Algorithms
Subtopic: First Missing Positive
Difficulty: Hard

Question: Find first missing positive integer in O(n) time O(1) space?
A: Sort array
B: Use array indices as hash, place each num at index num-1
C: Use hashset
D: Linear scan

✔ Correct Answer: B

Reason: Place each positive number at its value's index (num at index num-1), then scan for first index where value doesn't match, O(n) time O(1) space.

Tag: Normal

---

### Question 771
Domain: Data Structures
Topic: String Manipulation
Subtopic: Simplify Path
Difficulty: Medium

Question: How to simplify Unix file path?
A: String replacement
B: Split by '/', use stack, push dirs, pop on '..'
C: Remove all dots
D: Reverse path

✔ Correct Answer: B

Reason: Split path by '/', use stack: push directory names, pop on '..', ignore '.' and empty, join stack with '/', O(n) time.

Tag: Normal

---

### Question 772
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Accounts Merge
Difficulty: Medium

Question: How to merge accounts with common emails?
A: Compare all pairs
B: Union-Find on emails, group by component
C: Sort emails
D: Hashmap only

✔ Correct Answer: B

Reason: Union-Find treats emails as nodes, union emails in same account, group by root component, O(n*α(n)) where n is total emails.

Tag: Normal

---

### Question 773
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: All Nodes Distance K
Difficulty: Medium

Question: Find all nodes at distance K from target in binary tree?
A: BFS from target only
B: Build parent pointers, BFS treating as undirected graph
C: Level order from root
D: Preorder traversal

✔ Correct Answer: B

Reason: Add parent pointers, BFS from target in all directions (left, right, parent) treating as undirected graph, track visited, O(n) time.

Tag: Normal

---

### Question 774
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Distinct Subsequences
Difficulty: Hard

Question: Count distinct subsequences of s that equal t?
A: Generate all subsequences
B: DP: dp[i][j] = count for s[0:i] and t[0:j]
C: Greedy matching
D: Backtracking

✔ Correct Answer: B

Reason: DP: if s[i]==t[j], dp[i][j] = dp[i-1][j-1] + dp[i-1][j] (use or skip), else dp[i][j] = dp[i-1][j], O(m*n).

Tag: Normal

---

### Question 775
Domain: Data Structures
Topic: Array Techniques
Subtopic: Longest Consecutive Sequence
Difficulty: Medium

Question: Find longest consecutive sequence in unsorted array in O(n)?
A: Sort first O(n log n)
B: HashSet, for each sequence start, count length
C: Nested loops
D: Binary search

✔ Correct Answer: B

Reason: Add all to hashset, for each number without num-1 (sequence start), count consecutive numbers, track max, O(n) time.

Tag: Normal

---

### Question 776
Domain: Data Structures
Topic: String Algorithms
Subtopic: Wildcard Matching
Difficulty: Hard

Question: Implement wildcard matching with ? and * operators?
A: String comparison
B: DP: dp[i][j] = match of s[0:i] and p[0:j], handle * matching zero or more
C: Greedy
D: Regex library

✔ Correct Answer: B

Reason: DP: ? matches one char, * matches zero or more, dp[i][j] considers char match, ? match, and * cases (match zero or more), O(m*n).

Tag: Normal

---

### Question 777
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Height Trees
Difficulty: Medium

Question: Find roots that minimize tree height in undirected graph?
A: Try each node as root
B: Trim leaves iteratively, remaining nodes are centers
C: BFS from random node
D: DFS all paths

✔ Correct Answer: B

Reason: Minimum height tree roots are graph centers, iteratively remove leaves (degree 1 nodes) until 1-2 nodes remain, O(n) time.

Tag: Normal

---

### Question 778
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Sum Root to Leaf Numbers
Difficulty: Medium

Question: How to sum all root-to-leaf numbers in binary tree?
A: DFS tracking current number, add at leaves
B: Level order sum
C: Inorder traversal
D: Count nodes

✔ Correct Answer: A

Reason: DFS passing current number (num*10 + node.val), at leaf add to total sum, backtrack, O(n) time.

Tag: Normal

---

### Question 779
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Scramble String
Difficulty: Hard

Question: Check if s2 is scrambled version of s1 (binary tree scrambling)?
A: Compare sorted strings
B: DP/Recursion: try all split points, check if scrambled
C: Character count
D: Reverse string

✔ Correct Answer: B

Reason: Recursively try each split point, check if (left1 scrambles left2 and right1 scrambles right2) or (left1 scrambles right2 and right1 scrambles left2).

Tag: Normal

---

### Question 780
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Maximum Gap
Difficulty: Hard

Question: Find maximum gap between sorted elements in O(n) time?
A: Sort and compare O(n log n)
B: Bucket sort: gap must be >= ceiling((max-min)/(n-1))
C: Linear scan
D: Heap

✔ Correct Answer: B

Reason: Pigeonhole principle: max gap >= (max-min)/(n-1), use buckets of this size, max gap is between buckets, O(n) time and space.

Tag: Normal

---

### Question 781
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Critical Connections
Difficulty: Hard

Question: Find critical connections (bridges) in network?
A: Remove each edge and check connectivity
B: Tarjan's algorithm with DFS and low-link values
C: BFS from each node
D: Count degrees

✔ Correct Answer: B

Reason: Tarjan's algorithm: DFS tracking discovery time and low-link value, edge is bridge if low[child] > disc[parent], O(V+E).

Tag: Normal

---

### Question 782
Domain: Data Structures
Topic: String Algorithms
Subtopic: Shortest Palindrome
Difficulty: Hard

Question: Find shortest palindrome by adding characters to front?
A: Add reverse of string
B: Find longest palindromic prefix using KMP, add remaining reversed
C: Check all possibilities
D: Add one character

✔ Correct Answer: B

Reason: Use KMP to find longest prefix that's palindrome (match s with reverse), add remaining suffix reversed to front, O(n) time.

Tag: Normal

---

### Question 783
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Recover BST
Difficulty: Hard

Question: Two nodes swapped in BST, how to recover?
A: Rebuild tree
B: Inorder traversal finds two violations, swap them back
C: Level order fix
D: Preorder fix

✔ Correct Answer: B

Reason: Inorder of BST is sorted, find two positions where order violated (first and second), swap those nodes' values, O(n) time O(1) space.

Tag: Normal

---

### Question 784
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Maximal Rectangle
Difficulty: Hard

Question: Find largest rectangle of 1s in binary matrix?
A: Check all rectangles
B: Convert to histogram problem for each row
C: Count 1s
D: Greedy

✔ Correct Answer: B

Reason: For each row, compute heights of consecutive 1s, apply largest rectangle in histogram algorithm, O(m*n) time.

Tag: Normal

---

### Question 785
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Best Time to Buy and Sell Stock III
Difficulty: Hard

Question: Maximum profit with at most 2 transactions?
A: Try all combinations
B: DP tracking max profit after each transaction state
C: Greedy two largest gains
D: Sort prices

✔ Correct Answer: B

Reason: DP with states: buy1, sell1, buy2, sell2, update each considering previous state and current price, O(n) time O(1) space.

Tag: Normal

---

### Question 786
Domain: Data Structures
Topic: String Manipulation
Subtopic: Text Justification
Difficulty: Hard

Question: How to justify text with maxWidth?
A: Add spaces randomly
B: Distribute spaces evenly, left-justify last line
C: Center align all
D: Right align

✔ Correct Answer: B

Reason: Pack words greedily, distribute extra spaces evenly between words (left to right for remainder), last line left-justified, O(n) time.

Tag: Normal

---

### Question 787
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Cheapest Flights Within K Stops
Difficulty: Medium

Question: Find cheapest flight with at most K stops?
A: Dijkstra's algorithm
B: BFS with price tracking, limit depth to K+1
C: DFS all paths
D: Greedy shortest path

✔ Correct Answer: B

Reason: BFS level by level (each level is one stop), track minimum price to each city, limit to K+1 levels, O(K*E) time.

Tag: Normal

---

### Question 788
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Tree Maximum Width
Difficulty: Medium

Question: How to find maximum width of binary tree?
A: Count all nodes
B: Level order with position indices, width = max - min + 1
C: Count leaves
D: Height of tree

✔ Correct Answer: B

Reason: Assign position indices (left child: 2*pos, right: 2*pos+1), at each level width = rightmost - leftmost + 1, track max, O(n).

Tag: Normal

---

### Question 789
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Stone Game
Difficulty: Medium

Question: Two players pick stones from ends, can first player always win with even piles?
A: Depends on values
B: Yes, first player can always choose all even or all odd indices
C: No
D: Random

✔ Correct Answer: B

Reason: With even number of piles, first player can force taking all even-indexed or all odd-indexed piles, one set has more stones.

Tag: Normal

---

### Question 790
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Subarray Sum Equals K
Difficulty: Medium

Question: Count subarrays with sum equal to k?
A: Check all subarrays O(n²)
B: Prefix sum with hashmap tracking frequencies
C: Sort array
D: Two pointers

✔ Correct Answer: B

Reason: Track prefix sums in hashmap, for each position check if (prefix_sum - k) exists, count occurrences, O(n) time.

Tag: Normal

---

### Question 791
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Palindromic Subsequence
Difficulty: Medium

Question: How to find LPS length?
A: Check all subsequences
B: DP: dp[i][j] = LPS length in s[i:j], or LCS of s and reverse(s)
C: Greedy
D: Expand around centers

✔ Correct Answer: B

Reason: DP: if s[i]==s[j], dp[i][j]=dp[i+1][j-1]+2, else max(dp[i+1][j], dp[i][j-1]), or use LCS(s, reverse(s)), O(n²).

Tag: Normal

---

### Question 792
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Swim in Rising Water
Difficulty: Hard

Question: Minimum time to swim from top-left to bottom-right as water rises?
A: BFS shortest path
B: Binary search on time + BFS, or Dijkstra with max height as cost
C: DFS all paths
D: Greedy

✔ Correct Answer: B

Reason: Binary search on time, check if path exists with BFS, or use modified Dijkstra minimizing maximum height on path, O(n² log n).

Tag: Normal

---

### Question 793
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Distribute Coins in Binary Tree
Difficulty: Medium

Question: Minimum moves to distribute coins so each node has one?
A: Count total coins
B: Post-order: moves = sum of |balance| of children
C: Level order distribution
D: Preorder distribution

✔ Correct Answer: B

Reason: Post-order compute balance (coins - 1) for each subtree, moves through edge = |balance|, sum all moves, O(n) time.

Tag: Normal

---

### Question 794
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Cost Tree From Leaf Values
Difficulty: Medium

Question: Build tree minimizing sum of non-leaf values (node.val = max of leaves in subtree)?
A: Random tree
B: Greedy or DP: merge smallest adjacent leaves first
C: Balanced tree
D: Left-skewed tree

✔ Correct Answer: B

Reason: Greedy with stack or DP: merge adjacent leaves with smallest product first, minimizes intermediate node values, O(n²) DP or O(n) greedy.

Tag: Normal

---

### Question 795
Domain: Data Structures
Topic: Array Techniques
Subtopic: Minimum Window Subsequence
Difficulty: Hard

Question: Find minimum window in S containing T as subsequence?
A: Check all windows
B: Two pointers: expand to find T, contract to minimize
C: Dynamic programming
D: Sort strings

✔ Correct Answer: B

Reason: Expand right pointer matching T characters, when complete contract left pointer while maintaining match, track minimum window, O(S*T).

Tag: Normal

---

### Question 796
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bus Routes
Difficulty: Hard

Question: Minimum buses to reach target stop from source?
A: BFS on stops
B: BFS on bus routes (nodes are buses, edges if share stop)
C: DFS all routes
D: Greedy nearest

✔ Correct Answer: B

Reason: Model buses as nodes, edge if buses share stop, BFS finds minimum buses, track visited buses and stops, O(N*S) where N buses, S stops.

Tag: Normal

---

### Question 797
Domain: Data Structures
Topic: String Algorithms
Subtopic: Palindrome Pairs
Difficulty: Hard

Question: Find all pairs of words that concatenate to palindrome?
A: Check all pairs O(n²*k)
B: Trie with reverse lookup, check prefixes and suffixes
C: Sort and compare
D: Hashmap only

✔ Correct Answer: B

Reason: For each word, check if reverse exists (full palindrome), check prefixes (if suffix is palindrome), check suffixes (if prefix is palindrome), O(n*k²).

Tag: Normal

---

### Question 798
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Maximum Binary Tree
Difficulty: Medium

Question: How to construct maximum binary tree from array (root is max, recurse on left/right)?
A: Random construction
B: Find max as root, recursively build left and right subtrees
C: Inorder construction
D: Level order construction

✔ Correct Answer: B

Reason: Find maximum element as root, elements to left form left subtree, elements to right form right subtree, recurse, O(n²) worst case.

Tag: Normal

---

### Question 799
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Cherry Pickup
Difficulty: Hard

Question: Maximum cherries collecting going down then up in grid?
A: Two separate paths
B: DP: two people going down simultaneously
C: Greedy path
D: BFS

✔ Correct Answer: B

Reason: Model as two people going down simultaneously, DP state (r1, c1, r2, c2), share cherry if same cell, O(n⁴) or O(n³) optimized.

Tag: Normal

---

### Question 800
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Count of Range Sum
Difficulty: Hard

Question: Count range sums in [lower, upper] in array?
A: Check all subarrays O(n²)
B: Merge sort with prefix sums counting inversions
C: Segment tree
D: Binary search

✔ Correct Answer: B

Reason: Modified merge sort on prefix sums, during merge count how many right elements in range [left+lower, left+upper], O(n log n).

Tag: Normal

---

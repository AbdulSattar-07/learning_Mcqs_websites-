# Data Structures - MCQ Batch 10
## Questions 901-1000

---

### Question 901
Domain: Data Structures
Topic: Heap Applications
Subtopic: Reorganize String
Difficulty: Medium

Question: Rearrange string so no two adjacent characters are same?
A: Sort string
B: Max heap by frequency, alternate most frequent characters
C: Random shuffle
D: Reverse string

✔ Correct Answer: B

Reason: Max heap of character frequencies, repeatedly take two most frequent, append to result, decrease counts, impossible if max frequency > (n+1)/2.

Tag: Normal

---

### Question 902
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Number of Vertices to Reach All Nodes
Difficulty: Medium

Question: Find minimum vertices from which all nodes are reachable?
A: All nodes
B: Nodes with no incoming edges
C: Highest degree nodes
D: Random nodes

✔ Correct Answer: B

Reason: Nodes with no incoming edges must be in answer (can't be reached from others), these are sufficient to reach all nodes, O(V+E).

Tag: Normal

---

### Question 903
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Add One Row to Tree
Difficulty: Medium

Question: How to add row of nodes at given depth?
A: Level order insertion
B: DFS to depth-1, insert new nodes as children
C: Preorder insertion
D: Random insertion

✔ Correct Answer: B

Reason: DFS to target depth-1, for each node create new nodes with old children, set new nodes as children, handle depth=1 special case, O(n).

Tag: Normal

---

### Question 904
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Coin Change 2
Difficulty: Medium

Question: Count combinations to make amount with coins?
A: Permutations
B: DP: dp[i] = ways to make amount i, iterate coins outer loop
C: Greedy
D: Backtracking

✔ Correct Answer: B

Reason: DP: for each coin, update dp[i] += dp[i-coin], coin loop outside prevents counting permutations, O(n*amount) time.

Tag: Normal

---

### Question 905
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Wiggle Subsequence
Difficulty: Medium

Question: Length of longest wiggle subsequence (alternating differences)?
A: Check all subsequences
B: Greedy: count direction changes
C: DP tracking up and down
D: Sort

✔ Correct Answer: B

Reason: Greedy counts peaks and valleys (direction changes), or DP: up[i] = longest ending with increase, down[i] = longest ending with decrease, O(n).

Tag: Normal

---

### Question 906
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Happy String
Difficulty: Medium

Question: Create longest string with a, b, c where no three consecutive same characters?
A: Random order
B: Greedy with heap: use most frequent, avoid three consecutive
C: Alternate characters
D: Sort

✔ Correct Answer: B

Reason: Max heap by frequency, greedily pick most frequent that doesn't create three consecutive, O(n log 3) = O(n) time.

Tag: Normal

---

### Question 907
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Find City With Smallest Number of Neighbors
Difficulty: Medium

Question: Find city with smallest number of reachable cities within distance threshold?
A: BFS from each city
B: Floyd-Warshall for all pairs shortest paths, count reachable
C: Dijkstra from each
D: DFS

✔ Correct Answer: B

Reason: Floyd-Warshall computes all pairs shortest paths, for each city count cities within threshold, return city with minimum count, O(n³).

Tag: Normal

---

### Question 908
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Even Odd Tree
Difficulty: Medium

Question: Check if tree is even-odd (even levels increasing odd values, odd levels decreasing even values)?
A: Inorder check
B: Level order traversal checking values and order at each level
C: DFS
D: Preorder

✔ Correct Answer: B

Reason: Level order traversal, for each level check: even level has odd values increasing, odd level has even values decreasing, O(n) time.

Tag: Normal

---

### Question 909
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Count Vowels Permutation
Difficulty: Hard

Question: Count strings of length n following vowel rules (a→e, e→a/i, etc.)?
A: Generate all strings
B: DP: dp[i][vowel] = count of strings length i ending with vowel
C: Calculate directly
D: Backtracking

✔ Correct Answer: B

Reason: DP: for each vowel track count of strings ending with it, update based on rules, sum all vowels at length n, O(n) time.

Tag: Normal

---

### Question 910
Domain: Data Structures
Topic: Array Techniques
Subtopic: Minimum Number of K Consecutive Bit Flips
Difficulty: Hard

Question: Minimum flips of k consecutive bits to make all 1s?
A: Try all positions
B: Greedy with flip tracking: flip when encountering 0
C: Random flips
D: Binary search

✔ Correct Answer: B

Reason: Greedy left to right, track active flips with queue or counter, when encountering 0 (considering flips) flip k bits, O(n) time.

Tag: Normal

---

### Question 911
Domain: Data Structures
Topic: String Manipulation
Subtopic: Reverse Only Letters
Difficulty: Easy

Question: Reverse only letters keeping other characters in place?
A: Reverse entire string
B: Two pointers swapping only letters
C: Stack
D: Sort

✔ Correct Answer: B

Reason: Two pointers from ends, skip non-letters, swap letters, O(n) time O(1) space.

Tag: Normal

---

### Question 912
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Shortest Path in Binary Matrix
Difficulty: Medium

Question: Shortest path from top-left to bottom-right in binary matrix (8 directions)?
A: DFS
B: BFS tracking distance
C: Dijkstra
D: Greedy

✔ Correct Answer: B

Reason: BFS from (0,0) exploring 8 directions, first time reaching (n-1,n-1) gives shortest path, O(n²) time.

Tag: Normal

---

### Question 913
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Maximum Width Ramp
Difficulty: Medium

Question: Maximum width ramp where i < j and arr[i] ≤ arr[j]?
A: Check all pairs O(n²)
B: Stack of decreasing indices, scan right finding matches
C: Sort
D: Two pointers

✔ Correct Answer: B

Reason: Build stack of decreasing elements (potential left boundaries), scan from right, for each element pop smaller stack elements computing width, O(n).

Tag: Normal

---

### Question 914
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Cost to Merge Stones
Difficulty: Hard

Question: Minimum cost to merge n piles into 1 with k consecutive merges?
A: Merge randomly
B: DP: dp[i][j][p] = min cost to merge piles i to j into p piles
C: Greedy smallest
D: Sort piles

✔ Correct Answer: B

Reason: DP: dp[i][j][1] = dp[i][j][k] + sum[i:j], dp[i][j][p] = min over mid of (dp[i][mid][1] + dp[mid+1][j][p-1]), O(n³*k).

Tag: Normal

---

### Question 915
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Boats to Save People
Difficulty: Medium

Question: Minimum boats to save people with weight limit (max 2 per boat)?
A: One boat per person
B: Sort weights, two pointers pairing lightest with heaviest
C: Greedy heaviest
D: Random pairing

✔ Correct Answer: B

Reason: Sort weights, two pointers: if lightest + heaviest ≤ limit pair them, else take heaviest alone, O(n log n) time.

Tag: Normal

---

### Question 916
Domain: Data Structures
Topic: String Algorithms
Subtopic: Buddy Strings
Difficulty: Easy

Question: Can swap two letters in s to make it equal to goal?
A: Compare directly
B: Check if exactly 2 differences and swappable, or equal with duplicates
C: Sort both
D: Count characters

✔ Correct Answer: B

Reason: If equal check for duplicate char (can swap same chars), if different check exactly 2 positions differ and swapping makes equal, O(n).

Tag: Normal

---

### Question 917
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Snakes and Ladders
Difficulty: Medium

Question: Minimum moves to reach end in snakes and ladders board?
A: DFS all paths
B: BFS treating board as graph, follow snakes/ladders
C: Greedy
D: Dijkstra

✔ Correct Answer: B

Reason: BFS from square 1, for each square try moves 1-6, follow snake/ladder if present, first to reach n² is minimum, O(n²).

Tag: Normal

---

### Question 918
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Find Bottom Left Tree Value
Difficulty: Medium

Question: Find leftmost value in last row of binary tree?
A: Inorder traversal
B: Level order traversal, return first value of last level
C: Preorder
D: DFS right side

✔ Correct Answer: B

Reason: Level order traversal, track first value of each level, last level's first value is answer, or DFS tracking max depth, O(n) time.

Tag: Normal

---

### Question 919
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Ones and Zeroes
Difficulty: Medium

Question: Maximum strings in subset with at most m zeros and n ones?
A: Greedy smallest strings
B: DP: dp[i][j] = max strings with i zeros and j ones
C: Sort strings
D: Backtracking

✔ Correct Answer: B

Reason: 2D knapsack: for each string count zeros and ones, update dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1), O(l*m*n) time.

Tag: Normal

---

### Question 920
Domain: Data Structures
Topic: Array Techniques
Subtopic: Partition Array Into Disjoint Intervals
Difficulty: Medium

Question: Find index to partition array where max(left) ≤ min(right)?
A: Try all indices
B: Precompute max from left and min from right arrays
C: Sort array
D: Binary search

✔ Correct Answer: B

Reason: Compute left_max[i] and right_min[i] arrays, find first i where left_max[i] ≤ right_min[i+1], O(n) time and space.

Tag: Normal

---

### Question 921
Domain: Data Structures
Topic: String Manipulation
Subtopic: Backspace String Compare
Difficulty: Easy

Question: Compare two strings with backspaces (#)?
A: Process backspaces, compare results
B: Two pointers from end, skip backspaced characters
C: Stack for each
D: Remove all #

✔ Correct Answer: B

Reason: Two pointers from end, count backspaces, skip characters accordingly, compare characters, O(n+m) time O(1) space.

Tag: Normal

---

### Question 922
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Rotting Oranges
Difficulty: Medium

Question: Minimum time for all oranges to rot (rot spreads to adjacent)?
A: Count oranges
B: Multi-source BFS from all rotten oranges, track time
C: DFS
D: Greedy

✔ Correct Answer: B

Reason: Multi-source BFS from all initially rotten oranges, each level is one minute, track time until all fresh oranges rot, O(m*n).

Tag: Normal

---

### Question 923
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Increasing Order Search Tree
Difficulty: Easy

Question: Rearrange BST to tree where all nodes have only right children (increasing order)?
A: Rebuild tree
B: Inorder traversal building new tree with right pointers only
C: Level order
D: Preorder

✔ Correct Answer: B

Reason: Inorder traversal visits nodes in increasing order, build new tree linking each node as right child of previous, O(n) time.

Tag: Normal

---

### Question 924
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Partition to K Equal Sum Subsets
Difficulty: Medium

Question: Can partition array into k subsets with equal sum?
A: Try all partitions
B: Backtracking with memoization, target = sum/k
C: Greedy division
D: Sort and split

✔ Correct Answer: B

Reason: If sum % k != 0 impossible, backtracking fills k buckets to target = sum/k, use bitmask for memoization, O(k*2^n) time.

Tag: Normal

---

### Question 925
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Maximize Sum of Array After K Negations
Difficulty: Easy

Question: Maximum sum after negating exactly k elements?
A: Negate random elements
B: Sort, negate k smallest, if k remains toggle smallest absolute value
C: Negate largest
D: Negate first k

✔ Correct Answer: B

Reason: Sort array, negate k smallest (prioritize negatives), if k remains after all negatives, toggle smallest absolute value repeatedly, O(n log n).

Tag: Normal

---

### Question 926
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Word in Dictionary
Difficulty: Easy

Question: Find longest word built one character at a time from dictionary?
A: Check longest words
B: Sort words, use set to check if prefix exists
C: Trie
D: Random

✔ Correct Answer: B

Reason: Sort words by length then lexicographically, for each word check if prefix (word[:-1]) in set, track longest valid word, O(n log n + n*L).

Tag: Normal

---

### Question 927
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Is Graph Bipartite
Difficulty: Medium

Question: Check if undirected graph is bipartite?
A: Count edges
B: BFS/DFS with 2-coloring, check for conflicts
C: Check degrees
D: Sort nodes

✔ Correct Answer: B

Reason: Try to color graph with 2 colors using BFS/DFS, if adjacent nodes get same color not bipartite, handle disconnected components, O(V+E).

Tag: Normal

---

### Question 928
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Trim Binary Search Tree
Difficulty: Medium

Question: Trim BST to keep only nodes in range [low, high]?
A: Remove and rebuild
B: Recursively: if node < low return right, if > high return left, else recurse both
C: Level order trim
D: Inorder trim

✔ Correct Answer: B

Reason: Recursion: if node.val < low entire left subtree invalid return trimmed right, if > high return trimmed left, else trim both children, O(n).

Tag: Normal

---

### Question 929
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Swaps to Make String Equal
Difficulty: Medium

Question: Minimum swaps to make two strings equal (swap chars at two positions)?
A: Count differences
B: Count xy and yx patterns, swaps = xy/2 + yx/2 + (xy%2)*2
C: Greedy swap
D: Sort strings

✔ Correct Answer: B

Reason: Count mismatches: xy (s1[i]='x', s2[i]='y') and yx patterns, each pair of same pattern needs 1 swap, mixed pair needs 2 swaps, O(n).

Tag: Normal

---

### Question 930
Domain: Data Structures
Topic: Array Techniques
Subtopic: Minimum Size Subarray Sum
Difficulty: Medium

Question: Minimum length subarray with sum ≥ target?
A: Check all subarrays
B: Sliding window: expand right, contract left when sum ≥ target
C: Binary search
D: Sort array

✔ Correct Answer: B

Reason: Sliding window: expand right adding elements, when sum ≥ target contract left while maintaining condition, track minimum length, O(n).

Tag: Normal

---

### Question 931
Domain: Data Structures
Topic: String Manipulation
Subtopic: Goat Latin
Difficulty: Easy

Question: Convert sentence to Goat Latin (move first letter to end + "ma" + "a"*index)?
A: String replacement
B: Split words, apply rules, join
C: Reverse words
D: Sort

✔ Correct Answer: B

Reason: Split by spaces, for each word apply vowel/consonant rule, append "ma" + "a"*word_index, join with spaces, O(n) time.

Tag: Normal

---

### Question 932
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Height Trees
Difficulty: Medium

Question: Why can there be at most 2 MHT roots?
A: Random property
B: Tree centers are at most 2 adjacent nodes
C: Always exactly 2
D: Can be more

✔ Correct Answer: B

Reason: Tree has 1 center (odd diameter) or 2 adjacent centers (even diameter), these minimize height, trimming leaves converges to center(s).

Tag: Normal

---

### Question 933
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Cousins in Binary Tree
Difficulty: Easy

Question: Check if two nodes are cousins (same depth, different parents)?
A: Compare values
B: DFS/BFS tracking depth and parent for both nodes
C: Level order
D: Inorder

✔ Correct Answer: B

Reason: DFS or BFS finding both nodes, record depth and parent for each, cousins if same depth and different parents, O(n) time.

Tag: Normal

---

### Question 934
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Ugly Number II
Difficulty: Medium

Question: Find nth ugly number (factors only 2, 3, 5)?
A: Check each number
B: DP with three pointers for multiples of 2, 3, 5
C: Generate randomly
D: Prime factorization

✔ Correct Answer: B

Reason: DP: maintain three pointers, next ugly = min(dp[i2]*2, dp[i3]*3, dp[i5]*5), increment corresponding pointer(s), O(n) time.

Tag: Normal

---

### Question 935
Domain: Data Structures
Topic: Array Algorithms
Subtopic: 3Sum Closest
Difficulty: Medium

Question: Find three numbers with sum closest to target?
A: Try all triplets O(n³)
B: Sort, fix one, two pointers for other two
C: Greedy
D: Binary search

✔ Correct Answer: B

Reason: Sort array, fix first element, use two pointers for remaining two, track closest sum to target, O(n²) time.

Tag: Normal

---

### Question 936
Domain: Data Structures
Topic: String Algorithms
Subtopic: Unique Email Addresses
Difficulty: Easy

Question: Count unique email addresses (ignore dots in local, ignore after + in local)?
A: Count all emails
B: Normalize each email, use set to count unique
C: Sort emails
D: Hashmap

✔ Correct Answer: B

Reason: For each email: split by @, remove dots from local, remove after +, combine with domain, add to set, return set size, O(n*L).

Tag: Normal

---

### Question 937
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Cheapest Flights K Stops (Bellman-Ford)
Difficulty: Medium

Question: Why use Bellman-Ford variant for K stops problem?
A: Faster than BFS
B: Relaxes edges K+1 times, naturally limits path length
C: Handles negative weights
D: Random

✔ Correct Answer: B

Reason: Bellman-Ford relaxes edges iteratively, K+1 iterations ensures paths with at most K stops, handles negative weights if present, O(K*E).

Tag: Normal

---

### Question 938
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: N-ary Tree Level Order Traversal
Difficulty: Medium

Question: How to perform level order traversal of N-ary tree?
A: Preorder
B: Queue-based BFS, process each level
C: DFS
D: Inorder

✔ Correct Answer: B

Reason: BFS with queue, track level size, process all nodes at current level before moving to next, O(n) time.

Tag: Normal

---

### Question 939
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Perfect Squares
Difficulty: Medium

Question: Minimum perfect squares that sum to n?
A: Try all combinations
B: DP: dp[i] = min(dp[i-j²]+1) for all j where j²≤i
C: Greedy largest squares
D: Math formula

✔ Correct Answer: B

Reason: DP: for each number, try subtracting all perfect squares, take minimum, dp[i] = min(dp[i-j²]+1), O(n*√n) time.

Tag: Normal

---

### Question 940
Domain: Data Structures
Topic: Array Techniques
Subtopic: Sort Colors
Difficulty: Medium

Question: Sort array of 0s, 1s, 2s in-place in one pass?
A: Counting sort
B: Dutch National Flag: three pointers (low, mid, high)
C: Quick sort
D: Merge sort

✔ Correct Answer: B

Reason: Three pointers: low for 0s, high for 2s, mid iterates, swap 0s to low, 2s to high, 1s stay in middle, O(n) time O(1) space.

Tag: Normal

---

### Question 941
Domain: Data Structures
Topic: String Manipulation
Subtopic: Reverse String II
Difficulty: Easy

Question: Reverse first k characters of every 2k characters?
A: Reverse entire string
B: Iterate in 2k chunks, reverse first k of each
C: Reverse all k-length substrings
D: Random

✔ Correct Answer: B

Reason: Iterate string in steps of 2k, reverse substring [i:i+k] for each chunk, handle remaining characters at end, O(n) time.

Tag: Normal

---

### Question 942
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: All Paths From Source to Target
Difficulty: Medium

Question: Find all paths from node 0 to node n-1 in DAG?
A: BFS
B: DFS with path tracking, backtrack
C: Dijkstra
D: Greedy

✔ Correct Answer: B

Reason: DFS from source maintaining current path, when reaching target add path copy to result, backtrack, O(2^n * n) worst case.

Tag: Normal

---

### Question 943
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Sum of Left Leaves
Difficulty: Easy

Question: Sum of all left leaf values?
A: Sum all leaves
B: DFS/BFS tracking if node is left child and leaf
C: Inorder sum
D: Level order sum

✔ Correct Answer: B

Reason: DFS passing flag indicating if current node is left child, if left child and leaf add to sum, O(n) time.

Tag: Normal

---

### Question 944
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Combination Sum IV
Difficulty: Medium

Question: Count combinations to make target (order matters)?
A: Backtracking
B: DP: dp[i] = sum of dp[i-num] for all nums
C: Greedy
D: Permutations

✔ Correct Answer: B

Reason: DP: for each amount, sum ways from all possible previous amounts (amount - num), target loop outside counts permutations, O(target*n).

Tag: Normal

---

### Question 945
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Find All Numbers Disappeared
Difficulty: Easy

Question: Find missing numbers in [1,n] array in O(n) time O(1) space?
A: Use hashset
B: Mark presence by negating value at index num-1
C: Sort array
D: Nested loops

✔ Correct Answer: B

Reason: For each num, negate value at index num-1, iterate again collecting indices with positive values (those numbers missing), O(n) time O(1) space.

Tag: Normal

---

### Question 946
Domain: Data Structures
Topic: String Algorithms
Subtopic: Isomorphic Strings
Difficulty: Easy

Question: Check if two strings are isomorphic (bijective character mapping)?
A: Compare lengths
B: Two hashmaps ensuring bijection (s→t and t→s)
C: Sort both
D: Count characters

✔ Correct Answer: B

Reason: Maintain two hashmaps for bidirectional mapping, ensure each character maps consistently and uniquely, O(n) time.

Tag: Normal

---

### Question 947
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Flower Planting With No Adjacent
Difficulty: Medium

Question: Assign 4 flower types to gardens where adjacent gardens have different flowers?
A: Random assignment
B: Greedy: for each garden, assign first available type not used by neighbors
C: Backtracking
D: Graph coloring algorithm

✔ Correct Answer: B

Reason: Greedy works because max degree is 3 (given constraint), always have at least one of 4 colors available, O(V+E) time.

Tag: Normal

---

### Question 948
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Univalued Binary Tree
Difficulty: Easy

Question: Check if all nodes have same value?
A: Count distinct values
B: DFS/BFS comparing each node with root value
C: Inorder check
D: Level order

✔ Correct Answer: B

Reason: DFS or BFS checking if each node's value equals root value, return false on first mismatch, O(n) time.

Tag: Normal

---

### Question 949
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Path Sum
Difficulty: Medium

Question: Minimum path sum from top-left to bottom-right (move right or down)?
A: Greedy down-right
B: DP: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
C: DFS all paths
D: Dijkstra

✔ Correct Answer: B

Reason: DP: minimum path to cell is cell value plus minimum of paths from top or left, O(m*n) time, can optimize to O(n) space.

Tag: Normal

---

### Question 950
Domain: Data Structures
Topic: Array Techniques
Subtopic: Monotonic Array
Difficulty: Easy

Question: Check if array is monotonic (all increasing or all decreasing)?
A: Sort and compare
B: Single pass tracking if increasing and decreasing
C: Compare first and last
D: Count changes

✔ Correct Answer: B

Reason: Iterate tracking if any decrease and any increase seen, monotonic if not both, O(n) time O(1) space.

Tag: Normal

---
### Question 951
Domain: Data Structures
Topic: String Manipulation
Subtopic: Reverse Vowels of String
Difficulty: Easy

Question: Reverse only vowels in string?
A: Reverse entire string
B: Two pointers swapping only vowels
C: Stack
D: Sort

✔ Correct Answer: B

Reason: Two pointers from ends, skip consonants, swap vowels when both pointers on vowels, O(n) time O(1) space.

Tag: Normal

---

### Question 952
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Maximal Network Rank
Difficulty: Medium

Question: Maximum network rank (sum of degrees of two cities minus shared edge)?
A: Sum all degrees
B: Try all pairs, compute rank = degree[a] + degree[b] - (1 if connected)
C: Highest degree city
D: Random

✔ Correct Answer: B

Reason: Try all city pairs, network rank = degree[i] + degree[j] - (1 if edge between them), track maximum, O(n²) time.

Tag: Normal

---

### Question 953
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Range Sum of BST
Difficulty: Easy

Question: Sum of values in BST within range [low, high]?
A: Sum all nodes
B: DFS pruning: skip left if node < low, skip right if node > high
C: Inorder traversal
D: Level order

✔ Correct Answer: B

Reason: DFS with pruning: if node.val < low skip left subtree, if > high skip right subtree, add node if in range, O(n) worst case.

Tag: Normal

---

### Question 954
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Turbulent Subarray
Difficulty: Medium

Question: Length of longest turbulent subarray (alternating comparison signs)?
A: Check all subarrays
B: DP tracking current length with last comparison direction
C: Greedy
D: Sort

✔ Correct Answer: B

Reason: Track current length and last comparison (< or >), extend if alternates, reset if same or equal, track maximum, O(n) time O(1) space.

Tag: Normal

---

### Question 955
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Squares of Sorted Array
Difficulty: Easy

Question: Return squares of sorted array in sorted order?
A: Square and sort O(n log n)
B: Two pointers from ends, compare absolute values
C: Square in place
D: Binary search

✔ Correct Answer: B

Reason: Two pointers from ends (largest absolute values), compare and place larger square at end of result, O(n) time O(n) space.

Tag: Normal

---

### Question 956
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Uncommon Subsequence II
Difficulty: Medium

Question: Find longest uncommon subsequence (not subsequence of any other string)?
A: Longest string
B: Check each string if it's subsequence of any other
C: Sort by length
D: Random

✔ Correct Answer: B

Reason: Sort by length descending, for each string check if it's subsequence of any other, first non-subsequence is answer, O(n²*L).

Tag: Normal

---

### Question 957
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Shortest Path to Get All Keys
Difficulty: Hard

Question: Shortest path to collect all keys in grid with locks?
A: DFS all paths
B: BFS with state (position, keys_collected)
C: Greedy nearest key
D: Dijkstra

✔ Correct Answer: B

Reason: BFS with state (row, col, keys_bitmask), can pass through lock if have key, collect keys updating bitmask, O(m*n*2^k) where k is key count.

Tag: Normal

---

### Question 958
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Merge Two Binary Trees
Difficulty: Easy

Question: Merge two trees (overlapping nodes sum values)?
A: Copy first tree
B: Recursively merge: sum overlapping, keep non-null children
C: Level order merge
D: Inorder merge

✔ Correct Answer: B

Reason: Recursion: if both nodes exist create new with sum and merge children, if one null return other, O(min(n,m)) time.

Tag: Normal

---

### Question 959
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Arithmetic Slices
Difficulty: Medium

Question: Count arithmetic subarrays (length ≥ 3, constant difference)?
A: Check all subarrays
B: Track current arithmetic sequence length, add to count
C: DP array
D: Greedy

✔ Correct Answer: B

Reason: Track current sequence length, when difference changes reset, for length L add (L-1)*(L-2)/2 subarrays, or increment count for each extension, O(n).

Tag: Normal

---

### Question 960
Domain: Data Structures
Topic: Array Techniques
Subtopic: Move Zeroes
Difficulty: Easy

Question: Move all zeros to end maintaining relative order of non-zeros?
A: Create new array
B: Two pointers: one for non-zero position, one iterating
C: Sort
D: Swap adjacent

✔ Correct Answer: B

Reason: Pointer for next non-zero position, iterate array, when finding non-zero swap with position pointer and increment, O(n) time O(1) space.

Tag: Normal

---

### Question 961
Domain: Data Structures
Topic: String Manipulation
Subtopic: Detect Capital
Difficulty: Easy

Question: Check if word uses capitals correctly (all caps, all lowercase, or first only)?
A: Count capitals
B: Check three conditions: all upper, all lower, or first upper rest lower
C: Regex
D: Sort

✔ Correct Answer: B

Reason: Check if word equals word.upper() or word.lower() or (word[0].isupper() and word[1:].islower()), O(n) time.

Tag: Normal

---

### Question 962
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Genetic Mutation
Difficulty: Medium

Question: Minimum mutations from start to end gene (one character change, must be in bank)?
A: Try all mutations
B: BFS treating genes as graph nodes, edges for one-char difference in bank
C: DFS
D: Greedy

✔ Correct Answer: B

Reason: BFS from start gene, try all one-character mutations in bank, track visited, first to reach end is minimum, O(B*N) where B is bank size.

Tag: Normal

---

### Question 963
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Diameter of N-ary Tree
Difficulty: Medium

Question: Find diameter of N-ary tree?
A: Count all nodes
B: DFS computing height, diameter through node = sum of two largest child heights
C: Level order
D: BFS

✔ Correct Answer: B

Reason: DFS computing height of each subtree, for each node diameter through it = sum of two largest child heights, track global max, O(n).

Tag: Normal

---

### Question 964
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Predict the Winner
Difficulty: Medium

Question: Can first player win picking from array ends?
A: Greedy largest
B: DP: dp[i][j] = max advantage for current player in range [i,j]
C: Random
D: Sum comparison

✔ Correct Answer: B

Reason: DP: dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1]), first player wins if dp[0][n-1] ≥ 0, O(n²).

Tag: Normal

---

### Question 965
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Third Maximum Number
Difficulty: Easy

Question: Find third distinct maximum, return max if less than 3 distinct?
A: Sort and pick third
B: Track three maximums in single pass
C: Heap
D: Count all

✔ Correct Answer: B

Reason: Maintain three variables for top three distinct maximums, update in single pass, handle duplicates, O(n) time O(1) space.

Tag: Normal

---

### Question 966
Domain: Data Structures
Topic: String Algorithms
Subtopic: License Key Formatting
Difficulty: Easy

Question: Format license key with dashes every k characters (first group can be shorter)?
A: Insert dashes randomly
B: Remove dashes, reverse, insert every k, reverse back
C: Count characters
D: Sort

✔ Correct Answer: B

Reason: Remove existing dashes, reverse string, insert dash every k characters, reverse result, ensures first group has remainder, O(n) time.

Tag: Normal

---

### Question 967
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Find the Town Judge
Difficulty: Easy

Question: Find town judge (trusted by all n-1 people, trusts nobody)?
A: Random person
B: Count in-degree and out-degree, judge has in=n-1 and out=0
C: Highest degree
D: First person

✔ Correct Answer: B

Reason: Track trust counts: in-degree (trusted by) and out-degree (trusts), judge has in-degree = n-1 and out-degree = 0, O(n+E).

Tag: Normal

---

### Question 968
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Two Sum IV - BST
Difficulty: Easy

Question: Find if two values in BST sum to k?
A: Check all pairs
B: Inorder traversal to sorted array, two pointers
C: Level order
D: Random

✔ Correct Answer: B

Reason: Inorder traversal gives sorted array, apply two pointers from ends, O(n) time and space, or use hashset during traversal.

Tag: Normal

---

### Question 969
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Wiggle Sort II
Difficulty: Medium

Question: Rearrange array so nums[0] < nums[1] > nums[2] < nums[3]...?
A: Sort array
B: Find median, partition, interleave from ends
C: Random shuffle
D: Greedy

✔ Correct Answer: B

Reason: Find median, partition into smaller and larger, place larger elements at odd indices from end, smaller at even indices from end, O(n) average.

Tag: Normal

---

### Question 970
Domain: Data Structures
Topic: Array Techniques
Subtopic: Contains Duplicate II
Difficulty: Easy

Question: Check if duplicate exists within k distance?
A: Check all pairs
B: Sliding window with hashset of size k
C: Sort array
D: Nested loops

✔ Correct Answer: B

Reason: Maintain hashset of last k elements, if current element in set return true, slide window removing old elements, O(n) time.

Tag: Normal

---

### Question 971
Domain: Data Structures
Topic: String Manipulation
Subtopic: Add Binary
Difficulty: Easy

Question: Add two binary strings?
A: Convert to decimal
B: Iterate from right with carry, build result
C: XOR operation
D: Sort

✔ Correct Answer: B

Reason: Iterate from right to left, add corresponding bits with carry, build result string, handle different lengths and final carry, O(max(m,n)).

Tag: Normal

---

### Question 972
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Employee Importance
Difficulty: Easy

Question: Get total importance of employee and all subordinates?
A: Count employees
B: DFS/BFS from employee summing importance values
C: Sum all
D: Greedy

✔ Correct Answer: B

Reason: DFS or BFS from target employee, traverse subordinates recursively, sum importance values, O(n) time.

Tag: Normal

---

### Question 973
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Minimum Depth of Binary Tree
Difficulty: Easy

Question: Find minimum depth (root to nearest leaf)?
A: Maximum depth
B: Level order BFS, return depth at first leaf
C: DFS all paths
D: Inorder

✔ Correct Answer: B

Reason: Level order BFS, return depth when first leaf encountered (node with no children), O(n) worst case but can terminate early.

Tag: Normal

---

### Question 974
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Climbing Stairs
Difficulty: Easy

Question: Ways to climb n stairs taking 1 or 2 steps?
A: 2^n
B: Fibonacci: dp[i] = dp[i-1] + dp[i-2]
C: n
D: n!

✔ Correct Answer: B

Reason: DP: ways to reach step i = ways to reach i-1 (then 1 step) + ways to reach i-2 (then 2 steps), Fibonacci sequence, O(n).

Tag: Normal

---

### Question 975
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Missing Number
Difficulty: Easy

Question: Find missing number in [0,n] array?
A: Sort and scan
B: Sum formula: n*(n+1)/2 - array_sum, or XOR all
C: Hashset
D: Nested loops

✔ Correct Answer: B

Reason: Expected sum = n*(n+1)/2, missing = expected - actual sum, or XOR all numbers and indices, O(n) time O(1) space.

Tag: Normal

---

### Question 976
Domain: Data Structures
Topic: String Algorithms
Subtopic: Word Pattern
Difficulty: Easy

Question: Check if string follows pattern (bijective mapping)?
A: Count characters
B: Two hashmaps ensuring bijection between pattern chars and words
C: Sort both
D: Length comparison

✔ Correct Answer: B

Reason: Split string by spaces, maintain two hashmaps for bidirectional mapping between pattern characters and words, O(n) time.

Tag: Normal

---

### Question 977
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Find Center of Star Graph
Difficulty: Easy

Question: Find center node in star graph (n-1 edges from center)?
A: Highest degree node
B: Common node in first two edges
C: First node
D: Random

✔ Correct Answer: B

Reason: Star graph has one center connected to all others, center appears in every edge, check first two edges for common node, O(1) time.

Tag: Normal

---

### Question 978
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Same Tree
Difficulty: Easy

Question: Check if two binary trees are identical?
A: Count nodes
B: Recursively compare structure and values
C: Inorder comparison only
D: Level order

✔ Correct Answer: B

Reason: Recursion: both null return true, one null return false, values equal and both subtrees identical, O(n) time.

Tag: Normal

---

### Question 979
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Pascal's Triangle
Difficulty: Easy

Question: Generate first n rows of Pascal's triangle?
A: Calculate each element separately
B: Each element = sum of two elements above it
C: Binomial formula for each
D: Random

✔ Correct Answer: B

Reason: Build row by row: row[i][j] = row[i-1][j-1] + row[i-1][j], edges are 1, O(n²) time and space.

Tag: Normal

---

### Question 980
Domain: Data Structures
Topic: Array Techniques
Subtopic: Intersection of Two Arrays
Difficulty: Easy

Question: Find intersection of two arrays (unique elements)?
A: Nested loops
B: Use two hashsets, find common elements
C: Sort both
D: Merge

✔ Correct Answer: B

Reason: Convert both to sets, compute intersection, return as array, O(n+m) time and space.

Tag: Normal

---

### Question 981
Domain: Data Structures
Topic: String Manipulation
Subtopic: Valid Palindrome II
Difficulty: Easy

Question: Check if string can be palindrome after deleting at most one character?
A: Delete each and check
B: Two pointers, on mismatch try skipping left or right
C: Sort string
D: Count characters

✔ Correct Answer: B

Reason: Two pointers from ends, on mismatch try skipping left character or right character, check if either results in palindrome, O(n) time.

Tag: Normal

---

### Question 982
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Flood Fill
Difficulty: Easy

Question: Implement flood fill (change connected same-color pixels)?
A: Change all pixels
B: DFS/BFS from starting pixel changing connected same-color pixels
C: Random fill
D: Diagonal fill

✔ Correct Answer: B

Reason: DFS or BFS from starting pixel, change color and recurse to 4-connected neighbors with same original color, O(m*n) time.

Tag: Normal

---

### Question 983
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Invert Binary Tree
Difficulty: Easy

Question: How to invert binary tree (swap left and right children)?
A: Inorder traversal
B: Recursively swap left and right children
C: Level order
D: Preorder only

✔ Correct Answer: B

Reason: Recursion: swap left and right children, recursively invert both subtrees, O(n) time, can also use BFS/DFS iteratively.

Tag: Normal

---

### Question 984
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Fibonacci Number
Difficulty: Easy

Question: Most space-efficient way to compute nth Fibonacci number?
A: Recursion
B: Iterative with two variables
C: DP array
D: Matrix exponentiation

✔ Correct Answer: B

Reason: Maintain only last two values, update iteratively: a, b = b, a+b, O(n) time O(1) space, better than DP array.

Tag: Normal

---

### Question 985
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Best Time to Buy and Sell Stock
Difficulty: Easy

Question: Maximum profit with one transaction?
A: Try all pairs
B: Track minimum price seen, update max profit
C: Greedy
D: Sort prices

✔ Correct Answer: B

Reason: Single pass tracking minimum price so far, at each price compute profit = price - min, update max profit, O(n) time O(1) space.

Tag: Normal

---

### Question 986
Domain: Data Structures
Topic: String Algorithms
Subtopic: Ransom Note
Difficulty: Easy

Question: Check if ransom note can be constructed from magazine?
A: Compare lengths
B: Count character frequencies, check if magazine has enough
C: Sort both
D: Substring search

✔ Correct Answer: B

Reason: Count character frequencies in magazine, for each character in ransom note check if available and decrement, O(m+n) time.

Tag: Normal

---

### Question 987
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Number of Provinces
Difficulty: Medium

Question: Count number of provinces (connected components) in graph?
A: Count nodes
B: DFS/BFS from each unvisited node, count components
C: Count edges
D: Union-Find

✔ Correct Answer: B

Reason: DFS or BFS from each unvisited node marking component, increment count for each new component, O(n²) for adjacency matrix.

Tag: Normal

---

### Question 988
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Path Sum
Difficulty: Easy

Question: Check if root-to-leaf path with given sum exists?
A: Sum all paths
B: DFS subtracting node value, check if leaf with sum=0
C: Level order
D: Inorder

✔ Correct Answer: B

Reason: DFS passing remaining sum (sum - node.val), at leaf check if remaining sum equals node value, O(n) time.

Tag: Normal

---

### Question 989
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Counting Bits
Difficulty: Easy

Question: Count number of 1s in binary representation for 0 to n?
A: Convert each to binary
B: DP: dp[i] = dp[i>>1] + (i&1)
C: Count manually
D: Lookup table

✔ Correct Answer: B

Reason: DP: number of 1s in i = number of 1s in i/2 plus last bit (i&1), or dp[i] = dp[i & (i-1)] + 1, O(n) time.

Tag: Normal

---

### Question 990
Domain: Data Structures
Topic: Array Techniques
Subtopic: Majority Element
Difficulty: Easy

Question: Find element appearing more than n/2 times?
A: Hashmap counting
B: Boyer-Moore voting algorithm
C: Sort and pick middle
D: Nested loops

✔ Correct Answer: B

Reason: Boyer-Moore: maintain candidate and count, increment if same, decrement if different, reset candidate when count=0, O(n) time O(1) space.

Tag: Normal

---

### Question 991
Domain: Data Structures
Topic: String Manipulation
Subtopic: Longest Common Prefix
Difficulty: Easy

Question: Find longest common prefix of string array?
A: Compare all pairs
B: Compare characters at each position across all strings
C: Sort and compare first and last
D: Random

✔ Correct Answer: B

Reason: Iterate character positions, check if all strings have same character at position, stop at first mismatch, O(S) where S is sum of all characters.

Tag: Normal

---

### Question 992
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Redundant Connection II
Difficulty: Hard

Question: Find edge to remove in directed graph to make rooted tree?
A: Remove any edge
B: Check for node with two parents or cycle, handle cases
C: Remove longest edge
D: Random

✔ Correct Answer: B

Reason: Two cases: node with two parents (try removing each), or cycle (use Union-Find), handle combination, O(n) time.

Tag: Normal

---

### Question 993
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Symmetric Tree
Difficulty: Easy

Question: Check if binary tree is symmetric?
A: Compare all nodes
B: Recursively check if left subtree mirrors right subtree
C: Inorder traversal
D: Level order

✔ Correct Answer: B

Reason: Recursion: check if left.left mirrors right.right and left.right mirrors right.left, values equal, O(n) time.

Tag: Normal

---

### Question 994
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Maximum Subarray
Difficulty: Easy

Question: Find maximum sum of contiguous subarray?
A: Check all subarrays O(n²)
B: Kadane's algorithm: max_ending = max(num, max_ending + num)
C: Greedy largest elements
D: Sort

✔ Correct Answer: B

Reason: Kadane's algorithm: track max sum ending at current position, update global max, O(n) time O(1) space.

Tag: Normal

---

### Question 995
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Two Sum
Difficulty: Easy

Question: Find two indices where values sum to target?
A: Nested loops O(n²)
B: Hashmap storing value to index
C: Sort and binary search
D: Greedy

✔ Correct Answer: B

Reason: Iterate array, for each element check if (target - element) in hashmap, store current element's index, O(n) time and space.

Tag: Normal

---

### Question 996
Domain: Data Structures
Topic: String Algorithms
Subtopic: Valid Anagram
Difficulty: Easy

Question: Check if two strings are anagrams?
A: Compare lengths only
B: Count character frequencies, compare counts
C: Reverse and compare
D: Random

✔ Correct Answer: B

Reason: Count character frequencies in both strings, compare frequency maps, or sort both and compare, O(n) time with counting.

Tag: Normal

---

### Question 997
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Max Area of Island
Difficulty: Medium

Question: Find maximum area of island in binary matrix?
A: Count all 1s
B: DFS from each unvisited land cell, track max area
C: BFS
D: Greedy

✔ Correct Answer: B

Reason: DFS from each unvisited land cell, count connected land cells (island area), track maximum area found, O(m*n) time.

Tag: Normal

---

### Question 998
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Maximum Depth of Binary Tree
Difficulty: Easy

Question: Find maximum depth of binary tree?
A: Count all nodes
B: Recursively: 1 + max(left_depth, right_depth)
C: Inorder traversal
D: Count leaves

✔ Correct Answer: B

Reason: Recursion: depth of tree is 1 plus maximum depth of subtrees, base case null returns 0, O(n) time.

Tag: Normal

---

### Question 999
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: House Robber II
Difficulty: Medium

Question: Maximum money robbing circular houses (first and last adjacent)?
A: Rob all houses
B: Run House Robber twice: exclude first house, exclude last house
C: Rob every other
D: Greedy

✔ Correct Answer: B

Reason: Can't rob both first and last, run linear House Robber on [0:n-1] and [1:n], take maximum of both results, O(n) time.

Tag: Normal

---

### Question 1000
Domain: Data Structures
Topic: Array Techniques
Subtopic: Remove Duplicates from Sorted Array
Difficulty: Easy

Question: Remove duplicates in-place from sorted array, return new length?
A: Create new array
B: Two pointers: one for unique position, one iterating
C: Hashset
D: Sort again

✔ Correct Answer: B

Reason: Two pointers: slow for next unique position, fast iterating, when arr[fast] != arr[slow] copy to slow+1 and increment slow, O(n) time O(1) space.

Tag: Normal

---

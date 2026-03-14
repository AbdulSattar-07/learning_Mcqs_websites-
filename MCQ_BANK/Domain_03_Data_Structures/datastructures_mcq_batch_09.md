# Data Structures - MCQ Batch 09
## Questions 801-900

---

### Question 801
Domain: Data Structures
Topic: Trie Applications
Subtopic: Replace Words
Difficulty: Medium

Question: How to replace words with shortest root from dictionary?
A) Check each word against all roots
B) Build trie of roots, search for shortest prefix match
C) Sort dictionary
D) Hashmap

✔ Correct Answer: B

Reason: Trie of roots enables efficient prefix matching, for each word traverse trie until leaf or mismatch, O(N) where N is total characters.

Tag: Normal

---

### Question 802
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Shortest Bridge
Difficulty: Medium

Question: Find shortest bridge connecting two islands in binary matrix?
A) BFS from all cells
B) DFS to find first island, BFS to find shortest path to second
C) Count distances
D) Diagonal search

✔ Correct Answer: B

Reason: DFS marks first island, multi-source BFS from first island finds shortest distance to second island (first 1 encountered), O(n²).

Tag: Normal

---

### Question 803
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum ASCII Delete Sum
Difficulty: Medium

Question: Minimum ASCII sum of deleted characters to make two strings equal?
A) Delete all different characters
B) DP: dp[i][j] = min cost for s1[0:i] and s2[0:j]
C) Greedy delete largest
D) Count differences

✔ Correct Answer: B

Reason: DP similar to edit distance but with ASCII costs: if match dp[i][j]=dp[i-1][j-1], else min(dp[i-1][j]+ascii(s1[i]), dp[i][j-1]+ascii(s2[j])).

Tag: Normal

---

### Question 804
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Find Duplicate Subtrees
Difficulty: Medium

Question: How to find all duplicate subtrees?
A) Compare all pairs
B) Serialize each subtree, use hashmap to track occurrences
C) Inorder comparison
D) Count nodes

✔ Correct Answer: B

Reason: Post-order serialize each subtree (structure + values), use hashmap to count serializations, duplicates appear multiple times, O(n²) worst case.

Tag: Normal

---

### Question 805
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Shortest Unsorted Subarray
Difficulty: Medium

Question: Find shortest subarray to sort to make entire array sorted?
A) Sort and compare
B) Find leftmost and rightmost out-of-place elements
C) Linear scan
D) Binary search

✔ Correct Answer: B

Reason: Find min and max in middle unsorted portion, extend boundaries to include all elements that should be between min and max, O(n) time.

Tag: Normal

---

### Question 806
Domain: Data Structures
Topic: String Algorithms
Subtopic: Repeated DNA Sequences
Difficulty: Medium

Question: Find all 10-letter sequences that occur more than once in DNA string?
A) Check all substrings
B) Sliding window with hashset tracking seen and repeated
C) Sort substrings
D) Trie

✔ Correct Answer: B

Reason: Sliding window of size 10, use hashset to track seen sequences, add to result when seen second time, O(n) time.

Tag: Normal

---

### Question 807
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Reconstruct Itinerary
Difficulty: Medium

Question: Reconstruct itinerary from tickets using all tickets once, lexical order?
A) Sort tickets
B) Hierholzer's algorithm for Eulerian path with DFS
C) BFS
D) Greedy

✔ Correct Answer: B

Reason: Eulerian path problem, DFS with backtracking, visit edges in lexical order, add to result in reverse during backtracking, O(E log E).

Tag: Normal

---

### Question 808
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Partition Equal Subset Sum
Difficulty: Medium

Question: Can array be partitioned into two subsets with equal sum?
A) Try all partitions
B) DP subset sum for target = total_sum/2
C) Greedy split
D) Sort and split

✔ Correct Answer: B

Reason: If total sum odd, impossible, else DP subset sum problem for target = sum/2, dp[i] = can achieve sum i, O(n*sum).

Tag: Normal

---

### Question 809
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Path Sum III
Difficulty: Medium

Question: Count paths with given sum (not necessarily root to leaf)?
A) Check all paths O(n²)
B) DFS with prefix sum hashmap
C) Level order
D) Inorder traversal

✔ Correct Answer: B

Reason: DFS tracking prefix sums, use hashmap to count paths: if (current_sum - target) in map, those paths end at current node, O(n) time.

Tag: Normal

---

### Question 810
Domain: Data Structures
Topic: Array Techniques
Subtopic: Find All Duplicates
Difficulty: Medium

Question: Find all duplicates in array where 1 ≤ a[i] ≤ n in O(n) time O(1) space?
A) Use hashset
B) Mark visited by negating value at index a[i]-1
C) Sort array
D) Nested loops

✔ Correct Answer: B

Reason: Use array as hashmap: for each num, negate value at index num-1, if already negative it's duplicate, O(n) time O(1) space.

Tag: Normal

---

### Question 811
Domain: Data Structures
Topic: String Manipulation
Subtopic: Decode String
Difficulty: Medium

Question: Decode string like "3[a2[c]]" to "accaccacc"?
A) Recursion only
B) Stack for numbers and strings, build result
C) String replacement
D) Iteration

✔ Correct Answer: B

Reason: Stack stores previous strings and repeat counts, on '[' push current state, on ']' pop and repeat, build result incrementally, O(n) time.

Tag: Normal

---

### Question 812
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Satisfiability of Equality Equations
Difficulty: Medium

Question: Check if equality equations are satisfiable?
A) Solve algebraically
B) Union-Find: union equal variables, check if inequal variables in same set
C) Graph coloring
D) DFS

✔ Correct Answer: B

Reason: Union-Find groups equal variables, then check inequality equations, if both variables in same component, contradiction, O(n*α(n)).

Tag: Normal

---

### Question 813
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Smallest String Starting From Leaf
Difficulty: Medium

Question: Find lexicographically smallest string from leaf to root?
A) Inorder traversal
B) DFS all root-to-leaf paths, reverse and compare
C) Level order
D) Preorder

✔ Correct Answer: B

Reason: DFS tracking current path, at leaves reverse path to get leaf-to-root string, compare and track lexicographically smallest, O(n).

Tag: Normal

---

### Question 814
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Target Sum
Difficulty: Medium

Question: Count ways to assign +/- to numbers to reach target?
A) Try all combinations 2^n
B) DP subset sum: find subset with sum = (total+target)/2
C) Greedy
D) Backtracking only

✔ Correct Answer: B

Reason: Transform to subset sum: P - N = target and P + N = total, so P = (total+target)/2, count subsets with this sum, O(n*sum).

Tag: Normal

---

### Question 815
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Advantage Shuffle
Difficulty: Medium

Question: Rearrange A to maximize advantage over B (A[i] > B[i] count)?
A) Sort both
B) Greedy: sort both, use smallest A that beats B[i], else use smallest remaining
C) Random shuffle
D) Reverse A

✔ Correct Answer: B

Reason: Sort A, for each B[i] in sorted order, assign smallest A that beats it, if none assign smallest remaining A, O(n log n).

Tag: Normal

---

### Question 816
Domain: Data Structures
Topic: String Algorithms
Subtopic: Bold Words in String
Difficulty: Medium

Question: How to bold all occurrences of dictionary words in string?
A) Replace each word
B) Mark bold intervals, merge overlapping, insert tags
C) Trie search
D) Regex

✔ Correct Answer: B

Reason: Find all occurrences marking intervals, merge overlapping intervals, insert <b> and </b> tags at interval boundaries, O(N*M) where N is string length.

Tag: Normal

---

### Question 817
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimize Malware Spread
Difficulty: Hard

Question: Which node removal minimizes malware spread?
A) Remove highest degree node
B) Union-Find to find components, remove node from largest infected component
C) Remove random node
D) BFS from each

✔ Correct Answer: B

Reason: Union-Find groups connected nodes, identify infected components, removing node from largest infected component with single initial infection minimizes spread.

Tag: Normal

---

### Question 818
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Flip Equivalent Binary Trees
Difficulty: Medium

Question: Check if trees are flip equivalent (can swap children)?
A) Compare structures only
B) Recursively check if equal or flipped children are equivalent
C) Inorder comparison
D) Level order comparison

✔ Correct Answer: B

Reason: Recursively check: roots equal and ((left1 equiv left2 and right1 equiv right2) or (left1 equiv right2 and right1 equiv left2)), O(n).

Tag: Normal

---

### Question 819
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Knight Probability
Difficulty: Medium

Question: Probability knight remains on board after K moves?
A) Count all paths
B) DP: dp[k][r][c] = probability at position after k moves
C) Random simulation
D) Greedy

✔ Correct Answer: B

Reason: DP: for each position and move count, probability = sum of (prev_prob / 8) from all valid previous positions, O(K*n²) time.

Tag: Normal

---

### Question 820
Domain: Data Structures
Topic: Array Techniques
Subtopic: Shortest Subarray with Sum at Least K
Difficulty: Hard

Question: Find shortest subarray with sum ≥ K?
A) Check all subarrays
B) Prefix sum with monotonic deque
C) Two pointers
D) Binary search

✔ Correct Answer: B

Reason: Monotonic deque of prefix sums, for each position remove smaller sums from back, check front for valid subarrays, O(n) time.

Tag: Normal

---

### Question 821
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Duplicate Substring
Difficulty: Hard

Question: Find longest duplicate substring?
A) Check all substrings O(n²)
B) Binary search on length + Rabin-Karp rolling hash
C) Trie
D) Sort suffixes

✔ Correct Answer: B

Reason: Binary search on substring length, for each length use Rabin-Karp rolling hash to check if duplicate exists, O(n log n) average.

Tag: Normal

---

### Question 822
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Regions Cut By Slashes
Difficulty: Medium

Question: Count regions in grid with '/', '\', and ' '?
A) Count slashes
B) Divide each cell into 4 triangles, Union-Find
C) DFS on cells
D) BFS

✔ Correct Answer: B

Reason: Each cell divided into 4 triangles (top, right, bottom, left), union triangles based on slashes and adjacent cells, count components, O(n²).

Tag: Normal

---

### Question 823
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Smallest Subtree with All Deepest Nodes
Difficulty: Medium

Question: Find smallest subtree containing all deepest nodes?
A) Find all deepest nodes
B) Recursively return depth and LCA of deepest nodes
C) Level order
D) Preorder

✔ Correct Answer: B

Reason: Post-order return (depth, subtree_root), if left and right depths equal, current is LCA, else return deeper side, O(n) time.

Tag: Normal

---

### Question 824
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Soup Servings
Difficulty: Medium

Question: Probability of serving soup A first with given operations?
A) Simulate all scenarios
B) DP with memoization on remaining amounts
C) Calculate directly
D) Random

✔ Correct Answer: B

Reason: DP: dp[a][b] = probability A finishes first with a ml of A and b ml of B remaining, consider all operations, memoize, O(n²).

Tag: Normal

---

### Question 825
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Pancake Sorting
Difficulty: Medium

Question: Sort array using only flip(k) operation (reverse first k elements)?
A) Bubble sort
B) Find max, flip to front, flip to position, repeat
C) Merge sort
D) Quick sort

✔ Correct Answer: B

Reason: For each position from end, find max in unsorted portion, flip to front, flip to correct position, O(n²) flips.

Tag: Normal

---

### Question 826
Domain: Data Structures
Topic: String Manipulation
Subtopic: Remove Duplicate Letters
Difficulty: Medium

Question: Remove duplicate letters to get lexicographically smallest result?
A) Remove all duplicates
B) Stack with greedy removal: pop if current < top and top appears later
C) Sort characters
D) First occurrence only

✔ Correct Answer: B

Reason: Stack maintains result, for each char if smaller than top and top appears later, pop top, ensures smallest lexicographic order, O(n).

Tag: Normal

---

### Question 827
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Possible Bipartition
Difficulty: Medium

Question: Check if graph can be bipartitioned (two groups with no internal edges)?
A) Count nodes
B) Graph coloring with 2 colors using BFS/DFS
C) Check degrees
D) Sort nodes

✔ Correct Answer: B

Reason: Try to 2-color graph: assign colors to connected nodes alternately, if conflict (adjacent same color) not bipartite, O(V+E).

Tag: Normal

---

### Question 828
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Complete Binary Tree Inserter
Difficulty: Medium

Question: How to implement insert in complete binary tree maintaining completeness?
A) Insert randomly
B) Level order queue tracking nodes with available children
C) Always insert left
D) Balanced insertion

✔ Correct Answer: B

Reason: Maintain queue of nodes with available children (< 2 children), insert at front node's available position, O(1) insertion with O(n) initialization.

Tag: Normal

---

### Question 829
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Profitable Schemes
Difficulty: Hard

Question: Count schemes with at least minProfit and at most G members?
A) Try all combinations
B) DP: dp[g][p] = ways with g members and p profit
C) Greedy
D) Backtracking

✔ Correct Answer: B

Reason: DP: for each crime, update dp[g][p] considering adding crime with its members and profit, sum dp[g][minProfit:] for all g, O(n*G*P).

Tag: Normal

---

### Question 830
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Minimum Domino Rotations
Difficulty: Medium

Question: Minimum rotations to make all dominoes show same value?
A) Try all values
B) Check if top[0] or bottom[0] can fill entire row, count swaps
C) Sort dominoes
D) Greedy

✔ Correct Answer: B

Reason: Only top[0] or bottom[0] can be answer, for each check if appears in every domino, count rotations needed, O(n) time.

Tag: Normal

---

### Question 831
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest String Chain
Difficulty: Medium

Question: Find longest chain where each word is predecessor of next (one letter added)?
A) Check all pairs
B) Sort by length, DP on each word checking predecessors
C) Trie
D) Greedy

✔ Correct Answer: B

Reason: Sort words by length, for each word try removing each character, check if predecessor exists in DP map, update chain length, O(n*L²).

Tag: Normal

---

### Question 832
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Shortest Path Visiting All Nodes
Difficulty: Hard

Question: Shortest path visiting all nodes in undirected graph (can revisit)?
A) DFS all paths
B) BFS with state (visited_set, current_node)
C) Dijkstra
D) Greedy nearest

✔ Correct Answer: B

Reason: BFS with state as (bitmask of visited nodes, current node), start from all nodes, find first state with all nodes visited, O(2^n * n²).

Tag: Normal

---

### Question 833
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Tree Coloring Game
Difficulty: Medium

Question: Can second player win tree coloring game?
A) Always
B) Check if second player can control larger subtree by blocking first player's node
C) Never
D) Random

✔ Correct Answer: B

Reason: Second player wins if can control > n/2 nodes, check three regions: left subtree, right subtree, and parent side of first player's node.

Tag: Normal

---

### Question 834
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Number of Longest Increasing Subsequence
Difficulty: Medium

Question: Count number of LIS (not just length)?
A) Generate all subsequences
B) DP: track both length and count at each position
C) Backtracking
D) Greedy

✔ Correct Answer: B

Reason: DP: lengths[i] = LIS length ending at i, counts[i] = number of LIS ending at i, update both arrays, sum counts where length is max.

Tag: Normal

---

### Question 835
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Largest Plus Sign
Difficulty: Medium

Question: Find largest plus sign of 1s in binary matrix?
A) Check all centers
B) Precompute consecutive 1s in 4 directions, min is plus size
C) DFS
D) Count 1s

✔ Correct Answer: B

Reason: For each cell, compute consecutive 1s in left, right, up, down directions, plus size = min of four directions, O(n²) time.

Tag: Normal

---

### Question 836
Domain: Data Structures
Topic: String Algorithms
Subtopic: Shortest Way to Form String
Difficulty: Medium

Question: Minimum subsequences of source to form target?
A) Greedy matching
B) For each char in target, find in source from last position, increment count on wrap
C) DP
D) Sort strings

✔ Correct Answer: B

Reason: Greedy: match target characters in source sequentially, when can't find next char in remaining source, start new subsequence, O(m*n).

Tag: Normal

---

### Question 837
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimum Cost to Connect Sticks
Difficulty: Medium

Question: Minimum cost to connect n sticks (cost = sum of lengths)?
A) Connect in order
B) Min heap: always connect two smallest sticks
C) Connect largest first
D) Random

✔ Correct Answer: B

Reason: Greedy with min heap: always merge two smallest sticks (like Huffman coding), minimizes total cost, O(n log n) time.

Tag: Normal

---

### Question 838
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Maximum Difference Between Node and Ancestor
Difficulty: Medium

Question: Find maximum |node.val - ancestor.val|?
A) Compare all pairs
B) DFS tracking min and max in path, compute difference at leaves
C) Level order
D) Inorder

✔ Correct Answer: B

Reason: DFS passing min and max values seen in current path, at each node update max difference with current min/max, O(n) time.

Tag: Normal

---

### Question 839
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Falling Path Sum
Difficulty: Medium

Question: Minimum sum of falling path in matrix (move down, down-left, down-right)?
A) Greedy down
B) DP: dp[i][j] = min path sum to position (i,j)
C) DFS all paths
D) Diagonal sum

✔ Correct Answer: B

Reason: DP: dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]), answer is min of last row, O(n²).

Tag: Normal

---

### Question 840
Domain: Data Structures
Topic: Array Techniques
Subtopic: Online Stock Span
Difficulty: Medium

Question: How to calculate stock span (consecutive days with price ≤ today)?
A) Check all previous days
B) Monotonic stack storing (price, span) pairs
C) Array scan
D) Heap

✔ Correct Answer: B

Reason: Stack maintains decreasing prices, pop smaller prices accumulating spans, push current with accumulated span, O(1) amortized per query.

Tag: Normal

---

### Question 841
Domain: Data Structures
Topic: String Manipulation
Subtopic: Minimum Add to Make Parentheses Valid
Difficulty: Medium

Question: Minimum insertions to make parentheses valid?
A) Count all parentheses
B) Track unmatched opening and closing counts
C) Stack size
D) String length

✔ Correct Answer: B

Reason: Track open count, increment on '(', decrement on ')' if open > 0 else increment close count, answer = open + close, O(n) time.

Tag: Normal

---

### Question 842
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Loud and Rich
Difficulty: Medium

Question: Find quietest person among richer people (including self)?
A) Check all people
B) DFS/BFS on reverse graph (richer → person), track minimum quiet
C) Sort by richness
D) Greedy

✔ Correct Answer: B

Reason: Build reverse graph (if a richer than b, edge b→a), DFS from each person finding minimum quiet value in reachable nodes, O(V+E).

Tag: Normal

---

### Question 843
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Construct Quad Tree
Difficulty: Medium

Question: How to construct quad tree from 2D grid?
A) Linear construction
B) Recursively divide into 4 quadrants, create leaf if all same
C) Level order
D) Random division

✔ Correct Answer: B

Reason: Recursively divide grid into 4 quadrants, if all values same create leaf, else create internal node with 4 children, O(n² log n).

Tag: Normal

---

### Question 844
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Best Time to Buy and Sell Stock IV
Difficulty: Hard

Question: Maximum profit with at most K transactions?
A) Try all combinations
B) DP: dp[k][i] = max profit with k transactions by day i
C) Greedy K largest gains
D) Sort prices

✔ Correct Answer: B

Reason: DP with states for each transaction: buy and sell, if k ≥ n/2 reduce to unlimited transactions, O(n*k) time.

Tag: Normal

---

### Question 845
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Koko Eating Bananas
Difficulty: Medium

Question: Minimum eating speed to finish all bananas in H hours?
A) Try all speeds
B) Binary search on speed, check if feasible
C) Greedy average
D) Sort piles

✔ Correct Answer: B

Reason: Binary search on speed [1, max(piles)], for each speed check if sum(ceil(pile/speed)) ≤ H, O(n log m) where m is max pile.

Tag: Normal

---

### Question 846
Domain: Data Structures
Topic: String Algorithms
Subtopic: Expressive Words
Difficulty: Medium

Question: Check if word can be stretched to match query (extend consecutive chars)?
A) String comparison
B) Two pointers checking groups, group in query must be ≥ 3 or equal
C) Count characters
D) Sort

✔ Correct Answer: B

Reason: Compare character groups, for each group in word, corresponding query group must have ≥ 3 chars or exact match, O(n) time.

Tag: Normal

---

### Question 847
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Most Stones Removed
Difficulty: Medium

Question: Maximum stones removable (remove if shares row or column with another)?
A) Remove all
B) Union-Find: stones in same row/column connected, remove all but one per component
C) Greedy
D) BFS

✔ Correct Answer: B

Reason: Union-Find connects stones sharing row or column, can remove all but one stone per component, answer = total - components, O(n).

Tag: Normal

---

### Question 848
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Longest Univalue Path
Difficulty: Medium

Question: Find longest path with same values in binary tree?
A) DFS all paths
B) Post-order: compute longest univalue path through each node
C) Level order
D) Inorder

✔ Correct Answer: B

Reason: Post-order: for each node, if child has same value extend path, path through node = left_length + right_length, track global max, O(n).

Tag: Normal

---

### Question 849
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Swaps to Make Sequences Increasing
Difficulty: Hard

Question: Minimum swaps to make both arrays strictly increasing?
A) Try all swaps
B) DP: track min swaps with/without swapping at position i
C) Greedy swap
D) Sort

✔ Correct Answer: B

Reason: DP: keep[i] = min swaps without swapping i, swap[i] = min swaps with swapping i, consider previous states and constraints, O(n).

Tag: Normal

---

### Question 850
Domain: Data Structures
Topic: Array Techniques
Subtopic: Car Fleet
Difficulty: Medium

Question: How many car fleets reach destination?
A) Count cars
B) Sort by position, calculate time to destination, count decreasing times
C) Simulate movement
D) Greedy

✔ Correct Answer: B

Reason: Sort cars by position, compute time to reach destination, iterate from end, if car takes longer than previous it forms new fleet, O(n log n).

Tag: Normal

---
### Question 851
Domain: Data Structures
Topic: String Algorithms
Subtopic: Consecutive Characters
Difficulty: Easy

Question: Find length of longest consecutive same character?
A) Nested loops
B) Single pass tracking current character and count
C) Sort string
D) Hashmap

✔ Correct Answer: B

Reason: Iterate string tracking current character and its count, update max when character changes, O(n) time O(1) space.

Tag: Normal

---

### Question 852
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Sentence Similarity II
Difficulty: Medium

Question: Check if two sentences are similar with transitive word pairs?
A) Direct comparison
B) Union-Find on word pairs, check if corresponding words connected
C) Hashmap
D) Sort words

✔ Correct Answer: B

Reason: Union-Find groups similar words transitively, check if each word pair in sentences belongs to same component, O(n*α(n)).

Tag: Normal

---

### Question 853
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Insufficient Nodes in Root to Leaf Paths
Difficulty: Medium

Question: Remove nodes where all root-to-leaf paths through them have sum < limit?
A) Remove all small values
B) Post-order: remove if both children removed and path sum < limit
C) Level order removal
D) Preorder removal

✔ Correct Answer: B

Reason: Post-order traversal: recursively process children, if leaf and path sum < limit return null, if both children null and not leaf return null, O(n).

Tag: Normal

---

### Question 854
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Cost For Tickets
Difficulty: Medium

Question: Minimum cost for train tickets (1-day, 7-day, 30-day passes)?
A) Buy daily passes
B) DP: dp[i] = min cost to cover days up to i
C) Greedy longest pass
D) Buy monthly only

✔ Correct Answer: B

Reason: DP: for each day, try all pass types, dp[i] = min(dp[i-1]+cost1, dp[i-7]+cost7, dp[i-30]+cost30), O(n) time.

Tag: Normal

---

### Question 855
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Minimum Number of Arrows
Difficulty: Medium

Question: Minimum arrows to burst all balloons (arrow at x bursts [start, end] if start ≤ x ≤ end)?
A) One arrow per balloon
B) Sort by end, greedy shoot at end of first, skip overlapping
C) Sort by start
D) Binary search

✔ Correct Answer: B

Reason: Sort intervals by end, shoot arrow at end of first balloon, skip all overlapping balloons, repeat, O(n log n) time.

Tag: Normal

---

### Question 856
Domain: Data Structures
Topic: String Manipulation
Subtopic: Shifting Letters
Difficulty: Medium

Question: Shift string where each position shifted by sum of shifts[i:n]?
A) Shift each position separately
B) Compute suffix sum of shifts, apply to each character
C) Shift randomly
D) Sort shifts

✔ Correct Answer: B

Reason: Compute suffix sum of shifts array, apply cumulative shift to each character with modulo 26, O(n) time.

Tag: Normal

---

### Question 857
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Couples Holding Hands
Difficulty: Hard

Question: Minimum swaps to make couples sit together?
A) Try all swaps
B) Union-Find or cycle detection: each swap fixes one couple
C) Greedy nearest
D) Sort couples

✔ Correct Answer: B

Reason: Model as graph where couples are nodes, edges connect mismatched couples, each cycle of length k needs k-1 swaps, O(n).

Tag: Normal

---

### Question 858
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Smallest String Starting From Leaf
Difficulty: Medium

Question: What traversal order is needed for leaf-to-root strings?
A) Preorder
B) DFS with path tracking, reverse at leaves
C) Level order
D) Inorder

✔ Correct Answer: B

Reason: DFS maintains current path from root, at leaves reverse path to get leaf-to-root string, compare all such strings, O(n).

Tag: Normal

---

### Question 859
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Tallest Billboard
Difficulty: Hard

Question: Maximum height of billboard with equal support rods on both sides?
A) Try all partitions
B) DP: dp[diff] = max height with difference diff between sides
C) Greedy tallest
D) Sort rods

✔ Correct Answer: B

Reason: DP on difference between two sides: dp[diff] = max sum of one side with this difference, answer is dp[0], O(n*sum) time.

Tag: Normal

---

### Question 860
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Fruit Into Baskets
Difficulty: Medium

Question: Maximum fruits collected with two baskets (longest subarray with 2 distinct values)?
A) Check all subarrays
B) Sliding window with hashmap tracking two types
C) Greedy
D) Sort fruits

✔ Correct Answer: B

Reason: Sliding window maintaining at most 2 fruit types in hashmap, expand right, contract left when > 2 types, track max length, O(n).

Tag: Normal

---

### Question 861
Domain: Data Structures
Topic: String Algorithms
Subtopic: Orderly Queue
Difficulty: Hard

Question: Smallest string after K rotations (move first K chars to end in any order)?
A) Try all rotations
B) If K=1 try all rotations, if K≥2 sort string
C) Reverse string
D) Random

✔ Correct Answer: B

Reason: K=1 allows only rotations, try all n rotations, K≥2 allows any permutation (bubble sort possible), return sorted string, O(n²) or O(n log n).

Tag: Normal

---

### Question 862
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Reorder Routes
Difficulty: Medium

Question: Minimum edge reversals so all cities reach city 0?
A) Reverse all edges
B) DFS from 0, count edges going away from 0
C) BFS
D) Count degrees

✔ Correct Answer: B

Reason: DFS from city 0, track original edge directions, count edges pointing away from 0 (need reversal), O(n) time.

Tag: Normal

---

### Question 863
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Delete Nodes and Return Forest
Difficulty: Medium

Question: Delete nodes and return remaining trees as forest?
A) Delete and rebuild
B) Post-order: if node deleted, children become roots
C) Level order deletion
D) Preorder deletion

✔ Correct Answer: B

Reason: Post-order traversal: process children first, if current node deleted add non-null children to result, return null, O(n) time.

Tag: Normal

---

### Question 864
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Pizza With 3n Slices
Difficulty: Hard

Question: Maximum sum picking n slices where adjacent slices can't be picked (circular)?
A) Greedy largest
B) DP: reduce to house robber on circular array, try twice
C) Pick every third
D) Random

✔ Correct Answer: B

Reason: Similar to house robber II (circular), run twice: exclude first slice, exclude last slice, take maximum, O(n²) with k=n/3 picks.

Tag: Normal

---

### Question 865
Domain: Data Structures
Topic: Array Techniques
Subtopic: Maximum Sum Circular Subarray
Difficulty: Medium

Question: Maximum sum of circular subarray?
A) Check all subarrays
B) Max of (Kadane's max, total - Kadane's min)
C) Sum all elements
D) Greedy

✔ Correct Answer: B

Reason: Circular max is either normal max subarray or total - min subarray (wraps around), use Kadane for both, handle all negative case, O(n).

Tag: Normal

---

### Question 866
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Chunked Palindrome
Difficulty: Hard

Question: Maximum chunks in palindrome decomposition (greedy shortest chunks)?
A) Check all decompositions
B) Two pointers from ends, match shortest equal chunks
C) DP
D) Divide in half

✔ Correct Answer: B

Reason: Two pointers from ends, find shortest matching prefix and suffix, increment count, recurse on middle, greedy gives maximum chunks, O(n²).

Tag: Normal

---

### Question 867
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Parallel Courses
Difficulty: Medium

Question: Minimum semesters to complete courses with prerequisites?
A) Count courses
B) Topological sort with BFS, track levels
C) DFS
D) Greedy

✔ Correct Answer: B

Reason: Topological sort using BFS (Kahn's algorithm), track level/semester for each course, answer is maximum level, detect cycle if can't complete all.

Tag: Normal

---

### Question 868
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Validate Binary Tree Nodes
Difficulty: Medium

Question: Check if edges form valid binary tree?
A) Count nodes
B) Check single root, no cycles, all nodes reachable, each node has ≤ 1 parent
C) DFS
D) Count edges

✔ Correct Answer: B

Reason: Verify: exactly one node with no parent (root), no cycles using visited set, all n nodes reachable from root, O(n) time.

Tag: Normal

---

### Question 869
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Frog Jump
Difficulty: Hard

Question: Can frog cross river jumping k-1, k, or k+1 units (last jump was k)?
A) Try all jumps
B) DP/DFS with memoization: dp[position][last_jump]
C) Greedy
D) BFS

✔ Correct Answer: B

Reason: DP state (current position, last jump size), try three next jumps, memoize, O(n²) time and space.

Tag: Normal

---

### Question 870
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Bag of Tokens
Difficulty: Medium

Question: Maximum score playing tokens face-up (cost power) or face-down (gain power)?
A) Random play
B) Sort tokens, greedy play smallest face-up, largest face-down
C) Play all face-up
D) Play all face-down

✔ Correct Answer: B

Reason: Sort tokens, two pointers: play smallest face-up to gain score, when power insufficient play largest face-down to gain power, O(n log n).

Tag: Normal

---

### Question 871
Domain: Data Structures
Topic: String Manipulation
Subtopic: Reverse Words in String III
Difficulty: Easy

Question: Reverse characters in each word but maintain word order?
A) Reverse entire string
B) Split by spaces, reverse each word, join
C) Reverse pairs
D) Stack

✔ Correct Answer: B

Reason: Split string by spaces, reverse each word individually, join back with spaces, O(n) time.

Tag: Normal

---

### Question 872
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Find Eventual Safe Nodes
Difficulty: Medium

Question: Find nodes that eventually reach terminal nodes (no outgoing edges)?
A) DFS from terminal nodes backward
B) DFS with coloring: detect cycles, safe nodes don't lead to cycles
C) BFS
D) Count edges

✔ Correct Answer: B

Reason: DFS with three colors (unvisited, visiting, safe), node safe if all neighbors safe, nodes in cycles or leading to cycles are unsafe, O(V+E).

Tag: Normal

---

### Question 873
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Leaf-Similar Trees
Difficulty: Easy

Question: Check if two trees have same leaf value sequence?
A) Compare all nodes
B) Extract leaf sequences with DFS, compare
C) Level order comparison
D) Inorder comparison

✔ Correct Answer: B

Reason: DFS to collect leaf values in order for both trees, compare sequences, O(n+m) time.

Tag: Normal

---

### Question 874
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Champagne Tower
Difficulty: Medium

Question: How much champagne in glass (query_row, query_col) after pouring?
A) Simulate pouring
B) DP: dp[r][c] = amount in glass, overflow splits to children
C) Calculate directly
D) Random

✔ Correct Answer: B

Reason: DP: pour into top, overflow = max(0, amount - 1), split equally to two children, dp[r][c] = min(1, amount), O(query_row²).

Tag: Normal

---

### Question 875
Domain: Data Structures
Topic: Array Techniques
Subtopic: Minimum Increment to Make Array Unique
Difficulty: Medium

Question: Minimum increments to make all array elements unique?
A) Increment randomly
B) Sort array, for duplicates increment to next available value
C) Hashset
D) Count duplicates

✔ Correct Answer: B

Reason: Sort array, iterate maintaining next available value, if current < next increment to next, accumulate moves, O(n log n) time.

Tag: Normal

---

### Question 876
Domain: Data Structures
Topic: String Algorithms
Subtopic: Longest Absolute File Path
Difficulty: Medium

Question: Find length of longest absolute file path?
A) Check all paths
B) Stack tracking directory depths and lengths
C) Recursion
D) Count characters

✔ Correct Answer: B

Reason: Stack stores cumulative length at each depth, on file (contains '.') compute full path length, on directory push to stack, O(n) time.

Tag: Normal

---

### Question 877
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Minimize Hamming Distance After Swap
Difficulty: Medium

Question: Minimum Hamming distance after swapping elements in allowed positions?
A) Try all swaps
B) Union-Find groups swappable positions, match optimally within groups
C) Greedy swap
D) Sort

✔ Correct Answer: B

Reason: Union-Find groups positions that can swap, within each group optimally match elements between arrays, O(n*α(n)) time.

Tag: Normal

---

### Question 878
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Maximum Level Sum
Difficulty: Medium

Question: Find level with maximum sum in binary tree?
A) Sum all nodes
B) Level order traversal computing sum at each level
C) DFS
D) Preorder sum

✔ Correct Answer: B

Reason: Level order traversal (BFS), compute sum of nodes at each level, track level with maximum sum, O(n) time.

Tag: Normal

---

### Question 879
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Arithmetic Subsequence
Difficulty: Medium

Question: Find length of longest arithmetic subsequence?
A) Check all subsequences
B) DP: dp[i][diff] = length of arithmetic seq ending at i with difference diff
C) Greedy
D) Sort array

✔ Correct Answer: B

Reason: DP with hashmap at each position tracking (difference → length), for each pair update dp[j][diff], O(n²) time.

Tag: Normal

---

### Question 880
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Smallest Range Covering K Lists
Difficulty: Hard

Question: Find smallest range covering at least one element from each of k sorted lists?
A) Merge all lists
B) Min heap with k elements, track max, update range
C) Binary search
D) Two pointers

✔ Correct Answer: B

Reason: Min heap with one element from each list, track current max, range = [heap.min, max], pop min and add next from its list, O(n log k).

Tag: Normal

---

### Question 881
Domain: Data Structures
Topic: String Algorithms
Subtopic: Camelcase Matching
Difficulty: Medium

Question: Check if query matches pattern with lowercase insertions?
A) String comparison
B) Two pointers: match uppercase exactly, skip lowercase in query
C) Regex
D) Sort

✔ Correct Answer: B

Reason: Two pointers: uppercase in query must match pattern exactly in order, lowercase in query can be skipped, O(n) time per query.

Tag: Normal

---

### Question 882
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Escape Large Maze
Difficulty: Hard

Question: Can reach target in large grid with blocked cells?
A) BFS entire grid
B) BFS limited steps (blocked cells can trap in area ≤ n*(n-1)/2)
C) DFS
D) Dijkstra

✔ Correct Answer: B

Reason: Blocked cells can trap in area at most n*(n-1)/2 where n is blocked count, BFS limited steps from both source and target, O(n²).

Tag: Normal

---

### Question 883
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Construct BST from Preorder
Difficulty: Medium

Question: How to construct BST from preorder traversal?
A) Sort and build
B) Recursively: first element is root, split by value into left/right
C) Inorder construction
D) Level order

✔ Correct Answer: B

Reason: First element is root, elements < root go to left subtree, elements > root go to right, recursively build, O(n) with bounds optimization.

Tag: Normal

---

### Question 884
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Minimum Difficulty of Job Schedule
Difficulty: Hard

Question: Minimum difficulty scheduling jobs over d days (difficulty = max job in day)?
A) Divide equally
B) DP: dp[i][j] = min difficulty for first i jobs in j days
C) Greedy
D) Random

✔ Correct Answer: B

Reason: DP: dp[i][j] = min over k of (dp[k][j-1] + max(jobs[k:i])), O(n²*d) time, can optimize with monotonic stack.

Tag: Normal

---

### Question 885
Domain: Data Structures
Topic: Array Techniques
Subtopic: Maximum Points from Cards
Difficulty: Medium

Question: Maximum points taking k cards from either end?
A) Take from larger end
B) Sliding window: try all combinations of left and right cards
C) Greedy largest
D) Binary search

✔ Correct Answer: B

Reason: Try all splits: i cards from left, k-i from right, compute sum for each, track maximum, O(k) time with prefix sums.

Tag: Normal

---

### Question 886
Domain: Data Structures
Topic: String Manipulation
Subtopic: Check If Word Occurs As Prefix
Difficulty: Easy

Question: Return index of first word having searchWord as prefix?
A) Check all words
B) Split sentence, iterate checking startsWith
C) Trie
D) Sort

✔ Correct Answer: B

Reason: Split sentence by spaces, iterate checking if each word starts with searchWord, return 1-indexed position, O(n*m) time.

Tag: Normal

---

### Question 887
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Number of Enclaves
Difficulty: Medium

Question: Count land cells that can't reach boundary?
A) Count all land
B) DFS from boundary marking reachable, count unmarked land
C) BFS from center
D) Greedy

✔ Correct Answer: B

Reason: DFS from all boundary land cells marking reachable cells, count remaining unmarked land cells, O(m*n) time.

Tag: Normal

---

### Question 888
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Sum of Distances in Tree
Difficulty: Hard

Question: For each node, sum of distances to all other nodes?
A) BFS from each node O(n²)
B) Two DFS: compute subtree info, then re-root to get answers
C) Level order
D) Preorder

✔ Correct Answer: B

Reason: First DFS computes subtree sizes and distances, second DFS re-roots tree updating distances using parent's answer, O(n) time.

Tag: Normal

---

### Question 889
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Number of Ways to Stay in Same Place
Difficulty: Hard

Question: Ways to stay at index 0 after exactly steps moves (left/right/stay)?
A) Try all paths
B) DP: dp[i][j] = ways to be at position i after j steps
C) Calculate directly
D) Greedy

✔ Correct Answer: B

Reason: DP: dp[i][j] = dp[i-1][j-1] + dp[i][j-1] + dp[i+1][j-1], base case dp[0][0]=1, answer is dp[0][steps], O(steps*n).

Tag: Normal

---

### Question 890
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Maximum Subarray Sum with One Deletion
Difficulty: Medium

Question: Maximum subarray sum allowing one element deletion?
A) Try deleting each element
B) DP: track max sum with 0 and 1 deletions
C) Kadane's algorithm
D) Greedy

✔ Correct Answer: B

Reason: DP: no_del[i] = max sum ending at i with no deletion, one_del[i] = max sum ending at i with one deletion, O(n) time O(1) space.

Tag: Normal

---

### Question 891
Domain: Data Structures
Topic: String Manipulation
Subtopic: Remove All Adjacent Duplicates II
Difficulty: Medium

Question: Remove k consecutive duplicate characters repeatedly?
A) Iterate removing pairs
B) Stack storing (char, count), pop when count reaches k
C) Recursion
D) Sort

✔ Correct Answer: B

Reason: Stack maintains (character, count) pairs, increment count for same char, pop when count = k, rebuild string from stack, O(n) time.

Tag: Normal

---

### Question 892
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Time Needed to Inform All Employees
Difficulty: Medium

Question: Time for manager to inform all employees in tree hierarchy?
A) Count employees
B) DFS computing max time from root to leaves
C) BFS
D) Sum all times

✔ Correct Answer: B

Reason: DFS from manager (root), for each node time = informTime[node] + max(time of children), O(n) time.

Tag: Normal

---

### Question 893
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Deepest Leaves Sum
Difficulty: Medium

Question: Sum of values at deepest level?
A) Sum all nodes
B) Level order traversal, sum last level
C) DFS tracking depth
D) Preorder sum

✔ Correct Answer: B

Reason: Level order traversal, keep summing current level, last level sum is answer, or DFS tracking max depth and sum, O(n) time.

Tag: Normal

---

### Question 894
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Arithmetic Subsequence of Given Difference
Difficulty: Medium

Question: Longest arithmetic subsequence with specific difference d?
A) Check all subsequences
B) DP: dp[num] = length of longest seq ending at num
C) Greedy
D) Sort array

✔ Correct Answer: B

Reason: DP with hashmap: dp[num] = dp[num-d] + 1, track maximum length, O(n) time and space.

Tag: Normal

---

### Question 895
Domain: Data Structures
Topic: Array Techniques
Subtopic: Minimum Moves to Equal Array Elements II
Difficulty: Medium

Question: Minimum moves to make all elements equal (increment or decrement one element)?
A) Move to average
B) Move all to median
C) Move to max
D) Move to min

✔ Correct Answer: B

Reason: Median minimizes sum of absolute deviations, find median, sum |arr[i] - median| for all elements, O(n log n) with sorting.

Tag: Normal

---

### Question 896
Domain: Data Structures
Topic: String Algorithms
Subtopic: Number of Matching Subsequences
Difficulty: Medium

Question: Count words that are subsequences of string s?
A) Check each word separately
B) Bucket words by first char, advance pointers as chars seen
C) Trie
D) Sort

✔ Correct Answer: B

Reason: Group words by next expected character, iterate s advancing words waiting for current char, O(n + total word length) time.

Tag: Normal

---

### Question 897
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Keys and Rooms
Difficulty: Medium

Question: Can visit all rooms starting from room 0 with keys?
A) Count rooms
B) DFS/BFS from room 0 collecting keys, check if all rooms visited
C) Check keys only
D) Greedy

✔ Correct Answer: B

Reason: DFS/BFS from room 0, collect keys and visit corresponding rooms, check if visited count equals total rooms, O(n+k) where k is total keys.

Tag: Normal

---

### Question 898
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Search Tree Iterator
Difficulty: Medium

Question: How to implement BST iterator with O(h) space?
A) Store all nodes in array
B) Stack for controlled inorder traversal
C) Recursion
D) Queue

✔ Correct Answer: B

Reason: Stack maintains path to current node, next() pops node, pushes right subtree's left path, O(h) space, O(1) amortized time per next().

Tag: Normal

---

### Question 899
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Stone Game II
Difficulty: Medium

Question: Maximum stones first player can get with M parameter (take 1 to 2M piles)?
A) Greedy
B) DP with memoization: dp[i][M] = max stones from position i with parameter M
C) Take all
D) Random

✔ Correct Answer: B

Reason: DP: try taking X piles (1 ≤ X ≤ 2M), opponent plays optimally on remaining, dp[i][M] = max over X of (suffix_sum - dp[i+X][max(M,X)]).

Tag: Normal

---

### Question 900
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Maximize Distance to Closest Person
Difficulty: Medium

Question: Maximum distance to closest person when sitting in empty seat?
A) Try all seats
B) Find largest gap between people, consider ends
C) Sit in middle
D) Random

✔ Correct Answer: B

Reason: Find all gaps between occupied seats, max distance = max(gap/2 for middle gaps, gap for end gaps), O(n) time.

Tag: Normal

---

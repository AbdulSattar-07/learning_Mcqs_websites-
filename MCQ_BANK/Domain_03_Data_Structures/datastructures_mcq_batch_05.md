# Data Structures - MCQ Batch 05
## Questions 401-500

---

### Question 401
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Splay Tree
Difficulty: Hard

Question: What is the key operation in splay trees?
A) Rotation
B) Splaying (moving accessed node to root)
C) Balancing
D) Coloring

✔ Correct Answer: B

Reason: Splay trees move recently accessed nodes to root through rotations (splaying), providing amortized O(log n) operations with good cache performance.

Tag: Normal

---

### Question 402
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Treap
Difficulty: Hard

Question: What two properties does a treap maintain?
A) Color and size
B) BST property by key, heap property by priority
C) Height and balance
D) Weight and depth

✔ Correct Answer: B

Reason: Treap combines binary search tree (ordered by keys) and heap (ordered by random priorities), providing probabilistic balancing.

Tag: Normal

---

### Question 403
Domain: Data Structures
Topic: String Matching
Subtopic: Boyer-Moore
Difficulty: Hard

Question: What makes Boyer-Moore algorithm efficient?
A) Compares left to right
B) Bad character and good suffix heuristics skip comparisons
C) Uses hashing
D) Compares all characters

✔ Correct Answer: B

Reason: Boyer-Moore uses bad character and good suffix rules to skip sections of text, often achieving sublinear time in practice.

Tag: Normal

---

### Question 404
Domain: Data Structures
Topic: String Matching
Subtopic: Z-Algorithm
Difficulty: Hard

Question: What does the Z-array store?
A) Character frequencies
B) Length of longest substring starting at i matching prefix
C) Hash values
D) Character positions

✔ Correct Answer: B

Reason: Z-algorithm computes Z-array where Z[i] is length of longest substring starting at i that matches prefix, enabling O(n+m) pattern matching.

Tag: Normal

---

### Question 405
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Cartesian Tree
Difficulty: Hard

Question: What properties does a Cartesian tree satisfy?
A) Only BST property
B) Heap property and in-order gives original sequence
C) Only heap property
D) No specific properties

✔ Correct Answer: B

Reason: Cartesian tree satisfies heap property (parent < children) and in-order traversal gives original sequence, useful for range minimum queries.

Tag: Normal

---

### Question 406
Domain: Data Structures
Topic: Range Queries
Subtopic: Sparse Table
Difficulty: Hard

Question: What is the query time complexity of sparse table for range minimum query?
A) O(1)
B) O(log n)
C) O(n)
D) O(√n)

✔ Correct Answer: A

Reason: Sparse table precomputes answers for power-of-2 ranges, enabling O(1) query by combining two overlapping ranges, with O(n log n) preprocessing.

Tag: Normal

---

### Question 407
Domain: Data Structures
Topic: Range Queries
Subtopic: Square Root Decomposition
Difficulty: Hard

Question: What is the query time complexity of square root decomposition?
A) O(1)
B) O(√n)
C) O(log n)
D) O(n)

✔ Correct Answer: B

Reason: Array divided into √n blocks. Query processes at most 2 partial blocks and √n complete blocks: O(√n).

Tag: Normal

---

### Question 408
Domain: Data Structures
Topic: Code Analysis
Subtopic: Kadane's Algorithm
Difficulty: Medium

```python
def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))
```
What is the output?
A) 4
B) 6
C) 7
D) 10

✔ Correct Answer: B

Reason: Maximum subarray is [4, -1, 2, 1] with sum 6. Kadane's algorithm finds this in O(n) time.

Tag: Past Paper

---

### Question 409
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Common Subsequence
Difficulty: Hard

Question: What is the time complexity of LCS using dynamic programming?
A) O(n)
B) O(n + m)
C) O(n * m)
D) O(2ⁿ)

✔ Correct Answer: C

Reason: LCS DP fills an (n+1)×(m+1) table where n and m are string lengths, requiring O(n*m) time and space.

Tag: Past Paper

---

### Question 410
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Edit Distance
Difficulty: Hard

Question: What operations are allowed in edit distance (Levenshtein distance)?
A) Insert only
B) Insert, delete, replace
C) Replace only
D) Delete only

✔ Correct Answer: B

Reason: Edit distance counts minimum operations (insert, delete, replace) to transform one string to another, computed using DP in O(n*m).

Tag: Normal

---


### Question 411
Domain: Data Structures
Topic: Code Analysis
Subtopic: LCS Implementation
Difficulty: Hard

```java
public static int lcs(String s1, String s2) {
    int m = s1.length(), n = s2.length();
    int[][] dp = new int[m+1][n+1];
    
    for(int i = 1; i <= m; i++) {
        for(int j = 1; j <= n; j++) {
            if(s1.charAt(i-1) == s2.charAt(j-1))
                dp[i][j] = dp[i-1][j-1] + 1;
            else
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
        }
    }
    return dp[m][n];
}

System.out.println(lcs("ABCD", "ACBD"));
```
What is the output?
A) 2
B) 3
C) 4
D) 0

✔ Correct Answer: B

Reason: LCS of "ABCD" and "ACBD" is "ABD" with length 3. Characters A, B, D appear in order in both strings.

Tag: Normal

---

### Question 412
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Knapsack Problem
Difficulty: Hard

Question: What is the time complexity of 0/1 knapsack using DP?
A) O(n)
B) O(n * W) where W is capacity
C) O(2ⁿ)
D) O(n²)

✔ Correct Answer: B

Reason: 0/1 knapsack DP fills table of size n×W where n is items and W is capacity, giving O(n*W) pseudo-polynomial time.

Tag: Past Paper

---

### Question 413
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Coin Change
Difficulty: Medium

Question: What type of DP problem is coin change (minimum coins)?
A) Linear DP
B) Unbounded knapsack variant
C) Tree DP
D) String DP

✔ Correct Answer: B

Reason: Coin change is an unbounded knapsack variant where each coin can be used unlimited times, solved with DP in O(amount * coins).

Tag: Normal

---

### Question 414
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Longest Increasing Subsequence
Difficulty: Hard

Question: What is the optimal time complexity for LIS problem?
A) O(n²)
B) O(n log n)
C) O(n)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: LIS can be solved in O(n²) with DP, but optimized to O(n log n) using binary search with patience sorting approach.

Tag: Normal

---

### Question 415
Domain: Data Structures
Topic: Code Analysis
Subtopic: LIS DP
Difficulty: Hard

```python
def lis_length(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis_length(arr))
```
What is the output?
A) 3
B) 4
C) 5
D) 6

✔ Correct Answer: B

Reason: LIS is [2, 3, 7, 18] or [2, 3, 7, 101] or [2, 5, 7, 18] etc., all with length 4.

Tag: Normal

---

### Question 416
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Matrix Chain Multiplication
Difficulty: Hard

Question: What does matrix chain multiplication DP optimize?
A) Matrix values
B) Order of multiplication to minimize operations
C) Matrix size
D) Storage

✔ Correct Answer: B

Reason: MCM finds optimal parenthesization order to minimize scalar multiplications, using DP in O(n³) time.

Tag: Past Paper

---

### Question 417
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Palindrome Partitioning
Difficulty: Hard

Question: What is the time complexity of finding minimum cuts for palindrome partitioning using DP?
A) O(n)
B) O(n²)
C) O(n³)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: DP approach precomputes palindrome table in O(n²), then finds minimum cuts in O(n²), total O(n²).

Tag: Normal

---

### Question 418
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bipartite Graph
Difficulty: Medium

Question: How can you check if a graph is bipartite?
A) Count vertices
B) 2-color using BFS/DFS
C) Count edges
D) Check connectivity

✔ Correct Answer: B

Reason: Graph is bipartite if and only if it can be 2-colored (no adjacent vertices same color), checked using BFS/DFS in O(V+E).

Tag: Normal

---

### Question 419
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

Reason: Articulation point (cut vertex) is a vertex whose removal disconnects the graph or increases number of connected components.

Tag: Normal

---

### Question 420
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bridges
Difficulty: Hard

Question: What is a bridge in a graph?
A) Longest edge
B) Edge whose removal increases connected components
C) Shortest edge
D) Heaviest edge

✔ Correct Answer: B

Reason: Bridge (cut edge) is an edge whose removal disconnects the graph, found using DFS with low and discovery times.

Tag: Normal

---

### Question 421
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Eulerian Path
Difficulty: Hard

Question: When does an undirected graph have an Eulerian path?
A) Always
B) Exactly 0 or 2 vertices with odd degree
C) All vertices even degree
D) Never

✔ Correct Answer: B

Reason: Eulerian path exists if exactly 0 (Eulerian circuit) or 2 vertices have odd degree. All others must have even degree.

Tag: Past Paper

---

### Question 422
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Hamiltonian Path
Difficulty: Hard

Question: What is the complexity of determining if Hamiltonian path exists?
A) O(n)
B) O(n²)
C) NP-complete
D) O(n log n)

✔ Correct Answer: C

Reason: Hamiltonian path problem (visiting each vertex exactly once) is NP-complete, no known polynomial-time algorithm exists.

Tag: Normal

---

### Question 423
Domain: Data Structures
Topic: Network Flow
Subtopic: Max Flow
Difficulty: Hard

Question: What is the time complexity of Ford-Fulkerson with BFS (Edmonds-Karp)?
A) O(V * E)
B) O(V * E²)
C) O(V²)
D) O(E²)

✔ Correct Answer: B

Reason: Edmonds-Karp (Ford-Fulkerson with BFS) runs in O(V*E²) time, finding augmenting paths in O(E) with at most O(VE) iterations.

Tag: Normal

---

### Question 424
Domain: Data Structures
Topic: Network Flow
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

### Question 425
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Counting Sort
Difficulty: Medium

Question: When is counting sort most efficient?
A) Large range of values
B) Small range of non-negative integers
C) Floating point numbers
D) Strings

✔ Correct Answer: B

Reason: Counting sort is O(n+k) where k is range. Efficient when k is O(n), but impractical for large ranges requiring excessive space.

Tag: Normal

---

### Question 426
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Radix Sort
Difficulty: Hard

Question: What is the time complexity of radix sort for n integers with d digits?
A) O(n)
B) O(d * n)
C) O(n log n)
D) O(n²)

✔ Correct Answer: B

Reason: Radix sort processes d digits, using counting sort for each digit in O(n), total O(d*n) where d is number of digits.

Tag: Normal

---

### Question 427
Domain: Data Structures
Topic: Sorting Algorithms
Subtopic: Bucket Sort
Difficulty: Medium

Question: When does bucket sort achieve O(n) time complexity?
A) Always
B) When input is uniformly distributed
C) Never
D) For sorted input

✔ Correct Answer: B

Reason: Bucket sort is O(n) on average when input is uniformly distributed across buckets. Worst case O(n²) if all elements in one bucket.

Tag: Normal

---

### Question 428
Domain: Data Structures
Topic: Code Analysis
Subtopic: Counting Sort
Difficulty: Medium

```cpp
#include <iostream>
#include <vector>
using namespace std;

void countingSort(vector<int>& arr) {
    int max_val = *max_element(arr.begin(), arr.end());
    vector<int> count(max_val + 1, 0);
    
    for(int num : arr)
        count[num]++;
    
    int idx = 0;
    for(int i = 0; i <= max_val; i++) {
        while(count[i]-- > 0)
            arr[idx++] = i;
    }
}

int main() {
    vector<int> arr = {4, 2, 2, 8, 3, 3, 1};
    countingSort(arr);
    cout << arr[3];
}
```
What is the output?
A) 2
B) 3
C) 4
D) 8

✔ Correct Answer: B

Reason: Sorted array: [1, 2, 2, 3, 3, 4, 8]. arr[3] = 3.

Tag: Normal

---

### Question 429
Domain: Data Structures
Topic: Selection Algorithms
Subtopic: Quickselect
Difficulty: Hard

Question: What is the average time complexity of quickselect for finding kth smallest element?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(k)

✔ Correct Answer: A

Reason: Quickselect has average O(n) by partitioning and recursing on one side only, though worst case is O(n²).

Tag: Normal

---

### Question 430
Domain: Data Structures
Topic: Selection Algorithms
Subtopic: Median of Medians
Difficulty: Hard

Question: What guarantee does median of medians provide?
A) Average O(n)
B) Worst-case O(n) for selection
C) O(log n) always
D) No guarantee

✔ Correct Answer: B

Reason: Median of medians algorithm guarantees worst-case O(n) time for selection by choosing good pivot, unlike quickselect's O(n²) worst case.

Tag: Normal

---

### Question 431
Domain: Data Structures
Topic: Code Analysis
Subtopic: Partition
Difficulty: Medium

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
pivot_idx = partition(arr, 0, 5)
print(arr[pivot_idx])
```
What is the output?
A) 1
B) 5
C) 7
D) 10

✔ Correct Answer: B

Reason: Pivot is 5. After partition, elements ≤5 are left of pivot. Pivot ends at its sorted position with value 5.

Tag: Normal

---

### Question 432
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Morris Traversal
Difficulty: Hard

Question: What is the space complexity of Morris traversal?
A) O(1)
B) O(log n)
C) O(n)
D) O(n log n)

✔ Correct Answer: A

Reason: Morris traversal uses threaded binary tree concept to traverse without stack/recursion, achieving O(1) space complexity.

Tag: Normal

---

### Question 433
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Lowest Common Ancestor
Difficulty: Hard

Question: What is the time complexity of LCA query using binary lifting after preprocessing?
A) O(1)
B) O(log n)
C) O(n)
D) O(√n)

✔ Correct Answer: B

Reason: Binary lifting preprocesses ancestors in O(n log n), then answers LCA queries in O(log n) by jumping up in powers of 2.

Tag: Normal

---

### Question 434
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Diameter
Difficulty: Medium

Question: How to find diameter of a tree efficiently?
A) Check all pairs
B) Two DFS/BFS passes
C) Sort vertices
D) Use heap

✔ Correct Answer: B

Reason: Find farthest node from any node using DFS/BFS, then find farthest from that node. Second distance is diameter. O(n) time.

Tag: Normal

---

### Question 435
Domain: Data Structures
Topic: Code Analysis
Subtopic: Tree Diameter
Difficulty: Hard

```python
def tree_diameter(adj, n):
    def bfs(start):
        visited = [False] * n
        queue = [(start, 0)]
        visited[start] = True
        farthest = (start, 0)
        
        while queue:
            node, dist = queue.pop(0)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
                    if dist + 1 > farthest[1]:
                        farthest = (neighbor, dist + 1)
        
        return farthest
    
    node, _ = bfs(0)
    _, diameter = bfs(node)
    return diameter

adj = [
    [1, 2],      # 0
    [0, 3, 4],   # 1
    [0],         # 2
    [1],         # 3
    [1]          # 4
]
print(tree_diameter(adj, 5))
```
What is the output?
A) 2
B) 3
C) 4
D) 5

✔ Correct Answer: B

Reason: Tree structure: 2-0-1-3 and 1-4. Longest path is 2-0-1-3 or 2-0-1-4 or 3-1-4, all length 3.

Tag: Normal

---

### Question 436
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Manacher's Algorithm
Difficulty: Hard

Question: What problem does Manacher's algorithm solve?
A) Sorting
B) Longest palindromic substring in O(n)
C) Pattern matching
D) Graph traversal

✔ Correct Answer: B

Reason: Manacher's algorithm finds longest palindromic substring in linear O(n) time using clever expansion around centers with memoization.

Tag: Normal

---

### Question 437
Domain: Data Structures
Topic: Advanced Algorithms
Subtopic: Aho-Corasick
Difficulty: Hard

Question: What does Aho-Corasick algorithm do?
A) Single pattern matching
B: Multiple pattern matching simultaneously
C) Sorting
D) Hashing

✔ Correct Answer: B

Reason: Aho-Corasick builds automaton from multiple patterns, finding all occurrences of all patterns in O(n + m + z) where z is matches.

Tag: Normal

---

### Question 438
Domain: Data Structures
Topic: Computational Geometry
Subtopic: Convex Hull
Difficulty: Hard

Question: What is the time complexity of Graham scan for convex hull?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(n³)

✔ Correct Answer: B

Reason: Graham scan sorts points by polar angle O(n log n), then processes in O(n), total O(n log n).

Tag: Normal

---

### Question 439
Domain: Data Structures
Topic: Computational Geometry
Subtopic: Line Intersection
Difficulty: Hard

Question: How to check if two line segments intersect?
A) Distance calculation
B) Orientation test and boundary checks
C) Slope comparison only
D) Midpoint check

✔ Correct Answer: B

Reason: Check if segments straddle each other using orientation tests (clockwise/counterclockwise) and handle boundary cases.

Tag: Normal

---

### Question 440
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Persistent Data Structures
Difficulty: Hard

Question: What is a persistent data structure?
A) Stored on disk
B) Preserves previous versions after modifications
C) Never changes
D) Temporary structure

✔ Correct Answer: B

Reason: Persistent data structures preserve all previous versions when modified, enabling access to historical states, using structural sharing for efficiency.

Tag: Normal

---

### Question 441
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Rope Data Structure
Difficulty: Hard

Question: What operations does rope data structure optimize?
A) Searching
B) String concatenation and substring operations
C) Sorting
D) Hashing

✔ Correct Answer: B

Reason: Rope represents strings as binary tree of smaller strings, enabling O(log n) concatenation and substring operations vs O(n) for arrays.

Tag: Normal

---

### Question 442
Domain: Data Structures
Topic: Code Analysis
Subtopic: Binary Search Variation
Difficulty: Hard

```cpp
#include <iostream>
#include <vector>
using namespace std;

int searchRotated(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    
    while(left <= right) {
        int mid = left + (right - left) / 2;
        
        if(arr[mid] == target) return mid;
        
        if(arr[left] <= arr[mid]) {
            if(target >= arr[left] && target < arr[mid])
                right = mid - 1;
            else
                left = mid + 1;
        } else {
            if(target > arr[mid] && target <= arr[right])
                left = mid + 1;
            else
                right = mid - 1;
        }
    }
    return -1;
}

int main() {
    vector<int> arr = {4, 5, 6, 7, 0, 1, 2};
    cout << searchRotated(arr, 0);
}
```
What is the output?
A) -1
B) 0
C) 4
D) 7

✔ Correct Answer: C

Reason: Array rotated at index 4. Binary search finds 0 at index 4 in O(log n) time.

Tag: Normal

---

### Question 443
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Dutch National Flag
Difficulty: Hard

Question: What problem does Dutch National Flag algorithm solve?
A) Sorting any array
B) Partitioning array into three parts (0s, 1s, 2s)
C) Binary search
D) Finding duplicates

✔ Correct Answer: B

Reason: Dutch National Flag algorithm partitions array with three values (0, 1, 2) in single pass using three pointers: O(n) time, O(1) space.

Tag: Normal

---

### Question 444
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Majority Element
Difficulty: Hard

Question: What is the time complexity of Boyer-Moore majority vote algorithm?
A) O(1)
B) O(n)
C) O(n log n)
D) O(n²)

✔ Correct Answer: B

Reason: Boyer-Moore finds majority element (appears >n/2 times) in O(n) time and O(1) space using voting mechanism.

Tag: Normal

---

### Question 445
Domain: Data Structures
Topic: Code Analysis
Subtopic: Majority Element
Difficulty: Medium

```python
def find_majority(arr):
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate

arr = [2, 2, 1, 1, 1, 2, 2]
print(find_majority(arr))
```
What is the output?
A) 1
B) 2
C) None
D) 0

✔ Correct Answer: B

Reason: Boyer-Moore voting: 2 appears 4 times (>7/2), is majority. Algorithm correctly identifies 2 as candidate.

Tag: Normal

---

### Question 446
Domain: Data Structures
Topic: Array Algorithms
Subtopic: Trapping Rain Water
Difficulty: Hard

Question: What is the optimal space complexity for trapping rain water problem?
A) O(1)
B) O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: A

Reason: Two-pointer approach solves in O(n) time and O(1) space by maintaining left and right max heights while moving pointers.

Tag: Normal

---

### Question 447
Domain: Data Structures
Topic: Stack Applications
Subtopic: Largest Rectangle
Difficulty: Hard

Question: What is the time complexity of finding largest rectangle in histogram using stack?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(n³)

✔ Correct Answer: A

Reason: Using monotonic stack, each bar is pushed and popped at most once, achieving O(n) time complexity.

Tag: Normal

---

### Question 448
Domain: Data Structures
Topic: Code Analysis
Subtopic: Stock Span
Difficulty: Medium

```java
import java.util.*;

public class StockSpan {
    public static int[] calculateSpan(int[] prices) {
        int n = prices.length;
        int[] span = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i < n; i++) {
            while(!stack.isEmpty() && prices[stack.peek()] <= prices[i])
                stack.pop();
            
            span[i] = stack.isEmpty() ? (i + 1) : (i - stack.peek());
            stack.push(i);
        }
        
        return span;
    }
    
    public static void main(String[] args) {
        int[] prices = {100, 80, 60, 70, 60, 75, 85};
        int[] span = calculateSpan(prices);
        System.out.println(span[6]);
    }
}
```
What is the output?
A) 1
B) 3
C) 6
D) 7

✔ Correct Answer: C

Reason: For price 85 at index 6, span counts consecutive days with price ≤85: 85,75,60,70,60,80 = 6 days.

Tag: Normal

---

### Question 449
Domain: Data Structures
Topic: Interval Problems
Subtopic: Merge Intervals
Difficulty: Medium

Question: What is the time complexity of merging overlapping intervals?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(1)

✔ Correct Answer: B

Reason: Sort intervals by start time O(n log n), then merge in single pass O(n), total O(n log n).

Tag: Normal

---

### Question 450
Domain: Data Structures
Topic: Interval Problems
Subtopic: Meeting Rooms
Difficulty: Medium

Question: How to find minimum meeting rooms required?
A) Count all meetings
B) Track overlapping intervals using events or heap
C) Random assignment
D) Sort by duration

✔ Correct Answer: B

Reason: Sort start/end times as events or use min-heap to track ongoing meetings, finding maximum concurrent meetings: O(n log n).

Tag: Normal

---


### Question 451
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Cycle Detection
Difficulty: Hard

Question: In Floyd's cycle detection, if slow and fast pointers meet, where should you start to find cycle start?
A) From meeting point
B) From head and meeting point, moving one step each
C) From head only
D) Random position

✔ Correct Answer: B

Reason: After meeting, start one pointer from head and one from meeting point, both moving one step. They meet at cycle start.

Tag: Past Paper

---

### Question 452
Domain: Data Structures
Topic: Linked List Algorithms
Subtopic: Intersection Point
Difficulty: Hard

Question: How to find intersection point of two linked lists efficiently?
A) Nested loops
B) Calculate lengths, align, then traverse together
C) Sort lists
D) Use hash table only

✔ Correct Answer: B

Reason: Calculate lengths, move longer list's pointer by difference, then traverse both together. They meet at intersection: O(m+n) time, O(1) space.

Tag: Normal

---

### Question 453
Domain: Data Structures
Topic: Code Analysis
Subtopic: List Intersection
Difficulty: Hard

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_intersection(headA, headB):
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA

# List A: 1->2->3->4
# List B: 5->3->4 (intersects at 3)
# What happens?
```
What is the key insight?
A) Lists never meet
B) Pointers traverse equal total distance
C) Random meeting
D) Always meet at head

✔ Correct Answer: B

Reason: Each pointer traverses both lists. If intersection exists, they meet there after equal distance (lenA + lenB - common).

Tag: Normal

---

### Question 454
Domain: Data Structures
Topic: Stack Applications
Subtopic: Min Stack
Difficulty: Hard

Question: How to implement a stack that supports getMin() in O(1)?
A) Sort stack
B) Maintain auxiliary stack tracking minimums
C) Linear search
D) Use heap

✔ Correct Answer: B

Reason: Maintain auxiliary stack where each element stores minimum up to that point, enabling O(1) getMin while maintaining O(1) push/pop.

Tag: Normal

---

### Question 455
Domain: Data Structures
Topic: Queue Applications
Subtopic: Deque
Difficulty: Medium

Question: What operations does a deque support?
A) Push/pop from one end only
B) Push/pop from both ends
C) Random access only
D) Middle insertion only

✔ Correct Answer: B

Reason: Deque (double-ended queue) supports O(1) insertion and deletion from both front and rear, more flexible than stack or queue.

Tag: Normal

---

### Question 456
Domain: Data Structures
Topic: Code Analysis
Subtopic: Deque Application
Difficulty: Hard

```cpp
#include <iostream>
#include <deque>
#include <vector>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> result;
    
    for(int i = 0; i < nums.size(); i++) {
        if(!dq.empty() && dq.front() == i - k)
            dq.pop_front();
        
        while(!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();
        
        dq.push_back(i);
        
        if(i >= k - 1)
            result.push_back(nums[dq.front()]);
    }
    
    return result;
}

int main() {
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    vector<int> res = maxSlidingWindow(nums, 3);
    cout << res[0] << " " << res[res.size()-1];
}
```
What is the output?
A) 1 7
B) 3 7
C) 3 6
D) 5 7

✔ Correct Answer: B

Reason: First window [1,3,-1] max=3. Last window [3,6,7] max=7. Output: 3 7.

Tag: Normal

---

### Question 457
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Serialize/Deserialize
Difficulty: Hard

Question: What traversal is commonly used for tree serialization?
A) In-order only
B) Pre-order or level-order with null markers
C) Post-order only
D) Random order

✔ Correct Answer: B

Reason: Pre-order or level-order with null markers allows unambiguous reconstruction. In-order alone is ambiguous without structure information.

Tag: Normal

---

### Question 458
Domain: Data Structures
Topic: Binary Tree
Subtopic: Views
Difficulty: Medium

Question: What is the right view of a binary tree?
A) All right children
B) Rightmost node at each level
C) All nodes on right
D) Root only

✔ Correct Answer: B

Reason: Right view shows rightmost visible node at each level when viewing tree from right side, found using level-order traversal.

Tag: Normal

---

### Question 459
Domain: Data Structures
Topic: Binary Tree
Subtopic: Vertical Order
Difficulty: Hard

Question: How to print vertical order traversal of binary tree?
A) In-order traversal
B) Assign horizontal distance, group by distance
C) Level-order only
D) Pre-order traversal

✔ Correct Answer: B

Reason: Assign horizontal distance (left child: hd-1, right child: hd+1), group nodes by distance, print each group top to bottom.

Tag: Normal

---

### Question 460
Domain: Data Structures
Topic: Code Analysis
Subtopic: Tree Path Sum
Difficulty: Medium

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == targetSum
    
    return (hasPathSum(root.left, targetSum - root.val) or 
            hasPathSum(root.right, targetSum - root.val))

# Tree:     5
#          / \
#         4   8
#        /   / \
#       11  13  4
#      /  \      \
#     7    2      1

# hasPathSum(root, 22) returns?
```
What does it return?
A) True (path 5->4->11->2)
B) False
C) None
D) Error

✔ Correct Answer: A

Reason: Path 5→4→11→2 sums to 22. Function returns True.

Tag: Normal

---

### Question 461
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Tarjan's Algorithm
Difficulty: Hard

Question: What does Tarjan's algorithm find in O(V+E)?
A) Shortest paths
B) Strongly connected components
C) Minimum spanning tree
D) Maximum flow

✔ Correct Answer: B

Reason: Tarjan's algorithm finds strongly connected components in single DFS pass using low-link values and stack: O(V+E).

Tag: Normal

---

### Question 462
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Kosaraju's Algorithm
Difficulty: Hard

Question: How many DFS passes does Kosaraju's algorithm require?
A) 1
B) 2
C) 3
D) V

✔ Correct Answer: B

Reason: Kosaraju's uses two DFS passes: first on original graph to get finish times, second on transposed graph in reverse finish order.

Tag: Normal

---

### Question 463
Domain: Data Structures
Topic: Trie Variations
Subtopic: Compressed Trie
Difficulty: Hard

Question: What is a compressed trie (radix tree)?
A) Encrypted trie
B) Trie with chains of single-child nodes compressed
C) Smaller trie
D) Faster trie

✔ Correct Answer: B

Reason: Compressed trie merges chains of nodes with single child into one edge, reducing space while maintaining functionality.

Tag: Normal

---

### Question 464
Domain: Data Structures
Topic: Trie Applications
Subtopic: Longest Common Prefix
Difficulty: Medium

Question: How can trie help find longest common prefix of strings?
A) Sort strings
B) Insert all, traverse from root until branching
C) Compare all pairs
D) Use hash table

✔ Correct Answer: B

Reason: Insert all strings in trie, then traverse from root until node has multiple children or is end. Path is longest common prefix.

Tag: Normal

---

### Question 465
Domain: Data Structures
Topic: Heap Applications
Subtopic: K Largest Elements
Difficulty: Medium

Question: What is the optimal approach to find k largest elements in array of size n?
A) Sort entire array
B) Use min-heap of size k
C) Use max-heap of size n
D) Linear search

✔ Correct Answer: B

Reason: Maintain min-heap of size k. For each element, if larger than heap min, replace it. Final heap has k largest: O(n log k).

Tag: Normal

---

### Question 466
Domain: Data Structures
Topic: Heap Applications
Subtopic: Median Stream
Difficulty: Hard

Question: How to find median of a stream efficiently?
A) Sort after each insertion
B) Use two heaps (max-heap for lower half, min-heap for upper half)
C) Use single heap
D) Use array

✔ Correct Answer: B

Reason: Maintain max-heap for lower half and min-heap for upper half, balancing sizes. Median is at heap roots: O(log n) insert, O(1) median.

Tag: Normal

---

### Question 467
Domain: Data Structures
Topic: Code Analysis
Subtopic: Kth Largest
Difficulty: Medium

```python
import heapq

def findKthLargest(nums, k):
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

nums = [3, 2, 1, 5, 6, 4]
print(findKthLargest(nums, 2))
```
What is the output?
A) 2
B) 4
C) 5
D) 6

✔ Correct Answer: C

Reason: 2nd largest element is 5. Min-heap of size 2 maintains two largest elements, root is 2nd largest.

Tag: Normal

---

### Question 468
Domain: Data Structures
Topic: Graph Coloring
Subtopic: Chromatic Number
Difficulty: Hard

Question: What is the chromatic number of a complete graph Kn?
A) 2
B) n-1
C) n
D) n+1

✔ Correct Answer: C

Reason: Complete graph Kn requires n colors as every vertex is adjacent to all others, needing unique color for each.

Tag: Normal

---

### Question 469
Domain: Data Structures
Topic: Graph Coloring
Subtopic: Bipartite
Difficulty: Medium

Question: What is the chromatic number of a bipartite graph?
A) 1
B) 2
C) 3
D) Depends on size

✔ Correct Answer: B

Reason: Bipartite graphs can be 2-colored by definition (vertices divided into two independent sets), so chromatic number is 2.

Tag: Normal

---

### Question 470
Domain: Data Structures
Topic: Tree Algorithms
Subtopic: Binary Lifting
Difficulty: Hard

Question: What is the preprocessing time for binary lifting?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: Binary lifting precomputes 2^i-th ancestor for each node up to log n levels, requiring O(n log n) time and space.

Tag: Normal

---


### Question 471
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Power of Two
Difficulty: Easy

Question: How to check if a number is power of 2 using bit manipulation?
A) n % 2 == 0
B) n & (n-1) == 0 and n != 0
C) n | (n-1) == 0
D) n ^ (n-1) == 0

✔ Correct Answer: B

Reason: Power of 2 has exactly one set bit. n & (n-1) clears rightmost set bit, result is 0 only for powers of 2.

Tag: Normal

---

### Question 472
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Count Set Bits
Difficulty: Easy

Question: What is the time complexity of Brian Kernighan's algorithm for counting set bits?
A) O(1)
B) O(log n)
C) O(number of set bits)
D) O(n)

✔ Correct Answer: C

Reason: n & (n-1) clears rightmost set bit. Algorithm loops only for each set bit, making it O(k) where k is set bits.

Tag: Normal

---

### Question 473
Domain: Data Structures
Topic: Code Analysis
Subtopic: Bit Manipulation
Difficulty: Medium

```cpp
#include <iostream>
using namespace std;

int countSetBits(int n) {
    int count = 0;
    while(n) {
        n = n & (n - 1);
        count++;
    }
    return count;
}

int main() {
    cout << countSetBits(15);
}
```
What is the output?
A) 3
B) 4
C) 15
D) 1

✔ Correct Answer: B

Reason: 15 in binary is 1111, which has 4 set bits. Brian Kernighan's algorithm counts them.

Tag: Normal

---

### Question 474
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: XOR Properties
Difficulty: Medium

Question: What is the result of a ^ a for any integer a?
A) a
B) 0
C) 1
D) 2a

✔ Correct Answer: B

Reason: XOR of a number with itself is always 0 because each bit cancels out (1^1=0, 0^0=0).

Tag: Normal

---

### Question 475
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Single Number
Difficulty: Medium

Question: How to find the single non-duplicate number in array where every other number appears twice?
A) Sort array
B) XOR all elements
C) Use hash map
D) Count frequencies

✔ Correct Answer: B

Reason: XOR all elements. Duplicates cancel out (a^a=0), leaving only the single number: O(n) time, O(1) space.

Tag: Normal

---

### Question 476
Domain: Data Structures
Topic: Code Analysis
Subtopic: XOR Application
Difficulty: Easy

```python
def find_single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4, 1, 2, 1, 2]
print(find_single(nums))
```
What is the output?
A) 0
B) 1
C) 2
D) 4

✔ Correct Answer: D

Reason: 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4. Duplicates cancel, leaving 4.

Tag: Normal

---

### Question 477
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Subset Generation
Difficulty: Hard

Question: How many subsets does a set of n elements have?
A) n
B) n²
C) 2ⁿ
D) n!

✔ Correct Answer: C

Reason: Each element can be included or excluded (2 choices), giving 2ⁿ total subsets including empty set.

Tag: Past Paper

---

### Question 478
Domain: Data Structures
Topic: Bit Manipulation
Subtopic: Bit Masking
Difficulty: Hard

Question: How to check if ith bit is set in number n?
A) n & (1 << i)
B) n | (1 << i)
C) n ^ (1 << i)
D) n >> i

✔ Correct Answer: A

Reason: (1 << i) creates mask with only ith bit set. n & (1 << i) is non-zero if ith bit is set in n.

Tag: Normal

---

### Question 479
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Subset Sum
Difficulty: Hard

Question: What is the time complexity of subset sum problem using DP?
A) O(n)
B) O(n * sum)
C) O(2ⁿ)
D) O(n²)

✔ Correct Answer: B

Reason: DP table of size n×sum where n is array size and sum is target. Pseudo-polynomial O(n*sum) time complexity.

Tag: Past Paper

---

### Question 480
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Partition Problem
Difficulty: Hard

Question: How is partition problem related to subset sum?
A) Unrelated
B) Partition is subset sum with target = total_sum/2
C) Partition is easier
D) Partition is sorting

✔ Correct Answer: B

Reason: Partition problem asks if array can be divided into two equal sum subsets, equivalent to finding subset with sum = total_sum/2.

Tag: Normal

---

### Question 481
Domain: Data Structures
Topic: Code Analysis
Subtopic: Subset Sum DP
Difficulty: Hard

```java
public static boolean subsetSum(int[] arr, int sum) {
    int n = arr.length;
    boolean[][] dp = new boolean[n+1][sum+1];
    
    for(int i = 0; i <= n; i++)
        dp[i][0] = true;
    
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= sum; j++) {
            dp[i][j] = dp[i-1][j];
            if(j >= arr[i-1])
                dp[i][j] = dp[i][j] || dp[i-1][j-arr[i-1]];
        }
    }
    
    return dp[n][sum];
}

int[] arr = {3, 34, 4, 12, 5, 2};
System.out.println(subsetSum(arr, 9));
```
What is the output?
A) true (subset: 4, 5)
B) false
C) Error
D) null

✔ Correct Answer: A

Reason: Subset {4, 5} sums to 9. DP correctly identifies this subset exists.

Tag: Normal

---

### Question 482
Domain: Data Structures
Topic: String Algorithms
Subtopic: Suffix Array
Difficulty: Hard

Question: What is the space complexity of suffix array?
A) O(1)
B) O(n)
C) O(n²)
D) O(n log n)

✔ Correct Answer: B

Reason: Suffix array stores starting indices of all n suffixes, requiring O(n) space. Can be built in O(n log n) or O(n) time.

Tag: Normal

---

### Question 483
Domain: Data Structures
Topic: String Algorithms
Subtopic: LCP Array
Difficulty: Hard

Question: What does LCP array store in context of suffix arrays?
A) Character frequencies
B) Longest common prefix between consecutive suffixes
C) String lengths
D) Hash values

✔ Correct Answer: B

Reason: LCP array stores length of longest common prefix between adjacent suffixes in sorted suffix array, useful for pattern matching.

Tag: Normal

---

### Question 484
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Fenwick Tree 2D
Difficulty: Hard

Question: What is the update time complexity of 2D Fenwick tree?
A) O(1)
B) O(log n)
C) O(log² n)
D) O(n)

✔ Correct Answer: C

Reason: 2D Fenwick tree updates by iterating through log n rows and log n columns, giving O(log² n) for both update and query.

Tag: Normal

---

### Question 485
Domain: Data Structures
Topic: Advanced Trees
Subtopic: Segment Tree 2D
Difficulty: Hard

Question: What is the space complexity of 2D segment tree for n×m matrix?
A) O(n*m)
B) O(4*n*m)
C) O(n+m)
D) O(log n * log m)

✔ Correct Answer: B

Reason: 2D segment tree requires 4×n×m space for complete tree structure, supporting range queries on 2D matrices.

Tag: Normal

---

### Question 486
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: A* Search
Difficulty: Hard

Question: What makes A* search different from Dijkstra's algorithm?
A) Uses BFS
B) Uses heuristic function to guide search
C) Only works on trees
D) Slower than Dijkstra

✔ Correct Answer: B

Reason: A* uses heuristic h(n) estimating distance to goal, evaluating f(n) = g(n) + h(n) to prioritize promising paths, often faster than Dijkstra.

Tag: Normal

---

### Question 487
Domain: Data Structures
Topic: Graph Algorithms
Subtopic: Bidirectional Search
Difficulty: Hard

Question: What is the advantage of bidirectional search?
A) Simpler implementation
B) Reduces search space from O(b^d) to O(b^(d/2))
C) Always faster
D) Uses less memory

✔ Correct Answer: B

Reason: Bidirectional search runs from start and goal simultaneously, meeting in middle. Reduces branching factor exponentially: O(b^(d/2)) vs O(b^d).

Tag: Normal

---

### Question 488
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Skip List
Difficulty: Hard

Question: What is the average time complexity of search in skip list?
A) O(1)
B) O(log n)
C) O(n)
D) O(√n)

✔ Correct Answer: B

Reason: Skip list uses probabilistic balancing with multiple levels, achieving O(log n) average time for search, insert, delete.

Tag: Normal

---

### Question 489
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Bloom Filter
Difficulty: Hard

Question: What is a key characteristic of Bloom filter?
A) No false positives or negatives
B) Possible false positives, no false negatives
C) Possible false negatives, no false positives
D) Both false positives and negatives

✔ Correct Answer: B

Reason: Bloom filter is probabilistic data structure that may report element exists when it doesn't (false positive), but never misses existing elements.

Tag: Normal

---

### Question 490
Domain: Data Structures
Topic: Advanced Data Structures
Subtopic: Count-Min Sketch
Difficulty: Hard

Question: What does Count-Min Sketch provide?
A) Exact frequency counts
B) Approximate frequency counts with overestimation
C) Exact median
D) Sorting

✔ Correct Answer: B

Reason: Count-Min Sketch uses multiple hash functions and counters to approximate frequencies, may overestimate but never underestimate.

Tag: Normal

---

### Question 491
Domain: Data Structures
Topic: Code Analysis
Subtopic: Sliding Window Maximum
Difficulty: Hard

```python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
res = maxSlidingWindow(nums, 3)
print(len(res))
```
What is the output?
A) 3
B) 5
C) 6
D) 8

✔ Correct Answer: C

Reason: Array has 8 elements, window size 3. Number of windows = 8-3+1 = 6. Result has 6 maximums.

Tag: Normal

---

### Question 492
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Egg Drop
Difficulty: Hard

Question: What is the time complexity of egg drop problem using DP?
A) O(n)
B) O(k*n²) where k is eggs, n is floors
C) O(n²)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: DP table of size k×n, each cell requires O(n) trials to compute minimum, giving O(k*n²) time complexity.

Tag: Past Paper

---

### Question 493
Domain: Data Structures
Topic: Dynamic Programming
Subtopic: Word Break
Difficulty: Hard

Question: What is the time complexity of word break problem using DP?
A) O(n)
B) O(n²)
C) O(n³)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: DP checks all substrings: outer loop O(n), inner loop O(n) for each position, total O(n²) with dictionary lookup.

Tag: Normal

---

### Question 494
Domain: Data Structures
Topic: Code Analysis
Subtopic: Word Break DP
Difficulty: Hard

```python
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[n]

s = "leetcode"
wordDict = {"leet", "code"}
print(wordBreak(s, wordDict))
```
What is the output?
A) True
B) False
C) None
D) Error

✔ Correct Answer: A

Reason: "leetcode" can be segmented as "leet" + "code", both in dictionary. DP returns True.

Tag: Normal

---

### Question 495
Domain: Data Structures
Topic: Greedy Algorithms
Subtopic: Activity Selection
Difficulty: Medium

Question: What is the greedy choice for activity selection problem?
A) Longest duration
B) Earliest start time
C) Earliest finish time
D) Latest start time

✔ Correct Answer: C

Reason: Selecting activity with earliest finish time maximizes remaining time for other activities, giving optimal solution.

Tag: Past Paper

---

### Question 496
Domain: Data Structures
Topic: Greedy Algorithms
Subtopic: Huffman Coding
Difficulty: Hard

Question: What data structure is used to build Huffman tree?
A) Stack
B) Min-heap (priority queue)
C) Max-heap
D) Array

✔ Correct Answer: B

Reason: Huffman coding uses min-heap to repeatedly extract two minimum frequency nodes and merge them, building optimal prefix-free code.

Tag: Normal

---

### Question 497
Domain: Data Structures
Topic: Code Analysis
Subtopic: Activity Selection
Difficulty: Medium

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Activity {
    int start, finish;
};

bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

int maxActivities(vector<Activity>& activities) {
    sort(activities.begin(), activities.end(), compare);
    
    int count = 1;
    int lastFinish = activities[0].finish;
    
    for(int i = 1; i < activities.size(); i++) {
        if(activities[i].start >= lastFinish) {
            count++;
            lastFinish = activities[i].finish;
        }
    }
    
    return count;
}

int main() {
    vector<Activity> activities = {{1,3}, {2,5}, {4,6}, {6,7}, {5,8}, {8,9}};
    cout << maxActivities(activities);
}
```
What is the output?
A) 2
B) 3
C) 4
D) 6

✔ Correct Answer: C

Reason: Greedy selection: (1,3), (4,6), (6,7), (8,9) = 4 non-overlapping activities.

Tag: Normal

---

### Question 498
Domain: Data Structures
Topic: Greedy Algorithms
Subtopic: Fractional Knapsack
Difficulty: Medium

Question: What is the time complexity of fractional knapsack?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(2ⁿ)

✔ Correct Answer: B

Reason: Sort items by value/weight ratio O(n log n), then greedily pick items. Unlike 0/1 knapsack, greedy works for fractional.

Tag: Normal

---

### Question 499
Domain: Data Structures
Topic: Backtracking
Subtopic: N-Queens
Difficulty: Hard

Question: What is the time complexity of N-Queens problem?
A) O(n!)
B) O(n²)
C) O(2ⁿ)
D) O(n)

✔ Correct Answer: A

Reason: N-Queens uses backtracking with approximately O(n!) time as it tries placing queens in different positions with pruning.

Tag: Past Paper

---

### Question 500
Domain: Data Structures
Topic: Code Analysis
Subtopic: Sudoku Solver
Difficulty: Hard

```python
def isValid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True

# What does this function do?
```
What is the purpose?
A) Solves sudoku
B) Validates if placing num at (row,col) is valid
C) Generates sudoku
D) Counts solutions

✔ Correct Answer: B

Reason: Function checks if placing num at position (row, col) violates sudoku rules (row, column, 3×3 box uniqueness).

Tag: Normal

---
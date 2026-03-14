# Programming - MCQ Batch 07
## Questions 601-700

---

### Question 601
Domain: Programming
Topic: Graph Representation
Subtopic: Adjacency Matrix
Difficulty: Medium

Question: What is adjacency matrix?
A) Matrix operations
B) 2D array where matrix[i][j] indicates edge between vertices i and j
C) Adjacent matrices
D) Sorted matrix

✔ Correct Answer: B

Reason: Adjacency matrix is 2D array representing graph. matrix[i][j]=1 if edge exists, 0 otherwise. Space O(V²), good for dense graphs.

Tag: Past Paper

---

### Question 602
Domain: Programming
Topic: Code Analysis
Subtopic: Graph Representation
Difficulty: Hard

Question: Which representation is better for sparse graph?
A) Adjacency matrix
B) Adjacency list
C) Same
D) Neither

✔ Correct Answer: B

Reason: Sparse graph has few edges. Adjacency list uses O(V+E) space. Matrix uses O(V²), wasteful for sparse graphs.

Tag: Normal

---

### Question 603
Domain: Programming
Topic: Graph Traversal
Subtopic: BFS
Difficulty: Hard

Question: What data structure does BFS use?
A) Stack
B) Queue
C) Priority queue
D) Array

✔ Correct Answer: B

Reason: BFS (Breadth-First Search) uses queue (FIFO). Explores level by level. DFS uses stack (LIFO) or recursion.

Tag: Past Paper

---

### Question 604
Domain: Programming
Topic: Graph Traversal
Subtopic: DFS
Difficulty: Hard

Question: What data structure does DFS use?
A) Queue
B) Stack (or recursion)
C: Priority queue
C) [Missing option - Please review]

D) Linked list

✔ Correct Answer: B

Reason: DFS (Depth-First Search) uses stack (explicit or implicit via recursion). Explores as deep as possible before backtracking.

Tag: Past Paper

---

### Question 605
Domain: Programming
Topic: Code Analysis
Subtopic: BFS Implementation
Difficulty: Hard

Question: What is the output for BFS starting from 0?
```python
from collections import deque

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}

def bfs(start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result

print(bfs(0))
```
A) [0, 1, 2, 3]
B) [0, 1, 2, 3] or [0, 2, 1, 3]
C) [0, 3, 2, 1]
D) Error

✔ Correct Answer: B

Reason: BFS explores level by level. From 0: visits 0, then neighbors 1,2 (order depends on insertion), then 3. Possible: [0,1,2,3] or [0,2,1,3].

Tag: Normal

---

### Question 606
Domain: Programming
Topic: Tree Traversal
Subtopic: Inorder Traversal
Difficulty: Medium

Question: What is inorder traversal order for binary tree?
A) Root, Left, Right
B) Left, Root, Right
C) Left, Right, Root
D) Right, Root, Left

✔ Correct Answer: B

Reason: Inorder: Left subtree, Root, Right subtree. For BST, gives sorted order. Preorder: Root, Left, Right. Postorder: Left, Right, Root.

Tag: Past Paper

---

### Question 607
Domain: Programming
Topic: Tree Traversal
Subtopic: Preorder Traversal
Difficulty: Medium

Question: What is preorder traversal order?
A) Left, Root, Right
B) Root, Left, Right
C) Left, Right, Root
D) Right, Left, Root

✔ Correct Answer: B

Reason: Preorder: Root, Left subtree, Right subtree. Used for creating copy of tree or prefix expression evaluation.

Tag: Past Paper

---

### Question 608
Domain: Programming
Topic: Tree Traversal
Subtopic: Postorder Traversal
Difficulty: Medium

Question: What is postorder traversal order?
A) Root, Left, Right
B) Left, Right, Root
C) Left, Root, Right
D) Right, Root, Left

✔ Correct Answer: B

Reason: Postorder: Left subtree, Right subtree, Root. Used for deleting tree or postfix expression evaluation.

Tag: Past Paper

---

### Question 609
Domain: Programming
Topic: Code Analysis
Subtopic: Tree Height
Difficulty: Hard

Question: What is the output?
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(height(root))
```
A) 2
B) 3
C) 4
D) 1

✔ Correct Answer: B

Reason: Height is longest path from root to leaf. Path: 1→2→4 has 3 nodes. Height = 3.

Tag: Normal

---

### Question 610
Domain: Programming
Topic: Binary Search Tree
Subtopic: BST Property
Difficulty: Medium

Question: What is BST property?
A) Balanced tree
B) Left subtree < root < right subtree
C) Complete tree
D) Full tree

✔ Correct Answer: B

Reason: BST property: all left subtree values < root, all right subtree values > root. Enables O(log n) search in balanced BST.

Tag: Past Paper

---

### Question 611
Domain: Programming
Topic: Code Analysis
Subtopic: BST Search
Difficulty: Hard

Question: What is time complexity of BST search in balanced tree?
A) O(n)
B) O(log n)
C) O(1)
D) O(n²)

✔ Correct Answer: B

Reason: Balanced BST has height log n. Search compares with root, goes left or right, eliminating half: O(log n). Unbalanced worst case: O(n).

Tag: Past Paper

---

### Question 612
Domain: Programming
Topic: Heap
Subtopic: Heap Property
Difficulty: Hard

Question: What is max heap property?
A) Maximum size
B) Parent >= children
C) Parent <= children
D) Sorted array

✔ Correct Answer: B

Reason: Max heap: parent value >= children values. Root is maximum. Min heap: parent <= children. Used in priority queues.

Tag: Past Paper

---

### Question 613
Domain: Programming
Topic: Code Analysis
Subtopic: heapq Module
Difficulty: Hard

Question: What is the output?
```python
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))
```
A) 3
B) 1
C) 2
D) Error

✔ Correct Answer: B

Reason: heapq implements min heap. heappop() removes and returns smallest element. Smallest is 1.

Tag: Normal

---

### Question 614
Domain: Programming
Topic: Priority Queue
Subtopic: Queue Priority
Difficulty: Medium

Question: What is priority queue?
A) Fast queue
B) Queue where elements have priorities, highest priority dequeued first
C) FIFO queue
D) Stack

✔ Correct Answer: B

Reason: Priority queue serves elements by priority, not insertion order. Implemented with heap for O(log n) operations.

Tag: Normal

---

### Question 615
Domain: Programming
Topic: Code Analysis
Subtopic: Queue Module
Difficulty: Medium

Question: What does queue.Queue() provide?
A) Simple list
B) Thread-safe FIFO queue
C) Stack
D) Priority queue only

✔ Correct Answer: B

Reason: queue.Queue() is thread-safe FIFO queue. queue.LifoQueue() for stack. queue.PriorityQueue() for priority queue.

Tag: Normal

---

### Question 616
Domain: Programming
Topic: Linked List
Subtopic: Node Structure
Difficulty: Easy

Question: What does linked list node contain?
A) Only data
B) Data and reference to next node
C) Only reference
D) Index

✔ Correct Answer: B

Reason: Linked list node contains data and reference (pointer) to next node. Last node points to None/null. Doubly linked has prev reference too.

Tag: Past Paper

---

### Question 617
Domain: Programming
Topic: Code Analysis
Subtopic: Linked List Traversal
Difficulty: Medium

Question: What is the output?
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

current = head
while current:
    print(current.data, end=' ')
    current = current.next
```
A) 3 2 1
B) 1 2 3
C) 1
D) Error

✔ Correct Answer: B

Reason: Traverses linked list from head, printing each node's data. Outputs: 1 2 3.

Tag: Normal

---

### Question 618
Domain: Programming
Topic: Linked List
Subtopic: Insertion
Difficulty: Medium

Question: What is time complexity of inserting at beginning of linked list?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Insert at beginning: create node, point to current head, update head. Constant time O(1). Insert at end without tail: O(n).

Tag: Normal

---

### Question 619
Domain: Programming
Topic: Linked List
Subtopic: Doubly Linked List
Difficulty: Medium

Question: What is advantage of doubly linked list?
A) Uses less memory
B) Can traverse in both directions
C) Faster
D) Simpler

✔ Correct Answer: B

Reason: Doubly linked list has prev and next pointers, allowing bidirectional traversal. Uses more memory but enables efficient operations.

Tag: Normal

---

### Question 620
Domain: Programming
Topic: Code Analysis
Subtopic: Circular Linked List
Difficulty: Hard

Question: What makes linked list circular?
A) Round nodes
B) Last node points back to first node
C) Sorted nodes
D) No null

✔ Correct Answer: B

Reason: Circular linked list: last node's next points to head instead of None, forming circle. Useful for round-robin scheduling.

Tag: Normal

---

### Question 621
Domain: Programming
Topic: Stack Applications
Subtopic: Expression Evaluation
Difficulty: Hard

Question: What data structure evaluates postfix expressions?
A) Queue
B) Stack
C) Tree
D) Array

✔ Correct Answer: B

Reason: Stack evaluates postfix: push operands, pop two for operator, push result. "3 4 +" → push 3, push 4, pop both, push 7.

Tag: Normal

---

### Question 622
Domain: Programming
Topic: Code Analysis
Subtopic: Balanced Parentheses
Difficulty: Hard

Question: What does this code check?
```python
def is_balanced(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0
```
A) String length
B) If parentheses/brackets are balanced
C) Character count
D) Duplicates

✔ Correct Answer: B

Reason: Uses stack to match opening/closing brackets. Push opening, pop and match for closing. Balanced if stack empty at end.

Tag: Normal

---

### Question 623
Domain: Programming
Topic: Queue Applications
Subtopic: Level Order Traversal
Difficulty: Hard

Question: What traversal uses queue?
A) Inorder
B) Level order (BFS)
C) Preorder
D) Postorder

✔ Correct Answer: B

Reason: Level order traversal (BFS) uses queue to visit nodes level by level. Enqueue root, dequeue, enqueue children, repeat.

Tag: Normal

---

### Question 624
Domain: Programming
Topic: Hashing
Subtopic: Hash Table Operations
Difficulty: Medium

Question: What is average time complexity of hash table operations?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Hash table provides O(1) average time for insert, delete, search. Worst case O(n) with many collisions.

Tag: Past Paper

---

### Question 625
Domain: Programming
Topic: Code Analysis
Subtopic: Set Operations Performance
Difficulty: Medium

Question: What is time complexity of set1.intersection(set2)?
A) O(1)
B) O(min(len(set1), len(set2)))
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: Intersection iterates smaller set, checking membership in larger (O(1) per check). Total: O(min(m, n)).

Tag: Normal

---

### Question 626
Domain: Programming
Topic: String Algorithms
Subtopic: String Reversal
Difficulty: Easy

Question: What is the output?
```python
s = "hello"
print(s[::-1])
```
A) hello
B) olleh
C) Error
D) h

✔ Correct Answer: B

Reason: Slice [::-1] reverses string. "hello" becomes "olleh". Works for any sequence.

Tag: Normal

---

### Question 627
Domain: Programming
Topic: String Algorithms
Subtopic: Anagram Check
Difficulty: Medium

Question: How do you check if two strings are anagrams?
A) Compare directly
B) Sort both and compare, or count character frequencies
C) Check length only
D) Reverse and compare

✔ Correct Answer: B

Reason: Anagrams have same characters in different order. sorted(s1) == sorted(s2) or Counter(s1) == Counter(s2) checks this.

Tag: Normal

---

### Question 628
Domain: Programming
Topic: Code Analysis
Subtopic: Character Frequency
Difficulty: Medium

Question: What is the output?
```python
from collections import Counter
s = "hello"
c = Counter(s)
print(c.most_common(1))
```
A) [('h', 1)]
B) [('l', 2)]
C) [('o', 1)]
D) Error

✔ Correct Answer: B

Reason: Counter counts character frequencies. most_common(1) returns most frequent: 'l' appears 2 times.

Tag: Normal

---

### Question 629
Domain: Programming
Topic: Array Algorithms
Subtopic: Kadane's Algorithm
Difficulty: Hard

Question: What problem does Kadane's algorithm solve?
A) Sorting
B) Maximum sum contiguous subarray
C) Searching
D) Reversing

✔ Correct Answer: B

Reason: Kadane's algorithm finds maximum sum of contiguous subarray in O(n) time using dynamic programming approach.

Tag: Normal

---

### Question 630
Domain: Programming
Topic: Code Analysis
Subtopic: Maximum Subarray
Difficulty: Hard

Question: What is the output?
```python
def max_subarray(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
```
A) 4
B) 6
C) 10
D) -2

✔ Correct Answer: B

Reason: Kadane's algorithm finds maximum subarray sum. Subarray [4, -1, 2, 1] has sum 6 (maximum).

Tag: Normal

---

### Question 631
Domain: Programming
Topic: Dynamic Programming
Subtopic: Fibonacci DP
Difficulty: Hard

Question: What is time complexity of DP fibonacci?
A) O(2ⁿ)
B) O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: DP fibonacci (memoization or tabulation) computes each value once, storing for reuse. O(n) time, O(n) space. Naive recursion: O(2ⁿ).

Tag: Normal

---

### Question 632
Domain: Programming
Topic: Code Analysis
Subtopic: DP Tabulation
Difficulty: Hard

Question: What is the output?
```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib(6))
```
A) 5
B) 8
C) 13
D) 6

✔ Correct Answer: B

Reason: Fibonacci sequence: 0,1,1,2,3,5,8,13... fib(6) is 7th number (0-indexed): 8.

Tag: Normal

---

### Question 633
Domain: Programming
Topic: Dynamic Programming
Subtopic: Knapsack Problem
Difficulty: Hard

Question: What is 0/1 knapsack problem?
A) Bag problem
B) Select items with max value within weight capacity (each item once)
C) Sorting problem
D) Packing problem

✔ Correct Answer: B

Reason: 0/1 knapsack: given items with weights and values, select subset maximizing value without exceeding capacity. Each item taken 0 or 1 times.

Tag: Past Paper

---

### Question 634
Domain: Programming
Topic: Dynamic Programming
Subtopic: Longest Common Subsequence
Difficulty: Hard

Question: What is LCS problem?
A) Longest string
B) Longest subsequence common to two sequences
C) Longest substring
D) Largest number

✔ Correct Answer: B

Reason: LCS finds longest subsequence present in both sequences (not necessarily contiguous). "ABCD" and "ACBD" have LCS "ABD" (length 3).

Tag: Normal

---

### Question 635
Domain: Programming
Topic: Code Analysis
Subtopic: LCS Length
Difficulty: Hard

Question: What is LCS length of "AGGTAB" and "GXTXAYB"?
A) 3
B) 4
C) 5
D) 6

✔ Correct Answer: B

Reason: LCS is "GTAB" (length 4). Common subsequence maintaining order: G, T, A, B.

Tag: Normal

---

### Question 636
Domain: Programming
Topic: Bit Manipulation
Subtopic: Check Bit
Difficulty: Hard

Question: How do you check if nth bit is set?
A) x & n
B) (x & (1 << n)) != 0
C) x | n
D) x ^ n

✔ Correct Answer: B

Reason: 1 << n creates mask with only nth bit set. x & mask isolates nth bit. Non-zero means bit is set.

Tag: Normal

---

### Question 637
Domain: Programming
Topic: Code Analysis
Subtopic: Set Bit
Difficulty: Hard

Question: How do you set nth bit to 1?
A) x & (1 << n)
B) x | (1 << n)
C) x ^ (1 << n)
D) x - (1 << n)

✔ Correct Answer: B

Reason: OR with mask sets bit. x | (1 << n) sets nth bit to 1 without affecting others.

Tag: Normal

---

### Question 638
Domain: Programming
Topic: Bit Manipulation
Subtopic: Clear Bit
Difficulty: Hard

Question: How do you clear nth bit (set to 0)?
A) x | (1 << n)
B) x & ~(1 << n)
C) x ^ (1 << n)
D) x - n

✔ Correct Answer: B

Reason: AND with inverted mask clears bit. ~(1 << n) has all bits 1 except nth. x & ~(1 << n) clears nth bit.

Tag: Normal

---

### Question 639
Domain: Programming
Topic: Code Analysis
Subtopic: Toggle Bit
Difficulty: Hard

Question: How do you toggle nth bit?
A) x & (1 << n)
B) x ^ (1 << n)
C) x | (1 << n)
D) x - (1 << n)

✔ Correct Answer: B

Reason: XOR with mask toggles bit. x ^ (1 << n) flips nth bit (0→1, 1→0).

Tag: Normal

---

### Question 640
Domain: Programming
Topic: Bit Manipulation
Subtopic: Count Set Bits
Difficulty: Hard

Question: What is the output?
```python
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

print(count_bits(7))
```
A) 1
B) 3
C) 7
D) 0

✔ Correct Answer: B

Reason: Counts set bits in binary. 7 = 111 (binary) has 3 set bits. n & 1 checks rightmost bit, n >>= 1 shifts right.

Tag: Normal

---

### Question 641
Domain: Programming
Topic: Bit Manipulation
Subtopic: Power of Two
Difficulty: Hard

Question: How do you check if number is power of 2?
A) n % 2 == 0
B) (n & (n - 1)) == 0 and n != 0
C) n / 2 == integer
D) n > 0

✔ Correct Answer: B

Reason: Power of 2 has single set bit. n & (n-1) clears rightmost bit. If result is 0 (and n≠0), n is power of 2.

Tag: Normal

---

### Question 642
Domain: Programming
Topic: Code Analysis
Subtopic: Swap Without Temp
Difficulty: Hard

Question: What is the output?
```python
a, b = 5, 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
```
A) 5 10
B) 10 5
C) 0 0
D) Error

✔ Correct Answer: B

Reason: XOR swap without temp variable. After operations: a=10, b=5. XOR properties: x^x=0, x^0=x, x^y^y=x.

Tag: Normal

---

### Question 643
Domain: Programming
Topic: Searching Algorithms
Subtopic: Jump Search
Difficulty: Hard

Question: What is jump search?
A) Random search
B) Searches sorted array by jumping ahead by fixed steps
C) Binary search
D) Linear search

✔ Correct Answer: B

Reason: Jump search jumps ahead by √n steps in sorted array, then linear search in block. Time: O(√n), between linear and binary.

Tag: Normal

---

### Question 644
Domain: Programming
Topic: Searching Algorithms
Subtopic: Interpolation Search
Difficulty: Hard

Question: When is interpolation search better than binary search?
A) Always
B) Uniformly distributed sorted data
C) Never
D) Unsorted data

✔ Correct Answer: B

Reason: Interpolation search estimates position based on value distribution. O(log log n) for uniform data, O(n) worst case. Binary search: O(log n) always.

Tag: Normal

---

### Question 645
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Insertion Sort
Difficulty: Medium

Question: What is time complexity of insertion sort?
A) O(n log n)
B) O(n²)
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Insertion sort: O(n²) worst/average case, O(n) best case (nearly sorted). Efficient for small or nearly sorted arrays.

Tag: Past Paper

---

### Question 646
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Selection Sort
Difficulty: Medium

Question: What does selection sort do?
A) Selects random elements
B) Repeatedly selects minimum and places at beginning
C) Selects pivot
D) Selects median

✔ Correct Answer: B

Reason: Selection sort finds minimum in unsorted portion, swaps with first unsorted element. O(n²) all cases, not stable.

Tag: Normal

---

### Question 647
Domain: Programming
Topic: Code Analysis
Subtopic: Counting Sort
Difficulty: Hard

Question: When is counting sort efficient?
A) Always
B) When range of values is small compared to n
C) Large ranges
D) Never

✔ Correct Answer: B

Reason: Counting sort counts occurrences of each value. O(n+k) where k is range. Efficient when k is small. Not comparison-based.

Tag: Normal

---

### Question 648
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Radix Sort
Difficulty: Hard

Question: What is radix sort?
A) Radius sorting
B) Sorts by processing digits/characters position by position
C) Comparison sort
D) Random sort

✔ Correct Answer: B

Reason: Radix sort processes digits from least to most significant (or reverse), using stable sort for each digit. O(d*n) where d is digits.

Tag: Normal

---

### Question 649
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Heap Sort
Difficulty: Hard

Question: What is time complexity of heap sort?
A) O(n²)
B) O(n log n)
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Heap sort builds heap O(n), then extracts max n times O(log n each): O(n log n) all cases. In-place, not stable.

Tag: Past Paper

---

### Question 650
Domain: Programming
Topic: Code Analysis
Subtopic: Sorting Comparison
Difficulty: Medium

Question: Which sort is stable?
A) Quick sort
B) Merge sort
C) Heap sort
D) Selection sort

✔ Correct Answer: B

Reason: Stable sorts maintain relative order of equal elements. Merge sort is stable. Quick sort, heap sort, selection sort typically aren't.

Tag: Normal

---

### Question 651
Domain: Programming
Topic: Recursion Optimization
Subtopic: Tail Call Optimization
Difficulty: Hard

Question: Does Python support tail call optimization?
A) Yes
B) No
C) Only in Python 3
D) Only with decorator

✔ Correct Answer: B

Reason: Python doesn't support TCO (Guido's design choice). Tail recursive functions still use stack space. Use iteration for deep recursion.

Tag: Normal

---

### Question 652
Domain: Programming
Topic: Code Analysis
Subtopic: Memoization Decorator
Difficulty: Hard

Question: What does this decorator do?
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
A) Limits recursion
B) Caches function results (memoization)
C) Logs calls
D) Validates input

✔ Correct Answer: B

Reason: lru_cache decorator caches function results. Subsequent calls with same arguments return cached value. maxsize=None: unlimited cache.

Tag: Normal

---

### Question 653
Domain: Programming
Topic: Complexity Analysis
Subtopic: Space Complexity
Difficulty: Medium

Question: What is space complexity?
A) Disk space
B) Memory used by algorithm relative to input size
C) Code length
D) Variable count

✔ Correct Answer: B

Reason: Space complexity measures memory used by algorithm (variables, data structures, recursion stack) as function of input size.

Tag: Past Paper

---

### Question 654
Domain: Programming
Topic: Code Analysis
Subtopic: Auxiliary Space
Difficulty: Medium

Question: What is auxiliary space?
A) Extra space
B) Extra space used excluding input
C) Total space
D) Stack space

✔ Correct Answer: B

Reason: Auxiliary space is extra space used by algorithm excluding input. Total space = input space + auxiliary space.

Tag: Normal

---

### Question 655
Domain: Programming
Topic: Complexity Analysis
Subtopic: Best vs Worst Case
Difficulty: Medium

Question: What is worst-case time complexity?
A) Slowest execution
B) Maximum time for any input of size n
C) Average time
D) Best time

✔ Correct Answer: B

Reason: Worst-case is maximum time over all possible inputs of size n. Best-case is minimum. Average-case is expected time.

Tag: Past Paper

---

### Question 656
Domain: Programming
Topic: Code Analysis
Subtopic: Amortized Analysis
Difficulty: Hard

Question: What is amortized time complexity?
A) Amortized cost
B) Average time per operation over sequence of operations
C) Worst case
D) Best case

✔ Correct Answer: B

Reason: Amortized analysis averages cost over sequence. Dynamic array append: O(1) amortized (occasional O(n) resize averaged over many O(1) appends).

Tag: Normal

---

### Question 657
Domain: Programming
Topic: String Matching
Subtopic: Naive Pattern Matching
Difficulty: Medium

Question: What is time complexity of naive string matching?
A) O(n)
B) O(n*m) where n=text length, m=pattern length
C) O(log n)
D) O(1)

✔ Correct Answer: B

Reason: Naive algorithm checks pattern at each text position. Worst case: O((n-m+1)*m) ≈ O(n*m). KMP algorithm improves to O(n+m).

Tag: Normal

---

### Question 658
Domain: Programming
Topic: Algorithm Paradigms
Subtopic: Brute Force
Difficulty: Easy

Question: What is brute force approach?
A) Forced execution
B) Try all possible solutions
C) Optimized algorithm
D) Random approach

✔ Correct Answer: B

Reason: Brute force exhaustively tries all possibilities. Simple but often inefficient. Used when no better algorithm or for small inputs.

Tag: Normal

---

### Question 659
Domain: Programming
Topic: Code Analysis
Subtopic: Linear Search
Difficulty: Easy

Question: What is the output?
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30))
```
A) 30
B) 2
C) -1
D) 3

✔ Correct Answer: B

Reason: Linear search finds 30 at index 2. Returns index 2.

Tag: Normal

---

### Question 660
Domain: Programming
Topic: Matrix Operations
Subtopic: Matrix Traversal
Difficulty: Medium

Question: What is the output?
```python
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for val in row:
        print(val, end=' ')
```
A) 1 3 2 4
B) 1 2 3 4
C) 4 3 2 1
D) Error

✔ Correct Answer: B

Reason: Nested loops traverse matrix row by row. Prints: 1 2 3 4.

Tag: Normal

---

### Question 661
Domain: Programming
Topic: Matrix Operations
Subtopic: Matrix Transpose
Difficulty: Medium

Question: What is matrix transpose?
A) Matrix rotation
B) Rows become columns, columns become rows
C) Matrix inversion
D) Matrix multiplication

✔ Correct Answer: B

Reason: Transpose swaps rows and columns. Element at [i][j] moves to [j][i]. [[1,2],[3,4]] → [[1,3],[2,4]].

Tag: Normal

---

### Question 662
Domain: Programming
Topic: Code Analysis
Subtopic: Transpose Implementation
Difficulty: Hard

Question: What is the output?
```python
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[matrix[j][i] for j in range(len(matrix))] 
             for i in range(len(matrix[0]))]
print(transpose)
```
A) [[1, 2, 3], [4, 5, 6]]
B) [[1, 4], [2, 5], [3, 6]]
C) [[6, 5, 4], [3, 2, 1]]
D) Error

✔ Correct Answer: B

Reason: Comprehension transposes matrix. Outer loop iterates columns, inner iterates rows. Result: [[1,4], [2,5], [3,6]].

Tag: Normal

---

### Question 663
Domain: Programming
Topic: Recursion Patterns
Subtopic: Tree Recursion
Difficulty: Hard

Question: What is tree recursion?
A) Recursion on trees
B) Function makes multiple recursive calls
C) Single recursive call
D) No recursion

✔ Correct Answer: B

Reason: Tree recursion: function makes multiple recursive calls (like fibonacci). Creates tree of calls. Linear recursion makes single recursive call.

Tag: Normal

---

### Question 664
Domain: Programming
Topic: Code Analysis
Subtopic: Recursive Tree
Difficulty: Hard

Question: How many recursive calls for fib(4)?
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
A) 4
B) 9
C) 5
D) 8

✔ Correct Answer: B

Reason: fib(4) calls fib(3) and fib(2). fib(3) calls fib(2) and fib(1), etc. Total calls: 9 (including fib(4) itself).

Tag: Normal

---

### Question 665
Domain: Programming
Topic: String Manipulation
Subtopic: String Builder
Difficulty: Hard

Question: Why use StringBuilder in Java?
A) Builds strings
B) Mutable, efficient for multiple string modifications
C) Immutable strings
D) String validation

✔ Correct Answer: B

Reason: StringBuilder is mutable, efficient for multiple modifications. String concatenation creates new objects. StringBuilder modifies in-place.

Tag: Normal

---

### Question 666
Domain: Programming
Topic: Code Analysis
Subtopic: StringBuilder Usage
Difficulty: Medium

Question: What is the output?
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");
sb.insert(5, ",");
System.out.println(sb.toString());
```
A) Hello World
B) Hello, World
C) Hello,World
D) Error

✔ Correct Answer: B

Reason: append(" World") → "Hello World". insert(5, ",") inserts comma at index 5 → "Hello, World".

Tag: Normal

---

### Question 667
Domain: Programming
Topic: Collections
Subtopic: ArrayList vs LinkedList
Difficulty: Hard

Question: When is LinkedList better than ArrayList in Java?
A) Always
B) Frequent insertions/deletions at beginning/middle
C) Random access
D) Never

✔ Correct Answer: B

Reason: LinkedList: O(1) insert/delete at known position. ArrayList: O(n) due to shifting. ArrayList better for random access O(1) vs O(n).

Tag: Normal

---

### Question 668
Domain: Programming
Topic: Code Analysis
Subtopic: ArrayList Operations
Difficulty: Medium

Question: What is the output?
```java
ArrayList<Integer> list = new ArrayList<>();
list.add(10);
list.add(20);
list.add(1, 15);
System.out.println(list.get(1));
```
A) 10
B) 15
C) 20
D) Error

✔ Correct Answer: B

Reason: add(1, 15) inserts 15 at index 1, shifting 20 right. List: [10, 15, 20]. get(1) returns 15.

Tag: Normal

---

### Question 669
Domain: Programming
Topic: HashMap
Subtopic: HashMap Basics
Difficulty: Easy

Question: What does HashMap store?
A) Only keys
B) Key-value pairs
C) Only values
D) Arrays

✔ Correct Answer: B

Reason: HashMap stores key-value pairs with O(1) average lookup. Keys must be unique, values can duplicate.

Tag: Normal

---

### Question 670
Domain: Programming
Topic: Code Analysis
Subtopic: HashMap Operations
Difficulty: Medium

Question: What is the output?
```java
HashMap<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("a", 3);
System.out.println(map.get("a"));
```
A) 1
B) 3
C) Error
D) null

✔ Correct Answer: B

Reason: put("a", 3) overwrites previous value. Keys are unique. map.get("a") returns latest value: 3.

Tag: Normal

---

### Question 671
Domain: Programming
Topic: HashSet
Subtopic: Set Operations
Difficulty: Easy

Question: What does HashSet guarantee?
A) Order
B) No duplicate elements
C) Sorted elements
D) Indexed access

✔ Correct Answer: B

Reason: HashSet stores unique elements (no duplicates), unordered. add() returns false if element exists. O(1) average operations.

Tag: Normal

---

### Question 672
Domain: Programming
Topic: Code Analysis
Subtopic: HashSet Usage
Difficulty: Medium

Question: What is the output?
```java
HashSet<Integer> set = new HashSet<>();
set.add(1);
set.add(2);
set.add(1);
System.out.println(set.size());
```
A) 3
B) 2
C) 1
D) Error

✔ Correct Answer: B

Reason: HashSet doesn't allow duplicates. Second add(1) doesn't add (already exists). Size is 2.

Tag: Normal

---

### Question 673
Domain: Programming
Topic: TreeMap
Subtopic: Sorted Map
Difficulty: Medium

Question: What does TreeMap provide?
A) Tree structure
B) Sorted key-value pairs (Red-Black tree)
C) Unsorted map
D) Array map

✔ Correct Answer: B

Reason: TreeMap maintains sorted order of keys using Red-Black tree. O(log n) operations. HashMap is O(1) but unordered.

Tag: Normal

---

### Question 674
Domain: Programming
Topic: Code Analysis
Subtopic: TreeSet
Difficulty: Medium

Question: What is the output?
```java
TreeSet<Integer> set = new TreeSet<>();
set.add(3);
set.add(1);
set.add(2);
System.out.println(set);
```
A) [3, 1, 2]
B) [1, 2, 3]
C) [2, 1, 3]
D) Error

✔ Correct Answer: B

Reason: TreeSet maintains sorted order. Elements sorted: [1, 2, 3].

Tag: Normal

---

### Question 675
Domain: Programming
Topic: Queue Interface
Subtopic: Queue Methods
Difficulty: Medium

Question: What's the difference between add() and offer() in Queue?
A) No difference
B) add() throws exception if full, offer() returns false
C) offer() is faster
D) add() is deprecated

✔ Correct Answer: B

Reason: add() throws exception if queue full. offer() returns false. remove() throws exception if empty, poll() returns null.

Tag: Normal

---

### Question 676
Domain: Programming
Topic: Code Analysis
Subtopic: PriorityQueue
Difficulty: Hard

Question: What is the output?
```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(3);
pq.add(1);
pq.add(2);
System.out.println(pq.poll());
System.out.println(pq.poll());
```
A) 3 1
B) 1 2
C) 3 2
D) Error

✔ Correct Answer: B

Reason: PriorityQueue is min heap by default. poll() removes smallest. First poll: 1, second poll: 2.

Tag: Normal

---

### Question 677
Domain: Programming
Topic: Comparable Interface
Subtopic: Natural Ordering
Difficulty: Hard

Question: What does Comparable interface provide?
A) Comparison operators
B) Natural ordering by implementing compareTo()
C) Equality check
D) Sorting algorithm

✔ Correct Answer: B

Reason: Comparable interface defines natural ordering via compareTo() method. Classes implementing it can be sorted with Collections.sort().

Tag: Normal

---

### Question 678
Domain: Programming
Topic: Code Analysis
Subtopic: compareTo Method
Difficulty: Hard

Question: What should compareTo() return?
```java
class Person implements Comparable<Person> {
    int age;
    public int compareTo(Person other) {
        return this.age - other.age;
    }
}
```
A) Boolean
B) Negative if less, 0 if equal, positive if greater
C) Always 0
D) Age difference only

✔ Correct Answer: B

Reason: compareTo() returns negative if this < other, 0 if equal, positive if this > other. Defines natural ordering.

Tag: Normal

---

### Question 679
Domain: Programming
Topic: Comparator Interface
Subtopic: Custom Ordering
Difficulty: Hard

Question: When use Comparator instead of Comparable?
A) Never
B) For custom ordering or when can't modify class
C) Always
D) Only for numbers

✔ Correct Answer: B

Reason: Comparable defines natural ordering (one way). Comparator provides custom ordering (multiple ways) without modifying class.

Tag: Normal

---

### Question 680
Domain: Programming
Topic: Code Analysis
Subtopic: Comparator Usage
Difficulty: Hard

Question: What is the output?
```java
List<String> words = Arrays.asList("apple", "pie", "banana");
Collections.sort(words, (a, b) -> a.length() - b.length());
System.out.println(words.get(0));
```
A) apple
B) pie
C) banana
D) Error

✔ Correct Answer: B

Reason: Comparator sorts by length. "pie" has length 3 (shortest). words.get(0) returns first: "pie".

Tag: Normal

---

### Question 681
Domain: Programming
Topic: Streams API
Subtopic: Stream Creation
Difficulty: Medium

Question: What is Stream in Java 8+?
A) Input/output stream
B) Sequence of elements supporting functional operations
C) Data stream
D) File stream

✔ Correct Answer: B

Reason: Stream is sequence supporting functional operations (filter, map, reduce). Doesn't store data, processes elements from source.

Tag: Normal

---

### Question 682
Domain: Programming
Topic: Code Analysis
Subtopic: Stream Operations
Difficulty: Hard

Question: What is the output?
```java
List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);
int sum = nums.stream()
              .filter(n -> n % 2 == 0)
              .mapToInt(n -> n * 2)
              .sum();
System.out.println(sum);
```
A) 15
B) 12
C) 6
D) 30

✔ Correct Answer: B

Reason: filter() keeps even numbers [2,4]. mapToInt() doubles them [4,8]. sum() adds: 4+8=12.

Tag: Normal

---

### Question 683
Domain: Programming
Topic: Streams API
Subtopic: Intermediate vs Terminal
Difficulty: Hard

Question: What's the difference between intermediate and terminal operations?
A) No difference
B) Intermediate returns stream (lazy), terminal produces result
C) Terminal is faster
D) Intermediate is final

✔ Correct Answer: B

Reason: Intermediate operations (filter, map) return stream, are lazy. Terminal operations (collect, sum) trigger execution, produce result.

Tag: Normal

---

### Question 684
Domain: Programming
Topic: Code Analysis
Subtopic: Stream Collect
Difficulty: Hard

Question: What is the output?
```java
List<String> words = Arrays.asList("a", "bb", "ccc");
List<Integer> lengths = words.stream()
                             .map(String::length)
                             .collect(Collectors.toList());
System.out.println(lengths);
```
A) [a, bb, ccc]
B) [1, 2, 3]
C) 6
D) Error

✔ Correct Answer: B

Reason: map(String::length) transforms strings to lengths. collect() gathers into list: [1, 2, 3].

Tag: Normal

---

### Question 685
Domain: Programming
Topic: Optional
Subtopic: Optional Class
Difficulty: Hard

Question: What is Optional in Java 8+?
A) Optional parameter
B) Container that may or may not contain value (avoids null)
C) Optional method
D) Configuration

✔ Correct Answer: B

Reason: Optional is container for potentially absent value, avoiding null pointer exceptions. Use isPresent(), get(), orElse().

Tag: Normal

---

### Question 686
Domain: Programming
Topic: Code Analysis
Subtopic: Optional Usage
Difficulty: Hard

Question: What is the output?
```java
Optional<String> opt = Optional.ofNullable(null);
System.out.println(opt.orElse("Default"));
```
A) null
B) Default
C) Error
D) Optional.empty

✔ Correct Answer: B

Reason: ofNullable(null) creates empty Optional. orElse() returns default value when empty: "Default".

Tag: Normal

---

### Question 687
Domain: Programming
Topic: Lambda Expressions
Subtopic: Functional Interface
Difficulty: Hard

Question: What is functional interface?
A) Any interface
B) Interface with exactly one abstract method
C) Multiple methods
D) No methods

✔ Correct Answer: B

Reason: Functional interface has single abstract method (SAM), can be implemented with lambda. @FunctionalInterface annotation validates.

Tag: Normal

---

### Question 688
Domain: Programming
Topic: Code Analysis
Subtopic: Lambda Syntax
Difficulty: Medium

Question: What is the output?
```java
List<Integer> nums = Arrays.asList(1, 2, 3);
nums.forEach(n -> System.out.print(n * 2 + " "));
```
A) 1 2 3
B) 2 4 6
C) 6
D) Error

✔ Correct Answer: B

Reason: forEach() applies lambda to each element. Lambda doubles each: 1*2=2, 2*2=4, 3*2=6. Prints: 2 4 6.

Tag: Normal

---

### Question 689
Domain: Programming
Topic: Method References
Subtopic: Method Reference Syntax
Difficulty: Hard

Question: What does System.out::println represent?
A) Method call
B) Method reference (equivalent to lambda)
C) Static method
D) Error

✔ Correct Answer: B

Reason: :: is method reference syntax. System.out::println is equivalent to lambda: x -> System.out.println(x). More concise.

Tag: Normal

---

### Question 690
Domain: Programming
Topic: Code Analysis
Subtopic: Method Reference Types
Difficulty: Hard

Question: What type of method reference is String::length?
A) Instance method of object
B) Instance method of class
C) Static method
D) Constructor

✔ Correct Answer: B

Reason: String::length is instance method reference of arbitrary object. Used like: strings.stream().map(String::length). Other types: object::method, Class::staticMethod, Class::new.

Tag: Normal

---

### Question 691
Domain: Programming
Topic: Exception Handling
Subtopic: Try-with-Resources
Difficulty: Hard

Question: What does try-with-resources do in Java?
A) Tries resources
B) Automatically closes resources implementing AutoCloseable
C) Catches exceptions
D) Allocates resources

✔ Correct Answer: B

Reason: try-with-resources automatically closes resources (files, connections) implementing AutoCloseable, even if exception occurs.

Tag: Normal

---

### Question 692
Domain: Programming
Topic: Code Analysis
Subtopic: AutoCloseable
Difficulty: Hard

Question: What is the output?
```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line = br.readLine();
    System.out.println(line);
}
// br is closed automatically
```
A) Error (not closed)
B) Reads line, closes automatically
C) File remains open
D) Syntax error

✔ Correct Answer: B

Reason: try-with-resources automatically calls br.close() after block, even if exception. No explicit close() needed.

Tag: Normal

---

### Question 693
Domain: Programming
Topic: Generics
Subtopic: Generic Class
Difficulty: Hard

Question: What does this generic class do?
```java
class Box<T> {
    private T value;
    public void set(T value) { this.value = value; }
    public T get() { return value; }
}
```
A) Only integers
B) Works with any type T
C) Only strings
D) Error

✔ Correct Answer: B

Reason: Generic class with type parameter T. Box<Integer>, Box<String> create type-specific instances. Provides type safety.

Tag: Normal

---

### Question 694
Domain: Programming
Topic: Generics
Subtopic: Bounded Type Parameters
Difficulty: Hard

Question: What does <T extends Number> mean?
A) T is Number
B) T must be Number or its subclass
C) T extends class
D) Error

✔ Correct Answer: B

Reason: Bounded type parameter: T must be Number or subclass (Integer, Double, etc.). Restricts generic type, enables calling Number methods.

Tag: Normal

---

### Question 695
Domain: Programming
Topic: Code Analysis
Subtopic: Wildcard Generics
Difficulty: Hard

Question: What does List<?> mean?
A) List of anything
B) List of unknown type (wildcard)
C) Empty list
D) Error

✔ Correct Answer: B

Reason: ? is wildcard representing unknown type. List<?> can be List<Integer>, List<String>, etc. Read-only for type safety.

Tag: Normal

---

### Question 696
Domain: Programming
Topic: Annotations
Subtopic: @Override
Difficulty: Easy

Question: What does @Override annotation do?
A) Overrides always
B) Indicates method overrides superclass method, compiler checks
C) Required for overriding
D) Deletes method

✔ Correct Answer: B

Reason: @Override tells compiler to verify method actually overrides superclass method. Catches errors like typos. Not required but recommended.

Tag: Normal

---

### Question 697
Domain: Programming
Topic: Annotations
Subtopic: @Deprecated
Difficulty: Easy

Question: What does @Deprecated indicate?
A) Deleted
B) Element shouldn't be used, may be removed in future
C) Broken
D) Old version

✔ Correct Answer: B

Reason: @Deprecated marks element as discouraged for use, typically has better alternative. Compiler warns when used.

Tag: Normal

---

### Question 698
Domain: Programming
Topic: Code Analysis
Subtopic: @SuppressWarnings
Difficulty: Medium

Question: What does @SuppressWarnings("unchecked") do?
A) Suppresses errors
B) Suppresses compiler warnings for unchecked operations
C) Fixes warnings
D) Deletes warnings

✔ Correct Answer: B

Reason: @SuppressWarnings tells compiler to suppress specific warnings. "unchecked" suppresses generic type warnings. Use sparingly.

Tag: Normal

---

### Question 699
Domain: Programming
Topic: Reflection
Subtopic: Reflection API
Difficulty: Hard

Question: What is reflection in Java?
A) Code reflection
B) Inspecting and modifying classes/methods/fields at runtime
C) Mirroring code
D) Debugging

✔ Correct Answer: B

Reason: Reflection API allows inspecting class structure, invoking methods, accessing fields at runtime. Powerful but slow, breaks encapsulation.

Tag: Normal

---

### Question 700
Domain: Programming
Topic: Code Analysis
Subtopic: Class Object
Difficulty: Hard

Question: What is the output?
```java
Class<?> cls = String.class;
System.out.println(cls.getName());
```
A) String
B) java.lang.String
C) class String
D) Error

✔ Correct Answer: B

Reason: Class object represents class metadata. getName() returns fully qualified name: "java.lang.String".

Tag: Normal

---

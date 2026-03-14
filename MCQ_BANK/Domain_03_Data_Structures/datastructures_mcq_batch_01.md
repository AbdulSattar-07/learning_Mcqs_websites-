# Data Structures - MCQ Batch 01
## Questions 1-100

---

### Question 1
Domain: Data Structures
Topic: Arrays
Subtopic: Array Basics
Difficulty: Easy

Question: What is an array?
A) Random collection
B) Contiguous memory storing elements of same type
C) Linked structure
D) Tree structure

✔ Correct Answer: B

Reason: Array stores elements in contiguous memory locations, same type, accessed by index. Fixed size in static arrays.

Tag: Past Paper

---

### Question 2
Domain: Data Structures
Topic: Arrays
Subtopic: Array Indexing
Difficulty: Easy

Question: What is time complexity of accessing array element by index?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Array elements accessed directly using base address + (index * element_size). Constant time O(1) regardless of array size.

Tag: Past Paper

---

### Question 3
Domain: Data Structures
Topic: Code Analysis
Subtopic: Array Declaration
Difficulty: Easy

Question: What is the output?
```cpp
int arr[5] = {1, 2, 3};
cout << arr[4];
```
A) Error
B) 0
C) Garbage value
D) 3

✔ Correct Answer: B

Reason: Partial initialization sets remaining elements to 0. arr[4] initialized to 0.

Tag: Normal

---

### Question 4
Domain: Data Structures
Topic: Arrays
Subtopic: Array Insertion
Difficulty: Medium

Question: What is time complexity of inserting element at beginning of array?
A) O(1)
B) O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Insert at beginning requires shifting all n elements right. O(n) time. Insert at end: O(1) if space available.

Tag: Past Paper

---

### Question 5
Domain: Data Structures
Topic: Arrays
Subtopic: Array Deletion
Difficulty: Medium

Question: What is time complexity of deleting element from middle of array?
A) O(1)
B) O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Delete from middle requires shifting elements left to fill gap. O(n) time. Delete from end: O(1).

Tag: Normal

---

### Question 6
Domain: Data Structures
Topic: Code Analysis
Subtopic: Array Traversal
Difficulty: Easy

Question: What is the output?
```python
arr = [10, 20, 30, 40]
for i in range(len(arr)):
    arr[i] += 5
print(arr[2])
```
A) 30
B) 35
C) 25
D) Error

✔ Correct Answer: B

Reason: Loop adds 5 to each element. arr[2] was 30, becomes 30+5=35.

Tag: Normal

---

### Question 7
Domain: Data Structures
Topic: Arrays
Subtopic: Multi-dimensional Arrays
Difficulty: Medium

Question: How is 2D array stored in memory?
A) Randomly
B) Row-major (C/C++/Python) or column-major (Fortran)
C) Diagonally
D) Not stored

✔ Correct Answer: B

Reason: 2D arrays stored linearly. Row-major: rows stored consecutively. Column-major: columns stored consecutively. Affects cache performance.

Tag: Normal

---

### Question 8
Domain: Data Structures
Topic: Code Analysis
Subtopic: 2D Array Access
Difficulty: Medium

Question: What is the output?
```java
int[][] matrix = {{1, 2}, {3, 4}, {5, 6}};
System.out.println(matrix[1][1]);
```
A) 1
B) 4
C) 3
D) 2

✔ Correct Answer: B

Reason: matrix[1][1] accesses row 1, column 1 (0-indexed). Row 1 is {3, 4}, column 1 is 4.

Tag: Normal

---

### Question 9
Domain: Data Structures
Topic: Dynamic Arrays
Subtopic: ArrayList/Vector
Difficulty: Medium

Question: How does dynamic array handle growth?
A) Fixed size
B) Allocates larger array, copies elements when full
C) Linked list
D) Never grows

✔ Correct Answer: B

Reason: When full, allocates new array (typically 2x size), copies elements, deallocates old. Amortized O(1) append.

Tag: Past Paper

---

### Question 10
Domain: Data Structures
Topic: Code Analysis
Subtopic: Dynamic Array Growth
Difficulty: Hard

Question: What is amortized time complexity of n append operations on dynamic array?
A) O(n²)
B) O(n)
C) O(log n)
D) O(1)

✔ Correct Answer: B

Reason: Most appends O(1), occasional resize O(n). Total cost for n appends: O(n). Amortized per operation: O(1).

Tag: Normal

---

### Question 11
Domain: Data Structures
Topic: Linked Lists
Subtopic: Singly Linked List
Difficulty: Easy

Question: What does each node in singly linked list contain?
A) Data only
B) Data and pointer to next node
C) Data and two pointers
D) Index and data

✔ Correct Answer: B

Reason: Singly linked list node contains data and single pointer to next node. Last node points to NULL.

Tag: Past Paper

---

### Question 12
Domain: Data Structures
Topic: Code Analysis
Subtopic: Linked List Insertion
Difficulty: Medium

Question: What is the output?
```cpp
struct Node {
    int data;
    Node* next;
};

Node* head = new Node{1, nullptr};
Node* newNode = new Node{2, head};
head = newNode;
cout << head->data;
```
A) 1
B) 2
C) Error
D) 0

✔ Correct Answer: B

Reason: newNode with data 2 points to old head. head updated to newNode. head->data is 2.

Tag: Normal

---

### Question 13
Domain: Data Structures
Topic: Linked Lists
Subtopic: Insertion Complexity
Difficulty: Easy

Question: What is time complexity of inserting at beginning of linked list?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Create node, point to current head, update head pointer. Three O(1) operations: O(1) total.

Tag: Past Paper

---

### Question 14
Domain: Data Structures
Topic: Linked Lists
Subtopic: Traversal
Difficulty: Easy

Question: What is time complexity of searching element in linked list?
A) O(1)
B) O(n)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Must traverse from head, checking each node. Worst case: element at end or not present. O(n) time.

Tag: Normal

---

### Question 15
Domain: Data Structures
Topic: Code Analysis
Subtopic: Linked List Length
Difficulty: Medium

Question: What is the output?
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(length(head))
```
A) 1
B) 3
C) 2
D) Error

✔ Correct Answer: B

Reason: Traverses list counting nodes. Three nodes: 1→2→3. Returns 3.

Tag: Normal

---

### Question 16
Domain: Data Structures
Topic: Doubly Linked Lists
Subtopic: DLL Structure
Difficulty: Medium

Question: What does doubly linked list node contain?
A) Data and next
B) Data, next, and prev pointers
C) Data only
D) Three pointers

✔ Correct Answer: B

Reason: Doubly linked list node has data, next pointer, and prev pointer. Enables bidirectional traversal.

Tag: Past Paper

---

### Question 17
Domain: Data Structures
Topic: Doubly Linked Lists
Subtopic: DLL Advantages
Difficulty: Medium

Question: What advantage does doubly linked list have over singly linked list?
A) Less memory
B) Can traverse backward, easier deletion
C) Faster insertion
D) No advantage

✔ Correct Answer: B

Reason: DLL allows backward traversal, easier deletion (no need to track previous). Uses more memory (extra pointer).

Tag: Normal

---

### Question 18
Domain: Data Structures
Topic: Code Analysis
Subtopic: DLL Insertion
Difficulty: Hard

Question: What is time complexity of inserting after given node in DLL?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Given node pointer, update 4 pointers (newNode.next, newNode.prev, next.prev, node.next). All O(1): total O(1).

Tag: Normal

---

### Question 19
Domain: Data Structures
Topic: Circular Linked Lists
Subtopic: Circular Structure
Difficulty: Medium

Question: What makes linked list circular?
A) Round nodes
B) Last node points to first node (head)
C) Sorted nodes
D) No NULL

✔ Correct Answer: B

Reason: Circular linked list: last node's next points to head instead of NULL. Can be singly or doubly circular.

Tag: Normal

---

### Question 20
Domain: Data Structures
Topic: Code Analysis
Subtopic: Circular List Detection
Difficulty: Hard

Question: How do you detect if linked list has cycle?
A) Count nodes
B) Floyd's cycle detection (slow and fast pointers)
C) Check all nodes
D) Cannot detect

✔ Correct Answer: B

Reason: Floyd's algorithm: slow moves 1 step, fast moves 2 steps. If they meet, cycle exists. O(n) time, O(1) space.

Tag: Past Paper

---

### Question 21
Domain: Data Structures
Topic: Code Analysis
Subtopic: Cycle Detection
Difficulty: Hard

Question: What is the output?
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

head = Node(1)
head.next = Node(2)
head.next.next = head  # Creates cycle
print(has_cycle(head))
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: List has cycle (node 2 points back to head). Fast and slow pointers eventually meet. Returns True.

Tag: Normal

---

### Question 22
Domain: Data Structures
Topic: Linked Lists
Subtopic: Reverse Linked List
Difficulty: Hard

Question: What is time complexity of reversing linked list?
A) O(n²)
B) O(n)
C) O(1)
D) O(log n)

✔ Correct Answer: B

Reason: Traverse list once, reversing pointers. Visit each node once: O(n) time, O(1) space (iterative).

Tag: Normal

---

### Question 23
Domain: Data Structures
Topic: Code Analysis
Subtopic: List Reversal
Difficulty: Hard

Question: What is the output?
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
new_head = reverse(head)
print(new_head.data, new_head.next.data)
```
A) 1 2
B) 3 2
C) 3 1
D) Error

✔ Correct Answer: B

Reason: Reverses list: 1→2→3 becomes 3→2→1. new_head.data=3, new_head.next.data=2.

Tag: Normal

---

### Question 24
Domain: Data Structures
Topic: Linked Lists
Subtopic: Middle Element
Difficulty: Hard

Question: How do you find middle element in one pass?
A) Count then traverse
B) Slow and fast pointers (slow moves 1, fast moves 2)
C) Cannot in one pass
D) Binary search

✔ Correct Answer: B

Reason: Fast pointer moves twice as fast. When fast reaches end, slow is at middle. O(n) time, one pass.

Tag: Normal

---

### Question 25
Domain: Data Structures
Topic: Code Analysis
Subtopic: Find Middle
Difficulty: Hard

Question: What is the output?
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# List: 1→2→3→4→5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print(find_middle(head))
```
A) 2
B) 3
C) 4
D) 1

✔ Correct Answer: B

Reason: 5 nodes, middle is 3rd node. When fast reaches end, slow at node 3.

Tag: Normal

---

### Question 26
Domain: Data Structures
Topic: Linked Lists
Subtopic: Merge Sorted Lists
Difficulty: Hard

Question: What is time complexity of merging two sorted linked lists?
A) O(1)
B) O(n + m)
C) O(n * m)
D) O(log n)

✔ Correct Answer: B

Reason: Compare heads, add smaller to result, advance pointer. Process all nodes from both lists: O(n+m).

Tag: Normal

---

### Question 27
Domain: Data Structures
Topic: Code Analysis
Subtopic: List Merge
Difficulty: Hard

Question: What is the output?
```python
def merge_sorted(l1, l2):
    dummy = Node(0)
    current = dummy
    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next

# l1: 1→3→5, l2: 2→4
# Result?
```
A) 1→2→3→4→5
B) 1→2→3→4→5
C) 5→4→3→2→1
D) Error

✔ Correct Answer: A

Reason: Merges sorted lists maintaining order: 1→2→3→4→5.

Tag: Normal

---

### Question 28
Domain: Data Structures
Topic: Linked Lists
Subtopic: Remove Duplicates
Difficulty: Medium

Question: How do you remove duplicates from sorted linked list?
A) Use set
B) Compare adjacent nodes, remove if equal
C) Sort again
D) Cannot remove

✔ Correct Answer: B

Reason: Sorted list has duplicates adjacent. Compare current with next, skip if equal. O(n) time, O(1) space.

Tag: Normal

---

### Question 29
Domain: Data Structures
Topic: Code Analysis
Subtopic: Duplicate Removal
Difficulty: Hard

Question: What is the output?
```python
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

# List: 1→1→2→3→3
# After removal?
```
A) 1→2→3
B) 1→2→3
C) 1→1→2→3→3
D) Error

✔ Correct Answer: A

Reason: Removes duplicate adjacent nodes. Result: 1→2→3.

Tag: Normal

---

### Question 30
Domain: Data Structures
Topic: Stacks
Subtopic: Stack Basics
Difficulty: Easy

Question: What principle does stack follow?
A) FIFO
B) LIFO (Last In First Out)
C) Random access
D) Priority

✔ Correct Answer: B

Reason: Stack follows LIFO: last element added is first removed. Like stack of plates. Operations: push, pop, peek.

Tag: Past Paper

---

### Question 31
Domain: Data Structures
Topic: Stacks
Subtopic: Stack Operations
Difficulty: Easy

Question: What is time complexity of push and pop operations?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Push adds to top, pop removes from top. Both constant time O(1) operations.

Tag: Past Paper

---

### Question 32
Domain: Data Structures
Topic: Code Analysis
Subtopic: Stack Implementation
Difficulty: Medium

Question: What is the output?
```python
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.pop()
print(stack[-1])
```
A) 10
B) 20
C) 30
D) Error

✔ Correct Answer: B

Reason: Stack: [10, 20, 30]. pop() removes 30: [10, 20]. stack[-1] is top element: 20.

Tag: Normal

---

### Question 33
Domain: Data Structures
Topic: Stacks
Subtopic: Stack Underflow
Difficulty: Easy

Question: What is stack underflow?
A) Stack overflow
B) Attempting to pop from empty stack
C) Stack full
D) Stack error

✔ Correct Answer: B

Reason: Stack underflow occurs when popping from empty stack. Should check isEmpty() before pop to avoid error.

Tag: Normal

---

### Question 34
Domain: Data Structures
Topic: Stacks
Subtopic: Stack Overflow
Difficulty: Easy

Question: What is stack overflow?
A) Underflow
B) Attempting to push to full stack (fixed size)
C) Stack empty
D) Stack error

✔ Correct Answer: B

Reason: Stack overflow occurs when pushing to full fixed-size stack. Dynamic stacks (using arrays/lists) grow automatically.

Tag: Normal

---

### Question 35
Domain: Data Structures
Topic: Code Analysis
Subtopic: Stack Peek
Difficulty: Easy

Question: What is the output?
```java
Stack<Integer> stack = new Stack<>();
stack.push(5);
stack.push(10);
System.out.println(stack.peek());
System.out.println(stack.size());
```
A) 5, 1
B) 10, 2
C) 10, 1
D) Error

✔ Correct Answer: B

Reason: peek() returns top element without removing. Top is 10. size() returns 2 (both elements still in stack).

Tag: Normal

---

### Question 36
Domain: Data Structures
Topic: Stack Applications
Subtopic: Function Call Stack
Difficulty: Medium

Question: What does call stack store?
A) Function names
B) Function call information (parameters, return address, local variables)
C) Global variables
D) Code

✔ Correct Answer: B

Reason: Call stack stores activation records with parameters, local variables, return address. Each function call pushes frame, return pops frame.

Tag: Past Paper

---

### Question 37
Domain: Data Structures
Topic: Stack Applications
Subtopic: Expression Evaluation
Difficulty: Hard

Question: What is postfix notation?
A) Prefix notation
B) Operators after operands (3 4 +)
C) Infix notation
D) No notation

✔ Correct Answer: B

Reason: Postfix (Reverse Polish Notation): operators follow operands. 3 4 + means 3+4. No parentheses needed, evaluated with stack.

Tag: Normal

---

### Question 38
Domain: Data Structures
Topic: Code Analysis
Subtopic: Postfix Evaluation
Difficulty: Hard

Question: What is the output?
```python
def eval_postfix(expr):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '*':
                stack.append(a * b)
    return stack[0]

print(eval_postfix("3 4 + 2 *"))
```
A) 9
B) 14
C) 11
D) Error

✔ Correct Answer: B

Reason: 3 4 + = 7, then 7 2 * = 14. Stack-based evaluation.

Tag: Normal

---

### Question 39
Domain: Data Structures
Topic: Stack Applications
Subtopic: Infix to Postfix
Difficulty: Hard

Question: What data structure converts infix to postfix?
A) Queue
B) Stack (for operators)
C) Tree
D) Array

✔ Correct Answer: B

Reason: Stack holds operators based on precedence. Scan infix, output operands immediately, push/pop operators by precedence rules.

Tag: Normal

---

### Question 40
Domain: Data Structures
Topic: Stack Applications
Subtopic: Balanced Parentheses
Difficulty: Medium

Question: What is time complexity of checking balanced parentheses using stack?
A) O(n²)
B) O(n)
C) O(1)
D) O(log n)

✔ Correct Answer: B

Reason: Single pass through string, O(1) operations per character. O(n) time, O(n) space (worst case: all opening).

Tag: Normal

---

### Question 41
Domain: Data Structures
Topic: Code Analysis
Subtopic: Parentheses Matching
Difficulty: Hard

Question: What is the output?
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

print(is_balanced("({[]})"))
print(is_balanced("({[})"))
```
A) True True
B) True False
C) False False
D) False True

✔ Correct Answer: B

Reason: First is balanced: ({[]}) matches correctly. Second is not: ({[}) has mismatched closing.

Tag: Normal

---

### Question 42
Domain: Data Structures
Topic: Queues
Subtopic: Queue Basics
Difficulty: Easy

Question: What principle does queue follow?
A) LIFO
B) FIFO (First In First Out)
C) Random access
D) Priority

✔ Correct Answer: B

Reason: Queue follows FIFO: first element added is first removed. Like waiting line. Operations: enqueue, dequeue.

Tag: Past Paper

---

### Question 43
Domain: Data Structures
Topic: Queues
Subtopic: Queue Operations
Difficulty: Easy

Question: What is time complexity of enqueue and dequeue?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Enqueue adds to rear, dequeue removes from front. Both O(1) with proper implementation (linked list or circular array).

Tag: Past Paper

---

### Question 44
Domain: Data Structures
Topic: Code Analysis
Subtopic: Queue Using List
Difficulty: Medium

Question: What is the output?
```python
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue[0])
```
A) 1
B) 2
C) 3
D) Error

✔ Correct Answer: B

Reason: Queue: [1, 2, 3]. popleft() removes 1: [2, 3]. queue[0] is front: 2.

Tag: Normal

---

### Question 45
Domain: Data Structures
Topic: Queues
Subtopic: Circular Queue
Difficulty: Medium

Question: What is advantage of circular queue?
A) Circular shape
B) Reuses empty space at beginning
C) Faster operations
D) No advantage

✔ Correct Answer: B

Reason: Circular queue wraps around, reusing space freed by dequeue. Linear queue wastes space at beginning. Uses modulo arithmetic.

Tag: Normal

---

### Question 46
Domain: Data Structures
Topic: Code Analysis
Subtopic: Circular Queue
Difficulty: Hard

Question: In circular queue with size 5, if front=3 and rear=1, how many elements?
A) 2
B) 4
C) 3
D) 1

✔ Correct Answer: B

Reason: Circular: rear wrapped around. Elements at indices 3, 4, 0, 1. Count: (rear - front + size) % size + 1 = (1-3+5)%5+1 = 4.

Tag: Normal

---

### Question 47
Domain: Data Structures
Topic: Deque
Subtopic: Double-Ended Queue
Difficulty: Medium

Question: What operations does deque support?
A) One end only
B) Insert and delete at both ends
C) Middle only
D) Random access only

✔ Correct Answer: B

Reason: Deque (double-ended queue) supports O(1) operations at both ends: appendleft, append, popleft, pop.

Tag: Past Paper

---

### Question 48
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
dq.pop()
print(list(dq))
```
A) [1, 2, 3]
B) [1, 2, 3]
C) [0, 1, 2, 3, 4]
D) [2, 3]

✔ Correct Answer: A

Reason: Start [1,2,3], appendleft(0)→[0,1,2,3], append(4)→[0,1,2,3,4], popleft()→[1,2,3,4], pop()→[1,2,3].

Tag: Normal

---

### Question 49
Domain: Data Structures
Topic: Priority Queue
Subtopic: PQ Basics
Difficulty: Medium

Question: What is priority queue?
A) Fast queue
B) Queue where elements have priorities, highest priority dequeued first
C) FIFO queue
D) Stack

✔ Correct Answer: B

Reason: Priority queue serves elements by priority, not insertion order. Typically implemented with heap for O(log n) operations.

Tag: Past Paper

---

### Question 50
Domain: Data Structures
Topic: Priority Queue
Subtopic: PQ Implementation
Difficulty: Hard

Question: What data structure efficiently implements priority queue?
A) Array
B) Heap
C) Linked list
D) Stack

✔ Correct Answer: B

Reason: Heap provides O(log n) insert and delete-max/min. Array: O(n) for one operation. Heap is optimal for priority queue.

Tag: Past Paper

---

### Question 51
Domain: Data Structures
Topic: Code Analysis
Subtopic: Priority Queue Usage
Difficulty: Medium

Question: What is the output?
```python
import heapq
pq = []
heapq.heappush(pq, (2, 'task2'))
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (3, 'task3'))
print(heapq.heappop(pq)[1])
```
A) task3
B) task1
C) task2
D) Error

✔ Correct Answer: B

Reason: Min heap by priority. Lowest priority (1, 'task1') dequeued first. [1] accesses task name: 'task1'.

Tag: Normal

---

### Question 52
Domain: Data Structures
Topic: Binary Trees
Subtopic: Tree Basics
Difficulty: Easy

Question: What is binary tree?
A) Two trees
B) Tree where each node has at most two children
C) Tree with two nodes
D) Sorted tree

✔ Correct Answer: B

Reason: Binary tree: each node has at most 2 children (left and right). Can have 0, 1, or 2 children.

Tag: Past Paper

---

### Question 53
Domain: Data Structures
Topic: Binary Trees
Subtopic: Tree Terminology
Difficulty: Easy

Question: What is leaf node?
A) First node
B) Node with no children
C) Root node
D) Parent node

✔ Correct Answer: B

Reason: Leaf (terminal) node has no children. Internal nodes have at least one child. Root is topmost node.

Tag: Normal

---

### Question 54
Domain: Data Structures
Topic: Code Analysis
Subtopic: Tree Node Structure
Difficulty: Easy

Question: What does binary tree node contain?
```cpp
struct Node {
    int data;
    Node* left;
    Node* right;
};
```
A) Data only
B) Data and two child pointers
C) Data and parent
D) Index and data

✔ Correct Answer: B

Reason: Binary tree node contains data, left child pointer, right child pointer. May optionally include parent pointer.

Tag: Normal

---

### Question 55
Domain: Data Structures
Topic: Binary Trees
Subtopic: Tree Height
Difficulty: Medium

Question: What is height of tree with single node?
A) 0
B) 1
C) -1
D) Undefined

✔ Correct Answer: B

Reason: Height is number of edges on longest path to leaf. Single node (root) has height 1. Empty tree: height 0 (or -1 by some definitions).

Tag: Normal

---

### Question 56
Domain: Data Structures
Topic: Binary Trees
Subtopic: Tree Depth
Difficulty: Easy

Question: What is depth of root node?
A) 1
B) 0
C) -1
D) Height

✔ Correct Answer: B

Reason: Depth is number of edges from root to node. Root has depth 0. Height measured from bottom, depth from top.

Tag: Normal

---

### Question 57
Domain: Data Structures
Topic: Code Analysis
Subtopic: Count Nodes
Difficulty: Medium

Question: What is the output?
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(count_nodes(root))
```
A) 3
B) 4
C) 5
D) 2

✔ Correct Answer: B

Reason: Recursively counts nodes. Tree has 4 nodes: 1, 2, 3, 4. Returns 4.

Tag: Normal

---

### Question 58
Domain: Data Structures
Topic: Binary Trees
Subtopic: Full Binary Tree
Difficulty: Medium

Question: What is full binary tree?
A) Tree is full
B) Every node has 0 or 2 children
C) All levels filled
D) Balanced tree

✔ Correct Answer: B

Reason: Full binary tree: every node has either 0 children (leaf) or 2 children. No nodes with single child.

Tag: Past Paper

---

### Question 59
Domain: Data Structures
Topic: Binary Trees
Subtopic: Complete Binary Tree
Difficulty: Medium

Question: What is complete binary tree?
A) Fully filled
B) All levels filled except possibly last, filled left to right
C) Balanced tree
D) Full tree

✔ Correct Answer: B

Reason: Complete binary tree: all levels filled except last, last level filled left to right. Used in heaps.

Tag: Past Paper

---

### Question 60
Domain: Data Structures
Topic: Binary Trees
Subtopic: Perfect Binary Tree
Difficulty: Medium

Question: What is perfect binary tree?
A) Best tree
B) All internal nodes have 2 children, all leaves at same level
C) Balanced tree
D) Complete tree

✔ Correct Answer: B

Reason: Perfect binary tree: all internal nodes have 2 children, all leaves at same depth. Has 2^h - 1 nodes for height h.

Tag: Normal

---

### Question 61
Domain: Data Structures
Topic: Code Analysis
Subtopic: Tree Levels
Difficulty: Medium

Question: How many nodes in perfect binary tree of height 3?
A) 3
B) 7
C) 8
D) 15

✔ Correct Answer: B

Reason: Perfect tree with height h has 2^h - 1 nodes. Height 3: 2³ - 1 = 7 nodes.

Tag: Normal

---

### Question 62
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Inorder Traversal
Difficulty: Medium

Question: What is inorder traversal sequence?
A) Root, Left, Right
B) Left, Root, Right
C) Left, Right, Root
D) Right, Root, Left

✔ Correct Answer: B

Reason: Inorder: Left subtree, Root, Right subtree. For BST, gives sorted order.

Tag: Past Paper

---

### Question 63
Domain: Data Structures
Topic: Code Analysis
Subtopic: Inorder Implementation
Difficulty: Hard

Question: What is the output?
```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# Tree:     2
#          / \
#         1   3
root = Node(2)
root.left = Node(1)
root.right = Node(3)
inorder(root)
```
A) 2 1 3
B) 1 2 3
C) 1 3 2
D) 3 2 1

✔ Correct Answer: B

Reason: Inorder: left(1), root(2), right(3). Outputs: 1 2 3.

Tag: Normal

---

### Question 64
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Preorder Traversal
Difficulty: Medium

Question: What is preorder traversal sequence?
A) Left, Root, Right
B) Root, Left, Right
C) Left, Right, Root
D) Right, Left, Root

✔ Correct Answer: B

Reason: Preorder: Root, Left subtree, Right subtree. Used for creating copy of tree.

Tag: Past Paper

---

### Question 65
Domain: Data Structures
Topic: Code Analysis
Subtopic: Preorder Implementation
Difficulty: Medium

Question: What is the output?
```python
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

# Tree:     2
#          / \
#         1   3
root = Node(2)
root.left = Node(1)
root.right = Node(3)
preorder(root)
```
A) 1 2 3
B) 2 1 3
C) 1 3 2
D) 3 2 1

✔ Correct Answer: B

Reason: Preorder: root(2), left(1), right(3). Outputs: 2 1 3.

Tag: Normal

---

### Question 66
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Postorder Traversal
Difficulty: Medium

Question: What is postorder traversal sequence?
A) Root, Left, Right
B) Left, Right, Root
C) Left, Root, Right
D) Right, Root, Left

✔ Correct Answer: B

Reason: Postorder: Left subtree, Right subtree, Root. Used for deleting tree or evaluating expression trees.

Tag: Past Paper

---

### Question 67
Domain: Data Structures
Topic: Code Analysis
Subtopic: Postorder Implementation
Difficulty: Medium

Question: What is the output?
```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

# Tree:     2
#          / \
#         1   3
root = Node(2)
root.left = Node(1)
root.right = Node(3)
postorder(root)
```
A) 2 1 3
B) 1 3 2
C) 1 2 3
D) 3 2 1

✔ Correct Answer: B

Reason: Postorder: left(1), right(3), root(2). Outputs: 1 3 2.

Tag: Normal

---

### Question 68
Domain: Data Structures
Topic: Tree Traversal
Subtopic: Level Order Traversal
Difficulty: Hard

Question: What data structure is used for level order traversal?
A) Stack
B) Queue
C) Array
D) Linked list

✔ Correct Answer: B

Reason: Level order (BFS) uses queue. Enqueue root, dequeue, enqueue children, repeat. Visits level by level.

Tag: Past Paper

---

### Question 69
Domain: Data Structures
Topic: Code Analysis
Subtopic: Level Order Implementation
Difficulty: Hard

Question: What is the output?
```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Tree:     1
#          / \
#         2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)
level_order(root)
```
A) 2 1 3
B) 1 2 3
C) 1 3 2
D) 3 2 1

✔ Correct Answer: B

Reason: Level order: level 0 (1), level 1 (2, 3). Outputs: 1 2 3.

Tag: Normal

---

### Question 70
Domain: Data Structures
Topic: Binary Search Trees
Subtopic: BST Property
Difficulty: Medium

Question: What is BST property?
A) Balanced tree
B) Left subtree values < root < right subtree values
C) Complete tree
D) Full tree

✔ Correct Answer: B

Reason: BST property: all left subtree values less than root, all right subtree values greater. Enables efficient search.

Tag: Past Paper

---

### Question 71
Domain: Data Structures
Topic: Code Analysis
Subtopic: BST Search
Difficulty: Hard

Question: What is the output?
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search_bst(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search_bst(root.left, key)
    return search_bst(root.right, key)

# BST:      5
#          / \
#         3   7
root = Node(5)
root.left = Node(3)
root.right = Node(7)
result = search_bst(root, 7)
print(result.data if result else "Not found")
```
A) 5
B) 7
C) Not found
D) Error

✔ Correct Answer: B

Reason: Searches BST for 7. 7 > 5, goes right, finds 7. Returns node with data 7.

Tag: Normal

---

### Question 72
Domain: Data Structures
Topic: Binary Search Trees
Subtopic: BST Search Complexity
Difficulty: Medium

Question: What is time complexity of BST search in balanced tree?
A) O(n)
B) O(log n)
C) O(1)
D) O(n²)

✔ Correct Answer: B

Reason: Balanced BST has height log n. Each comparison eliminates half of tree. O(log n) time. Unbalanced worst case: O(n).

Tag: Past Paper

---

### Question 73
Domain: Data Structures
Topic: Binary Search Trees
Subtopic: BST Insertion
Difficulty: Medium

Question: What is time complexity of BST insertion in balanced tree?
A) O(n)
B) O(log n)
C) O(1)
D) O(n²)

✔ Correct Answer: B

Reason: Search for position (O(log n)), insert node (O(1)). Total: O(log n) in balanced tree.

Tag: Past Paper

---

### Question 74
Domain: Data Structures
Topic: Code Analysis
Subtopic: BST Insertion
Difficulty: Hard

Question: What is the output?
```python
def insert_bst(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert_bst(root.left, key)
    else:
        root.right = insert_bst(root.right, key)
    return root

root = Node(5)
root = insert_bst(root, 3)
root = insert_bst(root, 7)
root = insert_bst(root, 1)
# Inorder traversal gives?
```
A) 5 3 7 1
B) 1 3 5 7
C) 7 5 3 1
D) Error

✔ Correct Answer: B

Reason: BST insertions maintain property. Inorder traversal of BST gives sorted order: 1 3 5 7.

Tag: Normal

---

### Question 75
Domain: Data Structures
Topic: Binary Search Trees
Subtopic: BST Deletion
Difficulty: Hard

Question: What is most complex case in BST deletion?
A) Leaf node
B) Node with two children
C) Node with one child
D) Root node

✔ Correct Answer: B

Reason: Deleting node with two children requires finding inorder successor (or predecessor), replacing value, deleting successor. Most complex case.

Tag: Normal

---

### Question 76
Domain: Data Structures
Topic: Code Analysis
Subtopic: BST Minimum
Difficulty: Medium

Question: What is the output?
```python
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.data

# BST:      5
#          / \
#         3   7
#        /
#       1
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
print(find_min(root))
```
A) 5
B) 1
C) 3
D) 7

✔ Correct Answer: B

Reason: Minimum in BST is leftmost node. Traverse left until no left child. Finds 1.

Tag: Normal

---

### Question 77
Domain: Data Structures
Topic: Binary Search Trees
Subtopic: BST Maximum
Difficulty: Easy

Question: Where is maximum element in BST?
A) Root
B) Rightmost node
C) Leftmost node
D) Random

✔ Correct Answer: B

Reason: Maximum in BST is rightmost node. Traverse right until no right child.

Tag: Normal

---

### Question 78
Domain: Data Structures
Topic: Binary Search Trees
Subtopic: Inorder Successor
Difficulty: Hard

Question: What is inorder successor of node in BST?
A) Next node
B) Node with next larger value
C) Right child
D) Parent

✔ Correct Answer: B

Reason: Inorder successor is node with next larger value. If right subtree exists, successor is leftmost in right subtree.

Tag: Normal

---

### Question 79
Domain: Data Structures
Topic: Code Analysis
Subtopic: BST Validation
Difficulty: Hard

Question: What is the output?
```python
def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.data <= min_val or root.data >= max_val:
        return False
    return (is_bst(root.left, min_val, root.data) and
            is_bst(root.right, root.data, max_val))

# Tree:     5
#          / \
#         3   7
#        /
#       6
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(6)
print(is_bst(root))
```
A) True
B) False
C) Error
D) None

✔ Correct Answer: B

Reason: Node 6 in left subtree of 5 but 6 > 5. Violates BST property. Returns False.

Tag: Normal

---

### Question 80
Domain: Data Structures
Topic: AVL Trees
Subtopic: Balanced BST
Difficulty: Hard

Question: What is AVL tree?
A) Any tree
B) Self-balancing BST where heights of subtrees differ by at most 1
C) Unbalanced tree
D) Binary tree

✔ Correct Answer: B

Reason: AVL tree maintains balance: |height(left) - height(right)| ≤ 1 for all nodes. Guarantees O(log n) operations through rotations.

Tag: Past Paper

---

### Question 81
Domain: Data Structures
Topic: AVL Trees
Subtopic: Balance Factor
Difficulty: Hard

Question: What is balance factor?
A) Tree size
B) height(left subtree) - height(right subtree)
C) Node count
D) Tree depth

✔ Correct Answer: B

Reason: Balance factor = height(left) - height(right). AVL tree: balance factor must be -1, 0, or 1 for all nodes.

Tag: Normal

---

### Question 82
Domain: Data Structures
Topic: Code Analysis
Subtopic: AVL Balance Check
Difficulty: Hard

Question: Which balance factor violates AVL property?
A) 0
B) 2
C) 1
D) -1

✔ Correct Answer: B

Reason: AVL allows balance factors: -1, 0, 1. Balance factor 2 or -2 violates property, requires rotation.

Tag: Normal

---

### Question 83
Domain: Data Structures
Topic: AVL Trees
Subtopic: Rotations
Difficulty: Hard

Question: What are the four types of AVL rotations?
A) Up, Down, Left, Right
B) LL, RR, LR, RL
C) Single, Double
D) Forward, Backward

✔ Correct Answer: B

Reason: Four rotations: Left-Left (right rotation), Right-Right (left rotation), Left-Right (left then right), Right-Left (right then left).

Tag: Normal

---

### Question 84
Domain: Data Structures
Topic: AVL Trees
Subtopic: Rotation Complexity
Difficulty: Medium

Question: What is time complexity of AVL rotation?
A) O(n)
B) O(1)
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Rotation updates few pointers (constant number). O(1) time. Insertion/deletion: O(log n) search + O(1) rotation = O(log n).

Tag: Normal

---

### Question 85
Domain: Data Structures
Topic: Code Analysis
Subtopic: Right Rotation
Difficulty: Hard

Question: What does right rotation do?
```
    y              x
   / \            / \
  x   C    →     A   y
 / \                / \
A   B              B   C
```
A) Rotates right
B) Makes x root, y becomes right child
C) Deletes node
D) Balances always

✔ Correct Answer: B

Reason: Right rotation: x becomes new root, y becomes x's right child, B becomes y's left child. Used for LL case.

Tag: Normal

---

### Question 86
Domain: Data Structures
Topic: Red-Black Trees
Subtopic: RB Tree Properties
Difficulty: Hard

Question: What is Red-Black tree property?
A) All nodes red
B) Self-balancing BST with color property (red/black nodes)
C) All nodes black
D) Colored tree

✔ Correct Answer: B

Reason: Red-Black tree: BST with color property ensuring balance. Root black, red nodes have black children, all paths have same black height.

Tag: Normal

---

### Question 87
Domain: Data Structures
Topic: Red-Black Trees
Subtopic: RB vs AVL
Difficulty: Hard

Question: What's the difference between AVL and Red-Black trees?
A) No difference
B) AVL more strictly balanced, RB faster insertions/deletions
C) RB is balanced, AVL isn't
D) AVL is deprecated

✔ Correct Answer: B

Reason: AVL more strictly balanced (better search). Red-Black allows more imbalance (faster insert/delete, fewer rotations). Both O(log n).

Tag: Normal

---

### Question 88
Domain: Data Structures
Topic: B-Trees
Subtopic: B-Tree Basics
Difficulty: Hard

Question: What is B-tree?
A) Binary tree
B) Self-balancing tree with nodes having multiple keys and children
C) Balanced tree
D) B-type tree

✔ Correct Answer: B

Reason: B-tree: self-balancing, nodes have multiple keys (sorted) and children. Used in databases, file systems. Minimizes disk I/O.

Tag: Normal

---

### Question 89
Domain: Data Structures
Topic: B-Trees
Subtopic: B-Tree Order
Difficulty: Hard

Question: What does order m mean in B-tree?
A) m nodes
B) Maximum m children per node
C) m levels
D) m keys

✔ Correct Answer: B

Reason: B-tree of order m: each node has at most m children and m-1 keys. Minimum children: ⌈m/2⌉ (except root).

Tag: Normal

---

### Question 90
Domain: Data Structures
Topic: Code Analysis
Subtopic: B-Tree Properties
Difficulty: Hard

Question: Why are B-trees used in databases?
A) Faster
B) Minimize disk I/O by storing multiple keys per node
C) Simpler
D) Less memory

✔ Correct Answer: B

Reason: B-trees have high fanout (many children), reducing tree height. Fewer disk accesses needed. Node size matches disk block size.

Tag: Normal

---

### Question 91
Domain: Data Structures
Topic: Heaps
Subtopic: Heap Property
Difficulty: Medium

Question: What is max heap property?
A) Maximum size
B) Parent value ≥ children values
C) Parent value ≤ children values
D) Sorted array

✔ Correct Answer: B

Reason: Max heap: parent ≥ children. Root is maximum. Min heap: parent ≤ children. Root is minimum.

Tag: Past Paper

---

### Question 92
Domain: Data Structures
Topic: Heaps
Subtopic: Heap Representation
Difficulty: Medium

Question: How is binary heap typically stored?
A) Linked list
B) Array
C) Matrix
D) Tree pointers

✔ Correct Answer: B

Reason: Binary heap stored in array. For index i: left child at 2i+1, right child at 2i+2, parent at (i-1)/2. Space-efficient.

Tag: Past Paper

---

### Question 93
Domain: Data Structures
Topic: Code Analysis
Subtopic: Heap Array Indexing
Difficulty: Medium

Question: In array-based heap, if parent is at index 3, where are children?
A) 4 and 5
B) 7 and 8
C) 6 and 7
D) 1 and 2

✔ Correct Answer: B

Reason: Left child: 2*3+1 = 7. Right child: 2*3+2 = 8. Children at indices 7 and 8.

Tag: Normal

---

### Question 94
Domain: Data Structures
Topic: Heaps
Subtopic: Heap Insertion
Difficulty: Medium

Question: What is time complexity of inserting into heap?
A) O(1)
B) O(log n)
C) O(n)
D) O(n²)

✔ Correct Answer: B

Reason: Insert at end (O(1)), bubble up to maintain heap property (O(log n) worst case). Total: O(log n).

Tag: Past Paper

---

### Question 95
Domain: Data Structures
Topic: Code Analysis
Subtopic: Heapify Up
Difficulty: Hard

Question: What does heapify up do?
```python
def heapify_up(heap, index):
    parent = (index - 1) // 2
    if index > 0 and heap[index] > heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        heapify_up(heap, parent)
```
A) Sorts heap
B) Moves element up until heap property satisfied
C) Deletes element
D) Error

✔ Correct Answer: B

Reason: Compares with parent, swaps if violates max heap property, recursively continues. Restores heap property after insertion.

Tag: Normal

---

### Question 96
Domain: Data Structures
Topic: Heaps
Subtopic: Extract Max
Difficulty: Medium

Question: What is time complexity of extracting maximum from max heap?
A) O(1)
B) O(log n)
C) O(n)
D) O(n²)

✔ Correct Answer: B

Reason: Remove root (O(1)), move last element to root (O(1)), heapify down (O(log n)). Total: O(log n).

Tag: Past Paper

---

### Question 97
Domain: Data Structures
Topic: Code Analysis
Subtopic: Heapify Down
Difficulty: Hard

Question: What does heapify down do after extracting root?
A) Deletes heap
B) Moves root down, swapping with larger child until heap property satisfied
C) Sorts heap
D) Nothing

✔ Correct Answer: B

Reason: After moving last element to root, heapify down compares with children, swaps with larger child, continues until heap property restored.

Tag: Normal

---

### Question 98
Domain: Data Structures
Topic: Heaps
Subtopic: Build Heap
Difficulty: Hard

Question: What is time complexity of building heap from n elements?
A) O(n²)
B) O(n)
C) O(n log n)
D) O(log n)

✔ Correct Answer: B

Reason: Build heap by heapifying from last non-leaf to root. Appears O(n log n) but mathematical analysis proves O(n).

Tag: Normal

---

### Question 99
Domain: Data Structures
Topic: Code Analysis
Subtopic: Heap Sort
Difficulty: Hard

Question: What is time complexity of heap sort?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: Build heap O(n), extract max n times O(log n each). Total: O(n log n) all cases. In-place, not stable.

Tag: Past Paper

---

### Question 100
Domain: Data Structures
Topic: Heaps
Subtopic: Heap Applications
Difficulty: Easy

Question: What is primary use of heap?
A) Sorting only
B) Implementing priority queue
C) Searching
D) Storage

✔ Correct Answer: B

Reason: Heaps efficiently implement priority queues with O(log n) insert and extract-min/max. Also used in heap sort, graph algorithms.

Tag: Normal

---

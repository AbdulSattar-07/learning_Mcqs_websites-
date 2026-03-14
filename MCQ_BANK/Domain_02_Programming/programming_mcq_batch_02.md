# Programming - MCQ Batch 02
## Questions 101-200

---

### Question 101
Domain: Programming
Topic: Collections
Subtopic: ArrayList vs Array
Difficulty: Medium

Question: What is the main advantage of ArrayList over arrays in Java?
A) Faster access
B) Dynamic size adjustment
C) Less memory usage
D) Simpler syntax

✔ Correct Answer: B

Reason: ArrayList can dynamically grow or shrink, while arrays have fixed size. ArrayList provides flexibility at the cost of slight performance overhead.

Tag: Normal

---

### Question 102
Domain: Programming
Topic: Collections
Subtopic: LinkedList
Difficulty: Medium

Question: When is LinkedList preferred over ArrayList?
A) Random access
B) Frequent insertions/deletions at beginning or middle
C: Always
D) Never

✔ Correct Answer: B

Reason: LinkedList excels at insertions/deletions (O(1) at ends) but slower random access (O(n)). ArrayList is opposite: fast access, slow insertions.

Tag: Normal

---

### Question 103
Domain: Programming
Topic: Collections
Subtopic: HashMap
Difficulty: Easy

Question: What data structure does HashMap implement?
A) List
B) Key-value pairs
C) Queue
D) Stack

✔ Correct Answer: B

Reason: HashMap stores key-value pairs, providing fast O(1) average-case lookup, insertion, and deletion using hash-based indexing.

Tag: Past Paper

---

### Question 104
Domain: Programming
Topic: Collections
Subtopic: HashSet
Difficulty: Easy

Question: What is the key characteristic of a Set?
A) Allows duplicates
B) No duplicate elements
C) Ordered elements
D) Fixed size

✔ Correct Answer: B

Reason: Sets store unique elements only, automatically rejecting duplicates. HashSet uses hashing for O(1) operations but doesn't maintain order.

Tag: Normal

---

### Question 105
Domain: Programming
Topic: Collections
Subtopic: TreeMap
Difficulty: Medium

Question: How does TreeMap differ from HashMap?
A) Faster
B) Maintains sorted order of keys
C) Allows duplicates
D) Uses less memory

✔ Correct Answer: B

Reason: TreeMap maintains keys in sorted order using Red-Black tree (O(log n) operations), while HashMap is unordered but faster (O(1) average).

Tag: Normal

---



### Question 106
Domain: Programming
Topic: Code Analysis
Subtopic: HashMap Operations
Difficulty: Medium

Question: What is the output?
```java
HashMap<String, Integer> map = new HashMap<>();
map.put("A", 1);
map.put("A", 2);
System.out.println(map.get("A"));
```
A) 1
B) 2
C) 3
D) Error

✔ Correct Answer: B

Reason: HashMap doesn't allow duplicate keys. Second put("A", 2) overwrites the first value, so get("A") returns 2.

Tag: Normal

---

### Question 107
Domain: Programming
Topic: Collections
Subtopic: Queue
Difficulty: Easy

Question: What principle does a Queue follow?
A) LIFO
B) FIFO
C) Random access
D) Sorted order

✔ Correct Answer: B

Reason: Queue follows FIFO (First In First Out) - elements are removed in the order they were added, like a line of people.

Tag: Past Paper

---

### Question 108
Domain: Programming
Topic: Collections
Subtopic: Stack
Difficulty: Easy

Question: What principle does a Stack follow?
A) FIFO
B) LIFO
C) Random access
D) Sorted order

✔ Correct Answer: B

Reason: Stack follows LIFO (Last In First Out) - the most recently added element is removed first, like a stack of plates.

Tag: Past Paper

---

### Question 109
Domain: Programming
Topic: Code Analysis
Subtopic: Stack Operations
Difficulty: Medium

Question: What is the output?
```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack.pop())
```
A) 1
B) 2
C) 3
D) Error

✔ Correct Answer: C

Reason: Stack operations: push 1, 2, 3. pop() removes and returns the last element (top of stack): 3.

Tag: Normal

---

### Question 110
Domain: Programming
Topic: Algorithms
Subtopic: Time Complexity
Difficulty: Medium

Question: What is the time complexity of binary search?
A) O(n)
B) O(log n)
C) O(n²)
D) O(1)

✔ Correct Answer: B

Reason: Binary search divides search space in half each iteration, resulting in O(log n) time complexity for sorted arrays.

Tag: Past Paper

---

### Question 111
Domain: Programming
Topic: Algorithms
Subtopic: Linear Search
Difficulty: Easy

Question: What is the worst-case time complexity of linear search?
A) O(1)
B) O(log n)
C) O(n)
D) O(n²)

✔ Correct Answer: C

Reason: Linear search checks each element sequentially. In worst case (element not found or at end), it checks all n elements: O(n).

Tag: Normal

---

### Question 112
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Bubble Sort
Difficulty: Medium

Question: What is the time complexity of bubble sort in worst case?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✔ Correct Answer: C

Reason: Bubble sort uses nested loops, comparing and swapping adjacent elements. Worst case requires n*(n-1)/2 comparisons: O(n²).

Tag: Past Paper

---

### Question 113
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Quick Sort
Difficulty: Hard

Question: What is the average-case time complexity of quick sort?
A) O(n)
B) O(n log n)
C) O(n²)
D) O(log n)

✔ Correct Answer: B

Reason: Quick sort's average case is O(n log n) with good pivot selection. Worst case (already sorted with bad pivot) is O(n²).

Tag: Normal

---

### Question 114
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Merge Sort
Difficulty: Medium

Question: What is merge sort's time complexity in all cases?
A) O(n)
B) O(n log n)
C) O(n²)
D) Varies

✔ Correct Answer: B

Reason: Merge sort consistently performs at O(n log n) in best, average, and worst cases due to divide-and-conquer approach.

Tag: Normal

---

### Question 115
Domain: Programming
Topic: Code Analysis
Subtopic: Recursion Trace
Difficulty: Hard

Question: What does this return for fib(5)?
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
A) 3
B) 5
C) 8
D) 13

✔ Correct Answer: B

Reason: fib(5) = fib(4) + fib(3) = 3 + 2 = 5. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8...

Tag: Past Paper

---

### Question 116
Domain: Programming
Topic: String Manipulation
Subtopic: String Methods
Difficulty: Easy

Question: What does the substring method do?
A) Adds strings
B) Extracts portion of string
C) Deletes string
D) Reverses string

✔ Correct Answer: B

Reason: substring() extracts a portion of string between specified indices, returning a new string without modifying the original.

Tag: Normal

---

### Question 117
Domain: Programming
Topic: Code Analysis
Subtopic: String Concatenation
Difficulty: Medium

Question: What is the output?
```java
String s1 = "Hello";
String s2 = "World";
System.out.println(s1 + " " + s2);
```
A) HelloWorld
B) Hello World
C) Error
D) null

✔ Correct Answer: B

Reason: The + operator concatenates strings. s1 + " " + s2 produces "Hello" + " " + "World" = "Hello World".

Tag: Normal

---

### Question 118
Domain: Programming
Topic: String Manipulation
Subtopic: StringBuilder
Difficulty: Medium

Question: Why use StringBuilder instead of String concatenation in loops?
A) Simpler syntax
B) Better performance, avoids creating many temporary objects
C) Required by compiler
D) No difference

✔ Correct Answer: B

Reason: String concatenation in loops creates many temporary immutable String objects. StringBuilder is mutable and efficient for repeated modifications.

Tag: Normal

---

### Question 119
Domain: Programming
Topic: Code Analysis
Subtopic: String Comparison
Difficulty: Hard

Question: What is the output in Java?
```java
String s1 = "test";
String s2 = "test";
String s3 = new String("test");
System.out.println(s1 == s2);
System.out.println(s1 == s3);
```
A) true, true
B) true, false
C) false, false
D) false, true

✔ Correct Answer: B

Reason: s1 and s2 reference same string literal in pool (true). s3 is new object with different reference (false). Use equals() for content comparison.

Tag: Normal

---

### Question 120
Domain: Programming
Topic: Regular Expressions
Subtopic: Pattern Matching
Difficulty: Medium

Question: What does the regex pattern "\\d+" match?
A) One digit
B) One or more digits
C) Any character
D) Letters only

✔ Correct Answer: B

Reason: \\d matches a digit, + means one or more. So \\d+ matches sequences of one or more consecutive digits.

Tag: Normal

---



### Question 121
Domain: Programming
Topic: Regular Expressions
Subtopic: Metacharacters
Difficulty: Medium

Question: What does the regex pattern "^test$" match?
A) Any string containing "test"
B) Exactly "test" as complete string
C) Strings starting with "test"
D) Strings ending with "test"

✔ Correct Answer: B

Reason: ^ anchors to start, $ anchors to end. ^test$ matches only strings that are exactly "test" with nothing before or after.

Tag: Normal

---

### Question 122
Domain: Programming
Topic: Lambda Expressions
Subtopic: Lambda Basics
Difficulty: Medium

Question: What are lambda expressions?
A) Greek letters
B) Anonymous functions with concise syntax
C) Named functions
D) Class methods

✔ Correct Answer: B

Reason: Lambda expressions are anonymous (unnamed) functions with concise syntax, useful for short operations passed as arguments.

Tag: Normal

---

### Question 123
Domain: Programming
Topic: Code Analysis
Subtopic: Lambda in Python
Difficulty: Medium

Question: What is the output?
```python
f = lambda x: x * 2
print(f(5))
```
A) 5
B) 10
C) 25
D) Error

✔ Correct Answer: B

Reason: Lambda creates anonymous function that doubles input. f(5) returns 5 * 2 = 10.

Tag: Normal

---

### Question 124
Domain: Programming
Topic: Functional Programming
Subtopic: Map Function
Difficulty: Medium

Question: What does the map function do?
A) Creates maps
B) Applies function to each element in collection
C) Filters elements
D) Sorts elements

✔ Correct Answer: B

Reason: map() applies a given function to each element in a collection, returning new collection with transformed elements.

Tag: Normal

---

### Question 125
Domain: Programming
Topic: Functional Programming
Subtopic: Filter Function
Difficulty: Easy

Question: What does the filter function do?
A) Removes all elements
B) Returns elements that satisfy a condition
C) Sorts elements
D) Transforms elements

✔ Correct Answer: B

Reason: filter() returns a new collection containing only elements that satisfy the given predicate/condition function.

Tag: Normal

---

### Question 126
Domain: Programming
Topic: Functional Programming
Subtopic: Reduce Function
Difficulty: Hard

Question: What does reduce function do?
A) Reduces size
B) Reduces collection to single value by applying function cumulatively
C) Removes elements
D) Sorts elements

✔ Correct Answer: B

Reason: reduce() applies a function cumulatively to elements, reducing the collection to a single value (sum, product, concatenation, etc.).

Tag: Normal

---

### Question 127
Domain: Programming
Topic: Code Analysis
Subtopic: Map Function
Difficulty: Medium

Question: What is the output?
```python
nums = [1, 2, 3, 4]
result = list(map(lambda x: x**2, nums))
print(result)
```
A) [1, 2, 3, 4]
B) [1, 4, 9, 16]
C) [2, 4, 6, 8]
D) Error

✔ Correct Answer: B

Reason: map applies lambda (squares each number) to each element: 1²=1, 2²=4, 3²=9, 4²=16.

Tag: Normal

---

### Question 128
Domain: Programming
Topic: Code Analysis
Subtopic: Filter Function
Difficulty: Medium

Question: What is the output?
```python
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
```
A) [1, 3, 5]
B) [2, 4, 6]
C) [1, 2, 3, 4, 5, 6]
D) []

✔ Correct Answer: B

Reason: filter keeps elements where lambda returns True. x % 2 == 0 is true for even numbers: 2, 4, 6.

Tag: Normal

---

### Question 129
Domain: Programming
Topic: Decorators
Subtopic: Python Decorators
Difficulty: Hard

Question: What is a decorator in Python?
A) Design pattern
B) Function that modifies another function's behavior
C) Class decorator
D) Variable modifier

✔ Correct Answer: B

Reason: Decorators are functions that wrap other functions to modify their behavior without changing their code, using @decorator syntax.

Tag: Normal

---

### Question 130
Domain: Programming
Topic: Generators
Subtopic: Python Generators
Difficulty: Hard

Question: What does yield keyword do in Python?
A) Returns and exits
B) Returns value and pauses, resuming on next call
C) Stops execution
D) Raises exception

✔ Correct Answer: B

Reason: yield returns a value and pauses function execution, maintaining state. Next call resumes from where it paused, creating generators.

Tag: Normal

---

### Question 131
Domain: Programming
Topic: Code Analysis
Subtopic: Generator Output
Difficulty: Hard

Question: What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
```
A) 1 1
B) 1 2
C) 2 3
D) Error

✔ Correct Answer: B

Reason: First next(g) returns 1 and pauses. Second next(g) resumes and returns 2. Generators maintain state between calls.

Tag: Normal

---

### Question 132
Domain: Programming
Topic: Iterators
Subtopic: Iterator Protocol
Difficulty: Medium

Question: What methods must an iterator implement in Python?
A) next() only
B) __iter__() and __next__()
C) __init__() only
D) get() and set()

✔ Correct Answer: B

Reason: Python iterators must implement __iter__() (returns self) and __next__() (returns next value or raises StopIteration).

Tag: Normal

---

### Question 133
Domain: Programming
Topic: List Comprehension
Subtopic: Python List Comprehension
Difficulty: Medium

Question: What is the output?
```python
result = [x*2 for x in range(5) if x % 2 == 0]
print(result)
```
A) [0, 2, 4, 6, 8]
B) [0, 4, 8]
C) [2, 4, 6, 8]
D) [0, 2, 4]

✔ Correct Answer: B

Reason: range(5) gives 0,1,2,3,4. Filter even (0,2,4), multiply by 2: [0, 4, 8].

Tag: Normal

---

### Question 134
Domain: Programming
Topic: Dictionary Comprehension
Subtopic: Python Dict Comprehension
Difficulty: Hard

Question: What is the output?
```python
d = {x: x**2 for x in range(1, 4)}
print(d)
```
A) {1: 1, 2: 4, 3: 9}
B) [1, 4, 9]
C) {0: 0, 1: 1, 2: 4}
D) Error

✔ Correct Answer: A

Reason: Dict comprehension creates dictionary with x as key and x² as value for x in 1, 2, 3.

Tag: Normal

---

### Question 135
Domain: Programming
Topic: Closures
Subtopic: Closure Basics
Difficulty: Hard

Question: What is a closure?
A) Closing files
B) Function retaining access to outer scope variables
C) Class closure
D) Loop termination

✔ Correct Answer: B

Reason: Closure is a function that retains access to variables from its enclosing scope even after outer function has returned.

Tag: Normal

---

### Question 136
Domain: Programming
Topic: Code Analysis
Subtopic: Closure Example
Difficulty: Hard

Question: What is the output?
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f(5))
```
A) 5
B) 10
C) 15
D) Error

✔ Correct Answer: C

Reason: inner function closes over x=10 from outer scope. f is inner with x=10. f(5) returns 10 + 5 = 15.

Tag: Normal

---

### Question 136
Domain: Programming
Topic: Higher-Order Functions
Subtopic: Function as Argument
Difficulty: Medium

Question: What is a higher-order function?
A) Complex function
B) Function that takes functions as arguments or returns functions
C) Fast function
D) Recursive function

✔ Correct Answer: B

Reason: Higher-order functions accept functions as parameters or return functions, enabling functional programming patterns like map, filter, reduce.

Tag: Normal

---

### Question 137
Domain: Programming
Topic: Modules
Subtopic: Import Statements
Difficulty: Easy

Question: What does import statement do?
A) Exports code
B) Includes code from another module/file
C) Deletes modules
D) Compiles code

✔ Correct Answer: B

Reason: import statement includes code from other modules, enabling code organization and reuse across files.

Tag: Normal

---

### Question 138
Domain: Programming
Topic: Modules
Subtopic: Namespace
Difficulty: Medium

Question: What is a namespace?
A) Variable name
B) Container for identifiers to avoid naming conflicts
C) Function name
D) Class name

✔ Correct Answer: B

Reason: Namespace is a container that holds identifiers (variables, functions, classes), preventing naming conflicts between different modules.

Tag: Normal

---

### Question 139
Domain: Programming
Topic: Packages
Subtopic: Package Management
Difficulty: Easy

Question: What is a package manager?
A) File manager
B) Tool for installing and managing software libraries
C) Code editor
D) Compiler

✔ Correct Answer: B

Reason: Package managers (npm, pip, Maven) automate installing, updating, and managing software dependencies and libraries.

Tag: Normal

---

### Question 140
Domain: Programming
Topic: Virtual Environments
Subtopic: Python venv
Difficulty: Medium

Question: Why use virtual environments in Python?
A) Faster execution
B) Isolate project dependencies
C) Better security only
D) Required by Python

✔ Correct Answer: B

Reason: Virtual environments isolate project dependencies, preventing conflicts between different projects requiring different library versions.

Tag: Normal

---



### Question 141
Domain: Programming
Topic: Debugging
Subtopic: Debugging Techniques
Difficulty: Easy

Question: What is a breakpoint in debugging?
A) Breaking code
B) Point where execution pauses for inspection
C) Error point
D) End point

✔ Correct Answer: B

Reason: Breakpoint is a marker where debugger pauses execution, allowing inspection of variables, call stack, and program state.

Tag: Normal

---

### Question 142
Domain: Programming
Topic: Debugging
Subtopic: Watch Variables
Difficulty: Easy

Question: What is a watch variable in debugging?
A) Time variable
B) Variable monitored for value changes
C) Constant variable
D) Deleted variable

✔ Correct Answer: B

Reason: Watch variables are monitored by debugger, showing their values and changes during execution, helping track state.

Tag: Normal

---

### Question 143
Domain: Programming
Topic: Testing
Subtopic: Unit Testing
Difficulty: Easy

Question: What is unit testing?
A) Testing entire system
B) Testing individual components in isolation
C) User testing
D) Performance testing

✔ Correct Answer: B

Reason: Unit testing tests individual units (functions, methods, classes) in isolation to verify they work correctly, forming foundation of test pyramid.

Tag: Past Paper

---

### Question 144
Domain: Programming
Topic: Testing
Subtopic: Test-Driven Development
Difficulty: Medium

Question: What is the TDD cycle?
A) Code, test, deploy
B) Red (write failing test), Green (make it pass), Refactor
C) Test only
D) Code only

✔ Correct Answer: B

Reason: TDD follows Red-Green-Refactor: write failing test first, write minimal code to pass, then refactor while keeping tests green.

Tag: Normal

---

### Question 145
Domain: Programming
Topic: Testing
Subtopic: Assertions
Difficulty: Easy

Question: What do assertions do in testing?
A) Assert dominance
B) Verify expected conditions are true
C) Delete code
D) Optimize code

✔ Correct Answer: B

Reason: Assertions check if expected conditions are true, failing the test if not, verifying code behavior matches expectations.

Tag: Normal

---

### Question 146
Domain: Programming
Topic: Testing
Subtopic: Mocking
Difficulty: Hard

Question: What is mocking in unit testing?
A) Making fun of code
B) Creating fake objects to simulate dependencies
C) Testing real objects
D) Deleting tests

✔ Correct Answer: B

Reason: Mocking creates fake objects that simulate real dependencies, allowing isolated testing without external dependencies like databases or APIs.

Tag: Normal

---

### Question 147
Domain: Programming
Topic: Design Patterns
Subtopic: Singleton Pattern
Difficulty: Medium

Question: What does Singleton pattern ensure?
A) Multiple instances
B) Only one instance of class exists
C) No instances
D) Infinite instances

✔ Correct Answer: B

Reason: Singleton pattern ensures a class has only one instance and provides global access point to it, useful for shared resources.

Tag: Past Paper

---

### Question 148
Domain: Programming
Topic: Design Patterns
Subtopic: Factory Pattern
Difficulty: Medium

Question: What does Factory pattern do?
A) Creates factories
B) Creates objects without specifying exact class
C) Deletes objects
D) Copies objects

✔ Correct Answer: B

Reason: Factory pattern provides interface for creating objects without specifying exact class, delegating instantiation to subclasses or factory methods.

Tag: Normal

---

### Question 149
Domain: Programming
Topic: Design Patterns
Subtopic: Observer Pattern
Difficulty: Hard

Question: What problem does Observer pattern solve?
A) Object creation
B) One-to-many dependency where changes notify dependents
C) Object deletion
D) Object copying

✔ Correct Answer: B

Reason: Observer pattern defines one-to-many dependency where subject notifies all observers automatically when state changes, enabling loose coupling.

Tag: Normal

---

### Question 150
Domain: Programming
Topic: Design Patterns
Subtopic: Strategy Pattern
Difficulty: Hard

Question: What does Strategy pattern enable?
A) Game strategies
B) Selecting algorithm at runtime
C) Fixed algorithm
D) No algorithms

✔ Correct Answer: B

Reason: Strategy pattern defines family of algorithms, encapsulates each, and makes them interchangeable, allowing algorithm selection at runtime.

Tag: Normal

---

### Question 151
Domain: Programming
Topic: Code Analysis
Subtopic: Ternary Operator
Difficulty: Medium

Question: What is the output?
```java
int x = 10;
String result = (x > 5) ? "Big" : "Small";
System.out.println(result);
```
A) 10
B) Big
C) Small
D) Error

✔ Correct Answer: B

Reason: Ternary operator: condition ? value_if_true : value_if_false. Since 10 > 5 is true, result is "Big".

Tag: Normal

---

### Question 152
Domain: Programming
Topic: Operators
Subtopic: Short-Circuit Evaluation
Difficulty: Medium

Question: In expression (false && someFunction()), is someFunction() called?
A) Yes, always
B) No, short-circuit evaluation skips it
C) Sometimes
D) Depends on compiler

✔ Correct Answer: B

Reason: && short-circuits: if left side is false, right side isn't evaluated since result is already false. Improves performance and prevents errors.

Tag: Normal

---

### Question 153
Domain: Programming
Topic: Code Analysis
Subtopic: Short-Circuit
Difficulty: Hard

Question: What is the output?
```python
def test():
    print("Called")
    return True

result = False and test()
```
A) Called, then False
B) False (test not called)
C) True
D) Error

✔ Correct Answer: B

Reason: and short-circuits. Since left side is False, test() is never called. No output, result is False.

Tag: Normal

---

### Question 154
Domain: Programming
Topic: Enumerations
Subtopic: Enum Basics
Difficulty: Easy

Question: What is an enumeration (enum)?
A) Counting numbers
B) Set of named constant values
C) Array type
D) Loop type

✔ Correct Answer: B

Reason: Enums define a set of named constants, improving code readability and type safety compared to using raw integers or strings.

Tag: Normal

---

### Question 155
Domain: Programming
Topic: Constants
Subtopic: Final/Const
Difficulty: Easy

Question: What does the final keyword do in Java?
A) Ends program
B) Makes variable/method/class unchangeable
C) Speeds up code
D) Deletes variable

✔ Correct Answer: B

Reason: final makes variables constant (can't reassign), methods non-overridable, and classes non-inheritable, enforcing immutability.

Tag: Normal

---

### Question 156
Domain: Programming
Topic: Code Analysis
Subtopic: Final Variables
Difficulty: Medium

Question: What happens here?
```java
final int x = 10;
x = 20;
```
A) x becomes 20
B) Compilation error
C) Runtime error
D) x remains 10

✔ Correct Answer: B

Reason: final variables cannot be reassigned after initialization. Attempting to reassign causes compilation error.

Tag: Normal

---

### Question 157
Domain: Programming
Topic: Variable Arguments
Subtopic: Varargs
Difficulty: Medium

Question: What does varargs allow in Java?
A) Variable types
B) Variable number of arguments
C) No arguments
D) Fixed arguments only

✔ Correct Answer: B

Reason: Varargs (Type... name) allows methods to accept variable number of arguments, treated as array inside method.

Tag: Normal

---

### Question 158
Domain: Programming
Topic: Code Analysis
Subtopic: Varargs Usage
Difficulty: Medium

Question: What is the output?
```java
public static int sum(int... nums) {
    int total = 0;
    for(int n : nums) total += n;
    return total;
}
System.out.println(sum(1, 2, 3, 4));
```
A) 4
B) 10
C) 24
D) Error

✔ Correct Answer: B

Reason: Varargs accepts multiple arguments as array. sum(1,2,3,4) adds all: 1+2+3+4 = 10.

Tag: Normal

---

### Question 159
Domain: Programming
Topic: Annotations
Subtopic: Java Annotations
Difficulty: Medium

Question: What is @Override annotation used for?
A) Override variables
B) Indicate method overrides parent method
C) Create new method
D) Delete method

✔ Correct Answer: B

Reason: @Override indicates method is overriding parent class method, enabling compiler to verify override is correct and catch errors.

Tag: Normal

---

### Question 160
Domain: Programming
Topic: Annotations
Subtopic: Deprecated
Difficulty: Easy

Question: What does @Deprecated annotation indicate?
A) Deleted code
B) Code should not be used, may be removed in future
C) New code
D) Optimized code

✔ Correct Answer: B

Reason: @Deprecated marks code that should no longer be used, warning developers it may be removed in future versions.

Tag: Normal

---



### Question 161
Domain: Programming
Topic: Multithreading
Subtopic: Thread Basics
Difficulty: Easy

Question: What is a thread?
A) String thread
B) Lightweight unit of execution within a process
C) Process itself
D) Function

✔ Correct Answer: B

Reason: Thread is a lightweight execution unit within a process, sharing process resources but having its own stack and program counter.

Tag: Past Paper

---

### Question 162
Domain: Programming
Topic: Multithreading
Subtopic: Thread vs Process
Difficulty: Medium

Question: How do threads differ from processes?
A) Same thing
B) Threads share memory, processes have separate memory
C) Threads are slower
D) Processes share memory

✔ Correct Answer: B

Reason: Threads within a process share memory space, while processes have separate memory. Threads are lighter weight with faster context switching.

Tag: Normal

---

### Question 163
Domain: Programming
Topic: Multithreading
Subtopic: Race Condition
Difficulty: Hard

Question: What is a race condition?
A) Fast execution
B) Multiple threads accessing shared data causing unpredictable results
C) Thread racing
D) Performance competition

✔ Correct Answer: B

Reason: Race condition occurs when multiple threads access shared data concurrently and outcome depends on timing, causing unpredictable behavior.

Tag: Past Paper

---

### Question 164
Domain: Programming
Topic: Multithreading
Subtopic: Synchronization
Difficulty: Medium

Question: What is the purpose of synchronization?
A) Sync time
B) Prevent race conditions by controlling thread access
C) Speed up threads
D) Delete threads

✔ Correct Answer: B

Reason: Synchronization controls thread access to shared resources, preventing race conditions by ensuring only one thread accesses critical section at a time.

Tag: Normal

---

### Question 165
Domain: Programming
Topic: Multithreading
Subtopic: Mutex
Difficulty: Medium

Question: What is a mutex?
A) Multiple threads
B) Mutual exclusion lock for thread synchronization
C) Thread type
D) Process type

✔ Correct Answer: B

Reason: Mutex (mutual exclusion) is a locking mechanism ensuring only one thread can access a resource at a time, preventing race conditions.

Tag: Normal

---

### Question 166
Domain: Programming
Topic: Multithreading
Subtopic: Deadlock
Difficulty: Hard

Question: What is deadlock?
A) Dead thread
B) Two or more threads waiting for each other indefinitely
C) Fast lock
D) No lock

✔ Correct Answer: B

Reason: Deadlock occurs when threads wait for resources held by each other in circular dependency, causing all to block indefinitely.

Tag: Past Paper

---

### Question 167
Domain: Programming
Topic: Multithreading
Subtopic: Deadlock Conditions
Difficulty: Hard

Question: How many conditions must be present for deadlock?
A) 2
B) 3
C) 4
D) 5

✔ Correct Answer: C

Reason: Four conditions for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait. All four must be present.

Tag: Normal

---

### Question 168
Domain: Programming
Topic: Multithreading
Subtopic: Thread Pool
Difficulty: Medium

Question: What is a thread pool?
A) Swimming pool
B) Collection of reusable threads for task execution
C) Single thread
D) Thread storage

✔ Correct Answer: B

Reason: Thread pool maintains collection of reusable threads, avoiding overhead of creating/destroying threads for each task, improving performance.

Tag: Normal

---

### Question 169
Domain: Programming
Topic: Asynchronous Programming
Subtopic: Async/Await
Difficulty: Medium

Question: What does async/await provide?
A) Synchronous code
B) Writing asynchronous code in synchronous style
C) Faster execution
D) Thread creation

✔ Correct Answer: B

Reason: async/await allows writing asynchronous code that looks synchronous, improving readability while maintaining non-blocking behavior.

Tag: Normal

---

### Question 170
Domain: Programming
Topic: Asynchronous Programming
Subtopic: Promises
Difficulty: Medium

Question: What is a Promise in JavaScript?
A) Guaranteed result
B) Object representing eventual completion or failure of async operation
C) Synchronous operation
D) Loop structure

✔ Correct Answer: B

Reason: Promise represents eventual result of asynchronous operation, with states: pending, fulfilled, or rejected, enabling async flow control.

Tag: Normal

---

### Question 171
Domain: Programming
Topic: Code Analysis
Subtopic: Promise Chaining
Difficulty: Hard

Question: What is the output?
```javascript
Promise.resolve(5)
  .then(x => x * 2)
  .then(x => x + 3)
  .then(x => console.log(x));
```
A) 5
B) 10
C) 13
D) 8

✔ Correct Answer: C

Reason: Promise chain: 5 * 2 = 10, then 10 + 3 = 13. Each then receives result from previous.

Tag: Normal

---

### Question 172
Domain: Programming
Topic: Asynchronous Programming
Subtopic: Callback Hell
Difficulty: Medium

Question: What is callback hell?
A) Error callbacks
B) Deeply nested callbacks reducing readability
C) Fast callbacks
D) No callbacks

✔ Correct Answer: B

Reason: Callback hell (pyramid of doom) is deeply nested callbacks making code hard to read and maintain, solved by Promises and async/await.

Tag: Normal

---

### Question 173
Domain: Programming
Topic: Error Handling
Subtopic: Exception Types
Difficulty: Medium

Question: What is a checked exception in Java?
A) Checked at runtime only
B) Must be declared or caught at compile time
C) Never checked
D) Optional handling

✔ Correct Answer: B

Reason: Checked exceptions must be declared (throws) or caught (try-catch) at compile time. Unchecked exceptions (RuntimeException) don't require declaration.

Tag: Normal

---

### Question 174
Domain: Programming
Topic: Error Handling
Subtopic: Custom Exceptions
Difficulty: Medium

Question: Why create custom exceptions?
A) More exceptions
B) Provide specific error information for domain
C) Required by language
D) Faster execution

✔ Correct Answer: B

Reason: Custom exceptions provide domain-specific error information, improving error handling and making code more maintainable and understandable.

Tag: Normal

---

### Question 175
Domain: Programming
Topic: Code Analysis
Subtopic: Exception Propagation
Difficulty: Hard

Question: What happens if exception is not caught?
A) Ignored
B) Propagates up call stack until caught or terminates program
C) Automatically handled
D) Deleted

✔ Correct Answer: B

Reason: Uncaught exceptions propagate up the call stack. If never caught, they terminate the program with error message and stack trace.

Tag: Normal

---

### Question 176
Domain: Programming
Topic: Input/Output
Subtopic: Buffered I/O
Difficulty: Medium

Question: What is the advantage of buffered I/O?
A) No advantage
B) Reduces system calls by batching operations
C) Slower
D) More memory always

✔ Correct Answer: B

Reason: Buffered I/O accumulates data in memory buffer, reducing expensive system calls by performing fewer, larger I/O operations.

Tag: Normal

---

### Question 177
Domain: Programming
Topic: Serialization
Subtopic: Object Serialization
Difficulty: Medium

Question: What is serialization?
A) Serial numbers
B) Converting object to byte stream for storage/transmission
C) Sorting objects
D) Deleting objects

✔ Correct Answer: B

Reason: Serialization converts objects to byte streams for storage or network transmission. Deserialization reconstructs objects from bytes.

Tag: Normal

---

### Question 178
Domain: Programming
Topic: Serialization
Subtopic: JSON
Difficulty: Easy

Question: What is JSON?
A) Java Object Notation
B) JavaScript Object Notation
C) JSON Object Network
D) Java Serialization

✔ Correct Answer: B

Reason: JSON (JavaScript Object Notation) is lightweight text format for data interchange, human-readable and language-independent.

Tag: Normal

---

### Question 179
Domain: Programming
Topic: Code Analysis
Subtopic: JSON Parsing
Difficulty: Medium

Question: What is the output?
```python
import json
data = '{"name": "John", "age": 30}'
obj = json.loads(data)
print(obj["age"])
```
A) "30"
B) 30
C) Error
D) null

✔ Correct Answer: B

Reason: json.loads() parses JSON string to Python dict. obj["age"] accesses the age value: 30 (as integer).

Tag: Normal

---

### Question 180
Domain: Programming
Topic: Regular Expressions
Subtopic: Character Classes
Difficulty: Medium

Question: What does [a-z] match in regex?
A) Exactly "a-z"
B) Any lowercase letter
C) Any letter
D) Any character

✔ Correct Answer: B

Reason: [a-z] is a character class matching any single lowercase letter from a to z. [A-Za-z] matches any letter.

Tag: Normal

---



### Question 181
Domain: Programming
Topic: Regular Expressions
Subtopic: Quantifiers
Difficulty: Medium

Question: What does the regex pattern "a{3,5}" match?
A) Exactly 3 'a's
B) 3 to 5 consecutive 'a's
C) 3 or 5 'a's only
D) Any number of 'a's

✔ Correct Answer: B

Reason: {3,5} quantifier matches between 3 and 5 occurrences. "a{3,5}" matches "aaa", "aaaa", or "aaaaa".

Tag: Normal

---

### Question 182
Domain: Programming
Topic: Regular Expressions
Subtopic: Greedy vs Lazy
Difficulty: Hard

Question: What is the difference between .* and .*? in regex?
A) No difference
B) .* is greedy (matches maximum), .*? is lazy (matches minimum)
C) .*? is faster
D) .* is lazy

✔ Correct Answer: B

Reason: * is greedy (matches as much as possible), *? is lazy/non-greedy (matches as little as possible), affecting match length.

Tag: Normal

---

### Question 183
Domain: Programming
Topic: Code Analysis
Subtopic: Switch Statement
Difficulty: Medium

Question: What is the output?
```java
int x = 2;
switch(x) {
    case 1: System.out.print("A");
    case 2: System.out.print("B");
    case 3: System.out.print("C");
    default: System.out.print("D");
}
```
A) B
B) BCD
C) BD
D) ABCD

✔ Correct Answer: B

Reason: Without break statements, execution falls through. Starts at case 2 (prints B), continues through case 3 (C) and default (D): "BCD".

Tag: Past Paper

---

### Question 184
Domain: Programming
Topic: Control Structures
Subtopic: Break Statement
Difficulty: Easy

Question: What does break statement do in loops?
A) Breaks code
B) Exits loop immediately
C) Skips current iteration
D) Restarts loop

✔ Correct Answer: B

Reason: break exits the innermost loop or switch statement immediately, transferring control to the statement after the loop.

Tag: Normal

---

### Question 185
Domain: Programming
Topic: Control Structures
Subtopic: Continue Statement
Difficulty: Easy

Question: What does continue statement do?
A) Continues program
B) Skips rest of current iteration, continues with next
C) Exits loop
D) Stops program

✔ Correct Answer: B

Reason: continue skips remaining code in current loop iteration and proceeds to next iteration, unlike break which exits loop entirely.

Tag: Normal

---

### Question 186
Domain: Programming
Topic: Code Analysis
Subtopic: Continue in Loop
Difficulty: Medium

Question: What is the output?
```python
for i in range(5):
    if i == 2:
        continue
    print(i, end=' ')
```
A) 0 1 2 3 4
B) 0 1 3 4
C) 2
D) 0 1

✔ Correct Answer: B

Reason: Loop iterates 0-4. When i==2, continue skips print. Output: 0 1 3 4 (skipping 2).

Tag: Normal

---

### Question 187
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: this Keyword
Difficulty: Easy

Question: What does 'this' keyword refer to?
A) Previous object
B) Current object instance
C) Next object
D) Parent class

✔ Correct Answer: B

Reason: 'this' refers to the current object instance, used to access instance variables and methods, especially when parameter names shadow fields.

Tag: Normal

---

### Question 188
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: super Keyword
Difficulty: Medium

Question: What does 'super' keyword do?
A) Superior class
B) Refers to parent class members
C) Current class
D) Deletes class

✔ Correct Answer: B

Reason: 'super' refers to parent class, used to call parent constructor or access parent methods/fields that are overridden in subclass.

Tag: Normal

---

### Question 189
Domain: Programming
Topic: Code Analysis
Subtopic: Inheritance
Difficulty: Hard

Question: What is the output?
```java
class Parent {
    void show() { System.out.print("Parent"); }
}
class Child extends Parent {
    void show() { System.out.print("Child"); }
}
Parent p = new Child();
p.show();
```
A) Parent
B) Child
C) ParentChild
D) Error

✔ Correct Answer: B

Reason: Runtime polymorphism: reference type is Parent but object is Child. Method called is determined by object type: Child's show().

Tag: Past Paper

---

### Question 190
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: instanceof Operator
Difficulty: Medium

Question: What does instanceof operator check?
A) Instance count
B) Whether object is instance of specific class/interface
C) Object size
D) Object speed

✔ Correct Answer: B

Reason: instanceof checks if object is an instance of specified class or implements specified interface, returning boolean.

Tag: Normal

---

### Question 191
Domain: Programming
Topic: Code Analysis
Subtopic: instanceof Usage
Difficulty: Medium

Question: What is the output?
```java
String s = "Hello";
System.out.println(s instanceof String);
System.out.println(s instanceof Object);
```
A) true, false
B) true, true
C) false, true
D) false, false

✔ Correct Answer: B

Reason: String is instance of String class (true). String also extends Object, so it's instance of Object too (true).

Tag: Normal

---

### Question 192
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Composition
Difficulty: Medium

Question: What is composition in OOP?
A) Writing code
B) Building complex objects from simpler ones (has-a relationship)
C) Inheritance
D) Polymorphism

✔ Correct Answer: B

Reason: Composition builds objects by containing other objects (has-a relationship), often preferred over inheritance for flexibility and loose coupling.

Tag: Normal

---

### Question 193
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Aggregation
Difficulty: Hard

Question: How does aggregation differ from composition?
A) Same thing
B) Aggregation: contained objects can exist independently
C) Aggregation is faster
D) Composition is newer

✔ Correct Answer: B

Reason: Aggregation is weak association where contained objects can exist independently. Composition is strong: contained objects' lifecycle depends on container.

Tag: Normal

---

### Question 194
Domain: Programming
Topic: Memory Management
Subtopic: Garbage Collection
Difficulty: Medium

Question: What is garbage collection?
A) Deleting code
B) Automatic memory management freeing unused objects
C) Manual memory management
D) Memory allocation

✔ Correct Answer: B

Reason: Garbage collection automatically identifies and frees memory occupied by objects no longer referenced, preventing memory leaks.

Tag: Normal

---

### Question 195
Domain: Programming
Topic: Memory Management
Subtopic: Reference Counting
Difficulty: Hard

Question: What is reference counting?
A) Counting variables
B) Tracking number of references to object for memory management
C) Counting functions
D) Counting lines

✔ Correct Answer: B

Reason: Reference counting tracks how many references point to an object, freeing memory when count reaches zero, though it can't handle circular references.

Tag: Normal

---

### Question 196
Domain: Programming
Topic: Memory Management
Subtopic: Mark and Sweep
Difficulty: Hard

Question: How does mark-and-sweep garbage collection work?
A) Marks errors
B) Marks reachable objects, sweeps unmarked ones
C) Sweeps all objects
D) Marks all objects

✔ Correct Answer: B

Reason: Mark phase identifies reachable objects from roots. Sweep phase frees memory of unmarked (unreachable) objects, handling circular references.

Tag: Normal

---

### Question 197
Domain: Programming
Topic: Code Analysis
Subtopic: Array Iteration
Difficulty: Easy

Question: What is the output?
```python
arr = [10, 20, 30]
for val in arr:
    print(val, end=' ')
```
A) 0 1 2
B) 10 20 30
C) 30 20 10
D) Error

✔ Correct Answer: B

Reason: for-each loop iterates through array values directly (not indices), printing each value: 10 20 30.

Tag: Normal

---

### Question 198
Domain: Programming
Topic: Code Analysis
Subtopic: Enumerate
Difficulty: Medium

Question: What is the output?
```python
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val, end=' ')
```
A) a b c
B) 0 a 1 b 2 c
C) 1 a 2 b 3 c
D) Error

✔ Correct Answer: B

Reason: enumerate() returns index and value pairs. Outputs: 0 a 1 b 2 c (zero-based indexing).

Tag: Normal

---

### Question 199
Domain: Programming
Topic: Code Analysis
Subtopic: List Methods
Difficulty: Medium

Question: What is the output?
```python
lst = [1, 2, 3]
lst.append(4)
lst.extend([5, 6])
print(len(lst))
```
A) 4
B) 5
C) 6
D) 7

✔ Correct Answer: C

Reason: Start with 3 elements. append(4) adds one element (4 total). extend([5,6]) adds two elements (6 total).

Tag: Normal

---

### Question 200
Domain: Programming
Topic: Code Analysis
Subtopic: List Slicing
Difficulty: Hard

Question: What is the output?
```python
lst = [0, 1, 2, 3, 4, 5]
print(lst[::2])
```
A) [0, 1, 2]
B) [0, 2, 4]
C) [1, 3, 5]
D) [0, 1, 2, 3, 4, 5]

✔ Correct Answer: B

Reason: Slicing [::2] means start to end with step 2, selecting every second element: indices 0, 2, 4 → [0, 2, 4].

Tag: Normal

---

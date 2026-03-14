# Programming - MCQ Batch 05
## Questions 401-500

---

### Question 401
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Composition
Difficulty: Hard

Question: What is composition in OOP?
A) Inheritance
B) Object contains other objects as members (has-a relationship)
C) Method composition
D) Class merging

✔ Correct Answer: B

Reason: Composition is has-a relationship where object contains other objects as members. Car has-a Engine. Favored over inheritance for flexibility.

Tag: Past Paper

---

### Question 402
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Aggregation
Difficulty: Hard

Question: What's the difference between composition and aggregation?
A) No difference
B) Composition implies ownership, aggregation doesn't
C) Aggregation is faster
D) Composition is deprecated

✔ Correct Answer: B

Reason: Composition: strong ownership (Engine dies with Car). Aggregation: weak relationship (Professor and Department can exist independently).

Tag: Normal

---

### Question 403
Domain: Programming
Topic: Code Analysis
Subtopic: Composition Example
Difficulty: Medium

Question: What relationship is shown?
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
```
A) Inheritance
B) Composition
C) Aggregation
D) Association

✔ Correct Answer: B

Reason: Car contains Engine object as member. Car has-a Engine, demonstrating composition relationship.

Tag: Normal

---

### Question 404
Domain: Programming
Topic: SOLID Principles
Subtopic: Single Responsibility
Difficulty: Hard

Question: What is Single Responsibility Principle?
A) One class per file
B) Class should have only one reason to change
C) One method per class
D) Single inheritance

✔ Correct Answer: B

Reason: SRP states class should have one responsibility/reason to change, improving maintainability and reducing coupling.

Tag: Past Paper

---

### Question 405
Domain: Programming
Topic: SOLID Principles
Subtopic: Open/Closed Principle
Difficulty: Hard

Question: What is Open/Closed Principle?
A) Open files, close them
B) Open for extension, closed for modification
C) Always open classes
D) Close all methods

✔ Correct Answer: B

Reason: OCP: software entities should be open for extension (add new functionality) but closed for modification (don't change existing code).

Tag: Normal

---

### Question 406
Domain: Programming
Topic: SOLID Principles
Subtopic: Liskov Substitution
Difficulty: Hard

Question: What is Liskov Substitution Principle?
A) Substitute variables
B) Subclass objects should be substitutable for superclass objects
C) Replace methods
D) Swap classes

✔ Correct Answer: B

Reason: LSP: objects of subclass should work wherever superclass objects work without breaking functionality, ensuring proper inheritance.

Tag: Normal

---

### Question 407
Domain: Programming
Topic: SOLID Principles
Subtopic: Interface Segregation
Difficulty: Hard

Question: What is Interface Segregation Principle?
A) Separate interfaces
B) Clients shouldn't depend on interfaces they don't use
C) One interface only
D) No interfaces

✔ Correct Answer: B

Reason: ISP: split large interfaces into smaller, specific ones so clients only depend on methods they use, avoiding fat interfaces.

Tag: Normal

---

### Question 408
Domain: Programming
Topic: SOLID Principles
Subtopic: Dependency Inversion
Difficulty: Hard

Question: What is Dependency Inversion Principle?
A) Invert dependencies
B) Depend on abstractions, not concrete implementations
C) No dependencies
D) Reverse inheritance

✔ Correct Answer: B

Reason: DIP: high-level modules shouldn't depend on low-level modules, both should depend on abstractions (interfaces), reducing coupling.

Tag: Normal

---

### Question 409
Domain: Programming
Topic: Code Analysis
Subtopic: Method Chaining
Difficulty: Medium

Question: What is the output?
```python
class Builder:
    def __init__(self):
        self.value = ""
    def add(self, s):
        self.value += s
        return self
    def build(self):
        return self.value

result = Builder().add("Hello").add(" World").build()
print(result)
```
A) Error
B) Hello World
C) Builder object
D) None

✔ Correct Answer: B

Reason: Method chaining: each add() returns self, allowing chaining. Builds "Hello" + " World" = "Hello World".

Tag: Normal

---

### Question 410
Domain: Programming
Topic: Immutability
Subtopic: Immutable Objects
Difficulty: Medium

Question: Which Python types are immutable?
A) list, dict
B) int, str, tuple
C) set, list
D) All types

✔ Correct Answer: B

Reason: Immutable types: int, float, str, tuple, frozenset. Mutable types: list, dict, set. Immutable objects cannot be modified after creation.

Tag: Past Paper

---

### Question 411
Domain: Programming
Topic: Code Analysis
Subtopic: String Immutability
Difficulty: Medium

Question: What is the output?
```python
s = "hello"
s[0] = "H"
print(s)
```
A) Hello
B) TypeError
C) hello
D) H

✔ Correct Answer: B

Reason: Strings are immutable in Python. Cannot modify individual characters. Attempting to do so raises TypeError.

Tag: Normal

---

### Question 412
Domain: Programming
Topic: List vs Tuple
Subtopic: Performance
Difficulty: Medium

Question: Why are tuples generally faster than lists?
A) Smaller size
B) Immutability allows optimizations
C) Better algorithms
D) No difference

✔ Correct Answer: B

Reason: Tuples are immutable, allowing Python to optimize memory allocation and access. Lists need extra overhead for dynamic resizing.

Tag: Normal

---

### Question 413
Domain: Programming
Topic: Code Analysis
Subtopic: Identity vs Equality
Difficulty: Hard

Question: What is the output?
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)
```
A) True True
B) True False
C) False True
D) False False

✔ Correct Answer: B

Reason: == checks value equality (True, same content). 'is' checks identity (False, different objects in memory).

Tag: Normal

---

### Question 414
Domain: Programming
Topic: Identity Operators
Subtopic: is vs ==
Difficulty: Medium

Question: What does 'is' operator check?
A) Value equality
B) Object identity (same memory location)
C) Type equality
D) String equality

✔ Correct Answer: B

Reason: 'is' checks if two references point to same object in memory. == checks if values are equal.

Tag: Normal

---

### Question 415
Domain: Programming
Topic: Code Analysis
Subtopic: None Identity
Difficulty: Easy

Question: What is the correct way to check for None?
```python
x = None
```
A) x == None
B) x is None
C) x = None
D) not x

✔ Correct Answer: B

Reason: Use 'is None' to check for None (singleton object). 'is' checks identity, more appropriate than == for None.

Tag: Normal

---

### Question 416
Domain: Programming
Topic: Membership Operators
Subtopic: in Operator
Difficulty: Easy

Question: What does 'in' operator do?
A) Inputs value
B) Checks if value exists in sequence
C) Includes file
D) Imports module

✔ Correct Answer: B

Reason: 'in' checks membership. Returns True if value exists in sequence (list, tuple, string, set, dict keys).

Tag: Normal

---

### Question 417
Domain: Programming
Topic: Code Analysis
Subtopic: String Membership
Difficulty: Easy

Question: What is the output?
```python
print("ell" in "hello")
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: 'in' checks substring existence. "ell" is substring of "hello", returns True.

Tag: Normal

---

### Question 418
Domain: Programming
Topic: Global Variables
Subtopic: global Keyword
Difficulty: Medium

Question: What does global keyword do in Python?
A) Makes variable public
B) Allows function to modify global variable
C) Creates global variable
D) Deletes variable

✔ Correct Answer: B

Reason: global keyword declares that variable refers to global scope, allowing function to modify global variable instead of creating local one.

Tag: Normal

---

### Question 419
Domain: Programming
Topic: Code Analysis
Subtopic: Global Scope
Difficulty: Hard

Question: What is the output?
```python
x = 10
def modify():
    global x
    x = 20

modify()
print(x)
```
A) 10
B) 20
C) Error
D) None

✔ Correct Answer: B

Reason: global x allows function to modify global variable. x changed to 20 globally. Prints 20.

Tag: Normal

---

### Question 420
Domain: Programming
Topic: Nonlocal Keyword
Subtopic: Nested Scope
Difficulty: Hard

Question: What does nonlocal keyword do?
A) Makes variable global
B) Refers to variable in nearest enclosing scope (not global)
C) Creates local variable
D) Deletes variable

✔ Correct Answer: B

Reason: nonlocal allows inner function to modify variable from enclosing (but not global) scope, used in nested functions.

Tag: Normal

---

### Question 421
Domain: Programming
Topic: Code Analysis
Subtopic: Nonlocal Example
Difficulty: Hard

Question: What is the output?
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)

outer()
```
A) 10
B) 20
C) Error
D) None

✔ Correct Answer: B

Reason: nonlocal x allows inner() to modify outer's x. x changed to 20 in outer's scope. Prints 20.

Tag: Normal

---

### Question 422
Domain: Programming
Topic: List Methods
Subtopic: List Extend
Difficulty: Medium

Question: What's the difference between append() and extend()?
A) No difference
B) append() adds single element, extend() adds all elements from iterable
C) extend() is slower
D) append() is deprecated

✔ Correct Answer: B

Reason: append() adds single element (even if list). extend() iterates and adds each element. [1].append([2,3])→[1,[2,3]], [1].extend([2,3])→[1,2,3].

Tag: Normal

---

### Question 423
Domain: Programming
Topic: Code Analysis
Subtopic: List Insert
Difficulty: Easy

Question: What is the output?
```python
lst = [1, 2, 4]
lst.insert(2, 3)
print(lst)
```
A) [1, 2, 3, 4]
B) [1, 2, 4, 3]
C) [3, 1, 2, 4]
D) Error

✔ Correct Answer: A

Reason: insert(2, 3) inserts value 3 at index 2. Elements shift right. Result: [1, 2, 3, 4].

Tag: Normal

---

### Question 424
Domain: Programming
Topic: List Methods
Subtopic: List Clear
Difficulty: Easy

Question: What does list.clear() do?
A) Clears screen
B) Removes all elements from list
C) Deletes list
D) Sorts list

✔ Correct Answer: B

Reason: clear() removes all elements, making list empty []. List object still exists but contains no elements.

Tag: Normal

---

### Question 425
Domain: Programming
Topic: Code Analysis
Subtopic: List Copy
Difficulty: Hard

Question: What is the output?
```python
lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1)
```
A) [1, 2, 3]
B) [1, 2, 3, 4]
C) [4]
D) Error

✔ Correct Answer: B

Reason: lst2 = lst1 creates reference, not copy. Both point to same list. Modifying lst2 affects lst1. Use lst2 = lst1.copy() for independent copy.

Tag: Normal

---

### Question 426
Domain: Programming
Topic: Dictionary Methods
Subtopic: setdefault
Difficulty: Hard

Question: What does dict.setdefault(key, default) do?
A) Sets default for all keys
B) Returns value if key exists, otherwise sets key to default and returns it
C) Deletes key
D) Resets dictionary

✔ Correct Answer: B

Reason: setdefault() returns value if key exists. If not, inserts key with default value and returns it. Useful for initializing nested structures.

Tag: Normal

---

### Question 427
Domain: Programming
Topic: Code Analysis
Subtopic: setdefault Example
Difficulty: Hard

Question: What is the output?
```python
d = {'a': 1}
result = d.setdefault('b', 2)
print(result, d)
```
A) None {'a': 1}
B) 2 {'a': 1, 'b': 2}
C) 2 {'a': 1}
D) Error

✔ Correct Answer: B

Reason: Key 'b' doesn't exist. setdefault() adds 'b': 2 to dict and returns 2. Prints: 2 {'a': 1, 'b': 2}.

Tag: Normal

---

### Question 428
Domain: Programming
Topic: Dictionary Methods
Subtopic: popitem
Difficulty: Medium

Question: What does dict.popitem() do?
A) Pops specific item
B) Removes and returns last inserted key-value pair
C) Removes first item
D) Clears dictionary

✔ Correct Answer: B

Reason: popitem() removes and returns last inserted key-value pair as tuple (Python 3.7+, dicts are ordered). Raises KeyError if empty.

Tag: Normal

---

### Question 429
Domain: Programming
Topic: Code Analysis
Subtopic: Dict Pop
Difficulty: Medium

Question: What is the output?
```python
d = {'a': 1, 'b': 2}
val = d.pop('a', 0)
print(val, d)
```
A) 0 {'a': 1, 'b': 2}
B) 1 {'b': 2}
C) 2 {'a': 1}
D) Error

✔ Correct Answer: B

Reason: pop('a', 0) removes key 'a', returns its value 1. Default 0 used if key doesn't exist. Result: 1 {'b': 2}.

Tag: Normal

---

### Question 430
Domain: Programming
Topic: Collections Module
Subtopic: defaultdict
Difficulty: Hard

Question: What is defaultdict?
A) Default dictionary
B) Dictionary that provides default value for missing keys
C) Empty dictionary
D) Sorted dictionary

✔ Correct Answer: B

Reason: defaultdict (from collections) automatically creates default value for missing keys using factory function, avoiding KeyError.

Tag: Normal

---

### Question 431
Domain: Programming
Topic: Code Analysis
Subtopic: defaultdict Example
Difficulty: Hard

Question: What is the output?
```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(d['a'])
```
A) Error
B) 1
C) 0
D) None

✔ Correct Answer: B

Reason: defaultdict(int) creates default value 0 for missing keys. d['a'] starts at 0, += 1 makes it 1.

Tag: Normal

---

### Question 432
Domain: Programming
Topic: Collections Module
Subtopic: Counter
Difficulty: Medium

Question: What does Counter do?
A) Counts lines
B) Counts occurrences of elements
C) Increments counter
D) Counts files

✔ Correct Answer: B

Reason: Counter (from collections) is dict subclass for counting hashable objects. Counter(['a','b','a']) returns {'a': 2, 'b': 1}.

Tag: Normal

---

### Question 433
Domain: Programming
Topic: Code Analysis
Subtopic: Counter Example
Difficulty: Medium

Question: What is the output?
```python
from collections import Counter
c = Counter("hello")
print(c['l'])
```
A) 1
B) 2
C) 0
D) Error

✔ Correct Answer: B

Reason: Counter counts character occurrences. 'l' appears twice in "hello". Returns 2.

Tag: Normal

---

### Question 434
Domain: Programming
Topic: Collections Module
Subtopic: OrderedDict
Difficulty: Medium

Question: What was OrderedDict used for before Python 3.7?
A) Sorting
B) Maintaining insertion order of keys
C) Ordering values
D) No purpose

✔ Correct Answer: B

Reason: OrderedDict maintained insertion order. Python 3.7+ regular dicts are ordered, making OrderedDict less necessary but still useful for equality checks.

Tag: Normal

---

### Question 435
Domain: Programming
Topic: Collections Module
Subtopic: deque
Difficulty: Hard

Question: What is deque?
A) Queue only
B) Double-ended queue supporting efficient operations at both ends
C) Stack only
D) Priority queue

✔ Correct Answer: B

Reason: deque (double-ended queue) from collections supports O(1) append/pop from both ends, unlike list (O(n) for left operations).

Tag: Normal

---

### Question 436
Domain: Programming
Topic: Code Analysis
Subtopic: deque Operations
Difficulty: Hard

Question: What is the output?
```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
d.pop()
print(list(d))
```
A) [1, 2, 3]
B) [0, 1, 2]
C) [0, 1, 2, 3]
D) [1, 2]

✔ Correct Answer: B

Reason: appendleft(0) adds 0 at start: [0,1,2,3]. pop() removes from right: [0,1,2].

Tag: Normal

---

### Question 437
Domain: Programming
Topic: Itertools Module
Subtopic: chain
Difficulty: Medium

Question: What does itertools.chain() do?
A) Creates chain
B) Chains multiple iterables into single iterator
C) Links functions
D) Chains strings

✔ Correct Answer: B

Reason: chain() combines multiple iterables into single iterator. chain([1,2], [3,4]) yields 1, 2, 3, 4.

Tag: Normal

---

### Question 438
Domain: Programming
Topic: Code Analysis
Subtopic: itertools.combinations
Difficulty: Hard

Question: What is the output?
```python
from itertools import combinations
result = list(combinations([1, 2, 3], 2))
print(len(result))
```
A) 2
B) 3
C) 6
D) 9

✔ Correct Answer: B

Reason: combinations([1,2,3], 2) generates all 2-element combinations: (1,2), (1,3), (2,3). Length is 3.

Tag: Normal

---

### Question 439
Domain: Programming
Topic: Itertools Module
Subtopic: permutations
Difficulty: Medium

Question: What's the difference between combinations and permutations?
A) No difference
B) Permutations consider order, combinations don't
C) Combinations are faster
D) Permutations are deprecated

✔ Correct Answer: B

Reason: Permutations consider order: (1,2) ≠ (2,1). Combinations don't: (1,2) = (2,1). permutations([1,2], 2) gives (1,2) and (2,1).

Tag: Normal

---

### Question 440
Domain: Programming
Topic: Code Analysis
Subtopic: itertools.product
Difficulty: Hard

Question: What is the output?
```python
from itertools import product
result = list(product([1, 2], ['a', 'b']))
print(len(result))
```
A) 2
B) 4
C) 3
D) 6

✔ Correct Answer: B

Reason: product() computes Cartesian product: (1,'a'), (1,'b'), (2,'a'), (2,'b'). Length is 2 * 2 = 4.

Tag: Normal

---

### Question 441
Domain: Programming
Topic: JSON
Subtopic: JSON Serialization
Difficulty: Easy

Question: What does json.dumps() do?
A) Dumps garbage
B) Converts Python object to JSON string
C) Reads JSON
D) Deletes JSON

✔ Correct Answer: B

Reason: dumps() serializes Python object to JSON string. loads() deserializes JSON string to Python object.

Tag: Normal

---

### Question 442
Domain: Programming
Topic: Code Analysis
Subtopic: JSON Parsing
Difficulty: Medium

Question: What is the output?
```python
import json
data = '{"name": "Alice", "age": 25}'
obj = json.loads(data)
print(obj['name'])
```
A) {"name": "Alice", "age": 25}
B) Alice
C) Error
D) name

✔ Correct Answer: B

Reason: loads() parses JSON string to Python dict. obj['name'] accesses value: "Alice".

Tag: Normal

---

### Question 443
Domain: Programming
Topic: JSON
Subtopic: JSON File Operations
Difficulty: Medium

Question: What does json.dump() do (without 's')?
A) Same as dumps()
B) Writes JSON to file object
C) Reads JSON
D) Error

✔ Correct Answer: B

Reason: dump() writes JSON to file object. dumps() returns JSON string. load() reads from file, loads() parses string.

Tag: Normal

---

### Question 444
Domain: Programming
Topic: CSV
Subtopic: CSV Reading
Difficulty: Easy

Question: What module handles CSV files in Python?
A) csv
B) file
C) pandas
D) excel

✔ Correct Answer: A

Reason: csv module provides classes for reading/writing CSV files. csv.reader() reads, csv.writer() writes. pandas also handles CSV but csv is standard library.

Tag: Normal

---

### Question 445
Domain: Programming
Topic: Code Analysis
Subtopic: CSV Reader
Difficulty: Medium

Question: What does this code do?
```python
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
A) Writes CSV
B) Reads CSV, prints each row as list
C) Deletes CSV
D) Error

✔ Correct Answer: B

Reason: csv.reader() reads CSV file, yielding each row as list of strings. Loop prints each row.

Tag: Normal

---

### Question 446
Domain: Programming
Topic: Datetime Module
Subtopic: Current Date
Difficulty: Easy

Question: How do you get current date in Python?
A) date.now()
B) datetime.now() or date.today()
C) current_date()
D) time.date()

✔ Correct Answer: B

Reason: datetime.now() returns current datetime. date.today() returns current date. From datetime module.

Tag: Normal

---

### Question 447
Domain: Programming
Topic: Code Analysis
Subtopic: Date Formatting
Difficulty: Medium

Question: What is the output?
```python
from datetime import datetime
dt = datetime(2024, 3, 15)
print(dt.strftime("%Y-%m-%d"))
```
A) 2024/3/15
B) 2024-03-15
C) 15-03-2024
D) Error

✔ Correct Answer: B

Reason: strftime() formats datetime. %Y=year(4-digit), %m=month(2-digit), %d=day(2-digit). Output: "2024-03-15".

Tag: Normal

---

### Question 448
Domain: Programming
Topic: Datetime Module
Subtopic: Date Parsing
Difficulty: Medium

Question: What does strptime() do?
A) Formats date
B) Parses string to datetime object
C) Gets current time
D) Calculates time difference

✔ Correct Answer: B

Reason: strptime() parses string to datetime using format. datetime.strptime("2024-03-15", "%Y-%m-%d") creates datetime object.

Tag: Normal

---

### Question 449
Domain: Programming
Topic: Code Analysis
Subtopic: Timedelta
Difficulty: Medium

Question: What is the output?
```python
from datetime import datetime, timedelta
dt = datetime(2024, 1, 1)
new_dt = dt + timedelta(days=10)
print(new_dt.day)
```
A) 1
B) 11
C) 10
D) Error

✔ Correct Answer: B

Reason: timedelta(days=10) adds 10 days to January 1. Result is January 11. new_dt.day returns 11.

Tag: Normal

---

### Question 450
Domain: Programming
Topic: Random Module
Subtopic: Random Integer
Difficulty: Easy

Question: What does random.randint(a, b) return?
A) Float between a and b
B) Random integer between a and b (inclusive)
C) Random integer less than b
D) Always a

✔ Correct Answer: B

Reason: randint(a, b) returns random integer N where a <= N <= b (both inclusive). random.randrange(a, b) excludes b.

Tag: Normal

---

### Question 451
Domain: Programming
Topic: Code Analysis
Subtopic: Random Choice
Difficulty: Easy

Question: What does this code do?
```python
import random
colors = ['red', 'blue', 'green']
print(random.choice(colors))
```
A) Prints all colors
B) Prints one random color
C) Error
D) Prints 'colors'

✔ Correct Answer: B

Reason: random.choice() returns random element from non-empty sequence. Prints one of: 'red', 'blue', or 'green'.

Tag: Normal

---

### Question 452
Domain: Programming
Topic: Random Module
Subtopic: Shuffle
Difficulty: Easy

Question: What does random.shuffle() do?
A) Shuffles cards
B) Randomly reorders list in-place
C) Returns shuffled copy
D) Sorts randomly

✔ Correct Answer: B

Reason: shuffle() randomly reorders list in-place, modifying original. For immutable copy, use random.sample(list, len(list)).

Tag: Normal

---

### Question 453
Domain: Programming
Topic: Math Module
Subtopic: Math Functions
Difficulty: Easy

Question: What does math.ceil() do?
A) Floors value
B) Rounds up to nearest integer
C) Rounds down
D) Rounds to nearest

✔ Correct Answer: B

Reason: ceil() rounds up to nearest integer. ceil(4.1) = 5. floor() rounds down. round() rounds to nearest.

Tag: Normal

---

### Question 454
Domain: Programming
Topic: Code Analysis
Subtopic: Math Floor
Difficulty: Easy

Question: What is the output?
```python
import math
print(math.floor(4.9))
```
A) 5
B) 4
C) 4.9
D) Error

✔ Correct Answer: B

Reason: floor() rounds down to nearest integer. 4.9 rounds down to 4.

Tag: Normal

---

### Question 455
Domain: Programming
Topic: Math Module
Subtopic: Power Function
Difficulty: Easy

Question: What does math.pow() return?
A) Integer
B) Float
C) String
D) Boolean

✔ Correct Answer: B

Reason: math.pow(x, y) returns float. ** operator returns int if both operands are int. math.pow(2, 3) = 8.0, 2**3 = 8.

Tag: Normal

---

### Question 456
Domain: Programming
Topic: Code Analysis
Subtopic: Math sqrt
Difficulty: Easy

Question: What is the output?
```python
import math
print(math.sqrt(16))
```
A) 4
B) 4.0
C) 256
D) Error

✔ Correct Answer: B

Reason: sqrt() returns square root as float. sqrt(16) = 4.0.

Tag: Normal

---

### Question 457
Domain: Programming
Topic: Math Module
Subtopic: Trigonometric Functions
Difficulty: Medium

Question: What unit do math.sin(), math.cos() use?
A) Degrees
B) Radians
C) Gradians
D) Percentage

✔ Correct Answer: B

Reason: Python's math trigonometric functions use radians. Use math.radians() to convert degrees to radians, math.degrees() for reverse.

Tag: Normal

---

### Question 458
Domain: Programming
Topic: Code Analysis
Subtopic: Absolute Value
Difficulty: Easy

Question: What is the output?
```python
print(abs(-15))
```
A) -15
B) 15
C) 0
D) Error

✔ Correct Answer: B

Reason: abs() returns absolute value (distance from zero). abs(-15) = 15, abs(15) = 15.

Tag: Normal

---

### Question 459
Domain: Programming
Topic: Built-in Functions
Subtopic: min and max
Difficulty: Easy

Question: What does min() function do?
A) Minimizes code
B) Returns smallest element
C) Returns largest element
D) Counts elements

✔ Correct Answer: B

Reason: min() returns smallest element from iterable or arguments. max() returns largest. min([3,1,2]) = 1.

Tag: Normal

---

### Question 460
Domain: Programming
Topic: Code Analysis
Subtopic: max with Key
Difficulty: Hard

Question: What is the output?
```python
words = ['apple', 'pie', 'banana']
result = max(words, key=len)
print(result)
```
A) pie
B) banana
C) apple
D) Error

✔ Correct Answer: B

Reason: max(key=len) finds element with maximum length. "banana" has length 6 (longest).

Tag: Normal

---

### Question 461
Domain: Programming
Topic: Built-in Functions
Subtopic: sum Function
Difficulty: Easy

Question: What does sum() function do?
A) Sums strings
B) Returns sum of numeric iterable
C) Counts elements
D) Multiplies elements

✔ Correct Answer: B

Reason: sum() returns sum of numeric iterable. sum([1,2,3]) = 6. Optional start parameter: sum([1,2], 10) = 13.

Tag: Normal

---

### Question 462
Domain: Programming
Topic: Code Analysis
Subtopic: len Function
Difficulty: Easy

Question: What is the output?
```python
print(len("hello"))
print(len([1, 2, 3]))
```
A) 5 3
B) 4 3
C) 5 4
D) Error

✔ Correct Answer: A

Reason: len() returns number of items. "hello" has 5 characters, [1,2,3] has 3 elements.

Tag: Normal

---

### Question 463
Domain: Programming
Topic: Built-in Functions
Subtopic: range Function
Difficulty: Easy

Question: What does range(5) generate?
A) [1, 2, 3, 4, 5]
B) [0, 1, 2, 3, 4]
C) [5]
D) [0, 1, 2, 3, 4, 5]

✔ Correct Answer: B

Reason: range(5) generates numbers from 0 to 4 (excludes stop value). range(start, stop, step) for custom ranges.

Tag: Normal

---

### Question 464
Domain: Programming
Topic: Code Analysis
Subtopic: range with Step
Difficulty: Medium

Question: What is the output?
```python
print(list(range(0, 10, 2)))
```
A) [0, 2, 4, 6, 8]
B) [0, 2, 4, 6, 8, 10]
C) [2, 4, 6, 8, 10]
D) Error

✔ Correct Answer: A

Reason: range(0, 10, 2) starts at 0, stops before 10, step 2. Generates: 0, 2, 4, 6, 8.

Tag: Normal

---

### Question 465
Domain: Programming
Topic: Built-in Functions
Subtopic: reversed Function
Difficulty: Easy

Question: What does reversed() return?
A) Reversed list
B) Reverse iterator
C) Reversed string
D) Error

✔ Correct Answer: B

Reason: reversed() returns reverse iterator (doesn't modify original). Convert to list with list(reversed(seq)). list.reverse() modifies in-place.

Tag: Normal

---

### Question 466
Domain: Programming
Topic: Code Analysis
Subtopic: isinstance Function
Difficulty: Medium

Question: What is the output?
```python
x = [1, 2, 3]
print(isinstance(x, list))
print(isinstance(x, (list, tuple)))
```
A) True False
B) True True
C) False True
D) False False

✔ Correct Answer: B

Reason: isinstance(x, list) checks if x is list (True). isinstance(x, (list, tuple)) checks if x is either type (True).

Tag: Normal

---

### Question 467
Domain: Programming
Topic: Type Checking
Subtopic: type vs isinstance
Difficulty: Hard

Question: What's the difference between type() and isinstance()?
A) No difference
B) isinstance() considers inheritance, type() checks exact type
C) type() is faster
D) isinstance() is deprecated

✔ Correct Answer: B

Reason: isinstance() returns True for subclasses (inheritance-aware). type() checks exact type only. isinstance() preferred for type checking.

Tag: Normal

---

### Question 468
Domain: Programming
Topic: Code Analysis
Subtopic: Type Function
Difficulty: Easy

Question: What is the output?
```python
x = 5
print(type(x).__name__)
```
A) 5
B) int
C) integer
D) number

✔ Correct Answer: B

Reason: type(x) returns type object. __name__ attribute gives type name as string: "int".

Tag: Normal

---

### Question 469
Domain: Programming
Topic: Built-in Functions
Subtopic: input Function
Difficulty: Easy

Question: What type does input() return?
A) int
B) str
C) Depends on input
D) None

✔ Correct Answer: B

Reason: input() always returns string. Must convert to int/float if needed: int(input()). Python 2's raw_input() became input() in Python 3.

Tag: Normal

---

### Question 470
Domain: Programming
Topic: Code Analysis
Subtopic: Type Conversion
Difficulty: Medium

Question: What is the output?
```python
x = input()  # user enters: 42
print(type(x).__name__)
```
A) int
B) str
C) float
D) number

✔ Correct Answer: B

Reason: input() returns string regardless of what user types. "42" is string. Use int(input()) for integer.

Tag: Normal

---

### Question 471
Domain: Programming
Topic: Built-in Functions
Subtopic: eval Function
Difficulty: Hard

Question: What does eval() do?
A) Evaluates performance
B) Executes Python expression from string
C) Validates code
D) Evaluates variables

✔ Correct Answer: B

Reason: eval() evaluates Python expression string and returns result. eval("2+3") returns 5. Security risk with untrusted input.

Tag: Normal

---

### Question 472
Domain: Programming
Topic: Code Analysis
Subtopic: eval Example
Difficulty: Hard

Question: What is the output?
```python
x = 10
result = eval("x * 2 + 5")
print(result)
```
A) "x * 2 + 5"
B) 25
C) Error
D) 15

✔ Correct Answer: B

Reason: eval() evaluates expression with access to variables. x * 2 + 5 = 10 * 2 + 5 = 25.

Tag: Normal

---

### Question 473
Domain: Programming
Topic: Built-in Functions
Subtopic: exec Function
Difficulty: Hard

Question: What's the difference between eval() and exec()?
A) No difference
B) eval() for expressions, exec() for statements
C) exec() is faster
D) eval() is deprecated

✔ Correct Answer: B

Reason: eval() evaluates expressions, returns value. exec() executes statements (assignments, loops), returns None. Both are security risks.

Tag: Normal

---

### Question 474
Domain: Programming
Topic: Comprehension Performance
Subtopic: Generator Expression
Difficulty: Hard

Question: What's the advantage of generator expression over list comprehension?
A) Faster
B) Memory efficient (lazy evaluation)
C) Easier syntax
D) No advantage

✔ Correct Answer: B

Reason: Generator expression (x for x in range(n)) generates values on-demand (lazy), using less memory than list comprehension [x for x in range(n)].

Tag: Normal

---

### Question 475
Domain: Programming
Topic: Code Analysis
Subtopic: Generator vs List
Difficulty: Hard

Question: What is the output?
```python
gen = (x**2 for x in range(3))
print(type(gen).__name__)
```
A) list
B) generator
C) tuple
D) iterator

✔ Correct Answer: B

Reason: Parentheses create generator expression. type is generator. Square brackets [] create list comprehension.

Tag: Normal

---

### Question 476
Domain: Programming
Topic: Memory Efficiency
Subtopic: sys.getsizeof
Difficulty: Medium

Question: What does sys.getsizeof() return?
A) File size
B) Memory size of object in bytes
C) String length
D) Array size

✔ Correct Answer: B

Reason: getsizeof() returns memory consumption of object in bytes. Useful for comparing memory usage of different data structures.

Tag: Normal

---

### Question 477
Domain: Programming
Topic: Code Analysis
Subtopic: Object Size Comparison
Difficulty: Hard

Question: Which uses less memory for large sequences?
```python
list_comp = [x for x in range(1000000)]
gen_exp = (x for x in range(1000000))
```
A) list_comp
B) gen_exp
C) Same
D) Neither

✔ Correct Answer: B

Reason: Generator expression generates values on-demand, storing only current value. List comprehension stores all million values in memory.

Tag: Normal

---

### Question 478
Domain: Programming
Topic: String Methods
Subtopic: startswith and endswith
Difficulty: Easy

Question: What does str.startswith() check?
A) String length
B) If string starts with specified prefix
C) String type
D) First character only

✔ Correct Answer: B

Reason: startswith() checks if string begins with prefix. "hello".startswith("he") returns True. endswith() checks suffix.

Tag: Normal

---

### Question 479
Domain: Programming
Topic: Code Analysis
Subtopic: String Case Methods
Difficulty: Easy

Question: What is the output?
```python
s = "Hello World"
print(s.lower())
```
A) Hello World
B) hello world
C) HELLO WORLD
D) Error

✔ Correct Answer: B

Reason: lower() converts all characters to lowercase. Returns "hello world". upper() converts to uppercase.

Tag: Normal

---

### Question 480
Domain: Programming
Topic: String Methods
Subtopic: String Find
Difficulty: Medium

Question: What does str.find() return if substring not found?
A) None
B) -1
C) 0
D) Error

✔ Correct Answer: B

Reason: find() returns index of first occurrence, or -1 if not found. index() raises ValueError if not found.

Tag: Normal

---

### Question 481
Domain: Programming
Topic: Code Analysis
Subtopic: String Count
Difficulty: Easy

Question: What is the output?
```python
s = "hello hello world"
print(s.count("hello"))
```
A) 1
B) 2
C) 3
D) 0

✔ Correct Answer: B

Reason: count() returns number of non-overlapping occurrences. "hello" appears twice.

Tag: Normal

---

### Question 482
Domain: Programming
Topic: String Methods
Subtopic: String isdigit
Difficulty: Easy

Question: What does str.isdigit() check?
A) If string is number
B) If all characters are digits
C) If contains digits
D) String length

✔ Correct Answer: B

Reason: isdigit() returns True if all characters are digits. "123".isdigit() = True, "12a".isdigit() = False.

Tag: Normal

---

### Question 483
Domain: Programming
Topic: Code Analysis
Subtopic: String isalpha
Difficulty: Easy

Question: What is the output?
```python
print("Hello".isalpha())
print("Hello123".isalpha())
```
A) True True
B) True False
C) False True
D) False False

✔ Correct Answer: B

Reason: isalpha() checks if all characters are alphabetic. "Hello" is all letters (True). "Hello123" contains digits (False).

Tag: Normal

---

### Question 484
Domain: Programming
Topic: String Methods
Subtopic: String isalnum
Difficulty: Easy

Question: What does str.isalnum() check?
A) If numeric
B) If all characters are alphanumeric (letters or digits)
C) If alphabetic
D) If special characters

✔ Correct Answer: B

Reason: isalnum() returns True if all characters are letters or digits. "Hello123".isalnum() = True, "Hello 123".isalnum() = False (space).

Tag: Normal

---

### Question 485
Domain: Programming
Topic: Code Analysis
Subtopic: String Formatting
Difficulty: Medium

Question: What is the output?
```python
print("{:05d}".format(42))
```
A) 42
B) 00042
C) 42000
D) Error

✔ Correct Answer: B

Reason: {:05d} formats integer with zero-padding to width 5. 42 becomes "00042".

Tag: Normal

---

### Question 486
Domain: Programming
Topic: String Formatting
Subtopic: Float Formatting
Difficulty: Medium

Question: What is the output?
```python
print("{:.2f}".format(3.14159))
```
A) 3.14159
B) 3.14
C) 3.1
D) 3

✔ Correct Answer: B

Reason: {:.2f} formats float to 2 decimal places. 3.14159 becomes "3.14" (rounded).

Tag: Normal

---

### Question 487
Domain: Programming
Topic: Code Analysis
Subtopic: String Center
Difficulty: Medium

Question: What is the output?
```python
s = "Hi"
print(s.center(6, '*'))
```
A) Hi****
B) **Hi**
C) ****Hi
D) Hi

✔ Correct Answer: B

Reason: center(width, fillchar) centers string in field of given width, padding with fillchar. "Hi" centered in 6: "**Hi**".

Tag: Normal

---

### Question 488
Domain: Programming
Topic: String Methods
Subtopic: String zfill
Difficulty: Easy

Question: What does str.zfill(width) do?
A) Fills with spaces
B) Pads string with zeros on left to reach width
C) Fills with z
D) Removes zeros

✔ Correct Answer: B

Reason: zfill() pads numeric string with zeros on left. "42".zfill(5) = "00042". Handles signs correctly.

Tag: Normal

---

### Question 489
Domain: Programming
Topic: Code Analysis
Subtopic: String Partition
Difficulty: Hard

Question: What is the output?
```python
s = "hello-world"
print(s.partition('-'))
```
A) ['hello', 'world']
B) ('hello', '-', 'world')
C) 'hello world'
D) Error

✔ Correct Answer: B

Reason: partition() splits at first occurrence of separator, returns 3-tuple: (before, separator, after).

Tag: Normal

---

### Question 490
Domain: Programming
Topic: List Methods
Subtopic: List Index
Difficulty: Medium

Question: What does list.index(value) return?
A) Value
B) Index of first occurrence
C) All indices
D) Boolean

✔ Correct Answer: B

Reason: index() returns index of first occurrence of value. Raises ValueError if not found. [1,2,3,2].index(2) = 1.

Tag: Normal

---

### Question 491
Domain: Programming
Topic: Code Analysis
Subtopic: List Index with Range
Difficulty: Hard

Question: What is the output?
```python
lst = [1, 2, 3, 2, 4]
print(lst.index(2, 2))
```
A) 1
B) 3
C) 2
D) Error

✔ Correct Answer: B

Reason: index(value, start) searches from start index. Searches for 2 starting from index 2, finds it at index 3.

Tag: Normal

---

### Question 492
Domain: Programming
Topic: Copying
Subtopic: copy Module
Difficulty: Hard

Question: What does copy.deepcopy() do?
A) Shallow copy
B) Recursively copies object and all nested objects
C) Copies reference
D) Deletes copy

✔ Correct Answer: B

Reason: deepcopy() creates independent copy of object and all nested objects. Shallow copy (copy.copy()) copies only top level.

Tag: Normal

---

### Question 493
Domain: Programming
Topic: Code Analysis
Subtopic: Shallow Copy Issue
Difficulty: Hard

Question: What is the output?
```python
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print(original[0][0])
```
A) 1
B) 99
C) Error
D) None

✔ Correct Answer: B

Reason: Shallow copy copies outer list but nested lists are references. Modifying shallow[0][0] affects original[0][0]. Use deepcopy() for independence.

Tag: Normal

---

### Question 494
Domain: Programming
Topic: Metaclasses
Subtopic: type Function
Difficulty: Hard

Question: What can type() do besides checking types?
A) Nothing else
B) Create new classes dynamically
C) Delete types
D) Convert types

✔ Correct Answer: B

Reason: type(name, bases, dict) creates new class dynamically. type('MyClass', (), {'x': 5}) creates class with attribute x.

Tag: Normal

---

### Question 495
Domain: Programming
Topic: Code Analysis
Subtopic: Dynamic Class Creation
Difficulty: Hard

Question: What is the output?
```python
MyClass = type('MyClass', (), {'value': 42})
obj = MyClass()
print(obj.value)
```
A) Error
B) 42
C) None
D) MyClass

✔ Correct Answer: B

Reason: type() creates class with attribute value=42. obj is instance, obj.value accesses attribute: 42.

Tag: Normal

---

### Question 496
Domain: Programming
Topic: Callable
Subtopic: __call__ Method
Difficulty: Hard

Question: What does __call__ method do?
A) Calls function
B) Makes object callable like function
C) Calls constructor
D) Deletes object

✔ Correct Answer: B

Reason: __call__ makes object callable. obj() invokes __call__ method. Useful for function-like objects with state.

Tag: Normal

---

### Question 497
Domain: Programming
Topic: Code Analysis
Subtopic: Callable Object
Difficulty: Hard

Question: What is the output?
```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))
```
A) 2
B) 10
C) 5
D) Error

✔ Correct Answer: B

Reason: __call__ makes double callable. double(5) invokes __call__(5), returns 5 * 2 = 10.

Tag: Normal

---

### Question 498
Domain: Programming
Topic: Iterators
Subtopic: __iter__ and __next__
Difficulty: Hard

Question: What methods make an object iterable?
A) __get__ and __set__
B) __iter__ and __next__
C) __start__ and __stop__
D) __begin__ and __end__

✔ Correct Answer: B

Reason: __iter__ returns iterator object. __next__ returns next value or raises StopIteration. Together they make object iterable in for loops.

Tag: Normal

---

### Question 499
Domain: Programming
Topic: Code Analysis
Subtopic: Custom Iterator
Difficulty: Hard

Question: What is the output?
```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        raise StopIteration

for i in Counter(3):
    print(i, end=' ')
```
A) 0 1 2
B) 1 2 3
C) 0 1 2 3
D) Error

✔ Correct Answer: B

Reason: Custom iterator counts from 1 to max. __next__ increments n then returns it. Outputs: 1 2 3.

Tag: Normal

---

### Question 500
Domain: Programming
Topic: Context Managers
Subtopic: __enter__ and __exit__
Difficulty: Hard

Question: What methods implement context manager protocol?
A) __start__ and __stop__
B) __enter__ and __exit__
C) __open__ and __close__
D) __begin__ and __end__

✔ Correct Answer: B

Reason: __enter__ called when entering 'with' block, __exit__ called when exiting (even on exception). Enables resource management.

Tag: Normal

---

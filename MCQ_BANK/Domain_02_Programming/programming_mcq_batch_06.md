# Programming - MCQ Batch 06
## Questions 501-600

---

### Question 501
Domain: Programming
Topic: Code Analysis
Subtopic: Custom Context Manager
Difficulty: Hard

Question: What is the output?
```python
class MyContext:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, *args):
        print("Exit")

with MyContext():
    print("Inside")
```
A) Inside
B) Enter Inside Exit
C) Enter Exit
D) Error

✔ Correct Answer: B

Reason: __enter__ called first (prints Enter), then block executes (prints Inside), finally __exit__ called (prints Exit).

Tag: Normal

---

### Question 502
Domain: Programming
Topic: Decorators
Subtopic: Decorator with Arguments
Difficulty: Hard

Question: How do you create decorator that accepts arguments?
A) Not possible
B) Decorator factory (function returning decorator)
C) Use global variables
D) Multiple decorators

✔ Correct Answer: B

Reason: Decorator with arguments requires decorator factory: function that takes arguments and returns actual decorator function.

Tag: Normal

---

### Question 503
Domain: Programming
Topic: Code Analysis
Subtopic: Parameterized Decorator
Difficulty: Hard

Question: What is the output?
```python
def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi", end=' ')

greet()
```
A) Hi
B) Hi Hi Hi
C) 3
D) Error

✔ Correct Answer: B

Reason: @repeat(3) calls repeat(3) returning decorator. Decorator wraps greet to execute 3 times. Prints: Hi Hi Hi.

Tag: Normal

---

### Question 504
Domain: Programming
Topic: Decorators
Subtopic: functools.wraps
Difficulty: Hard

Question: Why use @functools.wraps in decorators?
A) Wraps gifts
B) Preserves original function's metadata (__name__, __doc__)
C) Faster execution
D) Required syntax

✔ Correct Answer: B

Reason: @wraps(func) copies metadata from original function to wrapper, preserving __name__, __doc__, etc., important for introspection.

Tag: Normal

---

### Question 505
Domain: Programming
Topic: Code Analysis
Subtopic: Multiple Decorators
Difficulty: Hard

Question: What is the execution order?
```python
@decorator1
@decorator2
def func():
    pass
```
A) decorator1 then decorator2
B) decorator2 then decorator1 (bottom to top)
C) Simultaneous
D) Random

✔ Correct Answer: B

Reason: Decorators applied bottom to top. decorator2 wraps func first, then decorator1 wraps result. Equivalent to decorator1(decorator2(func)).

Tag: Normal

---

### Question 506
Domain: Programming
Topic: Class Decorators
Subtopic: @staticmethod
Difficulty: Medium

Question: What does @staticmethod do?
A) Makes variable static
B) Method doesn't receive self or cls, behaves like regular function
C) Makes method global
D) Deletes method

✔ Correct Answer: B

Reason: @staticmethod creates method that doesn't receive implicit first argument (self/cls). Used for utility functions related to class.

Tag: Past Paper

---

### Question 507
Domain: Programming
Topic: Class Decorators
Subtopic: @classmethod
Difficulty: Medium

Question: What does @classmethod receive as first parameter?
A) self
B) cls (class itself)
C) instance
D) Nothing

✔ Correct Answer: B

Reason: @classmethod receives class (cls) as first parameter instead of instance (self). Used for alternative constructors and class-level operations.

Tag: Past Paper

---

### Question 508
Domain: Programming
Topic: Code Analysis
Subtopic: classmethod Example
Difficulty: Hard

Question: What is the output?
```python
class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())
```
A) 0
B) 2
C) 1
D) Error

✔ Correct Answer: B

Reason: Each Person creation increments class variable count. Two persons created, count = 2. get_count() returns cls.count = 2.

Tag: Normal

---

### Question 509
Domain: Programming
Topic: Inheritance
Subtopic: Multiple Inheritance
Difficulty: Hard

Question: What is multiple inheritance?
A) Multiple classes
B) Class inherits from multiple parent classes
C) Multiple objects
D) Not allowed

✔ Correct Answer: B

Reason: Multiple inheritance allows class to inherit from multiple parents. class Child(Parent1, Parent2). Can cause diamond problem.

Tag: Past Paper

---

### Question 510
Domain: Programming
Topic: Inheritance
Subtopic: Method Resolution Order
Difficulty: Hard

Question: What is MRO in Python?
A) Most Recent Object
B) Order in which methods are searched in inheritance hierarchy
C) Memory Read Order
D) Module Resolution Order

✔ Correct Answer: B

Reason: MRO (Method Resolution Order) determines order Python searches for methods in inheritance hierarchy. Use ClassName.__mro__ or .mro() to view.

Tag: Normal

---

### Question 511
Domain: Programming
Topic: Code Analysis
Subtopic: Diamond Problem
Difficulty: Hard

Question: What is the diamond problem?
```python
class A:
    def method(self): print("A")
class B(A):
    def method(self): print("B")
class C(A):
    def method(self): print("C")
class D(B, C):
    pass
```
A) No problem
B) Ambiguity in which parent's method to inherit
C) Syntax error
D) Memory issue

✔ Correct Answer: B

Reason: Diamond problem: D inherits from B and C, both inherit from A. Which method() to use? Python uses MRO (C3 linearization) to resolve.

Tag: Normal

---

### Question 512
Domain: Programming
Topic: Mixins
Subtopic: Mixin Classes
Difficulty: Hard

Question: What is a mixin?
A) Mixed types
B) Class providing specific functionality to be inherited
C) Mixed inheritance
D) Error class

✔ Correct Answer: B

Reason: Mixin is class designed to provide specific functionality through inheritance, not meant to stand alone. Used for code reuse.

Tag: Normal

---

### Question 513
Domain: Programming
Topic: Abstract Base Classes
Subtopic: ABC Module
Difficulty: Hard

Question: How do you create abstract class in Python?
A) abstract keyword
B) Inherit from ABC, use @abstractmethod
C) Use interface
D) Not possible

✔ Correct Answer: B

Reason: Import ABC from abc module, inherit from it, decorate methods with @abstractmethod. Cannot instantiate abstract class directly.

Tag: Normal

---

### Question 514
Domain: Programming
Topic: Code Analysis
Subtopic: Abstract Method
Difficulty: Hard

Question: What happens?
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

s = Shape()
```
A) Creates object
B) TypeError (cannot instantiate abstract class)
C) None object
D) Empty object

✔ Correct Answer: B

Reason: Cannot instantiate abstract class with unimplemented abstract methods. Must create concrete subclass implementing area().

Tag: Normal

---

### Question 515
Domain: Programming
Topic: Dataclasses
Subtopic: @dataclass Decorator
Difficulty: Medium

Question: What does @dataclass decorator do in Python 3.7+?
A) Creates database
B) Automatically generates __init__, __repr__, __eq__ methods
C) Validates data
D) Encrypts data

✔ Correct Answer: B

Reason: @dataclass automatically generates boilerplate methods (__init__, __repr__, __eq__, etc.) from class annotations, reducing code.

Tag: Normal

---

### Question 516
Domain: Programming
Topic: Code Analysis
Subtopic: Dataclass Example
Difficulty: Medium

Question: What is the output?
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print(p)
```
A) <Point object>
B) Point(x=3, y=4)
C) (3, 4)
D) Error

✔ Correct Answer: B

Reason: @dataclass generates __repr__ showing field names and values. Prints: Point(x=3, y=4).

Tag: Normal

---

### Question 517
Domain: Programming
Topic: Named Tuples
Subtopic: namedtuple
Difficulty: Medium

Question: What is namedtuple?
A) Named variable
B) Tuple subclass with named fields
C) Dictionary
D) List with names

✔ Correct Answer: B

Reason: namedtuple creates tuple subclass with named fields, accessible by name or index. Immutable, memory-efficient alternative to classes.

Tag: Normal

---

### Question 518
Domain: Programming
Topic: Code Analysis
Subtopic: namedtuple Usage
Difficulty: Medium

Question: What is the output?
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p[1])
```
A) 10 10
B) 10 20
C) 20 20
D) Error

✔ Correct Answer: B

Reason: namedtuple allows access by name (p.x = 10) or index (p[1] = 20). Prints: 10 20.

Tag: Normal

---

### Question 519
Domain: Programming
Topic: Enum
Subtopic: Enum Members
Difficulty: Medium

Question: How do you access enum member value?
```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
```
A) Color.RED
B) Color.RED.value
C) Color[1]
D) Color.value.RED

✔ Correct Answer: B

Reason: Color.RED is enum member. Color.RED.value accesses underlying value (1). Color.RED.name gives "RED".

Tag: Normal

---

### Question 520
Domain: Programming
Topic: Code Analysis
Subtopic: Enum Iteration
Difficulty: Medium

Question: What is the output?
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    APPROVED = 2

for s in Status:
    print(s.name, end=' ')
```
A) 1 2
B) PENDING APPROVED
C) Status.PENDING Status.APPROVED
D) Error

✔ Correct Answer: B

Reason: Iterating over enum yields members. s.name gives member name. Prints: PENDING APPROVED.

Tag: Normal

---

### Question 521
Domain: Programming
Topic: Regular Expressions
Subtopic: re.match vs re.search
Difficulty: Medium

Question: What's the difference between re.match() and re.search()?
A) No difference
B) match() checks from start, search() checks entire string
C) search() is faster
D) match() is deprecated

✔ Correct Answer: B

Reason: match() checks if pattern matches at string start. search() finds pattern anywhere in string. search() more commonly used.

Tag: Normal

---

### Question 522
Domain: Programming
Topic: Code Analysis
Subtopic: Regex Search
Difficulty: Medium

Question: What is the output?
```python
import re
text = "The price is 100 dollars"
match = re.search(r'\d+', text)
print(match.group() if match else "No match")
```
A) The
B) 100
C) dollars
D) No match

✔ Correct Answer: B

Reason: \d+ matches one or more digits. search() finds "100". group() returns matched string: "100".

Tag: Normal

---

### Question 523
Domain: Programming
Topic: Regular Expressions
Subtopic: re.findall
Difficulty: Medium

Question: What does re.findall() return?
A) First match
B) List of all matches
C) Match object
D) Boolean

✔ Correct Answer: B

Reason: findall() returns list of all non-overlapping matches. re.findall(r'\d+', "a1b2c3") returns ['1', '2', '3'].

Tag: Normal

---

### Question 524
Domain: Programming
Topic: Code Analysis
Subtopic: Regex Groups
Difficulty: Hard

Question: What is the output?
```python
import re
text = "John: 25"
match = re.search(r'(\w+): (\d+)', text)
print(match.group(1), match.group(2))
```
A) John: 25
B) John 25
C) 1 2
D) Error

✔ Correct Answer: B

Reason: Parentheses create capture groups. group(1) is first group "John", group(2) is second group "25". group(0) is entire match.

Tag: Normal

---

### Question 525
Domain: Programming
Topic: Regular Expressions
Subtopic: re.sub
Difficulty: Medium

Question: What does re.sub() do?
A) Subtracts
B) Replaces pattern matches with replacement string
C) Finds substring
D) Subscribes

✔ Correct Answer: B

Reason: sub() replaces all pattern matches with replacement. re.sub(r'\d+', 'X', "a1b2") returns "aXbX".

Tag: Normal

---

### Question 526
Domain: Programming
Topic: Code Analysis
Subtopic: Regex Substitution
Difficulty: Hard

Question: What is the output?
```python
import re
text = "Price: $100"
result = re.sub(r'\$(\d+)', r'USD \1', text)
print(result)
```
A) Price: $100
B) Price: USD 100
C) Price: USD $100
D) Error

✔ Correct Answer: B

Reason: \1 references first capture group (\d+). Replaces "$100" with "USD 100". Result: "Price: USD 100".

Tag: Normal

---

### Question 527
Domain: Programming
Topic: Regular Expressions
Subtopic: Regex Compilation
Difficulty: Medium

Question: Why compile regex pattern?
A) Required
B) Performance optimization for repeated use
C) Syntax checking
D) No benefit

✔ Correct Answer: B

Reason: re.compile() compiles pattern once, reusable for multiple operations. More efficient than recompiling pattern each time.

Tag: Normal

---

### Question 528
Domain: Programming
Topic: Code Analysis
Subtopic: Compiled Regex
Difficulty: Medium

Question: What is the output?
```python
import re
pattern = re.compile(r'\d+')
print(pattern.findall("a1b2c3"))
```
A) ['a', 'b', 'c']
B) ['1', '2', '3']
C) ['a1', 'b2', 'c3']
D) Error

✔ Correct Answer: B

Reason: Compiled pattern has same methods. findall() finds all digit sequences: ['1', '2', '3'].

Tag: Normal

---

### Question 529
Domain: Programming
Topic: Threading
Subtopic: Thread Creation
Difficulty: Medium

Question: How do you create thread in Python?
A) thread.start()
B) threading.Thread(target=function)
C) new Thread()
D) create_thread()

✔ Correct Answer: B

Reason: Create Thread object with target function: threading.Thread(target=func). Call start() to begin execution. join() waits for completion.

Tag: Normal

---

### Question 530
Domain: Programming
Topic: Code Analysis
Subtopic: Thread Execution
Difficulty: Hard

Question: What is the output?
```python
import threading

def print_nums():
    for i in range(3):
        print(i, end=' ')

t = threading.Thread(target=print_nums)
t.start()
t.join()
print("Done")
```
A) Done
B) 0 1 2 Done
C) Random order
D) Error

✔ Correct Answer: B

Reason: start() begins thread execution. join() waits for thread to complete. Prints 0 1 2, then Done after thread finishes.

Tag: Normal

---

### Question 531
Domain: Programming
Topic: Threading
Subtopic: GIL
Difficulty: Hard

Question: What is GIL in Python?
A) Graphics Interface Library
B) Global Interpreter Lock preventing true parallelism
C) General Input Library
D) Global Integer Limit

✔ Correct Answer: B

Reason: GIL (Global Interpreter Lock) allows only one thread to execute Python bytecode at a time, limiting CPU-bound parallelism. Use multiprocessing for true parallelism.

Tag: Normal

---

### Question 532
Domain: Programming
Topic: Threading
Subtopic: Thread Safety
Difficulty: Hard

Question: What is a race condition?
A) Fast execution
B) Multiple threads accessing shared data causing unpredictable results
C) Thread competition
D) Performance issue

✔ Correct Answer: B

Reason: Race condition occurs when multiple threads access/modify shared data concurrently without synchronization, causing unpredictable behavior.

Tag: Past Paper

---

### Question 533
Domain: Programming
Topic: Threading
Subtopic: Locks
Difficulty: Hard

Question: What is a mutex/lock?
A) Locked file
B) Synchronization primitive ensuring only one thread accesses resource
C) Thread type
D) Error handler

✔ Correct Answer: B

Reason: Mutex (mutual exclusion) or lock ensures only one thread can access critical section at a time, preventing race conditions.

Tag: Normal

---

### Question 534
Domain: Programming
Topic: Code Analysis
Subtopic: Lock Usage
Difficulty: Hard

Question: What does this code prevent?
```python
import threading
lock = threading.Lock()

def critical_section():
    with lock:
        # shared resource access
        pass
```
A) Errors
B) Race conditions on shared resource
C) Slow execution
D) Memory leaks

✔ Correct Answer: B

Reason: Lock ensures only one thread executes critical section at a time, preventing race conditions on shared resource.

Tag: Normal

---

### Question 535
Domain: Programming
Topic: Multiprocessing
Subtopic: Process vs Thread
Difficulty: Medium

Question: What's the key difference between process and thread?
A) No difference
B) Processes have separate memory, threads share memory
C) Threads are faster always
D) Processes are deprecated

✔ Correct Answer: B

Reason: Processes have separate memory spaces (isolated). Threads share memory within process. Processes avoid GIL but have higher overhead.

Tag: Past Paper

---

### Question 536
Domain: Programming
Topic: Code Analysis
Subtopic: Process Creation
Difficulty: Medium

Question: What does this code do?
```python
from multiprocessing import Process

def worker():
    print("Working")

p = Process(target=worker)
p.start()
p.join()
```
A) Creates thread
B) Creates separate process executing worker
C) Error
D) Nothing

✔ Correct Answer: B

Reason: Process creates separate process. start() begins execution, join() waits for completion. True parallelism, bypasses GIL.

Tag: Normal

---

### Question 537
Domain: Programming
Topic: Async Programming
Subtopic: Coroutines
Difficulty: Hard

Question: What is a coroutine?
A) Core routine
B) Function that can pause and resume execution
C) Thread
D) Process

✔ Correct Answer: B

Reason: Coroutine is function defined with async def, can pause (await) and resume, enabling cooperative multitasking without threads.

Tag: Normal

---

### Question 538
Domain: Programming
Topic: Code Analysis
Subtopic: Async Function
Difficulty: Hard

Question: What is the output?
```python
import asyncio

async def greet():
    return "Hello"

result = asyncio.run(greet())
print(result)
```
A) <coroutine>
B) Hello
C) None
D) Error

✔ Correct Answer: B

Reason: asyncio.run() executes coroutine and returns result. greet() returns "Hello", asyncio.run() gets it. Prints: Hello.

Tag: Normal

---

### Question 539
Domain: Programming
Topic: Async Programming
Subtopic: await Keyword
Difficulty: Hard

Question: Where can await be used?
A) Anywhere
B) Only inside async functions
C) Only in main
D) Only in classes

✔ Correct Answer: B

Reason: await can only be used inside async functions. Pauses execution until awaited coroutine completes, then resumes with result.

Tag: Normal

---

### Question 540
Domain: Programming
Topic: Code Analysis
Subtopic: Async Await
Difficulty: Hard

Question: What is the output?
```python
import asyncio

async def fetch():
    await asyncio.sleep(0)
    return "Data"

async def main():
    result = await fetch()
    print(result)

asyncio.run(main())
```
A) <coroutine>
B) Data
C) None
D) Error

✔ Correct Answer: B

Reason: await fetch() pauses until fetch() completes, returns "Data". Prints: Data. asyncio.sleep(0) yields control.

Tag: Normal

---

### Question 541
Domain: Programming
Topic: Async Programming
Subtopic: asyncio.gather
Difficulty: Hard

Question: What does asyncio.gather() do?
A) Gathers data
B) Runs multiple coroutines concurrently, returns results
C) Collects errors
D) Gathers threads

✔ Correct Answer: B

Reason: gather() runs multiple coroutines concurrently, waits for all to complete, returns list of results in order.

Tag: Normal

---

### Question 542
Domain: Programming
Topic: Code Analysis
Subtopic: Concurrent Execution
Difficulty: Hard

Question: What is the output?
```python
import asyncio

async def task(n):
    return n * 2

async def main():
    results = await asyncio.gather(task(1), task(2), task(3))
    print(results)

asyncio.run(main())
```
A) [1, 2, 3]
B) [2, 4, 6]
C) 6
D) Error

✔ Correct Answer: B

Reason: gather() runs three tasks concurrently. Each doubles input: 1*2=2, 2*2=4, 3*2=6. Returns [2, 4, 6].

Tag: Normal

---

### Question 543
Domain: Programming
Topic: List Comprehension
Subtopic: Flattening
Difficulty: Hard

Question: What is the output?
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)
```
A) [[1, 2], [3, 4], [5, 6]]
B) [1, 2, 3, 4, 5, 6]
C) [1, 3, 5]
D) Error

✔ Correct Answer: B

Reason: Nested comprehension flattens 2D list. Outer loop iterates rows, inner loop iterates numbers. Result: [1, 2, 3, 4, 5, 6].

Tag: Normal

---

### Question 544
Domain: Programming
Topic: Walrus Operator
Subtopic: Assignment Expression
Difficulty: Hard

Question: What does := operator do in Python 3.8+?
A) Comparison
B) Assignment expression (assigns and returns value)
C) Division
D) Type hint

✔ Correct Answer: B

Reason: Walrus operator := assigns value and returns it in single expression. if (n := len(list)) > 10: uses n in condition and body.

Tag: Normal

---

### Question 545
Domain: Programming
Topic: Code Analysis
Subtopic: Walrus Operator
Difficulty: Hard

Question: What is the output?
```python
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(n)
```
A) True
B) 5
C) 3
D) Error

✔ Correct Answer: B

Reason: := assigns len(data)=5 to n and uses it in condition. Condition True (5>3), prints n: 5.

Tag: Normal

---

### Question 546
Domain: Programming
Topic: Match Statement
Subtopic: Structural Pattern Matching
Difficulty: Hard

Question: What feature does match statement provide in Python 3.10+?
A) String matching
B) Structural pattern matching (like switch with patterns)
C) Regex matching
D) Type matching only

✔ Correct Answer: B

Reason: match statement provides structural pattern matching, more powerful than switch, supporting destructuring, guards, and complex patterns.

Tag: Normal

---

### Question 547
Domain: Programming
Topic: Code Analysis
Subtopic: Match Example
Difficulty: Hard

Question: What is the output?
```python
def check(value):
    match value:
        case 0:
            return "Zero"
        case 1 | 2:
            return "One or Two"
        case _:
            return "Other"

print(check(2))
```
A) Zero
B) One or Two
C) Other
D) Error

✔ Correct Answer: B

Reason: match checks value against patterns. value=2 matches case 1|2 (OR pattern). Returns "One or Two".

Tag: Normal

---

### Question 548
Domain: Programming
Topic: Type Hints
Subtopic: Union Types
Difficulty: Medium

Question: What does Union[int, str] mean?
A) Integer and string
B) Parameter can be int or str
C) Integer or string sum
D) Error

✔ Correct Answer: B

Reason: Union type hint indicates parameter/return can be one of specified types. Union[int, str] means int or str. Python 3.10+ uses int | str.

Tag: Normal

---

### Question 549
Domain: Programming
Topic: Type Hints
Subtopic: Optional Type
Difficulty: Medium

Question: What does Optional[int] mean?
A) Optional parameter
B) int or None
C) Integer only
D) No type

✔ Correct Answer: B

Reason: Optional[int] is shorthand for Union[int, None]. Indicates value can be int or None.

Tag: Normal

---

### Question 550
Domain: Programming
Topic: Code Analysis
Subtopic: Type Hints with Collections
Difficulty: Hard

Question: What does this type hint mean?
```python
def process(data: list[int]) -> dict[str, int]:
    pass
```
A) Any list and dict
B) List of ints, returns dict with str keys and int values
C) List and dict types
D) Error

✔ Correct Answer: B

Reason: list[int] is list containing integers. dict[str, int] is dict with string keys and integer values. Python 3.9+ syntax.

Tag: Normal

---

### Question 551
Domain: Programming
Topic: Protocols
Subtopic: Duck Typing Protocol
Difficulty: Hard

Question: What is a Protocol in Python typing?
A) Network protocol
B) Structural subtyping (defines interface without inheritance)
C) Security protocol
D) Communication protocol

✔ Correct Answer: B

Reason: Protocol (from typing) defines structural interface. Classes matching structure satisfy protocol without explicit inheritance (duck typing formalized).

Tag: Normal

---

### Question 552
Domain: Programming
Topic: Generics
Subtopic: TypeVar
Difficulty: Hard

Question: What is TypeVar used for?
A) Variable type
B) Generic type parameters in functions/classes
C) Type validation
D) Variable declaration

✔ Correct Answer: B

Reason: TypeVar creates generic type variable for type hints. T = TypeVar('T') allows function to work with any type while maintaining type consistency.

Tag: Normal

---

### Question 553
Domain: Programming
Topic: Code Analysis
Subtopic: Generic Function
Difficulty: Hard

Question: What does this type hint ensure?
```python
from typing import TypeVar
T = TypeVar('T')

def first(items: list[T]) -> T:
    return items[0]
```
A) Nothing
B) Return type matches list element type
C) Only integers
D) Error

✔ Correct Answer: B

Reason: Generic T ensures return type matches list element type. list[int] returns int, list[str] returns str. Type consistency.

Tag: Normal

---

### Question 554
Domain: Programming
Topic: Logging
Subtopic: Logging Levels
Difficulty: Medium

Question: What are the standard logging levels in order?
A) INFO, WARNING, ERROR
B) DEBUG, INFO, WARNING, ERROR, CRITICAL
C) LOW, MEDIUM, HIGH
D) 1, 2, 3, 4, 5

✔ Correct Answer: B

Reason: Logging levels (increasing severity): DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50). Set level to filter messages.

Tag: Normal

---

### Question 555
Domain: Programming
Topic: Code Analysis
Subtopic: Logger Usage
Difficulty: Medium

Question: What does this code do?
```python
import logging
logging.basicConfig(level=logging.WARNING)
logging.debug("Debug msg")
logging.warning("Warning msg")
```
A) Prints both
B) Prints only warning
C) Prints only debug
D) Prints nothing

✔ Correct Answer: B

Reason: Level set to WARNING. DEBUG messages ignored (lower severity). WARNING and above are logged. Prints: Warning msg.

Tag: Normal

---

### Question 556
Domain: Programming
Topic: Logging
Subtopic: Logger Configuration
Difficulty: Medium

Question: What does logging.basicConfig() do?
A) Basic configuration
B) Configures root logger (level, format, handlers)
C) Creates logger
D) Deletes logs

✔ Correct Answer: B

Reason: basicConfig() configures root logger with level, format, filename, etc. Must be called before logging. Only affects root logger.

Tag: Normal

---

### Question 557
Domain: Programming
Topic: Code Analysis
Subtopic: Log Formatting
Difficulty: Hard

Question: What does this format string show?
```python
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Test")
```
A) Test
B) Timestamp - INFO - Test
C) INFO Test
D) Error

✔ Correct Answer: B

Reason: Format string specifies log format. %(asctime)s=timestamp, %(levelname)s=level, %(message)s=message. Output: "2024-03-14 10:30:00 - INFO - Test".

Tag: Normal

---

### Question 558
Domain: Programming
Topic: Unit Testing
Subtopic: unittest Module
Difficulty: Medium

Question: What is unittest?
A) Single test
B) Python's built-in testing framework
C) Unit converter
D) Measurement tool

✔ Correct Answer: B

Reason: unittest is Python's standard testing framework, providing test discovery, fixtures, assertions, and test runners.

Tag: Normal

---

### Question 559
Domain: Programming
Topic: Code Analysis
Subtopic: Test Case
Difficulty: Medium

Question: What does this test check?
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
```
A) Subtraction
B) If 2+2 equals 4
C) Multiplication
D) Nothing

✔ Correct Answer: B

Reason: assertEqual() asserts first argument equals second. Tests if 2+2 equals 4. Test passes if True, fails if False.

Tag: Normal

---

### Question 560
Domain: Programming
Topic: Unit Testing
Subtopic: Test Assertions
Difficulty: Easy

Question: What does assertTrue() do?
A) Makes value true
B) Asserts condition is True, fails test if False
C) Returns True
D) Prints True

✔ Correct Answer: B

Reason: assertTrue(condition) asserts condition is True. If False, test fails with AssertionError. assertFalse() checks for False.

Tag: Normal

---

### Question 561
Domain: Programming
Topic: Code Analysis
Subtopic: Test Setup
Difficulty: Medium

Question: What is setUp() method for?
```python
class TestExample(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]
    
    def test_something(self):
        pass
```
A) Sets up environment
B) Runs before each test method
C) Runs once before all tests
D) Not needed

✔ Correct Answer: B

Reason: setUp() runs before each test method, initializing test fixtures. tearDown() runs after each test for cleanup.

Tag: Normal

---

### Question 562
Domain: Programming
Topic: Unit Testing
Subtopic: Test Fixtures
Difficulty: Medium

Question: What is setUpClass() used for?
A) Sets up each test
B) Runs once before all tests in class
C) Sets up class variables
D) Not used

✔ Correct Answer: B

Reason: setUpClass() (class method) runs once before all tests in class. setUp() runs before each test. tearDownClass() runs once after all tests.

Tag: Normal

---

### Question 563
Domain: Programming
Topic: Code Analysis
Subtopic: assertRaises
Difficulty: Hard

Question: What does this test verify?
```python
def test_division(self):
    with self.assertRaises(ZeroDivisionError):
        result = 10 / 0
```
A) Division works
B) ZeroDivisionError is raised
C) No error occurs
D) Result is correct

✔ Correct Answer: B

Reason: assertRaises() verifies specific exception is raised. Test passes if ZeroDivisionError occurs, fails if no exception or different exception.

Tag: Normal

---

### Question 564
Domain: Programming
Topic: Mocking
Subtopic: unittest.mock
Difficulty: Hard

Question: What is mocking in testing?
A) Making fun
B) Replacing real objects with test doubles
C) Mock data
D) Fake tests

✔ Correct Answer: B

Reason: Mocking replaces real objects/functions with controlled test doubles (mocks), isolating unit under test from dependencies.

Tag: Normal

---

### Question 565
Domain: Programming
Topic: Code Analysis
Subtopic: Mock Object
Difficulty: Hard

Question: What does this code do?
```python
from unittest.mock import Mock

mock_func = Mock(return_value=42)
result = mock_func()
print(result)
```
A) Error
B) 42
C) None
D) Mock object

✔ Correct Answer: B

Reason: Mock object with return_value=42. Calling mock_func() returns 42. Can verify calls with mock_func.assert_called_once().

Tag: Normal

---

### Question 566
Domain: Programming
Topic: Debugging
Subtopic: pdb Module
Difficulty: Medium

Question: What is pdb?
A) Python database
B) Python debugger
C) Package manager
D) Performance tool

✔ Correct Answer: B

Reason: pdb is Python's built-in debugger. import pdb; pdb.set_trace() sets breakpoint. Use commands: n (next), s (step), c (continue).

Tag: Normal

---

### Question 567
Domain: Programming
Topic: Code Analysis
Subtopic: Breakpoint
Difficulty: Medium

Question: What does breakpoint() do in Python 3.7+?
A) Breaks code
B) Sets debugger breakpoint (calls pdb.set_trace())
C) Stops execution permanently
D) Error

✔ Correct Answer: B

Reason: breakpoint() is built-in function that invokes debugger (pdb by default). Cleaner than import pdb; pdb.set_trace().

Tag: Normal

---

### Question 568
Domain: Programming
Topic: Performance
Subtopic: timeit Module
Difficulty: Medium

Question: What is timeit used for?
A) Time zones
B) Measuring execution time of code snippets
C) Setting timers
D) Time formatting

✔ Correct Answer: B

Reason: timeit module measures execution time of small code snippets, running multiple times for accurate measurement, disabling garbage collection.

Tag: Normal

---

### Question 569
Domain: Programming
Topic: Code Analysis
Subtopic: timeit Usage
Difficulty: Hard

Question: What does this measure?
```python
import timeit
time = timeit.timeit('[x**2 for x in range(100)]', number=1000)
print(time)
```
A) Single execution time
B) Total time for 1000 executions
C) Average time
D) Error

✔ Correct Answer: B

Reason: timeit() executes statement 1000 times (number=1000), returns total time in seconds. Divide by 1000 for average.

Tag: Normal

---

### Question 570
Domain: Programming
Topic: Profiling
Subtopic: cProfile
Difficulty: Hard

Question: What is cProfile used for?
A) User profiles
B) Performance profiling (analyzing function call times)
C) Code profiles
D) Configuration profiles

✔ Correct Answer: B

Reason: cProfile profiles Python programs, showing time spent in each function, number of calls, helping identify performance bottlenecks.

Tag: Normal

---

### Question 571
Domain: Programming
Topic: Memory Profiling
Subtopic: memory_profiler
Difficulty: Hard

Question: What does memory_profiler measure?
A) Memory size
B) Line-by-line memory consumption
C) Memory speed
D) Memory type

✔ Correct Answer: B

Reason: memory_profiler measures memory usage line-by-line, identifying memory-intensive operations and potential leaks.

Tag: Normal

---

### Question 572
Domain: Programming
Topic: Code Optimization
Subtopic: List vs Generator
Difficulty: Medium

Question: When should you use generator instead of list?
A) Always
B) When processing large sequences once
C) Never
D) Only for small data

✔ Correct Answer: B

Reason: Generators efficient for large sequences processed once (lazy evaluation). Lists better for multiple iterations or random access.

Tag: Normal

---

### Question 573
Domain: Programming
Topic: Code Analysis
Subtopic: String Concatenation
Difficulty: Hard

Question: Which is more efficient for concatenating many strings?
A) s = s + new_string (in loop)
B) ''.join(list_of_strings)
C) Same efficiency
D) s += new_string

✔ Correct Answer: B

Reason: Strings are immutable. += creates new string each time (O(n²)). join() is O(n), more efficient for many concatenations.

Tag: Normal

---

### Question 574
Domain: Programming
Topic: Data Structures
Subtopic: Set vs List Lookup
Difficulty: Medium

Question: What is time complexity of 'x in set' vs 'x in list'?
A) Both O(n)
B) O(1) for set, O(n) for list
C) Both O(1)
D) O(n) for set, O(1) for list

✔ Correct Answer: B

Reason: Set uses hash table: O(1) average lookup. List requires linear search: O(n). Use sets for membership testing.

Tag: Past Paper

---

### Question 575
Domain: Programming
Topic: Code Analysis
Subtopic: Dictionary Lookup
Difficulty: Easy

Question: What is time complexity of dictionary key lookup?
A) O(n)
B) O(1) average
C) O(log n)
D) O(n²)

✔ Correct Answer: B

Reason: Dictionary uses hash table, providing O(1) average time for lookup, insertion, deletion. Worst case O(n) with hash collisions.

Tag: Normal

---

### Question 576
Domain: Programming
Topic: Algorithm Complexity
Subtopic: Binary Search
Difficulty: Medium

Question: What is time complexity of binary search?
A) O(n)
B) O(log n)
C) O(1)
D) O(n²)

✔ Correct Answer: B

Reason: Binary search divides search space in half each iteration. For n elements, takes log₂(n) steps. Requires sorted array.

Tag: Past Paper

---

### Question 577
Domain: Programming
Topic: Code Analysis
Subtopic: Linear Search
Difficulty: Easy

Question: What is time complexity of linear search?
A) O(log n)
B) O(n)
C) O(1)
D) O(n log n)

✔ Correct Answer: B

Reason: Linear search checks each element sequentially. Worst case checks all n elements: O(n). Works on unsorted arrays.

Tag: Normal

---

### Question 578
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Bubble Sort
Difficulty: Medium

Question: What is time complexity of bubble sort?
A) O(n)
B) O(n²)
C) O(log n)
D) O(n log n)

✔ Correct Answer: B

Reason: Bubble sort compares adjacent elements, swapping if needed. Nested loops: O(n²) worst and average case. O(n) best case (already sorted).

Tag: Past Paper

---

### Question 579
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Merge Sort
Difficulty: Hard

Question: What is time complexity of merge sort?
A) O(n²)
B) O(n log n)
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Merge sort divides array (log n levels), merges (n work per level): O(n log n) all cases. Stable, requires O(n) extra space.

Tag: Past Paper

---

### Question 580
Domain: Programming
Topic: Sorting Algorithms
Subtopic: Quick Sort
Difficulty: Hard

Question: What is average time complexity of quick sort?
A) O(n²)
B) O(n log n)
C) O(n)
D) O(log n)

✔ Correct Answer: B

Reason: Quick sort average case O(n log n). Worst case O(n²) with poor pivot selection. In-place, not stable. Often fastest in practice.

Tag: Past Paper

---

### Question 581
Domain: Programming
Topic: Code Analysis
Subtopic: Sorting Stability
Difficulty: Hard

Question: What is a stable sort?
A) Doesn't crash
B) Maintains relative order of equal elements
C) Fast sort
D) Sorted permanently

✔ Correct Answer: B

Reason: Stable sort preserves relative order of elements with equal keys. Merge sort is stable, quick sort typically isn't.

Tag: Normal

---

### Question 582
Domain: Programming
Topic: Hash Tables
Subtopic: Hash Function
Difficulty: Medium

Question: What is a hash function?
A) Hashing passwords
B) Maps data to fixed-size value (hash code)
C) Deletes data
D) Encrypts data

✔ Correct Answer: B

Reason: Hash function converts input to fixed-size hash code, used in hash tables for fast lookup. Good hash function minimizes collisions.

Tag: Past Paper

---

### Question 583
Domain: Programming
Topic: Hash Tables
Subtopic: Collision Handling
Difficulty: Hard

Question: What is collision in hash table?
A) Memory collision
B) Different keys produce same hash code
C) Syntax error
D) Type mismatch

✔ Correct Answer: B

Reason: Collision occurs when different keys hash to same index. Resolved by chaining (linked lists) or open addressing (probing).

Tag: Normal

---

### Question 584
Domain: Programming
Topic: Code Analysis
Subtopic: Hash Function
Difficulty: Medium

Question: What is the output?
```python
print(hash("hello"))
print(hash("hello"))
```
A) Different values
B) Same value both times
C) Error
D) 0

✔ Correct Answer: B

Reason: hash() returns hash value of object. Same object produces same hash (within session). Immutable objects are hashable.

Tag: Normal

---

### Question 585
Domain: Programming
Topic: Hashable Objects
Subtopic: Hashability
Difficulty: Medium

Question: Which objects are hashable in Python?
A) All objects
B) Immutable objects (int, str, tuple)
C) Mutable objects
D) None

✔ Correct Answer: B

Reason: Hashable objects are immutable: int, str, tuple (of hashables), frozenset. Lists, dicts, sets are unhashable (mutable).

Tag: Normal

---

### Question 586
Domain: Programming
Topic: Code Analysis
Subtopic: Unhashable Type
Difficulty: Medium

Question: What error occurs?
```python
d = {[1, 2]: "value"}
```
A) ValueError
B) TypeError: unhashable type: 'list'
C) KeyError
D) No error

✔ Correct Answer: B

Reason: Dictionary keys must be hashable. Lists are mutable and unhashable. Raises TypeError. Use tuple instead: {(1, 2): "value"}.

Tag: Normal

---

### Question 587
Domain: Programming
Topic: Recursion
Subtopic: Base Case
Difficulty: Easy

Question: What is a base case in recursion?
A) First case
B) Condition that stops recursion
C) Default case
D) Error case

✔ Correct Answer: B

Reason: Base case is terminating condition that stops recursion, preventing infinite recursion and stack overflow.

Tag: Past Paper

---

### Question 588
Domain: Programming
Topic: Code Analysis
Subtopic: Factorial Recursion
Difficulty: Medium

Question: What is the output?
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
```
A) 10
B) 24
C) 4
D) Error

✔ Correct Answer: B

Reason: factorial(4) = 4 * factorial(3) = 4 * 3 * 2 * 1 * 1 = 24. Base case: factorial(0) = 1.

Tag: Normal

---

### Question 589
Domain: Programming
Topic: Recursion
Subtopic: Stack Overflow
Difficulty: Hard

Question: What causes stack overflow in recursion?
A) Too much data
B) Missing or unreachable base case causing infinite recursion
C) Slow execution
D) Memory leak

✔ Correct Answer: B

Reason: Each recursive call adds frame to call stack. Without base case or with unreachable base case, stack grows until overflow.

Tag: Normal

---

### Question 590
Domain: Programming
Topic: Code Analysis
Subtopic: Recursion Depth
Difficulty: Hard

Question: What does sys.getrecursionlimit() return?
A) Recursion count
B) Maximum recursion depth allowed
C) Current depth
D) Error limit

✔ Correct Answer: B

Reason: getrecursionlimit() returns maximum recursion depth (default ~1000). setrecursionlimit() changes it. Prevents stack overflow.

Tag: Normal

---

### Question 591
Domain: Programming
Topic: Binary Search
Subtopic: Binary Search Implementation
Difficulty: Hard

Question: What is required for binary search?
A) Any array
B) Sorted array
C) Linked list
D) Hash table

✔ Correct Answer: B

Reason: Binary search requires sorted array to work correctly. Compares middle element, eliminates half of search space each iteration.

Tag: Past Paper

---

### Question 592
Domain: Programming
Topic: Code Analysis
Subtopic: Binary Search
Difficulty: Hard

Question: What is the output?
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 5))
```
A) -1
B) 2
C) 5
D) Error

✔ Correct Answer: B

Reason: Binary search finds 5 at index 2. Checks middle, adjusts search range, finds target at index 2.

Tag: Normal

---

### Question 593
Domain: Programming
Topic: Two Pointers
Subtopic: Two Pointer Technique
Difficulty: Hard

Question: What is two-pointer technique?
A) Two variables
B) Algorithm using two pointers moving through data structure
C) Double pointers
D) Pointer arithmetic

✔ Correct Answer: B

Reason: Two-pointer technique uses two pointers (often start/end) moving toward each other or same direction, efficient for array problems.

Tag: Normal

---

### Question 594
Domain: Programming
Topic: Code Analysis
Subtopic: Palindrome Check
Difficulty: Medium

Question: What does this code check?
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
A) String length
B) If string reads same forwards and backwards
C) String type
D) Duplicates

✔ Correct Answer: B

Reason: Two pointers from start and end compare characters moving inward. If all match, string is palindrome.

Tag: Normal

---

### Question 595
Domain: Programming
Topic: Sliding Window
Subtopic: Window Technique
Difficulty: Hard

Question: What is sliding window technique?
A) GUI windows
B) Maintains window of elements while traversing array
C) Window functions
D) Screen sliding

✔ Correct Answer: B

Reason: Sliding window maintains fixed or variable-size window of elements, sliding through array. Efficient for subarray/substring problems.

Tag: Normal

---

### Question 596
Domain: Programming
Topic: Code Analysis
Subtopic: Maximum Sum Subarray
Difficulty: Hard

Question: What algorithm finds maximum sum of k consecutive elements?
A) Binary search
B) Sliding window
C) Two pointers
D) Recursion

✔ Correct Answer: B

Reason: Sliding window of size k slides through array, maintaining sum. O(n) time instead of O(n*k) brute force.

Tag: Normal

---

### Question 597
Domain: Programming
Topic: Greedy Algorithms
Subtopic: Activity Selection
Difficulty: Hard

Question: What strategy does activity selection problem use?
A) Dynamic programming
B) Greedy (select activity finishing earliest)
C) Backtracking
D) Brute force

✔ Correct Answer: B

Reason: Activity selection uses greedy approach: sort by finish time, select activity finishing earliest, repeat. Gives optimal solution.

Tag: Normal

---

### Question 598
Domain: Programming
Topic: Backtracking
Subtopic: Backtracking Basics
Difficulty: Hard

Question: What is backtracking?
A) Going backwards
B) Trying solutions, undoing if doesn't work (trial and error)
C) Tracking back
D) Reverse iteration

✔ Correct Answer: B

Reason: Backtracking explores solutions recursively, abandoning path (backtracking) when it fails, trying alternative. Used for constraint satisfaction problems.

Tag: Past Paper

---

### Question 599
Domain: Programming
Topic: Code Analysis
Subtopic: N-Queens Problem
Difficulty: Hard

Question: What problem does N-Queens solve?
A) Chess game
B) Place N queens on N×N board so none attack each other
C) Sorting queens
D) Queen counting

✔ Correct Answer: B

Reason: N-Queens places N queens on chessboard where no two queens threaten each other. Classic backtracking problem.

Tag: Normal

---

### Question 600
Domain: Programming
Topic: Graph Representation
Subtopic: Adjacency List
Difficulty: Medium

Question: What is adjacency list?
A) List of adjacent rooms
B) Graph representation using list of neighbors for each vertex
C) Sorted list
D) Array list

✔ Correct Answer: B

Reason: Adjacency list represents graph as array/dict where each vertex has list of adjacent vertices. Space-efficient for sparse graphs.

Tag: Past Paper

---

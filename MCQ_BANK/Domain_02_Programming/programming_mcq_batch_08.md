# Programming - MCQ Batch 08
## Questions 701-800

---

### Question 701
Domain: Programming
Topic: Serialization
Subtopic: Object Serialization
Difficulty: Hard

Question: What is serialization?
A) Serial numbers
B) Converting object to byte stream for storage/transmission
C) Sorting objects
D) Object creation

✔ Correct Answer: B

Reason: Serialization converts object to byte stream (file, network). Deserialization reconstructs object. Used for persistence, communication.

Tag: Normal

---

### Question 702
Domain: Programming
Topic: Code Analysis
Subtopic: Pickle Module
Difficulty: Hard

Question: What does pickle module do in Python?
A) Pickles vegetables
B) Serializes/deserializes Python objects
C) Compresses files
D) Encrypts data

✔ Correct Answer: B

Reason: pickle serializes Python objects to bytes (pickle.dump()), deserializes back (pickle.load()). Python-specific, not secure for untrusted data.

Tag: Normal

---

### Question 703
Domain: Programming
Topic: Code Analysis
Subtopic: Pickle Usage
Difficulty: Medium

Question: What is the output?
```python
import pickle
data = {'name': 'Alice', 'age': 25}
serialized = pickle.dumps(data)
restored = pickle.loads(serialized)
print(restored['name'])
```
A) Error
B) Alice
C) {'name': 'Alice', 'age': 25}
D) None

✔ Correct Answer: B

Reason: dumps() serializes dict to bytes. loads() deserializes back to dict. restored['name'] accesses value: "Alice".

Tag: Normal

---

### Question 704
Domain: Programming
Topic: File Formats
Subtopic: JSON vs Pickle
Difficulty: Medium

Question: What's an advantage of JSON over pickle?
A) Faster
B) Language-independent, human-readable
C) More features
D) More secure

✔ Correct Answer: B

Reason: JSON is language-independent, human-readable, widely supported. Pickle is Python-specific, binary, supports more Python types.

Tag: Normal

---

### Question 705
Domain: Programming
Topic: Command Line
Subtopic: argparse Module
Difficulty: Medium

Question: What is argparse used for?
A) Parsing strings
B) Parsing command-line arguments
C) Parsing JSON
D) Parsing files

✔ Correct Answer: B

Reason: argparse module creates command-line interfaces, parsing arguments, generating help messages, validating input.

Tag: Normal

---

### Question 706
Domain: Programming
Topic: Code Analysis
Subtopic: argparse Usage
Difficulty: Hard

Question: What does this code do?
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True)
args = parser.parse_args()
print(args.name)
```
A) Parses file
B) Parses --name argument from command line
C) Error
D) Prints 'name'

✔ Correct Answer: B

Reason: Creates parser with required --name argument. parse_args() parses command line. args.name accesses value.

Tag: Normal

---

### Question 707
Domain: Programming
Topic: Regular Expressions
Subtopic: Greedy vs Non-greedy
Difficulty: Hard

Question: What's the difference between .* and .*??
A) No difference
B) .* is greedy (matches maximum), .*? is non-greedy (matches minimum)
C) .*? is faster
D) .* is deprecated

✔ Correct Answer: B

Reason: Greedy quantifiers match maximum possible. Non-greedy (lazy) quantifiers (?, *?, +?) match minimum. "<.*>" matches entire "<a><b>", "<.*?>" matches "<a>".

Tag: Normal

---

### Question 708
Domain: Programming
Topic: Code Analysis
Subtopic: Regex Greedy
Difficulty: Hard

Question: What is the output?
```python
import re
text = "<tag>content</tag>"
print(re.findall(r'<.*>', text))
print(re.findall(r'<.*?>', text))
```
A) Same output
B) ['<tag>content</tag>'], ['<tag>', '</tag>']
C) ['<tag>'], ['</tag>']
D) Error

✔ Correct Answer: B

Reason: <.*> is greedy, matches entire string. <.*?> is non-greedy, matches shortest: '<tag>' and '</tag>'.

Tag: Normal

---

### Question 709
Domain: Programming
Topic: Regular Expressions
Subtopic: Lookahead
Difficulty: Hard

Question: What is positive lookahead (?=...)?
A) Looks ahead
B) Matches if followed by pattern, doesn't consume characters
C) Matches pattern
D) Error syntax

✔ Correct Answer: B

Reason: Positive lookahead (?=pattern) asserts pattern follows, doesn't include it in match. "foo(?=bar)" matches "foo" only if followed by "bar".

Tag: Normal

---

### Question 710
Domain: Programming
Topic: Code Analysis
Subtopic: Lookahead Example
Difficulty: Hard

Question: What is the output?
```python
import re
text = "foo123bar"
match = re.search(r'foo(?=\d+)', text)
print(match.group() if match else "No match")
```
A) foo123
B) foo
C) 123
D) No match

✔ Correct Answer: B

Reason: foo(?=\d+) matches "foo" if followed by digits. Lookahead doesn't consume digits. Matches and returns "foo".

Tag: Normal

---

### Question 711
Domain: Programming
Topic: Regular Expressions
Subtopic: Lookbehind
Difficulty: Hard

Question: What is positive lookbehind (?<=...)?
A) Looks behind
B) Matches if preceded by pattern, doesn't consume characters
C) Matches pattern
D) Error syntax

✔ Correct Answer: B

Reason: Positive lookbehind (?<=pattern) asserts pattern precedes, doesn't include it in match. "(?<=@)\w+" matches username after @.

Tag: Normal

---

### Question 712
Domain: Programming
Topic: Code Analysis
Subtopic: Regex Anchors
Difficulty: Medium

Question: What is the output?
```python
import re
print(re.match(r'^\d+$', '123'))
print(re.match(r'^\d+$', '123abc'))
```
A) Match, Match
B) Match, None
C) None, None
D) None, Match

✔ Correct Answer: B

Reason: ^ matches start, $ matches end. ^\d+$ matches only if entire string is digits. '123' matches, '123abc' doesn't.

Tag: Normal

---

### Question 713
Domain: Programming
Topic: Regular Expressions
Subtopic: Word Boundary
Difficulty: Hard

Question: What does \b represent in regex?
A) Backspace
B) Word boundary
C) Beginning
D) Bold

✔ Correct Answer: B

Reason: \b matches word boundary (between \w and \W). \bcat\b matches "cat" but not "category". \B matches non-boundary.

Tag: Normal

---

### Question 714
Domain: Programming
Topic: Code Analysis
Subtopic: Word Boundary Example
Difficulty: Hard

Question: What is the output?
```python
import re
text = "cat category"
print(re.findall(r'\bcat\b', text))
```
A) ['cat', 'cat']
B) ['cat']
C) ['category']
D) []

✔ Correct Answer: B

Reason: \bcat\b matches "cat" as whole word only. Matches first "cat", not "cat" in "category". Returns ['cat'].

Tag: Normal

---

### Question 715
Domain: Programming
Topic: File Handling
Subtopic: Binary Files
Difficulty: Medium

Question: What mode opens file in binary mode?
A) 'b'
B) 'rb' or 'wb'
C) 'bin'
D) 'binary'

✔ Correct Answer: B

Reason: Add 'b' to mode: 'rb' (read binary), 'wb' (write binary). Binary mode for non-text files (images, executables).

Tag: Normal

---

### Question 716
Domain: Programming
Topic: Code Analysis
Subtopic: Binary File Reading
Difficulty: Medium

Question: What does this code read?
```python
with open('image.png', 'rb') as f:
    data = f.read()
print(type(data).__name__)
```
A) str
B) bytes
C) list
D) Error

✔ Correct Answer: B

Reason: Binary mode ('rb') reads as bytes object, not string. Suitable for non-text files.

Tag: Normal

---

### Question 717
Domain: Programming
Topic: File Handling
Subtopic: File Seek
Difficulty: Hard

Question: What does file.seek(0) do?
A) Seeks file
B) Moves file pointer to beginning
C) Deletes file
D) Closes file

✔ Correct Answer: B

Reason: seek(offset) moves file pointer to position. seek(0) moves to beginning. tell() returns current position.

Tag: Normal

---

### Question 718
Domain: Programming
Topic: Code Analysis
Subtopic: File Tell
Difficulty: Medium

Question: What is the output?
```python
with open('test.txt', 'w') as f:
    f.write("Hello")
    print(f.tell())
```
A) 0
B) 5
C) Hello
D) Error

✔ Correct Answer: B

Reason: tell() returns current file pointer position. After writing "Hello" (5 bytes), position is 5.

Tag: Normal

---

### Question 719
Domain: Programming
Topic: Path Operations
Subtopic: os.path Module
Difficulty: Easy

Question: What does os.path.join() do?
A) Joins strings
B) Joins path components with OS-appropriate separator
C) Joins files
D) Concatenates paths

✔ Correct Answer: B

Reason: os.path.join() combines path components with correct separator (/ or \). os.path.join('dir', 'file.txt') handles OS differences.

Tag: Normal

---

### Question 720
Domain: Programming
Topic: Code Analysis
Subtopic: Path Existence
Difficulty: Easy

Question: What does os.path.exists() check?
A) File content
B) If path exists (file or directory)
C) File permissions
D) File size

✔ Correct Answer: B

Reason: exists() returns True if path exists (file or directory). isfile() checks file specifically, isdir() checks directory.

Tag: Normal

---

### Question 721
Domain: Programming
Topic: Path Operations
Subtopic: pathlib Module
Difficulty: Medium

Question: What advantage does pathlib have over os.path?
A) Faster
B) Object-oriented, more intuitive API
C) More functions
D) No advantage

✔ Correct Answer: B

Reason: pathlib provides object-oriented path manipulation. Path('dir') / 'file.txt' more intuitive than os.path.join(). Modern Python prefers pathlib.

Tag: Normal

---

### Question 722
Domain: Programming
Topic: Code Analysis
Subtopic: pathlib Usage
Difficulty: Medium

Question: What is the output?
```python
from pathlib import Path
p = Path('folder/file.txt')
print(p.name)
print(p.suffix)
```
A) folder file.txt
B) file.txt .txt
C) folder .txt
D) Error

✔ Correct Answer: B

Reason: name property returns filename with extension. suffix returns file extension. stem returns name without extension.

Tag: Normal

---

### Question 723
Domain: Programming
Topic: Directory Operations
Subtopic: os.listdir
Difficulty: Easy

Question: What does os.listdir() return?
A) Directory path
B) List of entries in directory
C) File content
D) Directory size

✔ Correct Answer: B

Reason: listdir() returns list of filenames and subdirectories in directory. Doesn't include '.' and '..'. Use os.scandir() for more info.

Tag: Normal

---

### Question 724
Domain: Programming
Topic: Code Analysis
Subtopic: Directory Traversal
Difficulty: Hard

Question: What does os.walk() do?
```python
for root, dirs, files in os.walk('folder'):
    print(root, dirs, files)
```
A) Walks directory
B) Recursively traverses directory tree
C) Lists files only
D) Error

✔ Correct Answer: B

Reason: walk() generates tuples (dirpath, dirnames, filenames) for each directory in tree. Enables recursive directory processing.

Tag: Normal

---

### Question 725
Domain: Programming
Topic: Environment Variables
Subtopic: Setting Environment Variables
Difficulty: Medium

Question: How do you set environment variable in Python?
A) env.set()
B) os.environ['VAR'] = 'value'
C) setenv()
D) export VAR

✔ Correct Answer: B

Reason: os.environ is dict-like object. Set with os.environ['VAR'] = 'value'. Get with os.environ.get('VAR', default).

Tag: Normal

---

### Question 726
Domain: Programming
Topic: Code Analysis
Subtopic: Environment Variable
Difficulty: Medium

Question: What is the output?
```python
import os
os.environ['MY_VAR'] = 'test'
print(os.environ.get('MY_VAR', 'default'))
```
A) default
B) test
C) MY_VAR
D) Error

✔ Correct Answer: B

Reason: Sets MY_VAR to 'test'. get() retrieves it: "test". If not set, would return 'default'.

Tag: Normal

---

### Question 727
Domain: Programming
Topic: Subprocess
Subtopic: Running Commands
Difficulty: Medium

Question: What module runs external commands in Python?
A) os.system
B) subprocess
C) command
D) shell

✔ Correct Answer: B

Reason: subprocess module runs external commands, captures output, handles errors. subprocess.run() is recommended. os.system() is deprecated.

Tag: Normal

---

### Question 728
Domain: Programming
Topic: Code Analysis
Subtopic: subprocess.run
Difficulty: Hard

Question: What does this code do?
```python
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```
A) Error
B) Runs ls -l, captures output as string
C) Lists Python files
D) Nothing

✔ Correct Answer: B

Reason: run() executes command, capture_output=True captures stdout/stderr, text=True returns as string. result.stdout contains output.

Tag: Normal

---

### Question 729
Domain: Programming
Topic: Context Variables
Subtopic: Global State
Difficulty: Hard

Question: What problem do global variables cause in multithreading?
A) Slow execution
B) Race conditions, shared mutable state
C) Memory leaks
D) No problem

✔ Correct Answer: B

Reason: Global variables shared across threads cause race conditions without synchronization. Use thread-local storage or locks.

Tag: Normal

---

### Question 730
Domain: Programming
Topic: Code Analysis
Subtopic: Thread Local Storage
Difficulty: Hard

Question: What does threading.local() provide?
A) Local variables
B) Thread-specific data storage
C) Global storage
D) Shared storage

✔ Correct Answer: B

Reason: threading.local() creates object with thread-specific attributes. Each thread sees its own values, avoiding race conditions.

Tag: Normal

---

### Question 731
Domain: Programming
Topic: Concurrency
Subtopic: Semaphore
Difficulty: Hard

Question: What is a semaphore?
A) Signal
B) Synchronization primitive limiting concurrent access to resource
C) Thread type
D) Lock type

✔ Correct Answer: B

Reason: Semaphore maintains counter, allows n threads to access resource concurrently. acquire() decrements, release() increments. Mutex is semaphore with count 1.

Tag: Normal

---

### Question 732
Domain: Programming
Topic: Code Analysis
Subtopic: Semaphore Usage
Difficulty: Hard

Question: What does this code limit?
```python
from threading import Semaphore
sem = Semaphore(3)

def worker():
    with sem:
        # access resource
        pass
```
A) Nothing
B) Maximum 3 threads accessing resource concurrently
C) 3 total threads
D) 3 seconds

✔ Correct Answer: B

Reason: Semaphore(3) allows maximum 3 threads in critical section simultaneously. 4th thread waits until one releases.

Tag: Normal

---

### Question 733
Domain: Programming
Topic: Concurrency
Subtopic: Event
Difficulty: Hard

Question: What is threading.Event()?
A) Event handler
B) Synchronization primitive for thread communication
C) Event loop
D) Exception event

✔ Correct Answer: B

Reason: Event manages internal flag. Threads wait() for flag to be set(). Another thread calls set() to signal. Used for thread coordination.

Tag: Normal

---

### Question 734
Domain: Programming
Topic: Code Analysis
Subtopic: Condition Variable
Difficulty: Hard

Question: What is threading.Condition() used for?
A) Conditional execution
B) Complex thread synchronization (wait/notify pattern)
C) If statements
D) Error conditions

✔ Correct Answer: B

Reason: Condition variable allows threads to wait for condition, notified by other threads. wait() releases lock and waits, notify() wakes waiting thread.

Tag: Normal

---

### Question 735
Domain: Programming
Topic: Async Programming
Subtopic: Event Loop
Difficulty: Hard

Question: What is event loop in asyncio?
A) Loop event
B) Core managing and executing coroutines
C) For loop
D) Event handler

✔ Correct Answer: B

Reason: Event loop schedules and executes coroutines, handles I/O operations, manages callbacks. asyncio.run() creates and manages loop.

Tag: Normal

---

### Question 736
Domain: Programming
Topic: Code Analysis
Subtopic: asyncio.create_task
Difficulty: Hard

Question: What does asyncio.create_task() do?
A) Creates task list
B) Schedules coroutine to run concurrently
C) Creates thread
D) Creates process

✔ Correct Answer: B

Reason: create_task() wraps coroutine in Task, scheduling it for concurrent execution. Returns Task object for tracking/cancellation.

Tag: Normal

---

### Question 737
Domain: Programming
Topic: Async Programming
Subtopic: asyncio.wait
Difficulty: Hard

Question: What's the difference between asyncio.gather() and asyncio.wait()?
A) No difference
B) gather() returns results in order, wait() returns done/pending sets
C) wait() is faster
D) gather() is deprecated

✔ Correct Answer: B

Reason: gather() returns list of results in order. wait() returns (done, pending) sets of tasks, more control over completion.

Tag: Normal

---

### Question 738
Domain: Programming
Topic: Code Analysis
Subtopic: Task Cancellation
Difficulty: Hard

Question: What does this code do?
```python
import asyncio

async def main():
    task = asyncio.create_task(long_operation())
    await asyncio.sleep(1)
    task.cancel()
```
A) Completes task
B) Cancels task after 1 second
C) Error
D) Waits forever

✔ Correct Answer: B

Reason: create_task() starts long_operation() concurrently. After 1 second, cancel() requests cancellation. Task raises CancelledError.

Tag: Normal

---

### Question 739
Domain: Programming
Topic: Coroutines
Subtopic: async with
Difficulty: Hard

Question: What is async with used for?
A) Async loops
B) Asynchronous context managers
C) Async functions
D) Async variables

✔ Correct Answer: B

Reason: async with uses asynchronous context manager (__aenter__, __aexit__). For resources with async setup/cleanup (async file I/O, connections).

Tag: Normal

---

### Question 740
Domain: Programming
Topic: Code Analysis
Subtopic: async for
Difficulty: Hard

Question: What does async for do?
A) Async loop
B) Iterates over asynchronous iterator
C) Parallel loop
D) Error

✔ Correct Answer: B

Reason: async for iterates over async iterator (__aiter__, __anext__). Used with async generators or async iterables.

Tag: Normal

---

### Question 741
Domain: Programming
Topic: Weak References
Subtopic: weakref Module
Difficulty: Hard

Question: What is weak reference?
A) Weak pointer
B) Reference that doesn't prevent garbage collection
C) Null reference
D) Broken reference

✔ Correct Answer: B

Reason: Weak reference doesn't increase reference count, allowing object to be garbage collected. Used for caches, avoiding circular references.

Tag: Normal

---

### Question 742
Domain: Programming
Topic: Code Analysis
Subtopic: Circular Reference
Difficulty: Hard

Question: What problem does this create?
```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a
```
A) No problem
B) Circular reference (memory leak in some languages)
C) Syntax error
D) Infinite loop

✔ Correct Answer: B

Reason: Circular reference: a references b, b references a. Python's GC handles this, but problematic in languages with reference counting only.

Tag: Normal

---

### Question 743
Domain: Programming
Topic: Memory Management
Subtopic: Reference Counting
Difficulty: Hard

Question: What is reference counting?
A) Counting references
B) Memory management tracking number of references to object
C) Counting variables
D) Performance metric

✔ Correct Answer: B

Reason: Reference counting tracks references to object. When count reaches 0, memory freed. Python uses reference counting + cycle detector.

Tag: Normal

---

### Question 744
Domain: Programming
Topic: Code Analysis
Subtopic: del Statement
Difficulty: Medium

Question: What does del statement do?
A) Deletes file
B) Removes reference, may trigger garbage collection
C) Deletes variable permanently
D) Clears memory

✔ Correct Answer: B

Reason: del removes reference to object. If last reference, object becomes eligible for garbage collection. Doesn't directly free memory.

Tag: Normal

---

### Question 745
Domain: Programming
Topic: Garbage Collection
Subtopic: gc Module
Difficulty: Hard

Question: What does gc.collect() do?
A) Collects data
B) Forces garbage collection cycle
C) Collects variables
D) Collects errors

✔ Correct Answer: B

Reason: gc.collect() manually triggers garbage collection. Usually automatic, but manual collection useful for freeing memory immediately or debugging.

Tag: Normal

---

### Question 746
Domain: Programming
Topic: Code Analysis
Subtopic: Garbage Collection Control
Difficulty: Hard

Question: What does gc.disable() do?
A) Disables program
B) Disables automatic garbage collection
C) Disables imports
D) Error

✔ Correct Answer: B

Reason: gc.disable() turns off automatic GC. Useful for performance-critical sections. gc.enable() re-enables. Reference counting still works.

Tag: Normal

---

### Question 747
Domain: Programming
Topic: Performance Optimization
Subtopic: List Preallocation
Difficulty: Medium

Question: Why preallocate list size?
A) Required
B) Avoids repeated reallocation, improves performance
C) Uses more memory
D) No benefit

✔ Correct Answer: B

Reason: Preallocating (lst = [None] * n) avoids dynamic resizing. Growing list repeatedly reallocates memory. Preallocation faster for known size.

Tag: Normal

---

### Question 748
Domain: Programming
Topic: Code Analysis
Subtopic: Local Variable Optimization
Difficulty: Hard

Question: Why assign global function to local variable in loop?
```python
# Instead of:
for i in range(n):
    math.sqrt(i)

# Do:
sqrt = math.sqrt
for i in range(n):
    sqrt(i)
```
A) No benefit
B) Avoids repeated global lookup, faster
C) Required syntax
D) Uses less memory

✔ Correct Answer: B

Reason: Local variable access faster than global/attribute lookup. Assigning to local variable before loop avoids repeated lookups, micro-optimization.

Tag: Normal

---

### Question 749
Domain: Programming
Topic: Performance
Subtopic: List Comprehension vs Loop
Difficulty: Medium

Question: Which is generally faster?
A) for loop
B) List comprehension
C) Same speed
D) Depends on size

✔ Correct Answer: B

Reason: List comprehensions generally faster than equivalent for loops (optimized in C, less overhead). More readable too.

Tag: Normal

---

### Question 750
Domain: Programming
Topic: Code Analysis
Subtopic: Set Membership
Difficulty: Medium

Question: Which is faster for checking membership?
```python
# Option A
if item in large_list:
    pass

# Option B
if item in large_set:
    pass
```
A) large_list
B) large_set
C) Same
D) Depends

✔ Correct Answer: B

Reason: Set membership O(1) average using hash table. List membership O(n) requires linear search. Use sets for frequent membership tests.

Tag: Normal

---

### Question 751
Domain: Programming
Topic: String Optimization
Subtopic: String Interning
Difficulty: Hard

Question: What is string interning?
A) Internal strings
B) Storing only one copy of each distinct string value
C) String encryption
D) String compression

✔ Correct Answer: B

Reason: String interning stores single copy of each string value, reusing for identical strings. Python automatically interns some strings for memory efficiency.

Tag: Normal

---

### Question 752
Domain: Programming
Topic: Code Analysis
Subtopic: String Identity
Difficulty: Hard

Question: What is the output?
```python
a = "hello"
b = "hello"
print(a is b)
```
A) False
B) True (likely, due to interning)
C) Error
D) None

✔ Correct Answer: B

Reason: Python interns short string literals. a and b likely reference same interned string object. a is b returns True.

Tag: Normal

---

### Question 753
Domain: Programming
Topic: Slots
Subtopic: __slots__
Difficulty: Hard

Question: What does __slots__ do?
A) Creates slots
B) Restricts instance attributes, saves memory
C) Adds attributes
D) Deletes attributes

✔ Correct Answer: B

Reason: __slots__ defines fixed set of attributes, using less memory than __dict__. Prevents dynamic attribute addition. Useful for many instances.

Tag: Normal

---

### Question 754
Domain: Programming
Topic: Code Analysis
Subtopic: Slots Example
Difficulty: Hard

Question: What happens?
```python
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
p.z = 3
```
A) p.z = 3
B) AttributeError
C) p.z = None
D) No error

✔ Correct Answer: B

Reason: __slots__ restricts attributes to x and y. Attempting to add z raises AttributeError. No __dict__ created.

Tag: Normal

---

### Question 755
Domain: Programming
Topic: Property Decorators
Subtopic: Setter and Deleter
Difficulty: Hard

Question: What is the output?
```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        self._celsius = value

t = Temperature()
t.celsius = 25
print(t.celsius)
```
A) 0
B) 25
C) Error
D) None

✔ Correct Answer: B

Reason: @property creates getter. @celsius.setter creates setter. t.celsius = 25 calls setter, t.celsius calls getter. Prints 25.

Tag: Normal

---

### Question 756
Domain: Programming
Topic: Descriptors
Subtopic: Descriptor Protocol
Difficulty: Hard

Question: What methods define descriptor protocol?
A) __init__, __del__
B) __get__, __set__, __delete__
C) __enter__, __exit__
D) __iter__, __next__

✔ Correct Answer: B

Reason: Descriptors implement __get__, __set__, __delete__ for attribute access control. Properties are descriptors. Advanced Python feature.

Tag: Normal

---

### Question 757
Domain: Programming
Topic: Code Analysis
Subtopic: Class Attributes
Difficulty: Medium

Question: What is the output?
```python
class Test:
    x = 10

t1 = Test()
t2 = Test()
Test.x = 20
print(t1.x, t2.x)
```
A) 10 10
B) 20 20
C) 10 20
D) 20 10

✔ Correct Answer: B

Reason: x is class attribute shared by all instances. Changing Test.x affects all instances. Both print 20.

Tag: Normal

---

### Question 758
Domain: Programming
Topic: Class Methods
Subtopic: Alternative Constructors
Difficulty: Hard

Question: What is the output?
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

p = Person.from_birth_year("Alice", 1999)
print(p.age)
```
A) 1999
B) 25
C) 2024
D) Error

✔ Correct Answer: B

Reason: @classmethod creates alternative constructor. from_birth_year calculates age: 2024 - 1999 = 25. Returns Person with age 25.

Tag: Normal

---

### Question 759
Domain: Programming
Topic: Operator Overloading
Subtopic: Comparison Operators
Difficulty: Hard

Question: Which method overloads < operator?
A) __less__
B) __lt__
C) __lessthan__
D) __compare__

✔ Correct Answer: B

Reason: __lt__ overloads <. __le__ for <=, __gt__ for >, __ge__ for >=, __eq__ for ==, __ne__ for !=.

Tag: Normal

---

### Question 760
Domain: Programming
Topic: Code Analysis
Subtopic: Rich Comparison
Difficulty: Hard

Question: What is the output?
```python
class Number:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        return self.val < other.val

n1 = Number(5)
n2 = Number(10)
print(n1 < n2)
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: __lt__ enables < comparison. n1.val (5) < n2.val (10) returns True.

Tag: Normal

---

### Question 761
Domain: Programming
Topic: Operator Overloading
Subtopic: Container Methods
Difficulty: Hard

Question: Which method overloads len() function?
A) __length__
B) __len__
C) __size__
D) __count__

✔ Correct Answer: B

Reason: __len__ overloads len() function. len(obj) calls obj.__len__(). Must return non-negative integer.

Tag: Normal

---

### Question 762
Domain: Programming
Topic: Code Analysis
Subtopic: Indexing Overload
Difficulty: Hard

Question: What is the output?
```python
class MyList:
    def __init__(self):
        self.data = [1, 2, 3]
    def __getitem__(self, index):
        return self.data[index]

ml = MyList()
print(ml[1])
```
A) 1
B) 2
C) Error
D) [1, 2, 3]

✔ Correct Answer: B

Reason: __getitem__ overloads [] operator. ml[1] calls __getitem__(1), returns self.data[1] = 2.

Tag: Normal

---

### Question 763
Domain: Programming
Topic: Operator Overloading
Subtopic: setitem
Difficulty: Hard

Question: Which method overloads item assignment?
A) __set__
B) __setitem__
C) __assign__
D) __put__

✔ Correct Answer: B

Reason: __setitem__ overloads item assignment. obj[key] = value calls obj.__setitem__(key, value). __delitem__ for deletion.

Tag: Normal

---

### Question 764
Domain: Programming
Topic: Code Analysis
Subtopic: Contains Method
Difficulty: Medium

Question: What is the output?
```python
class MyContainer:
    def __init__(self):
        self.items = [1, 2, 3]
    def __contains__(self, item):
        return item in self.items

c = MyContainer()
print(2 in c)
```
A) False
B) True
C) Error
D) None

✔ Correct Answer: B

Reason: __contains__ overloads 'in' operator. 2 in c calls c.__contains__(2), checks if 2 in items. Returns True.

Tag: Normal

---

### Question 765
Domain: Programming
Topic: String Representation
Subtopic: __repr__ vs __str__
Difficulty: Hard

Question: What's the difference between __repr__ and __str__?
A) No difference
B) __repr__ for developers (unambiguous), __str__ for users (readable)
C) __str__ is faster
D) __repr__ is deprecated

✔ Correct Answer: B

Reason: __repr__ should be unambiguous, ideally recreate object. __str__ should be readable. print() uses __str__, repr() uses __repr__.

Tag: Normal

---

### Question 766
Domain: Programming
Topic: Code Analysis
Subtopic: repr Function
Difficulty: Medium

Question: What is the output?
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))
```
A) <Point object>
B) Point(3, 4)
C) (3, 4)
D) Error

✔ Correct Answer: B

Reason: repr(p) calls p.__repr__(), returns "Point(3, 4)". Useful for debugging.

Tag: Normal

---

### Question 767
Domain: Programming
Topic: Context Managers
Subtopic: contextlib
Difficulty: Hard

Question: What does @contextmanager decorator do?
A) Creates context
B) Converts generator to context manager
C) Manages contexts
D) Error

✔ Correct Answer: B

Reason: @contextmanager (from contextlib) converts generator function to context manager. yield separates __enter__ and __exit__ logic.

Tag: Normal

---

### Question 768
Domain: Programming
Topic: Code Analysis
Subtopic: contextmanager Example
Difficulty: Hard

Question: What is the output?
```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Enter")
    yield
    print("Exit")

with my_context():
    print("Inside")
```
A) Inside
B) Enter Inside Exit
C) Enter Exit
D) Error

✔ Correct Answer: B

Reason: Code before yield runs on enter (prints Enter), block executes (prints Inside), code after yield runs on exit (prints Exit).

Tag: Normal

---

### Question 769
Domain: Programming
Topic: Itertools
Subtopic: itertools.count
Difficulty: Medium

Question: What does itertools.count() do?
A) Counts elements
B) Infinite counter starting from value
C) Counts to limit
D) Counts occurrences

✔ Correct Answer: B

Reason: count(start, step) creates infinite iterator counting from start. count(10, 2) yields 10, 12, 14, ... Use with zip() or takewhile() to limit.

Tag: Normal

---

### Question 770
Domain: Programming
Topic: Code Analysis
Subtopic: itertools.cycle
Difficulty: Medium

Question: What is the output?
```python
from itertools import cycle, islice
cycler = cycle([1, 2, 3])
result = list(islice(cycler, 7))
print(result)
```
A) [1, 2, 3]
B) [1, 2, 3, 1, 2, 3, 1]
C) Error
D) [1, 2, 3, 4, 5, 6, 7]

✔ Correct Answer: B

Reason: cycle() repeats iterable infinitely. islice(cycler, 7) takes first 7 elements: [1, 2, 3, 1, 2, 3, 1].

Tag: Normal

---

### Question 771
Domain: Programming
Topic: Itertools
Subtopic: itertools.repeat
Difficulty: Easy

Question: What does itertools.repeat(value, times) do?
A) Repeats function
B) Repeats value specified number of times
C) Repeats forever
D) Duplicates list

✔ Correct Answer: B

Reason: repeat(value, times) yields value times times. repeat(5, 3) yields 5, 5, 5. Without times, repeats infinitely.

Tag: Normal

---

### Question 772
Domain: Programming
Topic: Code Analysis
Subtopic: itertools.groupby
Difficulty: Hard

Question: What does itertools.groupby() do?
A) Groups randomly
B) Groups consecutive elements by key function
C) Groups all elements
D) Sorts and groups

✔ Correct Answer: B

Reason: groupby() groups consecutive elements with same key. Requires sorted input for grouping all occurrences. Returns (key, group_iterator) pairs.

Tag: Normal

---

### Question 773
Domain: Programming
Topic: Itertools
Subtopic: itertools.islice
Difficulty: Medium

Question: What does itertools.islice() do?
A) Slices integers
B) Slices iterator (like list slicing for iterators)
C) Slices strings
D) Error

✔ Correct Answer: B

Reason: islice(iterable, start, stop, step) slices iterator without loading all elements. Memory-efficient for large iterators.

Tag: Normal

---

### Question 774
Domain: Programming
Topic: Code Analysis
Subtopic: itertools.takewhile
Difficulty: Hard

Question: What is the output?
```python
from itertools import takewhile
result = list(takewhile(lambda x: x < 5, [1, 2, 3, 6, 4, 7]))
print(result)
```
A) [1, 2, 3, 4]
B) [1, 2, 3]
C) [1, 2, 3, 6, 4, 7]
D) Error

✔ Correct Answer: B

Reason: takewhile() yields elements while condition True. Stops at first False (6 >= 5). Returns [1, 2, 3], doesn't continue after 6.

Tag: Normal

---

### Question 775
Domain: Programming
Topic: Itertools
Subtopic: itertools.dropwhile
Difficulty: Hard

Question: What does itertools.dropwhile() do?
A) Drops elements
B) Drops elements while condition True, yields rest
C) Drops all
D) Filters elements

✔ Correct Answer: B

Reason: dropwhile() skips elements while condition True, then yields all remaining. Opposite of takewhile(). dropwhile(lambda x: x<5, [1,2,6,3]) yields 6, 3.

Tag: Normal

---

### Question 776
Domain: Programming
Topic: Code Analysis
Subtopic: itertools.zip_longest
Difficulty: Hard

Question: What is the output?
```python
from itertools import zip_longest
result = list(zip_longest([1, 2], ['a', 'b', 'c'], fillvalue=0))
print(result)
```
A) [(1, 'a'), (2, 'b')]
B) [(1, 'a'), (2, 'b'), (0, 'c')]
C) Error
D) [(1, 'a'), (2, 'b'), (None, 'c')]

✔ Correct Answer: B

Reason: zip_longest() pairs elements, continuing until longest exhausted. Missing values filled with fillvalue (0). Result: [(1,'a'), (2,'b'), (0,'c')].

Tag: Normal

---

### Question 777
Domain: Programming
Topic: Functools
Subtopic: functools.partial
Difficulty: Hard

Question: What does functools.partial() do?
A) Partial function
B) Creates new function with some arguments pre-filled
C) Incomplete function
D) Error

✔ Correct Answer: B

Reason: partial() creates new function with some arguments fixed. partial(func, arg1) returns function needing remaining arguments.

Tag: Normal

---

### Question 778
Domain: Programming
Topic: Code Analysis
Subtopic: Partial Application
Difficulty: Hard

Question: What is the output?
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))
```
A) 10
B) 25
C) 7
D) Error

✔ Correct Answer: B

Reason: partial() fixes exponent=2. square(5) calls power(5, 2) = 5² = 25.

Tag: Normal

---

### Question 779
Domain: Programming
Topic: Functools
Subtopic: functools.reduce
Difficulty: Medium

Question: What does functools.reduce() require?
A) List only
B) Function taking two arguments and iterable
C) Single argument
D) No arguments

✔ Correct Answer: B

Reason: reduce(function, iterable) requires binary function (two arguments). Applies cumulatively: reduce(lambda x,y: x+y, [1,2,3]) = ((1+2)+3).

Tag: Normal

---

### Question 780
Domain: Programming
Topic: Code Analysis
Subtopic: reduce with Initial
Difficulty: Hard

Question: What is the output?
```python
from functools import reduce
result = reduce(lambda x, y: x + y, [1, 2, 3], 10)
print(result)
```
A) 6
B) 16
C) 10
D) Error

✔ Correct Answer: B

Reason: Third argument (10) is initial value. Computation: ((10+1)+2)+3 = 16. Without initial: ((1+2)+3) = 6.

Tag: Normal

---

### Question 781
Domain: Programming
Topic: Functools
Subtopic: functools.cache
Difficulty: Hard

Question: What's the difference between @cache and @lru_cache?
A) No difference
B) @cache has unlimited size, @lru_cache has size limit
C) @cache is slower
D) @lru_cache is deprecated

✔ Correct Answer: B

Reason: @cache (Python 3.9+) is @lru_cache(maxsize=None). Unlimited cache, simpler syntax. @lru_cache allows size limit.

Tag: Normal

---

### Question 782
Domain: Programming
Topic: Code Analysis
Subtopic: Cached Property
Difficulty: Hard

Question: What does @cached_property do?
```python
from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @cached_property
    def area(self):
        print("Computing")
        return 3.14 * self.radius ** 2
```
A) Computes every time
B) Computes once, caches result
C) Error
D) Never computes

✔ Correct Answer: B

Reason: @cached_property computes value on first access, caches it. Subsequent accesses return cached value without recomputation.

Tag: Normal

---

### Question 783
Domain: Programming
Topic: Operator Overloading
Subtopic: Unary Operators
Difficulty: Hard

Question: Which method overloads unary - operator?
A) __minus__
B) __neg__
C) __negative__
D) __sub__

✔ Correct Answer: B

Reason: __neg__ overloads unary -. __pos__ for unary +, __invert__ for ~, __abs__ for abs().

Tag: Normal

---

### Question 784
Domain: Programming
Topic: Code Analysis
Subtopic: Unary Operator
Difficulty: Hard

Question: What is the output?
```python
class Number:
    def __init__(self, val):
        self.val = val
    def __neg__(self):
        return Number(-self.val)

n = Number(5)
neg_n = -n
print(neg_n.val)
```
A) 5
B) -5
C) Error
D) None

✔ Correct Answer: B

Reason: __neg__ enables -n, returns new Number with negated value. neg_n.val = -5.

Tag: Normal

---

### Question 785
Domain: Programming
Topic: Operator Overloading
Subtopic: In-place Operators
Difficulty: Hard

Question: Which method overloads += operator?
A) __add__
B) __iadd__
C) __plus__
D) __increment__

✔ Correct Answer: B

Reason: __iadd__ overloads +=. __isub__ for -=, __imul__ for *=, etc. If not defined, falls back to __add__ creating new object.

Tag: Normal

---

### Question 786
Domain: Programming
Topic: Code Analysis
Subtopic: In-place Addition
Difficulty: Hard

Question: What is the output?
```python
class Counter:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):
        self.val += other
        return self

c = Counter(10)
c += 5
print(c.val)
```
A) 10
B) 15
C) Error
D) 5

✔ Correct Answer: B

Reason: __iadd__ modifies object in-place. c += 5 calls __iadd__(5), adds 5 to val. c.val = 15.

Tag: Normal

---

### Question 787
Domain: Programming
Topic: Magic Methods
Subtopic: __bool__
Difficulty: Medium

Question: What does __bool__ method do?
A) Creates boolean
B) Defines truthiness of object
C) Checks type
D) Converts to bool

✔ Correct Answer: B

Reason: __bool__ defines object's truth value. if obj: calls obj.__bool__(). If not defined, __len__ used (0 is False).

Tag: Normal

---

### Question 788
Domain: Programming
Topic: Code Analysis
Subtopic: Truthiness
Difficulty: Medium

Question: What is the output?
```python
class Empty:
    def __bool__(self):
        return False

obj = Empty()
if obj:
    print("True")
else:
    print("False")
```
A) True
B) False
C) Error
D) None

✔ Correct Answer: B

Reason: __bool__ returns False. if obj: evaluates to False. Prints "False".

Tag: Normal

---

### Question 789
Domain: Programming
Topic: Magic Methods
Subtopic: __hash__
Difficulty: Hard

Question: What must be true if __eq__ is overridden?
A) Nothing
B) Should override __hash__ too (if object hashable)
C) Must override __ne__
D) Cannot override

✔ Correct Answer: B

Reason: Objects comparing equal must have same hash. Override __eq__ makes object unhashable unless __hash__ also overridden. Equal objects need equal hashes.

Tag: Normal

---

### Question 790
Domain: Programming
Topic: Code Analysis
Subtopic: Hash and Equality
Difficulty: Hard

Question: What is the output?
```python
class Point:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

p1 = Point(5)
p2 = Point(5)
print(p1 == p2, hash(p1) == hash(p2))
```
A) False False
B) True True
C) True False
D) False True

✔ Correct Answer: B

Reason: __eq__ makes p1 == p2 True (same x). __hash__ ensures equal objects have equal hashes. Both True.

Tag: Normal

---

### Question 791
Domain: Programming
Topic: Descriptors
Subtopic: Property Implementation
Difficulty: Hard

Question: What is @property implemented with?
A) Magic method
B) Descriptor protocol
C) Decorator only
D) Function

✔ Correct Answer: B

Reason: @property is descriptor implementing __get__, __set__, __delete__. Descriptors are foundation for properties, methods, static/class methods.

Tag: Normal

---

### Question 792
Domain: Programming
Topic: Code Analysis
Subtopic: Custom Descriptor
Difficulty: Hard

Question: What is the output?
```python
class Descriptor:
    def __get__(self, obj, objtype=None):
        return 42

class MyClass:
    value = Descriptor()

obj = MyClass()
print(obj.value)
```
A) Descriptor object
B) 42
C) Error
D) None

✔ Correct Answer: B

Reason: Accessing obj.value calls Descriptor.__get__(), returns 42. Descriptors control attribute access.

Tag: Normal

---

### Question 793
Domain: Programming
Topic: Metaclasses
Subtopic: Metaclass Basics
Difficulty: Hard

Question: What is a metaclass?
A) Meta information
B) Class of a class (defines class behavior)
C) Parent class
D) Abstract class

✔ Correct Answer: B

Reason: Metaclass is class of a class. type is default metaclass. Metaclasses control class creation, customizing class behavior.

Tag: Normal

---

### Question 794
Domain: Programming
Topic: Code Analysis
Subtopic: Custom Metaclass
Difficulty: Hard

Question: What does this metaclass do?
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['id'] = 100
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.id)
```
A) Error
B) 100
C) None
D) Meta

✔ Correct Answer: B

Reason: Metaclass __new__ called when creating class. Adds 'id' attribute to class. MyClass.id = 100.

Tag: Normal

---

### Question 795
Domain: Programming
Topic: Generators
Subtopic: Generator Expressions
Difficulty: Medium

Question: What is the output?
```python
gen = (x**2 for x in range(5))
print(next(gen))
print(next(gen))
```
A) 0 0
B) 0 1
C) 1 4
D) Error

✔ Correct Answer: B

Reason: Generator expression creates generator. First next() yields 0² = 0. Second next() yields 1² = 1.

Tag: Normal

---

### Question 796
Domain: Programming
Topic: Generators
Subtopic: send Method
Difficulty: Hard

Question: What does generator.send(value) do?
A) Sends generator
B) Sends value to generator, resumes execution
C) Sends email
D) Error

✔ Correct Answer: B

Reason: send() sends value to generator, which receives it from yield expression. Resumes execution. Used for two-way communication.

Tag: Normal

---

### Question 797
Domain: Programming
Topic: Code Analysis
Subtopic: Generator Send
Difficulty: Hard

Question: What is the output?
```python
def gen():
    x = yield
    yield x * 2

g = gen()
next(g)  # Prime generator
print(g.send(5))
```
A) 5
B) 10
C) None
D) Error

✔ Correct Answer: B

Reason: First next() runs to first yield. send(5) assigns 5 to x, continues to yield x*2 = 10. Returns 10.

Tag: Normal

---

### Question 798
Domain: Programming
Topic: Generators
Subtopic: Generator Close
Difficulty: Hard

Question: What does generator.close() do?
A) Closes file
B) Raises GeneratorExit in generator, stops it
C) Closes program
D) Error

✔ Correct Answer: B

Reason: close() raises GeneratorExit at yield point, allowing cleanup. Generator cannot yield after GeneratorExit.

Tag: Normal

---

### Question 799
Domain: Programming
Topic: Code Analysis
Subtopic: Generator Throw
Difficulty: Hard

Question: What does generator.throw(exception) do?
A) Throws generator
B) Raises exception at yield point in generator
C) Catches exception
D) Error

✔ Correct Answer: B

Reason: throw() raises exception at current yield point. Generator can catch and handle it, or let it propagate.

Tag: Normal

---

### Question 800
Domain: Programming
Topic: Coroutines
Subtopic: yield from
Difficulty: Hard

Question: What does 'yield from' do?
A) Yields from function
B) Delegates to sub-generator/iterator
C) Yields multiple values
D) Error

✔ Correct Answer: B

Reason: 'yield from' delegates to sub-generator, yielding all its values. Simplifies generator composition. yield from range(3) yields 0, 1, 2.

Tag: Normal

---

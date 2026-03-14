# Programming - MCQ Batch 03
## Questions 201-300

---

### Question 201
Domain: Programming
Topic: Code Analysis
Subtopic: Dictionary Operations
Difficulty: Medium

Question: What is the output?
```python
d = {'a': 1, 'b': 2}
print(d.get('c', 0))
```
A) Error
B) None
C) 0
D) 'c'

✔ Correct Answer: C

Reason: get() method returns value for key if exists, otherwise returns default (second argument). Key 'c' doesn't exist, returns 0.

Tag: Normal

---

### Question 202
Domain: Programming
Topic: Tuples
Subtopic: Tuple Immutability
Difficulty: Easy

Question: What is the key characteristic of tuples?
A) Mutable
B) Immutable
C) Dynamic size
D) Sorted

✔ Correct Answer: B

Reason: Tuples are immutable sequences - once created, elements cannot be changed, added, or removed, providing data integrity.

Tag: Normal

---

### Question 203
Domain: Programming
Topic: Code Analysis
Subtopic: Tuple Unpacking
Difficulty: Medium

Question: What is the output?
```python
a, b, c = (10, 20, 30)
print(b)
```
A) 10
B) 20
C) 30
D) Error

✔ Correct Answer: B

Reason: Tuple unpacking assigns tuple elements to variables in order: a=10, b=20, c=30. Prints b which is 20.

Tag: Normal

---

### Question 204
Domain: Programming
Topic: Sets
Subtopic: Set Operations
Difficulty: Medium

Question: What does set1.union(set2) return?
A) Common elements
B) All elements from both sets
C) Elements only in set1
D) Empty set

✔ Correct Answer: B

Reason: union() returns new set containing all unique elements from both sets, combining them without duplicates.

Tag: Normal

---

### Question 205
Domain: Programming
Topic: Sets
Subtopic: Set Intersection
Difficulty: Easy

Question: What does set1.intersection(set2) return?
A) All elements
B) Common elements in both sets
C) Different elements
D) Empty set always

✔ Correct Answer: B

Reason: intersection() returns new set containing only elements present in both sets, finding commonality.

Tag: Normal

---


### Question 206
Domain: Programming
Topic: Code Analysis
Subtopic: Set Difference
Difficulty: Medium

Question: What is the output?
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 - set2)
```
A) {1, 2}
B) {3, 4}
C) {5, 6}
D) {1, 2, 3, 4, 5, 6}

✔ Correct Answer: A

Reason: Set difference (set1 - set2) returns elements in set1 but not in set2: {1, 2}.

Tag: Normal

---

### Question 207
Domain: Programming
Topic: Comprehensions
Subtopic: Set Comprehension
Difficulty: Medium

Question: What is the output?
```python
result = {x % 3 for x in range(6)}
print(result)
```
A) {0, 1, 2, 3, 4, 5}
B) {0, 1, 2}
C) [0, 1, 2, 0, 1, 2]
D) {0, 1, 2, 0, 1, 2}

✔ Correct Answer: B

Reason: Set comprehension with x % 3 for x in 0-5 gives: 0,1,2,0,1,2. Sets remove duplicates: {0, 1, 2}.

Tag: Normal

---

### Question 208
Domain: Programming
Topic: Nested Loops
Subtopic: Loop Complexity
Difficulty: Medium

Question: What is the time complexity of nested loops iterating n times each?
A) O(n)
B) O(2n)
C) O(n²)
D) O(log n)

✔ Correct Answer: C

Reason: Outer loop runs n times, inner loop runs n times for each outer iteration: n * n = O(n²).

Tag: Past Paper

---

### Question 209
Domain: Programming
Topic: Code Analysis
Subtopic: Nested Loop Output
Difficulty: Medium

Question: How many times does "X" print?
```java
for(int i=0; i<3; i++) {
    for(int j=0; j<2; j++) {
        System.out.print("X");
    }
}
```
A) 3
B) 5
C) 6
D) 9

✔ Correct Answer: C

Reason: Outer loop runs 3 times, inner loop runs 2 times per outer iteration: 3 * 2 = 6 times.

Tag: Normal

---

### Question 210
Domain: Programming
Topic: Conditional Operators
Subtopic: Logical AND
Difficulty: Easy

Question: When does (A && B) evaluate to true?
A) If A is true
B) If both A and B are true
C) If either is true
D) Never

✔ Correct Answer: B

Reason: Logical AND (&&) returns true only when both operands are true. If either is false, result is false.

Tag: Normal

---

### Question 211
Domain: Programming
Topic: Conditional Operators
Subtopic: Logical OR
Difficulty: Easy

Question: When does (A || B) evaluate to true?
A) Both must be true
B) At least one must be true
C) Both must be false
D) Never

✔ Correct Answer: B

Reason: Logical OR (||) returns true if at least one operand is true. Returns false only when both are false.

Tag: Normal

---

### Question 212
Domain: Programming
Topic: Code Analysis
Subtopic: Logical NOT
Difficulty: Easy

Question: What is the output?
```java
boolean flag = true;
System.out.println(!flag);
```
A) true
B) false
C) 1
D) 0

✔ Correct Answer: B

Reason: Logical NOT (!) inverts boolean value. !true = false.

Tag: Normal

---

### Question 213
Domain: Programming
Topic: Type Checking
Subtopic: Duck Typing
Difficulty: Hard

Question: What is duck typing?
A) Type checking ducks
B) Type determined by behavior, not explicit declaration
C) Static typing
D) No typing

✔ Correct Answer: B

Reason: Duck typing: "If it walks like a duck and quacks like a duck, it's a duck." Type determined by methods/properties, not inheritance.

Tag: Normal

---

### Question 214
Domain: Programming
Topic: Type Systems
Subtopic: Static vs Dynamic
Difficulty: Medium

Question: What characterizes statically typed languages?
A) No types
B) Types checked at compile time
C) Types checked at runtime
D) No type checking

✔ Correct Answer: B

Reason: Static typing checks types at compile time (C++, Java), catching type errors early. Dynamic typing checks at runtime (Python, JavaScript).

Tag: Normal

---

### Question 215
Domain: Programming
Topic: Type Systems
Subtopic: Strong vs Weak
Difficulty: Hard

Question: What characterizes strongly typed languages?
A) No type conversion
B) Strict type rules, limited implicit conversions
C) Weak types
D) No types

✔ Correct Answer: B

Reason: Strong typing enforces strict type rules with limited implicit conversions. Weak typing allows more implicit conversions (JavaScript: "5" + 1 = "51").

Tag: Normal

---

### Question 216
Domain: Programming
Topic: Code Analysis
Subtopic: Type Coercion
Difficulty: Hard

Question: What is the output in JavaScript?
```javascript
console.log("5" + 3);
console.log("5" - 3);
```
A) 8, 2
B) 53, 2
C) 8, 8
D) Error

✔ Correct Answer: B

Reason: + with string concatenates: "5" + 3 = "53". - coerces to numbers: "5" - 3 = 2. JavaScript's type coercion.

Tag: Normal

---

### Question 217
Domain: Programming
Topic: Operators
Subtopic: Equality Operators
Difficulty: Medium

Question: In JavaScript, what's the difference between == and ===?
A) No difference
B) == allows type coercion, === requires same type
C) === is faster
D) == is stricter

✔ Correct Answer: B

Reason: == performs type coercion before comparison. === (strict equality) requires same type and value, no coercion.

Tag: Normal

---

### Question 218
Domain: Programming
Topic: Code Analysis
Subtopic: Equality Comparison
Difficulty: Hard

Question: What is the output in JavaScript?
```javascript
console.log(0 == false);
console.log(0 === false);
```
A) true, true
B) true, false
C) false, false
D) false, true

✔ Correct Answer: B

Reason: 0 == false is true (type coercion: false becomes 0). 0 === false is false (different types: number vs boolean).

Tag: Normal

---

### Question 219
Domain: Programming
Topic: Scope
Subtopic: Block Scope
Difficulty: Medium

Question: Which keyword provides block scope in JavaScript?
A) var
B) let
C) function
D) global

✔ Correct Answer: B

Reason: let and const provide block scope (limited to {}). var has function scope, accessible throughout function regardless of blocks.

Tag: Normal

---

### Question 220
Domain: Programming
Topic: Code Analysis
Subtopic: Hoisting
Difficulty: Hard

Question: What is the output?
```javascript
console.log(x);
var x = 5;
```
A) 5
B) undefined
C) Error
D) null

✔ Correct Answer: B

Reason: var declarations are hoisted to top but initialization isn't. Declaration exists but value is undefined until assignment line.

Tag: Normal

---


### Question 221
Domain: Programming
Topic: Scope
Subtopic: Temporal Dead Zone
Difficulty: Hard

Question: What is the Temporal Dead Zone in JavaScript?
A) Time zone
B) Period between scope start and let/const initialization
C) Dead code
D) Timeout zone

✔ Correct Answer: B

Reason: TDZ is the period from block start to let/const initialization where variable exists but cannot be accessed, throwing ReferenceError.

Tag: Normal

---

### Question 222
Domain: Programming
Topic: Closures
Subtopic: Closure in Loops
Difficulty: Hard

Question: What is the output?
```javascript
for(var i=0; i<3; i++) {
    setTimeout(() => console.log(i), 100);
}
```
A) 0 1 2
B) 3 3 3
C) 0 0 0
D) Error

✔ Correct Answer: B

Reason: var has function scope. All closures reference same i. By timeout execution, loop finished with i=3. Using let fixes this.

Tag: Normal

---

### Question 223
Domain: Programming
Topic: Arrow Functions
Subtopic: this Binding
Difficulty: Hard

Question: How does 'this' behave in arrow functions?
A) Same as regular functions
B) Lexically bound to enclosing scope
C) Always undefined
D) Always global

✔ Correct Answer: B

Reason: Arrow functions don't have own 'this', they inherit it from enclosing scope (lexical binding), unlike regular functions with dynamic 'this'.

Tag: Normal

---

### Question 224
Domain: Programming
Topic: Prototypes
Subtopic: Prototype Chain
Difficulty: Hard

Question: What is the prototype chain in JavaScript?
A) Chain of functions
B) Mechanism for inheritance through prototype objects
C) Array chain
D) String chain

✔ Correct Answer: B

Reason: Prototype chain is how JavaScript implements inheritance. Objects inherit properties from their prototype, which inherits from its prototype, etc.

Tag: Normal

---

### Question 225
Domain: Programming
Topic: Classes
Subtopic: ES6 Classes
Difficulty: Medium

Question: Are JavaScript ES6 classes true classes?
A) Yes, completely different
B) No, syntactic sugar over prototypes
C) Yes, no prototypes
D) Not related

✔ Correct Answer: B

Reason: ES6 classes are syntactic sugar over JavaScript's prototype-based inheritance, providing cleaner syntax but same underlying mechanism.

Tag: Normal

---

### Question 226
Domain: Programming
Topic: Code Analysis
Subtopic: Class Inheritance
Difficulty: Medium

Question: What is the output?
```javascript
class Animal {
    speak() { return "Sound"; }
}
class Dog extends Animal {
    speak() { return "Bark"; }
}
let d = new Dog();
console.log(d.speak());
```
A) Sound
B) Bark
C) SoundBark
D) Error

✔ Correct Answer: B

Reason: Dog overrides speak() method. When called on Dog instance, Dog's version executes: "Bark".

Tag: Normal

---

### Question 227
Domain: Programming
Topic: Destructuring
Subtopic: Array Destructuring
Difficulty: Medium

Question: What is the output?
```javascript
let [a, , c] = [1, 2, 3];
console.log(a, c);
```
A) 1 2
B) 1 3
C) 2 3
D) Error

✔ Correct Answer: B

Reason: Array destructuring with skipped element (empty slot). a gets first (1), c gets third (3), second is skipped.

Tag: Normal

---

### Question 228
Domain: Programming
Topic: Destructuring
Subtopic: Object Destructuring
Difficulty: Medium

Question: What is the output?
```javascript
let {name, age} = {name: "John", age: 30, city: "NYC"};
console.log(name);
```
A) undefined
B) John
C) Error
D) {name: "John"}

✔ Correct Answer: B

Reason: Object destructuring extracts properties by name. name variable gets value "John" from object.

Tag: Normal

---

### Question 229
Domain: Programming
Topic: Spread Operator
Subtopic: Array Spread
Difficulty: Medium

Question: What is the output?
```javascript
let arr1 = [1, 2];
let arr2 = [...arr1, 3, 4];
console.log(arr2);
```
A) [[1,2], 3, 4]
B) [1, 2, 3, 4]
C) [1, 2]
D) Error

✔ Correct Answer: B

Reason: Spread operator (...) expands array elements. [...arr1, 3, 4] creates new array: [1, 2, 3, 4].

Tag: Normal

---

### Question 230
Domain: Programming
Topic: Rest Parameters
Subtopic: Rest Syntax
Difficulty: Medium

Question: What does rest parameter do?
A) Rest execution
B) Collects remaining arguments into array
C) Spreads array
D) Stops function

✔ Correct Answer: B

Reason: Rest parameter (...args) collects all remaining arguments into an array, opposite of spread which expands array.

Tag: Normal

---

### Question 231
Domain: Programming
Topic: Code Analysis
Subtopic: Rest Parameters
Difficulty: Hard

Question: What is the output?
```javascript
function test(first, ...rest) {
    console.log(rest.length);
}
test(1, 2, 3, 4);
```
A) 1
B) 3
C) 4
D) Error

✔ Correct Answer: B

Reason: first gets 1, rest collects remaining arguments [2, 3, 4]. rest.length is 3.

Tag: Normal

---

### Question 232
Domain: Programming
Topic: Default Parameters
Subtopic: Function Defaults
Difficulty: Easy

Question: What happens if argument is not provided for parameter with default value?
A) Error
B) Default value is used
C) undefined
D) null

✔ Correct Answer: B

Reason: Default parameters provide fallback values when arguments are not provided or are undefined, preventing errors.

Tag: Normal

---

### Question 233
Domain: Programming
Topic: Code Analysis
Subtopic: Default Parameters
Difficulty: Medium

Question: What is the output?
```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Alice")
```
A) Error
B) Hello Guest, Hello Alice
C) Hello Alice twice
D) Hello Guest twice

✔ Correct Answer: B

Reason: First call uses default "Guest". Second call uses provided "Alice". Outputs: Hello Guest, Hello Alice.

Tag: Normal

---

### Question 234
Domain: Programming
Topic: Recursion
Subtopic: Tail Recursion
Difficulty: Hard

Question: What is tail recursion?
A) Recursion at end
B) Recursive call is last operation in function
C) First recursion
D) No recursion

✔ Correct Answer: B

Reason: Tail recursion has recursive call as the last operation, allowing optimization (tail call optimization) to reuse stack frame.

Tag: Normal

---

### Question 235
Domain: Programming
Topic: Code Analysis
Subtopic: Recursion vs Iteration
Difficulty: Medium

Question: What is the iterative equivalent of this recursive sum?
```python
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n-1)
```
A) for loop accumulating sum
B) while loop only
C) No equivalent
D) Nested loops

✔ Correct Answer: A

Reason: Iterative version uses loop: total=0; for i in range(1, n+1): total += i. Same result without recursion overhead.

Tag: Normal

---

### Question 236
Domain: Programming
Topic: Memoization
Subtopic: Optimization
Difficulty: Hard

Question: What is memoization?
A) Memory allocation
B) Caching function results to avoid recomputation
C) Memory deletion
D) Memory compression

✔ Correct Answer: B

Reason: Memoization caches function results for given inputs, returning cached result on subsequent calls with same inputs, optimizing recursive functions.

Tag: Normal

---

### Question 237
Domain: Programming
Topic: Code Analysis
Subtopic: Memoization Example
Difficulty: Hard

Question: Why is memoized fibonacci faster?
A) Better algorithm
B) Avoids redundant recursive calls by caching
C) Uses iteration
D) No difference

✔ Correct Answer: B

Reason: Naive fibonacci has exponential time due to redundant calculations. Memoization caches results, reducing to O(n) by computing each value once.

Tag: Normal

---

### Question 238
Domain: Programming
Topic: Dynamic Programming
Subtopic: DP Basics
Difficulty: Hard

Question: What is dynamic programming?
A) Dynamic typing
B) Solving problems by breaking into overlapping subproblems
C) Runtime programming
D) Fast programming

✔ Correct Answer: B

Reason: DP solves optimization problems by breaking into overlapping subproblems, storing solutions to avoid recomputation (memoization or tabulation).

Tag: Past Paper

---

### Question 239
Domain: Programming
Topic: Algorithms
Subtopic: Greedy Algorithms
Difficulty: Medium

Question: What characterizes greedy algorithms?
A) Greedy for memory
B) Make locally optimal choice at each step
C) Try all possibilities
D) Random choices

✔ Correct Answer: B

Reason: Greedy algorithms make locally optimal choice at each step, hoping to find global optimum, efficient but don't always give optimal solution.

Tag: Normal

---

### Question 240
Domain: Programming
Topic: Algorithms
Subtopic: Divide and Conquer
Difficulty: Medium

Question: What is divide and conquer strategy?
A) Military strategy
B) Break problem into subproblems, solve recursively, combine
C) Sequential solving
D) Random solving

✔ Correct Answer: B

Reason: Divide and conquer breaks problem into smaller subproblems, solves recursively, then combines solutions (merge sort, quick sort, binary search).

Tag: Normal

---

### Question 241
Domain: Programming
Topic: Code Analysis
Subtopic: String Methods
Difficulty: Easy

Question: What is the output?
```python
s = "hello world"
print(s.upper())
```
A) hello world
B) HELLO WORLD
C) Hello World
D) Error

✔ Correct Answer: B

Reason: upper() method converts all characters to uppercase, returning new string "HELLO WORLD" (strings are immutable).

Tag: Normal

---

### Question 242
Domain: Programming
Topic: String Methods
Subtopic: String Splitting
Difficulty: Easy

Question: What does split() method do?
A) Splits characters
B) Splits string into list/array based on delimiter
C) Deletes string
D) Reverses string

✔ Correct Answer: B

Reason: split() divides string into list/array of substrings based on delimiter. "a,b,c".split(",") returns ["a", "b", "c"].

Tag: Normal

---

### Question 243
Domain: Programming
Topic: Code Analysis
Subtopic: String Join
Difficulty: Medium

Question: What is the output?
```python
words = ['Hello', 'World']
print(' '.join(words))
```
A) HelloWorld
B) Hello World
C) ['Hello', 'World']
D) Error

✔ Correct Answer: B

Reason: join() concatenates list elements with specified separator. ' '.join() joins with space: "Hello World".

Tag: Normal

---

### Question 244
Domain: Programming
Topic: String Methods
Subtopic: String Trimming
Difficulty: Easy

Question: What does trim() or strip() do?
A) Removes all spaces
B) Removes leading and trailing whitespace
C) Removes middle spaces
D) Adds spaces

✔ Correct Answer: B

Reason: trim() (JavaScript) or strip() (Python) removes whitespace from beginning and end of string, not from middle.

Tag: Normal

---

### Question 245
Domain: Programming
Topic: Code Analysis
Subtopic: String Replace
Difficulty: Medium

Question: What is the output?
```python
s = "hello hello"
print(s.replace("hello", "hi"))
```
A) hi hello
B) hi hi
C) hello hi
D) Error

✔ Correct Answer: B

Reason: replace() replaces all occurrences of substring. Both "hello" instances become "hi": "hi hi".

Tag: Normal

---

### Question 246
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Class Variables
Difficulty: Medium

Question: What is a class variable?
A) Instance variable
B) Variable shared by all instances of class
C) Local variable
D) Parameter

✔ Correct Answer: B

Reason: Class variables (static in Java) are shared across all instances, belonging to class itself rather than individual objects.

Tag: Normal

---

### Question 247
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Instance Variables
Difficulty: Easy

Question: What is an instance variable?
A) Shared by all instances
B) Unique to each object instance
C) Global variable
D) Constant

✔ Correct Answer: B

Reason: Instance variables are unique to each object, storing object-specific state, unlike class variables which are shared.

Tag: Normal

---

### Question 248
Domain: Programming
Topic: Code Analysis
Subtopic: Class vs Instance Variables
Difficulty: Hard

Question: What is the output?
```python
class Test:
    count = 0
    def __init__(self):
        Test.count += 1

t1 = Test()
t2 = Test()
print(Test.count)
```
A) 0
B) 1
C) 2
D) Error

✔ Correct Answer: C

Reason: count is class variable. Each __init__ increments it. Two objects created, count = 2.

Tag: Normal

---

### Question 249
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Property Decorators
Difficulty: Hard

Question: What does @property decorator do in Python?
A) Creates property
B) Makes method accessible as attribute
C) Deletes property
D) Encrypts property

✔ Correct Answer: B

Reason: @property decorator makes method accessible like an attribute, enabling getter/setter logic while maintaining attribute-like syntax.

Tag: Normal

---

### Question 250
Domain: Programming
Topic: Code Analysis
Subtopic: Property Getter
Difficulty: Hard

Question: What is the output?
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area)
```
A) Error (missing parentheses)
B) 78.5
C) Function object
D) 25

✔ Correct Answer: B

Reason: @property allows calling area without parentheses. Calculates 3.14 * 5² = 78.5.

Tag: Normal

---

### Question 251
Domain: Programming
Topic: Magic Methods
Subtopic: Dunder Methods
Difficulty: Medium

Question: What are dunder methods in Python?
A) Dangerous methods
B) Special methods with double underscores (__method__)
C) Deleted methods
D) Duplicate methods

✔ Correct Answer: B

Reason: Dunder (double underscore) methods like __init__, __str__, __add__ are special methods defining object behavior for built-in operations.

Tag: Normal

---

### Question 252
Domain: Programming
Topic: Code Analysis
Subtopic: __str__ Method
Difficulty: Medium

Question: What is the output?
```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"

p = Person("Alice")
print(p)
```
A) Object reference
B) Person: Alice
C) Alice
D) Error

✔ Correct Answer: B

Reason: __str__ defines string representation. print() calls __str__, returning "Person: Alice".

Tag: Normal

---

### Question 253
Domain: Programming
Topic: Magic Methods
Subtopic: Operator Overloading
Difficulty: Hard

Question: Which method overloads the + operator in Python?
A) __plus__
B) __add__
C) __sum__
D) __concat__

✔ Correct Answer: B

Reason: __add__ method overloads + operator, allowing custom addition behavior for objects. __sub__ for -, __mul__ for *, etc.

Tag: Normal

---

### Question 254
Domain: Programming
Topic: Code Analysis
Subtopic: Operator Overloading
Difficulty: Hard

Question: What is the output?
```python
class Point:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return Point(self.x + other.x)

p1 = Point(5)
p2 = Point(3)
p3 = p1 + p2
print(p3.x)
```
A) 5
B) 3
C) 8
D) Error

✔ Correct Answer: C

Reason: __add__ enables p1 + p2, creating new Point with x = 5 + 3 = 8.

Tag: Normal

---

### Question 255
Domain: Programming
Topic: Context Managers
Subtopic: with Statement
Difficulty: Medium

Question: What does 'with' statement ensure in Python?
A) Fast execution
B) Proper resource cleanup (calls __exit__)
C) Error prevention
D) Type checking

✔ Correct Answer: B

Reason: 'with' statement ensures __exit__ is called for cleanup even if exceptions occur, commonly used for file handling and resource management.

Tag: Normal

---

### Question 256
Domain: Programming
Topic: Code Analysis
Subtopic: Context Manager
Difficulty: Medium

Question: What is the advantage of this code?
```python
with open('file.txt', 'r') as f:
    data = f.read()
```
A) Faster reading
B) File automatically closed even if error occurs
C) Better encryption
D) Larger files

✔ Correct Answer: B

Reason: 'with' ensures file is properly closed after block, even if exception occurs, preventing resource leaks.

Tag: Normal

---

### Question 257
Domain: Programming
Topic: List Methods
Subtopic: List Modification
Difficulty: Easy

Question: What does list.pop() do without arguments?
A) Removes first element
B) Removes and returns last element
C) Removes all elements
D) Error

✔ Correct Answer: B

Reason: pop() without arguments removes and returns last element. pop(0) removes first. pop(i) removes element at index i.

Tag: Normal

---

### Question 258
Domain: Programming
Topic: Code Analysis
Subtopic: List Remove
Difficulty: Medium

Question: What is the output?
```python
lst = [1, 2, 3, 2, 4]
lst.remove(2)
print(lst)
```
A) [1, 3, 4]
B) [1, 3, 2, 4]
C) [1, 2, 3, 4]
D) Error

✔ Correct Answer: B

Reason: remove() removes first occurrence of value. First 2 is removed: [1, 3, 2, 4]. Second 2 remains.

Tag: Normal

---

### Question 259
Domain: Programming
Topic: List Methods
Subtopic: List Sorting
Difficulty: Easy

Question: What's the difference between sort() and sorted()?
A) No difference
B) sort() modifies list in-place, sorted() returns new sorted list
C) sorted() is slower
D) sort() returns new list

✔ Correct Answer: B

Reason: sort() modifies list in-place (returns None). sorted() returns new sorted list, leaving original unchanged.

Tag: Normal

---

### Question 260
Domain: Programming
Topic: Code Analysis
Subtopic: List Reverse
Difficulty: Easy

Question: What is the output?
```python
lst = [1, 2, 3]
lst.reverse()
print(lst)
```
A) [1, 2, 3]
B) [3, 2, 1]
C) [3, 1, 2]
D) Error

✔ Correct Answer: B

Reason: reverse() reverses list in-place. [1, 2, 3] becomes [3, 2, 1].

Tag: Normal

---

### Question 261
Domain: Programming
Topic: Dictionary Methods
Subtopic: Dict Keys
Difficulty: Easy

Question: What does dict.keys() return?
A) Values
B) View of dictionary keys
C) Items
D) Length

✔ Correct Answer: B

Reason: keys() returns view object containing dictionary keys, iterable for loops or convertible to list.

Tag: Normal

---

### Question 262
Domain: Programming
Topic: Code Analysis
Subtopic: Dict Iteration
Difficulty: Medium

Question: What is the output?
```python
d = {'a': 1, 'b': 2}
for key in d:
    print(key, end=' ')
```
A) 1 2
B) a b
C) a 1 b 2
D) Error

✔ Correct Answer: B

Reason: Iterating over dictionary directly iterates over keys. Prints: a b. Use d.items() for key-value pairs.

Tag: Normal

---

### Question 263
Domain: Programming
Topic: Dictionary Methods
Subtopic: Dict Update
Difficulty: Medium

Question: What does dict.update() do?
A) Updates one key
B) Merges another dictionary into current one
C) Deletes keys
D) Sorts dictionary

✔ Correct Answer: B

Reason: update() merges another dictionary, adding new keys and updating existing ones with new values.

Tag: Normal

---

### Question 264
Domain: Programming
Topic: Code Analysis
Subtopic: Dict Comprehension with Condition
Difficulty: Hard

Question: What is the output?
```python
d = {x: x**2 for x in range(5) if x % 2 == 0}
print(d)
```
A) {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
B) {0: 0, 2: 4, 4: 16}
C) {1: 1, 3: 9}
D) Error

✔ Correct Answer: B

Reason: Dict comprehension with filter. Even numbers (0, 2, 4) squared: {0: 0, 2: 4, 4: 16}.

Tag: Normal

---

### Question 265
Domain: Programming
Topic: Exception Handling
Subtopic: Multiple Except
Difficulty: Medium

Question: Can you have multiple except blocks?
A) No
B) Yes, to handle different exception types
C) Only two
D) Not recommended

✔ Correct Answer: B

Reason: Multiple except blocks handle different exception types differently, with more specific exceptions caught first, then general ones.

Tag: Normal

---

### Question 266
Domain: Programming
Topic: Code Analysis
Subtopic: Exception Handling
Difficulty: Hard

Question: What is the output?
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("A")
except Exception:
    print("B")
finally:
    print("C")
```
A) B C
B) A C
C) C
D) A B C

✔ Correct Answer: B

Reason: ZeroDivisionError caught by first except (prints A). finally always executes (prints C). Output: A C.

Tag: Normal

---

### Question 267
Domain: Programming
Topic: Exception Handling
Subtopic: Raise Statement
Difficulty: Medium

Question: What does raise statement do?
A) Raises variable
B) Throws/raises an exception
C) Increases value
D) Elevates priority

✔ Correct Answer: B

Reason: raise statement explicitly throws an exception, either creating new exception or re-raising current one.

Tag: Normal

---

### Question 268
Domain: Programming
Topic: Code Analysis
Subtopic: Custom Exception
Difficulty: Hard

Question: What is the output?
```python
class CustomError(Exception):
    pass

try:
    raise CustomError("Test")
except CustomError as e:
    print(str(e))
```
A) Error
B) Test
C) CustomError
D) None

✔ Correct Answer: B

Reason: Custom exception raised with message "Test". Caught and message printed: Test.

Tag: Normal

---

### Question 269
Domain: Programming
Topic: File Handling
Subtopic: File Reading
Difficulty: Easy

Question: What does read() method do?
A) Reads one line
B) Reads entire file content
C) Reads one character
D) Reads file name

✔ Correct Answer: B

Reason: read() reads entire file content as single string. readline() reads one line, readlines() reads all lines as list.

Tag: Normal

---

### Question 270
Domain: Programming
Topic: File Handling
Subtopic: File Writing
Difficulty: Easy

Question: What mode opens file for writing, creating if doesn't exist?
A) 'r'
B) 'w'
C) 'a'
D) 'x'

✔ Correct Answer: B

Reason: 'w' mode opens for writing, creating file if doesn't exist, truncating if exists. 'a' appends, 'x' creates only if doesn't exist.

Tag: Normal

---

### Question 271
Domain: Programming
Topic: Code Analysis
Subtopic: File Operations
Difficulty: Medium

Question: What is the output?
```python
with open('test.txt', 'w') as f:
    f.write("Hello")
    f.write("World")
```
File content?
A) Hello World
B) HelloWorld
C) Hello\nWorld
D) Error

✔ Correct Answer: B

Reason: write() doesn't add newlines automatically. Two writes concatenate: "HelloWorld". Use writelines() or add \n explicitly.

Tag: Normal

---

### Question 272
Domain: Programming
Topic: Command Line Arguments
Subtopic: sys.argv
Difficulty: Medium

Question: In Python, what is sys.argv[0]?
A) First argument
B) Script name
C) Number of arguments
D) Error

✔ Correct Answer: B

Reason: sys.argv[0] is the script name. sys.argv[1] onwards are command-line arguments passed to script.

Tag: Normal

---

### Question 273
Domain: Programming
Topic: Environment Variables
Subtopic: os.environ
Difficulty: Easy

Question: How do you access environment variables in Python?
A) env.get()
B) os.environ
C) sys.env
D) environment.get()

✔ Correct Answer: B

Reason: os.environ dictionary provides access to environment variables. Use os.environ.get('VAR') for safe access with default.

Tag: Normal

---

### Question 274
Domain: Programming
Topic: Code Analysis
Subtopic: List Comprehension with Condition
Difficulty: Medium

Question: What is the output?
```python
result = [x if x % 2 == 0 else x*2 for x in range(5)]
print(result)
```
A) [0, 1, 2, 3, 4]
B) [0, 2, 2, 6, 4]
C) [0, 2, 4, 6, 8]
D) Error

✔ Correct Answer: B

Reason: For each x: if even keep it, if odd double it. 0(even)→0, 1(odd)→2, 2(even)→2, 3(odd)→6, 4(even)→4.

Tag: Normal

---

### Question 275
Domain: Programming
Topic: Nested Functions
Subtopic: Inner Functions
Difficulty: Medium

Question: Can inner functions access outer function variables?
A) No
B) Yes, through closure
C) Only global variables
D) Only with special keyword

✔ Correct Answer: B

Reason: Inner functions can access outer function's variables through closure, even after outer function returns.

Tag: Normal

---

### Question 276
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

add5 = outer(5)
print(add5(3))
```
A) 5
B) 3
C) 8
D) Error

✔ Correct Answer: C

Reason: inner function closes over x from outer scope. add5 is inner with x=5. add5(3) returns 5+3=8.

Tag: Normal

---

### Question 277
Domain: Programming
Topic: Generators
Subtopic: yield Keyword
Difficulty: Hard

Question: What does yield keyword do?
A) Stops function
B) Pauses function, returns value, resumes on next call
C) Returns final value
D) Yields control

✔ Correct Answer: B

Reason: yield pauses function execution, returns value to caller, and resumes from that point on next iteration, creating generator.

Tag: Normal

---

### Question 278
Domain: Programming
Topic: Code Analysis
Subtopic: Generator Function
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
C) 3 3
D) Error

✔ Correct Answer: B

Reason: First next() returns 1, pauses. Second next() resumes, returns 2. Generator maintains state between calls.

Tag: Normal

---

### Question 279
Domain: Programming
Topic: Decorators
Subtopic: Function Decorators
Difficulty: Hard

Question: What is a decorator in Python?
A) Design pattern
B) Function that modifies another function's behavior
C) Class decorator
D) Variable modifier

✔ Correct Answer: B

Reason: Decorator is function that takes function as argument, adds functionality, returns modified function. Uses @decorator syntax.

Tag: Normal

---

### Question 280
Domain: Programming
Topic: Code Analysis
Subtopic: Decorator Example
Difficulty: Hard

Question: What is the output?
```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()
```
A) Hello
B) Before Hello After
C) Before After
D) Error

✔ Correct Answer: B

Reason: @decorator applies decorator to hello. Calling hello() executes wrapper which prints Before, calls original hello (prints Hello), prints After.

Tag: Normal

---

### Question 281
Domain: Programming
Topic: Lambda Functions
Subtopic: Lambda with Multiple Arguments
Difficulty: Medium

Question: What is the output?
```python
multiply = lambda x, y: x * y
print(multiply(4, 5))
```
A) 9
B) 20
C) 45
D) Error

✔ Correct Answer: B

Reason: Lambda with two parameters multiplies them. multiply(4, 5) returns 4 * 5 = 20.

Tag: Normal

---

### Question 282
Domain: Programming
Topic: Higher-Order Functions
Subtopic: Function as Argument
Difficulty: Medium

Question: What is a higher-order function?
A) Complex function
B) Function that takes function as argument or returns function
C) Fast function
D) Nested function

✔ Correct Answer: B

Reason: Higher-order functions operate on other functions by taking them as arguments or returning them (map, filter, decorators).

Tag: Normal

---

### Question 283
Domain: Programming
Topic: Code Analysis
Subtopic: Callback Function
Difficulty: Hard

Question: What is the output?
```javascript
function process(callback) {
    callback("Done");
}

process(function(msg) {
    console.log(msg);
});
```
A) undefined
B) Done
C) callback
D) Error

✔ Correct Answer: B

Reason: process() calls the callback function with "Done" as argument. Callback logs "Done".

Tag: Normal

---

### Question 284
Domain: Programming
Topic: Promises
Subtopic: Promise States
Difficulty: Medium

Question: What are the three states of a Promise?
A) start, middle, end
B) pending, fulfilled, rejected
C) new, running, done
D) open, closed, error

✔ Correct Answer: B

Reason: Promise has three states: pending (initial), fulfilled (successful), rejected (failed). Once settled (fulfilled/rejected), state is immutable.

Tag: Normal

---

### Question 285
Domain: Programming
Topic: Code Analysis
Subtopic: Promise Chain
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

Reason: Chain: 5 → multiply by 2 → 10 → add 3 → 13. Each then receives result from previous.

Tag: Normal

---

### Question 286
Domain: Programming
Topic: Async/Await
Subtopic: Async Functions
Difficulty: Medium

Question: What does async function always return?
A) Value
B) Promise
C) undefined
D) Callback

✔ Correct Answer: B

Reason: async functions always return Promise. If return value, it's wrapped in resolved Promise. If throw error, Promise is rejected.

Tag: Normal

---

### Question 287
Domain: Programming
Topic: Code Analysis
Subtopic: Await Keyword
Difficulty: Hard

Question: What does await do?
A) Waits forever
B) Pauses async function until Promise resolves
C) Stops execution
D) Creates Promise

✔ Correct Answer: B

Reason: await pauses async function execution until Promise resolves, then returns resolved value. Can only be used inside async functions.

Tag: Normal

---

### Question 288
Domain: Programming
Topic: Error Handling
Subtopic: Try-Catch with Async
Difficulty: Hard

Question: How do you handle errors in async/await?
A) .catch()
B) try-catch block
C) error callback
D) Cannot handle

✔ Correct Answer: B

Reason: Use try-catch blocks around await statements to handle rejected Promises. Alternative: use .catch() on Promise chain.

Tag: Normal

---

### Question 289
Domain: Programming
Topic: Code Analysis
Subtopic: Array Methods
Difficulty: Medium

Question: What is the output?
```javascript
let arr = [1, 2, 3, 4];
let result = arr.find(x => x > 2);
console.log(result);
```
A) [3, 4]
B) 3
C) true
D) 2

✔ Correct Answer: B

Reason: find() returns first element satisfying condition. First element > 2 is 3.

Tag: Normal

---

### Question 290
Domain: Programming
Topic: Array Methods
Subtopic: findIndex
Difficulty: Easy

Question: What does findIndex() return?
A) Element
B) Index of first element matching condition
C) All indices
D) Boolean

✔ Correct Answer: B

Reason: findIndex() returns index of first element satisfying condition. Returns -1 if no match found.

Tag: Normal

---

### Question 291
Domain: Programming
Topic: Code Analysis
Subtopic: Array Every
Difficulty: Medium

Question: What is the output?
```javascript
let arr = [2, 4, 6, 8];
console.log(arr.every(x => x % 2 === 0));
```
A) false
B) true
C) [true, true, true, true]
D) Error

✔ Correct Answer: B

Reason: every() tests if all elements satisfy condition. All elements are even, returns true.

Tag: Normal

---

### Question 292
Domain: Programming
Topic: Array Methods
Subtopic: Some Method
Difficulty: Easy

Question: What does some() method do?
A) Tests if all elements match
B) Tests if at least one element matches condition
C) Returns some elements
D) Removes elements

✔ Correct Answer: B

Reason: some() returns true if at least one element satisfies condition, false if none do. Opposite of every().

Tag: Normal

---

### Question 293
Domain: Programming
Topic: Code Analysis
Subtopic: Array Includes
Difficulty: Easy

Question: What is the output?
```javascript
let arr = [1, 2, 3];
console.log(arr.includes(2));
```
A) 1
B) true
C) false
D) 2

✔ Correct Answer: B

Reason: includes() checks if array contains value, returns boolean. Array contains 2, returns true.

Tag: Normal

---

### Question 294
Domain: Programming
Topic: Array Methods
Subtopic: Array Concat
Difficulty: Easy

Question: What does concat() do?
A) Concatenates strings
B) Merges arrays into new array
C) Modifies original array
D) Removes elements

✔ Correct Answer: B

Reason: concat() merges two or more arrays into new array without modifying originals. arr1.concat(arr2) returns combined array.

Tag: Normal

---

### Question 295
Domain: Programming
Topic: Code Analysis
Subtopic: Array Slice
Difficulty: Medium

Question: What is the output?
```python
arr = [0, 1, 2, 3, 4]
print(arr[1:4])
```
A) [0, 1, 2, 3]
B) [1, 2, 3]
C) [1, 2, 3, 4]
D) [2, 3, 4]

✔ Correct Answer: B

Reason: Slice [1:4] includes start index 1, excludes end index 4. Returns elements at indices 1, 2, 3: [1, 2, 3].

Tag: Normal

---

### Question 296
Domain: Programming
Topic: Array Methods
Subtopic: Array Splice
Difficulty: Hard

Question: What does splice() do in JavaScript?
A) Slices array
B) Modifies array by removing/adding elements in place
C) Creates new array
D) Sorts array

✔ Correct Answer: B

Reason: splice() modifies original array by removing/replacing/adding elements. slice() creates new array without modifying original.

Tag: Normal

---

### Question 297
Domain: Programming
Topic: Code Analysis
Subtopic: Splice Example
Difficulty: Hard

Question: What is the output?
```javascript
let arr = [1, 2, 3, 4, 5];
arr.splice(2, 2, 'a', 'b');
console.log(arr);
```
A) [1, 2, 3, 4, 5]
B) [1, 2, 'a', 'b', 5]
C) [1, 2, 'a', 'b']
D) ['a', 'b', 3, 4, 5]

✔ Correct Answer: B

Reason: splice(2, 2, 'a', 'b') starts at index 2, removes 2 elements (3, 4), inserts 'a', 'b'. Result: [1, 2, 'a', 'b', 5].

Tag: Normal

---

### Question 298
Domain: Programming
Topic: Regular Expressions
Subtopic: Pattern Matching
Difficulty: Medium

Question: What does \d represent in regex?
A) Letter
B) Digit
C) Dot
D) Delimiter

✔ Correct Answer: B

Reason: \d matches any digit (0-9). \D matches non-digits. \w matches word characters, \s matches whitespace.

Tag: Normal

---

### Question 299
Domain: Programming
Topic: Code Analysis
Subtopic: Regex Match
Difficulty: Hard

Question: What is the output?
```python
import re
text = "Phone: 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(match.group() if match else "No match")
```
A) No match
B) 123-456-7890
C) 123
D) Error

✔ Correct Answer: B

Reason: Pattern \d{3}-\d{3}-\d{4} matches phone format. search() finds match, group() returns matched string: "123-456-7890".

Tag: Normal

---

### Question 300
Domain: Programming
Topic: Regular Expressions
Subtopic: Regex Flags
Difficulty: Medium

Question: What does the 'i' flag do in regex?
A) Ignore spaces
B) Case-insensitive matching
C) Include newlines
D) Invert match

✔ Correct Answer: B

Reason: 'i' flag makes pattern matching case-insensitive. /hello/i matches "hello", "Hello", "HELLO". Other flags: g (global), m (multiline).

Tag: Normal

---
</content>
</file>
# Programming - MCQ Batch 04
## Questions 301-400

---

### Question 301
Domain: Programming
Topic: Object-Oriented Programming
Subtopic: Abstract Classes
Difficulty: Medium

Question: What is an abstract class?
A) Class without methods
B) Class that cannot be instantiated, serves as blueprint
C) Final class
D) Static class

✔ Correct Answer: B

Reason: Abstract class cannot be instantiated directly, contains abstract methods that must be implemented by subclasses, serving as template.

Tag: Past Paper

---

### Question 302
Domain: Programming
Topic: Code Analysis
Subtopic: Abstract Methods
Difficulty: Hard

Question: What happens if you try to instantiate an abstract class in Java?
```java
abstract class Shape {
    abstract void draw();
}
Shape s = new Shape();
```
A) Creates object
B) Compile error
C) Runtime error
D) Creates null

✔ Correct Answer: B

Reason: Cannot instantiate abstract class directly. Compile error occurs. Must create concrete subclass that implements abstract methods.

Tag: Normal

---

### Question 303
Domain: Programming
Topic: Interfaces
Subtopic: Interface vs Abstract Class
Difficulty: Hard

Question: What is a key difference between interface and abstract class in Java?
A) No difference
B) Interface supports multiple inheritance, abstract class doesn't
C) Abstract class is faster
D) Interface has constructors

✔ Correct Answer: B

Reason: Class can implement multiple interfaces but extend only one abstract class. Interfaces define contract, abstract classes provide partial implementation.

Tag: Past Paper

---

### Question 304
Domain: Programming
Topic: Code Analysis
Subtopic: Interface Implementation
Difficulty: Medium

Question: What is required when implementing an interface?
```java
interface Drawable {
    void draw();
}
class Circle implements Drawable {
    // ?
}
```
A) Nothing
B) Must implement all interface methods
C) Optional implementation
D) Only constructor

✔ Correct Answer: B

Reason: Class implementing interface must provide implementation for all interface methods, otherwise must be declared abstract.

Tag: Normal

---

### Question 305
Domain: Programming
Topic: Polymorphism
Subtopic: Method Overriding
Difficulty: Medium

Question: What is method overriding?
A) Overloading
B) Subclass provides specific implementation of superclass method
C) Deleting method
D) Renaming method

✔ Correct Answer: B

Reason: Overriding occurs when subclass provides its own implementation of inherited method with same signature, enabling runtime polymorphism.

Tag: Past Paper

---

### Question 306
Domain: Programming
Topic: Polymorphism
Subtopic: Method Overloading
Difficulty: Medium

Question: What is method overloading?
A) Too many methods
B) Multiple methods with same name but different parameters
C) Overriding
D: Deleting methods

✔ Correct Answer: B

Reason: Overloading allows multiple methods with same name but different parameter lists (number, type, order), resolved at compile time.

Tag: Past Paper

---

### Question 307
Domain: Programming
Topic: Code Analysis
Subtopic: Overloading Example
Difficulty: Medium

Question: Which methods are correctly overloaded?
```java
void print(int x) {}
void print(String s) {}
void print(int x, int y) {}
```
A) None
B) All three
C) Only first two
D) Error

✔ Correct Answer: B

Reason: All three have same name but different parameter lists (different types or counts), valid overloading.

Tag: Normal

---

### Question 308
Domain: Programming
Topic: Encapsulation
Subtopic: Access Modifiers
Difficulty: Easy

Question: Which access modifier makes member accessible only within class?
A) public
B) private
C) protected
D) default

✔ Correct Answer: B

Reason: private restricts access to within class only. public allows access from anywhere. protected allows subclasses. default allows package access.

Tag: Past Paper

---

### Question 309
Domain: Programming
Topic: Code Analysis
Subtopic: Getters and Setters
Difficulty: Medium

Question: Why use getters and setters instead of public fields?
```java
private int age;
public int getAge() { return age; }
public void setAge(int age) { this.age = age; }
```
A) Slower
B) Encapsulation, validation, control access
C) No benefit
D) Required by compiler

✔ Correct Answer: B

Reason: Getters/setters provide encapsulation, allow validation logic, enable changing implementation without affecting external code.

Tag: Normal

---

### Question 310
Domain: Programming
Topic: Inheritance
Subtopic: super Keyword
Difficulty: Medium

Question: What does super keyword do?
A) Makes class super
B) Refers to parent class members
C) Creates superclass
D) Deletes parent

✔ Correct Answer: B

Reason: super refers to parent class, used to call parent constructor (super()) or access parent methods/fields (super.method()).

Tag: Normal

---

### Question 311
Domain: Programming
Topic: Code Analysis
Subtopic: Constructor Chaining
Difficulty: Hard

Question: What is the output?
```java
class Parent {
    Parent() { System.out.print("A"); }
}
class Child extends Parent {
    Child() { System.out.print("B"); }
}
Child c = new Child();
```
A) B
B) AB
C) BA
D) Error

✔ Correct Answer: B

Reason: Parent constructor called first (implicit super()), prints A. Then Child constructor prints B. Output: AB.

Tag: Normal

---

### Question 312
Domain: Programming
Topic: Static Members
Subtopic: Static Methods
Difficulty: Medium

Question: Can static methods access instance variables?
A) Yes
B) No, only static members
C) Sometimes
D) With this keyword

✔ Correct Answer: B

Reason: Static methods belong to class, not instances. Cannot access instance variables directly, only static members. Need object reference for instance access.

Tag: Past Paper

---

### Question 313
Domain: Programming
Topic: Code Analysis
Subtopic: Static Context
Difficulty: Medium

Question: What is the output?
```java
class Test {
    int x = 10;
    static void display() {
        System.out.println(x);
    }
}
```
A) 10
B) 0
C) Compile error
D) Runtime error

✔ Correct Answer: C

Reason: Static method cannot access non-static instance variable x directly. Compile error: non-static variable cannot be referenced from static context.

Tag: Normal

---

### Question 314
Domain: Programming
Topic: Final Keyword
Subtopic: Final Variables
Difficulty: Easy

Question: What does final keyword do for variables?
A) Deletes variable
B) Makes variable constant (cannot be reassigned)
C) Makes variable global
D) Hides variable

✔ Correct Answer: B

Reason: final makes variable constant - value cannot be changed after initialization. Attempting reassignment causes compile error.

Tag: Normal

---

### Question 315
Domain: Programming
Topic: Final Keyword
Subtopic: Final Methods
Difficulty: Medium

Question: What does final keyword do for methods?
A) Deletes method
B) Prevents method from being overridden
C) Makes method static
D) Makes method abstract

✔ Correct Answer: B

Reason: final methods cannot be overridden by subclasses, ensuring method behavior remains unchanged in inheritance hierarchy.

Tag: Normal

---

### Question 316
Domain: Programming
Topic: Final Keyword
Subtopic: Final Classes
Difficulty: Medium

Question: What does final keyword do for classes?
A) Deletes class
B) Prevents class from being inherited
C) Makes class abstract
D) Makes all methods final

✔ Correct Answer: B

Reason: final class cannot be extended/inherited. Used for security, immutability (String class in Java is final).

Tag: Normal

---

### Question 317
Domain: Programming
Topic: Code Analysis
Subtopic: this Keyword
Difficulty: Easy

Question: What does 'this' refer to?
```java
class Person {
    String name;
    Person(String name) {
        this.name = name;
    }
}
```
A) Parameter
B) Current object instance
C) Parent class
D) Static context

✔ Correct Answer: B

Reason: 'this' refers to current object instance. Used to distinguish instance variable from parameter with same name.

Tag: Normal

---

### Question 318
Domain: Programming
Topic: Constructor Overloading
Subtopic: Multiple Constructors
Difficulty: Medium

Question: Can a class have multiple constructors?
A) No
B) Yes, with different parameter lists
C) Only two
D) Only with same parameters

✔ Correct Answer: B

Reason: Constructor overloading allows multiple constructors with different parameter lists, providing flexible object initialization.

Tag: Normal

---

### Question 319
Domain: Programming
Topic: Code Analysis
Subtopic: Default Constructor
Difficulty: Medium

Question: What happens if no constructor is defined?
```java
class Test {
    int x;
}
Test t = new Test();
```
A) Error
B) Compiler provides default no-arg constructor
C) Cannot create object
D) Null object

✔ Correct Answer: B

Reason: If no constructor defined, compiler automatically provides default no-argument constructor. Once you define any constructor, default is not provided.

Tag: Normal

---

### Question 320
Domain: Programming
Topic: Copy Constructor
Subtopic: Object Copying
Difficulty: Hard

Question: What is a copy constructor?
A) Copies class
B) Constructor that creates object by copying another object
C) Duplicate constructor
D) Clone method

✔ Correct Answer: B

Reason: Copy constructor initializes object using another object of same class, creating deep or shallow copy depending on implementation.

Tag: Normal

---

### Question 321
Domain: Programming
Topic: Code Analysis
Subtopic: Shallow vs Deep Copy
Difficulty: Hard

Question: What's the difference between shallow and deep copy?
A) No difference
B) Shallow copies references, deep copies actual objects
C) Deep is faster
D) Shallow is safer

✔ Correct Answer: B

Reason: Shallow copy copies object references (both point to same nested objects). Deep copy recursively copies all objects (independent copies).

Tag: Past Paper

---

### Question 322
Domain: Programming
Topic: Memory Management
Subtopic: Stack vs Heap
Difficulty: Medium

Question: Where are local variables stored?
A) Heap
B) Stack
C) Register
D) Cache

✔ Correct Answer: B

Reason: Local variables and function call information stored on stack (LIFO). Objects and dynamically allocated memory stored on heap.

Tag: Past Paper

---

### Question 323
Domain: Programming
Topic: Memory Management
Subtopic: Garbage Collection
Difficulty: Medium

Question: What is garbage collection?
A) Deleting files
B) Automatic memory management that reclaims unused objects
C) Manual memory deletion
D) Disk cleanup

✔ Correct Answer: B

Reason: Garbage collection automatically identifies and reclaims memory occupied by objects no longer referenced, preventing memory leaks (Java, Python, JavaScript).

Tag: Normal

---

### Question 324
Domain: Programming
Topic: Code Analysis
Subtopic: Memory Leak
Difficulty: Hard

Question: Which scenario can cause memory leak in Java?
A) Creating objects
B) Objects referenced but never used (e.g., in static collection)
C) Using garbage collection
D) Local variables

✔ Correct Answer: B

Reason: Memory leak occurs when objects remain referenced (preventing GC) but are never used, like forgotten entries in static collections.

Tag: Normal

---

### Question 325
Domain: Programming
Topic: Pointers
Subtopic: Pointer Basics
Difficulty: Medium

Question: What is a pointer in C++?
A) Arrow
B) Variable storing memory address
C) Function
D) Data type

✔ Correct Answer: B

Reason: Pointer is variable that stores memory address of another variable. Declared with * (int *ptr), dereferenced with *.

Tag: Past Paper

---

### Question 326
Domain: Programming
Topic: Code Analysis
Subtopic: Pointer Dereferencing
Difficulty: Hard

Question: What is the output?
```cpp
int x = 10;
int *ptr = &x;
cout << *ptr;
```
A) Address of x
B) 10
C) Address of ptr
D) Error

✔ Correct Answer: B

Reason: ptr stores address of x (&x). *ptr dereferences pointer, accessing value at that address: 10.

Tag: Normal

---

### Question 327
Domain: Programming
Topic: Pointers
Subtopic: Null Pointer
Difficulty: Easy

Question: What is a null pointer?
A) Deleted pointer
B) Pointer not pointing to any valid memory location
C) Pointer to zero
D) Empty pointer

✔ Correct Answer: B

Reason: Null pointer doesn't point to valid memory (nullptr in C++, NULL in C, None in Python). Dereferencing causes error.

Tag: Normal

---

### Question 328
Domain: Programming
Topic: References
Subtopic: Reference vs Pointer
Difficulty: Hard

Question: What's a key difference between reference and pointer in C++?
A) No difference
B) Reference cannot be null, must be initialized, cannot be reassigned
C) Pointer is faster
D) Reference uses more memory

✔ Correct Answer: B

Reason: Reference must be initialized, cannot be null or reassigned. Pointer can be null, reassigned, requires dereferencing (*).

Tag: Normal

---

### Question 329
Domain: Programming
Topic: Code Analysis
Subtopic: Pass by Reference
Difficulty: Medium

Question: What is the output?
```cpp
void modify(int &x) {
    x = 20;
}
int main() {
    int a = 10;
    modify(a);
    cout << a;
}
```
A) 10
B) 20
C) 0
D) Error

✔ Correct Answer: B

Reason: Pass by reference (&x) allows function to modify original variable. a is changed to 20.

Tag: Normal

---

### Question 330
Domain: Programming
Topic: Dynamic Memory
Subtopic: new and delete
Difficulty: Medium

Question: What does 'new' operator do in C++?
A) Creates variable
B) Allocates memory on heap, returns pointer
C) Deletes memory
D) Creates stack variable

✔ Correct Answer: B

Reason: 'new' allocates memory dynamically on heap, returns pointer to allocated memory. Must use 'delete' to free memory.

Tag: Normal

---

### Question 331
Domain: Programming
Topic: Code Analysis
Subtopic: Memory Allocation
Difficulty: Hard

Question: What is the output?
```cpp
int *arr = new int[5];
arr[0] = 10;
cout << arr[0];
delete[] arr;
```
A) Error
B) 10
C) Garbage value
D) 0

✔ Correct Answer: B

Reason: new int[5] allocates array on heap. arr[0]=10 sets first element. Prints 10. delete[] frees array memory.

Tag: Normal

---

### Question 332
Domain: Programming
Topic: Templates
Subtopic: Function Templates
Difficulty: Hard

Question: What are templates in C++?
A) Design patterns
B: Generic programming feature for type-independent code
C) Class templates only
D) Documentation

✔ Correct Answer: B

Reason: Templates enable generic programming, allowing functions/classes to work with any data type, specified at compile time.

Tag: Normal

---

### Question 333
Domain: Programming
Topic: Code Analysis
Subtopic: Template Function
Difficulty: Hard

Question: What is the output?
```cpp
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}
cout << max(5, 3);
```
A) 3
B) 5
C) Error
D) 0

✔ Correct Answer: B

Reason: Template function max works with any type. max(5, 3) instantiates with int, returns larger value: 5.

Tag: Normal

---

### Question 334
Domain: Programming
Topic: STL
Subtopic: Standard Template Library
Difficulty: Medium

Question: What does STL provide in C++?
A) Only algorithms
B) Collection of template classes and functions (containers, algorithms, iterators)
C) Only containers
D) Graphics library

✔ Correct Answer: B

Reason: STL provides generic containers (vector, map, set), algorithms (sort, find), and iterators for efficient data structure manipulation.

Tag: Normal

---

### Question 335
Domain: Programming
Topic: Code Analysis
Subtopic: Vector Operations
Difficulty: Medium

Question: What is the output?
```cpp
#include <vector>
vector<int> v = {1, 2, 3};
v.push_back(4);
cout << v.size();
```
A) 3
B) 4
C) 5
D) Error

✔ Correct Answer: B

Reason: Vector initialized with 3 elements. push_back(4) adds element. size() returns 4.

Tag: Normal

---

### Question 336
Domain: Programming
Topic: Iterators
Subtopic: Iterator Basics
Difficulty: Medium

Question: What is an iterator?
A) Loop counter
B) Object that points to elements in container
C) Function
D) Array index

✔ Correct Answer: B

Reason: Iterator is object that points to container elements, allowing traversal. Provides uniform interface for different container types.

Tag: Normal

---

### Question 337
Domain: Programming
Topic: Code Analysis
Subtopic: Iterator Usage
Difficulty: Hard

Question: What is the output?
```cpp
vector<int> v = {10, 20, 30};
auto it = v.begin();
cout << *it;
```
A) Address
B) 10
C) 30
D) Error

✔ Correct Answer: B

Reason: begin() returns iterator to first element. *it dereferences iterator, accessing value: 10.

Tag: Normal

---

### Question 338
Domain: Programming
Topic: Design Patterns
Subtopic: Singleton Pattern
Difficulty: Hard

Question: What is Singleton pattern?
A) Single function
B) Ensures class has only one instance with global access
C) Single inheritance
D) One method class

✔ Correct Answer: B

Reason: Singleton restricts class to single instance, provides global access point. Private constructor prevents external instantiation.

Tag: Past Paper

---

### Question 339
Domain: Programming
Topic: Design Patterns
Subtopic: Factory Pattern
Difficulty: Hard

Question: What is Factory pattern?
A) Manufacturing
B) Creates objects without specifying exact class
C) Deletes objects
D) Copies objects

✔ Correct Answer: B

Reason: Factory pattern provides interface for creating objects, letting subclasses decide which class to instantiate, promoting loose coupling.

Tag: Normal

---

### Question 340
Domain: Programming
Topic: Design Patterns
Subtopic: Observer Pattern
Difficulty: Hard

Question: What is Observer pattern?
A) Watches code
B) One-to-many dependency where observers notified of state changes
C) Debugging pattern
D) Testing pattern

✔ Correct Answer: B

Reason: Observer pattern defines one-to-many dependency. When subject's state changes, all observers are automatically notified and updated.

Tag: Normal

---

### Question 341
Domain: Programming
Topic: Code Analysis
Subtopic: Bitwise AND
Difficulty: Medium

Question: What is the output?
```python
print(5 & 3)
```
A) 8
B) 1
C) 15
D) 2

✔ Correct Answer: B

Reason: Bitwise AND: 5 (101) & 3 (011) = 001 = 1. Compares each bit, result bit is 1 only if both bits are 1.

Tag: Normal

---

### Question 342
Domain: Programming
Topic: Bitwise Operators
Subtopic: Bitwise OR
Difficulty: Medium

Question: What is the output?
```python
print(5 | 3)
```
A) 5
B) 7
C) 8
D) 1

✔ Correct Answer: B

Reason: Bitwise OR: 5 (101) | 3 (011) = 111 = 7. Result bit is 1 if either bit is 1.

Tag: Normal

---

### Question 343
Domain: Programming
Topic: Bitwise Operators
Subtopic: Bitwise XOR
Difficulty: Hard

Question: What is the output?
```python
print(5 ^ 3)
```
A) 2
B) 6
C) 7
D) 8

✔ Correct Answer: B

Reason: Bitwise XOR: 5 (101) ^ 3 (011) = 110 = 6. Result bit is 1 if bits are different.

Tag: Normal

---

### Question 344
Domain: Programming
Topic: Bitwise Operators
Subtopic: Left Shift
Difficulty: Medium

Question: What does x << 2 do?
A) Divides by 2
B) Multiplies x by 4 (shifts bits left by 2)
C) Adds 2
D) Subtracts 2

✔ Correct Answer: B

Reason: Left shift << moves bits left, filling with zeros. Each shift multiplies by 2. x << 2 = x * 2² = x * 4.

Tag: Normal

---

### Question 345
Domain: Programming
Topic: Code Analysis
Subtopic: Right Shift
Difficulty: Medium

Question: What is the output?
```python
print(16 >> 2)
```
A) 32
B) 4
C) 8
D) 2

✔ Correct Answer: B

Reason: Right shift >> moves bits right. Each shift divides by 2. 16 >> 2 = 16 / 2² = 16 / 4 = 4.

Tag: Normal

---

### Question 346
Domain: Programming
Topic: Bitwise Operators
Subtopic: Bitwise NOT
Difficulty: Hard

Question: What does bitwise NOT (~) do?
A) Deletes bits
B) Inverts all bits (0→1, 1→0)
C) Shifts bits
D) Adds bits

✔ Correct Answer: B

Reason: Bitwise NOT (~) inverts all bits. ~5 (00000101) = 11111010 (two's complement representation gives negative value).

Tag: Normal

---

### Question 347
Domain: Programming
Topic: Ternary Operator
Subtopic: Conditional Expression
Difficulty: Easy

Question: What is the syntax of ternary operator?
A) if ? then : else
B) condition ? value_if_true : value_if_false
C) condition : value ? value
D) ? condition : value

✔ Correct Answer: B

Reason: Ternary operator: condition ? value_if_true : value_if_false. Compact alternative to if-else for simple conditions.

Tag: Normal

---

### Question 348
Domain: Programming
Topic: Code Analysis
Subtopic: Ternary Operator
Difficulty: Easy

Question: What is the output?
```java
int x = 10;
String result = (x > 5) ? "Big" : "Small";
System.out.println(result);
```
A) 10
B) Big
C) Small
D) true

✔ Correct Answer: B

Reason: Condition x > 5 is true (10 > 5), so ternary returns "Big".

Tag: Normal

---

### Question 349
Domain: Programming
Topic: Switch Statement
Subtopic: Fall-through
Difficulty: Medium

Question: What happens without break in switch case?
A) Error
B) Fall-through to next case
C) Exits switch
D) Repeats case

✔ Correct Answer: B

Reason: Without break, execution falls through to next case. Intentional fall-through useful for multiple cases sharing code, but often unintended bug.

Tag: Normal

---

### Question 350
Domain: Programming
Topic: Code Analysis
Subtopic: Switch Default
Difficulty: Easy

Question: What is the output?
```java
int x = 5;
switch(x) {
    case 1: System.out.print("A"); break;
    case 2: System.out.print("B"); break;
    default: System.out.print("C");
}
```
A) A
B) B
C) C
D) Nothing

✔ Correct Answer: C

Reason: x=5 doesn't match any case. default case executes, prints C.

Tag: Normal

---

### Question 351
Domain: Programming
Topic: Enumerations
Subtopic: Enum Basics
Difficulty: Easy

Question: What is an enum?
A) Number type
B) Special type representing group of named constants
C) Array
D) Function

✔ Correct Answer: B

Reason: Enum (enumeration) defines set of named constants, improving code readability and type safety (enum Color {RED, GREEN, BLUE}).

Tag: Normal

---

### Question 352
Domain: Programming
Topic: Code Analysis
Subtopic: Enum Usage
Difficulty: Medium

Question: What is the output?
```java
enum Day {MONDAY, TUESDAY, WEDNESDAY}
Day d = Day.MONDAY;
System.out.println(d);
```
A) 0
B) MONDAY
C) Error
D) null

✔ Correct Answer: B

Reason: Enum constant prints its name. d is Day.MONDAY, prints "MONDAY".

Tag: Normal

---

### Question 353
Domain: Programming
Topic: Type Casting
Subtopic: Implicit Casting
Difficulty: Easy

Question: What is implicit type casting?
A) Manual casting
B) Automatic conversion by compiler (widening)
C) Error casting
D) No casting

✔ Correct Answer: B

Reason: Implicit casting (widening) automatically converts smaller type to larger (int to long, float to double) without data loss.

Tag: Normal

---

### Question 354
Domain: Programming
Topic: Type Casting
Subtopic: Explicit Casting
Difficulty: Medium

Question: When is explicit casting required?
A) Always
B) When narrowing (larger to smaller type)
C) Never
D) Only for strings

✔ Correct Answer: B

Reason: Explicit casting (narrowing) required when converting larger type to smaller (double to int), may lose data, requires (type) syntax.

Tag: Normal

---

### Question 355
Domain: Programming
Topic: Code Analysis
Subtopic: Type Casting
Difficulty: Medium

Question: What is the output?
```java
double d = 9.7;
int i = (int) d;
System.out.println(i);
```
A) 9.7
B) 9
C) 10
D) Error

✔ Correct Answer: B

Reason: Explicit cast (int) truncates decimal part. 9.7 becomes 9 (not rounded, truncated).

Tag: Normal

---

### Question 356
Domain: Programming
Topic: String Formatting
Subtopic: Format Strings
Difficulty: Medium

Question: What is the output?
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```
A) name is age years old
B) Alice is 25 years old
C) Error
D) {name} is {age} years old

✔ Correct Answer: B

Reason: f-string (formatted string literal) evaluates expressions inside {}. Outputs: "Alice is 25 years old".

Tag: Normal

---

### Question 357
Domain: Programming
Topic: String Formatting
Subtopic: Format Method
Difficulty: Easy

Question: What does .format() method do?
A) Formats disk
B) Inserts values into string placeholders
C) Formats code
D) Deletes string

✔ Correct Answer: B

Reason: format() inserts values into string placeholders {}. "Hello {}".format("World") returns "Hello World".

Tag: Normal

---

### Question 358
Domain: Programming
Topic: Code Analysis
Subtopic: String Formatting
Difficulty: Medium

Question: What is the output?
```python
print("{1} {0}".format("World", "Hello"))
```
A) World Hello
B) Hello World
C) 1 0
D) Error

✔ Correct Answer: B

Reason: Positional arguments: {1} refers to second argument "Hello", {0} to first "World". Output: "Hello World".

Tag: Normal

---

### Question 359
Domain: Programming
Topic: List Slicing
Subtopic: Negative Indices
Difficulty: Medium

Question: What is the output?
```python
arr = [0, 1, 2, 3, 4]
print(arr[-2:])
```
A) [0, 1]
B) [3, 4]
C) [4]
D) Error

✔ Correct Answer: B

Reason: Negative index -2 refers to second-last element. arr[-2:] slices from index -2 to end: [3, 4].

Tag: Normal

---

### Question 360
Domain: Programming
Topic: List Slicing
Subtopic: Step Parameter
Difficulty: Hard

Question: What is the output?
```python
arr = [0, 1, 2, 3, 4, 5]
print(arr[::2])
```
A) [0, 1, 2]
B) [0, 2, 4]
C) [1, 3, 5]
D) Error

✔ Correct Answer: B

Reason: Slice [::2] means start to end with step 2. Takes every second element: [0, 2, 4].

Tag: Normal

---

### Question 361
Domain: Programming
Topic: Code Analysis
Subtopic: Reverse Slice
Difficulty: Hard

Question: What is the output?
```python
arr = [1, 2, 3, 4]
print(arr[::-1])
```
A) [1, 2, 3, 4]
B) [4, 3, 2, 1]
C) [4]
D) Error

✔ Correct Answer: B

Reason: Slice [::-1] with negative step reverses sequence. Returns [4, 3, 2, 1].

Tag: Normal

---

### Question 362
Domain: Programming
Topic: Modules
Subtopic: Import Statement
Difficulty: Easy

Question: What does 'import math' do in Python?
A) Imports all modules
B) Imports math module for use
C) Deletes math
D) Creates math

✔ Correct Answer: B

Reason: import statement loads module, making its functions/classes available. Access with module.function (math.sqrt()).

Tag: Normal

---

### Question 363
Domain: Programming
Topic: Modules
Subtopic: from Import
Difficulty: Medium

Question: What's the difference between 'import math' and 'from math import sqrt'?
A) No difference
B) First imports entire module, second imports specific function
C) Second is slower
D) First is deprecated

✔ Correct Answer: B

Reason: 'import math' imports module (use math.sqrt()). 'from math import sqrt' imports specific function (use sqrt() directly).

Tag: Normal

---

### Question 364
Domain: Programming
Topic: Code Analysis
Subtopic: Import Alias
Difficulty: Easy

Question: What is the output?
```python
import numpy as np
arr = np.array([1, 2, 3])
print(type(arr).__name__)
```
A) list
B) ndarray
C) numpy
D) array

✔ Correct Answer: B

Reason: 'as np' creates alias. np.array() creates numpy ndarray. type().__name__ returns class name: "ndarray".

Tag: Normal

---

### Question 365
Domain: Programming
Topic: Packages
Subtopic: __init__.py
Difficulty: Medium

Question: What is the purpose of __init__.py?
A) Initializes variables
B) Marks directory as Python package
C) Main file
D) Configuration file

✔ Correct Answer: B

Reason: __init__.py marks directory as Python package, allowing imports. Can be empty or contain package initialization code.

Tag: Normal

---

### Question 366
Domain: Programming
Topic: Virtual Environments
Subtopic: venv Purpose
Difficulty: Easy

Question: Why use virtual environments?
A) Virtual machines
B) Isolate project dependencies from system Python
C) Faster execution
D) Cloud deployment

✔ Correct Answer: B

Reason: Virtual environments create isolated Python environments with separate dependencies, preventing conflicts between projects.

Tag: Normal

---

### Question 367
Domain: Programming
Topic: Package Management
Subtopic: pip
Difficulty: Easy

Question: What is pip?
A) Python interpreter
B) Package installer for Python
C) IDE
D) Compiler

✔ Correct Answer: B

Reason: pip is Python's package installer, used to install/manage packages from PyPI (Python Package Index).

Tag: Normal

---

### Question 368
Domain: Programming
Topic: Code Analysis
Subtopic: List Multiplication
Difficulty: Medium

Question: What is the output?
```python
arr = [1, 2] * 3
print(arr)
```
A) [3, 6]
B) [1, 2, 1, 2, 1, 2]
C) [1, 2, 3]
D) Error

✔ Correct Answer: B

Reason: List multiplication repeats list. [1, 2] * 3 creates [1, 2, 1, 2, 1, 2].

Tag: Normal

---

### Question 369
Domain: Programming
Topic: Tuple Operations
Subtopic: Tuple Concatenation
Difficulty: Easy

Question: Can tuples be concatenated?
A) No, immutable
B) Yes, creates new tuple
C) Only with lists
D) Requires special method

✔ Correct Answer: B

Reason: Tuples are immutable but can be concatenated with + operator, creating new tuple. (1, 2) + (3, 4) = (1, 2, 3, 4).

Tag: Normal

---

### Question 370
Domain: Programming
Topic: Code Analysis
Subtopic: Tuple Methods
Difficulty: Easy

Question: What is the output?
```python
t = (1, 2, 2, 3, 2)
print(t.count(2))
```
A) 1
B) 3
C) 2
D) 5

✔ Correct Answer: B

Reason: count() returns number of occurrences. 2 appears 3 times in tuple.

Tag: Normal

---

### Question 371
Domain: Programming
Topic: Set Operations
Subtopic: Symmetric Difference
Difficulty: Hard

Question: What does set1.symmetric_difference(set2) return?
A) Common elements
B) Elements in either set but not both
C) All elements
D) Empty set

✔ Correct Answer: B

Reason: Symmetric difference returns elements in either set but not in intersection. {1,2,3} ^ {2,3,4} = {1,4}.

Tag: Normal

---

### Question 372
Domain: Programming
Topic: Code Analysis
Subtopic: Set Subset
Difficulty: Medium

Question: What is the output?
```python
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))
```
A) False
B) True
C) {1, 2}
D) Error

✔ Correct Answer: B

Reason: issubset() checks if all elements of set1 are in set2. {1, 2} is subset of {1, 2, 3, 4}, returns True.

Tag: Normal

---

### Question 373
Domain: Programming
Topic: Dictionary Operations
Subtopic: Dict Merge
Difficulty: Medium

Question: What is the output in Python 3.9+?
```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = d1 | d2
print(d3)
```
A) {'a': 1, 'b': 2, 'c': 4}
B) {'a': 1, 'b': 3, 'c': 4}
C) Error
D) {'b': 3}

✔ Correct Answer: B

Reason: | operator (Python 3.9+) merges dictionaries. d2 values override d1 for common keys. Result: {'a': 1, 'b': 3, 'c': 4}.

Tag: Normal

---

### Question 374
Domain: Programming
Topic: Comprehensions
Subtopic: Nested Comprehension
Difficulty: Hard

Question: What is the output?
```python
matrix = [[j for j in range(3)] for i in range(2)]
print(matrix)
```
A) [0, 1, 2, 0, 1, 2]
B) [[0, 1, 2], [0, 1, 2]]
C) [[0, 0], [1, 1], [2, 2]]
D) Error

✔ Correct Answer: B

Reason: Nested comprehension creates 2D list. Outer loop runs 2 times, each creates inner list [0, 1, 2]. Result: [[0, 1, 2], [0, 1, 2]].

Tag: Normal

---

### Question 375
Domain: Programming
Topic: Code Analysis
Subtopic: Enumerate Function
Difficulty: Medium

Question: What is the output?
```python
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(i, val, end=' ')
```
A) 0 a 1 b 2 c
B) 1 a 2 b 3 c
C) a b c
D) Error

✔ Correct Answer: B

Reason: enumerate() with start=1 begins counting from 1. Outputs: 1 a 2 b 3 c.

Tag: Normal

---

### Question 376
Domain: Programming
Topic: Zip Function
Subtopic: Parallel Iteration
Difficulty: Medium

Question: What does zip() function do?
A) Compresses files
B) Combines multiple iterables into tuples
C) Zips arrays
D) Sorts lists

✔ Correct Answer: B

Reason: zip() pairs elements from multiple iterables into tuples. zip([1,2], ['a','b']) yields (1,'a'), (2,'b').

Tag: Normal

---

### Question 377
Domain: Programming
Topic: Code Analysis
Subtopic: Zip Example
Difficulty: Medium

Question: What is the output?
```python
names = ['Alice', 'Bob']
ages = [25, 30]
result = list(zip(names, ages))
print(result)
```
A) ['Alice', 'Bob', 25, 30]
B) [('Alice', 25), ('Bob', 30)]
C) {'Alice': 25, 'Bob': 30}
D) Error

✔ Correct Answer: B

Reason: zip() pairs corresponding elements. Creates list of tuples: [('Alice', 25), ('Bob', 30)].

Tag: Normal

---

### Question 378
Domain: Programming
Topic: Map Function
Subtopic: Transformation
Difficulty: Easy

Question: What does map() function do?
A) Creates map
B) Applies function to each element in iterable
C) Filters elements
D) Sorts elements

✔ Correct Answer: B

Reason: map() applies function to each element, returning iterator of results. map(lambda x: x*2, [1,2,3]) yields 2, 4, 6.

Tag: Normal

---

### Question 379
Domain: Programming
Topic: Code Analysis
Subtopic: Map with Lambda
Difficulty: Medium

Question: What is the output?
```python
result = list(map(lambda x: x**2, [1, 2, 3, 4]))
print(result)
```
A) [1, 2, 3, 4]
B) [1, 4, 9, 16]
C) [2, 4, 6, 8]
D) Error

✔ Correct Answer: B

Reason: map() applies lambda (squares each element) to list. 1²=1, 2²=4, 3²=9, 4²=16. Result: [1, 4, 9, 16].

Tag: Normal

---

### Question 380
Domain: Programming
Topic: Filter Function
Subtopic: Filtering
Difficulty: Easy

Question: What does filter() function do?
A) Filters water
B) Returns elements for which function returns True
C) Removes all elements
D) Sorts elements

✔ Correct Answer: B

Reason: filter() returns iterator of elements where function returns True. filter(lambda x: x>2, [1,2,3,4]) yields 3, 4.

Tag: Normal

---

### Question 381
Domain: Programming
Topic: Code Analysis
Subtopic: Filter Example
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

Reason: filter() keeps elements where lambda returns True. Even numbers (x % 2 == 0): [2, 4, 6].

Tag: Normal

---

### Question 382
Domain: Programming
Topic: Reduce Function
Subtopic: Accumulation
Difficulty: Hard

Question: What does reduce() function do?
A) Reduces size
B) Applies function cumulatively to reduce iterable to single value
C) Filters elements
D) Sorts elements

✔ Correct Answer: B

Reason: reduce() (from functools) applies function cumulatively. reduce(lambda x,y: x+y, [1,2,3,4]) computes ((1+2)+3)+4=10.

Tag: Normal

---

### Question 383
Domain: Programming
Topic: Code Analysis
Subtopic: Reduce Example
Difficulty: Hard

Question: What is the output?
```python
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)
```
A) 10
B) 24
C) 4
D) Error

✔ Correct Answer: B

Reason: reduce() multiplies cumulatively: ((1*2)*3)*4 = 24. Computes product of all elements.

Tag: Normal

---

### Question 384
Domain: Programming
Topic: Any and All
Subtopic: Boolean Aggregation
Difficulty: Medium

Question: What does any() function return?
A) Any element
B) True if at least one element is truthy
C) All elements
D) First element

✔ Correct Answer: B

Reason: any() returns True if at least one element is truthy, False if all are falsy. all() requires all elements to be truthy.

Tag: Normal

---

### Question 385
Domain: Programming
Topic: Code Analysis
Subtopic: All Function
Difficulty: Medium

Question: What is the output?
```python
print(all([True, True, False]))
print(any([True, True, False]))
```
A) True True
B) False True
C) False False
D) True False

✔ Correct Answer: B

Reason: all() returns False (not all are True). any() returns True (at least one is True).

Tag: Normal

---

### Question 386
Domain: Programming
Topic: Sorting
Subtopic: Custom Sort Key
Difficulty: Hard

Question: What is the output?
```python
words = ['apple', 'pie', 'zoo', 'a']
words.sort(key=len)
print(words)
```
A) ['a', 'apple', 'pie', 'zoo']
B) ['a', 'pie', 'zoo', 'apple']
C) ['apple', 'pie', 'zoo', 'a']
D) Error

✔ Correct Answer: B

Reason: sort(key=len) sorts by string length. Lengths: a(1), pie(3), zoo(3), apple(5). Result: ['a', 'pie', 'zoo', 'apple'].

Tag: Normal

---

### Question 387
Domain: Programming
Topic: Sorting
Subtopic: Reverse Sort
Difficulty: Easy

Question: How do you sort in descending order?
A) sort(desc=True)
B) sort(reverse=True)
C) sort(-1)
D) Cannot sort descending

✔ Correct Answer: B

Reason: sort(reverse=True) or sorted(list, reverse=True) sorts in descending order. Default is ascending.

Tag: Normal

---

### Question 388
Domain: Programming
Topic: Code Analysis
Subtopic: Lambda Sort Key
Difficulty: Hard

Question: What is the output?
```python
data = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
data.sort(key=lambda x: x[1])
print(data[0][0])
```
A) Alice
B) Bob
C) Charlie
D) 20

✔ Correct Answer: B

Reason: sort(key=lambda x: x[1]) sorts by second element (age). Youngest is Bob (20). data[0][0] is first person's name: "Bob".

Tag: Normal

---

### Question 389
Domain: Programming
Topic: Exception Types
Subtopic: Common Exceptions
Difficulty: Easy

Question: Which exception occurs when dividing by zero?
A) ValueError
B) ZeroDivisionError
C) ArithmeticError
D) MathError

✔ Correct Answer: B

Reason: ZeroDivisionError raised when dividing by zero. ValueError for invalid values, TypeError for wrong types.

Tag: Normal

---

### Question 390
Domain: Programming
Topic: Exception Types
Subtopic: IndexError
Difficulty: Easy

Question: When does IndexError occur?
A) Wrong type
B) Accessing index outside list bounds
C) Division by zero
D) Null value

✔ Correct Answer: B

Reason: IndexError raised when accessing list/array index that doesn't exist. arr[10] on 5-element list raises IndexError.

Tag: Normal

---

### Question 391
Domain: Programming
Topic: Code Analysis
Subtopic: KeyError
Difficulty: Medium

Question: What exception occurs?
```python
d = {'a': 1, 'b': 2}
print(d['c'])
```
A) ValueError
B) KeyError
C) IndexError
D) AttributeError

✔ Correct Answer: B

Reason: KeyError raised when accessing non-existent dictionary key. Use d.get('c') to avoid error (returns None).

Tag: Normal

---

### Question 392
Domain: Programming
Topic: Exception Types
Subtopic: AttributeError
Difficulty: Medium

Question: When does AttributeError occur?
A) Wrong attribute type
B) Accessing non-existent attribute or method
C) Missing import
D) Syntax error

✔ Correct Answer: B

Reason: AttributeError raised when accessing attribute/method that doesn't exist on object. obj.nonexistent_method() raises AttributeError.

Tag: Normal

---

### Question 393
Domain: Programming
Topic: Code Analysis
Subtopic: TypeError
Difficulty: Medium

Question: What exception occurs?
```python
result = "5" + 5
```
A) ValueError
B) TypeError
C) SyntaxError
D) No error

✔ Correct Answer: B

Reason: TypeError raised when operation applied to inappropriate type. Cannot concatenate string and integer in Python (JavaScript allows with coercion).

Tag: Normal

---

### Question 394
Domain: Programming
Topic: Assert Statement
Subtopic: Assertions
Difficulty: Medium

Question: What does assert statement do?
A) Assigns value
B) Tests condition, raises AssertionError if False
C) Asserts type
D) Prints message

✔ Correct Answer: B

Reason: assert tests condition, raises AssertionError if False. Used for debugging and testing assumptions. assert x > 0, "x must be positive".

Tag: Normal

---

### Question 395
Domain: Programming
Topic: Code Analysis
Subtopic: Assert Example
Difficulty: Medium

Question: What happens?
```python
x = -5
assert x > 0, "x must be positive"
```
A) Nothing
B) AssertionError with message
C) ValueError
D) Prints message

✔ Correct Answer: B

Reason: Condition x > 0 is False (-5 not > 0). assert raises AssertionError with message "x must be positive".

Tag: Normal

---

### Question 396
Domain: Programming
Topic: Type Hints
Subtopic: Function Annotations
Difficulty: Medium

Question: What are type hints in Python?
A) Required types
B) Optional annotations indicating expected types
C) Type enforcement
D) Comments

✔ Correct Answer: B

Reason: Type hints are optional annotations (def func(x: int) -> str:) indicating expected types, improving code clarity and enabling static analysis.

Tag: Normal

---

### Question 397
Domain: Programming
Topic: Code Analysis
Subtopic: Type Hints
Difficulty: Medium

Question: What is the purpose of this code?
```python
def add(a: int, b: int) -> int:
    return a + b
```
A) Enforces types at runtime
B) Documents expected types, enables static type checking
C) Required syntax
D) Slows execution

✔ Correct Answer: B

Reason: Type hints document expected types (parameters: int, return: int), enable tools like mypy for static checking, but don't enforce at runtime.

Tag: Normal

---

### Question 398
Domain: Programming
Topic: Docstrings
Subtopic: Documentation
Difficulty: Easy

Question: What is a docstring?
A) String variable
B) String literal documenting module/class/function
C) Debug string
D) Error message

✔ Correct Answer: B

Reason: Docstring is string literal (triple quotes) at beginning of module/class/function, documenting purpose and usage. Accessible via __doc__.

Tag: Normal

---

### Question 399
Domain: Programming
Topic: Code Analysis
Subtopic: Docstring Access
Difficulty: Medium

Question: What is the output?
```python
def greet():
    """Says hello"""
    print("Hello")

print(greet.__doc__)
```
A) None
B) Says hello
C) Hello
D) Error

✔ Correct Answer: B

Reason: __doc__ attribute contains function's docstring. Prints "Says hello".

Tag: Normal

---

### Question 400
Domain: Programming
Topic: Comments
Subtopic: Multi-line Comments
Difficulty: Easy

Question: How do you write multi-line comments in Python?
A) // comment
B) """ comment """ or ''' comment '''
C) /* comment */
D) # on each line

✔ Correct Answer: B

Reason: Triple quotes (""" or ''') create multi-line strings, used as comments. # creates single-line comments. /* */ is C/Java syntax.

Tag: Normal

---

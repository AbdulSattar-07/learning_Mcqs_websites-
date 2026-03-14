# Programming - MCQ Batch 10
## Questions 901-1000

---

### Question 901
Domain: Programming
Topic: Code Analysis
Subtopic: Composite Example
Difficulty: Hard

Question: What does this pattern enable?
```python
class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def operation(self):
        results = [child.operation() for child in self.children]
        return f"Composite({', '.join(results)})"
```
A) Nothing
B) Uniform treatment of individual and composite objects
C) Faster operations
D) Error

✔ Correct Answer: B

Reason: Both Leaf and Composite implement operation(). Client treats them uniformly. Composite delegates to children. Tree structure.

Tag: Normal

---

### Question 902
Domain: Programming
Topic: Design Patterns
Subtopic: Flyweight Pattern
Difficulty: Hard

Question: What is Flyweight pattern?
A) Lightweight objects
B) Shares common state to support many objects efficiently
C) Flying objects
D) Weight calculation

✔ Correct Answer: B

Reason: Flyweight minimizes memory by sharing common state (intrinsic) among objects. Extrinsic state passed to methods. Used for many similar objects.

Tag: Normal

---

### Question 903
Domain: Programming
Topic: Design Patterns
Subtopic: Bridge Pattern
Difficulty: Hard

Question: What is Bridge pattern?
A) Connects classes
B) Separates abstraction from implementation
C: Bridge between objects
D) Connection pattern

✔ Correct Answer: B

Reason: Bridge decouples abstraction from implementation, allowing independent variation. Composition over inheritance. Abstraction contains reference to implementation.

Tag: Normal

---

### Question 904
Domain: Programming
Topic: Code Analysis
Subtopic: Method Chaining Pattern
Difficulty: Medium

Question: What pattern does this demonstrate?
```python
class Builder:
    def __init__(self):
        self.value = ""
    
    def add_a(self):
        self.value += "A"
        return self
    
    def add_b(self):
        self.value += "B"
        return self
```
A) Chain pattern
B) Fluent interface (method chaining)
C) Builder only
D) Decorator

✔ Correct Answer: B

Reason: Fluent interface returns self from methods, enabling chaining: builder.add_a().add_b(). Improves readability.

Tag: Normal

---

### Question 905
Domain: Programming
Topic: Null Object Pattern
Subtopic: Null Handling
Difficulty: Hard

Question: What is Null Object pattern?
A) Null pointer
B) Object with neutral behavior instead of null checks
C) Empty object
D) Error object

✔ Correct Answer: B

Reason: Null Object provides default do-nothing behavior, eliminating null checks. Implements same interface as real object.

Tag: Normal

---

### Question 906
Domain: Programming
Topic: Code Analysis
Subtopic: Null Object Example
Difficulty: Hard

Question: What is the output?
```python
class Logger:
    def log(self, msg):
        print(msg)

class NullLogger:
    def log(self, msg):
        pass  # Do nothing

logger = NullLogger()
logger.log("Test")
```
A) Test
B) Nothing (no output)
C) Error
D) None

✔ Correct Answer: B

Reason: NullLogger implements log() but does nothing. No output. Avoids null checks, provides safe default behavior.

Tag: Normal

---

### Question 907
Domain: Programming
Topic: Dependency Injection
Subtopic: DI Basics
Difficulty: Hard

Question: What is dependency injection?
A) Injecting code
B) Providing dependencies from outside rather than creating internally
C) Dependency management
D) Injection attack

✔ Correct Answer: B

Reason: DI provides dependencies (objects) from outside (constructor, setter, interface). Reduces coupling, improves testability (can inject mocks).

Tag: Normal

---

### Question 908
Domain: Programming
Topic: Code Analysis
Subtopic: Constructor Injection
Difficulty: Hard

Question: What DI type is this?
```python
class Service:
    def __init__(self, repository):
        self.repository = repository
    
    def get_data(self):
        return self.repository.fetch()

# Usage
repo = Repository()
service = Service(repo)
```
A) Setter injection
B) Constructor injection
C) Interface injection
D) No injection

✔ Correct Answer: B

Reason: Dependency (repository) injected through constructor. Service doesn't create repository, receives it. Enables testing with mock repository.

Tag: Normal

---

### Question 909
Domain: Programming
Topic: Inversion of Control
Subtopic: IoC Container
Difficulty: Hard

Question: What is Inversion of Control?
A) Inverted code
B) Framework controls flow, calls your code (Hollywood Principle)
C) Control flow
D) Reverse logic

✔ Correct Answer: B

Reason: IoC: framework controls flow, calls your code ("Don't call us, we'll call you"). Opposite of traditional flow. DI is IoC implementation.

Tag: Normal

---

### Question 910
Domain: Programming
Topic: Code Quality
Subtopic: Code Smells
Difficulty: Medium

Question: What is a code smell?
A) Bad code
B) Indicator of potential problem in code
C) Syntax error
D) Bug

✔ Correct Answer: B

Reason: Code smell suggests deeper problem (long methods, duplicate code, large classes). Not bug, but indicates need for refactoring.

Tag: Normal

---

### Question 911
Domain: Programming
Topic: Refactoring
Subtopic: Extract Method
Difficulty: Medium

Question: What is Extract Method refactoring?
A) Extracts data
B) Moves code fragment into separate method
C) Deletes method
D) Copies method

✔ Correct Answer: B

Reason: Extract Method moves code fragment into new method with descriptive name. Reduces duplication, improves readability, enables reuse.

Tag: Normal

---

### Question 912
Domain: Programming
Topic: Code Analysis
Subtopic: Long Method Smell
Difficulty: Medium

Question: What indicates long method smell?
A) Method name length
B) Method doing too much, hard to understand
C) Many parameters
D) Long execution time

✔ Correct Answer: B

Reason: Long method has too many responsibilities, hard to understand/maintain. Refactor by extracting smaller methods with single responsibilities.

Tag: Normal

---

### Question 913
Domain: Programming
Topic: Refactoring
Subtopic: Rename Variable
Difficulty: Easy

Question: Why rename variables?
A) Required
B) Improve code clarity and readability
C) Faster execution
D) No benefit

✔ Correct Answer: B

Reason: Descriptive names improve code readability and maintainability. 'x' → 'user_count' makes purpose clear. Use IDE refactoring tools.

Tag: Normal

---

### Question 914
Domain: Programming
Topic: Code Analysis
Subtopic: Magic Numbers
Difficulty: Medium

Question: What is magic number smell?
A) Random numbers
B) Unexplained numeric literals in code
C) Lucky numbers
D) Constants

✔ Correct Answer: B

Reason: Magic numbers are unexplained literals (if x > 86400). Replace with named constants (SECONDS_PER_DAY = 86400) for clarity.

Tag: Normal

---

### Question 915
Domain: Programming
Topic: Refactoring
Subtopic: Replace Conditional with Polymorphism
Difficulty: Hard

Question: What does this refactoring do?
A) Removes conditions
B) Replaces type-checking conditionals with polymorphic method calls
C) Adds conditions
D) Optimizes conditions

✔ Correct Answer: B

Reason: Instead of if-else checking type, use polymorphism. Each type has own method implementation. More extensible, follows OCP.

Tag: Normal

---

### Question 916
Domain: Programming
Topic: Code Analysis
Subtopic: Duplicate Code
Difficulty: Easy

Question: What is duplicate code smell?
A) Copied files
B) Same or similar code in multiple places
C) Repeated execution
D) Backup code

✔ Correct Answer: B

Reason: Duplicate code violates DRY (Don't Repeat Yourself). Changes needed in multiple places. Refactor by extracting common code.

Tag: Normal

---

### Question 917
Domain: Programming
Topic: DRY Principle
Subtopic: Don't Repeat Yourself
Difficulty: Easy

Question: What is DRY principle?
A) Dry code
B) Every piece of knowledge should have single representation
C) No comments
D) Short code

✔ Correct Answer: B

Reason: DRY: avoid duplication, single source of truth. Changes made once. Opposite: WET (Write Everything Twice).

Tag: Normal

---

### Question 918
Domain: Programming
Topic: KISS Principle
Subtopic: Keep It Simple
Difficulty: Easy

Question: What is KISS principle?
A) Keep code short
B) Keep it simple, avoid unnecessary complexity
C) Kiss objects
D) Compact code

✔ Correct Answer: B

Reason: KISS: simplicity should be key goal. Avoid over-engineering. Simple solutions easier to understand, maintain, debug.

Tag: Normal

---

### Question 919
Domain: Programming
Topic: YAGNI Principle
Subtopic: You Aren't Gonna Need It
Difficulty: Medium

Question: What is YAGNI principle?
A) You need it
B) Don't add functionality until needed
C) Add everything
D) Future-proof code

✔ Correct Answer: B

Reason: YAGNI: don't implement features speculatively. Add functionality when actually needed. Reduces complexity, wasted effort.

Tag: Normal

---

### Question 920
Domain: Programming
Topic: Code Analysis
Subtopic: Premature Optimization
Difficulty: Medium

Question: What did Donald Knuth say about optimization?
A) Always optimize
B) Premature optimization is root of all evil
C) Never optimize
D) Optimize everything

✔ Correct Answer: B

Reason: "Premature optimization is root of all evil." Optimize after profiling, not based on assumptions. Focus on correctness first.

Tag: Normal

---

### Question 921
Domain: Programming
Topic: Testing
Subtopic: Test-Driven Development
Difficulty: Medium

Question: What is TDD cycle?
A) Test, Debug, Deploy
B) Red (failing test), Green (make it pass), Refactor
C) Test, Develop, Done
D) Write code, test, fix

✔ Correct Answer: B

Reason: TDD: write failing test (Red), write minimal code to pass (Green), refactor (improve design). Repeat. Tests drive design.

Tag: Normal

---

### Question 922
Domain: Programming
Topic: Testing
Subtopic: Unit vs Integration Tests
Difficulty: Medium

Question: What's the difference between unit and integration tests?
A) No difference
B) Unit tests single component, integration tests multiple components
C) Integration is faster
D) Unit tests everything

✔ Correct Answer: B

Reason: Unit tests test single component in isolation (with mocks). Integration tests test multiple components working together.

Tag: Normal

---

### Question 923
Domain: Programming
Topic: Code Analysis
Subtopic: Test Coverage
Difficulty: Medium

Question: What is code coverage?
A) Code amount
B) Percentage of code executed by tests
C) Test count
D) Code quality

✔ Correct Answer: B

Reason: Code coverage measures percentage of code (lines, branches, functions) executed by tests. High coverage doesn't guarantee quality but helps find untested code.

Tag: Normal

---

### Question 924
Domain: Programming
Topic: Testing
Subtopic: Mocking
Difficulty: Hard

Question: Why mock dependencies in unit tests?
A) Mock data
B) Isolate unit under test, control behavior, avoid external dependencies
C) Fake tests
D) Speed only

✔ Correct Answer: B

Reason: Mocking isolates unit, controls dependency behavior, avoids external systems (databases, APIs). Makes tests fast, reliable, focused.

Tag: Normal

---

### Question 925
Domain: Programming
Topic: Code Analysis
Subtopic: Test Doubles
Difficulty: Hard

Question: What's the difference between mock and stub?
A) No difference
B) Mock verifies interactions, stub provides canned responses
C) Stub is faster
D) Mock is deprecated

✔ Correct Answer: B

Reason: Stub provides predetermined responses. Mock verifies method calls, arguments, call count. Both are test doubles.

Tag: Normal

---

### Question 926
Domain: Programming
Topic: Version Control
Subtopic: Git Basics
Difficulty: Easy

Question: What does git commit do?
A) Commits crime
B) Saves changes to local repository
C) Uploads to server
D) Deletes changes

✔ Correct Answer: B

Reason: git commit saves staged changes to local repository with message. git push uploads commits to remote repository.

Tag: Normal

---

### Question 927
Domain: Programming
Topic: Code Analysis
Subtopic: Git Workflow
Difficulty: Medium

Question: What is typical Git workflow?
A) commit, add, push
B) add (stage), commit (save locally), push (upload)
C) push, commit, add
D) commit only

✔ Correct Answer: B

Reason: git add stages changes, git commit saves to local repo, git push uploads to remote. Pull before push to sync.

Tag: Normal

---

### Question 928
Domain: Programming
Topic: Version Control
Subtopic: Git Branches
Difficulty: Easy

Question: What is a Git branch?
A) Tree branch
B) Independent line of development
C) Code branch
D) Folder

✔ Correct Answer: B

Reason: Branch is pointer to commit, enabling parallel development. Create features in branches, merge to main. Lightweight in Git.

Tag: Normal

---

### Question 929
Domain: Programming
Topic: Code Analysis
Subtopic: Git Merge
Difficulty: Medium

Question: What does git merge do?
A) Merges files
B) Combines changes from different branches
C) Deletes branch
D) Merges commits

✔ Correct Answer: B

Reason: git merge integrates changes from one branch into another. Creates merge commit (or fast-forward). May require resolving conflicts.

Tag: Normal

---

### Question 930
Domain: Programming
Topic: Version Control
Subtopic: Merge Conflicts
Difficulty: Medium

Question: When do merge conflicts occur?
A) Always
B) When same lines modified in different branches
C) Different files
D) Never

✔ Correct Answer: B

Reason: Conflict occurs when same lines modified differently in branches being merged. Git can't auto-resolve, requires manual resolution.

Tag: Normal

---

### Question 931
Domain: Programming
Topic: Code Analysis
Subtopic: Git Rebase
Difficulty: Hard

Question: What's the difference between merge and rebase?
A) No difference
B) Merge creates merge commit, rebase rewrites history linearly
C) Rebase is faster
D) Merge is deprecated

✔ Correct Answer: B

Reason: Merge preserves history with merge commit. Rebase moves commits to new base, creating linear history. Don't rebase public branches.

Tag: Normal

---

### Question 932
Domain: Programming
Topic: Version Control
Subtopic: Git Stash
Difficulty: Medium

Question: What does git stash do?
A) Stashes files
B) Temporarily saves uncommitted changes
C) Deletes changes
D) Commits changes

✔ Correct Answer: B

Reason: git stash saves uncommitted changes temporarily, cleaning working directory. git stash pop restores changes. Useful for switching branches.

Tag: Normal

---

### Question 933
Domain: Programming
Topic: Code Analysis
Subtopic: Git Reset
Difficulty: Hard

Question: What does git reset --hard do?
A) Resets password
B) Discards all changes, resets to specified commit
C) Soft reset
D) Resets branch

✔ Correct Answer: B

Reason: --hard resets HEAD, index, and working directory to commit. Discards all changes. --soft keeps changes staged. --mixed (default) unstages.

Tag: Normal

---

### Question 934
Domain: Programming
Topic: Version Control
Subtopic: Git Revert
Difficulty: Medium

Question: What's the difference between reset and revert?
A) No difference
B) Reset removes commits, revert creates new commit undoing changes
C) Revert is faster
D) Reset is safer

✔ Correct Answer: B

Reason: reset removes commits (rewrites history). revert creates new commit undoing changes (preserves history). Revert safer for public branches.

Tag: Normal

---

### Question 935
Domain: Programming
Topic: Code Analysis
Subtopic: Git Cherry-pick
Difficulty: Hard

Question: What does git cherry-pick do?
A) Picks files
B) Applies specific commit from another branch
C) Picks branch
D) Selects changes

✔ Correct Answer: B

Reason: cherry-pick applies changes from specific commit to current branch. Useful for applying hotfix to multiple branches.

Tag: Normal

---

### Question 936
Domain: Programming
Topic: Code Review
Subtopic: Pull Request
Difficulty: Easy

Question: What is pull request?
A) Pulling code
B) Request to merge changes, enables code review
C) Download request
D) Pull from server

✔ Correct Answer: B

Reason: Pull request (PR) proposes merging changes, enabling team review, discussion, approval before merging. Central to collaborative development.

Tag: Normal

---

### Question 937
Domain: Programming
Topic: Code Analysis
Subtopic: Code Review Benefits
Difficulty: Easy

Question: What is main benefit of code review?
A) Slows development
B) Catches bugs, shares knowledge, improves quality
C) Required only
D) No benefit

✔ Correct Answer: B

Reason: Code review catches bugs early, shares knowledge, ensures standards, improves code quality. Collaborative learning opportunity.

Tag: Normal

---

### Question 938
Domain: Programming
Topic: Continuous Integration
Subtopic: CI Basics
Difficulty: Medium

Question: What is Continuous Integration?
A) Continuous coding
B) Automatically building and testing code on each commit
C) Integration testing
D) Continuous deployment

✔ Correct Answer: B

Reason: CI automatically builds and tests code when changes pushed. Catches integration issues early. Tools: Jenkins, GitHub Actions, GitLab CI.

Tag: Normal

---

### Question 939
Domain: Programming
Topic: Code Analysis
Subtopic: CI Pipeline
Difficulty: Medium

Question: What is typical CI pipeline?
A) Code only
B) Build, test, lint, deploy
C) Test only
D) Deploy only

✔ Correct Answer: B

Reason: CI pipeline: checkout code, install dependencies, build, run tests, lint, deploy (if tests pass). Automated quality checks.

Tag: Normal

---

### Question 940
Domain: Programming
Topic: Linting
Subtopic: Code Linting
Difficulty: Easy

Question: What is a linter?
A) Lint remover
B) Tool analyzing code for errors and style issues
C) Compiler
D) Formatter

✔ Correct Answer: B

Reason: Linter analyzes code for potential errors, style violations, suspicious constructs. Examples: pylint, eslint, flake8. Improves code quality.

Tag: Normal

---

### Question 941
Domain: Programming
Topic: Code Analysis
Subtopic: Linting Benefits
Difficulty: Easy

Question: What does linter catch?
A) Bugs only
B) Syntax errors, style issues, potential bugs, unused variables
C) Runtime errors
D) Logic errors only

✔ Correct Answer: B

Reason: Linters catch syntax errors, style violations, unused imports/variables, potential bugs. Don't catch all logic errors or runtime issues.

Tag: Normal

---

### Question 942
Domain: Programming
Topic: Code Formatting
Subtopic: Auto Formatting
Difficulty: Easy

Question: What does code formatter do?
A) Formats disk
B) Automatically formats code to consistent style
C) Formats output
D) Deletes code

✔ Correct Answer: B

Reason: Formatter automatically applies consistent style (indentation, spacing, line length). Examples: black (Python), prettier (JavaScript). Eliminates style debates.

Tag: Normal

---

### Question 943
Domain: Programming
Topic: Code Analysis
Subtopic: PEP 8
Difficulty: Easy

Question: What is PEP 8?
A) Python version
B) Python style guide
C) Python package
D) Python error

✔ Correct Answer: B

Reason: PEP 8 is official Python style guide covering naming, indentation, line length, imports. Tools like flake8 check PEP 8 compliance.

Tag: Normal

---

### Question 944
Domain: Programming
Topic: Documentation
Subtopic: API Documentation
Difficulty: Easy

Question: What should API documentation include?
A) Code only
B) Parameters, return values, exceptions, examples
C) Function names
D) Nothing

✔ Correct Answer: B

Reason: Good API docs describe parameters, return values, exceptions, usage examples. Helps users understand and use API correctly.

Tag: Normal

---

### Question 945
Domain: Programming
Topic: Code Analysis
Subtopic: Docstring Format
Difficulty: Medium

Question: What docstring format is this?
```python
def func(x, y):
    """
    Brief description.
    
    Args:
        x: First parameter
        y: Second parameter
    
    Returns:
        Result value
    """
    pass
```
A) reStructuredText
B) Google style
C) NumPy style
D) Custom

✔ Correct Answer: B

Reason: Google style docstring with Args and Returns sections. Other styles: NumPy (Parameters, Returns), reStructuredText (:param:, :returns:).

Tag: Normal

---

### Question 946
Domain: Programming
Topic: Type Checking
Subtopic: mypy
Difficulty: Medium

Question: What is mypy?
A) My Python
B) Static type checker for Python
C) Python version
D) Package manager

✔ Correct Answer: B

Reason: mypy is static type checker using type hints. Catches type errors before runtime. Optional, gradual typing.

Tag: Normal

---

### Question 947
Domain: Programming
Topic: Code Analysis
Subtopic: Type Checking Benefits
Difficulty: Medium

Question: What does static type checking catch?
A) Runtime errors
B) Type mismatches before execution
C) Logic errors
D) Performance issues

✔ Correct Answer: B

Reason: Static type checking catches type errors at development time, before running code. Doesn't catch logic errors or runtime issues.

Tag: Normal

---

### Question 948
Domain: Programming
Topic: Virtual Environments
Subtopic: requirements.txt
Difficulty: Easy

Question: What is requirements.txt?
A) Requirements document
B) Lists Python package dependencies
C) Configuration file
D) Test requirements

✔ Correct Answer: B

Reason: requirements.txt lists project dependencies with versions. pip install -r requirements.txt installs all. pip freeze > requirements.txt generates it.

Tag: Normal

---

### Question 949
Domain: Programming
Topic: Code Analysis
Subtopic: Package Versioning
Difficulty: Medium

Question: What does package==1.2.3 mean in requirements.txt?
A) Minimum version
B) Exact version 1.2.3
C) Maximum version
D) Any version

✔ Correct Answer: B

Reason: == specifies exact version. >= minimum version, <= maximum, ~= compatible version. Exact version ensures reproducibility.

Tag: Normal

---

### Question 950
Domain: Programming
Topic: Package Management
Subtopic: setup.py
Difficulty: Medium

Question: What is setup.py?
A) Setup script
B) Python package configuration and installation script
C) Configuration file
D) Setup wizard

✔ Correct Answer: B

Reason: setup.py defines package metadata, dependencies, entry points. Used by pip for installation. Modern alternative: pyproject.toml.

Tag: Normal

---

### Question 951
Domain: Programming
Topic: Code Analysis
Subtopic: Entry Points
Difficulty: Medium

Question: What does if __name__ == "__main__": do?
A) Checks name
B) Executes code only when script run directly, not imported
C) Main function
D) Error check

✔ Correct Answer: B

Reason: __name__ is "__main__" when script run directly, module name when imported. Allows module to be both importable and executable.

Tag: Normal

---

### Question 952
Domain: Programming
Topic: Modules
Subtopic: __all__
Difficulty: Medium

Question: What does __all__ define?
A) All variables
B) Public API (what's exported with from module import *)
C) All functions
D) All classes

✔ Correct Answer: B

Reason: __all__ list defines public API. from module import * imports only names in __all__. Doesn't affect direct imports.

Tag: Normal

---

### Question 953
Domain: Programming
Topic: Code Analysis
Subtopic: Module __all__
Difficulty: Medium

Question: What is the output?
```python
# module.py
__all__ = ['public_func']

def public_func():
    return "Public"

def private_func():
    return "Private"

# main.py
from module import *
print(public_func())
print(private_func())  # ?
```
A) Public Private
B) Public then NameError
C) Both errors
D) Private Public

✔ Correct Answer: B

Reason: import * imports only names in __all__. public_func imported, private_func not. Second print raises NameError.

Tag: Normal

---

### Question 954
Domain: Programming
Topic: Import System
Subtopic: Relative Imports
Difficulty: Medium

Question: What does from . import module mean?
A) Current directory
B) Relative import from current package
C) Parent directory
D) Error

✔ Correct Answer: B

Reason: . refers to current package, .. to parent. from . import module imports from current package. Relative imports only work in packages.

Tag: Normal

---

### Question 955
Domain: Programming
Topic: Code Analysis
Subtopic: Circular Imports
Difficulty: Hard

Question: What problem do circular imports cause?
A) Slow imports
B) Import deadlock or incomplete module initialization
C) No problem
D) Syntax error

✔ Correct Answer: B

Reason: Circular imports (A imports B, B imports A) can cause import errors or incomplete initialization. Refactor to break cycle or use local imports.

Tag: Normal

---

### Question 956
Domain: Programming
Topic: Performance
Subtopic: Big O Notation
Difficulty: Easy

Question: What does O(1) mean?
A) One operation
B) Constant time regardless of input size
C) One second
D) Single loop

✔ Correct Answer: B

Reason: O(1) means constant time, independent of input size. Array access, hash table lookup (average) are O(1).

Tag: Past Paper

---

### Question 957
Domain: Programming
Topic: Code Analysis
Subtopic: Complexity Comparison
Difficulty: Medium

Question: Which is fastest for large n?
A) O(n²)
B) O(n log n)
C) O(2ⁿ)
D) O(n!)

✔ Correct Answer: B

Reason: Growth rates: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!). O(n log n) fastest among options.

Tag: Normal

---

### Question 958
Domain: Programming
Topic: Complexity Analysis
Subtopic: Logarithmic Time
Difficulty: Medium

Question: What operations are O(log n)?
A) Linear search
B) Binary search, balanced tree operations
C) Array access
D) Sorting

✔ Correct Answer: B

Reason: O(log n): binary search, balanced BST/AVL operations. Halve problem size each step. Efficient for large datasets.

Tag: Past Paper

---

### Question 959
Domain: Programming
Topic: Code Analysis
Subtopic: Nested Loop Complexity
Difficulty: Medium

Question: What is time complexity?
```python
for i in range(n):
    for j in range(i):
        print(i, j)
```
A) O(n)
B) O(n²)
C) O(n log n)
D) O(2n)

✔ Correct Answer: B

Reason: Inner loop runs 0, 1, 2, ..., n-1 times. Total: 0+1+2+...+(n-1) = n(n-1)/2 = O(n²).

Tag: Normal

---

### Question 960
Domain: Programming
Topic: Complexity Analysis
Subtopic: Exponential Time
Difficulty: Hard

Question: What problems have O(2ⁿ) complexity?
A) Sorting
B) Naive recursive fibonacci, subset generation
C) Binary search
D) Linear search

✔ Correct Answer: B

Reason: O(2ⁿ): naive fibonacci (each call makes 2 calls), generating all subsets. Exponential growth, impractical for large n.

Tag: Normal

---

### Question 961
Domain: Programming
Topic: Code Analysis
Subtopic: Factorial Complexity
Difficulty: Hard

Question: What is time complexity of generating all permutations?
A) O(n²)
B) O(n!)
C) O(2ⁿ)
D) O(n log n)

✔ Correct Answer: B

Reason: n elements have n! permutations. Generating all requires O(n!) time. Extremely slow for n > 10.

Tag: Normal

---

### Question 962
Domain: Programming
Topic: Memoization
Subtopic: Cache Invalidation
Difficulty: Hard

Question: What is cache invalidation?
A) Invalid cache
B) Removing stale cached data
C) Cache validation
D) Cache creation

✔ Correct Answer: B

Reason: Cache invalidation removes outdated cached data when source changes. "Two hard things: cache invalidation and naming things."

Tag: Normal

---

### Question 963
Domain: Programming
Topic: Code Analysis
Subtopic: LRU Cache Eviction
Difficulty: Hard

Question: What does LRU cache evict?
A) Random item
B) Least recently used item
C) Oldest item
D) Largest item

✔ Correct Answer: B

Reason: LRU (Least Recently Used) evicts item not accessed for longest time. Assumes recently used items likely to be used again.

Tag: Normal

---

### Question 964
Domain: Programming
Topic: Caching Strategies
Subtopic: Cache Policies
Difficulty: Hard

Question: What is LFU cache?
A) Least Frequent Use
B) Least Frequently Used (evicts least accessed item)
C) Last First Use
D) Large File Use

✔ Correct Answer: B

Reason: LFU evicts item with lowest access count. Tracks frequency. Different from LRU (recency). FIFO evicts oldest.

Tag: Normal

---

### Question 965
Domain: Programming
Topic: Code Analysis
Subtopic: Memoization Decorator
Difficulty: Hard

Question: What is the output?
```python
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def expensive(n):
    print(f"Computing {n}")
    return n * 2

print(expensive(5))
print(expensive(5))
```
A) Computing 5, 10, Computing 5, 10
B) Computing 5, 10, 10
C) 10, 10
D) Error

✔ Correct Answer: B

Reason: First call computes and caches (prints "Computing 5", returns 10). Second call returns cached value (no print, returns 10).

Tag: Normal

---

### Question 966
Domain: Programming
Topic: Algorithm Optimization
Subtopic: Early Exit
Difficulty: Easy

Question: What is early exit optimization?
A) Exit program
B) Return/break as soon as result found
C) Exit loop
D) Error exit

✔ Correct Answer: B

Reason: Early exit stops processing when result found, avoiding unnecessary work. Search returns immediately when found, doesn't continue.

Tag: Normal

---

### Question 967
Domain: Programming
Topic: Code Analysis
Subtopic: Short-circuit Evaluation
Difficulty: Medium

Question: What is the output?
```python
def check():
    print("Checked")
    return False

result = False and check()
print(result)
```
A) Checked, False
B) False (no "Checked")
C) True
D) Error

✔ Correct Answer: B

Reason: Short-circuit: 'and' stops if first operand False (result already False). check() never called. Prints only: False.

Tag: Normal

---

### Question 968
Domain: Programming
Topic: Optimization
Subtopic: Loop Invariant
Difficulty: Medium

Question: What is loop invariant code motion?
A) Moving loops
B) Moving calculations outside loop if result doesn't change
C) Invariant loops
D) Loop optimization

✔ Correct Answer: B

Reason: Move loop-invariant calculations outside loop. Instead of computing len(arr) each iteration, compute once before loop.

Tag: Normal

---

### Question 969
Domain: Programming
Topic: Code Analysis
Subtopic: Loop Optimization
Difficulty: Medium

Question: Which is more efficient?
```python
# A
for i in range(len(arr)):
    process(arr[i])

# B
for item in arr:
    process(item)
```
A) A
B) B (avoids repeated len() and indexing)
C) Same
D) Depends

✔ Correct Answer: B

Reason: Direct iteration (B) avoids len() call and indexing overhead. More Pythonic and slightly faster.

Tag: Normal

---

### Question 970
Domain: Programming
Topic: Memory Optimization
Subtopic: Generator vs List
Difficulty: Medium

Question: What is the output?
```python
import sys
gen = (x for x in range(1000))
lst = [x for x in range(1000)]
print(sys.getsizeof(gen) < sys.getsizeof(lst))
```
A) False
B) True
C) Error
D) Same size

✔ Correct Answer: B

Reason: Generator stores only state (small). List stores all 1000 elements. Generator much smaller: True.

Tag: Normal

---

### Question 971
Domain: Programming
Topic: Code Analysis
Subtopic: String Interning
Difficulty: Hard

Question: What is the output?
```python
a = "hello"
b = "hel" + "lo"
print(a is b)
```
A) False
B) True (likely, due to compile-time optimization)
C) Error
D) None

✔ Correct Answer: B

Reason: Python optimizes "hel" + "lo" at compile time to "hello". Both a and b reference same interned string. a is b: True.

Tag: Normal

---

### Question 972
Domain: Programming
Topic: Performance
Subtopic: List vs Tuple Performance
Difficulty: Medium

Question: Why are tuples faster than lists?
A) Smaller
B) Immutable, allows optimizations (no resizing overhead)
C) Better algorithm
D) No difference

✔ Correct Answer: B

Reason: Tuples immutable, no resizing overhead. Python can optimize allocation. Iteration slightly faster. Use tuples for fixed data.

Tag: Normal

---

### Question 973
Domain: Programming
Topic: Code Analysis
Subtopic: Dictionary vs List Lookup
Difficulty: Medium

Question: For 1 million elements, which is faster for lookup?
A) List
B) Dictionary
C) Same
D) Tuple

✔ Correct Answer: B

Reason: Dictionary: O(1) average lookup. List: O(n) linear search. For large n, dictionary dramatically faster.

Tag: Normal

---

### Question 974
Domain: Programming
Topic: Algorithm Selection
Subtopic: Choosing Algorithm
Difficulty: Medium

Question: When is O(n²) algorithm acceptable?
A) Never
B) Small input size or simplicity matters more than performance
C) Always
D) Large inputs

✔ Correct Answer: B

Reason: For small n, O(n²) may be faster than O(n log n) due to lower constants. Simplicity sometimes more valuable than asymptotic efficiency.

Tag: Normal

---

### Question 975
Domain: Programming
Topic: Code Analysis
Subtopic: Algorithm Trade-offs
Difficulty: Hard

Question: What trade-off does memoization make?
A) No trade-off
B) Trades space for time (uses memory to save computation)
C) Trades time for space
D) No benefit

✔ Correct Answer: B

Reason: Memoization stores results (uses space) to avoid recomputation (saves time). Classic space-time trade-off.

Tag: Normal

---

### Question 976
Domain: Programming
Topic: Debugging
Subtopic: Print Debugging
Difficulty: Easy

Question: What is print debugging?
A) Printing code
B) Using print statements to trace execution and values
C) Debug printing
D) Print errors

✔ Correct Answer: B

Reason: Print debugging inserts print statements to observe values and flow. Simple but effective. Remove or use logging for production.

Tag: Normal

---

### Question 977
Domain: Programming
Topic: Code Analysis
Subtopic: Logging vs Print
Difficulty: Medium

Question: Why use logging instead of print for debugging?
A) Faster
B) Configurable levels, can disable, includes metadata
C) Required
D) No difference

✔ Correct Answer: B

Reason: Logging provides levels (DEBUG, INFO, etc.), can be disabled, includes timestamps/levels. Print statements must be manually removed.

Tag: Normal

---

### Question 978
Domain: Programming
Topic: Debugging
Subtopic: Debugger Commands
Difficulty: Medium

Question: What does 'step into' do in debugger?
A) Steps over
B) Enters function call to debug inside
C) Steps out
D) Continues

✔ Correct Answer: B

Reason: Step into enters function to debug line by line. Step over executes function without entering. Step out exits current function.

Tag: Normal

---

### Question 979
Domain: Programming
Topic: Code Analysis
Subtopic: Breakpoint Conditions
Difficulty: Medium

Question: What is conditional breakpoint?
A) if statement
B) Breakpoint that triggers only when condition true
C) Break in condition
D) Conditional code

✔ Correct Answer: B

Reason: Conditional breakpoint pauses execution only when specified condition true. Useful for debugging specific cases in loops.

Tag: Normal

---

### Question 980
Domain: Programming
Topic: Error Handling
Subtopic: Fail Fast
Difficulty: Medium

Question: What is fail fast principle?
A) Fast failure
B) Detect and report errors immediately
C) Never fail
D) Slow failure

✔ Correct Answer: B

Reason: Fail fast detects errors early, failing immediately rather than continuing with invalid state. Makes debugging easier, prevents cascading failures.

Tag: Normal

---

### Question 981
Domain: Programming
Topic: Code Analysis
Subtopic: Assertions for Validation
Difficulty: Medium

Question: What is the output?
```python
def divide(a, b):
    assert b != 0, "Division by zero"
    return a / b

print(divide(10, 0))
```
A) inf
B) AssertionError: Division by zero
C) 0
D) None

✔ Correct Answer: B

Reason: assert b != 0 fails when b=0, raising AssertionError with message. Assertions validate assumptions.

Tag: Normal

---

### Question 982
Domain: Programming
Topic: Code Readability
Subtopic: Naming Conventions
Difficulty: Easy

Question: What is Python naming convention for functions?
A) camelCase
B) snake_case
C) PascalCase
D) kebab-case

✔ Correct Answer: B

Reason: Python uses snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants. Follow PEP 8.

Tag: Normal

---

### Question 983
Domain: Programming
Topic: Code Analysis
Subtopic: Naming Conventions
Difficulty: Easy

Question: What is Java naming convention for classes?
A) snake_case
B) PascalCase
C) camelCase
D) lowercase

✔ Correct Answer: B

Reason: Java uses PascalCase for classes, camelCase for methods/variables, UPPER_CASE for constants. Follow Java conventions.

Tag: Normal

---

### Question 984
Domain: Programming
Topic: Code Readability
Subtopic: Magic Numbers
Difficulty: Medium

Question: What is the output?
```python
SECONDS_PER_DAY = 86400

def days_to_seconds(days):
    return days * SECONDS_PER_DAY

print(days_to_seconds(2))
```
A) 2
B) 172800
C) 86400
D) Error

✔ Correct Answer: B

Reason: Named constant SECONDS_PER_DAY (86400) improves readability. 2 * 86400 = 172800 seconds.

Tag: Normal

---

### Question 985
Domain: Programming
Topic: Code Organization
Subtopic: Single Responsibility
Difficulty: Medium

Question: What violates Single Responsibility Principle?
A) One method
B) Class handling multiple unrelated responsibilities
C) One class
D) Single file

✔ Correct Answer: B

Reason: Class should have one reason to change. Class handling database, UI, and business logic violates SRP. Split into focused classes.

Tag: Normal

---

### Question 986
Domain: Programming
Topic: Code Analysis
Subtopic: Function Length
Difficulty: Easy

Question: What is recommended maximum function length?
A) No limit
B) Short enough to understand at glance (typically < 20-30 lines)
C) 1000 lines
D) One line

✔ Correct Answer: B

Reason: Functions should be short, focused. If too long, extract methods. No strict limit, but aim for single responsibility and readability.

Tag: Normal

---

### Question 987
Domain: Programming
Topic: Code Organization
Subtopic: Cohesion
Difficulty: Medium

Question: What is high cohesion?
A) Sticky code
B) Class elements closely related and focused
C) Many classes
D) Coupled code

✔ Correct Answer: B

Reason: High cohesion: class elements work together toward single purpose. Low cohesion: unrelated elements. Aim for high cohesion.

Tag: Normal

---

### Question 988
Domain: Programming
Topic: Code Organization
Subtopic: Coupling
Difficulty: Medium

Question: What is loose coupling?
A) Loose code
B) Minimal dependencies between modules
C) No coupling
D) Tight integration

✔ Correct Answer: B

Reason: Loose coupling: minimal dependencies, modules independent. Tight coupling: high dependencies, changes ripple. Aim for loose coupling.

Tag: Past Paper

---

### Question 989
Domain: Programming
Topic: Code Analysis
Subtopic: Dependency Direction
Difficulty: Hard

Question: What does "depend on abstractions" mean?
A) Abstract code
B) Depend on interfaces/abstract classes, not concrete implementations
C) No dependencies
D) Abstract thinking

✔ Correct Answer: B

Reason: Depend on abstractions (interfaces) not concretions (implementations). Enables flexibility, testability. Dependency Inversion Principle.

Tag: Normal

---

### Question 990
Domain: Programming
Topic: Error Messages
Subtopic: Meaningful Errors
Difficulty: Easy

Question: What makes good error message?
A) Short
B) Describes what happened and how to fix
C) Technical only
D) Error code

✔ Correct Answer: B

Reason: Good error message explains what happened, why, and how to fix. Include context. "Invalid input" vs "Age must be positive integer".

Tag: Normal

---

### Question 991
Domain: Programming
Topic: Code Analysis
Subtopic: Custom Exceptions
Difficulty: Medium

Question: Why create custom exceptions?
A) More exceptions
B) Specific error types, better error handling
C) Required
D) No benefit

✔ Correct Answer: B

Reason: Custom exceptions provide specific error types, enabling targeted handling. InvalidAgeError more specific than ValueError.

Tag: Normal

---

### Question 992
Domain: Programming
Topic: Input Validation
Subtopic: Validation Importance
Difficulty: Easy

Question: Why validate user input?
A) Slow users
B) Prevent errors, security vulnerabilities, data corruption
C) Required only
D) No reason

✔ Correct Answer: B

Reason: Input validation prevents errors, security issues (injection attacks), data corruption. Validate type, range, format. Never trust user input.

Tag: Normal

---

### Question 993
Domain: Programming
Topic: Code Analysis
Subtopic: Input Validation Example
Difficulty: Medium

Question: What does this code prevent?
```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be 0-150")
    self.age = age
```
A) Nothing
B) Invalid type and out-of-range values
C) All errors
D) Syntax errors

✔ Correct Answer: B

Reason: Validates type (must be int) and range (0-150). Raises appropriate exceptions for invalid input. Prevents invalid state.

Tag: Normal

---

### Question 994
Domain: Programming
Topic: Security
Subtopic: SQL Injection
Difficulty: Hard

Question: How do you prevent SQL injection?
A) Validate input only
B) Use parameterized queries/prepared statements
C) Escape quotes
D) Cannot prevent

✔ Correct Answer: B

Reason: Parameterized queries separate SQL from data, preventing injection. Never concatenate user input into SQL. Use ORM or prepared statements.

Tag: Past Paper

---

### Question 995
Domain: Programming
Topic: Code Analysis
Subtopic: Unsafe SQL
Difficulty: Hard

Question: What's wrong with this code?
```python
username = input("Username: ")
query = f"SELECT * FROM users WHERE name = '{username}'"
cursor.execute(query)
```
A) Nothing
B) SQL injection vulnerability
C) Syntax error
D) Slow query

✔ Correct Answer: B

Reason: Concatenating user input into SQL enables injection. Input "' OR '1'='1" bypasses authentication. Use parameterized queries.

Tag: Normal

---

### Question 996
Domain: Programming
Topic: Security
Subtopic: XSS Prevention
Difficulty: Hard

Question: How do you prevent XSS (Cross-Site Scripting)?
A) Disable scripts
B) Escape/sanitize user input before displaying
C) Use HTTPS
D) Cannot prevent

✔ Correct Answer: B

Reason: XSS injects malicious scripts. Escape HTML special characters (<, >, &), use templating engines with auto-escaping, validate input.

Tag: Normal

---

### Question 997
Domain: Programming
Topic: Code Analysis
Subtopic: Password Storage
Difficulty: Hard

Question: How should passwords be stored?
A) Plain text
B) Hashed with salt using bcrypt/argon2
C) Encrypted
D) Encoded

✔ Correct Answer: B

Reason: Hash passwords with salt using strong algorithms (bcrypt, argon2, PBKDF2). Never store plain text. Encryption reversible, hashing isn't.

Tag: Past Paper

---

### Question 998
Domain: Programming
Topic: Security
Subtopic: CSRF Protection
Difficulty: Hard

Question: What is CSRF token?
A) Cross-site token
B) Random token validating request origin
C) Session token
D) API token

✔ Correct Answer: B

Reason: CSRF (Cross-Site Request Forgery) token validates request came from your site. Include in forms, verify on server. Prevents unauthorized requests.

Tag: Normal

---

### Question 999
Domain: Programming
Topic: Code Analysis
Subtopic: Environment Variables for Secrets
Difficulty: Medium

Question: Why store secrets in environment variables?
A) Convenient
B) Keeps secrets out of code/version control
C) Faster access
D) Required

✔ Correct Answer: B

Reason: Environment variables keep secrets (API keys, passwords) out of code and version control. Use .env files (not committed) or secret management services.

Tag: Normal

---

### Question 1000
Domain: Programming
Topic: Best Practices
Subtopic: Code Review Checklist
Difficulty: Easy

Question: What should code review check?
A) Syntax only
B) Correctness, readability, tests, security, performance
C) Style only
D) Nothing

✔ Correct Answer: B

Reason: Code review checks correctness, edge cases, readability, naming, tests, security vulnerabilities, performance, adherence to standards.

Tag: Normal

---

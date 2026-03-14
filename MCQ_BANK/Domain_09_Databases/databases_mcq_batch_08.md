# Databases MCQ Bank - Batch 08

## Questions 701-800

---

### Question 701
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT p.product_name, 
       COALESCE(SUM(s.quantity), 0) as total_sold
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_sold DESC;
```

A) Only products with sales
B) All products with total quantity sold (0 if no sales), ordered by quantity
C) Only sales records
D) Error

✔ Correct Answer: B

Reason: LEFT JOIN includes all products, COALESCE handles NULLs as 0, and results are ordered by total quantity sold.

Tag: Normal

---

### Question 702
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query calculate?
```sql
SELECT department,
       COUNT(*) as emp_count,
       AVG(salary) as avg_salary,
       MAX(salary) - MIN(salary) as salary_spread
FROM employees
GROUP BY department
HAVING COUNT(*) >= 5;
```

A) All departments
B) Departments with 5+ employees showing count, average, and salary range
C) Only salaries
D) Error

✔ Correct Answer: B

Reason: The query groups by department, calculates statistics, and filters to show only departments with 5 or more employees.

Tag: Normal

---

### Question 703
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this window function show?
```sql
SELECT name, department, salary,
       PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) as salary_percentile
FROM employees;
```

A) Random percentages
B) Each employee's salary percentile within their department
C) Only top employees
D) Error

✔ Correct Answer: B

Reason: PERCENT_RANK calculates the relative rank as a percentage (0 to 1) within each department partition.

Tag: Normal

---

### Question 704
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
SELECT customer_id, COUNT(DISTINCT product_id) as unique_products
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) > 10;
```

A) Counts all orders
B) Shows customers who purchased more than 10 different products
C) Shows all customers
D) Error

✔ Correct Answer: B

Reason: The query counts distinct products per customer and filters to show only those who bought more than 10 different products.

Tag: Normal

---

### Question 705
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT e1.name as Employee, e2.name as Colleague
FROM employees e1
INNER JOIN employees e2 ON e1.department = e2.department AND e1.employee_id <> e2.employee_id;
```

A) All employees
B) Pairs of employees in the same department
C) Only managers
D) Error

✔ Correct Answer: B

Reason: This self-join creates pairs of employees in the same department, excluding pairing an employee with themselves.

Tag: Normal

---

### Question 706
Domain: Databases
Topic: Database System Architecture
Subtopic: Query Compiler
Difficulty: Medium

Question: What does the query compiler do?

A) Compiles programs
B) Translates SQL into an internal representation and optimizes it
C) Deletes queries
D) Backs up queries

✔ Correct Answer: B

Reason: The query compiler parses SQL, translates it to internal representation (like relational algebra), and optimizes it.

Tag: Normal

---

### Question 707
Domain: Databases
Topic: Database System Architecture
Subtopic: Execution Engine
Difficulty: Easy

Question: What does the execution engine do?

A) Compiles queries
B) Executes the query execution plan
C) Stores data
D) Manages users

✔ Correct Answer: B

Reason: The execution engine carries out the operations specified in the query execution plan.

Tag: Normal

---

### Question 708
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Keys
Difficulty: Medium

Question: Can a relation have multiple candidate keys?

A) No, only one
B) Yes, multiple attributes or combinations can uniquely identify tuples
C) Never
D) Only two

✔ Correct Answer: B

Reason: A relation can have multiple candidate keys; any minimal set of attributes that uniquely identifies tuples is a candidate key.

Tag: Past Paper

---

### Question 709
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Keys
Difficulty: Easy

Question: How many primary keys can a table have?

A) Multiple
B) Exactly one
C) None
D) Unlimited

✔ Correct Answer: B

Reason: A table can have exactly one primary key, chosen from among the candidate keys.

Tag: Normal

---

### Question 710
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization Process
Difficulty: Medium

Question: What is the relationship between normal forms?

A) Independent
B) Each higher normal form includes requirements of lower forms
C) No relationship
D) Opposite requirements

✔ Correct Answer: B

Reason: Normal forms are cumulative; to be in 3NF, a relation must first be in 2NF, which requires 1NF.

Tag: Past Paper

---

### Question 711
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Decomposition Quality
Difficulty: Hard

Question: What makes a good decomposition?

A) Creates many tables
B) Lossless join and dependency preservation
C) Lossy join
D) Random decomposition

✔ Correct Answer: B

Reason: A good decomposition is lossless (can reconstruct original) and preserves functional dependencies.

Tag: Past Paper

---

### Question 712
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Properties
Difficulty: Medium

Question: Why is atomicity important?

A) It's not important
B) Prevents partial updates that leave database in inconsistent state
C) Slows down transactions
D) No reason

✔ Correct Answer: B

Reason: Atomicity ensures all-or-nothing execution, preventing partial updates that could leave the database inconsistent.

Tag: Normal

---

### Question 713
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Properties
Difficulty: Medium

Question: Why is isolation important?

A) It's not important
B) Prevents concurrent transactions from interfering with each other
C) Slows down transactions
D) No reason

✔ Correct Answer: B

Reason: Isolation prevents concurrent transactions from seeing each other's intermediate states, maintaining consistency.

Tag: Normal

---

### Question 714
Domain: Databases
Topic: Concurrency Control
Subtopic: Locking Granularity
Difficulty: Medium

Question: What is database-level locking?

A) Locking individual rows
B) Locking the entire database
C) No locking
D) Locking columns

✔ Correct Answer: B

Reason: Database-level locking locks the entire database, providing maximum isolation but minimum concurrency.

Tag: Normal

---

### Question 715
Domain: Databases
Topic: Concurrency Control
Subtopic: Locking Granularity
Difficulty: Medium

Question: What is row-level locking?

A) Locking entire table
B) Locking individual rows
C) No locking
D) Locking database

✔ Correct Answer: B

Reason: Row-level locking locks individual rows, providing maximum concurrency but higher overhead.

Tag: Normal

---

### Question 716
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Strategies
Difficulty: Medium

Question: What is forward recovery?

A) Backward recovery
B) Reapplying logged operations to restore database
C) No recovery
D) Deleting logs

✔ Correct Answer: B

Reason: Forward recovery (redo) reapplies logged operations from a backup to bring the database to a consistent state.

Tag: Normal

---

### Question 717
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Strategies
Difficulty: Medium

Question: What is backward recovery?

A) Forward recovery
B) Undoing operations to restore database to previous state
C) No recovery
D) Deleting logs

✔ Correct Answer: B

Reason: Backward recovery (undo) reverses operations to restore the database to a previous consistent state.

Tag: Normal

---

### Question 718
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Usage
Difficulty: Medium

Question: When does the optimizer choose not to use an index?

A) Never
B) When table scan is estimated to be faster (e.g., retrieving most rows)
C) Always uses index
D) Random choice

✔ Correct Answer: B

Reason: The optimizer may choose a table scan over an index when retrieving a large percentage of rows makes scanning more efficient.

Tag: Normal

---

### Question 719
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Composite Index Order
Difficulty: Hard

Question: In a composite index on (A, B, C), which queries can use the index?

A) Only queries on A, B, and C together
B) Queries on A, (A,B), or (A,B,C) - leftmost prefix
C) Any combination
D) None

✔ Correct Answer: B

Reason: Composite indexes can be used for queries on leftmost prefixes: A alone, A and B, or A, B, and C together.

Tag: Normal

---

### Question 720
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: What is the main advantage of hash join over nested loop join?

A) No advantage
B) More efficient for large tables with equality joins
C) Slower
D) Uses less memory

✔ Correct Answer: B

Reason: Hash join is more efficient for large tables with equality join conditions, building a hash table on one relation.

Tag: Normal

---

### Question 721
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: What is the main advantage of merge join?

A) No advantage
B) Efficient when both inputs are already sorted on join key
C) Slower than all others
D) Uses most memory

✔ Correct Answer: B

Reason: Merge join is very efficient when both inputs are already sorted on the join key, avoiding sorting overhead.

Tag: Normal

---

### Question 722
Domain: Databases
Topic: Database Security
Subtopic: Access Control Models
Difficulty: Medium

Question: What is discretionary access control (DAC)?

A) Mandatory control
B) Owner of resource controls access permissions
C) No control
D) System-controlled only

✔ Correct Answer: B

Reason: In DAC, the owner of a resource has discretion to grant or revoke access permissions to other users.

Tag: Normal

---

### Question 723
Domain: Databases
Topic: Database Security
Subtopic: SQL Injection
Difficulty: Medium

Question: What is a blind SQL injection?

A) Visible injection
B) Injection where attacker infers information without seeing direct output
C) No injection
D) Failed injection

✔ Correct Answer: B

Reason: Blind SQL injection occurs when the application doesn't display errors, so attackers infer information through true/false questions or timing.

Tag: Normal

---

### Question 724
Domain: Databases
Topic: Distributed Databases
Subtopic: Transparency Types
Difficulty: Medium

Question: What is transaction transparency?

A) Visible transactions
B) Users can execute transactions without knowing data distribution
C) No transactions
D) Manual transactions

✔ Correct Answer: B

Reason: Transaction transparency allows users to execute transactions as if on a centralized database, hiding distribution complexity.

Tag: Normal

---

### Question 725
Domain: Databases
Topic: Distributed Databases
Subtopic: Transparency Types
Difficulty: Medium

Question: What is performance transparency?

A) Visible performance
B) System performs consistently regardless of load or configuration changes
C) No performance
D) Manual optimization

✔ Correct Answer: B

Reason: Performance transparency ensures consistent performance despite changes in load, network, or system configuration.

Tag: Normal

---

### Question 726
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Document Databases
Difficulty: Medium

Question: What is a collection in MongoDB?

A) A row
B) A group of documents (similar to a table)
C) A column
D) A database

✔ Correct Answer: B

Reason: A collection in MongoDB is a group of documents, analogous to a table in relational databases.

Tag: Normal

---

### Question 727
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Document Databases
Difficulty: Easy

Question: What is a document in MongoDB?

A) A table
B) A JSON-like record (similar to a row)
C) A database
D) An index

✔ Correct Answer: B

Reason: A document in MongoDB is a JSON-like (BSON) record, analogous to a row in relational databases.

Tag: Normal

---

### Question 728
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Dimensional Modeling
Difficulty: Medium

Question: What is a factless fact table?

A) A table with no facts
B) A fact table recording events without numeric measures
C) A deleted table
D) An error

✔ Correct Answer: B

Reason: A factless fact table records events or relationships without numeric measures, like student course enrollment.

Tag: Normal

---

### Question 729
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Dimensional Modeling
Difficulty: Medium

Question: What is a bridge table?

A) A regular table
B) A table resolving many-to-many relationships in dimensional models
C) A deleted table
D) A backup table

✔ Correct Answer: B

Reason: A bridge table resolves many-to-many relationships between fact and dimension tables in dimensional models.

Tag: Normal

---

### Question 730
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Set Operations
Difficulty: Medium

Question: What is the result of UNION vs UNION ALL in terms of duplicates?

A) Both keep duplicates
B) UNION removes duplicates, UNION ALL keeps them
C) Both remove duplicates
D) No difference

✔ Correct Answer: B

Reason: UNION removes duplicate rows from the combined result, while UNION ALL keeps all rows including duplicates.

Tag: Normal

---

### Question 731
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: NULL Handling
Difficulty: Hard

Question: What is the result of (NULL AND FALSE)?

A) NULL
B) FALSE
C) TRUE
D) Error

✔ Correct Answer: B

Reason: In three-valued logic, (NULL AND FALSE) evaluates to FALSE because FALSE makes the entire expression FALSE regardless of the other operand.

Tag: Past Paper

---

### Question 732
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: NULL Handling
Difficulty: Hard

Question: What is the result of (NULL OR FALSE)?

A) TRUE
B) FALSE
C) NULL
D) Error

✔ Correct Answer: C

Reason: In three-valued logic, (NULL OR FALSE) evaluates to NULL because the result depends on the unknown NULL value.

Tag: Past Paper

---

### Question 733
Domain: Databases
Topic: Advanced SQL
Subtopic: Pivot Tables
Difficulty: Hard

Question: What is the purpose of PIVOT operation?

A) Rotating database
B) Converting row data into columns for cross-tabulation
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: PIVOT transforms row data into columns, useful for creating cross-tabulation reports and summary views.

Tag: Normal

---

### Question 734
Domain: Databases
Topic: Advanced SQL
Subtopic: Dynamic SQL
Difficulty: Hard

Question: What is a security risk with dynamic SQL?

A) No risks
B) SQL injection if user input is not properly sanitized
C) Too secure
D) No execution

✔ Correct Answer: B

Reason: Dynamic SQL is vulnerable to SQL injection if user input is concatenated into SQL strings without proper sanitization.

Tag: Normal

---

### Question 735
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Expressive Power
Difficulty: Hard

Question: Can relational algebra express recursive queries?

A) Yes, easily
B) No, it cannot express recursive queries
C) Sometimes
D) Always

✔ Correct Answer: B

Reason: Standard relational algebra cannot express recursive queries; SQL extensions like recursive CTEs are needed.

Tag: Past Paper

---

### Question 736
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Operators
Difficulty: Medium

Question: Is the difference operation (−) commutative?

A) Yes
B) No, R − S ≠ S − R
C) Sometimes
D) Always

✔ Correct Answer: B

Reason: Difference is not commutative; R − S gives tuples in R but not in S, while S − R gives tuples in S but not in R.

Tag: Past Paper

---

### Question 737
Domain: Databases
Topic: Database Design & Normalization
Subtopic: BCNF vs 3NF
Difficulty: Hard

Question: When might you choose 3NF over BCNF?

A) Never
B) When BCNF decomposition doesn't preserve dependencies
C) Always choose BCNF
D) Random choice

✔ Correct Answer: B

Reason: 3NF may be preferred over BCNF when BCNF decomposition would not preserve all functional dependencies.

Tag: Past Paper

---

### Question 738
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization Techniques
Difficulty: Medium

Question: What is a common denormalization technique?

A) Further normalization
B) Adding derived columns or redundant data
C) Removing all data
D) Random changes

✔ Correct Answer: B

Reason: Common denormalization includes adding derived columns (like totals) or redundant data to avoid joins.

Tag: Normal

---

### Question 739
Domain: Databases
Topic: Transaction Management
Subtopic: Concurrency Issues
Difficulty: Hard

Question: What is the uncommitted dependency problem?

A) No problem
B) Reading data written by an uncommitted transaction (dirty read)
C) Fast reads
D) Secure reads

✔ Correct Answer: B

Reason: Uncommitted dependency (dirty read) occurs when a transaction reads data written by another uncommitted transaction.

Tag: Past Paper

---

### Question 740
Domain: Databases
Topic: Transaction Management
Subtopic: Concurrency Issues
Difficulty: Hard

Question: What is the inconsistent analysis problem?

A) No problem
B) Reading data multiple times with different values due to concurrent updates
C) Fast analysis
D) Correct analysis

✔ Correct Answer: B

Reason: Inconsistent analysis occurs when a transaction reads data multiple times and gets different values due to concurrent updates.

Tag: Past Paper

---

### Question 741
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: What is the no-wait protocol?

A) Always wait
B) Transaction aborts immediately if it cannot acquire a lock
C) Wait indefinitely
D) Random waiting

✔ Correct Answer: B

Reason: In no-wait protocol, if a transaction cannot acquire a lock, it aborts immediately rather than waiting.

Tag: Normal

---

### Question 742
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: What is the cautious waiting protocol?

A) Never wait
B) Transaction waits only if the holding transaction is not waiting
C) Always wait
D) Random waiting

✔ Correct Answer: B

Reason: Cautious waiting allows a transaction to wait for a lock only if the holding transaction is not itself waiting for a lock.

Tag: Normal

---

### Question 743
Domain: Databases
Topic: Recovery Management
Subtopic: ARIES Algorithm
Difficulty: Hard

Question: What does the Analysis phase of ARIES do?

A) Executes queries
B) Determines which transactions to undo and redo
C) Deletes data
D) Backs up data

✔ Correct Answer: B

Reason: The Analysis phase scans the log to determine which transactions need to be undone and which need to be redone.

Tag: Past Paper

---

### Question 744
Domain: Databases
Topic: Recovery Management
Subtopic: ARIES Algorithm
Difficulty: Hard

Question: What does the Redo phase of ARIES do?

A) Undoes changes
B) Reapplies all logged operations from a certain point
C) Deletes logs
D) Backs up data

✔ Correct Answer: B

Reason: The Redo phase reapplies all logged operations to restore the database to its state at the time of failure.

Tag: Past Paper

---

### Question 745
Domain: Databases
Topic: Recovery Management
Subtopic: ARIES Algorithm
Difficulty: Hard

Question: What does the Undo phase of ARIES do?

A) Redoes changes
B) Reverses changes from transactions that were active at failure
C) Commits transactions
D) Backs up data

✔ Correct Answer: B

Reason: The Undo phase reverses changes made by transactions that were active but not committed at the time of failure.

Tag: Past Paper

---

### Question 746
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Types
Difficulty: Medium

Question: What is a unique index?

A) A regular index
B) An index that enforces uniqueness of values
C) A deleted index
D) A temporary index

✔ Correct Answer: B

Reason: A unique index ensures that all values in the indexed column(s) are unique, similar to a UNIQUE constraint.

Tag: Normal

---

### Question 747
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Types
Difficulty: Medium

Question: What is a function-based index?

A) A regular index
B) An index on the result of a function or expression
C) A deleted index
D) A backup index

✔ Correct Answer: B

Reason: A function-based index is built on the result of a function or expression rather than directly on column values.

Tag: Normal

---

### Question 748
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Optimization Levels
Difficulty: Medium

Question: What is heuristic optimization?

A) Random optimization
B) Using rules of thumb to transform queries
C) No optimization
D) Manual optimization

✔ Correct Answer: B

Reason: Heuristic optimization uses predefined rules (like pushing selections down) to transform queries without cost estimation.

Tag: Normal

---

### Question 749
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Optimization Levels
Difficulty: Medium

Question: What is cost-based optimization?

A) Minimizing costs
B) Evaluating multiple plans and choosing the one with lowest estimated cost
C) No optimization
D) Random selection

✔ Correct Answer: B

Reason: Cost-based optimization evaluates multiple execution plans using cost estimates and selects the plan with the lowest cost.

Tag: Normal

---

### Question 750
Domain: Databases
Topic: Database Security
Subtopic: Threats
Difficulty: Easy

Question: What is a database security vulnerability?

A) A strength
B) A weakness that can be exploited to compromise security
C) A feature
D) A backup

✔ Correct Answer: B

Reason: A vulnerability is a weakness in the system that can be exploited by threats to compromise security.

Tag: Normal

---

### Question 751
Domain: Databases
Topic: Database Security
Subtopic: Defense Mechanisms
Difficulty: Medium

Question: What is defense in depth in database security?

A) Single layer
B) Multiple layers of security controls
C) No defense
D) One strong control

✔ Correct Answer: B

Reason: Defense in depth uses multiple layers of security controls so that if one fails, others continue to provide protection.

Tag: Normal

---

### Question 752
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is a coordinator in distributed transactions?

A) A participant
B) The site that initiates and manages the transaction
C) A backup site
D) A deleted site

✔ Correct Answer: B

Reason: The coordinator is the site that initiates the distributed transaction and manages the commit protocol.

Tag: Normal

---

### Question 753
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is a participant in distributed transactions?

A) The coordinator
B) A site that executes part of the distributed transaction
C) A backup site
D) A deleted site

✔ Correct Answer: B

Reason: Participants are sites that execute portions of the distributed transaction under the coordinator's direction.

Tag: Normal

---

### Question 754
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: CAP Theorem
Difficulty: Hard

Question: What does "CP" mean in CAP theorem?

A) Consistent and Partition-tolerant
B) Consistent and Available
C) Complete and Perfect
D) Cached and Persistent

✔ Correct Answer: A

Reason: CP systems prioritize Consistency and Partition tolerance, potentially sacrificing Availability during network partitions.

Tag: Normal

---

### Question 755
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Replication Strategies
Difficulty: Medium

Question: What is master-master replication?

A) One master only
B) Multiple nodes can accept writes
C) No replication
D) Read-only replication

✔ Correct Answer: B

Reason: Master-master (multi-master) replication allows multiple nodes to accept write operations, requiring conflict resolution.

Tag: Normal

---

### Question 756
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining Tasks
Difficulty: Easy

Question: What is regression in data mining?

A) Going backward
B) Predicting continuous numeric values
C) Grouping data
D) Deleting data

✔ Correct Answer: B

Reason: Regression is a data mining task that predicts continuous numeric values (like price or temperature) based on input features.

Tag: Normal

---

### Question 757
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining Tasks
Difficulty: Easy

Question: What is association rule mining?

A) Random rules
B) Discovering relationships between items in datasets
C) Deleting associations
D) Backing up rules

✔ Correct Answer: B

Reason: Association rule mining discovers interesting relationships (like "customers who buy X also buy Y") in large datasets.

Tag: Normal

---

### Question 758
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT name FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE department = 'HR');
```

A) All employees
B) Employees earning more than every HR employee
C) Only HR employees
D) Error

✔ Correct Answer: B

Reason: The query selects employees whose salary is greater than the salary of all employees in the HR department.

Tag: Past Paper

---

### Question 759
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query do?
```sql
SELECT product_id, 
       SUM(CASE WHEN status = 'completed' THEN quantity ELSE 0 END) as completed_qty,
       SUM(CASE WHEN status = 'pending' THEN quantity ELSE 0 END) as pending_qty
FROM orders
GROUP BY product_id;
```

A) Counts orders
B) Calculates completed and pending quantities per product
C) Deletes orders
D) Error

✔ Correct Answer: B

Reason: The query uses conditional aggregation to calculate completed and pending quantities separately for each product.

Tag: Normal

---

### Question 760
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this window function calculate?
```sql
SELECT name, salary,
       salary - LAG(salary) OVER (ORDER BY salary) as salary_diff
FROM employees;
```

A) Total salary
B) Difference between each employee's salary and the next lower salary
C) Average salary
D) Error

✔ Correct Answer: B

Reason: LAG retrieves the previous (lower) salary in the ordered list, and the difference is calculated.

Tag: Normal

---

### Question 761
Domain: Databases
Topic: Database System Architecture
Subtopic: Catalog Management
Difficulty: Medium

Question: What is the system catalog (data dictionary)?

A) A user table
B) Metadata about database objects stored in the database itself
C) A backup catalog
D) A deleted catalog

✔ Correct Answer: B

Reason: The system catalog stores metadata about database objects (tables, columns, indexes, etc.) in special system tables.

Tag: Normal

---

### Question 762
Domain: Databases
Topic: Database System Architecture
Subtopic: Metadata
Difficulty: Easy

Question: What is metadata?

A) User data
B) Data about data (structure, constraints, relationships)
C) Deleted data
D) Backup data

✔ Correct Answer: B

Reason: Metadata is "data about data" - information describing the structure, constraints, and relationships of data.

Tag: Normal

---

### Question 763
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Constraints
Difficulty: Medium

Question: What is an assertion in databases?

A) A statement
B) A constraint that can involve multiple tables
C) A query
D) A backup

✔ Correct Answer: B

Reason: An assertion is a general constraint that can involve multiple tables and is checked whenever relevant data changes.

Tag: Normal

---

### Question 764
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Views
Difficulty: Easy

Question: Can you insert data through a view?

A) Never
B) Sometimes, depending on view definition and underlying tables
C) Always
D) Views are read-only always

✔ Correct Answer: B

Reason: Inserts through views are possible for simple views but may not be allowed for complex views with joins, aggregates, or DISTINCT.

Tag: Normal

---

### Question 765
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Trade-offs
Difficulty: Medium

Question: What is the trade-off between normalization and performance?

A) No trade-off
B) Higher normalization may require more joins, affecting read performance
C) Normalization always improves performance
D) No relationship

✔ Correct Answer: B

Reason: Higher normalization reduces redundancy but may require more joins, potentially affecting read query performance.

Tag: Normal

---

### Question 766
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Functional Dependencies
Difficulty: Hard

Question: What is a trivial functional dependency?

A) Important dependency
B) A dependency where the right side is a subset of the left side
C) Complex dependency
D) No dependency

✔ Correct Answer: B

Reason: A trivial FD has the right side as a subset of the left side (e.g., AB → A), always satisfied and provides no information.

Tag: Past Paper

---

### Question 767
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Scheduling
Difficulty: Hard

Question: What is a non-serial schedule?

A) A serial schedule
B) A schedule where operations from different transactions are interleaved
C) No schedule
D) A deleted schedule

✔ Correct Answer: B

Reason: A non-serial schedule interleaves operations from multiple transactions, allowing concurrent execution.

Tag: Past Paper

---

### Question 768
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Scheduling
Difficulty: Hard

Question: Why are non-serial schedules used?

A) They're not used
B) To improve system throughput and resource utilization
C) To slow down systems
D) No reason

✔ Correct Answer: B

Reason: Non-serial schedules allow concurrent execution, improving throughput and resource utilization compared to serial execution.

Tag: Normal

---

### Question 769
Domain: Databases
Topic: Concurrency Control
Subtopic: Phantom Problem
Difficulty: Hard

Question: How can phantom reads be prevented?

A) They cannot be prevented
B) Using range locks or serializable isolation level
C) Using shared locks only
D) No prevention needed

✔ Correct Answer: B

Reason: Phantom reads are prevented by using range locks (predicate locking) or serializable isolation level.

Tag: Past Paper

---

### Question 770
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Protocols
Difficulty: Hard

Question: What is the difference between 2PL and strict 2PL?

A) No difference
B) Strict 2PL holds all exclusive locks until commit/abort
C) 2PL is stricter
D) Random difference

✔ Correct Answer: B

Reason: Strict 2PL requires holding all exclusive locks until transaction commits or aborts, preventing cascading rollbacks.

Tag: Past Paper

---

### Question 771
Domain: Databases
Topic: Recovery Management
Subtopic: Log Records
Difficulty: Medium

Question: What is a compensation log record?

A) A regular log record
B) A log record describing undo operations during recovery
C) A deleted record
D) A backup record

✔ Correct Answer: B

Reason: Compensation log records (CLRs) describe undo operations performed during recovery, ensuring they're not undone again.

Tag: Normal

---

### Question 772
Domain: Databases
Topic: Recovery Management
Subtopic: Database States
Difficulty: Medium

Question: What is a consistent database state?

A) Any state
B) A state where all integrity constraints are satisfied
C) An inconsistent state
D) A deleted state

✔ Correct Answer: B

Reason: A consistent database state is one where all integrity constraints and business rules are satisfied.

Tag: Normal

---

### Question 773
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Performance
Difficulty: Medium

Question: What affects index performance?

A) Nothing
B) Index selectivity, size, fragmentation, and data distribution
C) Only size
D) Only type

✔ Correct Answer: B

Reason: Index performance is affected by selectivity, size, fragmentation level, and data distribution patterns.

Tag: Normal

---

### Question 774
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Design
Difficulty: Medium

Question: Should you index foreign key columns?

A) Never
B) Often beneficial, especially for join operations
C) Always harmful
D) Doesn't matter

✔ Correct Answer: B

Reason: Indexing foreign key columns is often beneficial as they're frequently used in joins and referential integrity checks.

Tag: Normal

---

### Question 775
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Rewriting
Difficulty: Hard

Question: What is subquery unnesting?

A) Creating subqueries
B) Converting subqueries to joins for better performance
C) Deleting subqueries
D) No transformation

✔ Correct Answer: B

Reason: Subquery unnesting transforms correlated subqueries into joins, often resulting in better performance.

Tag: Normal

---

### Question 776
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Execution Plans
Difficulty: Medium

Question: What is a query execution plan?

A) A backup plan
B) A detailed description of operations to execute a query
C) A security plan
D) A deletion plan

✔ Correct Answer: B

Reason: An execution plan details the sequence of operations (scans, joins, sorts) the database will perform to execute a query.

Tag: Normal

---

### Question 777
Domain: Databases
Topic: Database Security
Subtopic: Encryption
Difficulty: Medium

Question: What is transparent data encryption (TDE)?

A) Visible encryption
B) Automatic encryption at storage level transparent to applications
C) Manual encryption
D) No encryption

✔ Correct Answer: B

Reason: TDE automatically encrypts data at the storage level, transparent to applications accessing the data.

Tag: Normal

---

### Question 778
Domain: Databases
Topic: Database Security
Subtopic: Authentication
Difficulty: Easy

Question: What is two-factor authentication?

A) One factor
B) Authentication using two different types of credentials
C) No authentication
D) Three factors

✔ Correct Answer: B

Reason: Two-factor authentication requires two different types of credentials (e.g., password and token) for stronger security.

Tag: Normal

---

### Question 779
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Replication
Difficulty: Medium

Question: What is synchronous replication?

A) Asynchronous replication
B) Changes are replicated immediately before transaction commits
C) No replication
D) Delayed replication

✔ Correct Answer: B

Reason: Synchronous replication ensures changes are replicated to all replicas before the transaction commits, ensuring consistency.

Tag: Normal

---

### Question 780
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Replication
Difficulty: Medium

Question: What is asynchronous replication?

A) Synchronous replication
B) Changes are replicated after transaction commits
C) No replication
D) Immediate replication

✔ Correct Answer: B

Reason: Asynchronous replication replicates changes after the transaction commits, allowing faster commits but potential temporary inconsistency.

Tag: Normal

---

### Question 781
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Data Models
Difficulty: Medium

Question: What is denormalization in NoSQL?

A) Normalization
B) Storing related data together to avoid joins
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: NoSQL databases often denormalize data by storing related information together to avoid expensive join operations.

Tag: Normal

---

### Question 782
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Scalability
Difficulty: Easy

Question: What is horizontal scaling?

A) Vertical scaling
B) Adding more machines to distribute load
C) Adding more CPU to one machine
D) No scaling

✔ Correct Answer: B

Reason: Horizontal scaling (scale-out) adds more machines to distribute the load, a key strength of NoSQL databases.

Tag: Normal

---

### Question 783
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Quality
Difficulty: Easy

Question: What is data quality?

A) Data quantity
B) The degree to which data is accurate, complete, and consistent
C) Data size
D) Data age

✔ Correct Answer: B

Reason: Data quality measures how well data meets requirements for accuracy, completeness, consistency, and timeliness.

Tag: Normal

---

### Question 784
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Governance
Difficulty: Easy

Question: What is data governance?

A) Government data
B) Management of data availability, usability, integrity, and security
C) Data deletion
D) Data backup

✔ Correct Answer: B

Reason: Data governance is the overall management of data availability, usability, integrity, and security in an organization.

Tag: Normal

---

### Question 785
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Performance
Difficulty: Medium

Question: Why should you avoid SELECT * in production code?

A) It's required
B) It retrieves unnecessary columns, wasting resources
C) It's faster
D) No reason

✔ Correct Answer: B

Reason: SELECT * retrieves all columns including unnecessary ones, wasting network bandwidth, memory, and processing time.

Tag: Normal

---

### Question 786
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Best Practices
Difficulty: Easy

Question: Why should you use meaningful table and column names?

A) No reason
B) Improves code readability and maintainability
C) Slows down queries
D) Increases storage

✔ Correct Answer: B

Reason: Meaningful names improve code readability, making it easier to understand and maintain database schemas and queries.

Tag: Normal

---

### Question 787
Domain: Databases
Topic: Advanced SQL
Subtopic: Error Handling
Difficulty: Medium

Question: What is the purpose of TRY-CATCH blocks in SQL?

A) No purpose
B) Handling errors and exceptions gracefully
C) Speeding up queries
D) Deleting data

✔ Correct Answer: B

Reason: TRY-CATCH blocks allow graceful error handling, enabling custom error responses and preventing abrupt failures.

Tag: Normal

---

### Question 788
Domain: Databases
Topic: Advanced SQL
Subtopic: Batch Operations
Difficulty: Medium

Question: Why use batch operations instead of row-by-row processing?

A) No difference
B) Batch operations are more efficient, reducing overhead
C) Row-by-row is faster
D) No reason

✔ Correct Answer: B

Reason: Batch operations process multiple rows together, significantly reducing overhead compared to row-by-row processing.

Tag: Normal

---

### Question 789
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Query Optimization
Difficulty: Hard

Question: Which relational algebra transformation is always beneficial?

A) None are always beneficial
B) Pushing selections down (applying filters early)
C) Delaying selections
D) Random transformations

✔ Correct Answer: B

Reason: Pushing selections down (applying filters early) is generally beneficial as it reduces the size of intermediate results.

Tag: Normal

---

### Question 790
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Schema Evolution
Difficulty: Medium

Question: What is schema evolution?

A) No changes
B) Modifying database schema over time as requirements change
C) Deleting schema
D) Backing up schema

✔ Correct Answer: B

Reason: Schema evolution is the process of modifying the database schema over time to accommodate changing requirements.

Tag: Normal

---

### Question 791
Domain: Databases
Topic: Transaction Management
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is a blocking protocol?

A) Non-blocking protocol
B) A protocol where transactions may wait indefinitely
C) No waiting
D) Fast protocol

✔ Correct Answer: B

Reason: Blocking protocols (like 2PL) may cause transactions to wait indefinitely for locks, potentially leading to deadlocks.

Tag: Normal

---

### Question 792
Domain: Databases
Topic: Concurrency Control
Subtopic: Optimistic Concurrency
Difficulty: Hard

Question: When is optimistic concurrency control most effective?

A) High conflict scenarios
B) Low conflict scenarios with mostly read operations
C: Never effective
D) Always effective

✔ Correct Answer: B

Reason: Optimistic concurrency control works best when conflicts are rare, avoiding locking overhead for read-heavy workloads.

Tag: Normal

---

### Question 793
Domain: Databases
Topic: Recovery Management
Subtopic: Disaster Recovery
Difficulty: Easy

Question: What is RTO (Recovery Time Objective)?

A) Recovery cost
B) Maximum acceptable time to restore service after disaster
C) Recovery size
D) Recovery method

✔ Correct Answer: B

Reason: RTO is the maximum acceptable time to restore service after a disaster, defining recovery speed requirements.

Tag: Normal

---

### Question 794
Domain: Databases
Topic: Recovery Management
Subtopic: Disaster Recovery
Difficulty: Easy

Question: What is RPO (Recovery Point Objective)?

A) Recovery time
B) Maximum acceptable amount of data loss measured in time
C) Recovery cost
D) Recovery method

✔ Correct Answer: B

Reason: RPO is the maximum acceptable amount of data loss measured in time (e.g., losing up to 1 hour of data).

Tag: Normal

---

### Question 795
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Monitoring
Difficulty: Medium

Question: Why monitor index usage?

A) No reason
B) To identify unused indexes that waste resources
C) To slow down queries
D) To increase storage

✔ Correct Answer: B

Reason: Monitoring index usage helps identify unused indexes that consume storage and slow down write operations without providing benefits.

Tag: Normal

---

### Question 796
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Tuning
Difficulty: Medium

Question: What is query tuning?

A) Deleting queries
B) Optimizing queries to improve performance
C) Creating queries
D) Backing up queries

✔ Correct Answer: B

Reason: Query tuning is the process of analyzing and modifying queries to improve their execution performance.

Tag: Normal

---

### Question 797
Domain: Databases
Topic: Database Security
Subtopic: Compliance
Difficulty: Easy

Question: Why is database security compliance important?

A) It's not important
B) To meet legal and regulatory requirements
C) To slow down access
D) No reason

✔ Correct Answer: B

Reason: Security compliance ensures the organization meets legal and regulatory requirements for data protection and privacy.

Tag: Normal

---

### Question 798
Domain: Databases
Topic: Distributed Databases
Subtopic: Network Partitions
Difficulty: Hard

Question: What is split-brain in distributed systems?

A) No problem
B) Network partition causing multiple nodes to act as primary
C) Fast processing
D) Backup issue

✔ Correct Answer: B

Reason: Split-brain occurs when a network partition causes multiple nodes to believe they're the primary, potentially causing conflicts.

Tag: Normal

---

### Question 799
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Use Cases
Difficulty: Medium

Question: When should you use a relational database over NoSQL?

A) Never
B) When ACID compliance and complex queries are critical
C) Always use NoSQL
D) Random choice

✔ Correct Answer: B

Reason: Relational databases are preferred when ACID compliance, complex queries, and strong consistency are critical requirements.

Tag: Normal

---

### Question 800
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Big Data
Difficulty: Easy

Question: What characterizes big data?

A) Small volume
B) High volume, velocity, and variety (3 Vs)
C) Simple data
D) Static data

✔ Correct Answer: B

Reason: Big data is characterized by the 3 Vs: high Volume, Velocity (speed of generation), and Variety (different types).

Tag: Normal

---

**End of Batch 08**

# Databases MCQ Bank - Batch 05

## Questions 401-500

---

### Question 401
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the output of the following SQL query?
```sql
SELECT COUNT(*) FROM employees WHERE salary IS NULL;
```

A) 0
B) The number of employees with NULL salary
C) Error
D) All employees

✔ Correct Answer: B

Reason: COUNT(*) counts all rows where the condition is true, including rows where salary IS NULL.

Tag: Normal

---

### Question 402
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What will this query return?
```sql
SELECT * FROM products WHERE price BETWEEN 10 AND 20;
```

A) Products with price > 10 and < 20
B) Products with price >= 10 and <= 20
C) Products with price = 10 or = 20
D) Error

✔ Correct Answer: B

Reason: BETWEEN is inclusive, so it returns products with price >= 10 AND <= 20.

Tag: Normal

---

### Question 403
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query if the table has duplicate names?
```sql
SELECT DISTINCT name FROM customers ORDER BY name;
```

A) All names including duplicates
B) Unique names in sorted order
C) Error
D) Random names

✔ Correct Answer: B

Reason: DISTINCT removes duplicate names, and ORDER BY sorts the unique names alphabetically.

Tag: Normal

---

### Question 404
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query do?
```sql
SELECT department, AVG(salary) as avg_sal 
FROM employees 
GROUP BY department 
HAVING AVG(salary) > 50000;
```

A) Shows all departments
B) Shows departments with average salary > 50000
C) Shows all employees
D) Error

✔ Correct Answer: B

Reason: The query groups by department, calculates average salary, and filters to show only departments where average salary exceeds 50000.

Tag: Past Paper

---

### Question 405
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What will this query return?
```sql
SELECT name FROM employees WHERE name LIKE 'A%';
```

A) Names containing 'A'
B) Names starting with 'A'
C) Names ending with 'A'
D) Exact match 'A'

✔ Correct Answer: B

Reason: LIKE 'A%' matches names that start with 'A' followed by any characters.

Tag: Normal

---

### Question 406
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT e1.name 
FROM employees e1 
WHERE e1.salary > (SELECT AVG(salary) FROM employees);
```

A) All employees
B) Employees with above-average salary
C) Employees with below-average salary
D) Error

✔ Correct Answer: B

Reason: The subquery calculates the average salary, and the outer query selects employees whose salary exceeds this average.

Tag: Past Paper

---

### Question 407
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this UPDATE statement do?
```sql
UPDATE products SET price = price * 1.1 WHERE category = 'Electronics';
```

A) Sets all prices to 1.1
B) Increases electronics prices by 10%
C) Decreases prices
D) Error

✔ Correct Answer: B

Reason: Multiplying price by 1.1 increases it by 10% for all products in the Electronics category.

Tag: Normal

---

### Question 408
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What will this query return?
```sql
SELECT c.name, COUNT(o.order_id) 
FROM customers c 
LEFT JOIN orders o ON c.customer_id = o.customer_id 
GROUP BY c.name;
```

A) Only customers with orders
B) All customers with their order count (0 if no orders)
C) Only orders
D) Error

✔ Correct Answer: B

Reason: LEFT JOIN includes all customers, and COUNT counts orders (0 for customers without orders).

Tag: Past Paper

---

### Question 409
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this DELETE statement do?
```sql
DELETE FROM orders WHERE order_date < '2020-01-01';
```

A) Deletes all orders
B) Deletes orders before January 1, 2020
C) Deletes the orders table
D) Error

✔ Correct Answer: B

Reason: The DELETE statement removes all rows where order_date is before January 1, 2020.

Tag: Normal

---

### Question 410
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT name, salary,
CASE 
  WHEN salary > 100000 THEN 'High'
  WHEN salary > 50000 THEN 'Medium'
  ELSE 'Low'
END as salary_level
FROM employees;
```

A) Error
B) Employees with salary levels based on conditions
C) Only high salary employees
D) All employees with same level

✔ Correct Answer: B

Reason: The CASE expression categorizes employees into salary levels based on their salary ranges.

Tag: Normal

---

### Question 411
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query calculate?
```sql
SELECT name, salary,
ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;
```

A) Random numbers
B) Sequential rank numbers based on salary (highest first)
C) Salary values
D) Error

✔ Correct Answer: B

Reason: ROW_NUMBER() assigns sequential numbers to rows ordered by salary in descending order.

Tag: Normal

---

### Question 412
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What will this CTE query return?
```sql
WITH high_earners AS (
  SELECT * FROM employees WHERE salary > 80000
)
SELECT COUNT(*) FROM high_earners;
```

A) All employees
B) Count of employees earning more than 80000
C) Error
D) 80000

✔ Correct Answer: B

Reason: The CTE creates a temporary result set of high earners, then counts them.

Tag: Normal

---

### Question 413
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
SELECT * FROM employees WHERE department IN ('Sales', 'Marketing', 'HR');
```

A) Selects one department
B) Selects employees from Sales, Marketing, or HR departments
C) Error
D) Selects all departments

✔ Correct Answer: B

Reason: IN operator checks if department matches any value in the list (Sales, Marketing, or HR).

Tag: Normal

---

### Question 414
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the result of this query?
```sql
SELECT UPPER(name) FROM employees;
```

A) Lowercase names
B) Uppercase names
C) Original names
D) Error

✔ Correct Answer: B

Reason: UPPER() function converts all characters in the name to uppercase.

Tag: Normal

---

### Question 415
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT department, MAX(salary) - MIN(salary) as salary_range
FROM employees
GROUP BY department;
```

A) All salaries
B) Salary range (difference between highest and lowest) per department
C) Average salary
D) Error

✔ Correct Answer: B

Reason: The query calculates the difference between maximum and minimum salary for each department.

Tag: Normal

---

### Question 416
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Scenario-Based Questions
Difficulty: Medium

Question: A table stores student information with columns: StudentID, StudentName, CourseID, CourseName, InstructorName. What normalization issue exists?

A) No issues
B) Transitive dependency (CourseName and InstructorName depend on CourseID)
C) Partial dependency only
D) No dependencies

✔ Correct Answer: B

Reason: CourseName and InstructorName depend on CourseID, not StudentID, creating transitive dependencies violating 3NF.

Tag: Past Paper

---

### Question 417
Domain: Databases
Topic: Transaction Management
Subtopic: Scenario-Based Questions
Difficulty: Hard

Question: Transaction T1 reads data X, then T2 updates X and commits, then T1 reads X again. What problem occurs?

A) Dirty read
B) Non-repeatable read
C) Phantom read
D) No problem

✔ Correct Answer: B

Reason: T1 reads different values for X in the same transaction because T2 modified it, causing a non-repeatable read.

Tag: Past Paper

---

### Question 418
Domain: Databases
Topic: Concurrency Control
Subtopic: Scenario-Based Questions
Difficulty: Hard

Question: T1 holds a lock on record A and requests lock on B. T2 holds lock on B and requests lock on A. What situation is this?

A) No problem
B) Deadlock
C) Livelock
D) Starvation

✔ Correct Answer: B

Reason: This is a classic deadlock scenario where two transactions wait for each other's locks indefinitely.

Tag: Past Paper

---

### Question 419
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Scenario-Based Questions
Difficulty: Medium

Question: A table has 1 million rows. A query filters on a column with 3 distinct values. Should you create an index on this column?

A) Yes, always
B) Probably not, low selectivity makes index inefficient
C) Yes, definitely
D) Doesn't matter

✔ Correct Answer: B

Reason: With only 3 distinct values in 1 million rows, the index has very low selectivity and would likely be inefficient.

Tag: Normal

---

### Question 420
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Scenario-Based Questions
Difficulty: Hard

Question: A query joins three tables: A (10 rows), B (1000 rows), C (100 rows). What is the optimal join order?

A) A, B, C
B) B, C, A
C) C, B, A
D) Order doesn't matter

✔ Correct Answer: A

Reason: Starting with the smallest table (A) produces smaller intermediate results, reducing overall processing time.

Tag: Normal

---

### Question 421
Domain: Databases
Topic: Distributed Databases
Subtopic: Scenario-Based Questions
Difficulty: Hard

Question: A distributed database has sites in US and Europe. A transaction updates data in both sites. What protocol ensures atomicity?

A) One-phase commit
B) Two-phase commit
C) No protocol needed
D) Three-phase commit

✔ Correct Answer: B

Reason: Two-phase commit protocol ensures atomicity of distributed transactions across multiple sites.

Tag: Past Paper

---

### Question 422
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Scenario-Based Questions
Difficulty: Medium

Question: An application needs to store user sessions with automatic expiration. Which database type is most suitable?

A) Relational database
B) Key-value store with TTL support (like Redis)
C) Graph database
D) Document database

✔ Correct Answer: B

Reason: Key-value stores like Redis support Time-To-Live (TTL) for automatic expiration, ideal for session management.

Tag: Normal

---

### Question 423
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Scenario-Based Questions
Difficulty: Medium

Question: A retail company wants to analyze sales by product, store, and time. What schema is most appropriate?

A) 1NF schema
B) Star schema with Sales fact table and Product, Store, Time dimensions
C) Heap file
D) No schema

✔ Correct Answer: B

Reason: Star schema with a central fact table (Sales) and dimension tables (Product, Store, Time) is ideal for multi-dimensional analysis.

Tag: Normal

---

### Question 424
Domain: Databases
Topic: Database Security
Subtopic: Scenario-Based Questions
Difficulty: Medium

Question: A web application concatenates user input directly into SQL queries. What vulnerability exists?

A) No vulnerability
B) SQL injection
C) Buffer overflow
D) XSS only

✔ Correct Answer: B

Reason: Concatenating user input directly into SQL queries creates SQL injection vulnerabilities.

Tag: Past Paper

---

### Question 425
Domain: Databases
Topic: Recovery Management
Subtopic: Scenario-Based Questions
Difficulty: Medium

Question: A database crashes at 3 PM. The last full backup was at midnight, and transaction logs exist. What recovery approach should be used?

A) Restore full backup only
B) Restore full backup and apply transaction logs
C) No recovery possible
D) Start fresh

✔ Correct Answer: B

Reason: Restore the full backup from midnight and apply transaction logs to recover to the point of failure at 3 PM.

Tag: Normal

---

### Question 426
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Aggregate Functions
Difficulty: Easy

Question: What does COUNT(column_name) exclude?

A) All values
B) NULL values
C) Zero values
D) Negative values

✔ Correct Answer: B

Reason: COUNT(column_name) counts non-NULL values in the specified column.

Tag: Normal

---

### Question 427
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Aggregate Functions
Difficulty: Medium

Question: What is the difference between COUNT(*) and COUNT(column_name)?

A) No difference
B) COUNT(*) counts all rows, COUNT(column_name) counts non-NULL values
C) COUNT(*) is slower
D) COUNT(column_name) counts all rows

✔ Correct Answer: B

Reason: COUNT(*) counts all rows including those with NULLs, while COUNT(column_name) counts only non-NULL values in that column.

Tag: Normal

---

### Question 428
Domain: Databases
Topic: Advanced SQL
Subtopic: Partitioning
Difficulty: Hard

Question: What is table partitioning?

A) Deleting tables
B) Dividing a large table into smaller, manageable pieces
C) Joining tables
D) Encrypting tables

✔ Correct Answer: B

Reason: Table partitioning divides a large table into smaller physical pieces while maintaining a single logical table, improving performance and manageability.

Tag: Normal

---

### Question 429
Domain: Databases
Topic: Advanced SQL
Subtopic: Partition Types
Difficulty: Hard

Question: What is range partitioning?

A) Random partitioning
B) Partitioning based on ranges of values (e.g., date ranges)
C) No partitioning
D) Hash-based partitioning

✔ Correct Answer: B

Reason: Range partitioning divides data based on ranges of values, such as partitioning sales data by year or month.

Tag: Normal

---

### Question 430
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Constraints
Difficulty: Easy

Question: What does the CHECK constraint do?

A) Checks for duplicates
B) Ensures values in a column satisfy a specific condition
C) Checks foreign keys
D) Checks table size

✔ Correct Answer: B

Reason: CHECK constraint ensures that all values in a column satisfy a specific condition or expression.

Tag: Normal

---

### Question 431
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Constraints
Difficulty: Easy

Question: What does the DEFAULT constraint do?

A) Deletes default values
B) Provides a default value when no value is specified
C) Checks for defaults
D) Removes constraints

✔ Correct Answer: B

Reason: DEFAULT constraint provides a default value for a column when no value is explicitly specified during insertion.

Tag: Normal

---

### Question 432
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization Techniques
Difficulty: Medium

Question: What is a common denormalization technique?

A) Removing all redundancy
B) Adding redundant columns to avoid joins
C) Normalizing further
D) Deleting data

✔ Correct Answer: B

Reason: A common denormalization technique is adding redundant columns to tables to avoid expensive join operations.

Tag: Normal

---

### Question 433
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Properties
Difficulty: Easy

Question: Which ACID property ensures that committed changes are permanent?

A) Atomicity
B) Consistency
C) Isolation
D) Durability

✔ Correct Answer: D

Reason: Durability ensures that once a transaction is committed, its changes are permanent and survive system failures.

Tag: Past Paper

---

### Question 434
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Boundaries
Difficulty: Medium

Question: What marks the end of a successful transaction?

A) BEGIN
B) COMMIT
C) START
D) ROLLBACK

✔ Correct Answer: B

Reason: COMMIT marks the successful end of a transaction, making all changes permanent.

Tag: Normal

---

### Question 435
Domain: Databases
Topic: Concurrency Control
Subtopic: Locking Protocols
Difficulty: Hard

Question: What does strict two-phase locking require?

A) Locks can be released anytime
B) All exclusive locks held until transaction commits or aborts
C) No locks needed
D) Only shared locks

✔ Correct Answer: B

Reason: Strict 2PL requires that all exclusive locks be held until the transaction commits or aborts, preventing cascading rollbacks.

Tag: Past Paper

---

### Question 436
Domain: Databases
Topic: Concurrency Control
Subtopic: Locking Protocols
Difficulty: Hard

Question: What does rigorous two-phase locking require?

A) No locks
B) All locks (shared and exclusive) held until transaction commits or aborts
C) Only exclusive locks held
D) Locks released immediately

✔ Correct Answer: B

Reason: Rigorous 2PL requires that all locks (both shared and exclusive) be held until transaction commits or aborts.

Tag: Past Paper

---

### Question 437
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Techniques
Difficulty: Medium

Question: What is the purpose of a redo operation?

A) To undo changes
B) To reapply committed transaction changes after a crash
C) To delete data
D) To backup data

✔ Correct Answer: B

Reason: Redo operations reapply changes from committed transactions that may not have been written to disk before a crash.

Tag: Past Paper

---

### Question 438
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Techniques
Difficulty: Medium

Question: What is the purpose of an undo operation?

A) To reapply changes
B) To reverse changes from uncommitted transactions
C) To commit transactions
D) To backup data

✔ Correct Answer: B

Reason: Undo operations reverse changes made by transactions that were active but not committed at the time of a crash.

Tag: Past Paper

---

### Question 439
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Selection
Difficulty: Medium

Question: Which columns are good candidates for indexing?

A) Columns rarely used in queries
B) Columns frequently used in WHERE, JOIN, and ORDER BY clauses
C) All columns
D) No columns

✔ Correct Answer: B

Reason: Columns frequently used in WHERE, JOIN, and ORDER BY clauses benefit most from indexing.

Tag: Normal

---

### Question 440
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Overhead
Difficulty: Medium

Question: What is a disadvantage of having too many indexes?

A) Faster queries
B) Slower INSERT, UPDATE, DELETE operations and increased storage
C) No disadvantages
D) Better performance

✔ Correct Answer: B

Reason: Too many indexes slow down write operations (INSERT, UPDATE, DELETE) because all indexes must be maintained, and they consume storage space.

Tag: Normal

---

### Question 441
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Execution
Difficulty: Medium

Question: What is the first step in query processing?

A) Execution
B) Parsing and translation
C) Optimization
D) Result return

✔ Correct Answer: B

Reason: The first step is parsing the SQL query and translating it into an internal representation (like relational algebra).

Tag: Normal

---

### Question 442
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Execution Steps
Difficulty: Medium

Question: What happens during the optimization phase?

A) Query is executed
B) The best execution plan is selected
C) Results are returned
D) Query is parsed

✔ Correct Answer: B

Reason: During optimization, the query optimizer evaluates different execution plans and selects the most efficient one.

Tag: Normal

---

### Question 443
Domain: Databases
Topic: Database Security
Subtopic: Authentication
Difficulty: Easy

Question: What is database authentication?

A) Granting privileges
B) Verifying the identity of users accessing the database
C) Encrypting data
D) Backing up data

✔ Correct Answer: B

Reason: Authentication is the process of verifying the identity of users attempting to access the database.

Tag: Normal

---

### Question 444
Domain: Databases
Topic: Database Security
Subtopic: Authorization
Difficulty: Easy

Question: What is database authorization?

A) Verifying identity
B) Determining what authenticated users are allowed to do
C) Encrypting data
D) Deleting users

✔ Correct Answer: B

Reason: Authorization determines what operations authenticated users are permitted to perform on database objects.

Tag: Normal

---

### Question 445
Domain: Databases
Topic: Distributed Databases
Subtopic: Transparency Types
Difficulty: Medium

Question: What is fragmentation transparency?

A) Visible fragmentation
B) Users can access data without knowing it's fragmented
C) No fragmentation
D) Encrypted fragmentation

✔ Correct Answer: B

Reason: Fragmentation transparency allows users to access data without needing to know how it's fragmented across sites.

Tag: Normal

---

### Question 446
Domain: Databases
Topic: Distributed Databases
Subtopic: Transparency Types
Difficulty: Medium

Question: What is replication transparency?

A) Visible replication
B) Users can access data without knowing it's replicated
C) No replication
D) Manual replication

✔ Correct Answer: B

Reason: Replication transparency allows users to access data without needing to know that copies exist at multiple sites.

Tag: Normal

---

### Question 447
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Data Models
Difficulty: Easy

Question: What data structure does a graph database primarily use?

A) Tables
B) Nodes and edges (relationships)
C) Key-value pairs
D) Documents

✔ Correct Answer: B

Reason: Graph databases use nodes (entities) and edges (relationships) to represent and store data.

Tag: Normal

---

### Question 448
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Use Cases
Difficulty: Medium

Question: Which NoSQL database type is best for social network data?

A) Key-value store
B) Graph database
C) Column-family store
D) Document database

✔ Correct Answer: B

Reason: Graph databases excel at representing and querying highly connected data like social networks with users and relationships.

Tag: Normal

---

### Question 449
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Warehouse Characteristics
Difficulty: Easy

Question: What does "subject-oriented" mean in data warehousing?

A) Random organization
B) Organized around major subjects like customers or products
C) No organization
D) Time-oriented only

✔ Correct Answer: B

Reason: Subject-oriented means the data warehouse is organized around major business subjects (customers, products, sales) rather than applications.

Tag: Normal

---

### Question 450
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Warehouse Characteristics
Difficulty: Easy

Question: What does "non-volatile" mean in data warehousing?

A) Data changes frequently
B) Data is stable and not updated or deleted regularly
C) Data is deleted daily
D) Data is temporary

✔ Correct Answer: B

Reason: Non-volatile means data in a warehouse is stable and not updated or deleted in the same way as operational databases.

Tag: Normal

---

### Question 451
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Set Operations
Difficulty: Medium

Question: What is required for UNION operations to work?

A) Different number of columns
B) Same number of columns with compatible data types
C) Different data types
D) No requirements

✔ Correct Answer: B

Reason: UNION requires that both SELECT statements have the same number of columns with compatible data types.

Tag: Normal

---

### Question 452
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Nested Queries
Difficulty: Medium

Question: What is a correlated subquery?

A) Independent subquery
B) Subquery that references columns from the outer query
C) Fast subquery
D) Deleted subquery

✔ Correct Answer: B

Reason: A correlated subquery references columns from the outer query and is evaluated once for each row of the outer query.

Tag: Past Paper

---

### Question 453
Domain: Databases
Topic: Advanced SQL
Subtopic: Transaction Control
Difficulty: Easy

Question: What does SET TRANSACTION ISOLATION LEVEL do?

A) Deletes transactions
B) Sets the isolation level for the current transaction
C) Commits transactions
D) Rolls back transactions

✔ Correct Answer: B

Reason: SET TRANSACTION ISOLATION LEVEL specifies the isolation level (Read Uncommitted, Read Committed, etc.) for the current transaction.

Tag: Normal

---

### Question 454
Domain: Databases
Topic: Advanced SQL
Subtopic: Sequences
Difficulty: Medium

Question: What is a sequence in databases?

A) A table
B) A database object that generates sequential numbers
C) A query
D) An index

✔ Correct Answer: B

Reason: A sequence is a database object that automatically generates sequential numeric values, often used for primary keys.

Tag: Normal

---

### Question 455
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Expression Equivalence
Difficulty: Hard

Question: Which operations are commutative in relational algebra?

A) None
B) Selection, Union, Intersection, Join
C) Only Selection
D) Only Join

✔ Correct Answer: B

Reason: Selection, Union, Intersection, and Join operations are commutative (order of operands doesn't matter).

Tag: Past Paper

---

### Question 456
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Schema Design
Difficulty: Medium

Question: What is a schema in database design?

A) A backup
B) The logical structure and organization of the database
C) A query
D) An index

✔ Correct Answer: B

Reason: A schema defines the logical structure and organization of the database, including tables, columns, relationships, and constraints.

Tag: Normal

---

### Question 457
Domain: Databases
Topic: Database Design & Normalization
Subtopic: ER to Relational Mapping
Difficulty: Hard

Question: How is a many-to-many relationship typically implemented in relational databases?

A) Single table
B) Junction (bridge) table with foreign keys to both entities
C) Two tables only
D) Cannot be implemented

✔ Correct Answer: B

Reason: Many-to-many relationships require a junction table containing foreign keys referencing both related entities.

Tag: Past Paper

---

### Question 458
Domain: Databases
Topic: Transaction Management
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is the coordinator's role in two-phase commit?

A) No role
B) Coordinates the commit process across all participating sites
C) Only stores data
D) Deletes data

✔ Correct Answer: B

Reason: The coordinator manages the two-phase commit protocol, ensuring all sites either commit or abort the transaction.

Tag: Normal

---

### Question 459
Domain: Databases
Topic: Concurrency Control
Subtopic: Timestamp Protocols
Difficulty: Hard

Question: How does timestamp ordering prevent conflicts?

A) Using locks
B) Assigning timestamps and ensuring operations execute in timestamp order
C) Random ordering
D) No prevention

✔ Correct Answer: B

Reason: Timestamp ordering assigns unique timestamps to transactions and ensures operations execute in timestamp order to maintain serializability.

Tag: Past Paper

---

### Question 460
Domain: Databases
Topic: Recovery Management
Subtopic: Checkpointing
Difficulty: Medium

Question: How does checkpointing improve recovery time?

A) It doesn't
B) Reduces the amount of log that needs to be processed during recovery
C) Increases recovery time
D) Deletes logs

✔ Correct Answer: B

Reason: Checkpointing marks a point where all changes are saved to disk, so recovery only needs to process logs after the last checkpoint.

Tag: Normal

---

### Question 461
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Statistics
Difficulty: Medium

Question: Why should index statistics be updated regularly?

A) They shouldn't be
B) To ensure the optimizer makes accurate cost estimates
C) To delete indexes
D) To slow down queries

✔ Correct Answer: B

Reason: Updated statistics help the query optimizer make accurate cost estimates and choose optimal execution plans.

Tag: Normal

---

### Question 462
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Access Methods
Difficulty: Medium

Question: When is a table scan more efficient than an index scan?

A) Never
B) When retrieving a large percentage of rows
C) Always
D) When table is empty

✔ Correct Answer: B

Reason: When retrieving a large percentage of rows (typically >20-30%), a table scan can be more efficient than multiple index lookups.

Tag: Normal

---

### Question 463
Domain: Databases
Topic: Database Security
Subtopic: Encryption at Rest
Difficulty: Easy

Question: What does encryption at rest protect?

A) Data in transit
B) Data stored on disk
C) Data in memory
D) Network traffic

✔ Correct Answer: B

Reason: Encryption at rest protects data stored on physical media (disks) from unauthorized access if the storage is compromised.

Tag: Normal

---

### Question 464
Domain: Databases
Topic: Database Security
Subtopic: Encryption in Transit
Difficulty: Easy

Question: What does encryption in transit protect?

A) Data on disk
B) Data being transmitted over networks
C) Backup data
D) Deleted data

✔ Correct Answer: B

Reason: Encryption in transit protects data while it's being transmitted over networks, preventing interception and eavesdropping.

Tag: Normal

---

### Question 465
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Query Execution
Difficulty: Hard

Question: What is the main cost factor in distributed query execution?

A) CPU time
B) Data transfer over the network
C) Memory usage
D) Disk space

✔ Correct Answer: B

Reason: Network data transfer is typically the most expensive operation in distributed query execution, often dominating total cost.

Tag: Normal

---

### Question 466
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Polyglot Persistence
Difficulty: Medium

Question: What is polyglot persistence?

A) Using one database type
B) Using different database technologies for different data storage needs
C) No persistence
D) Only relational databases

✔ Correct Answer: B

Reason: Polyglot persistence uses different database technologies (relational, document, graph, etc.) for different parts of an application based on specific needs.

Tag: Normal

---

### Question 467
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Quality
Difficulty: Easy

Question: What is data cleansing?

A) Deleting all data
B) Detecting and correcting corrupt or inaccurate data
C) Backing up data
D) Encrypting data

✔ Correct Answer: B

Reason: Data cleansing (or data scrubbing) is the process of detecting and correcting corrupt, inaccurate, or inconsistent data.

Tag: Normal

---

### Question 468
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Integration
Difficulty: Medium

Question: What is data integration in data warehousing?

A) Deleting data
B) Combining data from different sources into a unified view
C) Separating data
D) Encrypting data

✔ Correct Answer: B

Reason: Data integration combines data from disparate sources into a unified, consistent view for analysis.

Tag: Normal

---

### Question 469
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Transaction Isolation
Difficulty: Medium

Question: Which isolation level has the best performance but least consistency?

A) Serializable
B) Read Uncommitted
C) Repeatable Read
D) Read Committed

✔ Correct Answer: B

Reason: Read Uncommitted provides the best performance but allows dirty reads, offering the least consistency guarantees.

Tag: Normal

---

### Question 470
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Data Types
Difficulty: Easy

Question: Which SQL data type is used for storing large text?

A) INT
B) VARCHAR(MAX) or TEXT
C) DATE
D) BOOLEAN

✔ Correct Answer: B

Reason: VARCHAR(MAX), TEXT, or CLOB data types are used for storing large amounts of text data.

Tag: Normal

---

### Question 471
Domain: Databases
Topic: Advanced SQL
Subtopic: Execution Plans
Difficulty: Hard

Question: What is an execution plan?

A) A backup plan
B) A detailed description of how the database will execute a query
C) A security plan
D) A deletion plan

✔ Correct Answer: B

Reason: An execution plan shows the detailed steps the database engine will take to execute a query, including access methods and join strategies.

Tag: Normal

---

### Question 472
Domain: Databases
Topic: Advanced SQL
Subtopic: Query Performance
Difficulty: Medium

Question: What is a covering index?

A) An index that covers the table
B) An index that includes all columns needed by a query
C) A deleted index
D) A temporary index

✔ Correct Answer: B

Reason: A covering index includes all columns needed by a query, allowing the query to be satisfied entirely from the index without accessing the table.

Tag: Normal

---

### Question 473
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Integrity Constraints
Difficulty: Easy

Question: What happens when you try to delete a row referenced by a foreign key with ON DELETE CASCADE?

A) Deletion is prevented
B) Referenced rows in child tables are automatically deleted
C) Error occurs
D) Nothing happens

✔ Correct Answer: B

Reason: ON DELETE CASCADE automatically deletes all rows in child tables that reference the deleted row in the parent table.

Tag: Normal

---

### Question 474
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Integrity Constraints
Difficulty: Medium

Question: What does ON UPDATE RESTRICT do?

A) Allows updates
B) Prevents updates to primary key if foreign keys reference it
C) Cascades updates
D) Deletes rows

✔ Correct Answer: B

Reason: ON UPDATE RESTRICT prevents updates to a primary key value if foreign keys in other tables reference it.

Tag: Normal

---

### Question 475
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Patterns
Difficulty: Medium

Question: What is a lookup table?

A) A temporary table
B) A table containing reference data like country codes or status values
C) A deleted table
D) A backup table

✔ Correct Answer: B

Reason: A lookup table stores reference data (like country codes, status values) that other tables reference via foreign keys.

Tag: Normal

---

### Question 476
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Logging
Difficulty: Medium

Question: What is write-ahead logging (WAL)?

A) Writing data before logging
B) Writing log records before writing data pages to disk
C) No logging
D) Delayed logging

✔ Correct Answer: B

Reason: WAL ensures log records are written to stable storage before the corresponding data pages, enabling recovery.

Tag: Past Paper

---

### Question 477
Domain: Databases
Topic: Concurrency Control
Subtopic: Optimistic vs Pessimistic
Difficulty: Medium

Question: When is optimistic concurrency control most effective?

A) High conflict scenarios
B) Low conflict scenarios with mostly read operations
C) Never effective
D) Always effective

✔ Correct Answer: B

Reason: Optimistic concurrency control works best when conflicts are rare, avoiding locking overhead for mostly read operations.

Tag: Normal

---

### Question 478
Domain: Databases
Topic: Recovery Management
Subtopic: Backup Strategies
Difficulty: Easy

Question: What is the 3-2-1 backup rule?

A) 3 backups, 2 media types, 1 offsite
B) 3 databases, 2 servers, 1 backup
C) No rule
D) 3 servers only

✔ Correct Answer: A

Reason: The 3-2-1 rule recommends keeping 3 copies of data, on 2 different media types, with 1 copy offsite.

Tag: Normal

---

### Question 479
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Types
Difficulty: Hard

Question: What is a partial index?

A) An incomplete index
B) An index on a subset of rows meeting a condition
C) A deleted index
D) A temporary index

✔ Correct Answer: B

Reason: A partial index (or filtered index) indexes only rows that meet a specified condition, reducing index size.

Tag: Normal

---

### Question 480
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Optimization Techniques
Difficulty: Hard

Question: What is query rewriting?

A) Correcting syntax
B) Transforming a query into an equivalent but more efficient form
C) Deleting queries
D) Encrypting queries

✔ Correct Answer: B

Reason: Query rewriting transforms a query into an equivalent form that can be executed more efficiently using algebraic rules.

Tag: Normal

---

### Question 481
Domain: Databases
Topic: Database Security
Subtopic: Access Patterns
Difficulty: Medium

Question: What is anomaly detection in database security?

A) Finding bugs
B) Identifying unusual access patterns that may indicate security threats
C) Deleting anomalies
D) Creating anomalies

✔ Correct Answer: B

Reason: Anomaly detection identifies unusual access patterns or behaviors that deviate from normal usage, potentially indicating security threats.

Tag: Normal

---

### Question 482
Domain: Databases
Topic: Distributed Databases
Subtopic: Consistency Models
Difficulty: Hard

Question: What is eventual consistency?

A) Immediate consistency
B) System will become consistent over time if no new updates
C) Never consistent
D) Always consistent

✔ Correct Answer: B

Reason: Eventual consistency guarantees that if no new updates are made, all replicas will eventually converge to the same value.

Tag: Normal

---

### Question 483
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Database Selection
Difficulty: Medium

Question: When should you choose a document database?

A) For highly structured data
B) For semi-structured data with varying schemas
C) For graph data only
D) Never

✔ Correct Answer: B

Reason: Document databases are ideal for semi-structured data with varying schemas, like JSON documents with different fields.

Tag: Normal

---

### Question 484
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Transformation
Difficulty: Medium

Question: What is data transformation in ETL?

A) Deleting data
B) Converting data from source format to warehouse format
C) Backing up data
D) Encrypting data

✔ Correct Answer: B

Reason: Data transformation converts data from source system formats to the format required by the data warehouse, including cleaning and standardization.

Tag: Normal

---

### Question 485
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Performance Tips
Difficulty: Medium

Question: Why should you avoid SELECT * in production queries?

A) It's faster
B) It retrieves unnecessary columns, wasting resources
C) It's required
D) No reason

✔ Correct Answer: B

Reason: SELECT * retrieves all columns including unnecessary ones, wasting network bandwidth, memory, and processing time.

Tag: Normal

---

### Question 486
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT name FROM employees 
WHERE employee_id NOT IN (SELECT manager_id FROM employees WHERE manager_id IS NOT NULL);
```

A) All employees
B) Employees who are not managers
C) Only managers
D) Error

✔ Correct Answer: B

Reason: The query selects employees whose IDs don't appear in the manager_id column, i.e., employees who are not managers.

Tag: Normal

---

### Question 487
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this window function calculate?
```sql
SELECT name, salary,
SUM(salary) OVER (ORDER BY salary) as running_total
FROM employees;
```

A) Total salary
B) Running total of salaries ordered by salary amount
C) Average salary
D) Error

✔ Correct Answer: B

Reason: The window function calculates a running total of salaries, accumulating as it processes rows ordered by salary.

Tag: Normal

---

### Question 488
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Query Equivalence
Difficulty: Hard

Question: Are these queries equivalent?
Query 1: σ(A=5)(R ⋈ S)
Query 2: σ(A=5)(R) ⋈ S

A) No
B) Yes, if A is an attribute of R
C) Never equivalent
D) Always equivalent

✔ Correct Answer: B

Reason: If A is an attribute of R, pushing the selection before the join (Query 2) is equivalent and more efficient.

Tag: Past Paper

---

### Question 489
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Decisions
Difficulty: Medium

Question: When might you intentionally violate normalization rules?

A) Never
B) When read performance is critical and redundancy is acceptable
C) Always
D) When data is small

✔ Correct Answer: B

Reason: Intentional denormalization may be justified when read performance is critical and the costs of redundancy are acceptable.

Tag: Normal

---

### Question 490
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Design
Difficulty: Medium

Question: Why should transactions be kept short?

A) They shouldn't be
B) To reduce lock contention and improve concurrency
C) To increase lock time
D) No reason

✔ Correct Answer: B

Reason: Short transactions reduce the time locks are held, decreasing lock contention and improving overall system concurrency.

Tag: Normal

---

### Question 491
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Granularity Trade-offs
Difficulty: Medium

Question: What is the trade-off with fine-grained locking?

A) No trade-offs
B) Higher concurrency but more locking overhead
C) Lower concurrency
D) No overhead

✔ Correct Answer: B

Reason: Fine-grained locking allows higher concurrency but requires managing more locks, increasing overhead.

Tag: Normal

---

### Question 492
Domain: Databases
Topic: Recovery Management
Subtopic: Disaster Recovery
Difficulty: Easy

Question: What is a disaster recovery plan?

A) A backup schedule
B) A documented process for recovering from catastrophic failures
C) A delete plan
D) A security plan

✔ Correct Answer: B

Reason: A disaster recovery plan documents procedures for recovering database systems and data after catastrophic failures.

Tag: Normal

---

### Question 493
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Maintenance
Difficulty: Medium

Question: When should indexes be rebuilt?

A) Never
B) When fragmentation is high or statistics are outdated
C) Daily
D) Hourly

✔ Correct Answer: B

Reason: Indexes should be rebuilt when fragmentation reaches high levels or when statistics become significantly outdated.

Tag: Normal

---

### Question 494
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Subquery Optimization
Difficulty: Hard

Question: What is subquery flattening?

A) Deleting subqueries
B) Converting subqueries to joins for better performance
C) Encrypting subqueries
D) No optimization

✔ Correct Answer: B

Reason: Subquery flattening transforms subqueries into equivalent joins, often resulting in better performance.

Tag: Normal

---

### Question 495
Domain: Databases
Topic: Database Security
Subtopic: Security Best Practices
Difficulty: Easy

Question: Why should database accounts have strong passwords?

A) They shouldn't
B) To prevent unauthorized access through password guessing or brute force
C) For aesthetics
D) No reason

✔ Correct Answer: B

Reason: Strong passwords prevent unauthorized access by making password guessing and brute-force attacks impractical.

Tag: Normal

---

### Question 496
Domain: Databases
Topic: Distributed Databases
Subtopic: Network Partitions
Difficulty: Hard

Question: What is a network partition?

A) Disk partition
B) Network failure that splits the system into isolated groups
C) Data partition
D) No partition

✔ Correct Answer: B

Reason: A network partition is a failure that divides the distributed system into isolated groups that cannot communicate.

Tag: Normal

---

### Question 497
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Trade-offs
Difficulty: Medium

Question: What does "AP" mean in CAP theorem?

A) Available and Partition-tolerant
B) Atomic and Persistent
C) Accurate and Perfect
D) Automatic and Parallel

✔ Correct Answer: A

Reason: AP systems prioritize Availability and Partition tolerance, potentially sacrificing Consistency during network partitions.

Tag: Normal

---

### Question 498
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining Techniques
Difficulty: Easy

Question: What is classification in data mining?

A) Organizing files
B) Predicting categorical class labels for data instances
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Classification is a data mining technique that predicts categorical class labels (like spam/not spam) for data instances.

Tag: Normal

---

### Question 499
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining Techniques
Difficulty: Easy

Question: What is clustering in data mining?

A) Database clustering
B) Grouping similar data objects together
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Clustering groups similar data objects together based on their characteristics, without predefined categories.

Tag: Normal

---

### Question 500
Domain: Databases
Topic: Introduction to Database Systems
Subtopic: Database Evolution
Difficulty: Easy

Question: What advantage do relational databases have over hierarchical databases?

A) No advantages
B) Flexibility in querying and data independence
C) More complex
D) Slower performance

✔ Correct Answer: B

Reason: Relational databases provide greater flexibility in querying data and better data independence compared to hierarchical databases.

Tag: Normal

---

**End of Batch 05**

---

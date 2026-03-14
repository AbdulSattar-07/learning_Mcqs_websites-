# Databases MCQ Bank - Batch 06

## Questions 501-600

---

### Question 501
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT department, COUNT(*) as emp_count
FROM employees
GROUP BY department
ORDER BY emp_count DESC
LIMIT 3;
```

A) All departments
B) Top 3 departments with most employees
C) Bottom 3 departments
D) Error

✔ Correct Answer: B

Reason: The query groups by department, counts employees, orders by count descending, and limits to top 3 departments.

Tag: Normal

---

### Question 502
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
SELECT * FROM orders WHERE order_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);
```

A) Selects all orders
B) Selects orders from the last 30 days
C) Deletes old orders
D) Error

✔ Correct Answer: B

Reason: The query selects orders where order_date is within the last 30 days from the current date.

Tag: Normal

---

### Question 503
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What will this query return?
```sql
SELECT e1.name as Employee, e2.name as Manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

A) Only employees with managers
B) All employees with their manager names (NULL if no manager)
C) Only managers
D) Error

✔ Correct Answer: B

Reason: This self-join with LEFT JOIN returns all employees and their managers' names, showing NULL for employees without managers.

Tag: Past Paper

---

### Question 504
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query calculate?
```sql
SELECT product_id, 
       SUM(quantity * price) as total_revenue
FROM order_items
GROUP BY product_id
HAVING SUM(quantity * price) > 10000;
```

A) All products
B) Products with total revenue exceeding 10000
C) Products with price > 10000
D) Error

✔ Correct Answer: B

Reason: The query calculates total revenue per product and filters to show only products with revenue exceeding 10000.

Tag: Normal

---

### Question 505
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this recursive CTE do?
```sql
WITH RECURSIVE subordinates AS (
  SELECT employee_id, name, manager_id FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.name, e.manager_id 
  FROM employees e
  INNER JOIN subordinates s ON e.manager_id = s.employee_id
)
SELECT * FROM subordinates;
```

A) Selects one employee
B) Builds organizational hierarchy starting from top-level managers
C) Deletes employees
D) Error

✔ Correct Answer: B

Reason: This recursive CTE builds the complete organizational hierarchy starting from employees with no manager (top level).

Tag: Past Paper

---

### Question 506
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the output of this query if there are NULL values in the salary column?
```sql
SELECT AVG(salary) FROM employees;
```

A) Error
B) Average of non-NULL salaries
C) Average including NULLs as zero
D) NULL

✔ Correct Answer: B

Reason: AVG() ignores NULL values and calculates the average of only non-NULL values.

Tag: Normal

---

### Question 507
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT name FROM employees
WHERE employee_id IN (
  SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL
);
```

A) All employees
B) Employees who are managers
C) Employees who are not managers
D) Error

✔ Correct Answer: B

Reason: The subquery finds all manager IDs, and the outer query selects employees whose IDs match those manager IDs.

Tag: Normal

---

### Question 508
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does the PARTITION BY clause do in this query?
```sql
SELECT name, department, salary,
RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;
```

A) Deletes partitions
B) Ranks employees within each department separately
C) Ranks all employees together
D) Error

✔ Correct Answer: B

Reason: PARTITION BY divides the result set into partitions (by department), and RANK() is applied separately within each partition.

Tag: Normal

---

### Question 509
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What will this query do?
```sql
INSERT INTO archive_orders 
SELECT * FROM orders WHERE order_date < '2020-01-01';
```

A) Deletes orders
B) Copies old orders to archive_orders table
C) Updates orders
D) Error

✔ Correct Answer: B

Reason: INSERT INTO ... SELECT copies rows from orders table to archive_orders table based on the condition.

Tag: Normal

---

### Question 510
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT c.customer_name, COALESCE(SUM(o.amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_name;
```

A) Only customers with orders
B) All customers with total spent (0 if no orders)
C) Only orders
D) Error

✔ Correct Answer: B

Reason: LEFT JOIN includes all customers, and COALESCE returns 0 for customers with no orders (where SUM would be NULL).

Tag: Normal

---

### Question 511
Domain: Databases
Topic: Database System Architecture
Subtopic: Buffer Management
Difficulty: Medium

Question: What is a buffer pool?

A) A swimming pool
B) Memory area for caching disk pages
C) A backup storage
D) A deleted pool

✔ Correct Answer: B

Reason: A buffer pool is a memory area used to cache frequently accessed disk pages, reducing disk I/O.

Tag: Normal

---

### Question 512
Domain: Databases
Topic: Database System Architecture
Subtopic: Buffer Replacement
Difficulty: Hard

Question: What is the LRU buffer replacement policy?

A) Most recently used pages are replaced
B) Least recently used pages are replaced
C) Random replacement
D) No replacement

✔ Correct Answer: B

Reason: LRU (Least Recently Used) replaces the page that hasn't been accessed for the longest time.

Tag: Normal

---

### Question 513
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relation Properties
Difficulty: Medium

Question: Can a relation have duplicate tuples?

A) Yes, always
B) No, by definition relations contain unique tuples
C) Sometimes
D) Only in special cases

✔ Correct Answer: B

Reason: By definition, a relation is a set of tuples, and sets cannot contain duplicates.

Tag: Past Paper

---

### Question 514
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Attribute Ordering
Difficulty: Easy

Question: Does the order of attributes matter in a relation?

A) Yes, always
B) No, attribute order is insignificant in the relational model
C) Sometimes
D) Only for primary keys

✔ Correct Answer: B

Reason: In the relational model, the order of attributes (columns) is insignificant; attributes are accessed by name.

Tag: Past Paper

---

### Question 515
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization Process
Difficulty: Medium

Question: What is the first step in normalization?

A) Identify candidate keys
B) Eliminate repeating groups to achieve 1NF
C) Remove transitive dependencies
D) Create indexes

✔ Correct Answer: B

Reason: The first step in normalization is eliminating repeating groups and ensuring atomic values to achieve First Normal Form (1NF).

Tag: Past Paper

---

### Question 516
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization Benefits
Difficulty: Easy

Question: Which anomaly does normalization help prevent?

A) Network anomalies
B) Update, insertion, and deletion anomalies
C) Performance anomalies
D) Security anomalies

✔ Correct Answer: B

Reason: Normalization helps prevent update, insertion, and deletion anomalies caused by data redundancy.

Tag: Normal

---

### Question 517
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Conflicts
Difficulty: Hard

Question: What type of conflict occurs when T1 reads X, then T2 writes X?

A) Write-Write conflict
B) Read-Write conflict
C) Write-Read conflict
D) No conflict

✔ Correct Answer: B

Reason: This is a Read-Write (RW) conflict where T2's write affects T1's subsequent reads of X.

Tag: Past Paper

---

### Question 518
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Properties
Difficulty: Medium

Question: Which property ensures that either all operations of a transaction are executed or none are?

A) Consistency
B) Atomicity
C) Isolation
D) Durability

✔ Correct Answer: B

Reason: Atomicity ensures that a transaction is an all-or-nothing proposition.

Tag: Past Paper

---

### Question 519
Domain: Databases
Topic: Concurrency Control
Subtopic: Serializability Testing
Difficulty: Hard

Question: How can you test if a schedule is conflict serializable?

A) Random testing
B) Construct a precedence graph and check for cycles
C) Execute and observe
D) No testing possible

✔ Correct Answer: B

Reason: A schedule is conflict serializable if its precedence graph is acyclic.

Tag: Past Paper

---

### Question 520
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Modes
Difficulty: Medium

Question: What is an intent lock?

A) A strong lock
B) A lock indicating intention to acquire finer-grained locks
C) A deleted lock
D) A temporary lock

✔ Correct Answer: B

Reason: Intent locks indicate a transaction's intention to acquire locks at a finer granularity level.

Tag: Normal

---

### Question 521
Domain: Databases
Topic: Recovery Management
Subtopic: Log Records
Difficulty: Medium

Question: What information does a log record typically contain?

A) Only transaction ID
B) Transaction ID, operation type, data item, old value, new value
C) Only timestamps
D) Only user information

✔ Correct Answer: B

Reason: Log records contain transaction ID, operation type, affected data item, and before/after values for recovery.

Tag: Normal

---

### Question 522
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Algorithms
Difficulty: Hard

Question: What is the difference between undo and redo recovery?

A) No difference
B) Undo reverses uncommitted changes, redo reapplies committed changes
C) Undo is faster
D) Redo is not used

✔ Correct Answer: B

Reason: Undo reverses changes from uncommitted transactions, while redo reapplies changes from committed transactions.

Tag: Past Paper

---

### Question 523
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Primary Index
Difficulty: Medium

Question: What is a primary index?

A) The first index created
B) An index on the ordering key field of a sequentially ordered file
C) Any index
D) A deleted index

✔ Correct Answer: B

Reason: A primary index is built on the ordering key field of a file that is physically ordered by that field.

Tag: Past Paper

---

### Question 524
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Secondary Index
Difficulty: Medium

Question: What is a secondary index?

A) The second index created
B) An index on a non-ordering field
C) A backup index
D) A temporary index

✔ Correct Answer: B

Reason: A secondary index is an index on a field that is not used for physical ordering of the file.

Tag: Past Paper

---

### Question 525
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Selection Operation
Difficulty: Medium

Question: Which access method is most efficient for a selection with equality condition on a key attribute?

A) Linear search
B) Index scan using a key index
C) Full table scan
D) Random access

✔ Correct Answer: B

Reason: Using an index on the key attribute provides direct access, making it the most efficient method.

Tag: Normal

---

### Question 526
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: What is the main advantage of hash join?

A) Works on unsorted data
B) Efficient for large tables with equality join conditions
C) Requires less memory
D) Always fastest

✔ Correct Answer: B

Reason: Hash join is efficient for large tables with equality join conditions, building a hash table on one relation.

Tag: Normal

---

### Question 527
Domain: Databases
Topic: Database Security
Subtopic: View-Based Security
Difficulty: Medium

Question: How do views enhance security?

A) They don't
B) By restricting access to specific rows and columns
C) By encrypting all data
D) By deleting sensitive data

✔ Correct Answer: B

Reason: Views can restrict user access to specific rows and columns, hiding sensitive data while allowing access to authorized information.

Tag: Normal

---

### Question 528
Domain: Databases
Topic: Database Security
Subtopic: SQL Injection Prevention
Difficulty: Medium

Question: Which practice helps prevent SQL injection?

A) Using dynamic SQL
B) Using parameterized queries and input validation
C) Concatenating user input
D) Disabling security

✔ Correct Answer: B

Reason: Parameterized queries and input validation prevent SQL injection by separating SQL code from user data.

Tag: Past Paper

---

### Question 529
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Distribution
Difficulty: Medium

Question: What is horizontal fragmentation?

A) Splitting by columns
B) Splitting by rows based on predicates
C) No fragmentation
D) Random splitting

✔ Correct Answer: B

Reason: Horizontal fragmentation divides a relation into subsets of rows based on selection predicates.

Tag: Normal

---

### Question 530
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Distribution
Difficulty: Medium

Question: What is vertical fragmentation?

A) Splitting by rows
B) Splitting by columns (attributes)
C) No fragmentation
D) Random splitting

✔ Correct Answer: B

Reason: Vertical fragmentation divides a relation by columns, with each fragment containing a subset of attributes plus the primary key.

Tag: Normal

---

### Question 531
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: MongoDB
Difficulty: Easy

Question: What data format does MongoDB use?

A) XML
B) BSON (Binary JSON)
C) CSV
D) Plain text

✔ Correct Answer: B

Reason: MongoDB stores data in BSON (Binary JSON) format, which extends JSON with additional data types.

Tag: Normal

---

### Question 532
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Cassandra
Difficulty: Medium

Question: What consistency level in Cassandra requires all replicas to respond?

A) ONE
B) QUORUM
C) ALL
D) ANY

✔ Correct Answer: C

Reason: ALL consistency level requires all replica nodes to respond before the operation is considered successful.

Tag: Normal

---

### Question 533
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Dimensional Modeling
Difficulty: Easy

Question: What is dimensional modeling?

A) 3D modeling
B) A design technique for data warehouses using facts and dimensions
C) A programming technique
D) A backup technique

✔ Correct Answer: B

Reason: Dimensional modeling is a design technique for data warehouses that uses fact tables and dimension tables.

Tag: Normal

---

### Question 534
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Fact vs Dimension
Difficulty: Easy

Question: What is the main difference between fact and dimension tables?

A) No difference
B) Facts contain measures, dimensions contain descriptive attributes
C) Facts are smaller
D) Dimensions contain numbers only

✔ Correct Answer: B

Reason: Fact tables contain quantitative measures for analysis, while dimension tables contain descriptive attributes for context.

Tag: Normal

---

### Question 535
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Subquery Performance
Difficulty: Medium

Question: When might a correlated subquery be inefficient?

A) Never
B) When the outer query returns many rows
C) Always efficient
D) When outer query is small

✔ Correct Answer: B

Reason: Correlated subqueries execute once for each row in the outer query, becoming inefficient with many outer rows.

Tag: Normal

---

### Question 536
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: NULL Handling
Difficulty: Medium

Question: What is the result of (NULL OR TRUE)?

A) NULL
B) TRUE
C) FALSE
D) Error

✔ Correct Answer: B

Reason: In three-valued logic, (NULL OR TRUE) evaluates to TRUE because TRUE makes the entire expression TRUE regardless of the other operand.

Tag: Past Paper

---

### Question 537
Domain: Databases
Topic: Advanced SQL
Subtopic: Transactions
Difficulty: Easy

Question: What command explicitly starts a transaction?

A) START or BEGIN TRANSACTION
B) OPEN TRANSACTION
C) CREATE TRANSACTION
D) INIT TRANSACTION

✔ Correct Answer: A

Reason: START TRANSACTION or BEGIN TRANSACTION explicitly starts a new transaction.

Tag: Normal

---

### Question 538
Domain: Databases
Topic: Advanced SQL
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level prevents phantom reads?

A) Read Uncommitted
B) Read Committed
C) Repeatable Read
D) Serializable

✔ Correct Answer: D

Reason: Only Serializable isolation level prevents phantom reads by locking ranges of data.

Tag: Past Paper

---

### Question 539
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Relational Completeness
Difficulty: Hard

Question: What does it mean for a query language to be relationally complete?

A) It has all features
B) It can express all queries expressible in relational algebra
C) It's perfect
D) It has no bugs

✔ Correct Answer: B

Reason: A relationally complete language can express any query that can be expressed in relational algebra.

Tag: Past Paper

---

### Question 540
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Decomposition
Difficulty: Hard

Question: What is a lossless join decomposition?

A) A decomposition that loses data
B) A decomposition where the original relation can be reconstructed by joining
C) A fast decomposition
D) A deleted decomposition

✔ Correct Answer: B

Reason: Lossless join decomposition ensures the original relation can be reconstructed by joining the decomposed relations without spurious tuples.

Tag: Past Paper

---

### Question 541
Domain: Databases
Topic: Transaction Management
Subtopic: Concurrency Issues
Difficulty: Medium

Question: What is the lost update problem?

A) Lost data
B) Two transactions update the same data, and one update is lost
C) Slow updates
D) No problem

✔ Correct Answer: B

Reason: Lost update occurs when two transactions read and update the same data, and one transaction's update overwrites the other's.

Tag: Past Paper

---

### Question 542
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Handling
Difficulty: Medium

Question: What are the two main approaches to handling deadlocks?

A) Ignore them
B) Prevention and detection/recovery
C) Only prevention
D) Only detection

✔ Correct Answer: B

Reason: Deadlocks can be handled through prevention (avoiding conditions that lead to deadlock) or detection and recovery (detecting and breaking deadlocks).

Tag: Normal

---

### Question 543
Domain: Databases
Topic: Recovery Management
Subtopic: Transaction States
Difficulty: Medium

Question: What state is a transaction in after it has executed its final statement?

A) Active
B) Partially Committed
C) Committed
D) Failed

✔ Correct Answer: B

Reason: After executing the final statement, a transaction enters the Partially Committed state before being fully Committed.

Tag: Past Paper

---

### Question 544
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Multilevel Indexes
Difficulty: Hard

Question: Why are multilevel indexes used?

A) They're not used
B) To reduce the number of disk accesses for large indexes
C) To increase disk accesses
D) For decoration

✔ Correct Answer: B

Reason: Multilevel indexes create an index on the index, reducing the number of disk accesses needed to find entries.

Tag: Normal

---

### Question 545
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Cost Estimation
Difficulty: Hard

Question: What factors affect the cost of a query execution plan?

A) Only CPU time
B) Disk I/O, CPU time, memory usage, and network transfer
C) Only memory
D) Only network

✔ Correct Answer: B

Reason: Query cost includes disk I/O, CPU processing, memory usage, and (in distributed systems) network data transfer.

Tag: Normal

---

### Question 546
Domain: Databases
Topic: Database Security
Subtopic: Privilege Management
Difficulty: Easy

Question: What does the WITH GRANT OPTION allow?

A) Nothing special
B) The grantee to grant the privilege to others
C) Deleting privileges
D) Revoking all privileges

✔ Correct Answer: B

Reason: WITH GRANT OPTION allows the user receiving the privilege to grant that same privilege to other users.

Tag: Normal

---

### Question 547
Domain: Databases
Topic: Distributed Databases
Subtopic: Commit Protocols
Difficulty: Hard

Question: What are the two phases in two-phase commit?

A) Read and Write
B) Prepare (voting) and Commit (decision)
C) Lock and Unlock
D) Begin and End

✔ Correct Answer: B

Reason: Two-phase commit has a Prepare phase (where participants vote) and a Commit phase (where the coordinator makes the final decision).

Tag: Past Paper

---

### Question 548
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Data Models
Difficulty: Medium

Question: What is the main advantage of schema flexibility in NoSQL?

A) No advantage
B) Easier to evolve data structures without downtime
C) Slower performance
D) More complexity

✔ Correct Answer: B

Reason: Schema flexibility allows data structures to evolve without requiring schema migrations or downtime.

Tag: Normal

---

### Question 549
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Cubes
Difficulty: Medium

Question: What is a data cube?

A) A physical cube
B) A multidimensional array of data for OLAP analysis
C) A backup cube
D) A deleted cube

✔ Correct Answer: B

Reason: A data cube is a multidimensional representation of data that enables OLAP operations like slice, dice, drill-down, and roll-up.

Tag: Normal

---

### Question 550
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Performance
Difficulty: Medium

Question: Why can using functions on indexed columns in WHERE clauses hurt performance?

A) It doesn't
B) It prevents the optimizer from using the index effectively
C) It improves performance
D) No impact

✔ Correct Answer: B

Reason: Applying functions to indexed columns (e.g., WHERE UPPER(name) = 'JOHN') prevents index usage, forcing a table scan.

Tag: Normal

---

### Question 551
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT name, salary
FROM employees e1
WHERE salary > ALL (SELECT salary FROM employees e2 WHERE e2.department = 'Sales');
```

A) All employees
B) Employees earning more than all Sales department employees
C) Only Sales employees
D) Error

✔ Correct Answer: B

Reason: The query selects employees whose salary exceeds the salary of every employee in the Sales department.

Tag: Past Paper

---

### Question 552
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query calculate?
```sql
SELECT name, salary,
NTILE(4) OVER (ORDER BY salary) as quartile
FROM employees;
```

A) Random numbers
B) Divides employees into 4 salary quartiles
C) Calculates average
D) Error

✔ Correct Answer: B

Reason: NTILE(4) divides the ordered result set into 4 approximately equal groups (quartiles) based on salary.

Tag: Normal

---

### Question 553
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Schema vs Instance
Difficulty: Easy

Question: What is the difference between schema and instance?

A) No difference
B) Schema is the structure, instance is the data at a point in time
C) Instance is the structure
D) Schema is temporary

✔ Correct Answer: B

Reason: Schema defines the database structure (tables, columns, types), while instance is the actual data stored at a particular moment.

Tag: Past Paper

---

### Question 554
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Closure Algorithm
Difficulty: Hard

Question: What is the closure of a set of attributes used for?

A) Deleting attributes
B) Finding all attributes functionally determined by the set
C) Encrypting attributes
D) Sorting attributes

✔ Correct Answer: B

Reason: The closure algorithm finds all attributes that can be functionally determined from a given set of attributes.

Tag: Past Paper

---

### Question 555
Domain: Databases
Topic: Transaction Management
Subtopic: Serializability
Difficulty: Hard

Question: What is a serial schedule?

A) A fast schedule
B) A schedule where transactions execute one after another without interleaving
C) A parallel schedule
D) A deleted schedule

✔ Correct Answer: B

Reason: A serial schedule executes transactions sequentially without any interleaving of operations.

Tag: Past Paper

---

### Question 556
Domain: Databases
Topic: Concurrency Control
Subtopic: Timestamp Ordering
Difficulty: Hard

Question: What happens if a transaction tries to read data with a newer write timestamp?

A) Read proceeds normally
B) Transaction is rolled back
C) Data is deleted
D) Nothing happens

✔ Correct Answer: B

Reason: In timestamp ordering, if a transaction tries to read data written by a newer transaction, it violates timestamp order and must be rolled back.

Tag: Past Paper

---

### Question 557
Domain: Databases
Topic: Recovery Management
Subtopic: Checkpointing Types
Difficulty: Hard

Question: What is a consistent checkpoint?

A) An inconsistent checkpoint
B) A checkpoint where all transactions are either committed or not started
C) A random checkpoint
D) A deleted checkpoint

✔ Correct Answer: B

Reason: A consistent checkpoint is taken when no transactions are active, ensuring all committed changes are on disk.

Tag: Normal

---

### Question 558
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Clustering
Difficulty: Medium

Question: What is a clustering index?

A) A random index
B) An index on an ordering non-key field
C) A deleted index
D) A temporary index

✔ Correct Answer: B

Reason: A clustering index is built on an ordering non-key field where records with similar values are physically clustered together.

Tag: Past Paper

---

### Question 559
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Heuristic Rules
Difficulty: Medium

Question: Which heuristic rule is commonly used in query optimization?

A) Delay all operations
B) Perform selections and projections early
C) Perform joins first
D) Ignore indexes

✔ Correct Answer: B

Reason: A common heuristic is to perform selections and projections as early as possible to reduce the size of intermediate results.

Tag: Normal

---

### Question 560
Domain: Databases
Topic: Database Security
Subtopic: Inference Control
Difficulty: Hard

Question: What is inference control in database security?

A) Making inferences
B) Preventing users from deriving sensitive information from non-sensitive data
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Inference control prevents users from inferring sensitive information by combining non-sensitive data from multiple queries.

Tag: Normal

---

### Question 561
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Locking
Difficulty: Hard

Question: What is a centralized locking approach?

A) No locks
B) One site manages all locks for the distributed database
C) Each site manages its own locks
D) Random locking

✔ Correct Answer: B

Reason: In centralized locking, a single site (lock manager) manages all locks for the entire distributed database.

Tag: Normal

---

### Question 562
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Vector Clocks
Difficulty: Hard

Question: What are vector clocks used for in distributed databases?

A) Telling time
B) Tracking causality and detecting conflicts in distributed systems
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Vector clocks track causality relationships between events in distributed systems, helping detect and resolve conflicts.

Tag: Normal

---

### Question 563
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Association Rules
Difficulty: Medium

Question: What is association rule mining?

A) Mining minerals
B) Discovering relationships between items in large datasets
C) Deleting associations
D) Backing up rules

✔ Correct Answer: B

Reason: Association rule mining discovers interesting relationships (like "customers who buy X also buy Y") in large transaction datasets.

Tag: Normal

---

### Question 564
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Constraints
Difficulty: Easy

Question: What happens when you try to insert a duplicate value into a column with a UNIQUE constraint?

A) Insert succeeds
B) Insert fails with an error
C) Value is modified
D) Nothing happens

✔ Correct Answer: B

Reason: UNIQUE constraint prevents duplicate values; attempting to insert a duplicate causes the operation to fail with an error.

Tag: Normal

---

### Question 565
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Transactions
Difficulty: Easy

Question: What is the default transaction isolation level in most databases?

A) Read Uncommitted
B) Read Committed
C) Repeatable Read
D) Serializable

✔ Correct Answer: B

Reason: Most databases default to Read Committed isolation level, balancing consistency and performance.

Tag: Normal

---

### Question 566
Domain: Databases
Topic: Advanced SQL
Subtopic: Stored Procedures
Difficulty: Medium

Question: What is an advantage of stored procedures?

A) Slower execution
B) Reduced network traffic and improved security
C) More network traffic
D) No advantages

✔ Correct Answer: B

Reason: Stored procedures reduce network traffic (only procedure call is sent) and improve security by encapsulating logic.

Tag: Normal

---

### Question 567
Domain: Databases
Topic: Advanced SQL
Subtopic: Triggers
Difficulty: Medium

Question: What is a BEFORE trigger?

A) A trigger that fires after an event
B) A trigger that fires before an event occurs
C) A deleted trigger
D) A disabled trigger

✔ Correct Answer: B

Reason: A BEFORE trigger executes before the triggering event (INSERT, UPDATE, DELETE) occurs, allowing validation or modification.

Tag: Normal

---

### Question 568
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Tuple Variables
Difficulty: Hard

Question: What is a tuple variable in relational calculus?

A) A constant
B) A variable that ranges over tuples of a relation
C) A deleted variable
D) A numeric variable

✔ Correct Answer: B

Reason: A tuple variable ranges over all tuples in a relation, used to express queries in tuple relational calculus.

Tag: Past Paper

---

### Question 569
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Canonical Cover
Difficulty: Hard

Question: What is a canonical cover of functional dependencies?

A) A large set
B) A minimal equivalent set with no redundant dependencies
C) A deleted set
D) A random set

✔ Correct Answer: B

Reason: A canonical cover is a minimal set of functional dependencies equivalent to the original set, with no redundancy.

Tag: Past Paper

---

### Question 570
Domain: Databases
Topic: Transaction Management
Subtopic: Recoverable Schedules
Difficulty: Hard

Question: What is a recoverable schedule?

A) Any schedule
B) A schedule where transactions commit only after all transactions they read from have committed
C) A fast schedule
D) A deleted schedule

✔ Correct Answer: B

Reason: A recoverable schedule ensures that if T1 reads from T2, T2 commits before T1, preventing cascading aborts.

Tag: Past Paper

---

### Question 571
Domain: Databases
Topic: Concurrency Control
Subtopic: Graph-Based Protocols
Difficulty: Hard

Question: What is tree protocol in concurrency control?

A) A random protocol
B) A locking protocol where locks follow a tree structure
C) A deleted protocol
D) A backup protocol

✔ Correct Answer: B

Reason: Tree protocol imposes a partial ordering on data items in a tree structure, ensuring deadlock-free locking.

Tag: Past Paper

---

### Question 572
Domain: Databases
Topic: Recovery Management
Subtopic: Log-Based Recovery
Difficulty: Medium

Question: What is a redo-only recovery algorithm?

A) Only undoes changes
B) Only reapplies committed transaction changes
C) Does nothing
D) Deletes logs

✔ Correct Answer: B

Reason: Redo-only recovery reapplies changes from committed transactions without needing to undo uncommitted ones.

Tag: Normal

---

### Question 573
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Hashing
Difficulty: Medium

Question: What is extendible hashing?

A) Fixed-size hashing
B) A dynamic hashing technique that grows/shrinks as needed
C) No hashing
D) Deleted hashing

✔ Correct Answer: B

Reason: Extendible hashing is a dynamic hashing technique that allows the hash table to grow and shrink dynamically.

Tag: Normal

---

### Question 574
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Materialized Views
Difficulty: Medium

Question: When should materialized views be refreshed?

A) Never
B) When base tables change or on a schedule
C) Every second
D) Randomly

✔ Correct Answer: B

Reason: Materialized views should be refreshed when base tables change (immediate) or on a schedule (deferred) to maintain accuracy.

Tag: Normal

---

### Question 575
Domain: Databases
Topic: Database Security
Subtopic: Statistical Database Security
Difficulty: Hard

Question: What is a tracker attack in statistical databases?

A) A tracking system
B) Using multiple queries to infer individual values
C) A deleted attack
D) A backup attack

✔ Correct Answer: B

Reason: A tracker attack uses a sequence of statistical queries to infer individual data values that should be protected.

Tag: Normal

---

### Question 576
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Catalog
Difficulty: Medium

Question: What information does a distributed catalog contain?

A) Only table names
B) Metadata about data distribution, fragmentation, and replication
C) Only user data
D) Nothing

✔ Correct Answer: B

Reason: A distributed catalog stores metadata about how data is distributed, fragmented, and replicated across sites.

Tag: Normal

---

### Question 577
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistent Hashing
Difficulty: Hard

Question: What problem does consistent hashing solve in distributed systems?

A) No problem
B) Minimizing data movement when nodes are added/removed
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Consistent hashing minimizes the amount of data that needs to be moved when nodes are added or removed from the system.

Tag: Normal

---

### Question 578
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Profiling
Difficulty: Easy

Question: What is data profiling?

A) User profiling
B) Analyzing data to understand its structure, content, and quality
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Data profiling examines data to understand its structure, content, relationships, and quality issues.

Tag: Normal

---

### Question 579
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Window Functions
Difficulty: Hard

Question: What is the difference between ROWS and RANGE in window frame specifications?

A) No difference
B) ROWS counts physical rows, RANGE considers logical ranges based on values
C) ROWS is faster
D) RANGE is deprecated

✔ Correct Answer: B

Reason: ROWS defines the frame by counting physical rows, while RANGE defines it by logical value ranges.

Tag: Normal

---

### Question 580
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT department, 
       AVG(salary) OVER (PARTITION BY department) as dept_avg,
       AVG(salary) OVER () as company_avg
FROM employees;
```

A) Only department averages
B) Each employee with their department average and company-wide average
C) Only company average
D) Error

✔ Correct Answer: B

Reason: The query shows each employee with both their department's average salary and the company-wide average salary.

Tag: Normal

---

### Question 581
Domain: Databases
Topic: Advanced SQL
Subtopic: JSON Support
Difficulty: Medium

Question: What SQL function extracts a value from a JSON column?

A) GET_JSON()
B) JSON_EXTRACT() or JSON_VALUE()
C) EXTRACT_JSON()
D) VALUE_JSON()

✔ Correct Answer: B

Reason: JSON_EXTRACT() (MySQL) or JSON_VALUE() (SQL Server) extracts values from JSON data stored in columns.

Tag: Normal

---

### Question 582
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Weak Entity
Difficulty: Medium

Question: What is a weak entity?

A) A strong entity
B) An entity that cannot be uniquely identified without a related strong entity
C) A deleted entity
D) A temporary entity

✔ Correct Answer: B

Reason: A weak entity depends on a strong entity for its identification and cannot exist independently.

Tag: Past Paper

---

### Question 583
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization Scenarios
Difficulty: Medium

Question: When is denormalization justified?

A) Always
B) When read performance is critical and redundancy costs are acceptable
C) Never
D) Randomly

✔ Correct Answer: B

Reason: Denormalization is justified when read performance gains outweigh the costs of data redundancy and update complexity.

Tag: Normal

---

### Question 584
Domain: Databases
Topic: Transaction Management
Subtopic: Cascadeless Schedules
Difficulty: Hard

Question: What is a cascadeless schedule?

A) Any schedule
B) A schedule where transactions read only committed data
C) A fast schedule
D) A deleted schedule

✔ Correct Answer: B

Reason: A cascadeless schedule ensures transactions read only committed data, preventing cascading rollbacks.

Tag: Past Paper

---

### Question 585
Domain: Databases
Topic: Concurrency Control
Subtopic: Multiple Granularity Locking
Difficulty: Hard

Question: What is the purpose of intention locks in multiple granularity locking?

A) No purpose
B) To indicate intention to lock at finer granularity without locking entire hierarchy
C) To delete locks
D) To backup locks

✔ Correct Answer: B

Reason: Intention locks signal the intention to acquire locks at finer granularity, allowing efficient multi-level locking.

Tag: Past Paper

---

### Question 586
Domain: Databases
Topic: Recovery Management
Subtopic: Remote Backup
Difficulty: Easy

Question: What is remote backup?

A) Local backup
B) Maintaining backup copies at a geographically distant location
C) No backup
D) Deleted backup

✔ Correct Answer: B

Reason: Remote backup stores copies of data at a geographically distant location for disaster recovery.

Tag: Normal

---

### Question 587
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Linear Hashing
Difficulty: Hard

Question: What is linear hashing?

A) A static hashing method
B) A dynamic hashing method that grows incrementally
C) No hashing
D) Random hashing

✔ Correct Answer: B

Reason: Linear hashing is a dynamic hashing technique that allows the hash table to grow incrementally without reorganizing all data.

Tag: Normal

---

### Question 588
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Parallel Processing
Difficulty: Hard

Question: What is inter-query parallelism?

A) Parallelism within a query
B) Executing multiple different queries simultaneously
C) No parallelism
D) Sequential execution

✔ Correct Answer: B

Reason: Inter-query parallelism executes multiple different queries simultaneously on different processors.

Tag: Normal

---

### Question 589
Domain: Databases
Topic: Database Security
Subtopic: Mandatory Access Control
Difficulty: Medium

Question: What is mandatory access control (MAC)?

A) Optional access control
B) Access control based on security classifications and clearances
C) No access control
D) Random access control

✔ Correct Answer: B

Reason: MAC enforces access control based on security classifications of data and clearance levels of users.

Tag: Normal

---

### Question 590
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Optimization
Difficulty: Hard

Question: What is the main goal of distributed query optimization?

A) Maximize data transfer
B) Minimize total cost including communication and local processing
C) Increase complexity
D) Slow down queries

✔ Correct Answer: B

Reason: Distributed query optimization aims to minimize total cost, particularly expensive network communication costs.

Tag: Normal

---

### Question 591
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: NewSQL
Difficulty: Medium

Question: What is NewSQL?

A) Old SQL
B) Modern databases providing SQL interface with NoSQL scalability
C) No SQL support
D) Deleted SQL

✔ Correct Answer: B

Reason: NewSQL databases provide traditional SQL interface and ACID guarantees while offering NoSQL-like scalability.

Tag: Normal

---

### Question 592
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Lineage
Difficulty: Medium

Question: What is data lineage?

A) Data age
B) Tracking data from origin through transformations to destination
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Data lineage tracks the flow of data from its origin through various transformations to its final destination.

Tag: Normal

---

### Question 593
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Performance
Difficulty: Medium

Question: Why can implicit type conversion hurt query performance?

A) It doesn't
B) It prevents index usage and adds conversion overhead
C) It improves performance
D) No impact

✔ Correct Answer: B

Reason: Implicit type conversion can prevent index usage and add computational overhead for converting data types.

Tag: Normal

---

### Question 594
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
DELETE FROM orders WHERE order_id IN (SELECT order_id FROM orders GROUP BY order_id HAVING COUNT(*) > 1);
```

A) Deletes all orders
B) Attempts to delete duplicate orders (may have issues)
C) Updates orders
D) Creates orders

✔ Correct Answer: B

Reason: The query attempts to delete duplicate orders, though it may delete all duplicates rather than keeping one copy.

Tag: Normal

---

### Question 595
Domain: Databases
Topic: Advanced SQL
Subtopic: Full-Text Search
Difficulty: Medium

Question: What is full-text search?

A) Searching numbers
B) Searching text content within documents or large text fields
C) Searching dates
D) Searching images

✔ Correct Answer: B

Reason: Full-text search enables searching for words and phrases within large text fields or documents.

Tag: Normal

---

### Question 596
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Domain Independence
Difficulty: Hard

Question: What is domain independence in relational calculus?

A) No independence
B) Query results depend only on database content, not domain size
C) Random independence
D) Deleted independence

✔ Correct Answer: B

Reason: Domain independence ensures query results depend only on the database content, not on the size of attribute domains.

Tag: Past Paper

---

### Question 597
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Universal Relation
Difficulty: Hard

Question: What is a universal relation?

A) A small relation
B) A single relation containing all attributes of the database
C) A deleted relation
D) A temporary relation

✔ Correct Answer: B

Reason: A universal relation is a hypothetical single relation containing all attributes, used in normalization theory.

Tag: Past Paper

---

### Question 598
Domain: Databases
Topic: Transaction Management
Subtopic: Strict Schedules
Difficulty: Hard

Question: What is a strict schedule?

A) Any schedule
B) A schedule where transactions neither read nor write until all transactions that previously wrote have committed/aborted
C) A fast schedule
D) A deleted schedule

✔ Correct Answer: B

Reason: Strict schedules prevent both dirty reads and dirty writes by ensuring proper ordering of read/write operations.

Tag: Past Paper

---

### Question 599
Domain: Databases
Topic: Concurrency Control
Subtopic: Validation Phase
Difficulty: Hard

Question: What is checked during the validation phase of optimistic concurrency control?

A) Nothing
B) Whether the transaction's reads and writes conflict with other transactions
C) User permissions
D) Disk space

✔ Correct Answer: B

Reason: The validation phase checks if the transaction's operations conflict with concurrent transactions to ensure serializability.

Tag: Normal

---

### Question 600
Domain: Databases
Topic: Recovery Management
Subtopic: Database Mirroring
Difficulty: Medium

Question: What is database mirroring?

A) Backing up to tape
B) Maintaining an exact copy of the database on a separate server
C) Deleting data
D) Compressing data

✔ Correct Answer: B

Reason: Database mirroring maintains a synchronized copy of the database on a separate server for high availability and disaster recovery.

Tag: Normal

---

**End of Batch 06**

---

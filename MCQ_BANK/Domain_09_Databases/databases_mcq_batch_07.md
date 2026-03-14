# Databases MCQ Bank - Batch 07

## Questions 601-700

---

### Question 601
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT e.name, COUNT(d.dependent_id) as num_dependents
FROM employees e
LEFT JOIN dependents d ON e.employee_id = d.employee_id
GROUP BY e.employee_id, e.name
HAVING COUNT(d.dependent_id) >= 2;
```

A) All employees
B) Employees with 2 or more dependents
C) All dependents
D) Error

✔ Correct Answer: B

Reason: The query groups employees with their dependents and filters to show only those with 2 or more dependents.

Tag: Normal

---

### Question 602
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the result of this query?
```sql
SELECT CONCAT(first_name, ' ', last_name) as full_name
FROM employees
WHERE last_name LIKE '%son';
```

A) All employees
B) Employees whose last name ends with 'son'
C) Employees whose last name starts with 'son'
D) Error

✔ Correct Answer: B

Reason: LIKE '%son' matches last names ending with 'son', and CONCAT combines first and last names.

Tag: Normal

---

### Question 603
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query calculate?
```sql
SELECT product_id,
       SUM(quantity) as total_sold,
       SUM(quantity * price) as revenue,
       SUM(quantity * price) / SUM(quantity) as avg_price
FROM sales
GROUP BY product_id;
```

A) Only total quantity
B) Total quantity sold, revenue, and weighted average price per product
C) Only revenue
D) Error

✔ Correct Answer: B

Reason: The query calculates total quantity, total revenue, and weighted average price (revenue/quantity) for each product.

Tag: Normal

---

### Question 604
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this window function show?
```sql
SELECT name, department, salary,
       FIRST_VALUE(name) OVER (PARTITION BY department ORDER BY salary DESC) as highest_paid
FROM employees;
```

A) Random names
B) Each employee with the name of the highest-paid person in their department
C) Only highest-paid employees
D) Error

✔ Correct Answer: B

Reason: FIRST_VALUE returns the name of the first row (highest salary) in each department partition.

Tag: Normal

---

### Question 605
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
UPDATE employees 
SET salary = salary * 1.05 
WHERE department = 'IT' AND hire_date < '2020-01-01';
```

A) Deletes employees
B) Gives 5% raise to IT employees hired before 2020
C) Reduces salaries
D) Error

✔ Correct Answer: B

Reason: The query increases salary by 5% (multiplies by 1.05) for IT department employees hired before 2020.

Tag: Normal

---

### Question 606
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the output of this query?
```sql
SELECT department,
       RANK() OVER (ORDER BY AVG(salary) DESC) as dept_rank
FROM employees
GROUP BY department;
```

A) Employee ranks
B) Department ranks based on average salary
C) Salary values
D) Error

✔ Correct Answer: B

Reason: The query ranks departments based on their average salary, with highest average getting rank 1.

Tag: Normal

---

### Question 607
Domain: Databases
Topic: Database System Architecture
Subtopic: Query Processing Pipeline
Difficulty: Medium

Question: What is the correct order of query processing stages?

A) Execution, Parsing, Optimization
B) Parsing, Optimization, Execution
C) Optimization, Parsing, Execution
D) Random order

✔ Correct Answer: B

Reason: Query processing follows: Parsing (syntax check), Optimization (plan selection), Execution (running the plan).

Tag: Normal

---

### Question 608
Domain: Databases
Topic: Database System Architecture
Subtopic: Storage Manager
Difficulty: Medium

Question: What is the role of the storage manager?

A) Managing users
B) Managing physical storage and data access
C) Managing networks
D) Managing applications

✔ Correct Answer: B

Reason: The storage manager handles physical storage, file organization, and provides interface between physical storage and database.

Tag: Normal

---

### Question 609
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Integrity Rules
Difficulty: Easy

Question: What does the entity integrity rule state?

A) Foreign keys can be NULL
B) Primary key cannot be NULL
C) All attributes can be NULL
D) No rules exist

✔ Correct Answer: B

Reason: Entity integrity rule states that primary key attributes cannot contain NULL values.

Tag: Past Paper

---

### Question 610
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Integrity Rules
Difficulty: Easy

Question: What does the referential integrity rule state?

A) Primary keys must be unique
B) Foreign key must match a primary key value or be NULL
C) All values must be unique
D) No rules exist

✔ Correct Answer: B

Reason: Referential integrity requires that foreign key values either match a primary key value in the referenced table or be NULL.

Tag: Past Paper

---

### Question 611
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization Goals
Difficulty: Easy

Question: What is the main goal of normalization?

A) Increase redundancy
B) Minimize redundancy and dependency anomalies
C) Slow down queries
D) Increase storage

✔ Correct Answer: B

Reason: Normalization aims to minimize data redundancy and eliminate insertion, update, and deletion anomalies.

Tag: Normal

---

### Question 612
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Functional Dependency Types
Difficulty: Hard

Question: What is a full functional dependency?

A) Partial dependency
B) Attribute depends on the entire key, not just part of it
C) No dependency
D) Transitive dependency

✔ Correct Answer: B

Reason: Full functional dependency means a non-key attribute depends on the entire composite key, not just part of it.

Tag: Past Paper

---

### Question 613
Domain: Databases
Topic: Transaction Management
Subtopic: ACID Properties
Difficulty: Medium

Question: Which ACID property ensures database constraints are maintained?

A) Atomicity
B) Consistency
C) Isolation
D) Durability

✔ Correct Answer: B

Reason: Consistency ensures that transactions maintain database integrity constraints and business rules.

Tag: Past Paper

---

### Question 614
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Operations
Difficulty: Easy

Question: What operation marks the beginning of a transaction?

A) COMMIT
B) BEGIN TRANSACTION or START TRANSACTION
C) ROLLBACK
D) END

✔ Correct Answer: B

Reason: BEGIN TRANSACTION or START TRANSACTION explicitly marks the start of a transaction.

Tag: Normal

---

### Question 615
Domain: Databases
Topic: Concurrency Control
Subtopic: Locking Protocols
Difficulty: Medium

Question: What is the growing phase in two-phase locking?

A) Releasing locks
B) Acquiring locks without releasing any
C) No locks
D) Random locking

✔ Correct Answer: B

Reason: In the growing phase, a transaction can acquire locks but cannot release any locks.

Tag: Past Paper

---

### Question 616
Domain: Databases
Topic: Concurrency Control
Subtopic: Locking Protocols
Difficulty: Medium

Question: What is the shrinking phase in two-phase locking?

A) Acquiring locks
B) Releasing locks without acquiring new ones
C) No locks
D) Random locking

✔ Correct Answer: B

Reason: In the shrinking phase, a transaction can release locks but cannot acquire new locks.

Tag: Past Paper

---

### Question 617
Domain: Databases
Topic: Recovery Management
Subtopic: Failure Types
Difficulty: Easy

Question: What is a transaction failure?

A) System crash
B) Logical error or system error causing transaction abort
C) Disk failure
D) Network failure

✔ Correct Answer: B

Reason: Transaction failure occurs due to logical errors (like constraint violations) or system errors causing the transaction to abort.

Tag: Normal

---

### Question 618
Domain: Databases
Topic: Recovery Management
Subtopic: Failure Types
Difficulty: Easy

Question: What is a system crash?

A) Transaction error
B) Hardware or software failure causing loss of main memory contents
C) Disk failure
D) User error

✔ Correct Answer: B

Reason: System crash is a hardware or software failure that causes loss of volatile memory contents but not disk storage.

Tag: Normal

---

### Question 619
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Benefits
Difficulty: Easy

Question: What is the primary benefit of indexing?

A) Increased storage
B) Faster data retrieval
C) Slower queries
D) More complexity

✔ Correct Answer: B

Reason: Indexes provide fast access paths to data, significantly speeding up query execution.

Tag: Normal

---

### Question 620
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Costs
Difficulty: Easy

Question: What is a cost of maintaining indexes?

A) Faster writes
B) Slower INSERT, UPDATE, DELETE operations
C) Less storage
D) No costs

✔ Correct Answer: B

Reason: Indexes must be updated during write operations, adding overhead to INSERT, UPDATE, and DELETE.

Tag: Normal

---

### Question 621
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Selection Algorithms
Difficulty: Medium

Question: Which selection algorithm is most efficient for equality search on a key?

A) Linear search
B) Binary search or index scan
C) Full table scan
D) Random search

✔ Correct Answer: B

Reason: Binary search (on sorted data) or index scan provides efficient direct access for equality searches on keys.

Tag: Normal

---

### Question 622
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Strategies
Difficulty: Medium

Question: When is nested loop join most appropriate?

A) For large tables
B) When one table is small or inner table has an index
C) Never appropriate
D) Always appropriate

✔ Correct Answer: B

Reason: Nested loop join works well when one table is small or the inner table has an index on the join attribute.

Tag: Normal

---

### Question 623
Domain: Databases
Topic: Database Security
Subtopic: Authentication Methods
Difficulty: Easy

Question: What is password-based authentication?

A) No authentication
B) Verifying identity using username and password
C) Biometric authentication
D) Token-based only

✔ Correct Answer: B

Reason: Password-based authentication verifies user identity by checking username and password credentials.

Tag: Normal

---

### Question 624
Domain: Databases
Topic: Database Security
Subtopic: Authorization Levels
Difficulty: Medium

Question: What are the typical levels of authorization?

A) Only read
B) Read, Insert, Update, Delete, and administrative privileges
C) Only write
D) No levels

✔ Correct Answer: B

Reason: Authorization typically includes read, insert, update, delete privileges on data, plus administrative privileges.

Tag: Normal

---

### Question 625
Domain: Databases
Topic: Distributed Databases
Subtopic: Distribution Transparency
Difficulty: Easy

Question: What is distribution transparency?

A) Visible distribution
B) Users can access data without knowing its physical distribution
C) No distribution
D) Manual distribution

✔ Correct Answer: B

Reason: Distribution transparency hides the physical distribution of data, allowing users to access it as if it were centralized.

Tag: Normal

---

### Question 626
Domain: Databases
Topic: Distributed Databases
Subtopic: Advantages
Difficulty: Easy

Question: What is an advantage of distributed databases?

A) Increased complexity only
B) Improved reliability and availability
C) Slower performance
D) No advantages

✔ Correct Answer: B

Reason: Distributed databases improve reliability (through replication) and availability (data accessible from multiple sites).

Tag: Normal

---

### Question 627
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: NoSQL Advantages
Difficulty: Easy

Question: What is a key advantage of NoSQL databases?

A) ACID compliance only
B) Horizontal scalability and flexible schemas
C) Complex joins
D) Strict schemas

✔ Correct Answer: B

Reason: NoSQL databases excel at horizontal scalability and offer flexible schemas for evolving data structures.

Tag: Normal

---

### Question 628
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: NoSQL Trade-offs
Difficulty: Medium

Question: What do many NoSQL databases sacrifice for scalability?

A) Nothing
B) Strong consistency (ACID properties)
C) Performance
D) Storage capacity

✔ Correct Answer: B

Reason: Many NoSQL databases trade strong consistency for scalability and availability (following BASE instead of ACID).

Tag: Normal

---

### Question 629
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Warehouse Characteristics
Difficulty: Easy

Question: What does "time-variant" mean in data warehousing?

A) No time information
B) Data is stored with time dimension for historical analysis
C) Current data only
D) Random time

✔ Correct Answer: B

Reason: Time-variant means data warehouse maintains historical data with time stamps for trend analysis.

Tag: Normal

---

### Question 630
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Warehouse Characteristics
Difficulty: Easy

Question: What does "integrated" mean in data warehousing?

A) Separate data sources
B) Data from multiple sources is combined and standardized
C) No integration
D) Random data

✔ Correct Answer: B

Reason: Integrated means data from various sources is combined, cleaned, and standardized in the warehouse.

Tag: Normal

---

### Question 631
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Data Definition Language
Difficulty: Easy

Question: Which command is used to remove a table from the database?

A) DELETE TABLE
B) DROP TABLE
C) REMOVE TABLE
D) ERASE TABLE

✔ Correct Answer: B

Reason: DROP TABLE permanently removes a table and all its data from the database.

Tag: Normal

---

### Question 632
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Data Definition Language
Difficulty: Easy

Question: Which command is used to add a new column to an existing table?

A) ADD COLUMN
B) ALTER TABLE ... ADD
C) INSERT COLUMN
D) CREATE COLUMN

✔ Correct Answer: B

Reason: ALTER TABLE ... ADD is used to add new columns to an existing table.

Tag: Normal

---

### Question 633
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Aggregate Functions
Difficulty: Medium

Question: What happens when you use aggregate functions without GROUP BY?

A) Error
B) Aggregates are calculated over all rows
C) No calculation
D) Random results

✔ Correct Answer: B

Reason: Without GROUP BY, aggregate functions calculate over all rows in the result set, returning a single value.

Tag: Normal

---

### Question 634
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Subqueries
Difficulty: Medium

Question: Can a subquery return multiple columns?

A) No, never
B) Yes, when used with row comparisons or IN clause
C) Only one column always
D) Not applicable

✔ Correct Answer: B

Reason: Subqueries can return multiple columns when used with row comparisons or in the FROM clause.

Tag: Normal

---

### Question 635
Domain: Databases
Topic: Advanced SQL
Subtopic: Transactions
Difficulty: Medium

Question: What happens to locks when a transaction commits?

A) Locks remain
B) All locks held by the transaction are released
C) Locks are transferred
D) Nothing happens

✔ Correct Answer: B

Reason: When a transaction commits, all locks it holds are released, allowing other transactions to access the data.

Tag: Normal

---

### Question 636
Domain: Databases
Topic: Advanced SQL
Subtopic: Transactions
Difficulty: Medium

Question: What happens to changes when a transaction is rolled back?

A) Changes are kept
B) All changes are undone
C) Some changes remain
D) Nothing happens

✔ Correct Answer: B

Reason: ROLLBACK undoes all changes made by the transaction, restoring the database to its state before the transaction began.

Tag: Normal

---

### Question 637
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Operators
Difficulty: Medium

Question: Which relational algebra operator removes duplicate tuples?

A) Select (σ)
B) Project (π)
C) Union (∪)
D) All of them

✔ Correct Answer: B

Reason: Project (π) removes duplicate tuples from the result, as relations are sets and cannot contain duplicates.

Tag: Past Paper

---

### Question 638
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Operators
Difficulty: Medium

Question: What does the Cartesian product (×) operation produce?

A) Common tuples
B) All possible combinations of tuples from two relations
C) Matching tuples only
D) No tuples

✔ Correct Answer: B

Reason: Cartesian product combines each tuple from the first relation with every tuple from the second relation.

Tag: Past Paper

---

### Question 639
Domain: Databases
Topic: Database Design & Normalization
Subtopic: 2NF Requirements
Difficulty: Medium

Question: What must be true for a relation to be in 2NF?

A) No functional dependencies
B) In 1NF and no partial dependencies
C) In 3NF
D) No dependencies at all

✔ Correct Answer: B

Reason: 2NF requires the relation to be in 1NF and have no partial dependencies (non-key attributes fully depend on the entire key).

Tag: Past Paper

---

### Question 640
Domain: Databases
Topic: Database Design & Normalization
Subtopic: 3NF Requirements
Difficulty: Medium

Question: What must be true for a relation to be in 3NF?

A) No functional dependencies
B) In 2NF and no transitive dependencies
C) In 1NF only
D) No keys

✔ Correct Answer: B

Reason: 3NF requires the relation to be in 2NF and have no transitive dependencies (non-key attributes don't depend on other non-key attributes).

Tag: Past Paper

---

### Question 641
Domain: Databases
Topic: Transaction Management
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level allows the most concurrency?

A) Serializable
B) Read Uncommitted
C) Repeatable Read
D) Read Committed

✔ Correct Answer: B

Reason: Read Uncommitted allows the most concurrency by permitting dirty reads, but provides the least consistency.

Tag: Normal

---

### Question 642
Domain: Databases
Topic: Transaction Management
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level provides the strongest consistency?

A) Read Uncommitted
B) Read Committed
C) Repeatable Read
D) Serializable

✔ Correct Answer: D

Reason: Serializable provides the strongest consistency by preventing all anomalies, but allows the least concurrency.

Tag: Normal

---

### Question 643
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Detection
Difficulty: Hard

Question: How is deadlock typically detected?

A) Random checking
B) Using a wait-for graph to find cycles
C) No detection possible
D) User reports

✔ Correct Answer: B

Reason: Deadlock is detected by constructing a wait-for graph and checking for cycles, which indicate deadlock.

Tag: Past Paper

---

### Question 644
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Resolution
Difficulty: Medium

Question: How is deadlock typically resolved?

A) Waiting indefinitely
B) Aborting one or more transactions to break the cycle
C) Ignoring it
D) Restarting the system

✔ Correct Answer: B

Reason: Deadlock is resolved by selecting and aborting one or more transactions (victims) to break the circular wait.

Tag: Normal

---

### Question 645
Domain: Databases
Topic: Recovery Management
Subtopic: Backup Types
Difficulty: Easy

Question: What is the advantage of incremental backups over full backups?

A) No advantage
B) Faster backup and less storage space
C) Slower backup
D) More storage needed

✔ Correct Answer: B

Reason: Incremental backups are faster and require less storage as they only backup changed data since the last backup.

Tag: Normal

---

### Question 646
Domain: Databases
Topic: Recovery Management
Subtopic: Backup Types
Difficulty: Medium

Question: What is the disadvantage of incremental backups?

A) No disadvantage
B) Slower and more complex recovery process
C) Faster recovery
D) Simpler recovery

✔ Correct Answer: B

Reason: Recovery from incremental backups is slower and more complex, requiring the full backup plus all incremental backups.

Tag: Normal

---

### Question 647
Domain: Databases
Topic: Indexing & File Organization
Subtopic: B-Tree Properties
Difficulty: Hard

Question: What is a key property of B-trees?

A) Unbalanced structure
B) All leaf nodes are at the same level (balanced)
C) Random structure
D) No properties

✔ Correct Answer: B

Reason: B-trees are balanced trees where all leaf nodes are at the same level, ensuring consistent access time.

Tag: Past Paper

---

### Question 648
Domain: Databases
Topic: Indexing & File Organization
Subtopic: B+ Tree Properties
Difficulty: Hard

Question: Where is data stored in a B+ tree?

A) In all nodes
B) Only in leaf nodes
C) Only in root
D) Randomly

✔ Correct Answer: B

Reason: In B+ trees, all data is stored in leaf nodes, and internal nodes only contain keys for navigation.

Tag: Past Paper

---

### Question 649
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Cost Factors
Difficulty: Medium

Question: Which factor typically dominates query execution cost?

A) CPU time
B) Disk I/O operations
C) Memory usage
D) Network latency (in centralized systems)

✔ Correct Answer: B

Reason: Disk I/O is typically the dominant cost factor in query execution, being much slower than CPU or memory operations.

Tag: Normal

---

### Question 650
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Optimization Goals
Difficulty: Easy

Question: What is the primary goal of query optimization?

A) Maximize execution time
B) Minimize execution time and resource usage
C) Increase complexity
D) Use more resources

✔ Correct Answer: B

Reason: Query optimization aims to find the execution plan that minimizes execution time and resource usage.

Tag: Normal

---

### Question 651
Domain: Databases
Topic: Database Security
Subtopic: Threats
Difficulty: Easy

Question: What is a database security threat?

A) A benefit
B) Any circumstance or event that could harm the database
C) A feature
D) A backup

✔ Correct Answer: B

Reason: A security threat is any circumstance or event with potential to harm the database through unauthorized access, modification, or destruction.

Tag: Normal

---

### Question 652
Domain: Databases
Topic: Database Security
Subtopic: Controls
Difficulty: Easy

Question: What are database security controls?

A) Threats
B) Measures to protect against security threats
C) Vulnerabilities
D) Attacks

✔ Correct Answer: B

Reason: Security controls are protective measures implemented to prevent, detect, or minimize security threats.

Tag: Normal

---

### Question 653
Domain: Databases
Topic: Distributed Databases
Subtopic: Challenges
Difficulty: Medium

Question: What is a major challenge in distributed databases?

A) Too simple
B) Maintaining consistency across sites
C) Too fast
D) No challenges

✔ Correct Answer: B

Reason: Maintaining data consistency across multiple sites while ensuring availability is a major challenge in distributed databases.

Tag: Normal

---

### Question 654
Domain: Databases
Topic: Distributed Databases
Subtopic: Replication Benefits
Difficulty: Easy

Question: What is a benefit of data replication?

A) Increased complexity only
B) Improved availability and read performance
C) Slower access
D) No benefits

✔ Correct Answer: B

Reason: Replication improves availability (data accessible even if one site fails) and read performance (data can be read from nearest replica).

Tag: Normal

---

### Question 655
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Use Cases
Difficulty: Medium

Question: When is a key-value store most appropriate?

A) Complex queries
B) Simple lookups by key with high performance requirements
C) Complex relationships
D) Never appropriate

✔ Correct Answer: B

Reason: Key-value stores excel at simple, fast lookups by key, ideal for caching and session storage.

Tag: Normal

---

### Question 656
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Use Cases
Difficulty: Medium

Question: When is a graph database most appropriate?

A) Simple key-value lookups
B) Highly connected data with complex relationships
C) Flat data structures
D) Never appropriate

✔ Correct Answer: B

Reason: Graph databases are ideal for highly connected data where relationships are as important as the data itself.

Tag: Normal

---

### Question 657
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: ETL Process
Difficulty: Easy

Question: What does the "E" in ETL stand for?

A) Encrypt
B) Extract
C) Execute
D) Evaluate

✔ Correct Answer: B

Reason: ETL stands for Extract, Transform, Load - Extract is the first step of pulling data from source systems.

Tag: Normal

---

### Question 658
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: ETL Process
Difficulty: Easy

Question: What does the "T" in ETL stand for?

A) Transfer
B) Transform
C) Translate
D) Terminate

✔ Correct Answer: B

Reason: The "T" stands for Transform - converting data from source format to warehouse format.

Tag: Normal

---

### Question 659
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: ETL Process
Difficulty: Easy

Question: What does the "L" in ETL stand for?

A) Link
B) Load
C) List
D) Lock

✔ Correct Answer: B

Reason: The "L" stands for Load - loading transformed data into the data warehouse.

Tag: Normal

---

### Question 660
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query return?
```sql
SELECT * FROM products 
WHERE price > (SELECT AVG(price) FROM products);
```

A) All products
B) Products with above-average price
C) Cheapest products
D) Error

✔ Correct Answer: B

Reason: The subquery calculates average price, and the outer query selects products priced above that average.

Tag: Normal

---

### Question 661
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT customer_id, 
       order_date,
       LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) as prev_order
FROM orders;
```

A) Random dates
B) Each order with the customer's previous order date
C) Only first orders
D) Error

✔ Correct Answer: B

Reason: LAG retrieves the previous order date for each customer, ordered chronologically.

Tag: Normal

---

### Question 662
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query do?
```sql
SELECT name, salary,
       CUME_DIST() OVER (ORDER BY salary) as cumulative_dist
FROM employees;
```

A) Calculates sum
B) Calculates cumulative distribution (percentile) of each salary
C) Counts employees
D) Error

✔ Correct Answer: B

Reason: CUME_DIST() calculates the cumulative distribution (relative position) of each value in the ordered set.

Tag: Normal

---

### Question 663
Domain: Databases
Topic: Database System Architecture
Subtopic: Transaction Manager
Difficulty: Medium

Question: What is the role of the transaction manager?

A) Managing users
B) Ensuring ACID properties and coordinating transaction execution
C) Managing storage
D) Managing networks

✔ Correct Answer: B

Reason: The transaction manager ensures ACID properties are maintained and coordinates concurrent transaction execution.

Tag: Normal

---

### Question 664
Domain: Databases
Topic: Database System Architecture
Subtopic: Concurrency Control Manager
Difficulty: Medium

Question: What is the role of the concurrency control manager?

A) Managing users
B) Coordinating concurrent access to ensure serializability
C) Managing backups
D) Managing networks

✔ Correct Answer: B

Reason: The concurrency control manager coordinates concurrent data access to maintain consistency and serializability.

Tag: Normal

---

### Question 665
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relation vs Table
Difficulty: Easy

Question: What is the difference between a relation and a table?

A) Major difference
B) Relation is the formal term, table is the implementation
C) Table is formal
D) No connection

✔ Correct Answer: B

Reason: Relation is the formal mathematical term in relational theory, while table is the practical implementation term.

Tag: Normal

---

### Question 666
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Tuple vs Row
Difficulty: Easy

Question: What is the difference between a tuple and a row?

A) Major difference
B) Tuple is the formal term, row is the implementation
C) Row is formal
D) No connection

✔ Correct Answer: B

Reason: Tuple is the formal term in relational theory, while row is the practical implementation term.

Tag: Normal

---

### Question 667
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization Levels
Difficulty: Easy

Question: Which normal form is considered sufficient for most practical applications?

A) 1NF
B) 3NF or BCNF
C) 5NF
D) No normalization

✔ Correct Answer: B

Reason: 3NF or BCNF is generally considered sufficient for most practical applications, balancing normalization benefits with complexity.

Tag: Normal

---

### Question 668
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Higher Normal Forms
Difficulty: Hard

Question: When is 4NF or 5NF necessary?

A) Always
B) When dealing with complex multi-valued or join dependencies
C) Never
D) For all databases

✔ Correct Answer: B

Reason: 4NF and 5NF are needed only for complex scenarios involving multi-valued dependencies or join dependencies.

Tag: Normal

---

### Question 669
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Lifecycle
Difficulty: Medium

Question: What are the possible final states of a transaction?

A) Only Active
B) Committed or Aborted
C) Only Committed
D) Only Failed

✔ Correct Answer: B

Reason: A transaction ultimately ends in either Committed state (successful) or Aborted state (rolled back).

Tag: Normal

---

### Question 670
Domain: Databases
Topic: Transaction Management
Subtopic: Savepoints
Difficulty: Medium

Question: What is the benefit of using savepoints?

A) No benefit
B) Allows partial rollback without aborting entire transaction
C) Slows down transactions
D) Increases complexity only

✔ Correct Answer: B

Reason: Savepoints allow rolling back to a specific point within a transaction without aborting the entire transaction.

Tag: Normal

---

### Question 671
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Compatibility
Difficulty: Medium

Question: Can two exclusive locks be held on the same data item simultaneously?

A) Yes
B) No
C) Sometimes
D) Always

✔ Correct Answer: B

Reason: Exclusive locks are incompatible with all other locks; only one transaction can hold an exclusive lock at a time.

Tag: Normal

---

### Question 672
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Modes
Difficulty: Medium

Question: What is an update lock?

A) A shared lock
B) A lock that can be upgraded to exclusive, preventing deadlocks
C) An exclusive lock
D) No lock

✔ Correct Answer: B

Reason: Update locks allow reading while indicating intention to update, and can be upgraded to exclusive locks, preventing certain deadlocks.

Tag: Normal

---

### Question 673
Domain: Databases
Topic: Recovery Management
Subtopic: Log Types
Difficulty: Medium

Question: What is a physical log?

A) A logical log
B) A log recording physical changes to disk blocks
C) No log
D) A deleted log

✔ Correct Answer: B

Reason: Physical logs record actual byte-level changes to disk blocks, enabling physical recovery.

Tag: Normal

---

### Question 674
Domain: Databases
Topic: Recovery Management
Subtopic: Log Types
Difficulty: Medium

Question: What is a logical log?

A) A physical log
B) A log recording logical operations (like INSERT, UPDATE)
C) No log
D) A deleted log

✔ Correct Answer: B

Reason: Logical logs record high-level operations (INSERT, UPDATE, DELETE) rather than physical byte changes.

Tag: Normal

---

### Question 675
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Selection
Difficulty: Medium

Question: Should you index columns with very low cardinality?

A) Always
B) Generally no, as the index provides little benefit
C) Always beneficial
D) Doesn't matter

✔ Correct Answer: B

Reason: Low cardinality columns (few distinct values) benefit little from indexing as many rows share the same value.

Tag: Normal

---

### Question 676
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Selection
Difficulty: Medium

Question: Should you index columns frequently used in WHERE clauses?

A) No
B) Yes, they are good candidates for indexing
C) Never
D) Doesn't matter

✔ Correct Answer: B

Reason: Columns frequently used in WHERE clauses benefit significantly from indexing, speeding up query execution.

Tag: Normal

---

### Question 677
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Transformation
Difficulty: Hard

Question: What is predicate pushdown?

A) Deleting predicates
B) Moving filter conditions closer to data sources
C) Adding predicates
D) No transformation

✔ Correct Answer: B

Reason: Predicate pushdown moves filter conditions (WHERE clauses) as close to data sources as possible to reduce data processed.

Tag: Normal

---

### Question 678
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Transformation
Difficulty: Hard

Question: What is join reordering?

A) Random ordering
B) Changing the order of joins to minimize intermediate result sizes
C) No reordering
D) Alphabetical ordering

✔ Correct Answer: B

Reason: Join reordering changes the sequence of join operations to minimize intermediate result sizes and improve performance.

Tag: Normal

---

### Question 679
Domain: Databases
Topic: Database Security
Subtopic: Encryption
Difficulty: Easy

Question: What is the purpose of encrypting database backups?

A) To compress them
B) To protect data if backups are stolen or accessed
C) To speed up backups
D) No purpose

✔ Correct Answer: B

Reason: Encrypting backups protects sensitive data from unauthorized access if backup media is stolen or compromised.

Tag: Normal

---

### Question 680
Domain: Databases
Topic: Database Security
Subtopic: Auditing
Difficulty: Easy

Question: What is database auditing?

A) Deleting logs
B) Recording and monitoring database activities for security and compliance
C) Backing up data
D) Encrypting data

✔ Correct Answer: B

Reason: Database auditing records and monitors database activities to detect security violations and ensure compliance.

Tag: Normal

---

### Question 681
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Allocation Strategies
Difficulty: Medium

Question: What is centralized data allocation?

A) Data at all sites
B) All data stored at a single site
C) Random allocation
D) No allocation

✔ Correct Answer: B

Reason: Centralized allocation stores all data at a single site, simplest but creates a single point of failure.

Tag: Normal

---

### Question 682
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Allocation Strategies
Difficulty: Medium

Question: What is partitioned data allocation?

A) No partitioning
B) Data divided among sites with no replication
C) All data everywhere
D) Random allocation

✔ Correct Answer: B

Reason: Partitioned allocation divides data among sites without replication, each fragment stored at one site.

Tag: Normal

---

### Question 683
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Levels
Difficulty: Medium

Question: What is eventual consistency?

A) Immediate consistency
B) System becomes consistent over time if no new updates
C) Never consistent
D) Always consistent

✔ Correct Answer: B

Reason: Eventual consistency guarantees that without new updates, all replicas will eventually converge to the same value.

Tag: Normal

---

### Question 684
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Levels
Difficulty: Medium

Question: What is strong consistency?

A) Weak consistency
B) All reads return the most recent write immediately
C) Delayed consistency
D) No consistency

✔ Correct Answer: B

Reason: Strong consistency ensures all reads immediately return the value of the most recent write.

Tag: Normal

---

### Question 685
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mart
Difficulty: Easy

Question: How does a data mart differ from a data warehouse?

A) No difference
B) Data mart is smaller, focused on specific subject area
C) Data mart is larger
D) Data mart is older

✔ Correct Answer: B

Reason: A data mart is a subset of a data warehouse, focused on a specific business area or department.

Tag: Normal

---

### Question 686
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP vs OLTP
Difficulty: Medium

Question: What is the main difference in query patterns between OLAP and OLTP?

A) No difference
B) OLAP has complex analytical queries, OLTP has simple transactional queries
C) OLTP is more complex
D) Same queries

✔ Correct Answer: B

Reason: OLAP involves complex analytical queries on large datasets, while OLTP handles simple, frequent transactional queries.

Tag: Past Paper

---

### Question 687
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Performance Tips
Difficulty: Medium

Question: Why should you avoid using SELECT DISTINCT unnecessarily?

A) It's faster
B) It adds overhead for duplicate elimination
C) It's required
D: No reason

✔ Correct Answer: B

Reason: DISTINCT adds overhead for sorting/hashing to eliminate duplicates; avoid it if duplicates don't matter.

Tag: Normal

---

### Question 688
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Performance Tips
Difficulty: Medium

Question: Why should you use EXISTS instead of IN for large subqueries?

A) No difference
B) EXISTS can short-circuit and is often more efficient
C) IN is always faster
D) Doesn't matter

✔ Correct Answer: B

Reason: EXISTS can stop searching once a match is found (short-circuit), often more efficient than IN for large subqueries.

Tag: Normal

---

### Question 689
Domain: Databases
Topic: Advanced SQL
Subtopic: Common Table Expressions
Difficulty: Medium

Question: What is an advantage of CTEs over subqueries?

A) No advantage
B) Better readability and can be referenced multiple times
C) Slower execution
D) More complex

✔ Correct Answer: B

Reason: CTEs improve query readability and can be referenced multiple times in the same query, unlike subqueries.

Tag: Normal

---

### Question 690
Domain: Databases
Topic: Advanced SQL
Subtopic: Recursive Queries
Difficulty: Hard

Question: What type of data structure is best queried using recursive CTEs?

A) Flat data
B) Hierarchical or tree-structured data
C) Random data
D) No structure

✔ Correct Answer: B

Reason: Recursive CTEs are ideal for querying hierarchical data like organizational charts, bill of materials, or folder structures.

Tag: Normal

---

### Question 691
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Query Languages
Difficulty: Medium

Question: Is SQL relationally complete?

A) No
B) Yes, it can express all relational algebra queries
C) Partially
D) Unknown

✔ Correct Answer: B

Reason: SQL is relationally complete as it can express any query that can be expressed in relational algebra.

Tag: Past Paper

---

### Question 692
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Process
Difficulty: Easy

Question: What is the first step in database design?

A) Creating tables
B) Requirements analysis
C) Normalization
D) Implementation

✔ Correct Answer: B

Reason: Database design begins with requirements analysis to understand what data needs to be stored and how it will be used.

Tag: Normal

---

### Question 693
Domain: Databases
Topic: Database Design & Normalization
Subtopic: ER Modeling
Difficulty: Easy

Question: What does an ER diagram represent?

A) Physical storage
B) Conceptual data model with entities and relationships
C) Query execution
D) Network topology

✔ Correct Answer: B

Reason: ER diagrams represent the conceptual data model, showing entities, attributes, and relationships.

Tag: Normal

---

### Question 694
Domain: Databases
Topic: Transaction Management
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is the prepare phase in two-phase commit?

A) Final commit
B) Coordinator asks participants if they can commit
C) Rollback phase
D) No phase

✔ Correct Answer: B

Reason: In the prepare phase, the coordinator asks all participants if they are ready to commit the transaction.

Tag: Past Paper

---

### Question 695
Domain: Databases
Topic: Transaction Management
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is the commit phase in two-phase commit?

A) Prepare phase
B) Coordinator tells participants to commit or abort based on votes
C) Rollback only
D) No phase

✔ Correct Answer: B

Reason: In the commit phase, the coordinator instructs all participants to either commit (if all voted yes) or abort.

Tag: Past Paper

---

### Question 696
Domain: Databases
Topic: Concurrency Control
Subtopic: Serializability
Difficulty: Hard

Question: Is every serializable schedule conflict serializable?

A) Yes
B) No, some are view serializable but not conflict serializable
C) Always
D) Never

✔ Correct Answer: B

Reason: Some schedules are view serializable but not conflict serializable; conflict serializability is a subset of view serializability.

Tag: Past Paper

---

### Question 697
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Techniques
Difficulty: Hard

Question: What is the difference between immediate and deferred update?

A) No difference
B) Immediate writes to disk before commit, deferred writes after commit
C) Immediate is slower
D) Deferred is not used

✔ Correct Answer: B

Reason: Immediate update writes changes to disk before commit (needs undo/redo), deferred waits until commit (needs only redo).

Tag: Past Paper

---

### Question 698
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Maintenance
Difficulty: Medium

Question: What is index reorganization?

A) Deleting indexes
B) Defragmenting and optimizing index structure
C) Creating new indexes
D) No maintenance

✔ Correct Answer: B

Reason: Index reorganization defragments and optimizes the index structure to improve performance without full rebuild.

Tag: Normal

---

### Question 699
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Statistics
Difficulty: Medium

Question: What statistics does the optimizer use?

A) No statistics
B) Table size, index selectivity, data distribution
C) Only table names
D) Only user information

✔ Correct Answer: B

Reason: The optimizer uses statistics like table size, index selectivity, and data distribution to estimate query costs.

Tag: Normal

---

### Question 700
Domain: Databases
Topic: Database Security
Subtopic: Best Practices
Difficulty: Easy

Question: What is a database security best practice?

A) Share passwords
B) Implement least privilege, regular audits, and encryption
C) Disable all security
D) Allow all access

✔ Correct Answer: B

Reason: Best practices include implementing least privilege, conducting regular security audits, and encrypting sensitive data.

Tag: Normal

---

**End of Batch 07**

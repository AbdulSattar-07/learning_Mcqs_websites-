# Databases MCQ Bank - Batch 09

## Questions 801-900

---

### Question 801
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT department, 
       COUNT(*) as total_emp,
       COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () as percentage
FROM employees
GROUP BY department;
```

A) Only counts
B) Each department with employee count and percentage of total
C) Only percentages
D) Error

✔ Correct Answer: B

Reason: The query calculates each department's employee count and its percentage of the total workforce using a window function.

Tag: Normal

---

### Question 802
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT name, hire_date,
       DATEDIFF(CURRENT_DATE, hire_date) / 365 as years_employed
FROM employees
WHERE DATEDIFF(CURRENT_DATE, hire_date) / 365 >= 5;
```

A) All employees
B) Employees with 5 or more years of service
C) New employees
D) Error

✔ Correct Answer: B

Reason: The query calculates years of employment and filters to show only employees with 5 or more years of service.

Tag: Normal

---

### Question 803
Domain: Databases
Topic: Advanced SQL
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this recursive CTE calculate?
```sql
WITH RECURSIVE numbers AS (
  SELECT 1 as n
  UNION ALL
  SELECT n + 1 FROM numbers WHERE n < 10
)
SELECT * FROM numbers;
```

A) Random numbers
B) Numbers from 1 to 10
C) Only 1
D) Error

✔ Correct Answer: B

Reason: This recursive CTE generates a sequence of numbers from 1 to 10.

Tag: Normal

---

### Question 804
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
SELECT product_id, product_name
FROM products
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM sales);
```

A) All products
B) Products that have never been sold
C) Only sold products
D) Error

✔ Correct Answer: B

Reason: The query selects products whose IDs don't appear in the sales table, i.e., products never sold.

Tag: Normal

---

### Question 805
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the output of this query?
```sql
SELECT name, salary,
       CASE 
         WHEN salary >= (SELECT AVG(salary) FROM employees) THEN 'Above Average'
         ELSE 'Below Average'
       END as salary_category
FROM employees;
```

A) Only salaries
B) Each employee categorized as above or below average salary
C) Only names
D) Error

✔ Correct Answer: B

Reason: The query categorizes each employee based on whether their salary is above or below the company average.

Tag: Normal

---

### Question 806
Domain: Databases
Topic: Database System Architecture
Subtopic: Database Architecture
Difficulty: Easy

Question: What is a two-tier database architecture?

A) Three tiers
B) Client directly connects to database server
C) One tier
D) No tiers

✔ Correct Answer: B

Reason: Two-tier architecture has clients directly connecting to the database server without an intermediate application server.

Tag: Normal

---

### Question 807
Domain: Databases
Topic: Database System Architecture
Subtopic: Database Architecture
Difficulty: Easy

Question: What is a three-tier database architecture?

A) Two tiers
B) Client, application server, and database server
C) One tier
D) No tiers

✔ Correct Answer: B

Reason: Three-tier architecture separates presentation (client), application logic (middle tier), and data management (database server).

Tag: Normal

---

### Question 808
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relational Model
Difficulty: Easy

Question: Who proposed the relational model?

A) Bill Gates
B) E.F. Codd
C) Larry Ellison
D) Steve Jobs

✔ Correct Answer: B

Reason: E.F. Codd proposed the relational model in 1970, revolutionizing database management.

Tag: Past Paper

---

### Question 809
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relational Model
Difficulty: Medium

Question: What is the foundation of the relational model?

A) Objects
B) Mathematical set theory and predicate logic
C) Networks
D) Hierarchies

✔ Correct Answer: B

Reason: The relational model is based on mathematical set theory and first-order predicate logic.

Tag: Past Paper

---

### Question 810
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Principles
Difficulty: Easy

Question: What is the goal of good database design?

A) Maximum redundancy
B) Minimize redundancy while ensuring data integrity
C) Complex structure
D) Random organization

✔ Correct Answer: B

Reason: Good database design minimizes redundancy while ensuring data integrity, consistency, and efficient access.

Tag: Normal

---

### Question 811
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Process
Difficulty: Medium

Question: What comes after conceptual design in the database design process?

A) Implementation
B) Logical design
C) Physical design
D) Requirements analysis

✔ Correct Answer: B

Reason: The design process flows: Requirements → Conceptual → Logical → Physical → Implementation.

Tag: Normal

---

### Question 812
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Types
Difficulty: Easy

Question: What is a flat transaction?

A) Complex transaction
B) Simple transaction with no nested structure
C) Distributed transaction
D) Failed transaction

✔ Correct Answer: B

Reason: A flat transaction is a simple transaction without nested subtransactions or savepoints.

Tag: Normal

---

### Question 813
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Types
Difficulty: Medium

Question: What is a nested transaction?

A) Flat transaction
B) Transaction containing subtransactions
C) Failed transaction
D) No transaction

✔ Correct Answer: B

Reason: Nested transactions allow transactions to contain subtransactions, providing hierarchical transaction structure.

Tag: Normal

---

### Question 814
Domain: Databases
Topic: Concurrency Control
Subtopic: Concurrency Problems
Difficulty: Medium

Question: What is the write-write conflict?

A) Two reads
B) Two transactions writing to the same data item
C) Read and write
D) No conflict

✔ Correct Answer: B

Reason: Write-write conflict (lost update) occurs when two transactions write to the same data item, potentially losing one update.

Tag: Past Paper

---

### Question 815
Domain: Databases
Topic: Concurrency Control
Subtopic: Concurrency Problems
Difficulty: Medium

Question: What is the read-write conflict?

A) Two reads
B) One transaction reads while another writes the same data
C) Two writes
D) No conflict

✔ Correct Answer: B

Reason: Read-write conflict (unrepeatable read) occurs when one transaction reads data that another transaction is modifying.

Tag: Past Paper

---

### Question 816
Domain: Databases
Topic: Recovery Management
Subtopic: Failure Classification
Difficulty: Easy

Question: What is a transaction failure?

A) System crash
B) Logical error or constraint violation causing abort
C) Disk failure
D) Network failure

✔ Correct Answer: B

Reason: Transaction failure occurs due to logical errors, constraint violations, or deadlocks causing the transaction to abort.

Tag: Normal

---

### Question 817
Domain: Databases
Topic: Recovery Management
Subtopic: Failure Classification
Difficulty: Easy

Question: What is a media failure?

A) Transaction error
B) Physical damage to storage media
C) Network error
D) User error

✔ Correct Answer: B

Reason: Media failure involves physical damage to storage devices, requiring restoration from backups.

Tag: Normal

---

### Question 818
Domain: Databases
Topic: Indexing & File Organization
Subtopic: File Organization
Difficulty: Easy

Question: What is sequential file organization?

A) Random order
B) Records stored in sorted order by key
C) No organization
D) Hash-based

✔ Correct Answer: B

Reason: Sequential file organization stores records in sorted order based on a key field, enabling efficient sequential access.

Tag: Normal

---

### Question 819
Domain: Databases
Topic: Indexing & File Organization
Subtopic: File Organization
Difficulty: Easy

Question: What is heap file organization?

A) Sorted order
B) Records stored in no particular order
C) Hash-based
D) Tree-based

✔ Correct Answer: B

Reason: Heap file organization stores records in no particular order, typically in insertion order.

Tag: Normal

---

### Question 820
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Processing Steps
Difficulty: Medium

Question: What is query parsing?

A) Executing query
B) Checking syntax and translating to internal form
C) Optimizing query
D) Returning results

✔ Correct Answer: B

Reason: Query parsing checks SQL syntax and translates the query into an internal representation.

Tag: Normal

---

### Question 821
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Processing Steps
Difficulty: Medium

Question: What is query translation?

A) Language translation
B) Converting SQL to relational algebra or similar representation
C) Executing query
D) Returning results

✔ Correct Answer: B

Reason: Query translation converts SQL into an internal representation like relational algebra for processing.

Tag: Normal

---

### Question 822
Domain: Databases
Topic: Database Security
Subtopic: Security Levels
Difficulty: Easy

Question: What is physical security in databases?

A) Logical security
B) Protecting physical hardware and facilities
C) Software security
D) Network security

✔ Correct Answer: B

Reason: Physical security protects the physical hardware, servers, and facilities housing the database.

Tag: Normal

---

### Question 823
Domain: Databases
Topic: Database Security
Subtopic: Security Levels
Difficulty: Easy

Question: What is logical security in databases?

A) Physical security
B) Controlling access to data through authentication and authorization
C) Hardware security
D) Building security

✔ Correct Answer: B

Reason: Logical security controls who can access what data through authentication, authorization, and access controls.

Tag: Normal

---

### Question 824
Domain: Databases
Topic: Distributed Databases
Subtopic: Distribution Strategies
Difficulty: Medium

Question: What is replicated data allocation?

A) No replication
B) Data copies stored at multiple sites
C) Data at one site only
D) Random allocation

✔ Correct Answer: B

Reason: Replicated allocation stores copies of data at multiple sites for improved availability and performance.

Tag: Normal

---

### Question 825
Domain: Databases
Topic: Distributed Databases
Subtopic: Distribution Strategies
Difficulty: Medium

Question: What is hybrid data allocation?

A) One strategy only
B) Combination of partitioning and replication
C) No allocation
D) Random allocation

✔ Correct Answer: B

Reason: Hybrid allocation combines partitioning and replication strategies to optimize performance and availability.

Tag: Normal

---

### Question 826
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: NoSQL Categories
Difficulty: Easy

Question: What are the main categories of NoSQL databases?

A) Only one type
B) Key-value, document, column-family, and graph
C) Only relational
D) No categories

✔ Correct Answer: B

Reason: NoSQL databases are categorized into key-value stores, document databases, column-family stores, and graph databases.

Tag: Normal

---

### Question 827
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Schema Flexibility
Difficulty: Easy

Question: What does schema-on-read mean?

A) Fixed schema
B) Schema applied when data is read, not when written
C) No schema ever
D) Schema on write

✔ Correct Answer: B

Reason: Schema-on-read applies structure when data is read, allowing flexible storage of varied data structures.

Tag: Normal

---

### Question 828
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Warehouse Architecture
Difficulty: Medium

Question: What is a staging area in data warehousing?

A) Final storage
B) Temporary storage for data transformation before loading
C) User interface
D) Backup area

✔ Correct Answer: B

Reason: The staging area temporarily stores data during ETL processing before it's loaded into the warehouse.

Tag: Normal

---

### Question 829
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Warehouse Architecture
Difficulty: Medium

Question: What is metadata in a data warehouse?

A) User data
B) Data about the warehouse structure, sources, and transformations
C) Backup data
D) Deleted data

✔ Correct Answer: B

Reason: Metadata describes the warehouse structure, data sources, transformation rules, and refresh schedules.

Tag: Normal

---

### Question 830
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Data Types
Difficulty: Easy

Question: Which SQL data type stores whole numbers?

A) FLOAT
B) INTEGER or INT
C) VARCHAR
D) DATE

✔ Correct Answer: B

Reason: INTEGER (or INT) data type stores whole numbers without decimal points.

Tag: Normal

---

### Question 831
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Data Types
Difficulty: Easy

Question: Which SQL data type stores variable-length character strings?

A) INT
B) VARCHAR
C) DATE
D) BOOLEAN

✔ Correct Answer: B

Reason: VARCHAR stores variable-length character strings up to a specified maximum length.

Tag: Normal

---

### Question 832
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Data Types
Difficulty: Easy

Question: Which SQL data type stores date and time?

A) VARCHAR
B) DATETIME or TIMESTAMP
C) INT
D) BOOLEAN

✔ Correct Answer: B

Reason: DATETIME or TIMESTAMP data types store date and time information.

Tag: Normal

---

### Question 833
Domain: Databases
Topic: Advanced SQL
Subtopic: Transactions
Difficulty: Medium

Question: What is implicit transaction mode?

A) Manual transactions
B) Each statement automatically starts and commits a transaction
C) No transactions
D) Explicit only

✔ Correct Answer: B

Reason: In implicit (autocommit) mode, each SQL statement automatically starts and commits its own transaction.

Tag: Normal

---

### Question 834
Domain: Databases
Topic: Advanced SQL
Subtopic: Transactions
Difficulty: Medium

Question: What is explicit transaction mode?

A) Automatic transactions
B) Transactions must be explicitly started and committed
C) No transactions
D) Implicit only

✔ Correct Answer: B

Reason: In explicit mode, transactions must be explicitly started with BEGIN and ended with COMMIT or ROLLBACK.

Tag: Normal

---

### Question 835
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Operators
Difficulty: Medium

Question: What does the assignment operator (←) do in relational algebra?

A) Compares relations
B) Assigns the result of an expression to a relation variable
C) Deletes relations
D) No function

✔ Correct Answer: B

Reason: The assignment operator assigns the result of a relational algebra expression to a relation variable.

Tag: Past Paper

---

### Question 836
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Extended Operators
Difficulty: Hard

Question: What is the outer union operation?

A) Regular union
B) Union of relations with different schemas
C) Intersection
D) Difference

✔ Correct Answer: B

Reason: Outer union combines relations with different schemas, padding with NULLs where attributes don't match.

Tag: Normal

---

### Question 837
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Patterns
Difficulty: Medium

Question: What is a junction table?

A) A regular table
B) A table implementing many-to-many relationships
C) A deleted table
D) A backup table

✔ Correct Answer: B

Reason: A junction (bridge/associative) table implements many-to-many relationships by containing foreign keys to both related tables.

Tag: Normal

---

### Question 838
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Design Patterns
Difficulty: Medium

Question: What is a self-referencing table?

A) No references
B) A table with a foreign key referencing its own primary key
C) Two tables
D) A deleted table

✔ Correct Answer: B

Reason: A self-referencing table has a foreign key that references its own primary key, useful for hierarchical data.

Tag: Normal

---

### Question 839
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Control
Difficulty: Easy

Question: What does SET TRANSACTION do?

A) Executes transaction
B) Sets transaction characteristics like isolation level
C) Deletes transaction
D) Backs up transaction

✔ Correct Answer: B

Reason: SET TRANSACTION sets characteristics for the current transaction, such as isolation level or access mode.

Tag: Normal

---

### Question 840
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Control
Difficulty: Medium

Question: What is READ ONLY transaction mode?

A) Write only
B) Transaction can only read data, not modify it
C) Full access
D) No access

✔ Correct Answer: B

Reason: READ ONLY mode restricts the transaction to read operations only, preventing any data modifications.

Tag: Normal

---

### Question 841
Domain: Databases
Topic: Concurrency Control
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level is most prone to anomalies?

A) Serializable
B) Read Uncommitted
C) Repeatable Read
D) Read Committed

✔ Correct Answer: B

Reason: Read Uncommitted allows all anomalies (dirty reads, non-repeatable reads, phantom reads) for maximum concurrency.

Tag: Normal

---

### Question 842
Domain: Databases
Topic: Concurrency Control
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level prevents all anomalies?

A) Read Uncommitted
B) Read Committed
C) Repeatable Read
D) Serializable

✔ Correct Answer: D

Reason: Serializable prevents all anomalies by providing complete isolation, equivalent to serial execution.

Tag: Normal

---

### Question 843
Domain: Databases
Topic: Recovery Management
Subtopic: Backup Strategies
Difficulty: Easy

Question: What is the 3-2-1 backup strategy?

A) 3 servers, 2 databases, 1 backup
B) 3 copies, 2 different media, 1 offsite
C) 3 backups only
D) No strategy

✔ Correct Answer: B

Reason: 3-2-1 strategy: keep 3 copies of data, on 2 different media types, with 1 copy offsite.

Tag: Normal

---

### Question 844
Domain: Databases
Topic: Recovery Management
Subtopic: Backup Strategies
Difficulty: Medium

Question: What is a snapshot backup?

A) Full backup
B) Point-in-time copy of database state
C) Incremental backup
D) No backup

✔ Correct Answer: B

Reason: A snapshot creates a point-in-time copy of the database state, useful for quick recovery.

Tag: Normal

---

### Question 845
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Types
Difficulty: Medium

Question: What is a reverse key index?

A) Regular index
B) Index with reversed key values to distribute data evenly
C) Backward index
D) Deleted index

✔ Correct Answer: B

Reason: Reverse key indexes reverse the bytes of the key value to distribute sequential keys evenly, reducing contention.

Tag: Normal

---

### Question 846
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Types
Difficulty: Hard

Question: What is a bitmap join index?

A) Regular index
B) Bitmap index on join results between tables
C) Simple bitmap
D) Deleted index

✔ Correct Answer: B

Reason: Bitmap join indexes are built on the join of two or more tables, optimizing star schema queries.

Tag: Normal

---

### Question 847
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Optimization Techniques
Difficulty: Hard

Question: What is common subexpression elimination?

A) Adding expressions
B) Identifying and computing repeated subexpressions once
C) Deleting expressions
D) No optimization

✔ Correct Answer: B

Reason: Common subexpression elimination identifies repeated subexpressions and computes them once, reusing the result.

Tag: Normal

---

### Question 848
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Optimization Techniques
Difficulty: Hard

Question: What is constant folding?

A) Variable evaluation
B) Evaluating constant expressions at compile time
C) No evaluation
D) Runtime evaluation only

✔ Correct Answer: B

Reason: Constant folding evaluates constant expressions during query compilation rather than at runtime.

Tag: Normal

---

### Question 849
Domain: Databases
Topic: Database Security
Subtopic: Security Threats
Difficulty: Easy

Question: What is unauthorized access?

A) Authorized access
B) Accessing data without proper permissions
C) Normal access
D) No access

✔ Correct Answer: B

Reason: Unauthorized access occurs when someone accesses data or systems without proper authentication or authorization.

Tag: Normal

---

### Question 850
Domain: Databases
Topic: Database Security
Subtopic: Security Threats
Difficulty: Easy

Question: What is data breach?

A) Normal operation
B) Unauthorized access and extraction of sensitive data
C) Authorized access
D) Data backup

✔ Correct Answer: B

Reason: A data breach is an incident where sensitive data is accessed, stolen, or used by unauthorized parties.

Tag: Normal

---

### Question 851
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Query Processing
Difficulty: Hard

Question: What is query shipping?

A) Shipping data
B) Sending query to data location for execution
C) No shipping
D) Random shipping

✔ Correct Answer: B

Reason: Query shipping sends the query to the site where data resides, executing it there to minimize data transfer.

Tag: Normal

---

### Question 852
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Query Processing
Difficulty: Hard

Question: What is data shipping?

A) Shipping queries
B) Transferring data to query location for processing
C) No shipping
D) Random shipping

✔ Correct Answer: B

Reason: Data shipping transfers data to the site where the query originated for local processing.

Tag: Normal

---

### Question 853
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Models
Difficulty: Hard

Question: What is causal consistency?

A) No consistency
B) Causally related operations are seen in the same order by all nodes
C) Strong consistency
D) Random consistency

✔ Correct Answer: B

Reason: Causal consistency ensures that causally related operations are seen in the same order by all nodes.

Tag: Normal

---

### Question 854
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Models
Difficulty: Hard

Question: What is session consistency?

A) No consistency
B) Consistency within a client session
C) Global consistency
D) Random consistency

✔ Correct Answer: B

Reason: Session consistency guarantees consistency within a single client session, but not across different sessions.

Tag: Normal

---

### Question 855
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining Algorithms
Difficulty: Medium

Question: What is the Apriori algorithm used for?

A) Sorting data
B) Finding frequent itemsets and association rules
C) Deleting data
D) Backing up data

✔ Correct Answer: B

Reason: Apriori algorithm discovers frequent itemsets and generates association rules from transactional data.

Tag: Normal

---

### Question 856
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining Algorithms
Difficulty: Medium

Question: What is the FP-Growth algorithm?

A) Sorting algorithm
B) Frequent pattern mining without candidate generation
C) Deletion algorithm
D) Backup algorithm

✔ Correct Answer: B

Reason: FP-Growth (Frequent Pattern Growth) mines frequent patterns without generating candidate itemsets, using a tree structure.

Tag: Normal

---

### Question 857
Domain: Databases
Topic: Introduction to Database Systems
Subtopic: Database Evolution
Difficulty: Easy

Question: What was the first generation of database systems?

A) Relational
B) File systems and hierarchical databases
C) NoSQL
D) Cloud databases

✔ Correct Answer: B

Reason: First-generation databases included file systems and hierarchical databases like IMS in the 1960s.

Tag: Normal

---

### Question 858
Domain: Databases
Topic: Introduction to Database Systems
Subtopic: Database Evolution
Difficulty: Easy

Question: When did relational databases become mainstream?

A) 1960s
B) 1980s-1990s
C) 2000s
D) 2020s

✔ Correct Answer: B

Reason: Relational databases became mainstream in the 1980s-1990s with systems like Oracle, DB2, and SQL Server.

Tag: Normal

---

### Question 859
Domain: Databases
Topic: Database System Architecture
Subtopic: DBMS Components
Difficulty: Medium

Question: What is the query processor in DBMS?

A) Storage manager
B) Component that interprets and executes queries
C) User interface
D) Backup system

✔ Correct Answer: B

Reason: The query processor interprets, optimizes, and executes database queries.

Tag: Normal

---

### Question 860
Domain: Databases
Topic: Database System Architecture
Subtopic: DBMS Components
Difficulty: Medium

Question: What is the storage manager in DBMS?

A) Query processor
B) Component managing physical storage and data access
C) User interface
D) Network manager

✔ Correct Answer: B

Reason: The storage manager handles physical storage, file organization, buffer management, and data access.

Tag: Normal

---

### Question 861
Domain: Databases
Topic: Data Models
Subtopic: Object-Oriented Model
Difficulty: Medium

Question: What is encapsulation in object-oriented databases?

A) No protection
B) Bundling data and methods together, hiding internal details
C) Exposing everything
D) Deleting data

✔ Correct Answer: B

Reason: Encapsulation bundles data and methods together while hiding internal implementation details.

Tag: Normal

---

### Question 862
Domain: Databases
Topic: Data Models
Subtopic: Object-Oriented Model
Difficulty: Medium

Question: What is inheritance in object-oriented databases?

A) No relationships
B) Ability to derive new classes from existing ones
C) Deleting classes
D) Random relationships

✔ Correct Answer: B

Reason: Inheritance allows new classes to be derived from existing ones, inheriting their properties and methods.

Tag: Normal

---

### Question 863
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relational Constraints
Difficulty: Easy

Question: What is a CHECK constraint?

A) No constraint
B) Constraint that validates data against a condition
C) Foreign key
D) Primary key

✔ Correct Answer: B

Reason: CHECK constraint validates that data in a column meets a specified condition or rule.

Tag: Normal

---

### Question 864
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relational Constraints
Difficulty: Easy

Question: What is a DEFAULT constraint?

A) No default
B) Specifies a default value for a column
C) Foreign key
D) Primary key

✔ Correct Answer: B

Reason: DEFAULT constraint specifies a default value to be used when no value is provided for a column.

Tag: Normal

---

### Question 865
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query return?
```sql
SELECT customer_id, COUNT(*) as order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;
```

A) All customers
B) Customers with more than 5 orders
C) Customers with exactly 5 orders
D) Error

✔ Correct Answer: B

Reason: The HAVING clause filters groups to show only customers with more than 5 orders.

Tag: Normal

---

### Question 866
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT e1.name as employee, e2.name as manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

A) Only employees with managers
B) All employees with their managers (NULL for top-level)
C) Only managers
D) Error

✔ Correct Answer: B

Reason: Self-join with LEFT JOIN shows all employees and their managers, with NULL for employees without managers.

Tag: Normal

---

### Question 867
Domain: Databases
Topic: Advanced SQL
Subtopic: Window Functions
Difficulty: Hard

Question: What does ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW mean?

A) Current row only
B) From start of partition to current row
C) All rows
D) Error

✔ Correct Answer: B

Reason: This frame specification includes all rows from the start of the partition up to and including the current row.

Tag: Normal

---

### Question 868
Domain: Databases
Topic: Advanced SQL
Subtopic: Window Functions
Difficulty: Hard

Question: What does RANGE BETWEEN do in window functions?

A) Row-based frame
B) Value-based frame specification
C) No frame
D) Error

✔ Correct Answer: B

Reason: RANGE BETWEEN defines a value-based frame, including rows with values within a specified range.

Tag: Normal

---

### Question 869
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization
Difficulty: Medium

Question: When is denormalization appropriate?

A) Always
B) When read performance is critical and redundancy is acceptable
C) Never
D) Random times

✔ Correct Answer: B

Reason: Denormalization is appropriate when read performance is critical and the cost of redundancy is acceptable.

Tag: Normal

---

### Question 870
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization
Difficulty: Medium

Question: What is a materialized view?

A) Regular view
B) Precomputed view stored physically for performance
C) Deleted view
D) No view

✔ Correct Answer: B

Reason: A materialized view is a precomputed and physically stored view that improves query performance.

Tag: Normal

---

### Question 871
Domain: Databases
Topic: Transaction Management
Subtopic: Savepoints
Difficulty: Medium

Question: What is a savepoint in transactions?

A) End of transaction
B) Intermediate point to which transaction can be rolled back
C) Start of transaction
D) No point

✔ Correct Answer: B

Reason: A savepoint is an intermediate point within a transaction to which you can roll back without aborting the entire transaction.

Tag: Normal

---

### Question 872
Domain: Databases
Topic: Transaction Management
Subtopic: Savepoints
Difficulty: Medium

Question: What happens when you ROLLBACK TO SAVEPOINT?

A) Full rollback
B) Partial rollback to the specified savepoint
C) Commit
D) Nothing

✔ Correct Answer: B

Reason: ROLLBACK TO SAVEPOINT undoes changes made after the savepoint while keeping earlier changes.

Tag: Normal

---

### Question 873
Domain: Databases
Topic: Concurrency Control
Subtopic: Multiversion Concurrency Control
Difficulty: Hard

Question: What is MVCC?

A) Single version control
B) Maintaining multiple versions of data for concurrent access
C) No version control
D) Backup system

✔ Correct Answer: B

Reason: MVCC (Multiversion Concurrency Control) maintains multiple versions of data to allow concurrent reads and writes.

Tag: Normal

---

### Question 874
Domain: Databases
Topic: Concurrency Control
Subtopic: Multiversion Concurrency Control
Difficulty: Hard

Question: What is the main advantage of MVCC?

A) Slower performance
B) Readers don't block writers and writers don't block readers
C) More locks
D) Less concurrency

✔ Correct Answer: B

Reason: MVCC allows readers and writers to work concurrently without blocking each other, improving performance.

Tag: Normal

---

### Question 875
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Techniques
Difficulty: Medium

Question: What is immediate update recovery?

A) Deferred updates
B) Updates written to database before commit
C) No updates
D) Random updates

✔ Correct Answer: B

Reason: Immediate update writes changes to the database before transaction commits, requiring undo for recovery.

Tag: Normal

---

### Question 876
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Techniques
Difficulty: Medium

Question: What is deferred update recovery?

A) Immediate updates
B) Updates written to database only after commit
C) No updates
D) Random updates

✔ Correct Answer: B

Reason: Deferred update writes changes to the database only after transaction commits, requiring only redo for recovery.

Tag: Normal

---

### Question 877
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Buffer Management
Difficulty: Medium

Question: What is the buffer pool?

A) Disk storage
B) Memory area for caching disk pages
C) User interface
D) Network buffer

✔ Correct Answer: B

Reason: The buffer pool is a memory area that caches frequently accessed disk pages to reduce I/O operations.

Tag: Normal

---

### Question 878
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Buffer Management
Difficulty: Medium

Question: What is the LRU replacement policy?

A) Most recently used
B) Least Recently Used - replaces least recently accessed page
C) Random replacement
D) No replacement

✔ Correct Answer: B

Reason: LRU (Least Recently Used) replaces the page that hasn't been accessed for the longest time.

Tag: Normal

---

### Question 879
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: What is a hash join?

A) Nested loop join
B) Join using hash tables for matching
C) Merge join
D) No join

✔ Correct Answer: B

Reason: Hash join builds a hash table on one relation and probes it with the other relation for matching.

Tag: Normal

---

### Question 880
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: What is a merge join?

A) Hash join
B) Join of two sorted relations by merging
C) Nested loop
D) No join

✔ Correct Answer: B

Reason: Merge join (sort-merge join) merges two sorted relations, efficient when inputs are already sorted.

Tag: Normal

---

### Question 881
Domain: Databases
Topic: Database Security
Subtopic: Encryption
Difficulty: Medium

Question: What is Transparent Data Encryption (TDE)?

A) No encryption
B) Automatic encryption of data at rest
C) Manual encryption
D) Network encryption

✔ Correct Answer: B

Reason: TDE automatically encrypts data at rest (stored data) without requiring application changes.

Tag: Normal

---

### Question 882
Domain: Databases
Topic: Database Security
Subtopic: Encryption
Difficulty: Medium

Question: What is column-level encryption?

A) Table encryption
B) Encrypting specific columns containing sensitive data
C) Database encryption
D) No encryption

✔ Correct Answer: B

Reason: Column-level encryption encrypts specific columns containing sensitive data like credit cards or SSNs.

Tag: Normal

---

### Question 883
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is the two-phase commit protocol?

A) One phase
B) Protocol ensuring atomic commits across distributed sites
C) No protocol
D) Three phases

✔ Correct Answer: B

Reason: Two-phase commit (2PC) ensures all sites in a distributed transaction either commit or abort together.

Tag: Past Paper

---

### Question 884
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What are the phases in two-phase commit?

A) Commit and abort
B) Prepare (voting) and commit (decision)
C) Start and end
D) Read and write

✔ Correct Answer: B

Reason: 2PC has two phases: prepare phase (voting) where sites vote, and commit phase (decision) where coordinator decides.

Tag: Past Paper

---

### Question 885
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Graph Databases
Difficulty: Medium

Question: What is a graph database optimized for?

A) Tables
B) Relationships and connected data
C) Documents
D) Key-value pairs

✔ Correct Answer: B

Reason: Graph databases are optimized for storing and querying highly connected data and relationships.

Tag: Normal

---

### Question 886
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Graph Databases
Difficulty: Medium

Question: What are the main components of a graph database?

A) Tables and rows
B) Nodes (vertices) and edges (relationships)
C) Documents
D) Keys and values

✔ Correct Answer: B

Reason: Graph databases consist of nodes (entities) and edges (relationships) with properties.

Tag: Normal

---

### Question 887
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Operations
Difficulty: Medium

Question: What is drill-down in OLAP?

A) Moving up hierarchy
B) Moving from summary to detailed data
C) Rotating cube
D) Slicing data

✔ Correct Answer: B

Reason: Drill-down navigates from summary data to more detailed data by moving down the hierarchy.

Tag: Normal

---

### Question 888
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Operations
Difficulty: Medium

Question: What is roll-up in OLAP?

A) Moving down hierarchy
B) Moving from detailed to summary data
C) Rotating cube
D) Slicing data

✔ Correct Answer: B

Reason: Roll-up aggregates data by moving up the hierarchy from detailed to summary level.

Tag: Normal

---

### Question 889
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Easy

Question: What does this query do?
```sql
SELECT DISTINCT department
FROM employees;
```

A) All departments with duplicates
B) Unique departments only
C) All employees
D) Error

✔ Correct Answer: B

Reason: DISTINCT removes duplicate values, returning only unique department names.

Tag: Normal

---

### Question 890
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the result of this query?
```sql
SELECT name, salary
FROM employees
WHERE salary BETWEEN 50000 AND 100000;
```

A) Salaries outside range
B) Employees with salaries from 50000 to 100000 inclusive
C) Only 50000
D) Error

✔ Correct Answer: B

Reason: BETWEEN is inclusive, selecting employees with salaries from 50000 to 100000.

Tag: Normal

---

### Question 891
Domain: Databases
Topic: Advanced SQL
Subtopic: Subqueries
Difficulty: Medium

Question: What is a correlated subquery?

A) Independent subquery
B) Subquery that references columns from outer query
C) No subquery
D) Simple subquery

✔ Correct Answer: B

Reason: A correlated subquery references columns from the outer query and is executed once for each row.

Tag: Past Paper

---

### Question 892
Domain: Databases
Topic: Advanced SQL
Subtopic: Subqueries
Difficulty: Medium

Question: What is a scalar subquery?

A) Multiple rows
B) Subquery returning a single value
C) No rows
D) Multiple columns

✔ Correct Answer: B

Reason: A scalar subquery returns exactly one value (one row, one column) and can be used where a single value is expected.

Tag: Normal

---

### Question 893
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Functional Dependencies
Difficulty: Hard

Question: What is a trivial functional dependency?

A) Non-trivial dependency
B) Dependency where right side is subset of left side
C) No dependency
D) Complex dependency

✔ Correct Answer: B

Reason: A trivial functional dependency has the right side as a subset of the left side (e.g., AB → A).

Tag: Past Paper

---

### Question 894
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Functional Dependencies
Difficulty: Hard

Question: What is Armstrong's axioms?

A) Database rules
B) Set of inference rules for functional dependencies
C) Normalization forms
D) No axioms

✔ Correct Answer: B

Reason: Armstrong's axioms are inference rules (reflexivity, augmentation, transitivity) for deriving functional dependencies.

Tag: Past Paper

---

### Question 895
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction States
Difficulty: Easy

Question: What is the active state of a transaction?

A) Completed
B) Transaction is executing operations
C) Aborted
D) Committed

✔ Correct Answer: B

Reason: Active state is when the transaction is executing its read and write operations.

Tag: Normal

---

### Question 896
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction States
Difficulty: Easy

Question: What is the partially committed state?

A) Fully committed
B) Transaction completed but not yet committed
C) Aborted
D) Active

✔ Correct Answer: B

Reason: Partially committed state occurs after the last operation executes but before final commit.

Tag: Normal

---

### Question 897
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Handling
Difficulty: Medium

Question: What is deadlock prevention?

A) Detecting deadlocks
B) Ensuring deadlocks cannot occur by design
C) Recovering from deadlocks
D) Ignoring deadlocks

✔ Correct Answer: B

Reason: Deadlock prevention uses protocols that ensure deadlocks cannot occur by design (e.g., ordering resources).

Tag: Normal

---

### Question 898
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Handling
Difficulty: Medium

Question: What is deadlock detection?

A) Preventing deadlocks
B) Periodically checking for deadlock cycles
C) Ignoring deadlocks
D) No detection

✔ Correct Answer: B

Reason: Deadlock detection periodically checks for cycles in the wait-for graph to identify deadlocks.

Tag: Normal

---

### Question 899
Domain: Databases
Topic: Recovery Management
Subtopic: Checkpointing
Difficulty: Medium

Question: What is a fuzzy checkpoint?

A) Sharp checkpoint
B) Checkpoint that allows transactions to continue during checkpointing
C) No checkpoint
D) Failed checkpoint

✔ Correct Answer: B

Reason: Fuzzy checkpoint allows transactions to continue executing during the checkpointing process, minimizing disruption.

Tag: Normal

---

### Question 900
Domain: Databases
Topic: Recovery Management
Subtopic: Checkpointing
Difficulty: Medium

Question: What is the benefit of checkpointing?

A) Slower recovery
B) Reduces recovery time by limiting log scanning
C) No benefit
D) Increases recovery time

✔ Correct Answer: B

Reason: Checkpointing reduces recovery time by establishing a point from which log scanning can begin, avoiding full log analysis.

Tag: Normal

---

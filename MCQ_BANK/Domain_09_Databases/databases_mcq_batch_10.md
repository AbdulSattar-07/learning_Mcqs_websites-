# Databases MCQ Bank - Batch 10

## Questions 901-1000

---

### Question 901
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Performance
Difficulty: Medium

Question: What is index selectivity?

A) No selectivity
B) Ratio of distinct values to total rows
C) Random selection
D) All values

✔ Correct Answer: B

Reason: Index selectivity measures how unique the indexed values are, calculated as distinct values divided by total rows.

Tag: Normal

---

### Question 902
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Performance
Difficulty: Medium

Question: When is a full table scan more efficient than using an index?

A) Never
B) When selecting a large percentage of rows
C) Always
D) Random times

✔ Correct Answer: B

Reason: Full table scan is more efficient when selecting a large percentage of rows (typically >15-20%) due to index overhead.

Tag: Normal

---

### Question 903
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Cost Estimation
Difficulty: Hard

Question: What factors affect query cost estimation?

A) Only CPU
B) I/O cost, CPU cost, memory usage, and network cost
C) Only memory
D) No factors

✔ Correct Answer: B

Reason: Query cost estimation considers I/O operations, CPU processing, memory usage, and network transfer costs.

Tag: Normal

---

### Question 904
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Statistics
Difficulty: Medium

Question: What are database statistics used for?

A) Backup
B) Query optimization and cost estimation
C) User management
D: Security

✔ Correct Answer: B

Reason: Database statistics (cardinality, distribution) help the optimizer estimate costs and choose efficient execution plans.

Tag: Normal

---

### Question 905
Domain: Databases
Topic: Database Security
Subtopic: SQL Injection
Difficulty: Easy

Question: What is SQL injection?

A) Normal query
B: Malicious SQL code inserted through user input
C) Database backup
D) Index creation

✔ Correct Answer: B

Reason: SQL injection is a security vulnerability where attackers insert malicious SQL code through user input fields.

Tag: Past Paper

---

### Question 906
Domain: Databases
Topic: Database Security
Subtopic: SQL Injection
Difficulty: Medium

Question: How can SQL injection be prevented?

A) No prevention
B) Parameterized queries and input validation
C) Disable database
D) Remove all queries

✔ Correct Answer: B

Reason: SQL injection is prevented using parameterized queries (prepared statements), input validation, and proper escaping.

Tag: Past Paper

---

### Question 907
Domain: Databases
Topic: Distributed Databases
Subtopic: CAP Theorem
Difficulty: Hard

Question: What does CAP theorem state?

A) All three guaranteed
B) Distributed system can provide only two of: Consistency, Availability, Partition tolerance
C) None guaranteed
D: One guaranteed

✔ Correct Answer: B

Reason: CAP theorem states a distributed system can provide at most two of three guarantees: Consistency, Availability, Partition tolerance.

Tag: Past Paper

---

### Question 908
Domain: Databases
Topic: Distributed Databases
Subtopic: CAP Theorem
Difficulty: Hard

Question: What is partition tolerance in CAP theorem?

A) No partitions
B) System continues operating despite network partitions
C) System stops
D) No tolerance

✔ Correct Answer: B

Reason: Partition tolerance means the system continues to operate even when network partitions occur between nodes.

Tag: Past Paper

---

### Question 909
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Document Databases
Difficulty: Easy

Question: What is a document database?

A) Relational database
B) Database storing data as documents (JSON, XML)
C) File system
D) Graph database

✔ Correct Answer: B

Reason: Document databases store data as self-contained documents in formats like JSON or XML.

Tag: Normal

---

### Question 910
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Document Databases
Difficulty: Easy

Question: Which is an example of a document database?

A) MySQL
B) MongoDB
C: PostgreSQL
D) Oracle

✔ Correct Answer: B

Reason: MongoDB is a popular document database that stores data in JSON-like BSON format.

Tag: Normal

---

### Question 911
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Star Schema
Difficulty: Medium

Question: What is a star schema?

A) Complex schema
B) Central fact table surrounded by dimension tables
C) No schema
D) Random schema

✔ Correct Answer: B

Reason: Star schema has a central fact table connected to multiple dimension tables in a star-like pattern.

Tag: Normal

---

### Question 912
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Snowflake Schema
Difficulty: Medium

Question: How does snowflake schema differ from star schema?

A) No difference
B: Dimension tables are normalized into multiple related tables
C) Simpler structure
D) No dimensions

✔ Correct Answer: B

Reason: Snowflake schema normalizes dimension tables into multiple related tables, creating a more complex structure.

Tag: Normal

---

### Question 913
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

A) All departments
B) Departments with above-average salaries
C) All employees
D) Error

✔ Correct Answer: B

Reason: The query returns departments whose average salary exceeds the company-wide average salary.

Tag: Normal

---

### Question 914
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the result of this query?
```sql
SELECT name, COALESCE(phone, email, 'No contact') as contact
FROM customers;
```

A) Only phone numbers
B) First non-NULL value among phone, email, or 'No contact'
C) Only emails
D) Error

✔ Correct Answer: B

Reason: COALESCE returns the first non-NULL value from the list of arguments.

Tag: Normal

---

### Question 915
Domain: Databases
Topic: Advanced SQL
Subtopic: Common Table Expressions
Difficulty: Medium

Question: What is a CTE (Common Table Expression)?

A) Permanent table
B) Temporary named result set for a query
C) Index
D) View

✔ Correct Answer: B

Reason: CTE is a temporary named result set defined within a query using the WITH clause.

Tag: Normal

---

### Question 916
Domain: Databases
Topic: Advanced SQL
Subtopic: Common Table Expressions
Difficulty: Medium

Question: What is the advantage of using CTEs?

A) No advantage
B) Improved readability and ability to reference result multiple times
C: Slower performance
D) More complexity

✔ Correct Answer: B

Reason: CTEs improve query readability and allow the result to be referenced multiple times within the same query.

Tag: Normal

---

### Question 917
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Fifth Normal Form
Difficulty: Hard

Question: What is Fifth Normal Form (5NF)?

A) First normal form
B) Eliminates join dependencies
C) Second normal form
D) No normalization

✔ Correct Answer: B

Reason: 5NF (Project-Join Normal Form) eliminates join dependencies, ensuring no information loss from decomposition.

Tag: Past Paper

---

### Question 918
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Domain-Key Normal Form
Difficulty: Hard

Question: What is Domain-Key Normal Form (DKNF)?

A) Basic form
B) Ultimate normal form where all constraints are logical consequences of domains and keys
C: First normal form
D) No form

✔ Correct Answer: B

Reason: DKNF is the ultimate normal form where every constraint is a logical consequence of domain and key constraints.

Tag: Normal

---

### Question 919
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Isolation
Difficulty: Medium

Question: What is phantom read?

A) Reading deleted data
B) New rows appearing in repeated queries within same transaction
C) Reading uncommitted data
D) No read

✔ Correct Answer: B

Reason: Phantom read occurs when new rows matching a query appear in a repeated read within the same transaction.

Tag: Past Paper

---

### Question 920
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Isolation
Difficulty: Medium

Question: Which isolation level prevents phantom reads?

A) Read Uncommitted
B) Serializable
C) Read Committed
D) Repeatable Read (in most systems)

✔ Correct Answer: B

Reason: Serializable isolation level prevents all anomalies including phantom reads through complete isolation.

Tag: Past Paper

---

### Question 921
Domain: Databases
Topic: Concurrency Control
Subtopic: Optimistic Concurrency Control
Difficulty: Hard

Question: What is optimistic concurrency control?

A) Pessimistic locking
B: Assumes conflicts are rare, validates at commit time
C) Always locks
D) No control

✔ Correct Answer: B

Reason: Optimistic concurrency control assumes conflicts are rare and validates transactions at commit time rather than locking.

Tag: Normal

---

### Question 922
Domain: Databases
Topic: Concurrency Control
Subtopic: Optimistic Concurrency Control
Difficulty: Hard

Question: What are the phases of optimistic concurrency control?

A) One phase
B) Read, validation, and write phases
C) Two phases
D) No phases

✔ Correct Answer: B

Reason: Optimistic CC has three phases: read (execute), validation (check conflicts), and write (commit changes).

Tag: Normal

---

### Question 923
Domain: Databases
Topic: Recovery Management
Subtopic: ARIES Algorithm
Difficulty: Hard

Question: What does ARIES stand for?

A: Random acronym
B) Algorithm for Recovery and Isolation Exploiting Semantics
C) No meaning
D) Database name

✔ Correct Answer: B

Reason: ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) is a sophisticated recovery algorithm.

Tag: Normal

---

### Question 924
Domain: Databases
Topic: Recovery Management
Subtopic: ARIES Algorithm
Difficulty: Hard

Question: What are the phases of ARIES recovery?

A) One phase
B) Analysis, Redo, and Undo phases
C) Two phases
D) No phases

✔ Correct Answer: B

Reason: ARIES recovery has three phases: Analysis (determine state), Redo (repeat history), Undo (rollback uncommitted).

Tag: Normal

---

### Question 925
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Extendible Hashing
Difficulty: Hard

Question: What is extendible hashing?

A) Static hashing
B) Dynamic hashing that grows/shrinks without full reorganization
C) No hashing
D) Linear hashing

✔ Correct Answer: B

Reason: Extendible hashing is a dynamic hashing technique that allows the hash structure to grow and shrink dynamically.

Tag: Normal

---

### Question 926
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Linear Hashing
Difficulty: Hard

Question: What is linear hashing?

A) Static hashing
B) Dynamic hashing with gradual bucket splitting
C) No hashing
D) Extendible hashing

✔ Correct Answer: B

Reason: Linear hashing is a dynamic hashing technique that splits buckets gradually in a linear fashion.

Tag: Normal

---

### Question 927
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Rewriting
Difficulty: Medium

Question: What is query rewriting?

A) No changes
B) Transforming query into equivalent but more efficient form
C: Deleting query
D) Executing query

✔ Correct Answer: B

Reason: Query rewriting transforms a query into an equivalent form that can be executed more efficiently.

Tag: Normal

---

### Question 928
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Predicate Pushdown
Difficulty: Medium

Question: What is predicate pushdown?

A) Moving predicates up
B) Moving filter conditions closer to data source
C) No movement
D) Random placement

✔ Correct Answer: B

Reason: Predicate pushdown moves filter conditions (WHERE clauses) closer to the data source to reduce data transfer.

Tag: Normal

---

### Question 929
Domain: Databases
Topic: Database Security
Subtopic: Access Control Models
Difficulty: Medium

Question: What is Discretionary Access Control (DAC)?

A) Mandatory control
B) Owner controls access to their objects
C: No control
D) Role-based only

✔ Correct Answer: B

Reason: DAC allows object owners to control access permissions to their objects at their discretion.

Tag: Normal

---

### Question 930
Domain: Databases
Topic: Database Security
Subtopic: Access Control Models
Difficulty: Medium

Question: What is Mandatory Access Control (MAC)?

A) Discretionary control
B) System-enforced access based on security labels
C) No control
D) Owner control

✔ Correct Answer: B

Reason: MAC enforces access control based on system-defined security labels and clearance levels.

Tag: Normal

---

### Question 931
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Fragmentation
Difficulty: Medium

Question: What is horizontal fragmentation?

A) Vertical split
B) Splitting table by rows
C) No fragmentation
D) Random split

✔ Correct Answer: B

Reason: Horizontal fragmentation divides a table into subsets of rows, distributing them across sites.

Tag: Normal

---

### Question 932
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Fragmentation
Difficulty: Medium

Question: What is vertical fragmentation?

A) Horizontal split
B) Splitting table by columns
C) No fragmentation
D) Random split

✔ Correct Answer: B

Reason: Vertical fragmentation divides a table into subsets of columns, keeping the primary key in each fragment.

Tag: Normal

---

### Question 933
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Column-Family Databases
Difficulty: Medium

Question: What is a column-family database?

A) Row-based storage
B) Database storing data in column families
C) Document database
D) Graph database

✔ Correct Answer: B

Reason: Column-family databases store data in column families, optimized for queries on specific columns.

Tag: Normal

---

### Question 934
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Column-Family Databases
Difficulty: Medium

Question: Which is an example of a column-family database?

A) MongoDB
B) Apache Cassandra
C) MySQL
D) Neo4j

✔ Correct Answer: B

Reason: Apache Cassandra is a popular column-family (wide-column) database designed for scalability.

Tag: Normal

---

### Question 935
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: ETL Process
Difficulty: Easy

Question: What does ETL stand for?

A) Execute, Test, Load
B) Extract, Transform, Load
C) Enter, Transfer, List
D) Export, Track, Link

✔ Correct Answer: B

Reason: ETL stands for Extract (from sources), Transform (clean/convert), Load (into warehouse).

Tag: Normal

---

### Question 936
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: ETL Process
Difficulty: Medium

Question: What happens in the Transform phase of ETL?

A) Data extraction
B) Data cleaning, validation, and conversion
C) Data loading
D) No transformation

✔ Correct Answer: B

Reason: Transform phase cleans, validates, converts, and standardizes data before loading into the warehouse.

Tag: Normal

---

### Question 937
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What does this query return?
```sql
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d
WHERE e.department_id IS NULL;
```

A) Normal joins
B) Cartesian product of employees without departments and all departments
C) Only employees
D) Error

✔ Correct Answer: B

Reason: CROSS JOIN creates a Cartesian product; the WHERE clause filters to employees without assigned departments.

Tag: Normal

---

### Question 938
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What is the result of this query?
```sql
SELECT name, LENGTH(name) as name_length
FROM employees
ORDER BY name_length DESC
LIMIT 5;
```

A) All employees
B) 5 employees with longest names
C) 5 employees with shortest names
D) Error

✔ Correct Answer: B

Reason: The query returns the 5 employees with the longest names, ordered by name length descending.

Tag: Normal

---

### Question 939
Domain: Databases
Topic: Advanced SQL
Subtopic: Pivot Operations
Difficulty: Hard

Question: What does a PIVOT operation do?

A) No change
B) Converts rows to columns
C) Converts columns to rows
D) Deletes data

✔ Correct Answer: B

Reason: PIVOT rotates data from rows into columns, useful for creating cross-tabulation reports.

Tag: Normal

---

### Question 940
Domain: Databases
Topic: Advanced SQL
Subtopic: Unpivot Operations
Difficulty: Hard

Question: What does an UNPIVOT operation do?

A) No change
B) Converts columns to rows
C: Converts rows to columns
D) Deletes data

✔ Correct Answer: B

Reason: UNPIVOT rotates data from columns into rows, the reverse of PIVOT operation.

Tag: Normal

---

### Question 941
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Multivalued Dependencies
Difficulty: Hard

Question: What is a multivalued dependency?

A) Functional dependency
B) Dependency where one attribute determines a set of values
C) No dependency
D) Simple dependency

✔ Correct Answer: B

Reason: Multivalued dependency occurs when one attribute determines a set of values independently of other attributes.

Tag: Past Paper

---

### Question 942
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Fourth Normal Form
Difficulty: Hard

Question: What does Fourth Normal Form (4NF) eliminate?

A) Partial dependencies
B) Non-trivial multivalued dependencies
C) Transitive dependencies
D) No elimination

✔ Correct Answer: B

Reason: 4NF eliminates non-trivial multivalued dependencies, building on BCNF.

Tag: Past Paper

---

### Question 943
Domain: Databases
Topic: Transaction Management
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is a compensating transaction?

A) Normal transaction
B) Transaction that undoes effects of a committed transaction
C) Failed transaction
D) No transaction

✔ Correct Answer: B

Reason: Compensating transaction logically undoes the effects of a previously committed transaction.

Tag: Normal

---

### Question 944
Domain: Databases
Topic: Transaction Management
Subtopic: Long-Running Transactions
Difficulty: Medium

Question: What is a saga pattern?

A) Short transaction
B) Sequence of local transactions with compensating actions
C) Single transaction
D) No pattern

✔ Correct Answer: B

Reason: Saga pattern manages long-running transactions as a sequence of local transactions, each with a compensating action.

Tag: Normal

---

### Question 945
Domain: Databases
Topic: Concurrency Control
Subtopic: Timestamp Ordering
Difficulty: Hard

Question: What is timestamp ordering protocol?

A) Lock-based protocol
B) Ordering transactions by timestamps to ensure serializability
C) No ordering
D) Random ordering

✔ Correct Answer: B

Reason: Timestamp ordering assigns timestamps to transactions and orders operations to ensure serializable execution.

Tag: Normal

---

### Question 946
Domain: Databases
Topic: Concurrency Control
Subtopic: Timestamp Ordering
Difficulty: Hard

Question: What is the Thomas Write Rule?

A) Read rule
B) Optimization allowing outdated writes to be ignored
C: Lock rule
D) No rule

✔ Correct Answer: B

Reason: Thomas Write Rule is an optimization in timestamp ordering that ignores writes with outdated timestamps.

Tag: Normal

---

### Question 947
Domain: Databases
Topic: Recovery Management
Subtopic: Shadow Paging
Difficulty: Hard

Question: What is shadow paging?

A) Regular paging
B) Recovery technique using shadow copies of pages
C) No paging
D) Memory paging

✔ Correct Answer: B

Reason: Shadow paging maintains shadow copies of database pages, switching to new version on commit.

Tag: Normal

---

### Question 948
Domain: Databases
Topic: Recovery Management
Subtopic: Write-Ahead Logging
Difficulty: Medium

Question: What is the Write-Ahead Logging (WAL) protocol?

A) Write after commit
B) Log records must be written before data modifications
C: No logging
D) Random writing

✔ Correct Answer: B

Reason: WAL protocol requires log records to be written to stable storage before corresponding data modifications.

Tag: Past Paper

---

### Question 949
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Spatial Indexing
Difficulty: Hard

Question: What is an R-tree index?

A) Regular B-tree
B) Spatial index for multidimensional data
C) Hash index
D) No index

✔ Correct Answer: B

Reason: R-tree is a spatial index structure for efficiently indexing multidimensional data like geographic coordinates.

Tag: Normal

---

### Question 950
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Full-Text Indexing
Difficulty: Medium

Question: What is a full-text index?

A) Regular index
B) Index for efficient text searching and keyword queries
C: No index
D) Numeric index

✔ Correct Answer: B

Reason: Full-text index enables efficient searching of text content, supporting keyword searches and relevance ranking.

Tag: Normal

---

### Question 951
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Materialized Views
Difficulty: Medium

Question: When should materialized views be refreshed?

A) Never
B) Based on data change frequency and query patterns
C) Every second
D) Random times

✔ Correct Answer: B

Reason: Materialized view refresh strategy depends on how frequently underlying data changes and query requirements.

Tag: Normal

---

### Question 952
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Hints
Difficulty: Medium

Question: What are query hints?

A) Automatic optimization
B) Directives to influence optimizer's execution plan choices
C: No hints
D) Error messages

✔ Correct Answer: B

Reason: Query hints are directives that guide the optimizer to use specific indexes, join methods, or execution strategies.

Tag: Normal

---

### Question 953
Domain: Databases
Topic: Database Security
Subtopic: Auditing
Difficulty: Easy

Question: What is database auditing?

A) No tracking
B) Tracking and logging database activities for security
C: Backup process
D) Query optimization

✔ Correct Answer: B

Reason: Database auditing tracks and logs user activities, access attempts, and data modifications for security and compliance.

Tag: Normal

---

### Question 954
Domain: Databases
Topic: Database Security
Subtopic: Row-Level Security
Difficulty: Medium

Question: What is row-level security?

A) Table-level security
B) Access control at individual row level based on user attributes
C: No security
D) Column security

✔ Correct Answer: B

Reason: Row-level security restricts access to specific rows based on user attributes or roles.

Tag: Normal

---

### Question 955
Domain: Databases
Topic: Distributed Databases
Subtopic: Replication Strategies
Difficulty: Medium

Question: What is master-slave replication?

A) Peer-to-peer
B: One master for writes, multiple slaves for reads
C) No replication
D) Random replication

✔ Correct Answer: B

Reason: Master-slave replication has one master node handling writes and multiple slave nodes handling read queries.

Tag: Normal

---

### Question 956
Domain: Databases
Topic: Distributed Databases
Subtopic: Replication Strategies
Difficulty: Medium

Question: What is multi-master replication?

A) Single master
B) Multiple nodes can accept writes simultaneously
C: No replication
D) Read-only replication

✔ Correct Answer: B

Reason: Multi-master replication allows multiple nodes to accept write operations simultaneously, requiring conflict resolution.

Tag: Normal

---

### Question 957
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Key-Value Stores
Difficulty: Easy

Question: What is a key-value store?

A) Relational database
B) Database storing data as key-value pairs
C: Document database
D) Graph database

✔ Correct Answer: B

Reason: Key-value stores are simple databases that store data as key-value pairs, optimized for fast lookups.

Tag: Normal

---

### Question 958
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Key-Value Stores
Difficulty: Easy

Question: Which is an example of a key-value store?

A) MongoDB
B) Redis
C: PostgreSQL
D) Neo4j

✔ Correct Answer: B

Reason: Redis is a popular in-memory key-value store used for caching and real-time applications.

Tag: Normal

---

### Question 959
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Fact Tables
Difficulty: Medium

Question: What is a fact table?

A) Dimension table
B) Central table containing measurable business metrics
C: Lookup table
D) No table

✔ Correct Answer: B

Reason: Fact table stores quantitative business metrics (facts) and foreign keys to dimension tables.

Tag: Normal

---

### Question 960
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Dimension Tables
Difficulty: Medium

Question: What is a dimension table?

A) Fact table
B) Table containing descriptive attributes for analysis
C: No table
D) Transaction table

✔ Correct Answer: B

Reason: Dimension tables contain descriptive attributes (dimensions) used for filtering and grouping fact data.

Tag: Normal

---

### Question 961
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query do?
```sql
SELECT product_id, SUM(quantity) as total_sold
FROM sales
GROUP BY product_id
ORDER BY total_sold DESC;
```

A) Random order
B) Products ordered by total quantity sold (highest first)
C: Alphabetical order
D) Error

✔ Correct Answer: B

Reason: The query calculates total quantity sold per product and orders results by total sold in descending order.

Tag: Normal

---

### Question 962
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the result of this query?
```sql
SELECT name, salary,
       NTILE(4) OVER (ORDER BY salary) as quartile
FROM employees;
```

A) Random groups
B) Employees divided into 4 salary quartiles
C: Only salaries
D) Error

✔ Correct Answer: B

Reason: NTILE(4) divides employees into 4 equal groups (quartiles) based on salary ordering.

Tag: Normal

---

### Question 963
Domain: Databases
Topic: Advanced SQL
Subtopic: Recursive Queries
Difficulty: Hard

Question: What is a recursive CTE used for?

A) Simple queries
B) Hierarchical or graph-like data traversal
C: No use
D) Deletion only

✔ Correct Answer: B

Reason: Recursive CTEs are used for querying hierarchical data (org charts, bill of materials) and graph traversal.

Tag: Normal

---

### Question 964
Domain: Databases
Topic: Advanced SQL
Subtopic: Window Functions
Difficulty: Hard

Question: What does FIRST_VALUE() window function return?

A) Last value
B) First value in the window frame
C: Random value
D) Average value

✔ Correct Answer: B

Reason: FIRST_VALUE() returns the first value in the ordered window frame.

Tag: Normal

---

### Question 965
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization Techniques
Difficulty: Medium

Question: What is a summary table?

A) Normalized table
B) Precomputed aggregated data for performance
C: Regular table
D) Deleted table

✔ Correct Answer: B

Reason: Summary tables store precomputed aggregations to improve query performance for common analytical queries.

Tag: Normal

---

### Question 966
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization Techniques
Difficulty: Medium

Question: What is column duplication?

A) No duplication
B) Storing same data in multiple tables to avoid joins
C: Normalization
D) Deletion

✔ Correct Answer: B

Reason: Column duplication stores frequently accessed data in multiple tables to reduce join operations.

Tag: Normal

---

### Question 967
Domain: Databases
Topic: Transaction Management
Subtopic: Isolation Anomalies
Difficulty: Medium

Question: What is a dirty write?

A) Clean write
B) Overwriting uncommitted data from another transaction
C: Normal write
D) No write

✔ Correct Answer: B

Reason: Dirty write occurs when a transaction overwrites data written by another uncommitted transaction.

Tag: Normal

---

### Question 968
Domain: Databases
Topic: Transaction Management
Subtopic: Isolation Anomalies
Difficulty: Medium

Question: What is a lost update?

A) Successful update
B) One transaction's update is overwritten by another
C: No update
D) Saved update

✔ Correct Answer: B

Reason: Lost update occurs when two transactions read the same data and both update it, with one update overwriting the other.

Tag: Past Paper

---

### Question 969
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Granularity
Difficulty: Medium

Question: What is lock granularity?

A) Lock type
B) Size of data item that can be locked
C: Lock duration
D) No granularity

✔ Correct Answer: B

Reason: Lock granularity refers to the size of the data item that can be locked (database, table, page, row).

Tag: Normal

---

### Question 970
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Granularity
Difficulty: Medium

Question: What is the trade-off with fine-grained locking?

A) No trade-off
B: Higher concurrency but more lock overhead
C: Lower concurrency
D: No overhead

✔ Correct Answer: B

Reason: Fine-grained locking (row-level) allows higher concurrency but requires more lock management overhead.

Tag: Normal

---

### Question 971
Domain: Databases
Topic: Recovery Management
Subtopic: Log-Based Recovery
Difficulty: Medium

Question: What is a redo log?

A) Undo log
B: Log recording changes to redo committed transactions
C: No log
D: Backup log

✔ Correct Answer: B

Reason: Redo log records changes made by transactions to redo them during recovery after a crash.

Tag: Normal

---

### Question 972
Domain: Databases
Topic: Recovery Management
Subtopic: Log-Based Recovery
Difficulty: Medium

Question: What is an undo log?

A) Redo log
B) Log recording old values to undo uncommitted transactions
C: No log
D) Backup log

✔ Correct Answer: B

Reason: Undo log records old values before changes to undo uncommitted transactions during recovery.

Tag: Normal

---

### Question 973
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Maintenance
Difficulty: Medium

Question: What is index fragmentation?

A) No fragmentation
B: Logical disorder in index pages reducing performance
C: Perfect order
D: No impact

✔ Correct Answer: B

Reason: Index fragmentation occurs when index pages become logically disordered, reducing scan performance.

Tag: Normal

---

### Question 974
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Maintenance
Difficulty: Medium

Question: How is index fragmentation resolved?

A) Delete index
B: Rebuild or reorganize the index
C: Ignore it
D: No solution

✔ Correct Answer: B

Reason: Index fragmentation is resolved by rebuilding (complete recreation) or reorganizing (defragmenting) the index.

Tag: Normal

---

### Question 975
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Execution Plans
Difficulty: Easy

Question: What is an execution plan?

A) Database schema
B: Step-by-step strategy for executing a query
C: Backup plan
D: No plan

✔ Correct Answer: B

Reason: An execution plan is the optimizer's chosen strategy showing how a query will be executed.

Tag: Normal

---

### Question 976
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Execution Plans
Difficulty: Medium

Question: What is plan caching?

A) No caching
B: Storing compiled execution plans for reuse
C: Data caching
D: Random caching

✔ Correct Answer: B

Reason: Plan caching stores compiled execution plans in memory to avoid recompilation for repeated queries.

Tag: Normal

---

### Question 977
Domain: Databases
Topic: Database Security
Subtopic: Authentication Methods
Difficulty: Easy

Question: What is database authentication?

A) Authorization
B: Verifying user identity before granting access
C: No verification
D: Encryption

✔ Correct Answer: B

Reason: Authentication verifies the identity of users attempting to access the database system.

Tag: Normal

---

### Question 978
Domain: Databases
Topic: Database Security
Subtopic: Authentication Methods
Difficulty: Medium

Question: What is two-factor authentication (2FA)?

A) Single factor
B: Authentication requiring two different verification methods
C: No authentication
D: Three factors

✔ Correct Answer: B

Reason: 2FA requires two different authentication factors (e.g., password + token) for enhanced security.

Tag: Normal

---

### Question 979
Domain: Databases
Topic: Distributed Databases
Subtopic: Consistency Models
Difficulty: Hard

Question: What is eventual consistency?

A) Strong consistency
B: System will become consistent eventually, not immediately
C: No consistency
D: Immediate consistency

✔ Correct Answer: B

Reason: Eventual consistency guarantees that if no new updates are made, all replicas will eventually converge to the same value.

Tag: Normal

---

### Question 980
Domain: Databases
Topic: Distributed Databases
Subtopic: Consistency Models
Difficulty: Hard

Question: What is strong consistency?

A) Weak consistency
B: All reads return the most recent write immediately
C: No consistency
D: Eventual consistency

✔ Correct Answer: B

Reason: Strong consistency ensures all reads immediately reflect the most recent write across all nodes.

Tag: Normal

---

### Question 981
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: BASE Properties
Difficulty: Hard

Question: What does BASE stand for in NoSQL?

A) Random acronym
B: Basically Available, Soft state, Eventually consistent
C: No meaning
D: ACID alternative

✔ Correct Answer: B

Reason: BASE (Basically Available, Soft state, Eventually consistent) is an alternative to ACID for NoSQL systems.

Tag: Normal

---

### Question 982
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Sharding
Difficulty: Medium

Question: What is sharding?

A) Replication
B: Horizontal partitioning of data across multiple servers
C: Vertical partitioning
D: No partitioning

✔ Correct Answer: B

Reason: Sharding is horizontal partitioning that distributes data across multiple servers for scalability.

Tag: Normal

---

### Question 983
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Slowly Changing Dimensions
Difficulty: Hard

Question: What is a Type 1 Slowly Changing Dimension?

A: Preserves history
B: Overwrites old values with new ones
C: Adds new rows
D: No changes

✔ Correct Answer: B

Reason: Type 1 SCD simply overwrites old values with new ones, not preserving historical data.

Tag: Normal

---

### Question 984
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Slowly Changing Dimensions
Difficulty: Hard

Question: What is a Type 2 Slowly Changing Dimension?

A: Overwrites values
B: Creates new row for each change, preserving history
C: No changes
D: Updates in place

✔ Correct Answer: B

Reason: Type 2 SCD creates a new row for each change, maintaining complete historical records.

Tag: Normal

---

### Question 985
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Medium

Question: What does this query return?
```sql
SELECT CASE 
  WHEN salary < 50000 THEN 'Low'
  WHEN salary BETWEEN 50000 AND 100000 THEN 'Medium'
  ELSE 'High'
END as salary_range, COUNT(*) as count
FROM employees
GROUP BY salary_range;
```

A: All salaries
B: Count of employees in each salary range category
C: Only names
D: Error

✔ Correct Answer: B

Reason: The query categorizes employees into salary ranges and counts how many fall into each category.

Tag: Normal

---

### Question 986
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Code-Based Questions
Difficulty: Hard

Question: What is the output of this query?
```sql
SELECT department,
       SUM(salary) as total_salary,
       SUM(SUM(salary)) OVER () as company_total
FROM employees
GROUP BY department;
```

A: Only department totals
B: Each department's total and company-wide total
C: Only company total
D: Error

✔ Correct Answer: B

Reason: The query shows each department's salary total along with the company-wide total using a window function.

Tag: Normal

---

### Question 987
Domain: Databases
Topic: Advanced SQL
Subtopic: Lateral Joins
Difficulty: Hard

Question: What is a LATERAL join?

A: Regular join
B: Join allowing subquery to reference columns from preceding tables
C: No join
D: Cross join

✔ Correct Answer: B

Reason: LATERAL join allows a subquery in the FROM clause to reference columns from preceding tables in the same FROM clause.

Tag: Normal

---

### Question 988
Domain: Databases
Topic: Advanced SQL
Subtopic: Array Operations
Difficulty: Medium

Question: What SQL function unnests an array?

A: NEST
B: UNNEST or array expansion functions
C: GROUP
D: No function

✔ Correct Answer: B

Reason: UNNEST (or similar functions) expands an array into a set of rows, one per array element.

Tag: Normal

---

### Question 989
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Closure of Attributes
Difficulty: Hard

Question: What is the closure of a set of attributes?

A: No closure
B: Set of all attributes functionally determined by the given set
C: Random attributes
D: Primary key only

✔ Correct Answer: B

Reason: Closure of attributes is the set of all attributes that can be functionally determined from the given set.

Tag: Past Paper

---

### Question 990
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Candidate Keys
Difficulty: Medium

Question: What is a candidate key?

A: Foreign key
B: Minimal superkey that can uniquely identify tuples
C: Non-unique key
D: No key

✔ Correct Answer: B

Reason: A candidate key is a minimal set of attributes that uniquely identifies tuples (minimal superkey).

Tag: Past Paper

---

### Question 991
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Scheduling
Difficulty: Hard

Question: What is a serial schedule?

A: Concurrent schedule
B: Schedule where transactions execute one after another
C: Random schedule
D: No schedule

✔ Correct Answer: B

Reason: A serial schedule executes transactions sequentially without interleaving operations.

Tag: Past Paper

---

### Question 992
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Scheduling
Difficulty: Hard

Question: What is a serializable schedule?

A: Serial schedule only
B: Schedule equivalent to some serial schedule
C: Random schedule
D: No schedule

✔ Correct Answer: B

Reason: A serializable schedule produces the same result as some serial execution of the transactions.

Tag: Past Paper

---

### Question 993
Domain: Databases
Topic: Concurrency Control
Subtopic: Validation-Based Protocols
Difficulty: Hard

Question: What is validation in optimistic concurrency control?

A: No validation
B: Checking if transaction's reads are still valid at commit time
C: Lock acquisition
D: Random check

✔ Correct Answer: B

Reason: Validation phase checks if the transaction's read set is still valid and no conflicts occurred.

Tag: Normal

---

### Question 994
Domain: Databases
Topic: Concurrency Control
Subtopic: Graph-Based Protocols
Difficulty: Hard

Question: What is a wait-for graph?

A: No graph
B: Directed graph showing transaction wait dependencies
C: Random graph
D: Data structure

✔ Correct Answer: B

Reason: Wait-for graph is a directed graph where nodes are transactions and edges represent wait dependencies.

Tag: Normal

---

### Question 995
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Algorithms
Difficulty: Medium

Question: What is a commit point?

A: Start point
B: Point where transaction's effects become permanent
C: Abort point
D: No point

✔ Correct Answer: B

Reason: Commit point is when a transaction's changes are permanently recorded and cannot be undone.

Tag: Normal

---

### Question 996
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Algorithms
Difficulty: Medium

Question: What is rollback?

A: Commit
B: Undoing a transaction's changes
C: Redo
D: No action

✔ Correct Answer: B

Reason: Rollback undoes all changes made by a transaction, returning the database to its previous state.

Tag: Normal

---

### Question 997
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Database Pages
Difficulty: Easy

Question: What is a database page?

A: Web page
B: Fixed-size block of storage
C: Variable size
D: No structure

✔ Correct Answer: B

Reason: A database page (or block) is a fixed-size unit of storage, typically 4KB, 8KB, or 16KB.

Tag: Normal

---

### Question 998
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Cardinality Estimation
Difficulty: Hard

Question: What is cardinality estimation?

A: No estimation
B: Estimating number of rows in query results
C: Counting columns
D: Random guess

✔ Correct Answer: B

Reason: Cardinality estimation predicts the number of rows that will be returned by query operations.

Tag: Normal

---

### Question 999
Domain: Databases
Topic: Database Security
Subtopic: Principle of Least Privilege
Difficulty: Easy

Question: What is the principle of least privilege?

A: Maximum access
B: Users should have minimum permissions necessary for their tasks
C: No access
D: Random access

✔ Correct Answer: B

Reason: Principle of least privilege states users should have only the minimum permissions required to perform their job.

Tag: Normal

---

### Question 1000
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Database Design
Difficulty: Medium

Question: What is data locality in distributed databases?

A: Remote data
B: Placing data close to where it's frequently accessed
C: Random placement
D: No locality

✔ Correct Answer: B

Reason: Data locality principle places data at sites where it's most frequently accessed to minimize network traffic.

Tag: Normal

---

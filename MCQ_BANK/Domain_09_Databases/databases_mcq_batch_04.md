# Databases MCQ Bank - Batch 04

## Questions 301-400

---

### Question 301
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: String Manipulation
Difficulty: Easy

Question: Which SQL function concatenates two or more strings?

A) JOIN()
B) CONCAT()
C) MERGE()
D) COMBINE()

✔ Correct Answer: B

Reason: CONCAT() combines two or more strings into a single string.

Tag: Normal

---

### Question 302
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: String Manipulation
Difficulty: Easy

Question: Which SQL function removes leading and trailing spaces from a string?

A) STRIP()
B) CLEAN()
C) TRIM()
D) REMOVE()

✔ Correct Answer: C

Reason: TRIM() removes leading and trailing spaces (or specified characters) from a string.

Tag: Normal

---

### Question 303
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: String Manipulation
Difficulty: Medium

Question: Which SQL function extracts a substring from a string?

A) EXTRACT()
B) SUBSTRING() or SUBSTR()
C) PART()
D) SLICE()

✔ Correct Answer: B

Reason: SUBSTRING() (or SUBSTR()) extracts a portion of a string starting at a specified position.

Tag: Normal

---

### Question 304
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Date Functions
Difficulty: Medium

Question: Which SQL function adds a time interval to a date?

A) ADD_DATE()
B) DATE_ADD() or DATEADD()
C) PLUS_DATE()
D) INCREMENT_DATE()

✔ Correct Answer: B

Reason: DATE_ADD() (MySQL) or DATEADD() (SQL Server) adds a specified time interval to a date.

Tag: Normal

---

### Question 305
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Date Functions
Difficulty: Medium

Question: Which SQL function calculates the difference between two dates?

A) DATE_DIFF() or DATEDIFF()
B) SUBTRACT_DATE()
C) MINUS_DATE()
D) DIFF()

✔ Correct Answer: A

Reason: DATE_DIFF() or DATEDIFF() calculates the difference between two dates in specified units.

Tag: Normal

---

### Question 306
Domain: Databases
Topic: Advanced SQL
Subtopic: Temporary Tables
Difficulty: Medium

Question: What is a temporary table?

A) A permanent table
B) A table that exists only for the duration of a session or transaction
C) A backup table
D) A deleted table

✔ Correct Answer: B

Reason: A temporary table exists only for the duration of a database session or transaction and is automatically dropped afterward.

Tag: Normal

---

### Question 307
Domain: Databases
Topic: Advanced SQL
Subtopic: Table Variables
Difficulty: Medium

Question: What is a table variable?

A) A permanent table
B) A variable that holds a table structure in memory
C) A column variable
D) A database variable

✔ Correct Answer: B

Reason: A table variable is a special variable type that holds a table structure in memory, similar to temporary tables but with different scope.

Tag: Normal

---

### Question 308
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Null Values
Difficulty: Medium

Question: What is the result of NULL = NULL in SQL?

A) TRUE
B) FALSE
C) NULL
D) Error

✔ Correct Answer: C

Reason: In SQL, NULL = NULL evaluates to NULL (unknown), not TRUE, because NULL represents an unknown value.

Tag: Past Paper

---

### Question 309
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Null Values
Difficulty: Medium

Question: Which operator should be used to check for NULL values?

A) = NULL
B) == NULL
C) IS NULL
D) EQUALS NULL

✔ Correct Answer: C

Reason: IS NULL is the correct operator to check if a value is NULL; equality operators don't work with NULL.

Tag: Normal

---

### Question 310
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization Benefits
Difficulty: Easy

Question: What is a primary benefit of normalization?

A) Increased redundancy
B) Reduced data redundancy and improved data integrity
C) Slower queries
D) More storage space

✔ Correct Answer: B

Reason: Normalization reduces data redundancy and improves data integrity by organizing data efficiently.

Tag: Normal

---

### Question 311
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Over-Normalization
Difficulty: Medium

Question: What is a potential drawback of over-normalization?

A) Too much redundancy
B) Increased number of joins affecting query performance
C) Better performance
D) Simpler queries

✔ Correct Answer: B

Reason: Over-normalization can lead to too many tables requiring multiple joins, potentially degrading query performance.

Tag: Normal

---

### Question 312
Domain: Databases
Topic: Transaction Management
Subtopic: Autocommit Mode
Difficulty: Easy

Question: What is autocommit mode?

A) Manual commit required
B) Each SQL statement is automatically committed
C) No commits allowed
D) Delayed commits

✔ Correct Answer: B

Reason: In autocommit mode, each SQL statement is automatically committed immediately after execution.

Tag: Normal

---

### Question 313
Domain: Databases
Topic: Transaction Management
Subtopic: Explicit Transactions
Difficulty: Easy

Question: How do you start an explicit transaction in SQL?

A) START TRANSACTION or BEGIN TRANSACTION
B) OPEN TRANSACTION
C) CREATE TRANSACTION
D) NEW TRANSACTION

✔ Correct Answer: A

Reason: START TRANSACTION or BEGIN TRANSACTION explicitly starts a new transaction, disabling autocommit.

Tag: Normal

---

### Question 314
Domain: Databases
Topic: Concurrency Control
Subtopic: Read Committed Isolation
Difficulty: Medium

Question: What does Read Committed isolation level prevent?

A) All anomalies
B) Dirty reads
C) Phantom reads
D) All concurrent access

✔ Correct Answer: B

Reason: Read Committed prevents dirty reads by ensuring transactions only read committed data, but allows non-repeatable reads and phantom reads.

Tag: Past Paper

---

### Question 315
Domain: Databases
Topic: Concurrency Control
Subtopic: Repeatable Read Isolation
Difficulty: Medium

Question: What does Repeatable Read isolation level prevent?

A) Only dirty reads
B) Dirty reads and non-repeatable reads
C) All anomalies
D) Nothing

✔ Correct Answer: B

Reason: Repeatable Read prevents dirty reads and non-repeatable reads but may still allow phantom reads.

Tag: Past Paper

---

### Question 316
Domain: Databases
Topic: Recovery Management
Subtopic: Full Backup
Difficulty: Easy

Question: What is a full backup?

A) Backing up changed data only
B) A complete copy of the entire database
C) Backing up logs only
D) No backup

✔ Correct Answer: B

Reason: A full backup creates a complete copy of the entire database at a specific point in time.

Tag: Normal

---

### Question 317
Domain: Databases
Topic: Recovery Management
Subtopic: Incremental Backup
Difficulty: Easy

Question: What is an incremental backup?

A) A full backup
B) Backing up only data changed since the last backup
C) No backup
D) Backing up everything

✔ Correct Answer: B

Reason: An incremental backup backs up only the data that has changed since the last backup (full or incremental).

Tag: Normal

---

### Question 318
Domain: Databases
Topic: Recovery Management
Subtopic: Differential Backup
Difficulty: Medium

Question: What is a differential backup?

A) A full backup
B) Backing up data changed since the last full backup
C) Backing up logs only
D) No backup

✔ Correct Answer: B

Reason: A differential backup backs up all data that has changed since the last full backup.

Tag: Normal

---

### Question 319
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Maintenance
Difficulty: Medium

Question: What happens to indexes when data is inserted, updated, or deleted?

A) Nothing
B) Indexes must be updated to reflect changes
C) Indexes are deleted
D) Indexes are ignored

✔ Correct Answer: B

Reason: Indexes must be maintained (updated) when data changes, which adds overhead to write operations.

Tag: Normal

---

### Question 320
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Fragmentation
Difficulty: Medium

Question: What is index fragmentation?

A) Deleting indexes
B) Indexes becoming disorganized due to data modifications
C) Creating indexes
D) Encrypting indexes

✔ Correct Answer: B

Reason: Index fragmentation occurs when indexes become disorganized due to insertions, updates, and deletions, reducing performance.

Tag: Normal

---

### Question 321
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Predicate Pushdown
Difficulty: Hard

Question: What is predicate pushdown in query optimization?

A) Deleting predicates
B) Moving filter conditions closer to data sources to reduce data transfer
C) Adding predicates
D) Ignoring predicates

✔ Correct Answer: B

Reason: Predicate pushdown moves filter conditions (predicates) as close to the data source as possible to reduce the amount of data processed.

Tag: Normal

---

### Question 322
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Projection Pushdown
Difficulty: Hard

Question: What is projection pushdown?

A) Deleting columns
B) Selecting only needed columns early to reduce data transfer
C) Adding columns
D) Sorting columns

✔ Correct Answer: B

Reason: Projection pushdown selects only the needed columns as early as possible in query execution to reduce data transfer and processing.

Tag: Normal

---

### Question 323
Domain: Databases
Topic: Database Security
Subtopic: Separation of Duties
Difficulty: Medium

Question: What is separation of duties in database security?

A) One person does everything
B) Dividing responsibilities among multiple people to prevent fraud
C) No duties assigned
D) Random duty assignment

✔ Correct Answer: B

Reason: Separation of duties divides critical responsibilities among multiple people to prevent fraud and errors.

Tag: Normal

---

### Question 324
Domain: Databases
Topic: Database Security
Subtopic: Database Backup Security
Difficulty: Easy

Question: Why should database backups be encrypted?

A) To compress them
B) To protect sensitive data if backups are stolen or accessed
C) To speed up backups
D) To delete backups

✔ Correct Answer: B

Reason: Encrypting backups protects sensitive data from unauthorized access if backup media is stolen or compromised.

Tag: Normal

---

### Question 325
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Deadlock Detection
Difficulty: Hard

Question: What makes deadlock detection harder in distributed databases?

A) More users
B) Need to construct a global wait-for graph across multiple sites
C) Faster transactions
D) Smaller databases

✔ Correct Answer: B

Reason: Distributed deadlock detection requires constructing and analyzing a global wait-for graph across multiple sites, which is complex and costly.

Tag: Normal

---

### Question 326
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Query Optimization
Difficulty: Hard

Question: What is a major goal of distributed query optimization?

A) Maximize data transfer
B) Minimize data transfer between sites
C) Increase network traffic
D) Slow down queries

✔ Correct Answer: B

Reason: A major goal is to minimize data transfer between sites, as network communication is typically the most expensive operation.

Tag: Normal

---

### Question 327
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Document Store Features
Difficulty: Medium

Question: What is a key feature of document databases?

A) Fixed schema
B) Storing data in flexible, JSON-like documents
C) Only relational data
D) No data storage

✔ Correct Answer: B

Reason: Document databases store data in flexible, self-describing documents (typically JSON or BSON format) without requiring a fixed schema.

Tag: Normal

---

### Question 328
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Column-Family Features
Difficulty: Medium

Question: What is a key feature of column-family databases?

A) Row-oriented storage
B) Storing data in columns rather than rows for efficient analytics
C) No storage
D) Only text storage

✔ Correct Answer: B

Reason: Column-family databases store data by columns rather than rows, optimizing for analytical queries that access specific columns.

Tag: Normal

---

### Question 329
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Surrogate Keys
Difficulty: Medium

Question: What is a surrogate key in data warehousing?

A) A natural key
B) An artificial key with no business meaning
C) A foreign key
D) A composite key

✔ Correct Answer: B

Reason: A surrogate key is an artificial key (usually an integer) with no business meaning, used to uniquely identify records in dimension tables.

Tag: Normal

---

### Question 330
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Natural Keys
Difficulty: Easy

Question: What is a natural key?

A) An artificial key
B) A key derived from actual data attributes with business meaning
C) A random key
D) A deleted key

✔ Correct Answer: B

Reason: A natural key is derived from actual data attributes that have business meaning, like Social Security Number or Product Code.

Tag: Normal

---

### Question 331
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Conditional Aggregation
Difficulty: Hard

Question: How can you perform conditional aggregation in SQL?

A) Using WHERE only
B) Using CASE within aggregate functions
C) Using HAVING only
D) Not possible

✔ Correct Answer: B

Reason: Conditional aggregation uses CASE expressions within aggregate functions to aggregate based on conditions (e.g., SUM(CASE WHEN...)).

Tag: Normal

---

### Question 332
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: MERGE Statement
Difficulty: Hard

Question: What does the MERGE statement do?

A) Merges databases
B) Performs INSERT, UPDATE, or DELETE based on conditions in a single statement
C) Merges tables permanently
D) Deletes data

✔ Correct Answer: B

Reason: MERGE (or UPSERT) performs INSERT, UPDATE, or DELETE operations based on whether matching rows exist, in a single atomic statement.

Tag: Normal

---

### Question 333
Domain: Databases
Topic: Advanced SQL
Subtopic: Cursors
Difficulty: Medium

Question: What is a cursor in SQL?

A) A mouse pointer
B) A database object for row-by-row processing of result sets
C) A table
D) An index

✔ Correct Answer: B

Reason: A cursor is a database object that allows row-by-row processing of query result sets, useful when set-based operations aren't suitable.

Tag: Normal

---

### Question 334
Domain: Databases
Topic: Advanced SQL
Subtopic: Cursor Types
Difficulty: Hard

Question: What is a forward-only cursor?

A) A cursor that can move in any direction
B) A cursor that can only move forward through the result set
C) A cursor that moves backward
D) A static cursor

✔ Correct Answer: B

Reason: A forward-only cursor can only move forward through the result set, making it the fastest and least resource-intensive cursor type.

Tag: Normal

---

### Question 335
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Aggregate Functions in Relational Algebra
Difficulty: Hard

Question: How are aggregate functions represented in relational algebra?

A) They are not supported
B) Using the aggregation operator (G)
C) Using SELECT
D) Using PROJECT

✔ Correct Answer: B

Reason: Aggregate functions in relational algebra are represented using the aggregation operator (G), which groups and computes aggregates.

Tag: Past Paper

---

### Question 336
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Outer Join in Relational Algebra
Difficulty: Hard

Question: What does a left outer join preserve?

A) Only matching tuples
B) All tuples from the left relation, with NULLs for non-matching right tuples
C) All tuples from the right relation
D) No tuples

✔ Correct Answer: B

Reason: Left outer join preserves all tuples from the left relation, padding with NULLs where there's no match in the right relation.

Tag: Past Paper

---

### Question 337
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Superkey vs Candidate Key
Difficulty: Medium

Question: What is the difference between a superkey and a candidate key?

A) No difference
B) A candidate key is a minimal superkey
C) A superkey is smaller
D) A candidate key has more attributes

✔ Correct Answer: B

Reason: A candidate key is a minimal superkey - it has no unnecessary attributes, while a superkey may contain additional attributes.

Tag: Past Paper

---

### Question 338
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Prime Attributes
Difficulty: Medium

Question: What is a prime attribute?

A) The most important attribute
B) An attribute that is part of any candidate key
C) A foreign key
D) A non-key attribute

✔ Correct Answer: B

Reason: A prime attribute is an attribute that appears in at least one candidate key of the relation.

Tag: Past Paper

---

### Question 339
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Non-Prime Attributes
Difficulty: Easy

Question: What is a non-prime attribute?

A) An attribute in a candidate key
B) An attribute not part of any candidate key
C) A primary key
D) A foreign key

✔ Correct Answer: B

Reason: A non-prime attribute is an attribute that is not part of any candidate key.

Tag: Past Paper

---

### Question 340
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Log
Difficulty: Easy

Question: What information does a transaction log typically contain?

A) Only committed transactions
B) Before and after images of data, transaction IDs, and operation types
C) Only user information
D) Only timestamps

✔ Correct Answer: B

Reason: Transaction logs contain before/after images of data, transaction IDs, operation types, and timestamps for recovery purposes.

Tag: Normal

---

### Question 341
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Throughput
Difficulty: Medium

Question: What is transaction throughput?

A) The size of transactions
B) The number of transactions processed per unit time
C) The duration of transactions
D) The complexity of transactions

✔ Correct Answer: B

Reason: Transaction throughput measures the number of transactions a system can process per unit time, indicating system performance.

Tag: Normal

---

### Question 342
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Conversion
Difficulty: Hard

Question: What is lock conversion?

A) Deleting locks
B) Upgrading or downgrading lock types (e.g., shared to exclusive)
C) Creating locks
D) Ignoring locks

✔ Correct Answer: B

Reason: Lock conversion changes a lock from one type to another, such as upgrading a shared lock to an exclusive lock.

Tag: Normal

---

### Question 343
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Escalation
Difficulty: Medium

Question: What is lock escalation?

A) Increasing lock size
B) Converting many fine-grained locks to fewer coarse-grained locks
C) Deleting locks
D) Creating more locks

✔ Correct Answer: B

Reason: Lock escalation converts many fine-grained locks (row-level) to fewer coarse-grained locks (table-level) to reduce overhead.

Tag: Normal

---

### Question 344
Domain: Databases
Topic: Recovery Management
Subtopic: Transaction Log Truncation
Difficulty: Medium

Question: What is log truncation?

A) Deleting all logs
B) Removing inactive portions of the transaction log
C) Encrypting logs
D) Backing up logs

✔ Correct Answer: B

Reason: Log truncation removes inactive portions of the transaction log that are no longer needed for recovery, freeing space.

Tag: Normal

---

### Question 345
Domain: Databases
Topic: Recovery Management
Subtopic: Log Shipping
Difficulty: Medium

Question: What is log shipping?

A) Shipping physical logs
B) Automatically sending transaction logs to a standby server for disaster recovery
C) Deleting logs
D) Encrypting logs

✔ Correct Answer: B

Reason: Log shipping automatically sends transaction log backups to a standby server, which applies them to maintain a copy for disaster recovery.

Tag: Normal

---

### Question 346
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Rebuild vs Reorganize
Difficulty: Medium

Question: What is the difference between index rebuild and reorganize?

A) No difference
B) Rebuild recreates the index, reorganize defragments it in place
C) Reorganize is faster
D) Rebuild is always better

✔ Correct Answer: B

Reason: Rebuild completely recreates the index (more thorough but resource-intensive), while reorganize defragments it in place (less disruptive).

Tag: Normal

---

### Question 347
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Filtered Index
Difficulty: Medium

Question: What is a filtered index?

A) An index on all rows
B) An index on a subset of rows meeting a filter condition
C) A deleted index
D) A temporary index

✔ Correct Answer: B

Reason: A filtered index includes only rows that satisfy a filter predicate, reducing index size and maintenance costs.

Tag: Normal

---

### Question 348
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Cardinality Estimation
Difficulty: Hard

Question: What is cardinality estimation in query optimization?

A) Counting tables
B) Estimating the number of rows returned by operations
C) Counting columns
D) Estimating storage size

✔ Correct Answer: B

Reason: Cardinality estimation predicts the number of rows that will be returned by query operations, crucial for choosing optimal execution plans.

Tag: Normal

---

### Question 349
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Order Optimization
Difficulty: Hard

Question: Why is join order important in query optimization?

A) It's not important
B) Different join orders can have vastly different performance
C) All orders are the same
D) Only for aesthetics

✔ Correct Answer: B

Reason: Join order significantly affects performance; joining smaller intermediate results first typically reduces overall processing time.

Tag: Normal

---

### Question 350
Domain: Databases
Topic: Database Security
Subtopic: Privilege Escalation
Difficulty: Medium

Question: What is privilege escalation in database security?

A) Granting more privileges
B) Exploiting vulnerabilities to gain higher privileges than authorized
C) Normal privilege assignment
D) Removing privileges

✔ Correct Answer: B

Reason: Privilege escalation is a security attack where users exploit vulnerabilities to gain higher privileges than they're authorized to have.

Tag: Normal

---

### Question 351
Domain: Databases
Topic: Database Security
Subtopic: SQL Injection Types
Difficulty: Hard

Question: What is blind SQL injection?

A) Visible SQL injection
B) SQL injection where the attacker cannot see direct output but infers information
C) No SQL injection
D) Failed SQL injection

✔ Correct Answer: B

Reason: Blind SQL injection occurs when the application doesn't display database errors, so attackers infer information through true/false questions or time delays.

Tag: Normal

---

### Question 352
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Concurrency Control
Difficulty: Hard

Question: What is a major challenge in distributed concurrency control?

A) Single site coordination
B) Coordinating locks across multiple sites
C) No challenges
D) Faster processing

✔ Correct Answer: B

Reason: Distributed concurrency control must coordinate locks and transactions across multiple sites, dealing with network delays and potential failures.

Tag: Normal

---

### Question 353
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Recovery
Difficulty: Hard

Question: What makes recovery more complex in distributed databases?

A) Smaller databases
B) Need to coordinate recovery across multiple sites
C) Faster recovery
D) No complexity

✔ Correct Answer: B

Reason: Distributed recovery must coordinate recovery actions across multiple sites, ensuring global consistency despite potential site or network failures.

Tag: Normal

---

### Question 354
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Read Replicas
Difficulty: Medium

Question: What is the purpose of read replicas?

A) To handle writes
B) To distribute read load and improve read performance
C) To delete data
D) To backup data

✔ Correct Answer: B

Reason: Read replicas are copies of the database that handle read queries, distributing load and improving read performance.

Tag: Normal

---

### Question 355
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Write Concerns
Difficulty: Medium

Question: What is write concern in distributed databases?

A) Worrying about writes
B) The level of acknowledgment requested for write operations
C) Write speed
D) Write size

✔ Correct Answer: B

Reason: Write concern specifies the level of acknowledgment requested from the database for write operations (e.g., acknowledged by one node vs. majority).

Tag: Normal

---

### Question 356
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Fact Constellation Schema
Difficulty: Hard

Question: What is a fact constellation (galaxy) schema?

A) A single fact table
B) Multiple fact tables sharing dimension tables
C) No fact tables
D) One dimension table

✔ Correct Answer: B

Reason: A fact constellation (galaxy) schema contains multiple fact tables that share dimension tables, supporting complex analysis.

Tag: Normal

---

### Question 357
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Degenerate Dimension
Difficulty: Hard

Question: What is a degenerate dimension?

A) A broken dimension
B) A dimension key stored in the fact table without a corresponding dimension table
C) A deleted dimension
D) A temporary dimension

✔ Correct Answer: B

Reason: A degenerate dimension is a dimension key (like invoice number) stored in the fact table without a corresponding dimension table.

Tag: Normal

---

### Question 358
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: ISNULL vs COALESCE
Difficulty: Medium

Question: What is the main difference between ISNULL and COALESCE?

A) No difference
B) COALESCE can handle multiple arguments, ISNULL handles two
C) ISNULL is faster always
D) COALESCE is deprecated

✔ Correct Answer: B

Reason: COALESCE can evaluate multiple arguments and return the first non-NULL, while ISNULL (in some databases) handles only two arguments.

Tag: Normal

---

### Question 359
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: UNION vs UNION ALL Performance
Difficulty: Medium

Question: Why is UNION ALL typically faster than UNION?

A) It's not faster
B) UNION ALL doesn't remove duplicates, avoiding the sorting/comparison overhead
C) UNION is always faster
D) No performance difference

✔ Correct Answer: B

Reason: UNION ALL is faster because it doesn't perform duplicate elimination, which requires sorting or hashing the result set.

Tag: Normal

---

### Question 360
Domain: Databases
Topic: Advanced SQL
Subtopic: Dynamic SQL
Difficulty: Hard

Question: What is dynamic SQL?

A) Fast SQL
B) SQL statements constructed and executed at runtime
C) Static SQL
D) Deleted SQL

✔ Correct Answer: B

Reason: Dynamic SQL constructs SQL statements as strings at runtime and executes them, allowing flexible query generation.

Tag: Normal

---

### Question 361
Domain: Databases
Topic: Advanced SQL
Subtopic: Prepared Statements
Difficulty: Medium

Question: What is an advantage of prepared statements?

A) Slower execution
B) Protection against SQL injection and improved performance through reuse
C) More complex code
D) No advantages

✔ Correct Answer: B

Reason: Prepared statements protect against SQL injection by separating SQL from data, and improve performance by allowing query plan reuse.

Tag: Normal

---

### Question 362
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relation Properties
Difficulty: Medium

Question: Which property states that tuples in a relation are unordered?

A) Atomicity
B) No duplicate tuples
C) Tuple ordering is insignificant
D) Domain constraint

✔ Correct Answer: C

Reason: In the relational model, tuples have no inherent order; the order of rows in a relation is insignificant.

Tag: Past Paper

---

### Question 363
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Relation Properties
Difficulty: Medium

Question: Which property states that attribute values must be atomic?

A) First Normal Form
B) Tuple uniqueness
C) Domain constraint
D) Referential integrity

✔ Correct Answer: A

Reason: First Normal Form (1NF) requires that all attribute values be atomic (indivisible).

Tag: Past Paper

---

### Question 364
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Partial Dependency
Difficulty: Medium

Question: What is a partial dependency?

A) A complete dependency
B) A non-key attribute depends on part of a composite primary key
C) A transitive dependency
D) No dependency

✔ Correct Answer: B

Reason: A partial dependency occurs when a non-key attribute depends on only part of a composite primary key, violating 2NF.

Tag: Past Paper

---

### Question 365
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Full Functional Dependency
Difficulty: Medium

Question: What is a full functional dependency?

A) A partial dependency
B) A non-key attribute depends on the entire primary key
C) No dependency
D) A transitive dependency

✔ Correct Answer: B

Reason: A full functional dependency means a non-key attribute depends on the entire primary key, not just part of it.

Tag: Past Paper

---

### Question 366
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Abort
Difficulty: Easy

Question: What causes a transaction to abort?

A) Successful completion
B) Errors, deadlocks, or explicit rollback
C) Fast execution
D) No reason

✔ Correct Answer: B

Reason: Transactions abort due to errors, deadlock detection, constraint violations, or explicit ROLLBACK commands.

Tag: Normal

---

### Question 367
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Retry
Difficulty: Medium

Question: When should an aborted transaction be retried?

A) Never
B) When the abort was due to temporary conditions like deadlock
C) Always immediately
D) After deleting data

✔ Correct Answer: B

Reason: Transactions aborted due to temporary conditions (like deadlocks) can be retried, while those with logical errors should not.

Tag: Normal

---

### Question 368
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Timeout
Difficulty: Medium

Question: What is a lock timeout?

A) Locks never expire
B) Maximum time a transaction waits for a lock before aborting
C) Minimum lock time
D) Lock creation time

✔ Correct Answer: B

Reason: Lock timeout specifies the maximum time a transaction will wait to acquire a lock before aborting to prevent indefinite waiting.

Tag: Normal

---

### Question 369
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Compatibility Matrix
Difficulty: Hard

Question: Are two shared locks compatible?

A) No
B) Yes
C) Sometimes
D) Never defined

✔ Correct Answer: B

Reason: Two shared locks are compatible - multiple transactions can hold shared locks on the same data item simultaneously for reading.

Tag: Normal

---

### Question 370
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Compatibility Matrix
Difficulty: Hard

Question: Are shared and exclusive locks compatible?

A) Yes
B) No
C) Sometimes
D) Always

✔ Correct Answer: B

Reason: Shared and exclusive locks are incompatible - if one transaction holds a shared lock, another cannot acquire an exclusive lock.

Tag: Normal

---

### Question 371
Domain: Databases
Topic: Recovery Management
Subtopic: Hot Backup
Difficulty: Medium

Question: What is a hot backup?

A) A backup when the system is offline
B) A backup performed while the database is online and operational
C) A deleted backup
D) A corrupted backup

✔ Correct Answer: B

Reason: A hot backup (online backup) is performed while the database is online and users can continue accessing it.

Tag: Normal

---

### Question 372
Domain: Databases
Topic: Recovery Management
Subtopic: Cold Backup
Difficulty: Easy

Question: What is a cold backup?

A) A backup while the system is running
B) A backup performed when the database is shut down
C) A deleted backup
D) A compressed backup

✔ Correct Answer: B

Reason: A cold backup (offline backup) is performed when the database is completely shut down, ensuring consistency.

Tag: Normal

---

### Question 373
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Seek vs Index Scan
Difficulty: Medium

Question: What is the difference between index seek and index scan?

A) No difference
B) Seek uses the index to find specific rows, scan reads the entire index
C) Scan is always faster
D) Seek reads everything

✔ Correct Answer: B

Reason: Index seek uses the index structure to quickly locate specific rows, while index scan reads through the entire index sequentially.

Tag: Normal

---

### Question 374
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Included Columns
Difficulty: Medium

Question: What are included columns in an index?

A) Primary key columns
B) Non-key columns added to index leaf level for covering queries
C) Deleted columns
D) Foreign key columns

✔ Correct Answer: B

Reason: Included columns are non-key columns added to the leaf level of an index to create covering indexes without affecting the index structure.

Tag: Normal

---

### Question 375
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Nested Loop Join
Difficulty: Medium

Question: When is nested loop join most efficient?

A) For large tables
B) When one table is small or when using indexes
C) Never efficient
D) Always efficient

✔ Correct Answer: B

Reason: Nested loop join is most efficient when one table is small or when the inner table has an index on the join column.

Tag: Normal

---

### Question 376
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Sort-Merge Join
Difficulty: Medium

Question: What is a prerequisite for efficient sort-merge join?

A) No prerequisites
B) Both inputs should be sorted on the join key
C) Random order
D) One input sorted

✔ Correct Answer: B

Reason: Sort-merge join is most efficient when both inputs are already sorted on the join key, avoiding the sorting overhead.

Tag: Normal

---

### Question 377
Domain: Databases
Topic: Database Security
Subtopic: Least Privilege Implementation
Difficulty: Easy

Question: How should the principle of least privilege be implemented?

A) Give all privileges initially
B) Grant only necessary privileges and add more as needed
C) Give no privileges
D) Random privilege assignment

✔ Correct Answer: B

Reason: Implement least privilege by granting only the minimum necessary privileges initially and adding more only when justified.

Tag: Normal

---

### Question 378
Domain: Databases
Topic: Database Security
Subtopic: Security Patches
Difficulty: Easy

Question: Why are database security patches important?

A) They are not important
B) They fix known vulnerabilities that could be exploited
C) They slow down the database
D) They delete data

✔ Correct Answer: B

Reason: Security patches fix known vulnerabilities, preventing attackers from exploiting them to compromise the database.

Tag: Normal

---

### Question 379
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Catalog Management
Difficulty: Medium

Question: What is a distributed catalog?

A) A local catalog
B) Metadata about distributed database stored across sites
C) A deleted catalog
D) A backup catalog

✔ Correct Answer: B

Reason: A distributed catalog contains metadata about the distributed database structure, stored and managed across multiple sites.

Tag: Normal

---

### Question 380
Domain: Databases
Topic: Distributed Databases
Subtopic: Naming Transparency
Difficulty: Medium

Question: What is naming transparency in distributed databases?

A) Visible names
B) Users can access objects without knowing their location or local names
C) No names
D) Encrypted names

✔ Correct Answer: B

Reason: Naming transparency allows users to access database objects using a single global name without knowing their physical location or local names.

Tag: Normal

---

### Question 381
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Memcached
Difficulty: Easy

Question: What is Memcached?

A) A relational database
B) A distributed memory caching system
C) A file system
D) An operating system

✔ Correct Answer: B

Reason: Memcached is a distributed memory caching system used to speed up dynamic web applications by caching data in RAM.

Tag: Normal

---

### Question 382
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Elasticsearch
Difficulty: Medium

Question: What is Elasticsearch primarily used for?

A) Relational data storage
B) Full-text search and analytics
C) Image storage
D) Video streaming

✔ Correct Answer: B

Reason: Elasticsearch is a distributed search and analytics engine primarily used for full-text search, log analytics, and real-time data analysis.

Tag: Normal

---

### Question 383
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Junk Dimension
Difficulty: Hard

Question: What is a junk dimension?

A) Deleted dimension
B) A dimension combining multiple low-cardinality flags and indicators
C) A broken dimension
D) A temporary dimension

✔ Correct Answer: B

Reason: A junk dimension combines multiple low-cardinality flags and indicators into a single dimension to avoid cluttering the fact table.

Tag: Normal

---

### Question 384
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Role-Playing Dimension
Difficulty: Medium

Question: What is a role-playing dimension?

A) A dimension with no role
B) A dimension used multiple times in the same fact table with different meanings
C) A deleted dimension
D) A temporary dimension

✔ Correct Answer: B

Reason: A role-playing dimension is used multiple times in the same fact table with different meanings (e.g., Order Date, Ship Date, Delivery Date all referencing the same Date dimension).

Tag: Normal

---

### Question 385
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Implicit vs Explicit Joins
Difficulty: Medium

Question: What is the difference between implicit and explicit joins?

A) No difference
B) Explicit uses JOIN keyword, implicit uses WHERE clause
C) Implicit is faster
D) Explicit is deprecated

✔ Correct Answer: B

Reason: Explicit joins use the JOIN keyword in the FROM clause, while implicit joins list tables in FROM and specify join conditions in WHERE.

Tag: Normal

---

### Question 386
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Equi-Join
Difficulty: Easy

Question: What is an equi-join?

A) A join without conditions
B) A join using equality comparison in the join condition
C) A cross join
D) An outer join

✔ Correct Answer: B

Reason: An equi-join uses equality (=) comparison in the join condition to match rows from two tables.

Tag: Normal

---

### Question 387
Domain: Databases
Topic: Advanced SQL
Subtopic: Batch Processing
Difficulty: Medium

Question: What is batch processing in databases?

A) Processing one record at a time
B) Processing multiple records or statements together
C) No processing
D) Random processing

✔ Correct Answer: B

Reason: Batch processing executes multiple database operations together, improving efficiency by reducing overhead and network round-trips.

Tag: Normal

---

### Question 388
Domain: Databases
Topic: Advanced SQL
Subtopic: Bulk Insert
Difficulty: Medium

Question: What is bulk insert?

A) Inserting one row
B) Efficiently inserting large amounts of data in a single operation
C) Deleting data
D) Updating data

✔ Correct Answer: B

Reason: Bulk insert efficiently loads large amounts of data into a table in a single operation, much faster than individual inserts.

Tag: Normal

---

### Question 389
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Safe Expressions
Difficulty: Hard

Question: What is a safe expression in relational calculus?

A) An encrypted expression
B) An expression guaranteed to produce a finite result
C) A deleted expression
D) A fast expression

✔ Correct Answer: B

Reason: A safe expression in relational calculus is guaranteed to produce a finite result, avoiding infinite or undefined results.

Tag: Past Paper

---

### Question 390
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Normalization vs Performance
Difficulty: Medium

Question: When might you choose not to normalize a database?

A) Never
B) When read performance is critical and redundancy is acceptable
C) Always normalize
D) When data is small

✔ Correct Answer: B

Reason: Denormalization may be chosen when read performance is critical and the benefits outweigh the costs of data redundancy.

Tag: Normal

---

### Question 391
Domain: Databases
Topic: Transaction Management
Subtopic: Read-Only Transactions
Difficulty: Easy

Question: What is a read-only transaction?

A) A transaction that writes data
B) A transaction that only reads data without modifications
C) A deleted transaction
D) A failed transaction

✔ Correct Answer: B

Reason: A read-only transaction only reads data without making any modifications, allowing for optimizations in concurrency control.

Tag: Normal

---

### Question 392
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Isolation Trade-offs
Difficulty: Medium

Question: What is the trade-off with higher isolation levels?

A) Better performance
B) Reduced concurrency and potentially lower performance
C) No trade-offs
D) Faster transactions

✔ Correct Answer: B

Reason: Higher isolation levels provide stronger consistency guarantees but reduce concurrency and may lower performance due to increased locking.

Tag: Normal

---

### Question 393
Domain: Databases
Topic: Concurrency Control
Subtopic: Livelock
Difficulty: Hard

Question: What is livelock?

A) A permanent lock
B) Transactions repeatedly abort and retry without making progress
C) A fast lock
D) No lock

✔ Correct Answer: B

Reason: Livelock occurs when transactions repeatedly abort and retry in response to each other without making progress, though they're not blocked.

Tag: Normal

---

### Question 394
Domain: Databases
Topic: Concurrency Control
Subtopic: Starvation
Difficulty: Medium

Question: What is starvation in concurrency control?

A) Fast execution
B) A transaction waiting indefinitely while others proceed
C) No waiting
D) Immediate execution

✔ Correct Answer: B

Reason: Starvation occurs when a transaction waits indefinitely for resources while other transactions continue to execute.

Tag: Normal

---

### Question 395
Domain: Databases
Topic: Recovery Management
Subtopic: Recovery Point Objective (RPO)
Difficulty: Easy

Question: What is Recovery Point Objective (RPO)?

A) Time to recover
B) Maximum acceptable amount of data loss measured in time
C) Recovery speed
D) Backup size

✔ Correct Answer: B

Reason: RPO is the maximum acceptable amount of data loss measured in time (e.g., losing up to 1 hour of data is acceptable).

Tag: Normal

---

### Question 396
Domain: Databases
Topic: Recovery Management
Subtopic: High Availability
Difficulty: Easy

Question: What is high availability in databases?

A) Low uptime
B) Ensuring the database is operational and accessible most of the time
C) Frequent downtime
D) No availability

✔ Correct Answer: B

Reason: High availability ensures the database system remains operational and accessible with minimal downtime, often measured in "nines" (e.g., 99.99%).

Tag: Normal

---

### Question 397
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Hints
Difficulty: Medium

Question: What are index hints?

A) Suggestions for users
B) Directives to force the optimizer to use specific indexes
C) Error messages
D) Backup instructions

✔ Correct Answer: B

Reason: Index hints are directives that force or suggest the query optimizer to use specific indexes, overriding its default choice.

Tag: Normal

---

### Question 398
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Parallel Query Execution
Difficulty: Hard

Question: What is parallel query execution?

A) Sequential execution
B) Executing different parts of a query simultaneously on multiple processors
C) Single-threaded execution
D) Slow execution

✔ Correct Answer: B

Reason: Parallel query execution divides query operations across multiple processors or cores, executing them simultaneously to improve performance.

Tag: Normal

---

### Question 399
Domain: Databases
Topic: Database Security
Subtopic: Defense in Depth
Difficulty: Medium

Question: What is defense in depth in database security?

A) Single security layer
B) Multiple layers of security controls
C) No security
D) One strong control

✔ Correct Answer: B

Reason: Defense in depth uses multiple layers of security controls so that if one layer fails, others continue to provide protection.

Tag: Normal

---

### Question 400
Domain: Databases
Topic: Introduction to Database Systems
Subtopic: Database Evolution
Difficulty: Easy

Question: What was a major limitation of hierarchical and network databases?

A) Too flexible
B) Complex navigation and lack of data independence
C) Too simple
D) No limitations

✔ Correct Answer: B

Reason: Hierarchical and network databases required complex navigation through pointer structures and lacked data independence, leading to the development of relational databases.

Tag: Normal

---

**End of Batch 04**

# Databases MCQ Bank - Batch 02

## Questions 101-200

---

### Question 101
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: String Functions
Difficulty: Easy

Question: Which SQL function converts a string to uppercase?

A) LOWER()
B) UPPER()
C) CONCAT()
D) TRIM()

✔ Correct Answer: B

Reason: UPPER() is a string function that converts all characters in a string to uppercase.

Tag: Normal

---

### Question 102
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: String Functions
Difficulty: Easy

Question: Which SQL function returns the length of a string?

A) SIZE()
B) COUNT()
C) LENGTH() or LEN()
D) STRLEN()

✔ Correct Answer: C

Reason: LENGTH() (or LEN() in some databases) returns the number of characters in a string.

Tag: Normal

---

### Question 103
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Date Functions
Difficulty: Easy

Question: Which SQL function returns the current date and time?

A) TODAY()
B) NOW() or GETDATE()
C) CURRENT()
D) DATE()

✔ Correct Answer: B

Reason: NOW() (MySQL) or GETDATE() (SQL Server) returns the current date and time.

Tag: Normal

---

### Question 104
Domain: Databases
Topic: Advanced SQL
Subtopic: Window Functions
Difficulty: Hard

Question: What is a window function in SQL?

A) A function that opens database windows
B) A function that performs calculations across a set of rows related to the current row
C) A function that creates views
D) A function that manages transactions

✔ Correct Answer: B

Reason: Window functions perform calculations across a set of table rows that are related to the current row, without collapsing rows like aggregate functions.

Tag: Past Paper

---

### Question 105
Domain: Databases
Topic: Advanced SQL
Subtopic: ROW_NUMBER Function
Difficulty: Hard

Question: What does the ROW_NUMBER() window function do?

A) Counts total rows
B) Assigns a unique sequential number to each row within a partition
C) Returns the row size
D) Deletes row numbers

✔ Correct Answer: B

Reason: ROW_NUMBER() assigns a unique sequential integer to rows within a partition of a result set, starting at 1.

Tag: Normal

---

### Question 106
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Set Operations
Difficulty: Medium

Question: Which relational algebra operation returns tuples that are in both relations?

A) Union (∪)
B) Intersection (∩)
C) Difference (−)
D) Cartesian Product (×)

✔ Correct Answer: B

Reason: The Intersection operation returns tuples that appear in both relations.

Tag: Past Paper

---

### Question 107
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Set Operations
Difficulty: Medium

Question: Which relational algebra operation returns tuples in the first relation but not in the second?

A) Union (∪)
B) Intersection (∩)
C) Difference (−)
D) Join (⋈)

✔ Correct Answer: C

Reason: The Difference operation returns tuples that are in the first relation but not in the second.

Tag: Past Paper

---

### Question 108
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Functional Dependencies
Difficulty: Medium

Question: What is a functional dependency?

A) A dependency on functions
B) A constraint where one attribute uniquely determines another
C) A foreign key relationship
D) A type of index

✔ Correct Answer: B

Reason: A functional dependency is a constraint between two sets of attributes where one set uniquely determines the values of another set.

Tag: Past Paper

---

### Question 109
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Armstrong's Axioms
Difficulty: Hard

Question: Which of the following is NOT one of Armstrong's axioms?

A) Reflexivity
B) Augmentation
C) Transitivity
D) Multiplication

✔ Correct Answer: D

Reason: Armstrong's axioms are Reflexivity, Augmentation, and Transitivity. Multiplication is not one of them.

Tag: Past Paper

---

### Question 110
Domain: Databases
Topic: Transaction Management
Subtopic: Savepoints
Difficulty: Medium

Question: What is a savepoint in transaction management?

A) A backup of the database
B) A point within a transaction to which you can roll back
C) The end of a transaction
D) A type of lock

✔ Correct Answer: B

Reason: A savepoint is a point within a transaction to which you can roll back without rolling back the entire transaction.

Tag: Normal

---

### Question 111
Domain: Databases
Topic: Concurrency Control
Subtopic: Serializability
Difficulty: Hard

Question: What does serializability ensure?

A) Transactions run in parallel
B) Concurrent execution produces the same result as some serial execution
C) Transactions are fast
D) Transactions never fail

✔ Correct Answer: B

Reason: Serializability ensures that concurrent execution of transactions produces a result equivalent to some serial (sequential) execution of those transactions.

Tag: Past Paper

---

### Question 112
Domain: Databases
Topic: Concurrency Control
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level allows dirty reads?

A) Read Uncommitted
B) Read Committed
C) Repeatable Read
D) Serializable

✔ Correct Answer: A

Reason: Read Uncommitted is the lowest isolation level and allows dirty reads (reading uncommitted changes from other transactions).

Tag: Past Paper

---

### Question 113
Domain: Databases
Topic: Concurrency Control
Subtopic: Isolation Levels
Difficulty: Hard

Question: Which isolation level provides the highest level of isolation?

A) Read Uncommitted
B) Read Committed
C) Repeatable Read
D) Serializable

✔ Correct Answer: D

Reason: Serializable is the highest isolation level, preventing dirty reads, non-repeatable reads, and phantom reads.

Tag: Past Paper

---

### Question 114
Domain: Databases
Topic: Recovery Management
Subtopic: Shadow Paging
Difficulty: Hard

Question: What is shadow paging?

A) A backup technique
B) A recovery technique using shadow copies of pages
C) A type of index
D) A locking mechanism

✔ Correct Answer: B

Reason: Shadow paging is a recovery technique that maintains two page tables (current and shadow) to enable atomic updates and recovery.

Tag: Normal

---

### Question 115
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Dense vs Sparse Index
Difficulty: Medium

Question: What is a dense index?

A) An index with many entries
B) An index with an entry for every search key value in the file
C) An index with few entries
D) An index on multiple columns

✔ Correct Answer: B

Reason: A dense index has an index entry for every search key value in the data file.

Tag: Past Paper

---

### Question 116
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Dense vs Sparse Index
Difficulty: Medium

Question: What is a sparse index?

A) An index with few columns
B) An index with entries only for some search key values
C) An index on all columns
D) A temporary index

✔ Correct Answer: B

Reason: A sparse index has index entries only for some of the search key values, typically one per block, requiring the file to be sorted.

Tag: Past Paper

---

### Question 117
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: Which join algorithm is most efficient for large tables when both are sorted on the join attribute?

A) Nested loop join
B) Hash join
C) Merge join
D) Cartesian join

✔ Correct Answer: C

Reason: Merge join is most efficient for large sorted tables, as it scans both tables once in a coordinated manner.

Tag: Past Paper

---

### Question 118
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Join Algorithms
Difficulty: Hard

Question: Which join algorithm builds a hash table on one relation?

A) Nested loop join
B) Hash join
C) Merge join
D) Index join

✔ Correct Answer: B

Reason: Hash join builds a hash table on one relation (usually the smaller one) and probes it with tuples from the other relation.

Tag: Normal

---

### Question 119
Domain: Databases
Topic: Database Security
Subtopic: Views for Security
Difficulty: Medium

Question: How can views enhance database security?

A) By encrypting data
B) By restricting user access to specific columns or rows
C) By backing up data
D) By indexing data

✔ Correct Answer: B

Reason: Views can enhance security by providing users access only to specific columns or rows, hiding sensitive data.

Tag: Normal

---

### Question 120
Domain: Databases
Topic: Database Security
Subtopic: Audit Trails
Difficulty: Easy

Question: What is an audit trail in database security?

A) A backup log
B) A record of database activities for security monitoring
C) A type of index
D) A recovery mechanism

✔ Correct Answer: B

Reason: An audit trail is a chronological record of database activities used for security monitoring, compliance, and forensic analysis.

Tag: Normal

---

### Question 121
Domain: Databases
Topic: Distributed Databases
Subtopic: Horizontal Fragmentation
Difficulty: Medium

Question: What is horizontal fragmentation?

A) Splitting tables by columns
B) Splitting tables by rows based on conditions
C) Encrypting data
D) Compressing data

✔ Correct Answer: B

Reason: Horizontal fragmentation divides a relation by rows, with each fragment containing a subset of tuples based on some condition.

Tag: Normal

---

### Question 122
Domain: Databases
Topic: Distributed Databases
Subtopic: Vertical Fragmentation
Difficulty: Medium

Question: What is vertical fragmentation?

A) Splitting tables by rows
B) Splitting tables by columns
C) Deleting columns
D) Sorting columns

✔ Correct Answer: B

Reason: Vertical fragmentation divides a relation by columns, with each fragment containing a subset of attributes (usually including the primary key).

Tag: Normal

---

### Question 123
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: BASE Properties
Difficulty: Hard

Question: What does BASE stand for in NoSQL databases?

A) Basic Available Secure Efficient
B) Basically Available, Soft state, Eventually consistent
C) Backup And Storage Engine
D) Binary Accessible Structured Entities

✔ Correct Answer: B

Reason: BASE stands for Basically Available, Soft state, Eventually consistent - properties often associated with NoSQL databases as an alternative to ACID.

Tag: Past Paper

---

### Question 124
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Eventual Consistency
Difficulty: Medium

Question: What is eventual consistency?

A) Data is always consistent
B) Data will become consistent over time if no new updates are made
C) Data is never consistent
D) Data is immediately consistent

✔ Correct Answer: B

Reason: Eventual consistency guarantees that if no new updates are made to a data item, eventually all accesses will return the last updated value.

Tag: Normal

---

### Question 125
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Star Schema
Difficulty: Medium

Question: What is a star schema in data warehousing?

A) A schema shaped like a star
B) A schema with a central fact table connected to dimension tables
C) A type of index
D) A backup strategy

✔ Correct Answer: B

Reason: A star schema has a central fact table containing measures, surrounded by dimension tables containing descriptive attributes.

Tag: Past Paper

---

### Question 126
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Snowflake Schema
Difficulty: Medium

Question: How does a snowflake schema differ from a star schema?

A) It has more fact tables
B) Dimension tables are normalized into multiple related tables
C) It has fewer tables
D) It uses different data types

✔ Correct Answer: B

Reason: In a snowflake schema, dimension tables are normalized into multiple related tables, creating a more complex structure than a star schema.

Tag: Past Paper

---

### Question 127
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Self Join
Difficulty: Medium

Question: What is a self join?

A) A join with itself
B) A table joined with itself
C) A join that always succeeds
D) A join without conditions

✔ Correct Answer: B

Reason: A self join is a regular join where a table is joined with itself, typically using aliases to distinguish the two instances.

Tag: Normal

---

### Question 128
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Cross Join
Difficulty: Medium

Question: What does a CROSS JOIN produce?

A) Only matching rows
B) The Cartesian product of two tables
C) No rows
D) Only unique rows

✔ Correct Answer: B

Reason: CROSS JOIN produces the Cartesian product of two tables, combining each row from the first table with every row from the second table.

Tag: Normal

---

### Question 129
Domain: Databases
Topic: Advanced SQL
Subtopic: Common Table Expressions (CTE)
Difficulty: Hard

Question: What is a Common Table Expression (CTE)?

A) A permanent table
B) A temporary named result set that exists within a single query
C) A type of index
D) A stored procedure

✔ Correct Answer: B

Reason: A CTE is a temporary named result set defined using WITH clause, existing only within the execution scope of a single query.

Tag: Normal

---

### Question 130
Domain: Databases
Topic: Advanced SQL
Subtopic: Recursive CTE
Difficulty: Hard

Question: What is a recursive CTE used for?

A) Creating loops
B) Querying hierarchical or tree-structured data
C) Deleting data
D) Creating indexes

✔ Correct Answer: B

Reason: Recursive CTEs are used to query hierarchical or tree-structured data, such as organizational charts or bill of materials.

Tag: Normal

---

### Question 131
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Composite Key
Difficulty: Easy

Question: What is a composite key?

A) A key made of multiple attributes
B) A key made of one attribute
C) A foreign key
D) An index

✔ Correct Answer: A

Reason: A composite key is a primary key composed of two or more attributes that together uniquely identify a record.

Tag: Normal

---

### Question 132
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Alternate Key
Difficulty: Medium

Question: What is an alternate key?

A) A backup key
B) A candidate key that is not chosen as the primary key
C) A foreign key
D) A temporary key

✔ Correct Answer: B

Reason: An alternate key is a candidate key that was not selected as the primary key but can still uniquely identify records.

Tag: Past Paper

---

### Question 133
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Fourth Normal Form (4NF)
Difficulty: Hard

Question: What does Fourth Normal Form (4NF) eliminate?

A) Partial dependencies
B) Transitive dependencies
C) Multi-valued dependencies
D) Functional dependencies

✔ Correct Answer: C

Reason: 4NF eliminates multi-valued dependencies, where one attribute determines multiple independent multi-valued facts about another attribute.

Tag: Past Paper

---

### Question 134
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Fifth Normal Form (5NF)
Difficulty: Hard

Question: What does Fifth Normal Form (5NF) address?

A) Partial dependencies
B) Join dependencies
C) Transitive dependencies
D) Multi-valued dependencies

✔ Correct Answer: B

Reason: 5NF (also called Project-Join Normal Form) addresses join dependencies, ensuring that a relation cannot be decomposed into smaller relations without loss of information.

Tag: Past Paper

---

### Question 135
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Commands
Difficulty: Easy

Question: Which SQL command is used to permanently save transaction changes?

A) SAVE
B) COMMIT
C) END
D) FINISH

✔ Correct Answer: B

Reason: COMMIT is the TCL command that permanently saves all changes made in the current transaction.

Tag: Normal

---

### Question 136
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Commands
Difficulty: Easy

Question: Which SQL command is used to undo transaction changes?

A) UNDO
B) REVERT
C) ROLLBACK
D) CANCEL

✔ Correct Answer: C

Reason: ROLLBACK is the TCL command that undoes all changes made in the current transaction.

Tag: Normal

---

### Question 137
Domain: Databases
Topic: Concurrency Control
Subtopic: Phantom Reads
Difficulty: Hard

Question: What is a phantom read?

A) Reading deleted data
B) Reading new rows inserted by another transaction
C) Reading uncommitted data
D) Reading old data

✔ Correct Answer: B

Reason: A phantom read occurs when a transaction re-executes a query and finds new rows that were inserted by another committed transaction.

Tag: Past Paper

---

### Question 138
Domain: Databases
Topic: Concurrency Control
Subtopic: Non-Repeatable Reads
Difficulty: Medium

Question: What is a non-repeatable read?

A) A read that fails
B) Reading different values for the same row in the same transaction
C) Reading new rows
D) Reading deleted rows

✔ Correct Answer: B

Reason: A non-repeatable read occurs when a transaction reads the same row twice and gets different values because another transaction modified it.

Tag: Past Paper

---

### Question 139
Domain: Databases
Topic: Concurrency Control
Subtopic: Dirty Reads
Difficulty: Medium

Question: What is a dirty read?

A) Reading corrupted data
B) Reading uncommitted changes from another transaction
C) Reading old data
D) Reading encrypted data

✔ Correct Answer: B

Reason: A dirty read occurs when a transaction reads data that has been modified by another transaction but not yet committed.

Tag: Past Paper

---

### Question 140
Domain: Databases
Topic: Recovery Management
Subtopic: Write-Ahead Logging
Difficulty: Hard

Question: What is the write-ahead logging (WAL) protocol?

A) Writing data before logging
B) Writing log records to disk before writing data pages
C) Writing data and logs simultaneously
D) Writing logs after data

✔ Correct Answer: B

Reason: WAL protocol requires that log records be written to stable storage before the corresponding data pages are written, ensuring recoverability.

Tag: Past Paper

---

### Question 141
Domain: Databases
Topic: Indexing & File Organization
Subtopic: B+ Tree
Difficulty: Hard

Question: What is the main advantage of B+ trees over B-trees for database indexing?

A) Smaller size
B) All data is stored in leaf nodes, enabling efficient sequential access
C) Faster insertion
D) No advantage

✔ Correct Answer: B

Reason: In B+ trees, all data is stored in leaf nodes which are linked, enabling efficient sequential access and range queries.

Tag: Past Paper

---

### Question 142
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Bitmap Index
Difficulty: Medium

Question: When is a bitmap index most effective?

A) For high-cardinality columns
B) For low-cardinality columns with few distinct values
C) For text columns
D) For large text fields

✔ Correct Answer: B

Reason: Bitmap indexes are most effective for low-cardinality columns (few distinct values) like gender, status, or boolean fields.

Tag: Normal

---

### Question 143
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Rewriting
Difficulty: Medium

Question: What is query rewriting in optimization?

A) Correcting syntax errors
B) Transforming a query into an equivalent but more efficient form
C) Translating between SQL dialects
D) Formatting query text

✔ Correct Answer: B

Reason: Query rewriting transforms a query into an equivalent form that can be executed more efficiently, using algebraic transformations.

Tag: Normal

---

### Question 144
Domain: Databases
Topic: Database Security
Subtopic: Role-Based Access Control
Difficulty: Medium

Question: What is role-based access control (RBAC)?

A) Controlling database roles
B) Assigning permissions to roles rather than individual users
C) Creating user roles
D) Deleting user accounts

✔ Correct Answer: B

Reason: RBAC assigns permissions to roles, and users are assigned to roles, simplifying permission management.

Tag: Normal

---

### Question 145
Domain: Databases
Topic: Database Security
Subtopic: Data Masking
Difficulty: Medium

Question: What is data masking?

A) Deleting data
B) Hiding sensitive data by replacing it with fictitious but realistic data
C) Encrypting all data
D) Compressing data

✔ Correct Answer: B

Reason: Data masking obscures sensitive data by replacing it with fictitious but realistic values, useful for testing and development environments.

Tag: Normal

---

### Question 146
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Query Processing
Difficulty: Hard

Question: What is a major challenge in distributed query processing?

A) Syntax errors
B) Minimizing data transfer between sites
C) Creating tables
D) User authentication

✔ Correct Answer: B

Reason: A major challenge in distributed query processing is minimizing data transfer between sites to reduce network overhead and improve performance.

Tag: Normal

---

### Question 147
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Deadlock
Difficulty: Hard

Question: Why is deadlock detection more complex in distributed databases?

A) More users
B) Transactions span multiple sites requiring global deadlock detection
C) Larger databases
D) More tables

✔ Correct Answer: B

Reason: Distributed deadlock detection is complex because transactions can span multiple sites, requiring coordination to detect cycles in the global wait-for graph.

Tag: Normal

---

### Question 148
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Sharding
Difficulty: Medium

Question: What is sharding in databases?

A) Deleting data
B) Horizontally partitioning data across multiple servers
C) Encrypting data
D) Backing up data

✔ Correct Answer: B

Reason: Sharding is a horizontal partitioning technique that distributes data across multiple servers to improve scalability and performance.

Tag: Normal

---

### Question 149
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Replication Strategies
Difficulty: Medium

Question: What is master-slave replication?

A) All nodes are equal
B) One master node handles writes, slave nodes replicate and handle reads
C) No replication occurs
D) Random node selection

✔ Correct Answer: B

Reason: In master-slave replication, the master node handles all write operations, and slave nodes replicate the data and can handle read operations.

Tag: Normal

---

### Question 150
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Fact Table
Difficulty: Easy

Question: What does a fact table contain in a data warehouse?

A) Descriptive attributes
B) Quantitative measures and foreign keys to dimension tables
C) User information
D) System logs

✔ Correct Answer: B

Reason: A fact table contains quantitative measures (facts) for analysis and foreign keys linking to dimension tables.

Tag: Normal

---

### Question 151
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Dimension Table
Difficulty: Easy

Question: What does a dimension table contain?

A) Numeric measures
B) Descriptive attributes for analysis
C) Transaction logs
D) System metadata

✔ Correct Answer: B

Reason: Dimension tables contain descriptive attributes (dimensions) used for filtering, grouping, and labeling facts.

Tag: Normal

---

### Question 152
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: LIMIT Clause
Difficulty: Easy

Question: What does the LIMIT clause do?

A) Limits column width
B) Limits the number of rows returned
C) Limits user access
D) Limits table size

✔ Correct Answer: B

Reason: LIMIT (or TOP in some databases) restricts the number of rows returned by a query.

Tag: Normal

---

### Question 153
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: OFFSET Clause
Difficulty: Medium

Question: What is the purpose of the OFFSET clause?

A) To skip a specified number of rows before returning results
B) To sort results
C) To filter results
D) To join tables

✔ Correct Answer: A

Reason: OFFSET skips a specified number of rows before beginning to return rows, often used with LIMIT for pagination.

Tag: Normal

---

### Question 154
Domain: Databases
Topic: Advanced SQL
Subtopic: PIVOT Operation
Difficulty: Hard

Question: What does the PIVOT operation do?

A) Rotates the database
B) Transforms rows into columns
C) Deletes rows
D) Sorts columns

✔ Correct Answer: B

Reason: PIVOT transforms row data into columns, useful for creating cross-tabulation reports and summary views.

Tag: Normal

---

### Question 155
Domain: Databases
Topic: Advanced SQL
Subtopic: UNPIVOT Operation
Difficulty: Hard

Question: What does the UNPIVOT operation do?

A) Reverses a pivot
B) Transforms columns into rows
C) Deletes columns
D) Sorts rows

✔ Correct Answer: B

Reason: UNPIVOT transforms column data into rows, essentially reversing a PIVOT operation.

Tag: Normal

---

### Question 156
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Natural Join
Difficulty: Medium

Question: What is a natural join?

A) A join using all common attributes
B) A join without conditions
C) A cross join
D) An outer join

✔ Correct Answer: A

Reason: A natural join automatically joins tables based on all columns with the same name in both tables.

Tag: Past Paper

---

### Question 157
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Theta Join
Difficulty: Medium

Question: What is a theta join?

A) A join using only equality conditions
B) A join using any comparison operator
C) A natural join
D) A cross join

✔ Correct Answer: B

Reason: A theta join uses any comparison operator (=, <, >, ≤, ≥, ≠) in the join condition, not just equality.

Tag: Past Paper

---

### Question 158
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Lossless Decomposition
Difficulty: Hard

Question: What is lossless decomposition?

A) Decomposition that loses data
B) Decomposition where original relation can be reconstructed from decomposed relations
C) Decomposition that compresses data
D) Decomposition that deletes data

✔ Correct Answer: B

Reason: Lossless decomposition ensures that the original relation can be reconstructed by joining the decomposed relations without losing information.

Tag: Past Paper

---

### Question 159
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Dependency Preservation
Difficulty: Hard

Question: What does dependency preservation mean in decomposition?

A) All dependencies are deleted
B) All functional dependencies can be checked without joining relations
C) Dependencies are encrypted
D) Dependencies are backed up

✔ Correct Answer: B

Reason: Dependency preservation ensures that all functional dependencies can be checked by examining individual relations without needing to perform joins.

Tag: Past Paper

---

### Question 160
Domain: Databases
Topic: Transaction Management
Subtopic: Cascading Rollback
Difficulty: Hard

Question: What is cascading rollback?

A) Rolling back one transaction
B) Rolling back multiple transactions due to dependencies
C) A fast rollback
D) A partial rollback

✔ Correct Answer: B

Reason: Cascading rollback occurs when aborting one transaction forces the rollback of other transactions that read its uncommitted data.

Tag: Past Paper

---

### Question 161
Domain: Databases
Topic: Concurrency Control
Subtopic: Optimistic Concurrency Control
Difficulty: Hard

Question: How does optimistic concurrency control work?

A) Always locks data
B) Assumes conflicts are rare and validates at commit time
C) Never allows concurrent access
D) Uses timestamps only

✔ Correct Answer: B

Reason: Optimistic concurrency control assumes conflicts are rare, allows transactions to proceed without locking, and validates for conflicts at commit time.

Tag: Normal

---

### Question 162
Domain: Databases
Topic: Concurrency Control
Subtopic: Pessimistic Concurrency Control
Difficulty: Medium

Question: How does pessimistic concurrency control work?

A) Never uses locks
B) Locks data before accessing to prevent conflicts
C) Assumes no conflicts
D) Only validates at commit

✔ Correct Answer: B

Reason: Pessimistic concurrency control assumes conflicts are likely and locks data before accessing it to prevent conflicts.

Tag: Normal

---

### Question 163
Domain: Databases
Topic: Recovery Management
Subtopic: ARIES Recovery Algorithm
Difficulty: Hard

Question: What are the three phases of the ARIES recovery algorithm?

A) Read, Write, Commit
B) Analysis, Redo, Undo
C) Lock, Unlock, Validate
D) Begin, Execute, End

✔ Correct Answer: B

Reason: ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) has three phases: Analysis, Redo, and Undo.

Tag: Past Paper

---

### Question 164
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Inverted Index
Difficulty: Medium

Question: What is an inverted index primarily used for?

A) Numeric data
B) Full-text search
C) Date fields
D) Foreign keys

✔ Correct Answer: B

Reason: An inverted index maps content (words) to their locations in documents, primarily used for full-text search engines.

Tag: Normal

---

### Question 165
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Selectivity
Difficulty: Medium

Question: What is selectivity in query optimization?

A) The number of columns selected
B) The fraction of tuples that satisfy a condition
C) The speed of selection
D) The order of selection

✔ Correct Answer: B

Reason: Selectivity is the fraction of tuples that satisfy a selection condition, used to estimate the cost of query operations.

Tag: Normal

---

### Question 166
Domain: Databases
Topic: Database Security
Subtopic: Transparent Data Encryption
Difficulty: Medium

Question: What is transparent data encryption (TDE)?

A) Visible encryption
B) Automatic encryption/decryption at the storage level
C) Manual encryption
D) No encryption

✔ Correct Answer: B

Reason: TDE automatically encrypts data at rest at the storage level, transparent to applications accessing the data.

Tag: Normal

---

### Question 167
Domain: Databases
Topic: Database Security
Subtopic: Column-Level Encryption
Difficulty: Medium

Question: What is column-level encryption?

A) Encrypting entire tables
B) Encrypting specific columns containing sensitive data
C) Encrypting row data
D) Encrypting indexes

✔ Correct Answer: B

Reason: Column-level encryption selectively encrypts specific columns that contain sensitive data, providing granular security.

Tag: Normal

---

### Question 168
Domain: Databases
Topic: Distributed Databases
Subtopic: Quorum Consensus
Difficulty: Hard

Question: What is quorum consensus in distributed databases?

A) All nodes must agree
B) A majority of nodes must agree for an operation
C) Only one node decides
D) No consensus needed

✔ Correct Answer: B

Reason: Quorum consensus requires a majority of nodes to agree on an operation, balancing consistency and availability.

Tag: Normal

---

### Question 169
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Transaction
Difficulty: Medium

Question: What makes distributed transactions more complex than local transactions?

A) More users
B) Coordination across multiple sites with potential network failures
C) Larger data
D) More tables

✔ Correct Answer: B

Reason: Distributed transactions require coordination across multiple sites, dealing with network latency, failures, and maintaining ACID properties globally.

Tag: Normal

---

### Question 170
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Time-Series Databases
Difficulty: Medium

Question: What type of data are time-series databases optimized for?

A) Relational data
B) Data indexed by time stamps
C) Graph data
D) Document data

✔ Correct Answer: B

Reason: Time-series databases are optimized for storing and querying data indexed by time stamps, like sensor data or metrics.

Tag: Normal

---

### Question 171
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: In-Memory Databases
Difficulty: Medium

Question: What is the main advantage of in-memory databases?

A) Lower cost
B) Extremely fast data access
C) Larger storage capacity
D) Better security

✔ Correct Answer: B

Reason: In-memory databases store data in RAM rather than disk, providing extremely fast data access and query performance.

Tag: Normal

---

### Question 172
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Operations
Difficulty: Medium

Question: What is a drill-down operation in OLAP?

A) Deleting data
B) Navigating from less detailed to more detailed data
C) Summarizing data
D) Backing up data

✔ Correct Answer: B

Reason: Drill-down navigates from less detailed (aggregated) data to more detailed data, like going from yearly to monthly sales.

Tag: Normal

---

### Question 173
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Operations
Difficulty: Medium

Question: What is a roll-up operation in OLAP?

A) Deleting data
B) Navigating from more detailed to less detailed data
C) Filtering data
D) Sorting data

✔ Correct Answer: B

Reason: Roll-up (or drill-up) navigates from more detailed data to less detailed (aggregated) data, like going from monthly to yearly sales.

Tag: Normal

---

### Question 174
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Operations
Difficulty: Medium

Question: What is a slice operation in OLAP?

A) Deleting a dimension
B) Selecting a single value from one dimension
C) Rotating the cube
D) Aggregating data

✔ Correct Answer: B

Reason: Slice selects a single value from one dimension, creating a sub-cube with one fewer dimension.

Tag: Normal

---

### Question 175
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: OLAP Operations
Difficulty: Medium

Question: What is a dice operation in OLAP?

A) Random selection
B) Selecting specific values from multiple dimensions
C) Deleting data
D) Sorting data

✔ Correct Answer: B

Reason: Dice selects specific values from two or more dimensions, creating a sub-cube.

Tag: Normal

---

### Question 176
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: COALESCE Function
Difficulty: Medium

Question: What does the COALESCE function do?

A) Combines strings
B) Returns the first non-NULL value from a list
C) Counts NULL values
D) Deletes NULL values

✔ Correct Answer: B

Reason: COALESCE returns the first non-NULL value in a list of expressions, useful for handling NULL values.

Tag: Normal

---

### Question 177
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: NULLIF Function
Difficulty: Medium

Question: What does the NULLIF function do?

A) Removes NULL values
B) Returns NULL if two expressions are equal, otherwise returns the first expression
C) Counts NULL values
D) Converts NULL to zero

✔ Correct Answer: B

Reason: NULLIF returns NULL if the two arguments are equal; otherwise, it returns the first argument.

Tag: Normal

---

### Question 178
Domain: Databases
Topic: Advanced SQL
Subtopic: RANK Function
Difficulty: Hard

Question: How does RANK() differ from ROW_NUMBER()?

A) No difference
B) RANK() assigns the same rank to ties, ROW_NUMBER() assigns unique numbers
C) RANK() is faster
D) ROW_NUMBER() handles NULL better

✔ Correct Answer: B

Reason: RANK() assigns the same rank to rows with equal values (with gaps), while ROW_NUMBER() assigns unique sequential numbers regardless of ties.

Tag: Normal

---

### Question 179
Domain: Databases
Topic: Advanced SQL
Subtopic: DENSE_RANK Function
Difficulty: Hard

Question: How does DENSE_RANK() differ from RANK()?

A) No difference
B) DENSE_RANK() doesn't leave gaps in ranking after ties
C) DENSE_RANK() is faster
D) RANK() is more accurate

✔ Correct Answer: B

Reason: DENSE_RANK() assigns consecutive ranks without gaps after ties, while RANK() leaves gaps.

Tag: Normal

---

### Question 180
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Domain
Difficulty: Easy

Question: What is a domain in relational databases?

A) A website address
B) The set of allowable values for an attribute
C) A table name
D) A database name

✔ Correct Answer: B

Reason: A domain is the set of allowable (valid) values that an attribute can take.

Tag: Past Paper

---

### Question 181
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Tuple
Difficulty: Easy

Question: What is a tuple in relational databases?

A) A column
B) A row in a table
C) A table
D) A database

✔ Correct Answer: B

Reason: A tuple is a row in a relation (table), representing a single record.

Tag: Past Paper

---

### Question 182
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Cardinality
Difficulty: Easy

Question: What does cardinality refer to in relational databases?

A) The number of columns
B) The number of rows in a table
C) The number of tables
D) The number of databases

✔ Correct Answer: B

Reason: Cardinality refers to the number of tuples (rows) in a relation.

Tag: Past Paper

---

### Question 183
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Degree
Difficulty: Easy

Question: What does degree refer to in relational databases?

A) The number of rows
B) The number of attributes (columns) in a relation
C) The number of tables
D) The complexity of queries

✔ Correct Answer: B

Reason: Degree refers to the number of attributes (columns) in a relation.

Tag: Past Paper

---

### Question 184
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Anomalies
Difficulty: Medium

Question: What is an insertion anomaly?

A) Difficulty inserting data due to missing required information
B) Fast insertion
C) Automatic insertion
D) Encrypted insertion

✔ Correct Answer: A

Reason: An insertion anomaly occurs when certain data cannot be inserted without the presence of other data due to poor database design.

Tag: Past Paper

---

### Question 185
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Anomalies
Difficulty: Medium

Question: What is a deletion anomaly?

A) Fast deletion
B) Unintended loss of data when deleting other data
C) Encrypted deletion
D) Automatic deletion

✔ Correct Answer: B

Reason: A deletion anomaly occurs when deleting data unintentionally causes the loss of other important data.

Tag: Past Paper

---

### Question 186
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Anomalies
Difficulty: Medium

Question: What is an update anomaly?

A) Fast updates
B) Inconsistency when updating data in multiple places
C) Automatic updates
D) Encrypted updates

✔ Correct Answer: B

Reason: An update anomaly occurs when updating data in one place requires updating it in multiple places, risking inconsistency.

Tag: Past Paper

---

### Question 187
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Schedule
Difficulty: Hard

Question: What is a serial schedule?

A) A schedule with one transaction
B) A schedule where transactions execute one after another without interleaving
C) A fast schedule
D) A parallel schedule

✔ Correct Answer: B

Reason: A serial schedule executes transactions one after another without any interleaving of operations.

Tag: Past Paper

---

### Question 188
Domain: Databases
Topic: Transaction Management
Subtopic: Transaction Schedule
Difficulty: Hard

Question: What is a serializable schedule?

A) A serial schedule
B) A concurrent schedule equivalent to some serial schedule
C) A fast schedule
D) A schedule with no transactions

✔ Correct Answer: B

Reason: A serializable schedule is a concurrent schedule whose effect is equivalent to some serial schedule of the same transactions.

Tag: Past Paper

---

### Question 189
Domain: Databases
Topic: Concurrency Control
Subtopic: Lock Granularity
Difficulty: Medium

Question: What is lock granularity?

A) The size of locks
B) The size of the data item that can be locked
C) The number of locks
D) The speed of locking

✔ Correct Answer: B

Reason: Lock granularity refers to the size of the data item that can be locked, ranging from entire database to individual records or fields.

Tag: Normal

---

### Question 190
Domain: Databases
Topic: Concurrency Control
Subtopic: Intention Locks
Difficulty: Hard

Question: What is the purpose of intention locks?

A) To lock entire database
B) To indicate intention to acquire locks at finer granularity
C) To unlock data
D) To delete locks

✔ Correct Answer: B

Reason: Intention locks indicate a transaction's intention to acquire locks at a finer granularity level, enabling efficient multi-granularity locking.

Tag: Past Paper

---

### Question 191
Domain: Databases
Topic: Recovery Management
Subtopic: Immediate Update
Difficulty: Hard

Question: What is immediate update in recovery?

A) Updates are never written
B) Updates are written to disk before transaction commits
C) Updates are delayed
D) Updates are encrypted

✔ Correct Answer: B

Reason: In immediate update, database modifications are written to disk before the transaction commits, requiring both undo and redo for recovery.

Tag: Normal

---

### Question 192
Domain: Databases
Topic: Recovery Management
Subtopic: Deferred Update
Difficulty: Hard

Question: What is deferred update in recovery?

A) Updates are immediate
B) Updates are written to disk only after transaction commits
C) Updates are never written
D) Updates are encrypted

✔ Correct Answer: B

Reason: In deferred update, database modifications are written to disk only after the transaction commits, requiring only redo for recovery.

Tag: Normal

---

### Question 193
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Composite Index
Difficulty: Medium

Question: What is a composite index?

A) An index on a single column
B) An index on multiple columns
C) A temporary index
D) An encrypted index

✔ Correct Answer: B

Reason: A composite index is an index on two or more columns, useful for queries that filter on multiple columns.

Tag: Normal

---

### Question 194
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Covering Index
Difficulty: Medium

Question: What is a covering index?

A) An index that covers the entire table
B) An index that includes all columns needed by a query
C) A temporary index
D) A partial index

✔ Correct Answer: B

Reason: A covering index includes all columns needed by a query, allowing the query to be satisfied entirely from the index without accessing the table.

Tag: Normal

---

### Question 195
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Heuristic Optimization
Difficulty: Medium

Question: What is heuristic-based query optimization?

A) Random optimization
B) Using rules of thumb to transform queries
C) No optimization
D) Manual optimization

✔ Correct Answer: B

Reason: Heuristic-based optimization uses rules of thumb (like pushing selections down) to transform queries into more efficient forms.

Tag: Normal

---

### Question 196
Domain: Databases
Topic: Database Security
Subtopic: Principle of Least Privilege
Difficulty: Easy

Question: What does the principle of least privilege mean in database security?

A) Give maximum privileges
B) Give only the minimum privileges necessary
C) Give no privileges
D) Give random privileges

✔ Correct Answer: B

Reason: The principle of least privilege states that users should be granted only the minimum privileges necessary to perform their tasks.

Tag: Normal

---

### Question 197
Domain: Databases
Topic: Distributed Databases
Subtopic: CAP Theorem Trade-offs
Difficulty: Hard

Question: In the CAP theorem, what must be sacrificed during a network partition?

A) Nothing
B) Either Consistency or Availability
C) Partition tolerance
D) All three

✔ Correct Answer: B

Reason: During a network partition, a distributed system must choose between Consistency and Availability, as Partition tolerance is mandatory.

Tag: Past Paper

---

### Question 198
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: MapReduce
Difficulty: Hard

Question: What is MapReduce?

A) A database type
B) A programming model for processing large datasets in parallel
C) A query language
D) An indexing method

✔ Correct Answer: B

Reason: MapReduce is a programming model for processing and generating large datasets in parallel across distributed clusters.

Tag: Normal

---

### Question 199
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mart
Difficulty: Easy

Question: What is a data mart?

A) A shopping center for data
B) A subset of a data warehouse focused on a specific area
C) A backup system
D) A type of NoSQL database

✔ Correct Answer: B

Reason: A data mart is a subset of a data warehouse that focuses on a specific business area, department, or subject.

Tag: Normal

---

### Question 200
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Mining
Difficulty: Easy

Question: What is data mining?

A) Extracting raw data
B) Discovering patterns and knowledge from large datasets
C) Deleting old data
D) Backing up data

✔ Correct Answer: B

Reason: Data mining is the process of discovering patterns, correlations, and knowledge from large datasets using statistical and machine learning techniques.

Tag: Normal

---

**End of Batch 02**

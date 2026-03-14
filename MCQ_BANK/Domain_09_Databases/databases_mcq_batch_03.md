# Databases MCQ Bank - Batch 03

## Questions 201-300

---

### Question 201
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: EXISTS Operator
Difficulty: Medium

Question: What does the EXISTS operator check?

A) If a table exists
B) If a subquery returns any rows
C) If a column exists
D) If a database exists

✔ Correct Answer: B

Reason: EXISTS returns TRUE if the subquery returns one or more rows, used to test for the existence of rows.

Tag: Normal

---

### Question 202
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: ANY Operator
Difficulty: Medium

Question: What does the ANY operator do?

A) Returns any random row
B) Returns TRUE if any subquery value meets the condition
C) Deletes any row
D) Updates any row

✔ Correct Answer: B

Reason: ANY returns TRUE if the comparison is TRUE for at least one value returned by the subquery.

Tag: Normal

---

### Question 203
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: ALL Operator
Difficulty: Medium

Question: What does the ALL operator do?

A) Selects all rows
B) Returns TRUE if the comparison is TRUE for all subquery values
C) Deletes all rows
D) Updates all rows

✔ Correct Answer: B

Reason: ALL returns TRUE if the comparison is TRUE for all values returned by the subquery.

Tag: Normal

---

### Question 204
Domain: Databases
Topic: Advanced SQL
Subtopic: Materialized Views
Difficulty: Hard

Question: What is a materialized view?

A) A regular view
B) A view whose results are physically stored and periodically refreshed
C) A temporary view
D) An encrypted view

✔ Correct Answer: B

Reason: A materialized view stores the query results physically, improving query performance but requiring periodic refresh to stay current.

Tag: Normal

---

### Question 205
Domain: Databases
Topic: Advanced SQL
Subtopic: Indexed Views
Difficulty: Hard

Question: What is an indexed view?

A) A view with no index
B) A materialized view with indexes created on it
C) A temporary view
D) A virtual view

✔ Correct Answer: B

Reason: An indexed view (or materialized view with indexes) has one or more indexes created on it to further improve query performance.

Tag: Normal

---

### Question 206
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Division Operation
Difficulty: Hard

Question: What does the division operation in relational algebra do?

A) Divides numeric values
B) Finds tuples in one relation that match all tuples in another relation
C) Splits tables
D) Deletes rows

✔ Correct Answer: B

Reason: Division finds tuples in relation R that are associated with all tuples in relation S, useful for "for all" queries.

Tag: Past Paper

---

### Question 207
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Tuple Relational Calculus
Difficulty: Hard

Question: What is tuple relational calculus?

A) Calculating tuple sizes
B) A non-procedural query language using tuple variables
C) A procedural language
D) A programming language

✔ Correct Answer: B

Reason: Tuple relational calculus is a non-procedural query language that uses tuple variables to specify queries declaratively.

Tag: Past Paper

---

### Question 208
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Domain Relational Calculus
Difficulty: Hard

Question: What is domain relational calculus?

A) Calculating domains
B) A non-procedural query language using domain variables
C) A procedural language
D) A database design method

✔ Correct Answer: B

Reason: Domain relational calculus uses domain variables (ranging over attribute values) rather than tuple variables.

Tag: Past Paper

---

### Question 209
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Closure of Attributes
Difficulty: Hard

Question: What is the closure of a set of attributes?

A) Deleting attributes
B) The set of all attributes functionally determined by the given set
C) Encrypting attributes
D) Sorting attributes

✔ Correct Answer: B

Reason: The closure of a set of attributes is the set of all attributes that can be functionally determined from that set using functional dependencies.

Tag: Past Paper

---

### Question 210
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Minimal Cover
Difficulty: Hard

Question: What is a minimal cover (canonical cover) of functional dependencies?

A) The largest set of dependencies
B) A minimal set of dependencies equivalent to the original set
C) An encrypted set
D) A sorted set

✔ Correct Answer: B

Reason: A minimal cover is a minimal set of functional dependencies that is equivalent to the original set, with no redundant dependencies.

Tag: Past Paper

---

### Question 211
Domain: Databases
Topic: Transaction Management
Subtopic: Read-Write Conflicts
Difficulty: Hard

Question: What is a write-read (WR) conflict?

A) Two writes to the same data
B) A transaction reads data written by another uncommitted transaction
C) Two reads of the same data
D) No conflict

✔ Correct Answer: B

Reason: A WR conflict (dirty read) occurs when a transaction reads data that has been written but not committed by another transaction.

Tag: Past Paper

---

### Question 212
Domain: Databases
Topic: Transaction Management
Subtopic: Read-Write Conflicts
Difficulty: Hard

Question: What is a write-write (WW) conflict?

A) Two reads
B) Two transactions write to the same data item
C) A read and a write
D) No conflict

✔ Correct Answer: B

Reason: A WW conflict (lost update) occurs when two transactions write to the same data item, potentially causing one update to be lost.

Tag: Past Paper

---

### Question 213
Domain: Databases
Topic: Transaction Management
Subtopic: Read-Write Conflicts
Difficulty: Hard

Question: What is a read-write (RW) conflict?

A) Two reads
B) A transaction writes data that has been read by another uncommitted transaction
C) Two writes
D) No conflict

✔ Correct Answer: B

Reason: An RW conflict (unrepeatable read) occurs when a transaction writes data that has been read by another transaction, causing inconsistent reads.

Tag: Past Paper

---

### Question 214
Domain: Databases
Topic: Concurrency Control
Subtopic: Conflict Serializability
Difficulty: Hard

Question: What is conflict serializability?

A) No conflicts exist
B) A schedule is conflict equivalent to some serial schedule
C) All transactions conflict
D) Conflicts are ignored

✔ Correct Answer: B

Reason: A schedule is conflict serializable if it is conflict equivalent to some serial schedule, meaning non-conflicting operations can be reordered to produce a serial schedule.

Tag: Past Paper

---

### Question 215
Domain: Databases
Topic: Concurrency Control
Subtopic: View Serializability
Difficulty: Hard

Question: What is view serializability?

A) Viewing serial schedules
B) A schedule produces the same final database state as some serial schedule
C) No serializability
D) Visual representation

✔ Correct Answer: B

Reason: A schedule is view serializable if it produces the same final database state and intermediate reads as some serial schedule.

Tag: Past Paper

---

### Question 216
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: What is the wait-die scheme for deadlock prevention?

A) All transactions wait
B) Older transactions wait, younger transactions are rolled back
C) Younger transactions wait, older are rolled back
D) No waiting allowed

✔ Correct Answer: B

Reason: In wait-die, if an older transaction requests a lock held by a younger transaction, it waits; if younger requests from older, it dies (rolls back).

Tag: Past Paper

---

### Question 217
Domain: Databases
Topic: Concurrency Control
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: What is the wound-wait scheme for deadlock prevention?

A) All transactions wait
B) Older transactions force younger to roll back, younger wait for older
C) Younger force older to roll back
D) No waiting allowed

✔ Correct Answer: B

Reason: In wound-wait, if an older transaction requests a lock held by a younger transaction, the younger is wounded (rolled back); if younger requests from older, it waits.

Tag: Past Paper

---

### Question 218
Domain: Databases
Topic: Recovery Management
Subtopic: Fuzzy Checkpoint
Difficulty: Hard

Question: What is a fuzzy checkpoint?

A) An unclear checkpoint
B) A checkpoint that allows transactions to continue during checkpointing
C) A failed checkpoint
D) A deleted checkpoint

✔ Correct Answer: B

Reason: A fuzzy checkpoint allows transactions to continue executing during the checkpointing process, reducing system downtime.

Tag: Normal

---

### Question 219
Domain: Databases
Topic: Recovery Management
Subtopic: Media Recovery
Difficulty: Medium

Question: What is media recovery?

A) Recovering from transaction failures
B) Recovering from disk failures using backups
C) Recovering from power failures
D) Recovering from network failures

✔ Correct Answer: B

Reason: Media recovery deals with recovering the database from disk or storage media failures using backups and logs.

Tag: Normal

---

### Question 220
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Heap File Organization
Difficulty: Easy

Question: What is heap file organization?

A) Files sorted by key
B) Records stored in no particular order
C) Files organized in a tree
D) Files organized by hash

✔ Correct Answer: B

Reason: In heap file organization, records are stored in no particular order, typically in the order they are inserted.

Tag: Normal

---

### Question 221
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Sequential File Organization
Difficulty: Easy

Question: What is sequential file organization?

A) Random order
B) Records stored in sorted order based on a key
C) No organization
D) Hash-based order

✔ Correct Answer: B

Reason: Sequential file organization stores records in sorted order based on a search key, enabling efficient sequential access.

Tag: Normal

---

### Question 222
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Hash File Organization
Difficulty: Medium

Question: What is hash file organization?

A) Random storage
B) Records stored in buckets determined by a hash function
C) Sorted storage
D) Tree-based storage

✔ Correct Answer: B

Reason: Hash file organization uses a hash function to compute the bucket address where a record should be stored.

Tag: Normal

---

### Question 223
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Pipeline Processing
Difficulty: Hard

Question: What is pipelining in query processing?

A) Using multiple processors
B) Passing results from one operation directly to the next without materialization
C) Storing intermediate results
D) Sequential processing

✔ Correct Answer: B

Reason: Pipelining passes tuples from one operation to the next without storing intermediate results, improving efficiency.

Tag: Normal

---

### Question 224
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Materialization
Difficulty: Medium

Question: What is materialization in query processing?

A) Creating views
B) Storing intermediate results of operations
C) Deleting results
D) Encrypting results

✔ Correct Answer: B

Reason: Materialization stores the complete intermediate results of an operation before passing them to the next operation.

Tag: Normal

---

### Question 225
Domain: Databases
Topic: Database Security
Subtopic: Database Firewall
Difficulty: Medium

Question: What is a database firewall?

A) A network firewall
B) A security layer that monitors and blocks unauthorized database access
C) A backup system
D) An encryption tool

✔ Correct Answer: B

Reason: A database firewall monitors database traffic and blocks unauthorized access attempts, SQL injection, and other threats.

Tag: Normal

---

### Question 226
Domain: Databases
Topic: Database Security
Subtopic: Database Activity Monitoring
Difficulty: Medium

Question: What is Database Activity Monitoring (DAM)?

A) Monitoring database size
B) Real-time monitoring and recording of database activities
C) Monitoring network traffic
D) Monitoring CPU usage

✔ Correct Answer: B

Reason: DAM continuously monitors and records database activities in real-time to detect suspicious behavior and ensure compliance.

Tag: Normal

---

### Question 227
Domain: Databases
Topic: Distributed Databases
Subtopic: Homogeneous vs Heterogeneous
Difficulty: Easy

Question: What is a homogeneous distributed database?

A) All sites use different DBMS
B) All sites use the same DBMS
C) Only one site exists
D) No DBMS is used

✔ Correct Answer: B

Reason: In a homogeneous distributed database, all sites use the same DBMS software, simplifying management and query processing.

Tag: Normal

---

### Question 228
Domain: Databases
Topic: Distributed Databases
Subtopic: Homogeneous vs Heterogeneous
Difficulty: Easy

Question: What is a heterogeneous distributed database?

A) All sites use the same DBMS
B) Different sites use different DBMS
C) Only one site exists
D) No distribution exists

✔ Correct Answer: B

Reason: In a heterogeneous distributed database, different sites may use different DBMS software, requiring additional integration efforts.

Tag: Normal

---

### Question 229
Domain: Databases
Topic: Distributed Databases
Subtopic: Distributed Join
Difficulty: Hard

Question: What is a semijoin in distributed databases?

A) A partial join
B) A technique to reduce data transfer by sending only relevant tuples
C) A failed join
D) A cross join

✔ Correct Answer: B

Reason: Semijoin reduces data transfer in distributed joins by first sending a projection to filter tuples before transferring the full relation.

Tag: Past Paper

---

### Question 230
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Models
Difficulty: Hard

Question: What is strong consistency?

A) Data is eventually consistent
B) All reads return the most recent write
C) Data may be inconsistent
D) No consistency guarantee

✔ Correct Answer: B

Reason: Strong consistency guarantees that all reads return the value of the most recent write, providing immediate consistency.

Tag: Normal

---

### Question 231
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Consistency Models
Difficulty: Medium

Question: What is weak consistency?

A) Immediate consistency
B) No guarantee that reads will return the most recent write
C) Strong consistency
D) Perfect consistency

✔ Correct Answer: B

Reason: Weak consistency provides no guarantee that subsequent reads will return the most recent write immediately.

Tag: Normal

---

### Question 232
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Redis
Difficulty: Easy

Question: What type of NoSQL database is Redis?

A) Document database
B) Key-value store
C) Column-family database
D) Graph database

✔ Correct Answer: B

Reason: Redis is an in-memory key-value store known for high performance and support for various data structures.

Tag: Normal

---

### Question 233
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Neo4j
Difficulty: Easy

Question: What type of NoSQL database is Neo4j?

A) Document database
B) Key-value store
C) Graph database
D) Column-family database

✔ Correct Answer: C

Reason: Neo4j is a graph database optimized for storing and querying graph structures with nodes and relationships.

Tag: Normal

---

### Question 234
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Slowly Changing Dimensions
Difficulty: Medium

Question: What are slowly changing dimensions (SCD)?

A) Dimensions that never change
B) Dimensions whose attributes change slowly over time
C) Fast-changing dimensions
D) Static dimensions

✔ Correct Answer: B

Reason: Slowly changing dimensions are dimension attributes that change slowly and unpredictably over time, requiring strategies to track changes.

Tag: Normal

---

### Question 235
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: SCD Types
Difficulty: Medium

Question: What is Type 1 SCD?

A) Keeps history
B) Overwrites old values with new values
C) Adds new rows
D) Creates new columns

✔ Correct Answer: B

Reason: Type 1 SCD simply overwrites old attribute values with new values, maintaining no history.

Tag: Normal

---

### Question 236
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: SCD Types
Difficulty: Medium

Question: What is Type 2 SCD?

A) Overwrites values
B) Adds new rows to track historical changes
C) Adds new columns
D) Deletes old values

✔ Correct Answer: B

Reason: Type 2 SCD adds new rows with new surrogate keys to track historical changes, maintaining full history.

Tag: Normal

---

### Question 237
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: INTERSECT Operator
Difficulty: Medium

Question: What does the INTERSECT operator do?

A) Combines all rows
B) Returns rows that appear in both result sets
C) Returns rows from the first set only
D) Deletes rows

✔ Correct Answer: B

Reason: INTERSECT returns only the rows that appear in both result sets, removing duplicates.

Tag: Normal

---

### Question 238
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: EXCEPT/MINUS Operator
Difficulty: Medium

Question: What does the EXCEPT (or MINUS) operator do?

A) Adds rows
B) Returns rows from the first set that are not in the second set
C) Returns all rows
D) Multiplies values

✔ Correct Answer: B

Reason: EXCEPT (MINUS in Oracle) returns rows from the first query that are not present in the second query.

Tag: Normal

---

### Question 239
Domain: Databases
Topic: Advanced SQL
Subtopic: User-Defined Functions
Difficulty: Medium

Question: What is a user-defined function (UDF)?

A) A built-in function
B) A custom function created by users to encapsulate logic
C) A system function
D) A deleted function

✔ Correct Answer: B

Reason: A UDF is a custom function created by users to encapsulate reusable logic that can be called in SQL statements.

Tag: Normal

---

### Question 240
Domain: Databases
Topic: Advanced SQL
Subtopic: Scalar vs Table-Valued Functions
Difficulty: Medium

Question: What does a scalar function return?

A) Multiple rows
B) A single value
C) A table
D) Nothing

✔ Correct Answer: B

Reason: A scalar function returns a single value (scalar value) and can be used wherever an expression is allowed.

Tag: Normal

---

### Question 241
Domain: Databases
Topic: Advanced SQL
Subtopic: Scalar vs Table-Valued Functions
Difficulty: Medium

Question: What does a table-valued function return?

A) A single value
B) A table (set of rows)
C) Nothing
D) An error

✔ Correct Answer: B

Reason: A table-valued function returns a table (set of rows) and can be used in the FROM clause like a regular table.

Tag: Normal

---

### Question 242
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Entity Integrity
Difficulty: Easy

Question: What does entity integrity ensure?

A) Foreign keys are valid
B) Primary key values are unique and not NULL
C) All data is encrypted
D) All tables have indexes

✔ Correct Answer: B

Reason: Entity integrity ensures that primary key values are unique and not NULL, guaranteeing each entity can be uniquely identified.

Tag: Past Paper

---

### Question 243
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Referential Integrity Actions
Difficulty: Medium

Question: What does CASCADE do in referential integrity?

A) Prevents deletion
B) Automatically propagates changes to related rows
C) Ignores changes
D) Locks tables

✔ Correct Answer: B

Reason: CASCADE automatically propagates DELETE or UPDATE operations to related rows in child tables, maintaining referential integrity.

Tag: Normal

---

### Question 244
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Referential Integrity Actions
Difficulty: Medium

Question: What does SET NULL do in referential integrity?

A) Deletes rows
B) Sets foreign key values to NULL when referenced row is deleted
C) Prevents deletion
D) Cascades changes

✔ Correct Answer: B

Reason: SET NULL sets foreign key values to NULL when the referenced row in the parent table is deleted or updated.

Tag: Normal

---

### Question 245
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Denormalization Trade-offs
Difficulty: Medium

Question: What is a disadvantage of denormalization?

A) Faster reads
B) Increased data redundancy and update anomalies
C) Simpler queries
D) Better performance

✔ Correct Answer: B

Reason: Denormalization increases data redundancy and can reintroduce update anomalies, trading off data integrity for read performance.

Tag: Normal

---

### Question 246
Domain: Databases
Topic: Transaction Management
Subtopic: Nested Transactions
Difficulty: Hard

Question: What are nested transactions?

A) Transactions in different databases
B) Transactions within transactions forming a hierarchy
C) Parallel transactions
D) Sequential transactions

✔ Correct Answer: B

Reason: Nested transactions allow transactions to be composed hierarchically, where a transaction can contain subtransactions.

Tag: Normal

---

### Question 247
Domain: Databases
Topic: Transaction Management
Subtopic: Distributed Transactions
Difficulty: Hard

Question: What is a distributed transaction?

A) A transaction on one site
B) A transaction that accesses data on multiple sites
C) A fast transaction
D) A local transaction

✔ Correct Answer: B

Reason: A distributed transaction accesses and updates data on multiple sites in a distributed database system.

Tag: Normal

---

### Question 248
Domain: Databases
Topic: Concurrency Control
Subtopic: Multiversion Concurrency Control
Difficulty: Hard

Question: What is multiversion concurrency control (MVCC)?

A) Using one version of data
B) Maintaining multiple versions of data to allow concurrent access
C) Deleting old versions
D) Locking all versions

✔ Correct Answer: B

Reason: MVCC maintains multiple versions of data items, allowing readers to access old versions while writers create new versions, reducing lock contention.

Tag: Past Paper

---

### Question 249
Domain: Databases
Topic: Concurrency Control
Subtopic: Snapshot Isolation
Difficulty: Hard

Question: What is snapshot isolation?

A) Taking database snapshots
B) Each transaction sees a consistent snapshot of the database
C) No isolation
D) Maximum isolation

✔ Correct Answer: B

Reason: Snapshot isolation provides each transaction with a consistent snapshot of the database as it existed at transaction start.

Tag: Normal

---

### Question 250
Domain: Databases
Topic: Recovery Management
Subtopic: Crash Recovery
Difficulty: Medium

Question: What is crash recovery?

A) Preventing crashes
B) Restoring the database to a consistent state after a system crash
C) Backing up data
D) Monitoring crashes

✔ Correct Answer: B

Reason: Crash recovery restores the database to a consistent state after a system failure using transaction logs.

Tag: Normal

---

### Question 251
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Clustered vs Non-Clustered
Difficulty: Medium

Question: How many clustered indexes can a table have?

A) Unlimited
B) Only one
C) Two
D) None

✔ Correct Answer: B

Reason: A table can have only one clustered index because it determines the physical order of data in the table.

Tag: Normal

---

### Question 252
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Index Selectivity
Difficulty: Medium

Question: What is index selectivity?

A) The size of the index
B) The ratio of distinct values to total rows
C) The speed of the index
D) The type of index

✔ Correct Answer: B

Reason: Index selectivity measures the ratio of distinct values to total rows; higher selectivity means more distinct values and better index effectiveness.

Tag: Normal

---

### Question 253
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Plan Cache
Difficulty: Medium

Question: What is a query plan cache?

A) A cache for data
B) A cache storing compiled query execution plans for reuse
C) A backup cache
D) A temporary cache

✔ Correct Answer: B

Reason: Query plan cache stores compiled execution plans, allowing reuse without recompilation, improving performance.

Tag: Normal

---

### Question 254
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Statistics
Difficulty: Medium

Question: Why are database statistics important for query optimization?

A) They are not important
B) They help estimate costs and choose optimal execution plans
C) They slow down queries
D) They delete data

✔ Correct Answer: B

Reason: Database statistics (like row counts, value distributions) help the optimizer estimate operation costs and choose optimal execution plans.

Tag: Normal

---

### Question 255
Domain: Databases
Topic: Database Security
Subtopic: Row-Level Security
Difficulty: Medium

Question: What is row-level security?

A) Encrypting rows
B) Restricting access to specific rows based on user attributes
C) Deleting rows
D) Indexing rows

✔ Correct Answer: B

Reason: Row-level security restricts which rows users can access based on their attributes or roles, providing fine-grained access control.

Tag: Normal

---

### Question 256
Domain: Databases
Topic: Database Security
Subtopic: Dynamic Data Masking
Difficulty: Medium

Question: What is dynamic data masking?

A) Static masking
B) Real-time masking of sensitive data based on user privileges
C) Permanent masking
D) No masking

✔ Correct Answer: B

Reason: Dynamic data masking masks sensitive data in real-time based on user privileges without changing the actual stored data.

Tag: Normal

---

### Question 257
Domain: Databases
Topic: Distributed Databases
Subtopic: Global Schema
Difficulty: Medium

Question: What is a global schema in distributed databases?

A) A local schema
B) A unified schema representing the entire distributed database
C) A temporary schema
D) A backup schema

✔ Correct Answer: B

Reason: A global schema provides a unified view of the entire distributed database, hiding the distribution from users.

Tag: Normal

---

### Question 258
Domain: Databases
Topic: Distributed Databases
Subtopic: Local Schema
Difficulty: Easy

Question: What is a local schema in distributed databases?

A) The global view
B) The schema at a specific site
C) A temporary schema
D) A deleted schema

✔ Correct Answer: B

Reason: A local schema describes the database structure at a specific site in a distributed database system.

Tag: Normal

---

### Question 259
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Horizontal Scaling
Difficulty: Easy

Question: What is horizontal scaling (scale-out)?

A) Adding more powerful hardware to a single server
B) Adding more servers to distribute the load
C) Reducing servers
D) Vertical scaling

✔ Correct Answer: B

Reason: Horizontal scaling adds more servers to distribute the load, a key advantage of many NoSQL databases.

Tag: Normal

---

### Question 260
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Vertical Scaling
Difficulty: Easy

Question: What is vertical scaling (scale-up)?

A) Adding more servers
B) Adding more resources (CPU, RAM) to a single server
C) Removing servers
D) Horizontal scaling

✔ Correct Answer: B

Reason: Vertical scaling increases the capacity of a single server by adding more CPU, RAM, or storage.

Tag: Normal

---

### Question 261
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Conformed Dimensions
Difficulty: Medium

Question: What are conformed dimensions?

A) Dimensions unique to one fact table
B) Dimensions shared across multiple fact tables with consistent meaning
C) Temporary dimensions
D) Deleted dimensions

✔ Correct Answer: B

Reason: Conformed dimensions are shared across multiple fact tables with consistent structure and meaning, enabling cross-fact analysis.

Tag: Normal

---

### Question 262
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Aggregate Tables
Difficulty: Medium

Question: What are aggregate tables in data warehousing?

A) Tables with raw data
B) Pre-computed summary tables to improve query performance
C) Temporary tables
D) Backup tables

✔ Correct Answer: B

Reason: Aggregate tables store pre-computed summaries of data to improve query performance for common aggregation queries.

Tag: Normal

---

### Question 263
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: CAST Function
Difficulty: Easy

Question: What does the CAST function do?

A) Deletes data
B) Converts a value from one data type to another
C) Sorts data
D) Filters data

✔ Correct Answer: B

Reason: CAST explicitly converts a value from one data type to another (e.g., string to integer).

Tag: Normal

---

### Question 264
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: CONVERT Function
Difficulty: Easy

Question: What is the difference between CAST and CONVERT?

A) No difference
B) CONVERT offers more formatting options (database-specific)
C) CAST is faster
D) CONVERT is deprecated

✔ Correct Answer: B

Reason: While both convert data types, CONVERT (in some databases) offers additional formatting options, particularly for dates.

Tag: Normal

---

### Question 265
Domain: Databases
Topic: Advanced SQL
Subtopic: LEAD Function
Difficulty: Hard

Question: What does the LEAD window function do?

A) Returns the previous row's value
B) Returns the next row's value within a partition
C) Returns the first row's value
D) Returns the last row's value

✔ Correct Answer: B

Reason: LEAD accesses data from a subsequent row in the same result set without using a self-join.

Tag: Normal

---

### Question 266
Domain: Databases
Topic: Advanced SQL
Subtopic: LAG Function
Difficulty: Hard

Question: What does the LAG window function do?

A) Returns the next row's value
B) Returns the previous row's value within a partition
C) Returns the first row's value
D) Returns the last row's value

✔ Correct Answer: B

Reason: LAG accesses data from a previous row in the same result set without using a self-join.

Tag: Normal

---

### Question 267
Domain: Databases
Topic: Advanced SQL
Subtopic: FIRST_VALUE Function
Difficulty: Hard

Question: What does the FIRST_VALUE window function do?

A) Returns the last value
B) Returns the first value in an ordered partition
C) Returns the middle value
D) Returns a random value

✔ Correct Answer: B

Reason: FIRST_VALUE returns the first value in an ordered partition of a result set.

Tag: Normal

---

### Question 268
Domain: Databases
Topic: Advanced SQL
Subtopic: LAST_VALUE Function
Difficulty: Hard

Question: What does the LAST_VALUE window function do?

A) Returns the first value
B) Returns the last value in an ordered partition
C) Returns the middle value
D) Returns a random value

✔ Correct Answer: B

Reason: LAST_VALUE returns the last value in an ordered partition of a result set.

Tag: Normal

---

### Question 269
Domain: Databases
Topic: Relational Database Concepts
Subtopic: Atomicity of Attributes
Difficulty: Easy

Question: What does it mean for an attribute to be atomic?

A) It's very small
B) It contains indivisible values (no composite or multi-valued attributes)
C) It's encrypted
D) It's indexed

✔ Correct Answer: B

Reason: An atomic attribute contains indivisible values - it cannot be decomposed into smaller meaningful components.

Tag: Past Paper

---

### Question 270
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Trivial Functional Dependency
Difficulty: Hard

Question: What is a trivial functional dependency?

A) An important dependency
B) A dependency where the right side is a subset of the left side
C) A complex dependency
D) A deleted dependency

✔ Correct Answer: B

Reason: A trivial functional dependency has the right side as a subset of the left side (e.g., AB → A), always satisfied.

Tag: Past Paper

---

### Question 271
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Non-Trivial Functional Dependency
Difficulty: Medium

Question: What is a non-trivial functional dependency?

A) A simple dependency
B) A dependency where the right side is not a subset of the left side
C) A deleted dependency
D) An encrypted dependency

✔ Correct Answer: B

Reason: A non-trivial functional dependency has the right side not being a subset of the left side, providing meaningful information.

Tag: Past Paper

---

### Question 272
Domain: Databases
Topic: Transaction Management
Subtopic: Compensating Transactions
Difficulty: Hard

Question: What is a compensating transaction?

A) A fast transaction
B) A transaction that undoes the effects of a committed transaction
C) A parallel transaction
D) A deleted transaction

✔ Correct Answer: B

Reason: A compensating transaction logically undoes the effects of a previously committed transaction when rollback is not possible.

Tag: Normal

---

### Question 273
Domain: Databases
Topic: Transaction Management
Subtopic: Long-Running Transactions
Difficulty: Medium

Question: What challenge do long-running transactions pose?

A) They are too fast
B) They hold locks for extended periods, reducing concurrency
C) They use no resources
D) They never complete

✔ Correct Answer: B

Reason: Long-running transactions hold locks for extended periods, potentially blocking other transactions and reducing system concurrency.

Tag: Normal

---

### Question 274
Domain: Databases
Topic: Concurrency Control
Subtopic: Granularity of Locking
Difficulty: Medium

Question: What is fine-grained locking?

A) Locking large data items
B) Locking small data items like individual records
C) No locking
D) Locking the entire database

✔ Correct Answer: B

Reason: Fine-grained locking locks small data items (like individual records), allowing higher concurrency but with more overhead.

Tag: Normal

---

### Question 275
Domain: Databases
Topic: Concurrency Control
Subtopic: Granularity of Locking
Difficulty: Medium

Question: What is coarse-grained locking?

A) Locking small items
B) Locking large data items like entire tables
C) No locking
D) Locking individual fields

✔ Correct Answer: B

Reason: Coarse-grained locking locks large data items (like entire tables), reducing overhead but potentially reducing concurrency.

Tag: Normal

---

### Question 276
Domain: Databases
Topic: Recovery Management
Subtopic: Point-in-Time Recovery
Difficulty: Medium

Question: What is point-in-time recovery?

A) Recovering to the current time
B) Recovering the database to a specific moment in the past
C) Deleting recovery points
D) No recovery

✔ Correct Answer: B

Reason: Point-in-time recovery restores the database to a specific moment in the past using backups and transaction logs.

Tag: Normal

---

### Question 277
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Full-Text Index
Difficulty: Medium

Question: What is a full-text index used for?

A) Numeric searches
B) Searching text within documents or large text fields
C) Date searches
D) Foreign key searches

✔ Correct Answer: B

Reason: Full-text indexes enable efficient searching of words and phrases within large text fields or documents.

Tag: Normal

---

### Question 278
Domain: Databases
Topic: Indexing & File Organization
Subtopic: Spatial Index
Difficulty: Medium

Question: What is a spatial index used for?

A) Text searches
B) Geometric and geographic data queries
C) Numeric searches
D) Date searches

✔ Correct Answer: B

Reason: Spatial indexes optimize queries on geometric and geographic data, like finding nearby locations.

Tag: Normal

---

### Question 279
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Index Scan vs Table Scan
Difficulty: Medium

Question: When is a table scan more efficient than an index scan?

A) Never
B) When retrieving a large percentage of rows
C) Always
D) When the table is empty

✔ Correct Answer: B

Reason: A table scan can be more efficient when retrieving a large percentage of rows, as index overhead may exceed the benefit.

Tag: Normal

---

### Question 280
Domain: Databases
Topic: Query Processing & Optimization
Subtopic: Query Hints
Difficulty: Medium

Question: What are query hints?

A) Suggestions for users
B) Directives to influence the optimizer's execution plan choice
C) Error messages
D) Backup instructions

✔ Correct Answer: B

Reason: Query hints are directives that influence or override the query optimizer's execution plan choices.

Tag: Normal

---

### Question 281
Domain: Databases
Topic: Database Security
Subtopic: SQL Injection Prevention
Difficulty: Medium

Question: Which technique best prevents SQL injection?

A) Input validation only
B) Parameterized queries (prepared statements)
C) Longer passwords
D) Encryption

✔ Correct Answer: B

Reason: Parameterized queries (prepared statements) separate SQL code from data, effectively preventing SQL injection attacks.

Tag: Past Paper

---

### Question 282
Domain: Databases
Topic: Database Security
Subtopic: Stored Procedure Security
Difficulty: Medium

Question: How can stored procedures enhance security?

A) They cannot enhance security
B) By encapsulating logic and controlling data access
C) By slowing down queries
D) By deleting data

✔ Correct Answer: B

Reason: Stored procedures encapsulate business logic and can control data access, reducing direct table access and SQL injection risks.

Tag: Normal

---

### Question 283
Domain: Databases
Topic: Distributed Databases
Subtopic: Data Allocation
Difficulty: Medium

Question: What is data allocation in distributed databases?

A) Deleting data
B) Deciding where to store data fragments across sites
C) Encrypting data
D) Backing up data

✔ Correct Answer: B

Reason: Data allocation determines where to store data fragments across different sites to optimize performance and availability.

Tag: Normal

---

### Question 284
Domain: Databases
Topic: Distributed Databases
Subtopic: Location Transparency
Difficulty: Medium

Question: What is location transparency?

A) Visible data locations
B) Users can access data without knowing its physical location
C) No data locations
D) Encrypted locations

✔ Correct Answer: B

Reason: Location transparency allows users to access data without needing to know where it is physically stored in the distributed system.

Tag: Normal

---

### Question 285
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Schema-less Design
Difficulty: Easy

Question: What does schema-less (or schema-flexible) mean in NoSQL?

A) No data structure
B) Data can be stored without a predefined schema
C) Strict schema required
D) No data allowed

✔ Correct Answer: B

Reason: Schema-less (or schema-flexible) allows storing data without a predefined schema, enabling flexible and evolving data structures.

Tag: Normal

---

### Question 286
Domain: Databases
Topic: NoSQL & Modern Databases
Subtopic: Denormalization in NoSQL
Difficulty: Medium

Question: Why is denormalization common in NoSQL databases?

A) To increase complexity
B) To optimize read performance and reduce joins
C) To increase storage costs
D) To slow down queries

✔ Correct Answer: B

Reason: NoSQL databases often denormalize data to optimize read performance and avoid expensive join operations.

Tag: Normal

---

### Question 287
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Data Cube
Difficulty: Medium

Question: What is a data cube in OLAP?

A) A physical cube
B) A multi-dimensional representation of data for analysis
C) A backup cube
D) A deleted cube

✔ Correct Answer: B

Reason: A data cube is a multi-dimensional representation of data that enables analysis across multiple dimensions.

Tag: Normal

---

### Question 288
Domain: Databases
Topic: Data Warehousing & Data Mining
Subtopic: Pivot Operation
Difficulty: Medium

Question: What is a pivot operation in OLAP?

A) Deleting dimensions
B) Rotating the data cube to view different perspectives
C) Backing up data
D) Encrypting data

✔ Correct Answer: B

Reason: Pivot (or rotate) changes the dimensional orientation of the data cube, providing different perspectives on the data.

Tag: Normal

---

### Question 289
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Subquery Types
Difficulty: Medium

Question: What is a scalar subquery?

A) A subquery returning multiple rows
B) A subquery returning a single value
C) A subquery returning a table
D) A subquery returning nothing

✔ Correct Answer: B

Reason: A scalar subquery returns a single value (one row, one column) and can be used where a single value is expected.

Tag: Normal

---

### Question 290
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Subquery Types
Difficulty: Medium

Question: What is a row subquery?

A) A subquery returning one column
B) A subquery returning a single row with multiple columns
C) A subquery returning multiple rows
D) A subquery returning nothing

✔ Correct Answer: B

Reason: A row subquery returns a single row with one or more columns, used for row comparisons.

Tag: Normal

---

### Question 291
Domain: Databases
Topic: Structured Query Language (SQL)
Subtopic: Subquery Types
Difficulty: Medium

Question: What is a table subquery?

A) A subquery returning one value
B) A subquery returning multiple rows and columns
C) A subquery returning nothing
D) A subquery returning one row

✔ Correct Answer: B

Reason: A table subquery returns multiple rows and columns, essentially a table, often used with IN, EXISTS, or in FROM clause.

Tag: Normal

---

### Question 292
Domain: Databases
Topic: Advanced SQL
Subtopic: NTILE Function
Difficulty: Hard

Question: What does the NTILE window function do?

A) Returns tile numbers
B) Divides rows into a specified number of groups and assigns group numbers
C) Deletes rows
D) Sorts rows

✔ Correct Answer: B

Reason: NTILE divides an ordered partition into a specified number of groups (tiles) and assigns each row a group number.

Tag: Normal

---

### Question 293
Domain: Databases
Topic: Advanced SQL
Subtopic: PERCENT_RANK Function
Difficulty: Hard

Question: What does the PERCENT_RANK function calculate?

A) Percentage of NULL values
B) The relative rank of a row as a percentage
C) Percentage of total rows
D) Percentage of duplicates

✔ Correct Answer: B

Reason: PERCENT_RANK calculates the relative rank of a row within a partition as a percentage (0 to 1).

Tag: Normal

---

### Question 294
Domain: Databases
Topic: Relational Algebra & Calculus
Subtopic: Rename Operation
Difficulty: Easy

Question: What does the rename operation (ρ) do in relational algebra?

A) Deletes relations
B) Renames relations or attributes
C) Sorts relations
D) Joins relations

✔ Correct Answer: B

Reason: The rename operation (ρ) changes the name of a relation or its attributes, useful for avoiding name conflicts.

Tag: Past Paper

---

### Question 295
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Multivalued Dependency
Difficulty: Hard

Question: What is a multivalued dependency?

A) A functional dependency
B) A dependency where one attribute determines a set of values for another attribute
C) A transitive dependency
D) A partial dependency

✔ Correct Answer: B

Reason: A multivalued dependency exists when one attribute determines a set of values for another attribute, independent of other attributes.

Tag: Past Paper

---

### Question 296
Domain: Databases
Topic: Database Design & Normalization
Subtopic: Join Dependency
Difficulty: Hard

Question: What is a join dependency?

A) A functional dependency
B) A constraint where a relation can be losslessly decomposed into multiple relations
C) A foreign key
D) A primary key

✔ Correct Answer: B

Reason: A join dependency specifies that a relation can be losslessly decomposed into multiple relations and reconstructed by joining them.

Tag: Past Paper

---

### Question 297
Domain: Databases
Topic: Transaction Management
Subtopic: Phantom Problem
Difficulty: Hard

Question: What causes the phantom problem in transactions?

A) Deleted rows
B) New rows inserted by other transactions affecting query results
C) Updated rows
D) Locked rows

✔ Correct Answer: B

Reason: The phantom problem occurs when new rows inserted by other transactions appear in subsequent reads, affecting query results.

Tag: Past Paper

---

### Question 298
Domain: Databases
Topic: Concurrency Control
Subtopic: Validation-Based Protocol
Difficulty: Hard

Question: What are the three phases in validation-based (optimistic) concurrency control?

A) Lock, Execute, Unlock
B) Read, Validation, Write
C) Begin, Execute, Commit
D) Start, Process, End

✔ Correct Answer: B

Reason: Validation-based protocol has three phases: Read (execute without locks), Validation (check for conflicts), Write (commit if valid).

Tag: Past Paper

---

### Question 299
Domain: Databases
Topic: Recovery Management
Subtopic: Steal/No-Steal Policy
Difficulty: Hard

Question: What is a steal policy in buffer management?

A) Never write uncommitted data to disk
B) Allow writing uncommitted data to disk
C) Always steal data
D) Never use buffers

✔ Correct Answer: B

Reason: A steal policy allows the buffer manager to write uncommitted (dirty) pages to disk before transaction commit, requiring undo capability.

Tag: Past Paper

---

### Question 300
Domain: Databases
Topic: Recovery Management
Subtopic: Force/No-Force Policy
Difficulty: Hard

Question: What is a force policy in buffer management?

A) Never force writes
B) Force all modified pages to disk at commit time
C) Random writes
D) Delayed writes

✔ Correct Answer: B

Reason: A force policy requires all pages modified by a transaction to be written to disk before the transaction commits, eliminating need for redo.

Tag: Past Paper

---

**End of Batch 03**

---

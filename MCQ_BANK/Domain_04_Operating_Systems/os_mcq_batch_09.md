# Operating Systems - MCQ Batch 09
## Questions 801-900

---

### Question 801
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Operating System Evolution
Difficulty: Hard

Question: What innovation did third-generation operating systems introduce?
A) Batch processing
B) Multiprogramming and time-sharing
C) GUI
D) Mobile support

✔ Correct Answer: B

Reason: Third-generation OS (1960s-1980s) introduced multiprogramming, time-sharing, and interactive computing with terminals.

Tag: Normal

---

### Question 802
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Operating System Evolution
Difficulty: Hard

Question: What characterizes fourth-generation operating systems?
A) Command-line only
B) Personal computers, GUIs, networking
C) Mainframes only
D) No networking

✔ Correct Answer: B

Reason: Fourth-generation (1980s-present) brought personal computers, graphical interfaces, networking, and distributed systems.

Tag: Normal

---

### Question 803
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Calls vs Library Functions
Difficulty: Medium

Question: How do library functions differ from system calls?
A) No difference
B) Library functions may or may not invoke system calls
C) Library functions are slower
D) System calls are user-level

✔ Correct Answer: B

Reason: Library functions are user-level code that may wrap system calls (printf uses write) or perform purely user-level operations.

Tag: Normal

---

### Question 804
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Kernel Space vs User Space
Difficulty: Easy

Question: What is kernel space?
A) User memory
B) Protected memory region for kernel code and data
C) Disk space
D) Swap space

✔ Correct Answer: B

Reason: Kernel space is protected memory region where kernel code executes with full hardware access.

Tag: Normal

---

### Question 805
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Kernel Space vs User Space
Difficulty: Easy

Question: What is user space?
A) Kernel memory
B) Memory region where user applications execute
C) Disk space
D) Protected space

✔ Correct Answer: B

Reason: User space is memory region where user applications run with restricted privileges, isolated from kernel.

Tag: Normal

---

### Question 806
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Unikernel
Difficulty: Hard

Question: What is a unikernel?
A) Standard kernel
B) Specialized single-address-space machine image
C) Microkernel
D) Monolithic kernel

✔ Correct Answer: B

Reason: Unikernel compiles application and minimal OS into single-address-space image, eliminating user/kernel separation for efficiency.

Tag: Normal

---

### Question 807
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Library OS
Difficulty: Hard

Question: What is a library operating system?
A) Standard OS
B) OS functionality as libraries linked with application
C) No OS
D) Distributed OS

✔ Correct Answer: B

Reason: Library OS provides OS services as libraries linked into application, enabling customization and efficiency.

Tag: Normal

---

### Question 808
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Call Overhead
Difficulty: Hard

Question: What contributes most to system call overhead?
A) Parameter passing
B) Mode switch and TLB flush
C) Function call
D) Return value

✔ Correct Answer: B

Reason: Mode switch between user and kernel and potential TLB flush contribute most to system call overhead.

Tag: Normal

---

### Question 809
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Lifecycle
Difficulty: Medium

Question: What is the typical process lifecycle?
A) Random states
B) New → Ready → Running → Waiting/Ready → Terminated
C) Single state
D) No lifecycle

✔ Correct Answer: B

Reason: Process lifecycle: created (new), loaded (ready), executing (running), blocked (waiting), completed (terminated).

Tag: Past Paper

---

### Question 810
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Synchronization
Difficulty: Medium

Question: Why do processes need synchronization?
A) No need
B) Coordinate access to shared resources
C) Slow down execution
D) Increase complexity

✔ Correct Answer: B

Reason: Processes sharing resources need synchronization to prevent race conditions and ensure data consistency.

Tag: Normal

---

### Question 811
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Communication Patterns
Difficulty: Hard

Question: What is producer-consumer pattern?
A) Random communication
B) One produces data, another consumes it
C) No communication
D) Bidirectional equal

✔ Correct Answer: B

Reason: Producer-consumer pattern has producer generating data and consumer processing it, requiring synchronization for buffer access.

Tag: Normal

---

### Question 812
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Communication Patterns
Difficulty: Hard

Question: What is client-server pattern?
A) Peer-to-peer
B) Client requests services from server
C) No communication
D) Broadcast

✔ Correct Answer: B

Reason: Client-server pattern has clients requesting services from server, which processes requests and returns responses.

Tag: Normal

---

### Question 813
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Overhead
Difficulty: Medium

Question: What is scheduling overhead?
A) No overhead
B) Time spent selecting next process to run
C) Execution time
D) Waiting time

✔ Correct Answer: B

Reason: Scheduling overhead is time spent by scheduler selecting next process, including context switch time.

Tag: Normal

---

### Question 814
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Fairness
Difficulty: Medium

Question: What is fair scheduling?
A) Random allocation
B) Equal CPU time or proportional to priority
C) First come only
D) No fairness

✔ Correct Answer: B

Reason: Fair scheduling ensures processes receive equal CPU time or time proportional to priority/shares.

Tag: Normal

---

### Question 815
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Work-Conserving Scheduler
Difficulty: Hard

Question: What is a work-conserving scheduler?
A) Wastes CPU
B) Never leaves CPU idle if runnable processes exist
C) Allows idle CPU
D) No scheduling

✔ Correct Answer: B

Reason: Work-conserving scheduler never idles CPU when runnable processes exist, maximizing utilization.

Tag: Normal

---

### Question 816
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Proportional Share Scheduling
Difficulty: Hard

Question: How does stride scheduling work?
A) Random selection
B) Each process has stride, select minimum pass value
C) FCFS
D) Priority only

✔ Correct Answer: B

Reason: Stride scheduling assigns stride (inversely proportional to tickets), selects process with minimum pass value, increments by stride.

Tag: Normal

---

### Question 817
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multiprocessor Scheduling
Difficulty: Hard

Question: What is cache affinity in scheduling?
A) No affinity
B) Preference to schedule process on CPU with warm cache
C) Random CPU
D) Always different CPU

✔ Correct Answer: B

Reason: Cache affinity prefers scheduling process on CPU where it recently ran, benefiting from cached data.

Tag: Normal

---

### Question 818
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multiprocessor Scheduling
Difficulty: Hard

Question: What is work stealing in multiprocessor scheduling?
A) No stealing
B) Idle CPU takes work from busy CPU's queue
C) Fixed assignment
D) No load balancing

✔ Correct Answer: B

Reason: Work stealing allows idle CPU to steal tasks from busy CPU's run queue, improving load balance.

Tag: Normal

---

### Question 819
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Overhead
Difficulty: Medium

Question: Why are threads lighter than processes?
A) No difference
B) Share address space, less context to switch
C) Threads are heavier
D) Same overhead

✔ Correct Answer: B

Reason: Threads share address space and resources, requiring less memory and faster context switches than processes.

Tag: Normal

---

### Question 820
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Coordination
Difficulty: Medium

Question: What mechanisms coordinate threads?
A) No coordination
B) Mutexes, semaphores, condition variables, barriers
C) Only mutexes
D) No mechanisms

✔ Correct Answer: B

Reason: Thread coordination uses mutexes (mutual exclusion), semaphores (counting), condition variables (waiting), barriers (synchronization points).

Tag: Normal

---

### Question 821
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Pooling Benefits
Difficulty: Medium

Question: What are benefits of thread pools?
A) No benefits
B) Reduced creation overhead, resource control, better performance
C) Slower execution
D) More complexity only

✔ Correct Answer: B

Reason: Thread pools reduce thread creation/destruction overhead, limit concurrent threads, and improve response time.

Tag: Normal

---

### Question 822
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Pool Sizing
Difficulty: Hard

Question: How should thread pool size be determined?
A) Always maximum
B) Based on workload type, CPU cores, I/O wait time
C) Always minimum
D) Random size

✔ Correct Answer: B

Reason: Pool size depends on CPU-bound (≈cores) vs I/O-bound (more threads), balancing concurrency and overhead.

Tag: Normal

---

### Question 823
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Synchronization Primitives Performance
Difficulty: Hard

Question: Which synchronization primitive is fastest?
A) Semaphore
B) Atomic operations
C) Mutex
D) Monitor

✔ Correct Answer: B

Reason: Atomic operations using hardware support are fastest, avoiding kernel involvement and context switches.

Tag: Normal

---

### Question 824
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Deadlock vs Livelock vs Starvation
Difficulty: Medium

Question: What distinguishes deadlock, livelock, and starvation?
A) All same
B) Deadlock blocked, livelock active no progress, starvation indefinitely waiting
C) No difference
D) Random states

✔ Correct Answer: B

Reason: Deadlock: processes blocked; livelock: processes active but not progressing; starvation: process indefinitely denied resources.

Tag: Past Paper

---

### Question 825
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Lock Ordering
Difficulty: Hard

Question: How does lock ordering prevent deadlock?
A) Cannot prevent
B) All threads acquire locks in same order
C) Random order
D) No ordering

✔ Correct Answer: B

Reason: Consistent lock ordering prevents circular wait by ensuring all threads acquire locks in same global order.

Tag: Normal

---

### Question 826
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Try-Lock Pattern
Difficulty: Hard

Question: What is the try-lock pattern?
A) Always block
B) Attempt lock, back off if unavailable
C) Never lock
D) Force lock

✔ Correct Answer: B

Reason: Try-lock attempts to acquire lock without blocking; if unavailable, releases held locks and retries, avoiding deadlock.

Tag: Normal

---

### Question 827
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Double-Checked Locking
Difficulty: Hard

Question: What is double-checked locking?
A) Single check
B) Check condition before and after acquiring lock
C) No checking
D) Triple check

✔ Correct Answer: B

Reason: Double-checked locking checks condition before locking (fast path) and after locking (safety), reducing lock contention.

Tag: Normal

---

### Question 828
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Probability
Difficulty: Hard

Question: What factors increase deadlock probability?
A) Fewer resources
B) More processes, more resources per process, longer hold times
C) Fewer processes
D) No factors

✔ Correct Answer: B

Reason: Deadlock probability increases with more processes, more resources needed per process, and longer resource hold times.

Tag: Normal

---

### Question 829
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Cost
Difficulty: Hard

Question: What is the cost of deadlock prevention?
A) No cost
B) Reduced concurrency and resource utilization
C) Better performance
D) No impact

✔ Correct Answer: B

Reason: Deadlock prevention restricts resource usage patterns, reducing concurrency and potentially wasting resources.

Tag: Normal

---

### Question 830
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Hierarchy Performance
Difficulty: Medium

Question: Why is memory hierarchy important?
A) Not important
B) Balance speed, capacity, and cost
C) Single level better
D) No reason

✔ Correct Answer: B

Reason: Memory hierarchy balances fast expensive memory (cache) with slow cheap memory (disk), optimizing cost-performance.

Tag: Normal

---

### Question 831
Domain: Operating Systems
Topic: Memory Management
Subtopic: Cache Coherence
Difficulty: Hard

Question: What is cache coherence?
A) No coherence
B) Ensuring consistent view of memory across caches
C) Single cache
D) Random values

✔ Correct Answer: B

Reason: Cache coherence ensures all CPUs see consistent memory values when multiple caches hold copies of same location.

Tag: Normal

---

### Question 832
Domain: Operating Systems
Topic: Memory Management
Subtopic: Cache Coherence Protocols
Difficulty: Hard

Question: What is MESI protocol?
A) No protocol
B) Cache coherence protocol with Modified, Exclusive, Shared, Invalid states
C) Memory protocol
D) Network protocol

✔ Correct Answer: B

Reason: MESI is cache coherence protocol tracking cache line states: Modified (dirty), Exclusive (clean, only copy), Shared, Invalid.

Tag: Normal

---

### Question 833
Domain: Operating Systems
Topic: Memory Management
Subtopic: False Sharing
Difficulty: Hard

Question: What is false sharing?
A) Real sharing
B) Different variables on same cache line causing coherence traffic
C) No sharing
D) True sharing

✔ Correct Answer: B

Reason: False sharing occurs when threads access different variables on same cache line, causing unnecessary coherence traffic.

Tag: Normal

---

### Question 834
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Ordering
Difficulty: Hard

Question: What is memory ordering?
A) Random order
B) Order in which memory operations become visible
C) No order
D) Sequential only

✔ Correct Answer: B

Reason: Memory ordering defines order in which memory operations from different threads become visible, affecting concurrent correctness.

Tag: Normal

---

### Question 835
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Models
Difficulty: Hard

Question: What is sequential consistency?
A) No consistency
B) Operations appear in program order, interleaved arbitrarily
C) Random order
D) No order

✔ Correct Answer: B

Reason: Sequential consistency ensures operations from each thread appear in program order, with arbitrary interleaving between threads.

Tag: Normal

---

### Question 836
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Models
Difficulty: Hard

Question: What is relaxed memory ordering?
A) Strict ordering
B) Allows reordering for performance, requires explicit synchronization
C) Sequential only
D) No reordering

✔ Correct Answer: B

Reason: Relaxed memory models allow CPU/compiler to reorder operations for performance, requiring explicit barriers for synchronization.

Tag: Normal

---

### Question 837
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Replacement Performance
Difficulty: Hard

Question: What affects page replacement algorithm performance?
A) Only algorithm choice
B) Algorithm, working set size, memory size, access pattern
C) Only memory size
D) No factors

✔ Correct Answer: B

Reason: Performance depends on algorithm choice, process working set size, available memory, and memory access patterns.

Tag: Normal

---

### Question 838
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault Handling Cost
Difficulty: Hard

Question: What makes page faults expensive?
A) Not expensive
B) Disk I/O, context switch, TLB flush
C) Fast operation
D) No cost

✔ Correct Answer: B

Reason: Page faults require slow disk I/O (milliseconds), context switch to another process, and TLB flush.

Tag: Normal

---

### Question 839
Domain: Operating Systems
Topic: Memory Management
Subtopic: Swap Space Management
Difficulty: Medium

Question: Where should swap space be located?
A) Random location
B) Fast disk or SSD for better performance
C) Slow disk
D) Network

✔ Correct Answer: B

Reason: Swap space on fast disk or SSD reduces paging overhead, improving system performance under memory pressure.

Tag: Normal

---

### Question 840
Domain: Operating Systems
Topic: Memory Management
Subtopic: Swappiness
Difficulty: Hard

Question: What is swappiness in Linux?
A) No swapping
B) Kernel parameter controlling swap vs cache preference
C) Swap size
D) Swap speed

✔ Correct Answer: B

Reason: Swappiness (0-100) controls kernel's tendency to swap vs reclaim page cache; higher values prefer swapping.

Tag: Normal

---

### Question 841
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Layers
Difficulty: Medium

Question: What does the logical file system layer handle?
A) Physical blocks
B) File metadata, directory structure, protection
C) Device drivers
D) Hardware

✔ Correct Answer: B

Reason: Logical file system manages file metadata (inodes), directory structure, access control, and symbolic names.

Tag: Normal

---

### Question 842
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Layers
Difficulty: Medium

Question: What does the file organization layer handle?
A) Metadata only
B) Mapping logical blocks to physical blocks
C) User interface
D) Network

✔ Correct Answer: B

Reason: File organization layer translates logical block numbers to physical block addresses, managing free space.

Tag: Normal

---

### Question 843
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Performance
Difficulty: Hard

Question: What is the elevator seeking problem?
A) No problem
B) Disk head repeatedly passing over needed blocks
C) Fast seeking
D) No seeking

✔ Correct Answer: B

Reason: Elevator seeking occurs when disk head repeatedly passes over needed blocks while servicing other requests.

Tag: Normal

---

### Question 844
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Optimization
Difficulty: Hard

Question: What is block clustering?
A) Single blocks
B) Allocating multiple contiguous blocks together
C) Random blocks
D) No clustering

✔ Correct Answer: B

Reason: Block clustering allocates multiple contiguous blocks as unit, reducing fragmentation and improving sequential access.

Tag: Normal

---

### Question 845
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Optimization
Difficulty: Hard

Question: What is cylinder group optimization?
A) Random placement
B) Grouping related data in same cylinder group
C) No grouping
D) Single cylinder

✔ Correct Answer: B

Reason: Cylinder group optimization places related data (directory, files) in same cylinder group, reducing seek time.

Tag: Normal

---

### Question 846
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Metadata
Difficulty: Medium

Question: What is the difference between hard and soft links?
A) No difference
B) Hard links share inode, soft links are separate files with path
C) Soft links faster
D) Hard links slower

✔ Correct Answer: B

Reason: Hard links are directory entries sharing same inode; soft links are separate files containing pathname to target.

Tag: Past Paper

---

### Question 847
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Recovery
Difficulty: Hard

Question: What is fsck?
A) File system creator
B) File system consistency checker and repair tool
C) File system copier
D) No function

✔ Correct Answer: B

Reason: fsck (file system check) verifies and repairs file system inconsistencies after crashes or improper shutdowns.

Tag: Normal

---

### Question 848
Domain: Operating Systems
Topic: File System Management
Subtopic: Journaling Types
Difficulty: Hard

Question: What is metadata journaling?
A) Data journaling
B) Journaling only metadata changes
C) No journaling
D) Full journaling

✔ Correct Answer: B

Reason: Metadata journaling logs only metadata changes (not file data), faster than full journaling with good consistency.

Tag: Normal

---

### Question 849
Domain: Operating Systems
Topic: File System Management
Subtopic: Journaling Types
Difficulty: Hard

Question: What is full data journaling?
A) Metadata only
B) Journaling both metadata and file data
C) No journaling
D) Partial journaling

✔ Correct Answer: B

Reason: Full data journaling logs both metadata and file data changes, slowest but provides strongest consistency guarantees.

Tag: Normal

---

### Question 850
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Scheduling Fairness
Difficulty: Medium

Question: Which disk scheduling algorithm is most fair?
A) SSTF
B) FCFS
C) SCAN
D) Random

✔ Correct Answer: B

Reason: FCFS provides perfect fairness by serving requests in arrival order, though not optimal for performance.

Tag: Normal

---

### Question 851
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Performance Optimization
Difficulty: Hard

Question: What is disk striping?
A) Single disk
B) Distributing data across multiple disks
C) No distribution
D) Backup only

✔ Correct Answer: B

Reason: Disk striping (RAID 0) distributes data across multiple disks, enabling parallel access and improved throughput.

Tag: Normal

---

### Question 852
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Performance Characteristics
Difficulty: Medium

Question: Why do SSDs have consistent latency?
A) Variable latency
B) No mechanical parts, electronic access
C) Slower than HDD
D) Random latency

✔ Correct Answer: B

Reason: SSDs use electronic access without mechanical parts, providing consistent low latency regardless of data location.

Tag: Normal

---

### Question 853
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Write Amplification
Difficulty: Hard

Question: What causes write amplification in SSDs?
A) No amplification
B) Erase-before-write requirement and garbage collection
C) Read operations
D) No cause

✔ Correct Answer: B

Reason: Write amplification occurs because SSDs must erase entire blocks before writing, and garbage collection moves valid data.

Tag: Normal

---

### Question 854
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Performance
Difficulty: Hard

Question: Which RAID level has worst write performance?
A) RAID 0
B) RAID 5 (parity calculation overhead)
C) RAID 1
D) RAID 10

✔ Correct Answer: B

Reason: RAID 5 has worst write performance due to parity calculation and read-modify-write cycle for small writes.

Tag: Normal

---

### Question 855
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Rebuild
Difficulty: Hard

Question: What happens during RAID rebuild?
A) Nothing
B) Data reconstructed on replacement disk, system vulnerable
C) Instant recovery
D) No reconstruction

✔ Correct Answer: B

Reason: RAID rebuild reconstructs data on replacement disk using remaining disks; system vulnerable to second failure during rebuild.

Tag: Normal

---

### Question 856
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Storage Performance Metrics
Difficulty: Medium

Question: What is IOPS?
A) Input/Output Per Second
B) I/O Operations Per Second
C) Internal Operations Per Second
D) No metric

✔ Correct Answer: B

Reason: IOPS (I/O Operations Per Second) measures number of read/write operations storage can perform per second.

Tag: Normal

---

### Question 857
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Storage Performance Metrics
Difficulty: Medium

Question: What is storage throughput?
A) IOPS
B) Amount of data transferred per unit time
C) Latency
D) Capacity

✔ Correct Answer: B

Reason: Throughput measures data transfer rate (MB/s or GB/s), important for sequential access and large transfers.

Tag: Normal

---

### Question 858
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Models
Difficulty: Medium

Question: What is synchronous I/O?
A) Asynchronous
B) Application blocks until I/O completes
C) Non-blocking
D) Parallel I/O

✔ Correct Answer: B

Reason: Synchronous I/O blocks calling thread until operation completes, simple but may reduce concurrency.

Tag: Normal

---

### Question 859
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Models
Difficulty: Medium

Question: What is asynchronous I/O?
A) Blocking
B) Application continues while I/O proceeds
C) Synchronous
D) No I/O

✔ Correct Answer: B

Reason: Asynchronous I/O allows application to continue execution while I/O proceeds, improving concurrency.

Tag: Normal

---

### Question 860
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Multiplexing
Difficulty: Hard

Question: What is select/poll?
A) Single I/O
B) Monitoring multiple file descriptors for I/O readiness
C) No monitoring
D) Sequential I/O

✔ Correct Answer: B

Reason: select/poll allow monitoring multiple file descriptors, notifying when any become ready for I/O.

Tag: Normal

---

### Question 861
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Multiplexing
Difficulty: Hard

Question: What is epoll?
A) Old poll
B) Scalable I/O event notification mechanism
C) No polling
D) Simple poll

✔ Correct Answer: B

Reason: epoll is Linux mechanism for scalable I/O event notification, more efficient than select/poll for many file descriptors.

Tag: Normal

---

### Question 862
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Zero-Copy I/O
Difficulty: Hard

Question: What is zero-copy I/O?
A) Multiple copies
B) Transferring data without copying between kernel and user space
C) No transfer
D) Slow copy

✔ Correct Answer: B

Reason: Zero-copy techniques (sendfile, splice) transfer data without copying between kernel and user buffers, improving performance.

Tag: Normal

---

### Question 863
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Direct I/O
Difficulty: Hard

Question: What is direct I/O?
A) Cached I/O
B) Bypassing page cache for direct disk access
C) Indirect I/O
D) Buffered I/O

✔ Correct Answer: B

Reason: Direct I/O bypasses page cache, transferring directly between user buffer and disk, useful for databases.

Tag: Normal

---

### Question 864
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Memory-Mapped I/O
Difficulty: Medium

Question: What is the advantage of memory-mapped I/O for files?
A) Slower access
B) File access through memory operations, efficient for random access
C) More complex
D) No advantages

✔ Correct Answer: B

Reason: Memory-mapped files allow efficient random access through memory operations, leveraging virtual memory system.

Tag: Normal

---

### Question 865
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control
Difficulty: Easy

Question: What is the principle of least privilege?
A) Maximum privilege
B) Grant minimum privileges necessary
C) No privileges
D) Random privileges

✔ Correct Answer: B

Reason: Least privilege principle grants users/processes only minimum privileges needed to perform tasks, limiting damage from errors or attacks.

Tag: Past Paper

---

### Question 866
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Principles
Difficulty: Medium

Question: What is defense in depth?
A) Single defense
B) Multiple overlapping security layers
C) No defense
D) Single point

✔ Correct Answer: B

Reason: Defense in depth uses multiple security layers so if one fails, others still provide protection.

Tag: Normal

---

### Question 867
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Authentication
Difficulty: Medium

Question: What is multi-factor authentication?
A) Single factor
B) Requiring multiple authentication factors
C) No authentication
D) Password only

✔ Correct Answer: B

Reason: Multi-factor authentication requires multiple factors (knowledge, possession, inherence) for stronger security.

Tag: Normal

---

### Question 868
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Authorization
Difficulty: Medium

Question: What is the difference between authentication and authorization?
A) No difference
B) Authentication verifies identity, authorization determines permissions
C) Same thing
D) Random difference

✔ Correct Answer: B

Reason: Authentication verifies who you are; authorization determines what you're allowed to do.

Tag: Past Paper

---

### Question 869
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Cryptography
Difficulty: Medium

Question: What is a hash function?
A) Encryption
B) One-way function producing fixed-size output
C) Decryption
D) Reversible function

✔ Correct Answer: B

Reason: Hash function is one-way function producing fixed-size output (digest) from variable input, used for integrity verification.

Tag: Normal

---

### Question 870
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Cryptography
Difficulty: Hard

Question: What is a digital signature?
A) Handwritten signature
B) Encrypted hash proving authenticity and integrity
C) Password
D) Username

✔ Correct Answer: B

Reason: Digital signature is encrypted hash of message using private key, proving sender's identity and message integrity.

Tag: Normal

---

### Question 871
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Medium

Question: What is a phishing attack?
A) Network attack
B) Social engineering to steal credentials
C) Virus
D) Hardware attack

✔ Correct Answer: B

Reason: Phishing uses deceptive emails/websites to trick users into revealing credentials or sensitive information.

Tag: Normal

---

### Question 872
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Medium

Question: What is a SQL injection attack?
A) Hardware injection
B) Inserting malicious SQL code through input
C) Network attack
D) Physical attack

✔ Correct Answer: B

Reason: SQL injection inserts malicious SQL code through application input, exploiting poor input validation to access/modify database.

Tag: Normal

---

### Question 873
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Hard

Question: What is a zero-day exploit?
A) Old exploit
B) Exploiting vulnerability before patch available
C) Known exploit
D) Patched exploit

✔ Correct Answer: B

Reason: Zero-day exploit targets vulnerability unknown to vendor or before patch is available, highly dangerous.

Tag: Normal

---

### Question 874
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Defenses
Difficulty: Medium

Question: What is input validation?
A) No validation
B) Checking input for malicious content before processing
C) Output validation
D) No checking

✔ Correct Answer: B

Reason: Input validation checks and sanitizes user input before processing, preventing injection attacks and buffer overflows.

Tag: Normal

---

### Question 875
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Defenses
Difficulty: Hard

Question: What is principle of complete mediation?
A) Partial checking
B) Check every access to every object
C) No checking
D) One-time check

✔ Correct Answer: B

Reason: Complete mediation requires checking every access to every object against access control policy, no caching of permissions.

Tag: Normal

---

### Question 876
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Malware
Difficulty: Easy

Question: What is malware?
A) Good software
B) Malicious software designed to harm or exploit
C) System software
D) Application software

✔ Correct Answer: B

Reason: Malware is malicious software including viruses, worms, trojans, ransomware, designed to harm systems or steal data.

Tag: Normal

---

### Question 877
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Malware
Difficulty: Medium

Question: What is ransomware?
A) Free software
B) Malware encrypting data, demanding ransom
C) Antivirus
D) Backup software

✔ Correct Answer: B

Reason: Ransomware encrypts victim's data and demands payment for decryption key, major security threat.

Tag: Normal

---

### Question 878
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Malware
Difficulty: Medium

Question: What is a rootkit?
A) Root password
B) Malware hiding its presence and maintaining privileged access
C) Admin tool
D) Backup tool

✔ Correct Answer: B

Reason: Rootkit is malware that hides its presence and maintains privileged access by modifying OS components.

Tag: Normal

---

### Question 879
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Monitoring
Difficulty: Medium

Question: What is an intrusion prevention system (IPS)?
A) Detection only
B) Actively blocking detected threats
C) No prevention
D) Monitoring only

✔ Correct Answer: B

Reason: IPS actively blocks detected threats in real-time, unlike IDS which only detects and alerts.

Tag: Normal

---

### Question 880
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Policies
Difficulty: Medium

Question: What is a security policy?
A) Technical implementation
B) Rules defining what is and isn't allowed
C) Software
D) Hardware

✔ Correct Answer: B

Reason: Security policy defines organizational rules and practices for protecting information assets and systems.

Tag: Normal

---

### Question 881
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Performance
Difficulty: Medium

Question: What is CPU-bound workload?
A) I/O intensive
B) Limited by CPU processing speed
C) Memory intensive
D) Network intensive

✔ Correct Answer: B

Reason: CPU-bound workload spends most time computing, performance limited by CPU speed rather than I/O.

Tag: Normal

---

### Question 882
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Performance
Difficulty: Medium

Question: What is I/O-bound workload?
A) CPU intensive
B) Limited by I/O operations
C) Memory intensive
D) Network intensive

✔ Correct Answer: B

Reason: I/O-bound workload spends most time waiting for I/O operations, performance limited by I/O speed.

Tag: Normal

---

### Question 883
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Bottlenecks
Difficulty: Medium

Question: What is a system bottleneck?
A) Fast component
B) Component limiting overall system performance
C) No limitation
D) Optimal component

✔ Correct Answer: B

Reason: Bottleneck is system component that limits overall performance, identifying and addressing bottlenecks improves performance.

Tag: Normal

---

### Question 884
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Design
Difficulty: Hard

Question: What is the end-to-end principle?
A) Centralized control
B) Functionality at endpoints, not intermediate nodes
C) No principle
D) Middle control

✔ Correct Answer: B

Reason: End-to-end principle states functionality should be at endpoints (applications) rather than intermediate layers, improving flexibility.

Tag: Normal

---

### Question 885
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Design
Difficulty: Hard

Question: What is separation of mechanism and policy?
A) Combined approach
B) Separate what is done from how it's done
C) No separation
D) Single approach

✔ Correct Answer: B

Reason: Separating mechanism (how) from policy (what) provides flexibility to change policies without changing mechanisms.

Tag: Normal

---

### Question 886
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Monitoring
Difficulty: Medium

Question: What does ps command show?
A) File system
B) Process status and information
C) Network status
D) Disk usage

✔ Correct Answer: B

Reason: ps displays information about active processes including PID, CPU usage, memory usage, and command.

Tag: Normal

---

### Question 887
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Control
Difficulty: Easy

Question: What does kill command do?
A) Delete files
B) Send signal to process
C) Stop system
D) Format disk

✔ Correct Answer: B

Reason: kill sends signal to process (default SIGTERM), allowing graceful termination or other signal handling.

Tag: Normal

---

### Question 888
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Priority
Difficulty: Medium

Question: What does nice command do?
A) Delete process
B) Run process with modified priority
C) Stop process
D) Create process

✔ Correct Answer: B

Reason: nice runs command with specified nice value, affecting scheduling priority (positive = lower priority).

Tag: Normal

---

### Question 889
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Priority
Difficulty: Medium

Question: What does renice command do?
A) Create process
B) Change priority of running process
C) Terminate process
D) Suspend process

✔ Correct Answer: B

Reason: renice changes nice value (priority) of already running process, adjusting its scheduling priority.

Tag: Normal

---

### Question 890
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Information
Difficulty: Medium

Question: What does uptime command show?
A) Boot time only
B) System uptime and load averages
C) CPU speed
D) Memory size

✔ Correct Answer: B

Reason: uptime displays how long system has been running and load averages for 1, 5, and 15 minutes.

Tag: Normal

---

### Question 891
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Information
Difficulty: Easy

Question: What does free command show?
A) Disk space
B) Memory usage statistics
C) CPU usage
D) Network usage

✔ Correct Answer: B

Reason: free displays amount of free and used memory including physical RAM, swap, buffers, and cache.

Tag: Normal

---

### Question 892
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Mapping
Difficulty: Hard

Question: What does /proc/[pid]/maps show?
A) File maps
B) Process memory mappings
C) Network maps
D) Disk maps

✔ Correct Answer: B

Reason: /proc/[pid]/maps shows memory regions mapped into process address space including libraries, heap, stack.

Tag: Normal

---

### Question 893
Domain: Operating Systems
Topic: File System Management
Subtopic: Disk Usage
Difficulty: Easy

Question: What does df command show?
A) Directory files
B) Disk space usage by file system
C) Data files
D) Deleted files

✔ Correct Answer: B

Reason: df (disk free) displays disk space usage for mounted file systems, showing total, used, and available space.

Tag: Normal

---

### Question 894
Domain: Operating Systems
Topic: File System Management
Subtopic: Disk Usage
Difficulty: Easy

Question: What does du command show?
A) Disk usage by directory/file
B) Disk utility
C) Data upload
D) Device usage

✔ Correct Answer: A

Reason: du (disk usage) estimates space used by files and directories, useful for finding space-consuming items.

Tag: Normal

---

### Question 895
Domain: Operating Systems
Topic: File System Management
Subtopic: File Operations
Difficulty: Easy

Question: What does ln command do?
A) Line numbers
B) Create links between files
C) List names
D) Load network

✔ Correct Answer: B

Reason: ln creates hard links (default) or symbolic links (-s) between files, allowing multiple names for same file.

Tag: Normal

---

### Question 896
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Information
Difficulty: Medium

Question: What does lsblk command show?
A) List blocks
B) Block devices and their relationships
C) List backups
D) Load blocks

✔ Correct Answer: B

Reason: lsblk lists block devices (disks, partitions) and their hierarchical relationships, sizes, and mount points.

Tag: Normal

---

### Question 897
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Monitoring
Difficulty: Medium

Question: What does iotop command show?
A) I/O topology
B) I/O usage by process
C) IP topology
D) Image operations

✔ Correct Answer: B

Reason: iotop displays I/O usage by processes in real-time, identifying processes causing disk activity.

Tag: Normal

---

### Question 898
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Network Monitoring
Difficulty: Medium

Question: What does netstat command show?
A) Network statistics and connections
B) Net status only
C) Network speed
D) No information

✔ Correct Answer: A

Reason: netstat displays network connections, routing tables, interface statistics, and protocol statistics.

Tag: Normal

---

### Question 899
Domain: Operating Systems
Topic: Protection & Security
Subtopic: User Management
Difficulty: Easy

Question: What does sudo command do?
A) Super do
B) Execute command with superuser privileges
C) Switch user
D) System update

✔ Correct Answer: B

Reason: sudo allows authorized users to execute commands with superuser (root) privileges, logged for auditing.

Tag: Normal

---

### Question 900
Domain: Operating Systems
Topic: Protection & Security
Subtopic: File Permissions
Difficulty: Easy

Question: What does chmod command do?
A) Change mode
B) Change file permissions
C) Change owner
D) Change mount

✔ Correct Answer: B

Reason: chmod changes file access permissions (read, write, execute) for owner, group, and others.

Tag: Normal

---

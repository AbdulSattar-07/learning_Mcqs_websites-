# Operating Systems - MCQ Batch 07
## Questions 601-700

---

### Question 601
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Performance
Difficulty: Medium

Question: What is system throughput?
A) Single task speed
B) Amount of work completed per unit time
C) Memory size
D) CPU speed

✔ Correct Answer: B

Reason: System throughput measures total work completed per time unit, indicating overall system productivity and efficiency.

Tag: Normal

---

### Question 602
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Performance
Difficulty: Medium

Question: What is system response time?
A) Boot time
B) Time from request submission to first response
C) Shutdown time
D) Installation time

✔ Correct Answer: B

Reason: Response time measures elapsed time from request submission until first response appears, critical for interactive systems.

Tag: Normal

---

### Question 603
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Batch Processing
Difficulty: Easy

Question: What characterizes batch processing systems?
A) Interactive processing
B) Jobs executed in groups without user interaction
C) Real-time processing
D) Single job execution

✔ Correct Answer: B

Reason: Batch systems collect similar jobs and execute them as group without user interaction, maximizing resource utilization.

Tag: Normal

---

### Question 604
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Interactive Systems
Difficulty: Easy

Question: What defines interactive systems?
A) No user interaction
B) Direct user interaction with immediate feedback
C) Batch processing
D) Offline processing

✔ Correct Answer: B

Reason: Interactive systems provide immediate response to user input, allowing direct communication between user and system.

Tag: Normal

---

### Question 605
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Embedded Systems
Difficulty: Medium

Question: What characterizes embedded operating systems?
A) General purpose
B) Specialized for specific hardware and application
C) Desktop systems
D) Server systems

✔ Correct Answer: B

Reason: Embedded OS are specialized for specific hardware and applications, often with real-time constraints and resource limitations.

Tag: Normal

---

### Question 606
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Utilities
Difficulty: Easy

Question: What are system utilities?
A) Hardware components
B) Programs providing convenient environment for development
C) Kernel modules
D) Device drivers

✔ Correct Answer: B

Reason: System utilities (system programs) provide file management, status information, programming support, and other convenient services.

Tag: Normal

---

### Question 607
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Shell
Difficulty: Easy

Question: What is a shell?
A) Hardware case
B) Command interpreter interface between user and OS
C) Kernel component
D) File system

✔ Correct Answer: B

Reason: Shell is command-line interpreter that accepts and executes user commands, providing interface to OS services.

Tag: Normal

---

### Question 608
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Shell Types
Difficulty: Medium

Question: What distinguishes different shell types?
A) No difference
B) Command syntax, scripting features, built-in commands
C) Speed only
D) Color scheme

✔ Correct Answer: B

Reason: Shells differ in command syntax, scripting capabilities, built-in commands, and features (bash, csh, zsh, PowerShell).

Tag: Normal

---

### Question 609
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Boot Process
Difficulty: Medium

Question: What is the typical boot sequence?
A) Random order
B) BIOS/UEFI → bootloader → kernel → init/systemd
C) Direct to OS
D) No sequence

✔ Correct Answer: B

Reason: Boot sequence: firmware initializes hardware → bootloader loads kernel → kernel initializes → init/systemd starts services.

Tag: Normal

---

### Question 610
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Init Systems
Difficulty: Hard

Question: What is systemd?
A) System daemon
B) Modern init system and service manager
C) File system
D) Network protocol

✔ Correct Answer: B

Reason: systemd is modern init system replacing traditional SysV init, managing system services with parallel startup and dependencies.

Tag: Normal

---

### Question 611
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Priority
Difficulty: Medium

Question: What is process nice value in UNIX?
A) Friendliness rating
B) Priority hint affecting scheduling (-20 to 19)
C) Memory size
D) CPU time

✔ Correct Answer: B

Reason: Nice value (-20 highest priority to 19 lowest) suggests scheduling priority; lower values get more CPU time.

Tag: Normal

---

### Question 612
Domain: Operating Systems
Topic: Process Management
Subtopic: Process States Extended
Difficulty: Hard

Question: What is the suspended state?
A) Running state
B) Process swapped to disk, not eligible for execution
C) Ready state
D) Terminated state

✔ Correct Answer: B

Reason: Suspended state indicates process swapped to disk (suspended ready or suspended blocked), not in memory.

Tag: Normal

---

### Question 613
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Groups
Difficulty: Hard

Question: What is a process group?
A) Random processes
B) Collection of related processes sharing signals
C) Single process
D) No grouping

✔ Correct Answer: B

Reason: Process group is collection of related processes (typically pipeline) that can receive signals collectively.

Tag: Normal

---

### Question 614
Domain: Operating Systems
Topic: Process Management
Subtopic: Session
Difficulty: Hard

Question: What is a session in UNIX?
A) Login time
B) Collection of process groups associated with terminal
C) Single process
D) File system

✔ Correct Answer: B

Reason: Session is collection of process groups, typically all processes started from single login, sharing controlling terminal.

Tag: Normal

---

### Question 615
Domain: Operating Systems
Topic: Process Management
Subtopic: Daemon Processes
Difficulty: Medium

Question: What are daemon processes?
A) Evil processes
B) Background processes providing system services
C) User processes
D) Temporary processes

✔ Correct Answer: B

Reason: Daemons are background processes running continuously, providing system services without user interaction (e.g., httpd, sshd).

Tag: Normal

---

### Question 616
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Accounting
Difficulty: Hard

Question: What is process accounting?
A) Financial accounting
B) Recording process resource usage for billing/analysis
C) Process creation
D) Process termination

✔ Correct Answer: B

Reason: Process accounting tracks CPU time, memory usage, I/O operations per process for billing, analysis, and optimization.

Tag: Normal

---

### Question 617
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Domains
Difficulty: Hard

Question: What are scheduling domains in multiprocessor systems?
A) Network domains
B) Hierarchical grouping of CPUs for load balancing
C) Memory domains
D) No domains

✔ Correct Answer: B

Reason: Scheduling domains organize CPUs hierarchically (cores, packages, NUMA nodes) for efficient load balancing.

Tag: Normal

---

### Question 618
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Gang Scheduling
Difficulty: Hard

Question: What is gang scheduling?
A) Random scheduling
B) Scheduling related threads simultaneously on different CPUs
C) Single thread scheduling
D) Sequential scheduling

✔ Correct Answer: B

Reason: Gang scheduling schedules all threads of parallel application simultaneously on different processors, reducing synchronization delays.

Tag: Normal

---

### Question 619
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Completely Fair Scheduler
Difficulty: Hard

Question: What is CFS in Linux?
A) Complete File System
B) Scheduler providing fair CPU time based on virtual runtime
C) Cache File System
D) Network scheduler

✔ Correct Answer: B

Reason: CFS (Completely Fair Scheduler) tracks virtual runtime, scheduling process with smallest runtime next for fairness.

Tag: Normal

---

### Question 620
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Real-Time Scheduling Classes
Difficulty: Hard

Question: What are the real-time scheduling policies in Linux?
A) Only SCHED_OTHER
B) SCHED_FIFO and SCHED_RR
C) No real-time policies
D) Random policies

✔ Correct Answer: B

Reason: Linux provides SCHED_FIFO (first-in-first-out) and SCHED_RR (round-robin) for real-time scheduling with priorities.

Tag: Normal

---

### Question 621
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Priority Inversion Solution
Difficulty: Hard

Question: What is priority ceiling protocol?
A) Lowering priority
B) Resource assigned priority of highest-priority process that may lock it
C) Random priority
D) No protocol

✔ Correct Answer: B

Reason: Priority ceiling protocol assigns each resource ceiling priority equal to highest priority of any process that may lock it, preventing priority inversion.

Tag: Normal

---

### Question 622
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Scheduling
Difficulty: Medium

Question: What is process-contention scope (PCS)?
A) System-wide competition
B) Thread competes within its process
C) No competition
D) Global competition

✔ Correct Answer: B

Reason: PCS means user-level threads compete for CPU within their process, scheduled by thread library.

Tag: Normal

---

### Question 623
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Scheduling
Difficulty: Hard

Question: What is system-contention scope (SCS)?
A) Process-level competition
B) Thread competes system-wide with all threads
C) No competition
D) Local competition

✔ Correct Answer: B

Reason: SCS means kernel threads compete system-wide for CPU, scheduled by OS kernel like processes.

Tag: Normal

---

### Question 624
Domain: Operating Systems
Topic: Thread Management
Subtopic: Lightweight Process
Difficulty: Hard

Question: What is a lightweight process (LWP)?
A) Small process
B) Intermediate data structure between user and kernel threads
C) Heavy process
D) No process

✔ Correct Answer: B

Reason: LWP is kernel data structure providing virtual processor for user thread execution, used in many-to-many model.

Tag: Normal

---

### Question 625
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Synchronization
Difficulty: Medium

Question: Why do threads need synchronization?
A) No need
B) Prevent race conditions when accessing shared data
C) Slow down execution
D) Increase complexity

✔ Correct Answer: B

Reason: Threads sharing address space need synchronization to prevent race conditions and ensure data consistency.

Tag: Past Paper

---

### Question 626
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Mutex vs Semaphore
Difficulty: Medium

Question: What distinguishes mutex from binary semaphore?
A) No difference
B) Mutex has ownership, only owner can unlock
C) Semaphore is faster
D) Mutex is slower

✔ Correct Answer: B

Reason: Mutex has ownership concept; only thread that locked it can unlock it, unlike binary semaphore.

Tag: Normal

---

### Question 627
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Recursive Mutex
Difficulty: Hard

Question: What is a recursive mutex?
A) Non-recursive lock
B) Mutex that can be locked multiple times by same thread
C) Regular mutex
D) No mutex

✔ Correct Answer: B

Reason: Recursive mutex allows same thread to lock it multiple times, tracking lock count, useful for recursive functions.

Tag: Normal

---

### Question 628
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Read-Write Lock
Difficulty: Hard

Question: When should read-write locks be used?
A) Equal reads and writes
B) Read-heavy workloads
C) Write-heavy workloads
D: Never

✔ Correct Answer: B

Reason: Read-write locks optimize read-heavy workloads by allowing concurrent readers, beneficial when reads greatly outnumber writes.

Tag: Normal

---

### Question 629
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Atomic Variables
Difficulty: Hard

Question: What are atomic variables?
A) Regular variables
B) Variables with atomic operations without locks
C) Large variables
D) No variables

✔ Correct Answer: B

Reason: Atomic variables provide lock-free atomic operations (increment, compare-and-swap) using hardware support.

Tag: Normal

---

### Question 630
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Memory Barriers
Difficulty: Hard

Question: What are memory barriers?
A) Physical barriers
B) Instructions ensuring memory operation ordering
C) Memory allocation
D: No barriers

✔ Correct Answer: B

Reason: Memory barriers (fences) prevent CPU/compiler from reordering memory operations, ensuring visibility in concurrent programs.

Tag: Normal

---

### Question 631
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Happens-Before Relationship
Difficulty: Hard

Question: What is happens-before relationship?
A: Random relationship
B: Partial ordering ensuring one operation's effects visible to another
C: No relationship
D: Time-based only

✔ Correct Answer: B

Reason: Happens-before defines partial order where if A happens-before B, A's effects are visible to B, crucial for concurrent correctness.

Tag: Normal

---

### Question 632
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock vs Livelock
Difficulty: Medium

Question: How does livelock differ from deadlock?
A: Same thing
B: Livelock processes active but not progressing, deadlock processes blocked
C: Livelock is faster
D: No difference

✔ Correct Answer: B

Reason: Deadlock has processes blocked waiting; livelock has processes actively changing state but making no progress.

Tag: Normal

---

### Question 633
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention Tradeoffs
Difficulty: Hard

Question: What is the cost of preventing hold and wait?
A: No cost
B: Low resource utilization, possible starvation
C: Better performance
D: No impact

✔ Correct Answer: B

Reason: Requiring all resources at once causes low utilization (resources held but unused) and possible starvation.

Tag: Normal

---

### Question 634
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention Tradeoffs
Difficulty: Hard

Question: What is the cost of allowing preemption?
A: No cost
B: Overhead of saving/restoring state, not applicable to all resources
C: Faster execution
D: No impact

✔ Correct Answer: B

Reason: Preemption requires saving/restoring resource state and only works for resources whose state can be saved (memory, CPU, not printers).

Tag: Normal

---

### Question 635
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Allocation Algorithms
Difficulty: Medium

Question: Which allocation algorithm is fastest?
A: Best-fit
B: First-fit
C: Worst-fit
D: All equal

✔ Correct Answer: B

Reason: First-fit is fastest as it stops searching at first suitable hole, while best-fit and worst-fit search entire list.

Tag: Normal

---

### Question 636
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Compaction
Difficulty: Hard

Question: When should memory compaction be performed?
A: Always
B: When fragmentation severe and performance degraded
C: Never
D: Randomly

✔ Correct Answer: B

Reason: Compaction is expensive; perform only when external fragmentation significantly impacts allocation or performance.

Tag: Normal

---

### Question 637
Domain: Operating Systems
Topic: Memory Management
Subtopic: Paging Hardware
Difficulty: Medium

Question: What is the page table base register (PTBR)?
A: Page size register
B: Points to page table location
C: Frame register
D: No register

✔ Correct Answer: B

Reason: PTBR contains physical address of page table, loaded during context switch to access process's page table.

Tag: Normal

---

### Question 638
Domain: Operating Systems
Topic: Memory Management
Subtopic: Paging Hardware
Difficulty: Medium

Question: What is the page table length register (PTLR)?
A: Page size
B: Indicates page table size
C: Frame count
D: No register

✔ Correct Answer: B

Reason: PTLR indicates size of page table, used to check if page number is within valid range.

Tag: Normal

---

### Question 639
Domain: Operating Systems
Topic: Memory Management
Subtopic: Shared Pages
Difficulty: Hard

Question: What requirement must shared pages meet?
A: Any pages
B: Must be reentrant (read-only) code
C: Must be writable
D: No requirement

✔ Correct Answer: B

Reason: Shared pages must be reentrant (pure code) that doesn't modify itself, allowing safe sharing among processes.

Tag: Normal

---

### Question 640
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation Advantages
Difficulty: Medium

Question: What advantage does segmentation provide?
A: Fixed sizes
B: Logical organization matching program structure
C: No advantages
D: Slower access

✔ Correct Answer: B

Reason: Segmentation provides logical organization (code, data, stack segments) matching programmer's view, simplifying protection and sharing.

Tag: Normal

---

### Question 641
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation Disadvantages
Difficulty: Medium

Question: What is the main disadvantage of segmentation?
A: Too simple
B: External fragmentation from variable-size segments
C: Too fast
D: No disadvantages

✔ Correct Answer: B

Reason: Variable-size segments cause external fragmentation, requiring compaction or complex allocation algorithms.

Tag: Normal

---

### Question 642
Domain: Operating Systems
Topic: Memory Management
Subtopic: Virtual Memory Benefits
Difficulty: Easy

Question: What is a key benefit of virtual memory?
A: Slower execution
B: Programs larger than physical memory can execute
C: More complexity
D: Less memory

✔ Correct Answer: B

Reason: Virtual memory allows execution of programs larger than physical RAM by keeping only needed portions in memory.

Tag: Past Paper

---

### Question 643
Domain: Operating Systems
Topic: Memory Management
Subtopic: Virtual Memory Benefits
Difficulty: Medium

Question: How does virtual memory improve multiprogramming?
A: Reduces multiprogramming
B: More processes in memory as not all pages needed
C: No impact
D: Slows down

✔ Correct Answer: B

Reason: Virtual memory increases degree of multiprogramming as each process needs only subset of pages in memory.

Tag: Normal

---

### Question 644
Domain: Operating Systems
Topic: Memory Management
Subtopic: Demand Paging Optimization
Difficulty: Hard

Question: What is prepaging strategy?
A: No paging
B: Load predicted pages before referenced
C: Delayed paging
D: Random paging

✔ Correct Answer: B

Reason: Prepaging loads pages likely to be used soon (e.g., working set) to reduce page faults, trading I/O efficiency for prediction accuracy.

Tag: Normal

---

### Question 645
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Size Considerations
Difficulty: Hard

Question: What happens with very small page size?
A: Better performance
B: Large page table, more page faults, better locality
C: Optimal size
D: No impact

✔ Correct Answer: B

Reason: Small pages increase page table size and page faults but improve memory utilization and locality.

Tag: Normal

---

### Question 646
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Size Considerations
Difficulty: Hard

Question: What happens with very large page size?
A: Optimal performance
B: Internal fragmentation, fewer page faults, smaller table
C: Worse performance
D: No impact

✔ Correct Answer: B

Reason: Large pages reduce page table size and page faults but increase internal fragmentation and reduce locality.

Tag: Normal

---

### Question 647
Domain: Operating Systems
Topic: Memory Management
Subtopic: TLB Performance
Difficulty: Hard

Question: What is TLB coverage?
A: TLB size
B: Amount of memory addressable through TLB
C: TLB speed
D: No concept

✔ Correct Answer: B

Reason: TLB coverage (reach) is total memory accessible via TLB entries; increasing page size increases coverage.

Tag: Normal

---

### Question 648
Domain: Operating Systems
Topic: Memory Management
Subtopic: Inverted Page Table Benefits
Difficulty: Hard

Question: What is the main benefit of inverted page tables?
A: Faster access
B: Fixed size regardless of virtual address space
C: Simpler implementation
D: No benefits

✔ Correct Answer: B

Reason: Inverted page table size depends on physical memory (one entry per frame), not virtual address space size.

Tag: Normal

---

### Question 649
Domain: Operating Systems
Topic: Memory Management
Subtopic: Inverted Page Table Drawbacks
Difficulty: Hard

Question: What is the main drawback of inverted page tables?
A: Too large
B: Slower lookup requiring search or hashing
C: Too simple
D: No drawbacks

✔ Correct Answer: B

Reason: Inverted page tables require searching or hashing to find entry, slower than direct indexing in forward page tables.

Tag: Normal

---

### Question 650
Domain: Operating Systems
Topic: Memory Management
Subtopic: Copy-on-Write Benefits
Difficulty: Hard

Question: Why is copy-on-write beneficial for fork()?
A: Slower fork
B: Fast process creation, memory saved if no writes
C: More memory used
D: No benefits

✔ Correct Answer: B

Reason: COW makes fork() fast by sharing pages initially, copying only when written, saving memory and time.

Tag: Normal

---

### Question 651
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory-Mapped Files Benefits
Difficulty: Hard

Question: What is an advantage of memory-mapped files?
A: Slower access
B: File I/O through memory operations, efficient for large files
C: More complex
D: No advantages

✔ Correct Answer: B

Reason: Memory-mapped files allow file access through memory operations, efficient for large files and enabling shared memory IPC.

Tag: Normal

---

### Question 652
Domain: Operating Systems
Topic: Memory Management
Subtopic: Kernel Memory Allocation
Difficulty: Hard

Question: Why does kernel memory allocation differ from user memory?
A: No difference
B: Kernel needs contiguous physical memory, no page faults allowed
C: Kernel is simpler
D: User is more complex

✔ Correct Answer: B

Reason: Kernel often needs contiguous physical memory for DMA, cannot handle page faults in interrupt handlers.

Tag: Normal

---

### Question 653
Domain: Operating Systems
Topic: Memory Management
Subtopic: Thrashing Prevention
Difficulty: Medium

Question: How can thrashing be prevented?
A: Cannot prevent
B: Ensure sufficient frames per process, limit multiprogramming
C: Add more processes
D: Reduce memory

✔ Correct Answer: B

Reason: Prevent thrashing by ensuring each process has enough frames for working set and limiting degree of multiprogramming.

Tag: Normal

---

### Question 654
Domain: Operating Systems
Topic: Memory Management
Subtopic: Working Set Model
Difficulty: Hard

Question: What does working set model assume?
A: Random access
B: Locality of reference - process uses subset of pages
C: All pages used
D: No assumptions

✔ Correct Answer: B

Reason: Working set model assumes locality of reference, where process actively uses only subset of pages in time window.

Tag: Normal

---

### Question 655
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Mounting
Difficulty: Medium

Question: What happens when file system is unmounted?
A: File system deleted
B: File system detached, must ensure no open files
C: File system formatted
D: Nothing

✔ Correct Answer: B

Reason: Unmounting detaches file system from directory tree; OS must ensure no files are open before unmounting.

Tag: Normal

---

### Question 656
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Types
Difficulty: Medium

Question: What is a journaling file system?
A: No journal
B: Logs changes before committing for crash recovery
C: Slower system
D: Old system

✔ Correct Answer: B

Reason: Journaling file systems log metadata changes to journal before committing, enabling fast recovery after crashes.

Tag: Normal

---

### Question 657
Domain: Operating Systems
Topic: File System Management
Subtopic: ext4 Features
Difficulty: Hard

Question: What features does ext4 provide?
A: Basic features only
B: Extents, delayed allocation, journal checksums, large file support
C: No features
D: Minimal features

✔ Correct Answer: B

Reason: ext4 provides extents (contiguous blocks), delayed allocation, journal checksums, and supports large files/volumes.

Tag: Normal

---

### Question 658
Domain: Operating Systems
Topic: File System Management
Subtopic: NTFS Features
Difficulty: Hard

Question: What characterizes NTFS?
A: Simple file system
B: Journaling, ACLs, encryption, compression, large files
C: No features
D: FAT variant

✔ Correct Answer: B

Reason: NTFS provides journaling, access control lists, encryption, compression, and supports very large files and volumes.

Tag: Normal

---

### Question 659
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Performance
Difficulty: Medium

Question: What improves file system read performance?
A: Slower disk
B: Read-ahead (prefetching) and caching
C: Less memory
D: No optimization

✔ Correct Answer: B

Reason: Read-ahead prefetches sequential blocks, caching stores frequently accessed blocks, both improving read performance.

Tag: Normal

---

### Question 660
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Performance
Difficulty: Medium

Question: What improves file system write performance?
A: Synchronous writes
B: Write-behind (delayed write) and buffering
C: Immediate writes
D: No optimization

✔ Correct Answer: B

Reason: Write-behind delays writes to batch them efficiently, buffering accumulates writes, both improving write performance.

Tag: Normal

---

### Question 661
Domain: Operating Systems
Topic: File System Management
Subtopic: Block Allocation
Difficulty: Hard

Question: What is delayed allocation?
A: Immediate allocation
B: Defer block allocation until write-back
C: No allocation
D: Random allocation

✔ Correct Answer: B

Reason: Delayed allocation defers physical block allocation until data written to disk, allowing better allocation decisions.

Tag: Normal

---

### Question 662
Domain: Operating Systems
Topic: File System Management
Subtopic: Directory Caching
Difficulty: Medium

Question: What is directory name lookup cache (dcache)?
A: Disk cache
B: Cache mapping pathnames to inodes
C: Data cache
D: No cache

✔ Correct Answer: B

Reason: Dcache caches recent directory lookups, mapping pathnames to inodes, avoiding repeated directory traversals.

Tag: Normal

---

### Question 663
Domain: Operating Systems
Topic: File System Management
Subtopic: Inode Caching
Difficulty: Medium

Question: What is inode cache?
A: Data cache
B: Cache of recently accessed inodes
C: Directory cache
D: No cache

✔ Correct Answer: B

Reason: Inode cache keeps recently accessed inodes in memory, avoiding disk reads for file metadata.

Tag: Normal

---

### Question 664
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Reliability
Difficulty: Medium

Question: How do file systems ensure reliability?
A: No mechanisms
B: Journaling, checksums, redundancy, backups
C: Single copy only
D: No protection

✔ Correct Answer: B

Reason: Reliability ensured through journaling (consistency), checksums (corruption detection), redundancy (RAID), and backups.

Tag: Normal

---

### Question 665
Domain: Operating Systems
Topic: File System Management
Subtopic: Soft Updates
Difficulty: Hard

Question: What are soft updates?
A: Hard updates
B: Ordering metadata writes to maintain consistency
C: Random updates
D: No updates

✔ Correct Answer: B

Reason: Soft updates carefully order metadata writes to maintain file system consistency without journaling overhead.

Tag: Normal

---

### Question 666
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Scheduling Performance
Difficulty: Medium

Question: Which disk scheduling algorithm provides most uniform wait time?
A: FCFS
B: C-SCAN
C: SSTF
D: Random

✔ Correct Answer: B

Reason: C-SCAN provides more uniform wait time than SCAN by treating requests more fairly with circular pattern.

Tag: Normal

---

### Question 667
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Performance Factors
Difficulty: Medium

Question: What affects disk performance most?
A: Color
B: Seek time and rotational latency
C: Brand
D: Age only

✔ Correct Answer: B

Reason: Mechanical delays (seek time and rotational latency) dominate disk access time, far exceeding transfer time.

Tag: Normal

---

### Question 668
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Caching
Difficulty: Medium

Question: Where can disk caching occur?
A: Disk only
B: Disk controller, OS buffer cache, application
C: OS only
D: No caching

✔ Correct Answer: B

Reason: Disk caching occurs at multiple levels: disk controller cache, OS buffer cache, and application-level caching.

Tag: Normal

---

### Question 669
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Native Command Queuing
Difficulty: Hard

Question: What is NCQ?
A: No queuing
B: Disk reorders commands for optimal performance
C: FCFS queuing
D: Random queuing

✔ Correct Answer: B

Reason: NCQ (Native Command Queuing) allows disk to reorder queued commands for optimal head movement and performance.

Tag: Normal

---

### Question 670
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Performance
Difficulty: Medium

Question: Why are SSDs faster than HDDs?
A: Larger size
B: No mechanical parts, parallel access
C: Cheaper
D: Older technology

✔ Correct Answer: B

Reason: SSDs have no mechanical delays, support parallel operations across channels, and provide consistent low latency.

Tag: Normal

---

### Question 671
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Limitations
Difficulty: Hard

Question: What limits SSD lifespan?
A: Unlimited writes
B: Limited write/erase cycles per cell
C: Read operations
D: No limitations

✔ Correct Answer: B

Reason: Flash cells have limited write/erase cycles (thousands to millions), requiring wear leveling to extend lifespan.

Tag: Normal

---

### Question 672
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Garbage Collection
Difficulty: Hard

Question: Why do SSDs need garbage collection?
A: No need
B: Reclaim space from invalid pages, consolidate data
C: Delete files
D: Format disk

✔ Correct Answer: B

Reason: SSDs need garbage collection to reclaim space from invalid pages and consolidate valid data for efficient block erasure.

Tag: Normal

---

### Question 673
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Over-Provisioning
Difficulty: Hard

Question: What is over-provisioning in SSDs?
A: Under-provisioning
B: Extra capacity for wear leveling and performance
C: No extra space
D: User storage

✔ Correct Answer: B

Reason: Over-provisioning reserves extra capacity beyond advertised size for wear leveling, garbage collection, and maintaining performance.

Tag: Normal

---

### Question 674
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Performance
Difficulty: Hard

Question: Which RAID level provides best read performance?
A: RAID 1
B: RAID 0
C: RAID 5
D: RAID 6

✔ Correct Answer: B

Reason: RAID 0 provides best read performance through striping without redundancy overhead, though no fault tolerance.

Tag: Normal

---

### Question 675
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Reliability
Difficulty: Hard

Question: Which RAID level provides highest reliability?
A: RAID 0
B: RAID 6 or RAID 10
C: RAID 1
D: RAID 5

✔ Correct Answer: B

Reason: RAID 6 (two parity) and RAID 10 (mirrored stripes) provide highest reliability, surviving multiple disk failures.

Tag: Normal

---

### Question 676
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Storage Area Network
Difficulty: Hard

Question: What is a SAN?
A: Local storage
B: Network providing block-level storage access
C: File system
D: Direct attached storage

✔ Correct Answer: B

Reason: SAN (Storage Area Network) is dedicated network providing block-level storage access to multiple servers.

Tag: Normal

---

### Question 677
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Network Attached Storage
Difficulty: Hard

Question: How does NAS differ from SAN?
A: No difference
B: NAS provides file-level access, SAN provides block-level
C: NAS is faster
D: SAN is obsolete

✔ Correct Answer: B

Reason: NAS provides file-level access over network (NFS, SMB), while SAN provides block-level access (appears as local disk).

Tag: Normal

---

### Question 678
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Performance
Difficulty: Medium

Question: What improves I/O performance?
A: Slower devices
B: Buffering, caching, scheduling, asynchronous I/O
C: Less memory
D: No optimization

✔ Correct Answer: B

Reason: I/O performance improved through buffering (smooth speed differences), caching (reduce I/O), scheduling (order requests), async I/O (concurrency).

Tag: Normal

---

### Question 679
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Buffering
Difficulty: Medium

Question: What is double buffering?
A: Single buffer
B: Two buffers alternating for continuous I/O
C: No buffering
D: Triple buffering

✔ Correct Answer: B

Reason: Double buffering uses two buffers alternating: one being filled while other is processed, enabling continuous I/O.

Tag: Normal

---

### Question 680
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Scatter-Gather I/O
Difficulty: Hard

Question: What is scatter-gather I/O?
A: Single buffer I/O
B: Single I/O operation with multiple buffers
C: No I/O
D: Sequential I/O

✔ Correct Answer: B

Reason: Scatter-gather I/O allows single I/O operation to read into (scatter) or write from (gather) multiple buffers.

Tag: Normal

---

### Question 681
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Modes
Difficulty: Medium

Question: What is memory-mapped I/O advantage?
A: Slower access
B: Use standard memory instructions for I/O
C: More complex
D: No advantages

✔ Correct Answer: B

Reason: Memory-mapped I/O allows using standard load/store instructions for device access, simplifying programming.

Tag: Normal

---

### Question 682
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Modes
Difficulty: Medium

Question: What is port-mapped I/O advantage?
A: No advantages
B: Separate address space protects memory from I/O
C: Slower
D: More complex

✔ Correct Answer: B

Reason: Port-mapped I/O uses separate address space, preventing accidental memory access when performing I/O.

Tag: Normal

---

### Question 683
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Interrupt Coalescing
Difficulty: Hard

Question: What is interrupt coalescing?
A: More interrupts
B: Combining multiple interrupts into single interrupt
C: No interrupts
D: Random interrupts

✔ Correct Answer: B

Reason: Interrupt coalescing combines multiple device interrupts into single interrupt, reducing interrupt overhead for high-throughput devices.

Tag: Normal

---

### Question 684
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O APIC
Difficulty: Hard

Question: What is I/O APIC?
A: Old interrupt controller
B: Advanced interrupt controller for multiprocessor systems
C: No controller
D: Simple controller

✔ Correct Answer: B

Reason: I/O APIC (Advanced Programmable Interrupt Controller) handles interrupts in multiprocessor systems, replacing PIC.

Tag: Normal

---

### Question 685
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Principles
Difficulty: Medium

Question: What is the principle of separation of privilege?
A: Single privilege
B: Require multiple conditions for access
C: No separation
D: Unlimited privilege

✔ Correct Answer: B

Reason: Separation of privilege requires multiple independent conditions for access, reducing risk from single point of failure.

Tag: Normal

---

### Question 686
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Principles
Difficulty: Hard

Question: What is the principle of fail-safe defaults?
A: Default allow
B: Default deny unless explicitly permitted
C: No defaults
D: Random defaults

✔ Correct Answer: B

Reason: Fail-safe defaults deny access unless explicitly granted, more secure than allowing access unless explicitly denied.

Tag: Normal

---

### Question 687
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Principles
Difficulty: Hard

Question: What is the principle of economy of mechanism?
A: Complex design
B: Keep security mechanisms simple
C: Large systems
D: No principle

✔ Correct Answer: B

Reason: Economy of mechanism advocates simple, small security mechanisms that are easier to verify and less likely to have flaws.

Tag: Normal

---

### Question 688
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control Models
Difficulty: Hard

Question: What is Mandatory Access Control (MAC)?
A: User controls access
B: System enforces access based on security labels
C: No control
D: Optional control

✔ Correct Answer: B

Reason: MAC enforces access control based on security classifications and clearances, users cannot override system policy.

Tag: Normal

---

### Question 689
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Levels
Difficulty: Hard

Question: What is the Bell-LaPadula model?
A: Integrity model
B: Confidentiality model with no read up, no write down
C: Availability model
D: No model

✔ Correct Answer: B

Reason: Bell-LaPadula ensures confidentiality: no read up (can't read higher classification), no write down (can't write to lower).

Tag: Normal

---

### Question 690
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Levels
Difficulty: Hard

Question: What is the Biba model?
A: Confidentiality model
B: Integrity model with no write up, no read down
C: Availability model
D: No model

✔ Correct Answer: B

Reason: Biba ensures integrity: no write up (can't write to higher integrity), no read down (can't read lower integrity).

Tag: Normal

---

### Question 691
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Mechanisms
Difficulty: Medium

Question: What is two-factor authentication?
A: Single factor
B: Requires two different authentication factors
C: No authentication
D: Three factors

✔ Correct Answer: B

Reason: Two-factor authentication requires two different types of factors (e.g., password + token), stronger than single factor.

Tag: Normal

---

### Question 692
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Mechanisms
Difficulty: Hard

Question: What is challenge-response authentication?
A: Static password
B: Server challenges, client responds with computed value
C: No challenge
D: Simple password

✔ Correct Answer: B

Reason: Challenge-response sends random challenge, client computes response using secret, preventing replay attacks.

Tag: Normal

---

### Question 693
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Medium

Question: What is a brute-force attack?
A: Physical attack
B: Trying all possible passwords/keys
C: Social engineering
D: Network attack

✔ Correct Answer: B

Reason: Brute-force attack systematically tries all possible passwords or keys until correct one found.

Tag: Normal

---

### Question 694
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Hard

Question: What is a timing attack?
A: Random attack
B: Analyzing execution time to extract secrets
C: Slow attack
D: No attack

✔ Correct Answer: B

Reason: Timing attack analyzes time taken for operations to infer secret information like cryptographic keys.

Tag: Normal

---

### Question 695
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Hard

Question: What is a side-channel attack?
A: Direct attack
B: Exploiting information from physical implementation
C: Network attack
D: No attack

✔ Correct Answer: B

Reason: Side-channel attacks exploit information leaked through physical implementation (timing, power consumption, electromagnetic radiation).

Tag: Normal

---

### Question 696
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Defenses
Difficulty: Medium

Question: What is the purpose of DEP (Data Execution Prevention)?
A: Allow code execution anywhere
B: Prevent code execution from data pages
C: No prevention
D: Allow all execution

✔ Correct Answer: B

Reason: DEP marks data pages as non-executable, preventing buffer overflow attacks from executing injected code.

Tag: Normal

---

### Question 697
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Defenses
Difficulty: Hard

Question: What is control-flow integrity (CFI)?
A: No integrity
B: Ensuring program follows valid control-flow paths
C: Data integrity
D: Random flow

✔ Correct Answer: B

Reason: CFI ensures program control flow follows valid paths defined at compile time, preventing control-flow hijacking attacks.

Tag: Normal

---

### Question 698
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Secure Boot
Difficulty: Hard

Question: What is secure boot?
A: Fast boot
B: Verifying boot components using digital signatures
C: No verification
D: Slow boot

✔ Correct Answer: B

Reason: Secure boot verifies digital signatures of bootloader and OS components, preventing rootkit and bootkit infections.

Tag: Normal

---

### Question 699
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Trusted Platform Module
Difficulty: Hard

Question: What is TPM?
A: Software module
B: Hardware chip providing cryptographic functions
C: Network module
D: No module

✔ Correct Answer: B

Reason: TPM (Trusted Platform Module) is hardware chip providing secure key storage, random number generation, and cryptographic operations.

Tag: Normal

---

### Question 700
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Monitoring
Difficulty: Medium

Question: What is intrusion detection system (IDS)?
A: Prevention system
B: Monitors network/system for malicious activity
C: Firewall
D: Antivirus

✔ Correct Answer: B

Reason: IDS monitors network traffic and system activities for suspicious patterns indicating security breaches or attacks.

Tag: Normal

---

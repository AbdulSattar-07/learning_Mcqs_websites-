# Operating Systems - MCQ Batch 10
## Questions 901-1000

---

### Question 901
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Architecture
Difficulty: Medium

Question: What is a monolithic system?
A) Modular system
B) Single large kernel with all services
C) Distributed system
D) No kernel

✔ Correct Answer: B

Reason: Monolithic system has all OS services in single large kernel running in kernel mode, fast but less modular.

Tag: Normal

---

### Question 902
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Architecture
Difficulty: Hard

Question: What is a distributed operating system?
A) Single machine OS
B) OS managing multiple independent computers as single system
C) Local OS
D) No distribution

✔ Correct Answer: B

Reason: Distributed OS coordinates multiple independent computers, providing unified system view with resource sharing and communication.

Tag: Normal

---

### Question 903
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Calls
Difficulty: Medium

Question: What is the purpose of system call wrapper functions?
A) No purpose
B) Provide convenient interface hiding low-level details
C) Slow down calls
D) Add complexity

✔ Correct Answer: B

Reason: Wrapper functions (like printf wrapping write) provide convenient high-level interface hiding system call complexity.

Tag: Normal

---

### Question 904
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Operating System Services
Difficulty: Easy

Question: Which is an OS service for users?
A) Hardware management
B) Program execution, I/O operations, file manipulation
C) Kernel compilation
D) Hardware manufacturing

✔ Correct Answer: B

Reason: User-facing OS services include program execution, I/O operations, file system manipulation, and communication.

Tag: Normal

---

### Question 905
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Operating System Services
Difficulty: Medium

Question: Which is an OS service for system efficiency?
A) User interface
B) Resource allocation, accounting, protection
C) Application development
D) User documentation

✔ Correct Answer: B

Reason: System efficiency services include resource allocation, accounting (tracking usage), and protection/security.

Tag: Normal

---

### Question 906
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Command Interpreter
Difficulty: Easy

Question: What is the role of command interpreter?
A) Compile programs
B) Get and execute user commands
C) Manage memory
D) Control hardware

✔ Correct Answer: B

Reason: Command interpreter (shell) reads user commands and executes them, providing interface between user and OS.

Tag: Normal

---

### Question 907
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Graphical User Interface
Difficulty: Easy

Question: What is a GUI?
A) Command-line interface
B) Visual interface with windows, icons, menus
C) Text interface
D) No interface

✔ Correct Answer: B

Reason: GUI (Graphical User Interface) provides visual interface with windows, icons, menus, and pointer for user interaction.

Tag: Normal

---

### Question 908
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling States
Difficulty: Medium

Question: What is the ready state?
A) Process executing
B) Process waiting for CPU allocation
C) Process waiting for I/O
D) Process terminated

✔ Correct Answer: B

Reason: Ready state means process is loaded in memory and waiting for CPU allocation by scheduler.

Tag: Past Paper

---

### Question 909
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling States
Difficulty: Medium

Question: What is the running state?
A) Process waiting
B) Process currently executing on CPU
C) Process blocked
D) Process created

✔ Correct Answer: B

Reason: Running state means process is currently executing instructions on CPU.

Tag: Normal

---

### Question 910
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling States
Difficulty: Medium

Question: What is the waiting/blocked state?
A) Process executing
B) Process waiting for event or I/O completion
C) Process ready
D) Process terminated

✔ Correct Answer: B

Reason: Waiting/blocked state means process cannot continue until event occurs (I/O completion, signal, resource availability).

Tag: Normal

---

### Question 911
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Operations
Difficulty: Easy

Question: What are the two main process operations?
A) Read and write
B) Creation and termination
C) Start and stop
D) Load and unload

✔ Correct Answer: B

Reason: Main process operations are creation (fork, spawn) and termination (exit, abort), managing process lifecycle.

Tag: Normal

---

### Question 912
Domain: Operating Systems
Topic: Process Management
Subtopic: Interprocess Communication
Difficulty: Medium

Question: What are the two fundamental IPC models?
A) Fast and slow
B) Shared memory and message passing
C) Direct and indirect
D) Synchronous and asynchronous

✔ Correct Answer: B

Reason: Two fundamental IPC models: shared memory (processes share memory region) and message passing (exchange messages).

Tag: Past Paper

---

### Question 913
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Preemptive Scheduling
Difficulty: Medium

Question: When can preemptive scheduling occur?
A) Only at process termination
B) When process switches from running to ready or waiting
C) Never
D) Only at creation

✔ Correct Answer: B

Reason: Preemptive scheduling can occur when process switches from running to ready (preempted) or running to waiting (I/O).

Tag: Normal

---

### Question 914
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Non-Preemptive Scheduling
Difficulty: Medium

Question: When does non-preemptive scheduling occur?
A) Anytime
B) Only when process terminates or blocks
C) Every millisecond
D) Randomly

✔ Correct Answer: B

Reason: Non-preemptive scheduling occurs only when process voluntarily relinquishes CPU (terminates or blocks for I/O).

Tag: Normal

---

### Question 915
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Dispatcher
Difficulty: Medium

Question: What is dispatch latency?
A) Execution time
B) Time for dispatcher to stop one process and start another
C) Waiting time
D) Turnaround time

✔ Correct Answer: B

Reason: Dispatch latency is time taken by dispatcher to perform context switch, should be minimized for efficiency.

Tag: Normal

---

### Question 916
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Criteria
Difficulty: Easy

Question: What is waiting time?
A) Execution time
B) Time spent in ready queue
C) I/O time
D) Total time

✔ Correct Answer: B

Reason: Waiting time is sum of time periods process spends waiting in ready queue before getting CPU.

Tag: Past Paper

---

### Question 917
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Criteria
Difficulty: Easy

Question: What is response time?
A) Total time
B) Time from request to first response
C) Execution time
D) Waiting time

✔ Correct Answer: B

Reason: Response time measures time from request submission until first response produced, critical for interactive systems.

Tag: Normal

---

### Question 918
Domain: Operating Systems
Topic: Thread Management
Subtopic: Multithreading Benefits
Difficulty: Easy

Question: What is a benefit of multithreading?
A) More memory usage
B) Responsiveness and resource sharing
C) Slower execution
D) More complexity only

✔ Correct Answer: B

Reason: Multithreading benefits include responsiveness (continue running if part blocked), resource sharing, and economy.

Tag: Normal

---

### Question 919
Domain: Operating Systems
Topic: Thread Management
Subtopic: Multithreading Models
Difficulty: Hard

Question: What is the many-to-many model?
A) One-to-one mapping
B) Many user threads to many kernel threads
C) Many-to-one mapping
D) No mapping

✔ Correct Answer: B

Reason: Many-to-many model multiplexes many user threads to smaller or equal number of kernel threads, flexible and efficient.

Tag: Normal

---

### Question 920
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Libraries
Difficulty: Medium

Question: What is a thread library?
A) Book collection
B) API for creating and managing threads
C) File library
D) No library

✔ Correct Answer: B

Reason: Thread library provides API for thread creation, synchronization, and management (POSIX Pthreads, Windows threads, Java threads).

Tag: Normal

---

### Question 921
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Race Condition
Difficulty: Medium

Question: What causes race conditions?
A) Single thread
B) Multiple threads accessing shared data without synchronization
C) Slow execution
D) No shared data

✔ Correct Answer: B

Reason: Race conditions occur when multiple threads access shared data concurrently without proper synchronization, causing unpredictable results.

Tag: Past Paper

---

### Question 922
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Critical Section Problem
Difficulty: Medium

Question: What is mutual exclusion requirement?
A) All processes enter together
B) Only one process in critical section at a time
C) No processes enter
D) Random entry

✔ Correct Answer: B

Reason: Mutual exclusion ensures at most one process executes in critical section at any time, preventing race conditions.

Tag: Past Paper

---

### Question 923
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphore Operations
Difficulty: Medium

Question: What does wait() operation do on semaphore?
A) Increments value
B) Decrements value, blocks if negative
C) No change
D) Resets value

✔ Correct Answer: B

Reason: wait() (P operation) decrements semaphore; if result negative, process blocks until semaphore becomes positive.

Tag: Past Paper

---

### Question 924
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphore Operations
Difficulty: Medium

Question: What does signal() operation do on semaphore?
A) Decrements value
B) Increments value, wakes waiting process
C) Blocks process
D) No change

✔ Correct Answer: B

Reason: signal() (V operation) increments semaphore; if processes waiting, one is awakened to continue execution.

Tag: Normal

---

### Question 925
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Classical Problems
Difficulty: Hard

Question: What is the bounded buffer problem?
A) Unlimited buffer
B) Producer-consumer with fixed-size buffer
C) No buffer
D) Variable buffer

✔ Correct Answer: B

Reason: Bounded buffer problem involves producer and consumer sharing fixed-size buffer, requiring synchronization to prevent overflow/underflow.

Tag: Past Paper

---

### Question 926
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Conditions
Difficulty: Easy

Question: What is mutual exclusion condition for deadlock?
A) Shared resources
B) At least one resource must be non-shareable
C) All resources shareable
D) No resources

✔ Correct Answer: B

Reason: Mutual exclusion means at least one resource must be held in non-shareable mode for deadlock to occur.

Tag: Past Paper

---

### Question 927
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Conditions
Difficulty: Easy

Question: What is hold and wait condition?
A) Release all resources
B) Process holds resources while waiting for more
C) No holding
D) No waiting

✔ Correct Answer: B

Reason: Hold and wait means process holds at least one resource while waiting to acquire additional resources.

Tag: Past Paper

---

### Question 928
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Conditions
Difficulty: Easy

Question: What is no preemption condition?
A) Resources can be preempted
B) Resources cannot be forcibly taken
C) All resources preemptible
D) No resources

✔ Correct Answer: B

Reason: No preemption means resources cannot be forcibly removed from process; must be voluntarily released.

Tag: Normal

---

### Question 929
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Conditions
Difficulty: Medium

Question: What is circular wait condition?
A) Linear wait
B) Circular chain of processes waiting for resources
C) No waiting
D) Random wait

✔ Correct Answer: B

Reason: Circular wait forms closed chain where each process waits for resource held by next process in chain.

Tag: Past Paper

---

### Question 930
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Handling
Difficulty: Medium

Question: What are the three approaches to handle deadlocks?
A) Only prevention
B) Prevention, avoidance, detection and recovery
C) Only detection
D) Ignore only

✔ Correct Answer: B

Reason: Deadlock handling approaches: prevention (eliminate conditions), avoidance (safe state), detection and recovery (detect and break).

Tag: Normal

---

### Question 931
Domain: Operating Systems
Topic: Memory Management
Subtopic: Address Binding
Difficulty: Medium

Question: What is address binding?
A) No binding
B) Mapping symbolic addresses to physical addresses
C) Random mapping
D) No mapping

✔ Correct Answer: B

Reason: Address binding maps program addresses (symbolic, relocatable, absolute) to physical memory addresses.

Tag: Normal

---

### Question 932
Domain: Operating Systems
Topic: Memory Management
Subtopic: Logical vs Physical Address
Difficulty: Easy

Question: What is logical address?
A) Physical location
B) Address generated by CPU
C) Disk address
D) Network address

✔ Correct Answer: B

Reason: Logical (virtual) address is generated by CPU during program execution, translated to physical address by MMU.

Tag: Past Paper

---

### Question 933
Domain: Operating Systems
Topic: Memory Management
Subtopic: Logical vs Physical Address
Difficulty: Easy

Question: What is physical address?
A) CPU address
B) Actual memory hardware location
C) Virtual address
D) Logical address

✔ Correct Answer: B

Reason: Physical address is actual location in memory hardware where data resides, accessed by memory unit.

Tag: Normal

---

### Question 934
Domain: Operating Systems
Topic: Memory Management
Subtopic: Contiguous Allocation
Difficulty: Medium

Question: What is contiguous memory allocation?
A) Scattered allocation
B) Each process occupies single contiguous memory block
C) Random allocation
D) No allocation

✔ Correct Answer: B

Reason: Contiguous allocation assigns each process single continuous block of memory, simple but causes fragmentation.

Tag: Normal

---

### Question 935
Domain: Operating Systems
Topic: Memory Management
Subtopic: Paging
Difficulty: Easy

Question: What is paging?
A) Contiguous allocation
B) Dividing memory into fixed-size pages
C) Variable allocation
D) No division

✔ Correct Answer: B

Reason: Paging divides physical memory into fixed-size frames and logical memory into same-size pages, eliminating external fragmentation.

Tag: Past Paper

---

### Question 936
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Table
Difficulty: Medium

Question: What is page table?
A: Process table
B) Data structure mapping logical pages to physical frames
C) File table
D) Network table

✔ Correct Answer: B

Reason: Page table maintains mapping between logical page numbers and physical frame numbers for address translation.

Tag: Normal

---

### Question 937
Domain: Operating Systems
Topic: Memory Management
Subtopic: TLB
Difficulty: Hard

Question: What is TLB?
A) Table Lookup Buffer
B) Translation Lookaside Buffer - cache for page table entries
C) Total Logic Buffer
D) No buffer

✔ Correct Answer: B

Reason: TLB is fast associative cache storing recent page table entries for quick address translation without memory access.

Tag: Past Paper

---

### Question 938
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation
Difficulty: Medium

Question: What is segmentation?
A) Fixed-size division
B) Variable-size logical division based on program structure
C) No division
D) Page-based

✔ Correct Answer: B

Reason: Segmentation divides memory into variable-size segments based on logical program structure (code, data, stack).

Tag: Past Paper

---

### Question 939
Domain: Operating Systems
Topic: Memory Management
Subtopic: Virtual Memory
Difficulty: Easy

Question: What is virtual memory?
A) Physical RAM
B) Technique allowing execution of processes not entirely in memory
C) Cache memory
D) Disk storage

✔ Correct Answer: B

Reason: Virtual memory separates logical from physical memory, allowing programs larger than physical memory to execute.

Tag: Past Paper

---

### Question 940
Domain: Operating Systems
Topic: Memory Management
Subtopic: Demand Paging
Difficulty: Medium

Question: What is demand paging?
A) Load all pages
B) Load pages only when referenced
C) No paging
D) Pre-load all

✔ Correct Answer: B

Reason: Demand paging loads pages into memory only when accessed, reducing initial load time and memory usage.

Tag: Past Paper

---

### Question 941
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault
Difficulty: Easy

Question: What is page fault?
A) Hardware failure
B) Reference to page not in memory
C) Disk error
D) Program error

✔ Correct Answer: B

Reason: Page fault occurs when process references page not currently in physical memory, triggering OS to load it.

Tag: Past Paper

---

### Question 942
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Replacement
Difficulty: Medium

Question: When is page replacement needed?
A) Always
B) When page fault occurs and no free frames
C) Never
D) At startup

✔ Correct Answer: B

Reason: Page replacement selects victim page when page fault occurs but all frames are allocated.

Tag: Normal

---

### Question 943
Domain: Operating Systems
Topic: Memory Management
Subtopic: FIFO Page Replacement
Difficulty: Easy

Question: What is FIFO page replacement?
A) Replace newest
B) Replace oldest page in memory
C) Replace random
D) No replacement

✔ Correct Answer: B

Reason: FIFO replaces page that has been in memory longest, simple but may remove frequently used pages.

Tag: Past Paper

---

### Question 944
Domain: Operating Systems
Topic: Memory Management
Subtopic: LRU Page Replacement
Difficulty: Medium

Question: What is LRU page replacement?
A) Replace newest
B) Replace least recently used page
C) Replace random
D) Replace first

✔ Correct Answer: B

Reason: LRU replaces page unused for longest time, approximating optimal algorithm using past behavior.

Tag: Past Paper

---

### Question 945
Domain: Operating Systems
Topic: Memory Management
Subtopic: Thrashing
Difficulty: Medium

Question: What is thrashing?
A) Fast execution
B) Process spending more time paging than executing
C) Normal operation
D) Disk failure

✔ Correct Answer: B

Reason: Thrashing occurs when system spends most time swapping pages rather than executing, caused by insufficient memory.

Tag: Past Paper

---

### Question 946
Domain: Operating Systems
Topic: File System Management
Subtopic: File Concept
Difficulty: Easy

Question: What is a file?
A) Process
B) Named collection of related information
C) Memory location
D) CPU register

✔ Correct Answer: B

Reason: File is named collection of related information stored on secondary storage, representing programs or data.

Tag: Past Paper

---

### Question 947
Domain: Operating Systems
Topic: File System Management
Subtopic: File Operations
Difficulty: Easy

Question: Which is a basic file operation?
A) Compile
B) Create, read, write, delete
C) Execute
D) Debug

✔ Correct Answer: B

Reason: Basic file operations include create, delete, open, close, read, write, append, seek, and get/set attributes.

Tag: Normal

---

### Question 948
Domain: Operating Systems
Topic: File System Management
Subtopic: File Access Methods
Difficulty: Medium

Question: What is sequential access?
A) Random access
B) Records accessed in order from beginning
C) No access
D) Parallel access

✔ Correct Answer: B

Reason: Sequential access processes records in order from beginning to end, suitable for tape drives and batch processing.

Tag: Past Paper

---

### Question 949
Domain: Operating Systems
Topic: File System Management
Subtopic: File Access Methods
Difficulty: Medium

Question: What is direct access?
A) Sequential only
B) Access any record directly without reading previous
C) No access
D) Ordered only

✔ Correct Answer: B

Reason: Direct (random) access allows reading/writing records in any order without accessing previous records.

Tag: Normal

---

### Question 950
Domain: Operating Systems
Topic: File System Management
Subtopic: Directory Structure
Difficulty: Easy

Question: What is a directory?
A) Data file
B) Container organizing files and subdirectories
C) Process
D) Memory

✔ Correct Answer: B

Reason: Directory is special file containing information about files and subdirectories, organizing file system hierarchically.

Tag: Normal

---

### Question 951
Domain: Operating Systems
Topic: File System Management
Subtopic: File Allocation Methods
Difficulty: Medium

Question: What is contiguous file allocation?
A) Scattered blocks
B) Each file occupies consecutive disk blocks
C) Random allocation
D) No allocation

✔ Correct Answer: B

Reason: Contiguous allocation stores each file in consecutive disk blocks, providing fast sequential access but causing fragmentation.

Tag: Past Paper

---

### Question 952
Domain: Operating Systems
Topic: File System Management
Subtopic: File Allocation Methods
Difficulty: Medium

Question: What is linked allocation?
A) Contiguous blocks
B) Each block contains pointer to next block
C) Random blocks
D) No blocks

✔ Correct Answer: B

Reason: Linked allocation stores files as linked list of disk blocks, each containing pointer to next, eliminating external fragmentation.

Tag: Normal

---

### Question 953
Domain: Operating Systems
Topic: File System Management
Subtopic: File Allocation Methods
Difficulty: Hard

Question: What is indexed allocation?
A) No index
B) Index block contains pointers to all file blocks
C) Sequential allocation
D) Random allocation

✔ Correct Answer: B

Reason: Indexed allocation uses index block containing pointers to all blocks of file, supporting random access.

Tag: Past Paper

---

### Question 954
Domain: Operating Systems
Topic: File System Management
Subtopic: Free Space Management
Difficulty: Medium

Question: What is bitmap for free space management?
A) Image file
B) Bit array where each bit represents block status
C) Text file
D) Process list

✔ Correct Answer: B

Reason: Bitmap uses one bit per block (0=free, 1=allocated), providing efficient space management.

Tag: Normal

---

### Question 955
Domain: Operating Systems
Topic: File System Management
Subtopic: Free Space Management
Difficulty: Medium

Question: What is free list?
A) File list
B) Linked list of free disk blocks
C) Process list
D) User list

✔ Correct Answer: B

Reason: Free list maintains linked list of all free disk blocks, simple but requires traversal.

Tag: Normal

---

### Question 956
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Structure
Difficulty: Easy

Question: What is a disk sector?
A) Disk region
B) Smallest addressable unit on disk
C) Disk type
D) Disk speed

✔ Correct Answer: B

Reason: Sector is smallest addressable unit on disk, typically 512 bytes or 4KB, forming basic unit of disk I/O.

Tag: Normal

---

### Question 957
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Structure
Difficulty: Easy

Question: What is a disk track?
A) Disk path
B) Concentric circle on disk platter
C) Disk speed
D) Disk type

✔ Correct Answer: B

Reason: Track is concentric circle on disk platter where data is stored, with multiple tracks on each platter surface.

Tag: Normal

---

### Question 958
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Scheduling
Difficulty: Easy

Question: What is disk scheduling?
A) Process scheduling
B) Determining order of disk I/O requests
C) Memory scheduling
D) Network scheduling

✔ Correct Answer: B

Reason: Disk scheduling algorithms determine order in which pending disk I/O requests are serviced to minimize seek time.

Tag: Past Paper

---

### Question 959
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: FCFS Disk Scheduling
Difficulty: Easy

Question: What does FCFS disk scheduling do?
A) Shortest seek first
B) Serves requests in arrival order
C) Random service
D) No scheduling

✔ Correct Answer: B

Reason: FCFS services disk requests in order they arrive, simple and fair but may not minimize seek time.

Tag: Normal

---

### Question 960
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSTF Disk Scheduling
Difficulty: Medium

Question: What does SSTF stand for?
A) Shortest Service Time First
B) Shortest Seek Time First
C) Standard Seek Time First
D) Slowest Seek Time First

✔ Correct Answer: B

Reason: SSTF selects request with minimum seek time from current head position, reducing average seek time.

Tag: Past Paper

---

### Question 961
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SCAN Disk Scheduling
Difficulty: Medium

Question: How does SCAN disk scheduling work?
A) Random movement
B) Head moves in one direction servicing requests, then reverses
C) No movement
D) Circular movement

✔ Correct Answer: B

Reason: SCAN (elevator algorithm) moves disk arm in one direction servicing requests until reaching end, then reverses.

Tag: Normal

---

### Question 962
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID
Difficulty: Hard

Question: What does RAID stand for?
A) Random Array of Independent Disks
B) Redundant Array of Independent Disks
C) Rapid Access of Internal Data
D) Remote Array of Integrated Disks

✔ Correct Answer: B

Reason: RAID combines multiple disks for improved performance, reliability, or both through various configurations.

Tag: Past Paper

---

### Question 963
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Levels
Difficulty: Hard

Question: What does RAID 0 provide?
A) Mirroring
B) Striping without redundancy
C) Parity
D) Full redundancy

✔ Correct Answer: B

Reason: RAID 0 stripes data across multiple disks for improved performance but provides no redundancy.

Tag: Normal

---

### Question 964
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Levels
Difficulty: Hard

Question: What does RAID 1 provide?
A) Striping
B) Mirroring for redundancy
C) Parity
D) No redundancy

✔ Correct Answer: B

Reason: RAID 1 mirrors data across two disks, providing full redundancy and fault tolerance.

Tag: Normal

---

### Question 965
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Hardware
Difficulty: Easy

Question: What is a device controller?
A) User interface
B) Hardware managing I/O device operations
C) Software driver
D) Memory controller

✔ Correct Answer: B

Reason: Device controller is hardware that manages I/O device operations, containing registers for CPU communication.

Tag: Normal

---

### Question 966
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Device Drivers
Difficulty: Easy

Question: What is a device driver?
A) Hardware component
B) Software interface between OS and hardware device
C) User application
D) File system

✔ Correct Answer: B

Reason: Device driver is software providing standard interface between OS and hardware devices, translating generic commands.

Tag: Normal

---

### Question 967
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Methods
Difficulty: Medium

Question: What is programmed I/O?
A) Automatic I/O
B) CPU actively polls device status
C) DMA-based I/O
D) No I/O

✔ Correct Answer: B

Reason: Programmed I/O has CPU continuously check device status (polling) and transfer data, simple but wastes CPU cycles.

Tag: Normal

---

### Question 968
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Methods
Difficulty: Medium

Question: What is interrupt-driven I/O?
A) CPU polls continuously
B) Device signals CPU when ready via interrupt
C) No interrupts
D) Manual I/O

✔ Correct Answer: B

Reason: Interrupt-driven I/O allows CPU to do other work; device sends interrupt when ready, improving CPU utilization.

Tag: Past Paper

---

### Question 969
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: DMA
Difficulty: Hard

Question: What does DMA stand for?
A) Direct Memory Allocation
B) Direct Memory Access
C) Dynamic Memory Access
D) Direct Module Access

✔ Correct Answer: B

Reason: DMA allows devices to transfer data directly to/from memory without CPU intervention, freeing CPU.

Tag: Past Paper

---

### Question 970
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Buffering
Difficulty: Medium

Question: What is I/O buffering?
A) Deleting data
B) Temporary storage area for data transfer
C) Permanent storage
D) No storage

✔ Correct Answer: B

Reason: Buffering uses temporary storage to hold data during transfer between devices with different speeds.

Tag: Normal

---

### Question 971
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Spooling
Difficulty: Medium

Question: What is spooling?
A) Printing directly
B) Queuing output for device serving one request at a time
C) Deleting files
D) No queuing

✔ Correct Answer: B

Reason: Spooling queues jobs for devices like printers, allowing multiple processes to generate output concurrently.

Tag: Normal

---

### Question 972
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Goals
Difficulty: Easy

Question: What are the three main security goals?
A) Speed, Size, Storage
B) Confidentiality, Integrity, Availability
C) Cost, Quality, Time
D) Input, Process, Output

✔ Correct Answer: B

Reason: CIA triad: Confidentiality (prevent unauthorized disclosure), Integrity (prevent unauthorized modification), Availability (ensure authorized access).

Tag: Past Paper

---

### Question 973
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Authentication
Difficulty: Easy

Question: What is authentication?
A) Granting permissions
B) Verifying user identity
C) Encrypting data
D) Deleting users

✔ Correct Answer: B

Reason: Authentication verifies identity of user or process, typically using passwords, biometrics, or tokens.

Tag: Normal

---

### Question 974
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Authorization
Difficulty: Easy

Question: What is authorization?
A) Verifying identity
B) Determining what authenticated user can access
C) Creating users
D) Deleting permissions

✔ Correct Answer: B

Reason: Authorization determines what resources and operations authenticated user is permitted to access.

Tag: Normal

---

### Question 975
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control
Difficulty: Medium

Question: What is access control?
A) No control
B) Mechanisms restricting access to resources
C) Full access
D) Random access

✔ Correct Answer: B

Reason: Access control mechanisms restrict access to system resources based on user identity and permissions.

Tag: Normal

---

### Question 976
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Encryption
Difficulty: Medium

Question: What is encryption?
A) Deleting data
B) Transforming data to unreadable form
C) Compressing data
D) Copying data

✔ Correct Answer: B

Reason: Encryption transforms data into unreadable ciphertext using algorithm and key, protecting confidentiality.

Tag: Normal

---

### Question 977
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Firewall
Difficulty: Medium

Question: What is a firewall?
A) Physical barrier
B) System controlling network traffic based on rules
C) Antivirus software
D) Backup system

✔ Correct Answer: B

Reason: Firewall monitors and controls incoming/outgoing network traffic based on security rules, protecting against unauthorized access.

Tag: Normal

---

### Question 978
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Virus
Difficulty: Easy

Question: What is a computer virus?
A) Hardware problem
B) Self-replicating code spreading by modifying programs
C) Network issue
D) User error

✔ Correct Answer: B

Reason: Virus is malicious code that replicates by inserting copies into other programs or files.

Tag: Past Paper

---

### Question 979
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Worm
Difficulty: Medium

Question: What is a worm?
A) Virus variant
B) Self-replicating program spreading through network
C) Hardware bug
D) Software bug

✔ Correct Answer: B

Reason: Worm is self-contained program that replicates and spreads through networks without needing host program.

Tag: Normal

---

### Question 980
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Trojan Horse
Difficulty: Medium

Question: What is a trojan horse?
A) Virus type
B) Program appearing useful but containing malicious code
C) Network attack
D) Hardware failure

✔ Correct Answer: B

Reason: Trojan horse is program appearing legitimate but containing hidden malicious functionality.

Tag: Normal

---

### Question 981
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Operating System Functions
Difficulty: Easy

Question: Which is a primary function of operating system?
A) Compile programs
B) Resource management and process coordination
C) Create documents
D) Browse internet

✔ Correct Answer: B

Reason: Primary OS functions include resource management (CPU, memory, I/O), process coordination, and providing user interface.

Tag: Normal

---

### Question 982
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Operating System Goals
Difficulty: Medium

Question: What are the two main goals of operating systems?
A) Speed and size
B) Convenience for users and efficient resource utilization
C) Cost and quality
D) Security only

✔ Correct Answer: B

Reason: OS goals are user convenience (ease of use, good performance) and efficient resource utilization (maximize throughput, minimize waste).

Tag: Normal

---

### Question 983
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls
Difficulty: Easy

Question: What is a system call?
A) Function call
B) Interface between process and operating system
C) Hardware interrupt
D) Network protocol

✔ Correct Answer: B

Reason: System call provides programmatic interface for processes to request services from operating system kernel.

Tag: Past Paper

---

### Question 984
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Definition
Difficulty: Easy

Question: What is a process?
A) Program on disk
B) Program in execution
C) Compiled program
D) Text file

✔ Correct Answer: B

Reason: Process is active entity representing program in execution, including program counter, registers, and memory contents.

Tag: Past Paper

---

### Question 985
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Control Block
Difficulty: Medium

Question: What information does PCB contain?
A) Only program code
B) Process state, program counter, CPU registers, scheduling info
C) Only memory addresses
D) User interface data

✔ Correct Answer: B

Reason: PCB contains all information about process: state, program counter, registers, memory limits, open files, scheduling data.

Tag: Normal

---

### Question 986
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Algorithms
Difficulty: Easy

Question: What does FCFS stand for?
A) Fast CPU First Scheduled
B) First Come First Served
C) Final Check First System
D) First Created First Started

✔ Correct Answer: B

Reason: FCFS is simplest scheduling algorithm where processes are executed in order they arrive in ready queue.

Tag: Past Paper

---

### Question 987
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Algorithms
Difficulty: Medium

Question: What does SJF stand for?
A) Slow Job First
B) Shortest Job First
C) System Job First
D) Single Job First

✔ Correct Answer: B

Reason: SJF scheduling algorithm selects process with shortest CPU burst time, optimal for minimizing average waiting time.

Tag: Past Paper

---

### Question 988
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Algorithms
Difficulty: Easy

Question: What is Round Robin scheduling?
A) Random selection
B) Each process gets small time quantum in circular order
C) Priority-based
D) Shortest job first

✔ Correct Answer: B

Reason: Round Robin allocates small time quantum to each process in circular order, good for time-sharing systems.

Tag: Past Paper

---

### Question 989
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Definition
Difficulty: Easy

Question: What is a thread?
A) Separate process
B) Lightweight process or basic unit of CPU utilization
C) File system component
D) Memory unit

✔ Correct Answer: B

Reason: Thread is smallest unit of CPU utilization, consisting of thread ID, program counter, register set, and stack.

Tag: Past Paper

---

### Question 990
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Critical Section
Difficulty: Easy

Question: What is a critical section?
A) Important code
B) Code segment accessing shared resources
C) Error handling code
D) Initialization code

✔ Correct Answer: B

Reason: Critical section is code segment where shared resources are accessed, requiring mutual exclusion.

Tag: Past Paper

---

### Question 991
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphore
Difficulty: Medium

Question: What is a semaphore?
A) Hardware device
B) Synchronization tool using integer variable
C) Scheduling algorithm
D) Memory technique

✔ Correct Answer: B

Reason: Semaphore is integer variable accessed through atomic wait and signal operations for process synchronization.

Tag: Past Paper

---

### Question 992
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Definition
Difficulty: Easy

Question: What is a deadlock?
A) Fast process
B) Situation where processes wait indefinitely for resources
C) Scheduling algorithm
D) Memory technique

✔ Correct Answer: B

Reason: Deadlock is situation where set of processes are blocked, each waiting for resource held by another in the set.

Tag: Past Paper

---

### Question 993
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Management Unit
Difficulty: Medium

Question: What does MMU stand for?
A) Multiple Memory Usage
B) Memory Management Unit
C) Main Memory Unit
D) Manual Memory Update

✔ Correct Answer: B

Reason: MMU is hardware device that translates logical addresses to physical addresses at runtime.

Tag: Past Paper

---

### Question 994
Domain: Operating Systems
Topic: Memory Management
Subtopic: Fragmentation
Difficulty: Easy

Question: What is internal fragmentation?
A) Wasted space outside partitions
B) Wasted space within allocated partition
C) No fragmentation
D) Disk fragmentation

✔ Correct Answer: B

Reason: Internal fragmentation is unused memory within allocated partition when partition is larger than needed.

Tag: Past Paper

---

### Question 995
Domain: Operating Systems
Topic: Memory Management
Subtopic: Fragmentation
Difficulty: Easy

Question: What is external fragmentation?
A) Wasted space within partitions
B) Free memory scattered in small blocks
C) No fragmentation
D) Internal waste

✔ Correct Answer: B

Reason: External fragmentation occurs when free memory is broken into small scattered blocks, total sufficient but not contiguous.

Tag: Past Paper

---

### Question 996
Domain: Operating Systems
Topic: File System Management
Subtopic: File Attributes
Difficulty: Easy

Question: Which is typically a file attribute?
A) CPU speed
B) Name, size, type, permissions, timestamps
C) Network speed
D) Memory size

✔ Correct Answer: B

Reason: File attributes include name, type, size, location, protection, creation time, modification time, and owner.

Tag: Normal

---

### Question 997
Domain: Operating Systems
Topic: File System Management
Subtopic: File Protection
Difficulty: Easy

Question: What are the basic file access permissions in UNIX?
A) Create, Delete, Modify
B) Read, Write, Execute
C) Open, Close, Save
D) Copy, Move, Rename

✔ Correct Answer: B

Reason: UNIX file permissions are Read (r), Write (w), and Execute (x), applied to owner, group, and others.

Tag: Past Paper

---

### Question 998
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Performance
Difficulty: Easy

Question: What is seek time?
A) Data transfer time
B) Time to move disk head to track
C) Rotation time
D) Total access time

✔ Correct Answer: B

Reason: Seek time is time required to move disk read/write head to desired track, major component of disk access time.

Tag: Normal

---

### Question 999
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Scheduling
Difficulty: Medium

Question: Why is I/O scheduling needed?
A) Not needed
B) To order I/O requests for efficiency and fairness
C) To delete requests
D) To create requests

✔ Correct Answer: B

Reason: I/O scheduling orders pending I/O requests to improve system performance, reduce wait times, and ensure fairness.

Tag: Normal

---

### Question 1000
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Principles
Difficulty: Medium

Question: What is the principle of defense in depth?
A) Single security layer
B) Multiple overlapping security mechanisms
C) No security
D) Single point of failure

✔ Correct Answer: B

Reason: Defense in depth uses multiple overlapping security layers so if one mechanism fails, others still provide protection against attacks.

Tag: Normal

---

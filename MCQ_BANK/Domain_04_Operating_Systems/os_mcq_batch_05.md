# Operating Systems - MCQ Batch 05
## Questions 401-500

---

### Question 401
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Kernel Mode vs User Mode
Difficulty: Easy

Question: What is kernel mode?
A) User application mode
B) Privileged mode with full hardware access
C) Network mode
D) Graphics mode

✔ Correct Answer: B

Reason: Kernel mode (supervisor/privileged mode) allows unrestricted access to all hardware and system resources, used by OS kernel.

Tag: Past Paper

---

### Question 402
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Kernel Mode vs User Mode
Difficulty: Easy

Question: What is user mode?
A) Kernel mode
B) Restricted mode for user applications
C) Administrator mode
D) Root mode

✔ Correct Answer: B

Reason: User mode is restricted execution mode where applications run with limited access to hardware, requiring system calls for privileged operations.

Tag: Normal

---

### Question 403
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Mode Switching
Difficulty: Medium

Question: When does mode switch from user to kernel occur?
A) Never
B) System call, interrupt, or exception
C) Randomly
D) Only at boot

✔ Correct Answer: B

Reason: Mode switch to kernel occurs on system calls (explicit), interrupts (hardware events), or exceptions (errors like divide by zero).

Tag: Normal

---

### Question 404
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Dual-Mode Operation
Difficulty: Medium

Question: Why is dual-mode operation necessary?
A) Faster execution
B) Protect OS and users from malicious/erroneous programs
C) Reduce memory usage
D) Improve graphics

✔ Correct Answer: B

Reason: Dual-mode operation protects system by preventing user programs from executing privileged instructions or accessing protected memory.

Tag: Past Paper

---

### Question 405
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Virtualization
Difficulty: Medium

Question: What is virtualization?
A) Virtual reality
B) Running multiple OS instances on single hardware
C) Cloud storage
D) Network simulation

✔ Correct Answer: B

Reason: Virtualization creates virtual machines allowing multiple operating systems to run concurrently on single physical hardware.

Tag: Normal

---

### Question 406
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Hypervisor
Difficulty: Hard

Question: What is a hypervisor?
A) User application
B) Software managing virtual machines
C) File system
D) Network protocol

✔ Correct Answer: B

Reason: Hypervisor (Virtual Machine Monitor) manages virtual machines, allocating hardware resources and isolating guest operating systems.

Tag: Normal

---

### Question 407
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Type 1 vs Type 2 Hypervisor
Difficulty: Hard

Question: How does Type 1 hypervisor differ from Type 2?
A) No difference
B) Type 1 runs on bare metal, Type 2 runs on host OS
C) Type 1 is slower
D) Type 2 is obsolete

✔ Correct Answer: B

Reason: Type 1 (bare-metal) hypervisor runs directly on hardware; Type 2 (hosted) runs on top of host operating system.

Tag: Normal

---

### Question 408
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Boot
Difficulty: Medium

Question: What is the bootstrap program?
A) User application
B) Initial program loading OS kernel
C) File manager
D) Text editor

✔ Correct Answer: B

Reason: Bootstrap program (bootloader) is first program run at startup, initializing system and loading OS kernel into memory.

Tag: Normal

---

### Question 409
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: BIOS vs UEFI
Difficulty: Medium

Question: What is UEFI?
A) Old BIOS
B) Modern firmware interface replacing BIOS
C) Operating system
D) File system

✔ Correct Answer: B

Reason: UEFI (Unified Extensible Firmware Interface) is modern firmware standard replacing BIOS, providing faster boot and better security.

Tag: Normal

---

### Question 410
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Libraries
Difficulty: Easy

Question: What are system libraries?
A) Book collections
B) Collections of functions for common operations
C) Hardware components
D) Network protocols

✔ Correct Answer: B

Reason: System libraries (like libc) provide standard functions for common operations, simplifying application development.

Tag: Normal

---

### Question 411
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling Algorithms
Difficulty: Medium

Question: Which scheduling algorithm can cause starvation?
A) Round Robin
B) Priority scheduling without aging
C) FCFS
D) Round Robin with time quantum

✔ Correct Answer: B

Reason: Priority scheduling without aging can starve low-priority processes if high-priority processes continuously arrive.

Tag: Normal

---

### Question 412
Domain: Operating Systems
Topic: Process Management
Subtopic: Cooperative Multitasking
Difficulty: Medium

Question: What is cooperative multitasking?
A) Preemptive scheduling
B) Processes voluntarily yield CPU
C) Forced scheduling
D) No multitasking

✔ Correct Answer: B

Reason: Cooperative multitasking relies on processes voluntarily yielding CPU control, problematic if process doesn't cooperate.

Tag: Normal

---

### Question 413
Domain: Operating Systems
Topic: Process Management
Subtopic: Preemptive Multitasking
Difficulty: Easy

Question: What is preemptive multitasking?
A) Voluntary yielding
B) OS forcibly switches between processes
C) No switching
D) Manual switching

✔ Correct Answer: B

Reason: Preemptive multitasking allows OS to interrupt running process and switch to another, ensuring fair CPU distribution.

Tag: Normal

---

### Question 414
Domain: Operating Systems
Topic: Process Management
Subtopic: Context Switch Overhead
Difficulty: Hard

Question: What contributes to context switch overhead?
A) No overhead
B) Saving/restoring registers, updating PCB, TLB flush
C) Only register save
D) Only PCB update

✔ Correct Answer: B

Reason: Context switch overhead includes saving/restoring CPU registers, updating PCB, switching address spaces, and TLB flush.

Tag: Normal

---

### Question 415
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Affinity
Difficulty: Hard

Question: What is processor affinity?
A) Random CPU assignment
B) Tendency to keep process on same CPU
C) No CPU preference
D) Always different CPU

✔ Correct Answer: B

Reason: Processor affinity keeps process running on same CPU to benefit from warm cache, improving performance on multiprocessor systems.

Tag: Normal

---

### Question 416
Domain: Operating Systems
Topic: Process Management
Subtopic: Load Balancing
Difficulty: Medium

Question: What is load balancing in multiprocessor systems?
A) Uneven distribution
B) Distributing processes evenly across CPUs
C) Single CPU usage
D) No distribution

✔ Correct Answer: B

Reason: Load balancing distributes processes across multiple CPUs to maximize utilization and minimize response time.

Tag: Normal

---

### Question 417
Domain: Operating Systems
Topic: Process Management
Subtopic: Symmetric Multiprocessing
Difficulty: Hard

Question: What is SMP?
A) Single processor
B) Multiple processors sharing memory, each running OS copy
C) Asymmetric processing
D) No multiprocessing

✔ Correct Answer: B

Reason: SMP (Symmetric Multiprocessing) has multiple processors sharing memory and I/O, each capable of running any process.

Tag: Normal

---

### Question 418
Domain: Operating Systems
Topic: Process Management
Subtopic: Asymmetric Multiprocessing
Difficulty: Hard

Question: What characterizes asymmetric multiprocessing?
A) All processors equal
B) Master processor controls system, others execute user code
C) No multiprocessing
D) Random assignment

✔ Correct Answer: B

Reason: Asymmetric multiprocessing has master processor handling system tasks and scheduling, while other processors execute user processes.

Tag: Normal

---

### Question 419
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: CPU Affinity Types
Difficulty: Hard

Question: What is soft affinity?
A) Strict CPU binding
B) OS tries to keep process on same CPU but may migrate
C) No affinity
D) Random assignment

✔ Correct Answer: B

Reason: Soft affinity is OS policy attempting to keep process on same CPU but allowing migration for load balancing.

Tag: Normal

---

### Question 420
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: CPU Affinity Types
Difficulty: Hard

Question: What is hard affinity?
A) Flexible assignment
B) Process explicitly bound to specific CPU(s)
C) No binding
D) Automatic assignment

✔ Correct Answer: B

Reason: Hard affinity allows process to specify subset of CPUs it can run on, preventing migration to other CPUs.

Tag: Normal

---

### Question 421
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multicore Processors
Difficulty: Medium

Question: What is a multicore processor?
A) Single core
B) Multiple processing cores on single chip
C) Multiple chips
D) No cores

✔ Correct Answer: B

Reason: Multicore processor integrates multiple processing cores on single chip, providing true parallel execution.

Tag: Normal

---

### Question 422
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Memory Stall
Difficulty: Hard

Question: What is a memory stall?
A) Memory failure
B) CPU waiting for data from memory
C) Memory overflow
D) No stall

✔ Correct Answer: B

Reason: Memory stall occurs when CPU must wait for data from memory due to cache miss, wasting cycles.

Tag: Normal

---

### Question 423
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multithreading on Multicore
Difficulty: Hard

Question: How does hardware multithreading help with memory stalls?
A) Prevents stalls
B) Switches to another thread during stall
C) Increases stalls
D) No effect

✔ Correct Answer: B

Reason: Hardware multithreading allows core to switch to another thread during memory stall, keeping core busy and improving throughput.

Tag: Normal

---

### Question 424
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Coarse-Grained Multithreading
Difficulty: Hard

Question: What is coarse-grained multithreading?
A) Fine switching
B: Thread switch only on long-latency events
C) Constant switching
D) No switching

✔ Correct Answer: B

Reason: Coarse-grained multithreading switches threads only on costly events like memory stalls, with high thread-switch overhead.

Tag: Normal

---

### Question 425
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Fine-Grained Multithreading
Difficulty: Hard

Question: What is fine-grained multithreading?
A) Rare switching
B) Thread switch at every instruction cycle
C) No switching
D) Manual switching

✔ Correct Answer: B

Reason: Fine-grained (interleaved) multithreading switches between threads at instruction level, requiring low-overhead thread switching.

Tag: Normal

---

### Question 426
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Synchronization Primitives
Difficulty: Medium

Question: What is a barrier in thread synchronization?
A) Physical barrier
B) Synchronization point where threads wait for all to arrive
C) Lock type
D) No function

✔ Correct Answer: B

Reason: Barrier is synchronization point where threads must wait until all threads reach barrier before any can proceed.

Tag: Normal

---

### Question 427
Domain: Operating Systems
Topic: Thread Management
Subtopic: Reader-Writer Locks
Difficulty: Hard

Question: What do reader-writer locks allow?
A) One reader only
B) Multiple readers or one writer
C) Multiple writers
D) No access

✔ Correct Answer: B

Reason: Reader-writer locks allow multiple concurrent readers or single exclusive writer, optimizing for read-heavy workloads.

Tag: Normal

---

### Question 428
Domain: Operating Systems
Topic: Thread Management
Subtopic: Deadlock in Threads
Difficulty: Medium

Question: Can threads deadlock?
A) No, only processes
B) Yes, when competing for shared resources
C) Never possible
D) Only in single-threaded programs

✔ Correct Answer: B

Reason: Threads can deadlock when competing for locks or resources, same conditions as process deadlock apply.

Tag: Normal

---

### Question 429
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Livelock
Difficulty: Hard

Question: What is livelock?
A) Deadlock variant
B: Processes actively changing state but making no progress
C) Normal operation
D) System crash

✔ Correct Answer: B

Reason: Livelock occurs when processes continuously change state in response to each other without making progress, like two people blocking each other's path.

Tag: Normal

---

### Question 430
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Starvation
Difficulty: Medium

Question: What is starvation in OS?
A) Memory shortage
B) Process indefinitely denied resources
C) CPU shortage
D) Disk full

✔ Correct Answer: B

Reason: Starvation occurs when process is perpetually denied necessary resources, often due to unfair scheduling or resource allocation.

Tag: Past Paper

---

### Question 431
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Busy Waiting
Difficulty: Easy

Question: What is busy waiting?
A) Sleeping
B) Continuously checking condition in loop
C) Blocking
D) No waiting

✔ Correct Answer: B

Reason: Busy waiting (spinning) continuously checks condition in tight loop, wasting CPU cycles but avoiding context switch overhead.

Tag: Normal

---

### Question 432
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Sleep and Wakeup
Difficulty: Medium

Question: What do sleep and wakeup primitives do?
A) Power management
B) Block process and wake it later
C) Delete process
D) Create process

✔ Correct Answer: B

Reason: Sleep blocks calling process, wakeup awakens sleeping process, providing basic synchronization without busy waiting.

Tag: Normal

---

### Question 433
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Producer-Consumer Variants
Difficulty: Hard

Question: What is the multiple producer-consumer problem?
A) Single producer and consumer
B) Multiple producers and consumers sharing buffer
C: No producers
D) No consumers

✔ Correct Answer: B

Reason: Multiple producer-consumer problem extends classic problem to multiple producers and consumers, requiring careful synchronization.

Tag: Normal

---

### Question 434
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Characterization
Difficulty: Medium

Question: Are all four conditions necessary for deadlock?
A) Only one needed
B) All four must hold simultaneously
C) Any three sufficient
D) No conditions needed

✔ Correct Answer: B

Reason: Deadlock occurs only when all four conditions (mutual exclusion, hold and wait, no preemption, circular wait) hold simultaneously.

Tag: Past Paper

---

### Question 435
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention Tradeoffs
Difficulty: Hard

Question: What is a drawback of deadlock prevention?
A) No drawbacks
B) May reduce resource utilization and system throughput
C: Always optimal
D) Increases performance

✔ Correct Answer: B

Reason: Deadlock prevention restricts resource requests, potentially reducing resource utilization, concurrency, and system throughput.

Tag: Normal

---

### Question 436
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Avoidance Limitations
Difficulty: Hard

Question: What limits practical use of Banker's Algorithm?
A: No limitations
B) Requires knowing maximum resource needs in advance
C) Too simple
D) Always works perfectly

✔ Correct Answer: B

Reason: Banker's Algorithm requires processes to declare maximum resource needs in advance, often impractical in dynamic systems.

Tag: Normal

---

### Question 437
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Detection Frequency
Difficulty: Hard

Question: How often should deadlock detection run?
A) Continuously
B) Tradeoff between overhead and detection delay
C) Never
D) Once at startup

✔ Correct Answer: B

Reason: Frequent detection increases overhead but reduces delay; infrequent detection reduces overhead but delays recovery.

Tag: Normal

---

### Question 438
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Victim Selection
Difficulty: Hard

Question: What factors affect victim selection in deadlock recovery?
A) Random selection
B) Process priority, computation time, resources held
C) Alphabetical order
D) No factors

✔ Correct Answer: B

Reason: Victim selection considers process priority, execution time, resources held/needed, and number of processes to terminate.

Tag: Normal

---

### Question 439
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Hierarchy
Difficulty: Easy

Question: What is the typical memory hierarchy from fastest to slowest?
A) Disk, RAM, Cache
B) Registers, Cache, RAM, Disk
C) RAM, Cache, Registers
D) Random order

✔ Correct Answer: B

Reason: Memory hierarchy: Registers (fastest, smallest) → Cache → RAM → Disk (slowest, largest), balancing speed, size, and cost.

Tag: Normal

---

### Question 440
Domain: Operating Systems
Topic: Memory Management
Subtopic: Cache Memory
Difficulty: Easy

Question: What is cache memory?
A) Disk storage
B) Fast memory between CPU and RAM
C) Virtual memory
D) Swap space

✔ Correct Answer: B

Reason: Cache is small, fast memory storing frequently accessed data, reducing average memory access time.

Tag: Normal

---

### Question 441
Domain: Operating Systems
Topic: Memory Management
Subtopic: Cache Levels
Difficulty: Medium

Question: What are L1, L2, L3 caches?
A) Same cache
B) Multiple cache levels with increasing size and latency
C) Disk types
D) RAM types

✔ Correct Answer: B

Reason: L1 (smallest, fastest) is per-core, L2 (medium) may be per-core or shared, L3 (largest, slower) is typically shared.

Tag: Normal

---

### Question 442
Domain: Operating Systems
Topic: Memory Management
Subtopic: Cache Hit Ratio
Difficulty: Medium

Question: What is cache hit ratio?
A) Cache size
B) Percentage of memory accesses found in cache
C) Cache speed
D) Cache cost

✔ Correct Answer: B

Reason: Cache hit ratio is percentage of memory references satisfied by cache, higher ratio means better performance.

Tag: Normal

---

### Question 443
Domain: Operating Systems
Topic: Memory Management
Subtopic: Spatial Locality
Difficulty: Medium

Question: What is spatial locality?
A) Random access
B) Tendency to access nearby memory locations
C) Temporal pattern
D) No pattern

✔ Correct Answer: B

Reason: Spatial locality means if location is referenced, nearby locations likely to be referenced soon (e.g., array traversal).

Tag: Normal

---

### Question 444
Domain: Operating Systems
Topic: Memory Management
Subtopic: Temporal Locality
Difficulty: Medium

Question: What is temporal locality?
A) Spatial pattern
B) Tendency to access same location repeatedly
C) Random access
D) No pattern

✔ Correct Answer: B

Reason: Temporal locality means recently accessed location likely to be accessed again soon (e.g., loop variables).

Tag: Normal

---

### Question 445
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Protection
Difficulty: Easy

Question: Why is memory protection important?
A) Not important
B) Prevents processes from accessing each other's memory
C) Increases speed
D) Reduces size

✔ Correct Answer: B

Reason: Memory protection prevents processes from reading/writing other processes' memory, ensuring isolation and security.

Tag: Past Paper

---

### Question 446
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation Fault
Difficulty: Easy

Question: What causes a segmentation fault?
A) Correct memory access
B) Accessing memory outside allowed segment
C) Fast execution
D) Normal operation

✔ Correct Answer: B

Reason: Segmentation fault occurs when process attempts to access memory outside its allocated segments, triggering protection violation.

Tag: Normal

---

### Question 447
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Overcommitment
Difficulty: Hard

Question: What is memory overcommitment?
A) Exact allocation
B) Allocating more virtual memory than physical memory available
C) Under allocation
D) No allocation

✔ Correct Answer: B

Reason: Memory overcommitment allows system to allocate more virtual memory than physical RAM, relying on not all being used simultaneously.

Tag: Normal

---

### Question 448
Domain: Operating Systems
Topic: Memory Management
Subtopic: OOM Killer
Difficulty: Hard

Question: What is the OOM (Out of Memory) killer?
A) Memory allocator
B) Mechanism terminating processes when memory exhausted
C) Memory manager
D) No function

✔ Correct Answer: B

Reason: OOM killer selects and terminates processes when system runs out of memory, preventing complete system failure.

Tag: Normal

---

### Question 449
Domain: Operating Systems
Topic: Memory Management
Subtopic: Huge Pages
Difficulty: Hard

Question: What are huge pages?
A) Small pages
B) Larger page sizes reducing TLB misses
C) Normal pages
D) No pages

✔ Correct Answer: B

Reason: Huge pages (2MB, 1GB) reduce page table size and TLB misses for large memory applications, improving performance.

Tag: Normal

---

### Question 450
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Coloring
Difficulty: Hard

Question: What is page coloring?
A) Visual feature
B) Technique to reduce cache conflicts
C) Page marking
D) No function

✔ Correct Answer: B

Reason: Page coloring assigns pages to minimize cache conflicts by considering cache organization, improving cache utilization.

Tag: Normal

---

### Question 451
Domain: Operating Systems
Topic: Memory Management
Subtopic: NUMA
Difficulty: Hard

Question: What is NUMA?
A) Uniform memory access
B) Non-Uniform Memory Access - varying access times
C) No memory access
D) Network memory

✔ Correct Answer: B

Reason: NUMA (Non-Uniform Memory Access) architecture has memory access time depending on memory location relative to processor.

Tag: Normal

---

### Question 452
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Bandwidth
Difficulty: Medium

Question: What is memory bandwidth?
A) Memory size
B) Rate of data transfer to/from memory
C) Memory speed
D) Memory cost

✔ Correct Answer: B

Reason: Memory bandwidth measures rate at which data can be read from or written to memory, critical for performance.

Tag: Normal

---

### Question 453
Domain: Operating Systems
Topic: Memory Management
Subtopic: Working Set Model
Difficulty: Hard

Question: How is working set size determined?
A) Random
B) Pages referenced in time window Δ
C) All pages
D) No determination

✔ Correct Answer: B

Reason: Working set is set of pages referenced in most recent Δ time units, approximating process's memory needs.

Tag: Normal

---

### Question 454
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault Rate
Difficulty: Medium

Question: What indicates thrashing?
A) Low page fault rate
B) Very high page fault rate
C) No page faults
D) Constant rate

✔ Correct Answer: B

Reason: Thrashing indicated by very high page fault rate where system spends more time paging than executing.

Tag: Normal

---

### Question 455
Domain: Operating Systems
Topic: Memory Management
Subtopic: Demand Segmentation
Difficulty: Hard

Question: What is demand segmentation?
A) Load all segments
B) Load segments only when referenced
C) No segmentation
D) Pre-load segments

✔ Correct Answer: B

Reason: Demand segmentation loads segments into memory only when referenced, similar to demand paging but with variable-size segments.

Tag: Normal

---

### Question 456
Domain: Operating Systems
Topic: File System Management
Subtopic: File Descriptors
Difficulty: Medium

Question: What happens when a file is opened?
A) File deleted
B) File descriptor returned, entry added to open file table
C) File closed
D) Nothing

✔ Correct Answer: B

Reason: Opening file creates entry in open file table and returns file descriptor for subsequent operations.

Tag: Normal

---

### Question 457
Domain: Operating Systems
Topic: File System Management
Subtopic: File Pointer
Difficulty: Easy

Question: What is a file pointer?
A) Memory pointer
B) Current position in file for read/write
C) File name
D) File size

✔ Correct Answer: B

Reason: File pointer (file offset) tracks current position in file for next read/write operation, maintained per open file.

Tag: Normal

---

### Question 458
Domain: Operating Systems
Topic: File System Management
Subtopic: File Seek
Difficulty: Easy

Question: What does seek operation do?
A) Searches file content
B) Repositions file pointer
C) Deletes file
D) Creates file

✔ Correct Answer: B

Reason: Seek operation repositions file pointer to specified location, enabling random access to file contents.

Tag: Normal

---

### Question 459
Domain: Operating Systems
Topic: File System Management
Subtopic: Append Mode
Difficulty: Easy

Question: What is append mode?
A) Overwrite mode
B) Writes always added at end of file
C) Read mode
D) Delete mode

✔ Correct Answer: B

Reason: Append mode automatically positions file pointer at end before each write, ensuring data is added without overwriting.

Tag: Normal

---

### Question 460
Domain: Operating Systems
Topic: File System Management
Subtopic: File Truncation
Difficulty: Medium

Question: What does file truncation do?
A) Extends file
B) Reduces file size, discarding content
C) Renames file
D) Copies file

✔ Correct Answer: B

Reason: Truncation reduces file to specified size (often zero), discarding content beyond new size while keeping file.

Tag: Normal

---

### Question 461
Domain: Operating Systems
Topic: File System Management
Subtopic: Directory Operations
Difficulty: Easy

Question: Which is a directory operation?
A) Compile
B) Create, delete, list, rename
C) Execute
D) Debug

✔ Correct Answer: B

Reason: Directory operations include create, delete, opendir, closedir, readdir, rename, and link.

Tag: Normal

---

### Question 462
Domain: Operating Systems
Topic: File System Management
Subtopic: Current Working Directory
Difficulty: Easy

Question: What is the current working directory?
A) Root directory
B) Directory where process is currently working
C) Home directory
D) System directory

✔ Correct Answer: B

Reason: Current working directory is directory from which relative paths are resolved for process.

Tag: Normal

---

### Question 463
Domain: Operating Systems
Topic: File System Management
Subtopic: Root Directory
Difficulty: Easy

Question: What is the root directory?
A) User directory
B) Top-level directory in file system hierarchy
C) Current directory
D) Temporary directory

✔ Correct Answer: B

Reason: Root directory is top of file system tree (/ in UNIX, C:\ in Windows), containing all other directories.

Tag: Normal

---

### Question 464
Domain: Operating Systems
Topic: File System Management
Subtopic: Absolute vs Relative Path
Difficulty: Easy

Question: What distinguishes absolute from relative path?
A) Length
B) Absolute starts from root, relative from current directory
C) Speed
D) No difference

✔ Correct Answer: B

Reason: Absolute path specifies complete path from root; relative path specifies path from current working directory.

Tag: Normal

---

### Question 465
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Consistency
Difficulty: Hard

Question: What can cause file system inconsistency?
A) Normal operation
B) System crash during write operations
C) Reading files
D) Listing directories

✔ Correct Answer: B

Reason: Crashes during metadata updates can leave file system in inconsistent state with orphaned blocks or incorrect link counts.

Tag: Normal

---

### Question 466
Domain: Operating Systems
Topic: File System Management
Subtopic: Superblock
Difficulty: Medium

Question: What is a superblock?
A) Large block
B) Metadata about file system structure
C) Data block
D) No function

✔ Correct Answer: B

Reason: Superblock contains critical file system metadata including size, block count, free block count, and inode information.

Tag: Normal

---

### Question 467
Domain: Operating Systems
Topic: File System Management
Subtopic: Inode Structure
Difficulty: Hard

Question: What does an inode NOT contain?
A) File size
B) File name
C) Permissions
D) Block pointers

✔ Correct Answer: B

Reason: Inode contains file metadata and block pointers but not filename; directory entries map names to inode numbers.

Tag: Normal

---

### Question 468
Domain: Operating Systems
Topic: File System Management
Subtopic: Direct vs Indirect Blocks
Difficulty: Hard

Question: Why use indirect blocks in inodes?
A) Slower access
B) Support large files beyond direct pointers
C) Waste space
D) No reason

✔ Correct Answer: B

Reason: Indirect blocks point to blocks containing more pointers, allowing inodes to reference large files beyond direct pointer capacity.

Tag: Normal

---

### Question 469
Domain: Operating Systems
Topic: File System Management
Subtopic: Triple Indirect Blocks
Difficulty: Hard

Question: How many levels of indirection in triple indirect block?
A) One
B) Three
C) Two
D) None

✔ Correct Answer: B

Reason: Triple indirect block points to block of double indirect pointers, which point to single indirect blocks, which point to data blocks.

Tag: Normal

---

### Question 470
Domain: Operating Systems
Topic: File System Management
Subtopic: File Holes
Difficulty: Hard

Question: What is a sparse file?
A) Small file
B) File with unallocated regions (holes)
C) Dense file
D) Compressed file

✔ Correct Answer: B

Reason: Sparse file contains holes (unallocated regions) that read as zeros, saving disk space for large files with gaps.

Tag: Normal

---

### Question 471
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Access Time
Difficulty: Medium

Question: What is total disk access time?
A) Seek time only
B) Seek time + rotational latency + transfer time
C) Transfer time only
D) Rotation time only

✔ Correct Answer: B

Reason: Total access time = seek time (head movement) + rotational latency (sector rotation) + transfer time (data transfer).

Tag: Past Paper

---

### Question 472
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Performance
Difficulty: Medium

Question: Which factor most affects disk performance?
A) Color
B) Seek time
C) Brand
D) Age

✔ Correct Answer: B

Reason: Seek time (mechanical head movement) is typically largest component of disk access time, most affecting performance.

Tag: Normal

---

### Question 473
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Scheduling Goals
Difficulty: Easy

Question: What is the goal of disk scheduling?
A) Increase seek time
B) Minimize seek time and maximize throughput
C) Random access
D) Slow down disk

✔ Correct Answer: B

Reason: Disk scheduling aims to minimize seek time, maximize throughput, and provide fair access to all requests.

Tag: Normal

---

### Question 474
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSTF Disadvantage
Difficulty: Medium

Question: What is a problem with SSTF scheduling?
A) Too slow
B) Can cause starvation of distant requests
C) Too complex
D) No problems

✔ Correct Answer: B

Reason: SSTF may starve requests far from current head position if nearby requests keep arriving.

Tag: Normal

---

### Question 475
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: C-LOOK
Difficulty: Hard

Question: How does C-LOOK differ from C-SCAN?
A) Same algorithm
B) Returns to beginning at last request, not disk end
C) Slower
D) No difference

✔ Correct Answer: B

Reason: C-LOOK is like C-SCAN but reverses at last request in direction rather than going to physical disk end.

Tag: Normal

---

### Question 476
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Arm Scheduling
Difficulty: Medium

Question: What does the disk arm do?
A) Rotates platter
B) Moves read/write head across tracks
C) Transfers data
D) Powers disk

✔ Correct Answer: B

Reason: Disk arm moves read/write head assembly radially across disk surface to access different tracks.

Tag: Normal

---

### Question 477
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Rotational Speed
Difficulty: Easy

Question: What is typical HDD rotational speed?
A) 100 RPM
B) 5400-15000 RPM
C) 50000 RPM
D) 1 RPM

✔ Correct Answer: B

Reason: HDDs typically rotate at 5400 RPM (laptops), 7200 RPM (desktops), or 10000-15000 RPM (servers).

Tag: Normal

---

### Question 478
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Architecture
Difficulty: Medium

Question: What are the basic storage units in SSDs?
A) Platters
B) Flash memory cells organized in pages and blocks
C) Tracks
D) Sectors

✔ Correct Answer: B

Reason: SSDs use flash memory organized in pages (4-16KB) for read/write and blocks (128-256 pages) for erase operations.

Tag: Normal

---

### Question 479
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD Wear Leveling
Difficulty: Hard

Question: What is wear leveling in SSDs?
A) Physical leveling
B) Distributing writes evenly to extend lifespan
C) Reading data
D) Deleting data

✔ Correct Answer: B

Reason: Wear leveling distributes write/erase cycles evenly across flash cells since they have limited write endurance.

Tag: Normal

---

### Question 480
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: TRIM Command
Difficulty: Hard

Question: What does TRIM command do for SSDs?
A) Reads data
B) Informs SSD which blocks are no longer in use
C) Writes data
D) Formats SSD

✔ Correct Answer: B

Reason: TRIM tells SSD which data blocks are no longer needed, allowing efficient garbage collection and maintaining performance.

Tag: Normal

---

### Question 481
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Write Amplification
Difficulty: Hard

Question: What is write amplification in SSDs?
A) Writing once
B) Physical writes exceeding logical writes
C) No amplification
D) Reading data

✔ Correct Answer: B

Reason: Write amplification occurs when SSD must write more data physically than logically requested due to erase-before-write requirement.

Tag: Normal

---

### Question 482
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Parity
Difficulty: Hard

Question: How does RAID 5 calculate parity?
A) No parity
B) XOR of data blocks
C) Mirroring
D) Addition

✔ Correct Answer: B

Reason: RAID 5 uses XOR operation on data blocks to calculate parity, allowing reconstruction of failed disk data.

Tag: Normal

---

### Question 483
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Rebuild
Difficulty: Medium

Question: What happens during RAID rebuild?
A) Nothing
B) Data reconstructed on replacement disk
C) All data lost
D: System shutdown

✔ Correct Answer: B

Reason: RAID rebuild reconstructs data on replacement disk using remaining disks and parity information.

Tag: Normal

---

### Question 484
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Storage Virtualization
Difficulty: Hard

Question: What is storage virtualization?
A) Virtual reality
B) Abstracting physical storage into logical pools
C) No virtualization
D) Disk deletion

✔ Correct Answer: B

Reason: Storage virtualization pools physical storage from multiple devices into logical units, simplifying management and improving utilization.

Tag: Normal

---

### Question 485
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Buses
Difficulty: Medium

Question: What is an I/O bus?
A) Vehicle
B) Communication pathway between CPU and I/O devices
C) Storage device
D) Network cable

✔ Correct Answer: B

Reason: I/O bus is shared communication pathway connecting CPU, memory, and I/O devices for data transfer.

Tag: Normal

---

### Question 486
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: PCI Express
Difficulty: Medium

Question: What is PCIe?
A) Old parallel bus
B) High-speed serial expansion bus standard
C) Network protocol
D) File system

✔ Correct Answer: B

Reason: PCIe (PCI Express) is high-speed serial bus standard for connecting peripherals, replacing older PCI.

Tag: Normal

---

### Question 487
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: USB
Difficulty: Easy

Question: What does USB stand for?
A) Universal System Bus
B) Universal Serial Bus
C) Unified Storage Bus
D) Ultra Speed Bus

✔ Correct Answer: B

Reason: USB (Universal Serial Bus) is standard for connecting peripherals, supporting hot-plugging and power delivery.

Tag: Normal

---

### Question 488
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Interrupt Priority
Difficulty: Medium

Question: Why have interrupt priorities?
A) No reason
B) Handle urgent interrupts before less critical ones
C) Slow down system
D: Random handling

✔ Correct Answer: B

Reason: Interrupt priorities ensure time-critical interrupts (e.g., hardware failures) are handled before less urgent ones.

Tag: Normal

---

### Question 489
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Interrupt Masking
Difficulty: Hard

Question: What is interrupt masking?
A) Hiding interrupts
B) Temporarily disabling certain interrupts
C) Enabling all interrupts
D) No function

✔ Correct Answer: B

Reason: Interrupt masking temporarily disables specific interrupts during critical sections to prevent race conditions.

Tag: Normal

---

### Question 490
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Request Lifecycle
Difficulty: Hard

Question: What is the typical I/O request lifecycle?
A) Random
B) Request → queue → device processing → interrupt → completion
C) Immediate completion
D) No lifecycle

✔ Correct Answer: B

Reason: I/O request is queued, scheduled, processed by device, signals completion via interrupt, then handled by OS.

Tag: Normal

---

### Question 491
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Authentication Methods
Difficulty: Easy

Question: What are the three main authentication factors?
A) Name, age, address
B) Something you know, have, are
C) Password only
D) Username only

✔ Correct Answer: B

Reason: Authentication factors: knowledge (password), possession (token), inherence (biometric), often combined for multi-factor authentication.

Tag: Normal

---

### Question 492
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Password Security
Difficulty: Medium

Question: Why salt passwords before hashing?
A) Improve taste
B) Prevent rainbow table attacks
C) Slow down system
D: No reason

✔ Correct Answer: B

Reason: Salt (random data) added before hashing prevents precomputed rainbow table attacks and ensures identical passwords have different hashes.

Tag: Normal

---

### Question 493
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Biometric Authentication
Difficulty: Medium

Question: What is a false positive in biometric authentication?
A) Correct rejection
B) Incorrectly accepting unauthorized user
C) Correct acceptance
D) System error

✔ Correct Answer: B

Reason: False positive (false acceptance) occurs when system incorrectly authenticates unauthorized user, security risk.

Tag: Normal

---

### Question 494
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Principle of Complete Mediation
Difficulty: Hard

Question: What does complete mediation require?
A) No checking
B) Every access checked against access control
C: Random checking
D) One-time checking

✔ Correct Answer: B

Reason: Complete mediation requires every access to every object be checked against access control mechanism, no caching of permissions.

Tag: Normal

---

### Question 495
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Principle of Open Design
Difficulty: Hard

Question: What does open design principle state?
A) Hide everything
B) Security should not depend on secrecy of design
C) Proprietary only
D) No design needed

✔ Correct Answer: B

Reason: Open design principle states security should rely on secrecy of keys, not algorithms, allowing public scrutiny to find flaws.

Tag: Normal

---

### Question 496
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Buffer Overflow
Difficulty: Medium

Question: What is a buffer overflow attack?
A) Disk overflow
B) Writing beyond buffer boundaries to execute malicious code
C) Memory shortage
D) Normal operation

✔ Correct Answer: B

Reason: Buffer overflow writes data beyond buffer boundaries, potentially overwriting return addresses to execute attacker's code.

Tag: Normal

---

### Question 497
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Stack Canaries
Difficulty: Hard

Question: What are stack canaries?
A) Birds
B) Values placed on stack to detect buffer overflows
C) Stack pointers
D: No function

✔ Correct Answer: B

Reason: Stack canaries are known values placed between buffer and control data; modification indicates buffer overflow attempt.

Tag: Normal

---

### Question 498
Domain: Operating Systems
Topic: Protection & Security
Subtopic: ASLR
Difficulty: Hard

Question: What does ASLR do?
A) Static addressing
B) Randomizes memory addresses to prevent exploits
C) Allocates memory
D) Deletes memory

✔ Correct Answer: B

Reason: ASLR (Address Space Layout Randomization) randomizes memory locations of executables, libraries, and stack, hindering exploit attempts.

Tag: Normal

---

### Question 499
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Sandboxing
Difficulty: Medium

Question: What is sandboxing?
A) Beach activity
B) Isolating programs in restricted environment
C) Disk partitioning
D) Network configuration

✔ Correct Answer: B

Reason: Sandboxing runs untrusted programs in isolated environment with restricted access to system resources, limiting damage from malicious code.

Tag: Normal

---

### Question 500
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Auditing
Difficulty: Medium

Question: What is security auditing?
A) Financial audit
B: Recording and analyzing system activities for security
C) Performance monitoring
D) Disk checking

✔ Correct Answer: B

Reason: Security auditing logs system activities (logins, file access, privilege changes) for analysis, compliance, and incident investigation.

Tag: Normal

---

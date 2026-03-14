# Operating Systems - MCQ Batch 03
## Questions 201-300

---

### Question 201
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling
Difficulty: Medium

Question: What is a process scheduler?
A) Hardware component
B) OS component selecting next process to run
C) User application
D) File manager

✔ Correct Answer: B

Reason: Process scheduler selects which process from ready queue should be allocated CPU next, implementing scheduling algorithms.

Tag: Normal

---

### Question 202
Domain: Operating Systems
Topic: Process Management
Subtopic: Dispatcher
Difficulty: Medium

Question: What does the dispatcher do?
A) Schedules processes
B) Gives control of CPU to selected process
C) Creates processes
D) Terminates processes

✔ Correct Answer: B

Reason: Dispatcher performs context switch, switches to user mode, and jumps to proper location in selected process to restart it.

Tag: Normal

---

### Question 203
Domain: Operating Systems
Topic: Process Management
Subtopic: Dispatch Latency
Difficulty: Hard

Question: What is dispatch latency?
A) Process execution time
B) Time to stop one process and start another
C) Waiting time
D) Turnaround time

✔ Correct Answer: B

Reason: Dispatch latency is the time taken by dispatcher to stop current process and start the next, should be minimized for efficiency.

Tag: Normal

---

### Question 204
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: CPU Burst
Difficulty: Easy

Question: What is a CPU burst?
A) CPU explosion
B) Period of CPU execution by a process
C) CPU speed
D) CPU cache

✔ Correct Answer: B

Reason: CPU burst is the amount of time a process uses the CPU before making I/O request or terminating.

Tag: Normal

---

### Question 205
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: I/O Burst
Difficulty: Easy

Question: What is an I/O burst?
A) I/O device failure
B) Period waiting for I/O operation completion
C) I/O speed
D) I/O cache

✔ Correct Answer: B

Reason: I/O burst is the time a process spends waiting for I/O operation to complete before resuming CPU execution.

Tag: Normal

---

### Question 206
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Preemptive Scheduling
Difficulty: Medium

Question: In preemptive priority scheduling, when does preemption occur?
A) Never
B) When higher priority process arrives
C) After process completes
D) Randomly

✔ Correct Answer: B

Reason: Preemptive priority scheduling interrupts running process when a higher priority process enters ready queue, ensuring urgent tasks execute promptly.

Tag: Normal

---

### Question 207
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Shortest Remaining Time First
Difficulty: Hard

Question: What is SRTF scheduling?
A) Non-preemptive SJF
B) Preemptive version of SJF
C) Round Robin variant
D) FCFS variant

✔ Correct Answer: B

Reason: SRTF (Shortest Remaining Time First) is preemptive SJF where process with shortest remaining CPU burst is selected, optimal for minimizing average waiting time.

Tag: Normal

---

### Question 208
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multilevel Queue
Difficulty: Hard

Question: In multilevel queue scheduling, can a process move between queues?
A) Yes, always
B) No, queues are fixed
C) Only upward
D) Only downward

✔ Correct Answer: B

Reason: In multilevel queue, processes are permanently assigned to queues based on properties; multilevel feedback queue allows movement.

Tag: Normal

---

### Question 209
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Benefits
Difficulty: Easy

Question: Which is a benefit of multithreading?
A) Increased memory usage
B) Improved responsiveness
C) Slower execution
D) More complex debugging

✔ Correct Answer: B

Reason: Multithreading improves responsiveness by allowing program to continue running even if part is blocked, enhancing user experience.

Tag: Normal

---

### Question 210
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Creation
Difficulty: Medium

Question: Which POSIX function creates a new thread?
A) thread_create()
B) pthread_create()
C) create_thread()
D) new_thread()

✔ Correct Answer: B

Reason: pthread_create() is the POSIX Pthreads function for creating new threads, taking thread attributes and start routine as parameters.

Tag: Past Paper

---

### Question 211
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Termination
Difficulty: Easy

Question: Which function terminates a thread in Pthreads?
A) pthread_exit()
B) thread_exit()
C) exit_thread()
D) terminate()

✔ Correct Answer: A

Reason: pthread_exit() terminates the calling thread, optionally returning a value to joining threads.

Tag: Normal

---

### Question 212
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Joining
Difficulty: Medium

Question: What does pthread_join() do?
A) Creates thread
B) Waits for specified thread to terminate
C) Deletes thread
D) Suspends thread

✔ Correct Answer: B

Reason: pthread_join() blocks calling thread until specified thread terminates, allowing synchronization and retrieval of exit status.

Tag: Normal

---

### Question 213
Domain: Operating Systems
Topic: Thread Management
Subtopic: Kernel Threads
Difficulty: Medium

Question: What is an advantage of kernel-level threads?
A) Faster creation
B) Better multiprocessor utilization
C) No kernel support needed
D) Simpler implementation

✔ Correct Answer: B

Reason: Kernel threads can be scheduled on different processors simultaneously, providing true parallelism on multiprocessor systems.

Tag: Normal

---

### Question 214
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Pools
Difficulty: Hard

Question: What is a thread pool?
A) Collection of data
B) Pre-created threads waiting for tasks
C) Memory pool
D) Process pool

✔ Correct Answer: B

Reason: Thread pool maintains multiple pre-created threads that wait for tasks, reducing overhead of thread creation/destruction for each request.

Tag: Normal

---

### Question 215
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Atomic Operations
Difficulty: Medium

Question: What is an atomic operation?
A) Small operation
B) Operation completing without interruption
C) Slow operation
D) Complex operation

✔ Correct Answer: B

Reason: Atomic operation executes completely without interruption, appearing instantaneous to other threads, essential for synchronization primitives.

Tag: Normal

---

### Question 216
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Test-and-Set
Difficulty: Hard

Question: What does test-and-set instruction do?
A) Tests only
B) Atomically reads and sets a value
C) Sets only
D) Deletes value

✔ Correct Answer: B

Reason: Test-and-set atomically reads current value and sets it to true, used to implement locks with hardware support for mutual exclusion.

Tag: Normal

---

### Question 217
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Compare-and-Swap
Difficulty: Hard

Question: What is compare-and-swap (CAS)?
A) Comparison only
B) Atomically compares and conditionally swaps values
C) Swap only
D) Delete operation

✔ Correct Answer: B

Reason: CAS atomically compares memory location with expected value and updates it if they match, fundamental for lock-free programming.

Tag: Normal

---

### Question 218
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Spinlock
Difficulty: Medium

Question: What is a spinlock?
A) Rotating lock
B) Lock where thread busy-waits in loop
C) Sleeping lock
D) No lock

✔ Correct Answer: B

Reason: Spinlock causes thread to repeatedly check lock availability in tight loop, efficient for short wait times but wastes CPU for long waits.

Tag: Normal

---

### Question 219
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Mutex
Difficulty: Easy

Question: What does mutex stand for?
A) Multiple Execution
B) Mutual Exclusion
C) Multi Exit
D) Mutual Extension

✔ Correct Answer: B

Reason: Mutex (Mutual Exclusion) is a synchronization primitive ensuring only one thread accesses critical section at a time.

Tag: Past Paper

---

### Question 220
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Condition Variables
Difficulty: Hard

Question: What are condition variables used for?
A) Variable storage
B) Thread waiting for specific condition
C) Counting
D) Memory allocation

✔ Correct Answer: B

Reason: Condition variables allow threads to wait until particular condition becomes true, used with mutex for complex synchronization patterns.

Tag: Normal

---

### Question 221
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Hold and Wait
Difficulty: Easy

Question: What does "hold and wait" condition mean?
A) Process holds nothing
B) Process holds resources while waiting for more
C) Process waits only
D) No holding occurs

✔ Correct Answer: B

Reason: Hold and wait means process holds at least one resource while waiting to acquire additional resources held by other processes.

Tag: Normal

---

### Question 222
Domain: Operating Systems
Topic: Deadlocks
Subtopic: No Preemption
Difficulty: Medium

Question: What does "no preemption" condition mean for deadlock?
A) Resources can be forcibly taken
B) Resources cannot be forcibly removed from process
C) All resources preemptible
D) No resources exist

✔ Correct Answer: B

Reason: No preemption means resources cannot be forcibly taken from process; they must be voluntarily released, contributing to deadlock possibility.

Tag: Normal

---

### Question 223
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Circular Wait
Difficulty: Medium

Question: What is circular wait in deadlock?
A) Linear waiting
B) Circular chain of processes each waiting for resource held by next
C) No waiting
D) Random waiting

✔ Correct Answer: B

Reason: Circular wait forms a closed chain where each process waits for resource held by next process in chain, completing deadlock conditions.

Tag: Past Paper

---

### Question 224
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: How can hold and wait be prevented?
A) Allow unlimited resources
B) Require process to request all resources at once
C) Use more processes
D) Ignore the problem

✔ Correct Answer: B

Reason: Preventing hold and wait requires processes to request all needed resources atomically before execution, though this may reduce resource utilization.

Tag: Normal

---

### Question 225
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: How can circular wait be prevented?
A) Random allocation
B) Impose total ordering on resource types
C) Allow any order
D) Use more resources

✔ Correct Answer: B

Reason: Circular wait prevention imposes total ordering on resources, requiring processes to request resources in increasing order, breaking circular chain.

Tag: Normal

---

### Question 226
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Avoidance
Difficulty: Hard

Question: What is the Banker's Algorithm used for?
A) Banking transactions
B) Deadlock avoidance by safe state checking
C) Process scheduling
D) Memory allocation

✔ Correct Answer: B

Reason: Banker's Algorithm avoids deadlock by checking if resource allocation leaves system in safe state before granting requests.

Tag: Past Paper

---

### Question 227
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Safe State
Difficulty: Hard

Question: What is a safe state?
A) No processes running
B) System can allocate resources to each process in some order avoiding deadlock
C) All resources free
D) Deadlock exists

✔ Correct Answer: B

Reason: Safe state means there exists a sequence of process execution where all can complete without deadlock, even with maximum resource demands.

Tag: Normal

---

### Question 228
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Unsafe State
Difficulty: Medium

Question: Does unsafe state mean deadlock exists?
A) Yes, always
B) No, deadlock may occur but not guaranteed
C) No relation
D) Impossible state

✔ Correct Answer: B

Reason: Unsafe state means deadlock is possible but not certain; system cannot guarantee all processes can complete.

Tag: Normal

---

### Question 229
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Detection
Difficulty: Hard

Question: What does deadlock detection algorithm do?
A) Prevents deadlock
B) Examines system state to determine if deadlock exists
C) Avoids deadlock
D) Creates deadlock

✔ Correct Answer: B

Reason: Deadlock detection periodically examines resource allocation graph or matrices to determine if circular wait exists, indicating deadlock.

Tag: Normal

---

### Question 230
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Recovery
Difficulty: Medium

Question: What is process termination for deadlock recovery?
A) Terminate all processes
B) Abort one or more processes to break circular wait
C) Create new processes
D) Suspend processes

✔ Correct Answer: B

Reason: Process termination aborts one or more deadlocked processes to break circular wait, either all at once or one at a time.

Tag: Normal

---

### Question 231
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Recovery
Difficulty: Hard

Question: What is resource preemption for deadlock recovery?
A) No preemption
B) Forcibly take resources from processes to break deadlock
C) Give more resources
D) Delete resources

✔ Correct Answer: B

Reason: Resource preemption selects victim process, takes its resources to give to others, and rolls back victim to safe state.

Tag: Normal

---

### Question 232
Domain: Operating Systems
Topic: Memory Management
Subtopic: Logical vs Physical Address
Difficulty: Easy

Question: What is a logical address?
A) Physical memory location
B) Address generated by CPU
C) Disk address
D) Network address

✔ Correct Answer: B

Reason: Logical (virtual) address is generated by CPU during program execution, translated to physical address by MMU.

Tag: Past Paper

---

### Question 233
Domain: Operating Systems
Topic: Memory Management
Subtopic: Logical vs Physical Address
Difficulty: Easy

Question: What is a physical address?
A) CPU-generated address
B) Actual location in memory hardware
C) Disk location
D) Virtual address

✔ Correct Answer: B

Reason: Physical address is actual location in memory hardware where data resides, accessed by memory unit.

Tag: Normal

---

### Question 234
Domain: Operating Systems
Topic: Memory Management
Subtopic: MMU
Difficulty: Medium

Question: What does MMU stand for?
A) Memory Management Unit
B) Multiple Memory Usage
C) Main Memory Unit
D) Manual Memory Update

✔ Correct Answer: A

Reason: MMU (Memory Management Unit) is hardware device that translates logical addresses to physical addresses at runtime.

Tag: Past Paper

---

### Question 235
Domain: Operating Systems
Topic: Memory Management
Subtopic: Address Binding
Difficulty: Medium

Question: When does compile-time binding occur?
A) During execution
B) During compilation if memory location known
C) Never
D) After execution

✔ Correct Answer: B

Reason: Compile-time binding generates absolute code if memory location known in advance, requiring recompilation if location changes.

Tag: Normal

---

### Question 236
Domain: Operating Systems
Topic: Memory Management
Subtopic: Address Binding
Difficulty: Medium

Question: What is load-time binding?
A) Binding at compilation
B) Binding when program loaded into memory
C) Binding during execution
D) No binding

✔ Correct Answer: B

Reason: Load-time binding generates relocatable code, with final addresses assigned when program is loaded into memory.

Tag: Normal

---

### Question 237
Domain: Operating Systems
Topic: Memory Management
Subtopic: Address Binding
Difficulty: Hard

Question: What is execution-time binding?
A) Binding at compilation
B) Binding at load time
C) Binding delayed until runtime, allowing process movement
D) No binding

✔ Correct Answer: C

Reason: Execution-time (dynamic) binding delays address binding until runtime, allowing process to move in memory during execution, requires MMU support.

Tag: Normal

---

### Question 238
Domain: Operating Systems
Topic: Memory Management
Subtopic: Dynamic Loading
Difficulty: Medium

Question: What is dynamic loading?
A) Loading all at start
B) Routine loaded only when called
C) No loading
D) Static loading

✔ Correct Answer: B

Reason: Dynamic loading loads routines only when needed, improving memory utilization by not loading unused code.

Tag: Normal

---

### Question 239
Domain: Operating Systems
Topic: Memory Management
Subtopic: Dynamic Linking
Difficulty: Hard

Question: What is dynamic linking?
A) Linking at compile time
B) Linking postponed until execution time
C) No linking
D) Static linking

✔ Correct Answer: B

Reason: Dynamic linking delays linking until execution, with stub locating and loading library routines, saving memory through shared libraries.

Tag: Normal

---

### Question 240
Domain: Operating Systems
Topic: Memory Management
Subtopic: Swapping
Difficulty: Easy

Question: What is swapping?
A) Exchanging data
B) Moving process between memory and disk
C) Deleting process
D) Creating process

✔ Correct Answer: B

Reason: Swapping temporarily moves entire process from memory to backing store (swap space) and back, enabling multiprogramming beyond physical memory limits.

Tag: Past Paper

---

### Question 241
Domain: Operating Systems
Topic: Memory Management
Subtopic: Contiguous Allocation
Difficulty: Easy

Question: What is contiguous memory allocation?
A) Scattered allocation
B) Each process occupies single contiguous memory section
C) No allocation
D) Random allocation

✔ Correct Answer: B

Reason: Contiguous allocation assigns each process a single continuous block of memory, simple but causes fragmentation.

Tag: Normal

---

### Question 242
Domain: Operating Systems
Topic: Memory Management
Subtopic: Fixed Partitioning
Difficulty: Medium

Question: What is fixed partitioning?
A) Variable partitions
B) Memory divided into fixed-size partitions
C) No partitions
D) Dynamic partitions

✔ Correct Answer: B

Reason: Fixed partitioning divides memory into fixed-size partitions at system startup, simple but causes internal fragmentation.

Tag: Normal

---

### Question 243
Domain: Operating Systems
Topic: Memory Management
Subtopic: Variable Partitioning
Difficulty: Medium

Question: What is variable partitioning?
A) Fixed partitions
B) Partitions created dynamically based on process size
C) No partitions
D) Equal partitions

✔ Correct Answer: B

Reason: Variable (dynamic) partitioning creates partitions of exact size needed by process, reducing internal fragmentation but causing external fragmentation.

Tag: Normal

---

### Question 244
Domain: Operating Systems
Topic: Memory Management
Subtopic: Internal Fragmentation
Difficulty: Easy

Question: What is internal fragmentation?
A) Wasted space outside partitions
B) Wasted space within allocated partition
C) No fragmentation
D) Disk fragmentation

✔ Correct Answer: B

Reason: Internal fragmentation is unused memory within allocated partition when partition is larger than needed by process.

Tag: Past Paper

---

### Question 245
Domain: Operating Systems
Topic: Memory Management
Subtopic: External Fragmentation
Difficulty: Easy

Question: What is external fragmentation?
A) Wasted space within partitions
B) Free memory scattered in small blocks
C) No fragmentation
D) Internal waste

✔ Correct Answer: B

Reason: External fragmentation occurs when free memory is broken into small scattered blocks, total space sufficient but not contiguous.

Tag: Past Paper

---

### Question 246
Domain: Operating Systems
Topic: Memory Management
Subtopic: First Fit
Difficulty: Medium

Question: What is first-fit allocation strategy?
A) Best available hole
B) First hole large enough
C) Worst hole
D) Last hole

✔ Correct Answer: B

Reason: First-fit allocates first available hole large enough for process, fast but may leave small unusable holes.

Tag: Normal

---

### Question 247
Domain: Operating Systems
Topic: Memory Management
Subtopic: Best Fit
Difficulty: Medium

Question: What is best-fit allocation strategy?
A) First available hole
B) Smallest hole large enough
C) Largest hole
D) Random hole

✔ Correct Answer: B

Reason: Best-fit searches entire list for smallest hole that fits process, minimizes wasted space but slower and creates tiny unusable holes.

Tag: Normal

---

### Question 248
Domain: Operating Systems
Topic: Memory Management
Subtopic: Worst Fit
Difficulty: Medium

Question: What is worst-fit allocation strategy?
A) Smallest hole
B) Largest available hole
C) First hole
D) Random hole

✔ Correct Answer: B

Reason: Worst-fit allocates largest available hole, leaving larger remaining fragments that may be more useful, but wastes large holes.

Tag: Normal

---

### Question 249
Domain: Operating Systems
Topic: Memory Management
Subtopic: Compaction
Difficulty: Medium

Question: What is memory compaction?
A) Compression
B) Moving processes to create one large free block
C) Deletion
D) Expansion

✔ Correct Answer: B

Reason: Compaction shuffles memory contents to place all free memory together in one large block, eliminating external fragmentation but expensive.

Tag: Normal

---

### Question 250
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

### Question 251
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Table
Difficulty: Medium

Question: What is a page table?
A) Data table
B) Mapping from logical pages to physical frames
C) Process table
D) File table

✔ Correct Answer: B

Reason: Page table maintains mapping between logical page numbers and physical frame numbers for address translation.

Tag: Normal

---

### Question 252
Domain: Operating Systems
Topic: Memory Management
Subtopic: Frame
Difficulty: Easy

Question: What is a frame in memory management?
A) Picture frame
B) Fixed-size block of physical memory
C) Variable block
D) Disk block

✔ Correct Answer: B

Reason: Frame is a fixed-size block of physical memory, same size as page, used in paging systems.

Tag: Normal

---

### Question 253
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Size
Difficulty: Hard

Question: What is a typical page size?
A) 1 byte
B) 4 KB or 4 MB
C) 1 GB
D) Variable

✔ Correct Answer: B

Reason: Common page sizes are 4 KB (standard) or 4 MB (huge pages), balancing page table size and internal fragmentation.

Tag: Normal

---

### Question 254
Domain: Operating Systems
Topic: Memory Management
Subtopic: TLB
Difficulty: Hard

Question: What does TLB stand for?
A) Table Lookup Buffer
B) Translation Lookaside Buffer
C) Total Logic Buffer
D) Time Limit Buffer

✔ Correct Answer: B

Reason: TLB (Translation Lookaside Buffer) is fast associative cache storing recent page table entries for quick address translation.

Tag: Past Paper

---

### Question 255
Domain: Operating Systems
Topic: Memory Management
Subtopic: TLB Hit
Difficulty: Medium

Question: What is a TLB hit?
A) TLB miss
B) Page number found in TLB
C) TLB failure
D) Page fault

✔ Correct Answer: B

Reason: TLB hit occurs when page number is found in TLB, enabling fast address translation without accessing page table.

Tag: Normal

---

### Question 256
Domain: Operating Systems
Topic: Memory Management
Subtopic: Effective Access Time
Difficulty: Hard

Question: How does TLB affect effective memory access time?
A) Increases time
B) Reduces time by caching translations
C) No effect
D) Doubles time

✔ Correct Answer: B

Reason: TLB significantly reduces effective access time by caching frequently used page table entries, avoiding memory access for translation.

Tag: Normal

---

### Question 257
Domain: Operating Systems
Topic: Memory Management
Subtopic: Hierarchical Paging
Difficulty: Hard

Question: Why use hierarchical (multi-level) paging?
A) Slower access
B) Reduce page table size in memory
C) Increase complexity
D) No benefit

✔ Correct Answer: B

Reason: Hierarchical paging breaks page table into multiple levels, keeping only active portions in memory, reducing memory overhead for large address spaces.

Tag: Normal

---

### Question 258
Domain: Operating Systems
Topic: Memory Management
Subtopic: Hashed Page Table
Difficulty: Hard

Question: What is a hashed page table?
A) Sequential table
B) Hash function maps virtual page to linked list
C) No hashing
D) Direct mapping

✔ Correct Answer: B

Reason: Hashed page table uses hash function to map virtual page numbers to hash table entries containing linked lists of pages, efficient for sparse address spaces.

Tag: Normal

---

### Question 259
Domain: Operating Systems
Topic: Memory Management
Subtopic: Inverted Page Table
Difficulty: Hard

Question: What characterizes inverted page table?
A) One entry per page
B) One entry per physical frame
C) No entries
D) Multiple entries per page

✔ Correct Answer: B

Reason: Inverted page table has one entry per physical frame (not per page), reducing memory overhead but requiring search or hashing.

Tag: Normal

---

### Question 260
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation
Difficulty: Medium

Question: What is segmentation?
A) Fixed-size division
B) Variable-size logical division based on program structure
C) No division
D) Page-based division

✔ Correct Answer: B

Reason: Segmentation divides memory into variable-size segments based on logical program structure (code, data, stack), reflecting programmer's view.

Tag: Past Paper

---

### Question 261
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segment Table
Difficulty: Medium

Question: What does segment table contain?
A) Page numbers
B) Base address and limit for each segment
C) Frame numbers
D) Process IDs

✔ Correct Answer: B

Reason: Segment table stores base address (starting physical address) and limit (length) for each segment, enabling address translation and protection.

Tag: Normal

---

### Question 262
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation vs Paging
Difficulty: Hard

Question: What is main difference between paging and segmentation?
A) No difference
B) Paging uses fixed sizes, segmentation uses variable sizes
C) Paging is slower
D) Segmentation is obsolete

✔ Correct Answer: B

Reason: Paging uses fixed-size pages (physical view), segmentation uses variable-size segments (logical view), each with different advantages.

Tag: Normal

---

### Question 263
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

Reason: Virtual memory separates logical memory from physical memory, allowing programs larger than physical memory to execute.

Tag: Past Paper

---

### Question 264
Domain: Operating Systems
Topic: Memory Management
Subtopic: Demand Paging
Difficulty: Medium

Question: What is demand paging?
A) Loading all pages at start
B) Loading pages only when needed
C) No paging
D) Pre-loading all pages

✔ Correct Answer: B

Reason: Demand paging loads pages into memory only when accessed, reducing initial load time and memory usage.

Tag: Past Paper

---

### Question 265
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault
Difficulty: Easy

Question: What is a page fault?
A) Hardware failure
B) Reference to page not in memory
C) Disk error
D) Program error

✔ Correct Answer: B

Reason: Page fault occurs when process references page not currently in physical memory, triggering OS to load it from disk.

Tag: Past Paper

---

### Question 266
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault Handling
Difficulty: Medium

Question: What happens during page fault handling?
A) Process terminates
B) OS loads page from disk to memory
C) System crashes
D) Nothing

✔ Correct Answer: B

Reason: Page fault handler locates page on disk, finds free frame, loads page into frame, updates page table, and restarts instruction.

Tag: Normal

---

### Question 267
Domain: Operating Systems
Topic: Memory Management
Subtopic: Pure Demand Paging
Difficulty: Hard

Question: What is pure demand paging?
A) Load some pages initially
B) Start process with no pages in memory
C) Load all pages
D) No paging

✔ Correct Answer: B

Reason: Pure demand paging starts process with no pages loaded, bringing pages only as they're referenced, though first instructions cause many faults.

Tag: Normal

---

### Question 268
Domain: Operating Systems
Topic: Memory Management
Subtopic: Locality of Reference
Difficulty: Medium

Question: What is locality of reference?
A) Random access pattern
B) Tendency to access nearby memory locations
C) No pattern
D) Sequential only

✔ Correct Answer: B

Reason: Locality of reference means programs tend to access same or nearby memory locations repeatedly, making demand paging practical.

Tag: Normal

---

### Question 269
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Replacement
Difficulty: Easy

Question: When is page replacement needed?
A) Always
B) When page fault occurs and no free frames available
C) Never
D) At startup

✔ Correct Answer: B

Reason: Page replacement selects victim page to remove when page fault occurs but all frames are allocated, making room for new page.

Tag: Normal

---

### Question 270
Domain: Operating Systems
Topic: Memory Management
Subtopic: FIFO Page Replacement
Difficulty: Easy

Question: What is FIFO page replacement?
A) Replace most recently used
B) Replace oldest page in memory
C) Replace randomly
D) No replacement

✔ Correct Answer: B

Reason: FIFO replaces page that has been in memory longest, simple but may remove frequently used pages, suffers from Belady's Anomaly.

Tag: Past Paper

---

### Question 271
Domain: Operating Systems
Topic: Memory Management
Subtopic: Optimal Page Replacement
Difficulty: Hard

Question: What does optimal page replacement do?
A) Replace oldest page
B) Replace page not used for longest time in future
C) Replace randomly
D) Replace first page

✔ Correct Answer: B

Reason: Optimal algorithm replaces page that won't be used for longest time, minimizing page faults but impossible to implement (requires future knowledge).

Tag: Normal

---

### Question 272
Domain: Operating Systems
Topic: Memory Management
Subtopic: LRU Page Replacement
Difficulty: Medium

Question: What is LRU page replacement?
A) Replace newest page
B) Replace least recently used page
C) Replace randomly
D) Replace first page

✔ Correct Answer: B

Reason: LRU (Least Recently Used) replaces page unused for longest time, approximating optimal algorithm using past behavior to predict future.

Tag: Past Paper

---

### Question 273
Domain: Operating Systems
Topic: Memory Management
Subtopic: LRU Implementation
Difficulty: Hard

Question: Why is LRU difficult to implement?
A) Too simple
B) Requires hardware support or expensive software tracking
C) Too fast
D) No difficulty

✔ Correct Answer: B

Reason: True LRU requires timestamping or stack for every memory reference, expensive in hardware or software, leading to approximations.

Tag: Normal

---

### Question 274
Domain: Operating Systems
Topic: Memory Management
Subtopic: Second Chance Algorithm
Difficulty: Hard

Question: How does second chance (clock) algorithm work?
A) Pure FIFO
B) FIFO with reference bit giving second chance
C) Pure LRU
D) Random

✔ Correct Answer: B

Reason: Second chance uses FIFO with reference bit; if bit is set, clears it and gives page another chance, approximating LRU efficiently.

Tag: Normal

---

### Question 275
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

Reason: Thrashing occurs when system spends most time swapping pages in/out rather than executing, caused by insufficient memory or poor locality.

Tag: Past Paper

---

### Question 276
Domain: Operating Systems
Topic: Memory Management
Subtopic: Working Set
Difficulty: Hard

Question: What is a working set?
A) All pages
B) Set of pages actively used by process in time window
C) Random pages
D) No pages

✔ Correct Answer: B

Reason: Working set is collection of pages referenced by process during recent time interval, used to prevent thrashing by ensuring sufficient frames.

Tag: Normal

---

### Question 277
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault Frequency
Difficulty: Hard

Question: How is page fault frequency (PFF) used?
A) Ignored
B) Monitor to adjust frame allocation
C) Always constant
D) Not measurable

✔ Correct Answer: B

Reason: PFF monitors page fault rate; if too high, allocate more frames; if too low, reduce frames, preventing thrashing while optimizing memory use.

Tag: Normal

---

### Question 278
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Structure
Difficulty: Medium

Question: What is a file control block (FCB)?
A) Process control
B) Data structure containing file information
C) Memory block
D) CPU block

✔ Correct Answer: B

Reason: FCB (inode in UNIX) stores file metadata including permissions, timestamps, size, and disk block pointers.

Tag: Normal

---

### Question 279
Domain: Operating Systems
Topic: File System Management
Subtopic: Open File Table
Difficulty: Medium

Question: What is the open file table?
A) List of all files
B) Table tracking currently open files
C) Deleted files
D) Closed files

✔ Correct Answer: B

Reason: Open file table maintains information about files currently opened by processes, including file pointer and access mode.

Tag: Normal

---

### Question 280
Domain: Operating Systems
Topic: File System Management
Subtopic: File Descriptor
Difficulty: Easy

Question: What is a file descriptor?
A) File content
B) Integer index to open file table entry
C) File name
D) File size

✔ Correct Answer: B

Reason: File descriptor is small non-negative integer returned by open() system call, used to reference open file in subsequent operations.

Tag: Normal

---

### Question 281
Domain: Operating Systems
Topic: File System Management
Subtopic: Mount Point
Difficulty: Medium

Question: What is a mount point?
A) Hardware mount
B) Directory where file system is attached
C) Disk location
D) Network point

✔ Correct Answer: B

Reason: Mount point is directory in existing file system where another file system is attached, integrating multiple file systems into single tree.

Tag: Normal

---

### Question 282
Domain: Operating Systems
Topic: File System Management
Subtopic: Disk Caching
Difficulty: Medium

Question: What is disk caching?
A) Disk storage
B) Keeping frequently used disk blocks in memory
C) Disk deletion
D) Disk formatting

✔ Correct Answer: B

Reason: Disk cache (buffer cache) stores frequently accessed disk blocks in memory, reducing disk I/O and improving performance.

Tag: Normal

---

### Question 283
Domain: Operating Systems
Topic: File System Management
Subtopic: Write-Through Cache
Difficulty: Hard

Question: What is write-through caching?
A) Delayed write
B) Write to cache and disk immediately
C) No writing
D) Cache only

✔ Correct Answer: B

Reason: Write-through writes data to both cache and disk immediately, ensuring consistency but slower than write-back.

Tag: Normal

---

### Question 284
Domain: Operating Systems
Topic: File System Management
Subtopic: Write-Back Cache
Difficulty: Hard

Question: What is write-back caching?
A) Immediate disk write
B) Write to cache, disk write delayed
C) No caching
D) Read only

✔ Correct Answer: B

Reason: Write-back writes to cache immediately but delays disk write, faster but risks data loss on crash.

Tag: Normal

---

### Question 285
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

### Question 286
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Performance
Difficulty: Easy

Question: What is rotational latency?
A) Seek time
B) Time for desired sector to rotate under head
C) Transfer time
D) Total time

✔ Correct Answer: B

Reason: Rotational latency is time waiting for desired sector to rotate under read/write head after seek completes.

Tag: Normal

---

### Question 287
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Performance
Difficulty: Medium

Question: What is transfer time?
A) Seek time
B) Time to actually read/write data
C) Rotation time
D) Queue time

✔ Correct Answer: B

Reason: Transfer time is time to actually transfer data between disk and memory after head is positioned.

Tag: Normal

---

### Question 288
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD
Difficulty: Easy

Question: What does SSD stand for?
A) Super Speed Disk
B) Solid State Drive
C) Standard Storage Device
D) Sequential Storage Disk

✔ Correct Answer: B

Reason: SSD (Solid State Drive) uses flash memory instead of spinning platters, providing faster access and no mechanical parts.

Tag: Normal

---

### Question 289
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSD vs HDD
Difficulty: Medium

Question: What advantage do SSDs have over HDDs?
A) Cheaper
B) Faster access, no moving parts
C) More capacity
D) Longer lifespan

✔ Correct Answer: B

Reason: SSDs provide much faster random access, lower latency, and no mechanical failures, though more expensive per GB.

Tag: Normal

---

### Question 290
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Ports
Difficulty: Easy

Question: What are I/O ports?
A) Network ports
B) Registers for communication with devices
C) USB ports
D) Serial ports

✔ Correct Answer: B

Reason: I/O ports are registers or memory locations used for communication between CPU and I/O devices.

Tag: Normal

---

### Question 291
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Memory-Mapped I/O
Difficulty: Hard

Question: What is memory-mapped I/O?
A) Separate I/O address space
B) Device registers mapped to memory address space
C) No mapping
D) Disk mapping

✔ Correct Answer: B

Reason: Memory-mapped I/O maps device control registers into memory address space, allowing standard memory instructions for I/O operations.

Tag: Normal

---

### Question 292
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Port-Mapped I/O
Difficulty: Hard

Question: What is port-mapped I/O?
A) Memory-mapped
B) Separate address space for I/O devices
C) No ports
D) Network only

✔ Correct Answer: B

Reason: Port-mapped (isolated) I/O uses separate address space for I/O devices, requiring special I/O instructions.

Tag: Normal

---

### Question 293
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Threats
Difficulty: Easy

Question: What is a trojan horse?
A) Virus type
B) Program appearing useful but containing malicious code
C) Network attack
D) Hardware failure

✔ Correct Answer: B

Reason: Trojan horse is program that appears legitimate but contains hidden malicious functionality, tricking users into executing it.

Tag: Normal

---

### Question 294
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Threats
Difficulty: Easy

Question: What is a computer virus?
A) Hardware problem
B) Self-replicating code that spreads by modifying programs
C) Network issue
D) User error

✔ Correct Answer: B

Reason: Virus is malicious code that replicates by inserting copies into other programs or files, spreading when infected programs execute.

Tag: Past Paper

---

### Question 295
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Threats
Difficulty: Medium

Question: What is a worm?
A) Virus variant
B) Self-replicating program spreading through network
C) Hardware bug
D) Software bug

✔ Correct Answer: B

Reason: Worm is self-contained program that replicates and spreads through networks without needing host program, consuming resources.

Tag: Normal

---

### Question 296
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Mechanisms
Difficulty: Medium

Question: What is encryption?
A) Deleting data
B) Transforming data to unreadable form
C) Compressing data
D) Copying data

✔ Correct Answer: B

Reason: Encryption transforms data into unreadable ciphertext using algorithm and key, protecting confidentiality during storage or transmission.

Tag: Normal

---

### Question 297
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Mechanisms
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

### Question 298
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control
Difficulty: Hard

Question: What is Role-Based Access Control (RBAC)?
A) User-based control
B) Access based on user's role in organization
C) No control
D) Random access

✔ Correct Answer: B

Reason: RBAC assigns permissions to roles rather than individuals, simplifying administration and ensuring consistent access policies.

Tag: Normal

---

### Question 299
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Hard

Question: What is a denial-of-service (DoS) attack?
A) Stealing data
B) Overwhelming system to prevent legitimate access
C) Deleting files
D) Password cracking

✔ Correct Answer: B

Reason: DoS attack floods system with requests or exploits vulnerabilities to exhaust resources, preventing legitimate users from accessing services.

Tag: Normal

---

### Question 300
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Principles
Difficulty: Medium

Question: What is defense in depth?
A) Single security layer
B) Multiple layers of security controls
C) No security
D) Physical security only

✔ Correct Answer: B

Reason: Defense in depth uses multiple overlapping security mechanisms, so if one fails, others still provide protection.

Tag: Normal

---

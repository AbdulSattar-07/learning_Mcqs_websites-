# Operating Systems - MCQ Batch 04
## Questions 301-400

---

### Question 301
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Operating System Services
Difficulty: Easy

Question: Which service does an operating system provide to users?
A) Hardware manufacturing
B) Program execution
C) Internet creation
D) Electricity supply

✔ Correct Answer: B

Reason: Operating systems provide services including program execution, I/O operations, file system manipulation, communication, and error detection.

Tag: Normal

---

### Question 302
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: User Interface
Difficulty: Easy

Question: What are the two main types of user interfaces in operating systems?
A) Fast and slow
B) Command-line and graphical
C) Old and new
D) Simple and complex

✔ Correct Answer: B

Reason: Operating systems provide CLI (Command-Line Interface) for text-based interaction and GUI (Graphical User Interface) for visual interaction.

Tag: Normal

---

### Question 303
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Programs
Difficulty: Medium

Question: What are system programs?
A) User applications
B) Programs providing environment for program development and execution
C) Hardware drivers only
D) Games

✔ Correct Answer: B

Reason: System programs provide convenient environment for program development and execution, including file management, status information, and programming language support.

Tag: Normal

---

### Question 304
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls
Difficulty: Medium

Question: Which system call category handles process control?
A) File manipulation
B) fork(), exit(), wait()
C) Device management
D) Information maintenance

✔ Correct Answer: B

Reason: Process control system calls include fork() for creation, exit() for termination, wait() for synchronization, and exec() for loading programs.

Tag: Past Paper

---

### Question 305
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Call Implementation
Difficulty: Hard

Question: How are system calls typically implemented?
A) Direct hardware access
B) Through trap instruction to kernel mode
C) User mode only
D) No implementation needed

✔ Correct Answer: B

Reason: System calls use trap/software interrupt to switch from user mode to kernel mode, allowing controlled access to privileged operations.

Tag: Normal

---

### Question 306
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: API vs System Call
Difficulty: Medium

Question: What is the difference between API and system call?
A) No difference
B) API is high-level interface, system call is low-level kernel entry
C) API is slower
D) System call is obsolete

✔ Correct Answer: B

Reason: API (like POSIX) provides high-level programming interface, while system calls are actual entry points into kernel, often wrapped by API functions.

Tag: Normal

---

### Question 307
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Hybrid Systems
Difficulty: Hard

Question: What is a hybrid kernel?
A) Pure microkernel
B) Combines microkernel and monolithic approaches
C) No kernel
D) Pure monolithic

✔ Correct Answer: B

Reason: Hybrid kernels combine microkernel modularity with monolithic performance, keeping some services in kernel space for speed while maintaining structure.

Tag: Normal

---

### Question 308
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Modules
Difficulty: Medium

Question: What are loadable kernel modules?
A) User programs
B) Kernel components loaded dynamically as needed
C) Static libraries
D) Configuration files

✔ Correct Answer: B

Reason: Loadable kernel modules allow dynamic loading/unloading of kernel code at runtime, providing flexibility without rebooting.

Tag: Normal

---

### Question 309
Domain: Operating Systems
Topic: Process Management
Subtopic: Process vs Program
Difficulty: Easy

Question: What distinguishes a process from a program?
A) No difference
B) Process is active with execution state, program is passive code
C) Process is slower
D) Program is newer

✔ Correct Answer: B

Reason: Program is passive entity (code on disk), process is active entity with program counter, registers, and execution state.

Tag: Past Paper

---

### Question 310
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Memory Layout
Difficulty: Medium

Question: What are the typical sections of process memory?
A) Only code
B) Text, data, heap, stack
C) Only data
D) Random sections

✔ Correct Answer: B

Reason: Process memory includes text (code), data (global variables), heap (dynamic allocation), and stack (function calls, local variables).

Tag: Normal

---

### Question 311
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Identifier
Difficulty: Easy

Question: What is a PID?
A) Process Input Device
B) Process Identifier - unique number for each process
C) Program ID
D) Processor ID

✔ Correct Answer: B

Reason: PID (Process Identifier) is unique integer assigned to each process by OS for identification and management.

Tag: Normal

---

### Question 312
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Hierarchy
Difficulty: Medium

Question: In UNIX, what is the relationship between parent and child processes?
A) No relationship
B) Parent creates child, forming tree structure
C) Child creates parent
D) Random relationship

✔ Correct Answer: B

Reason: UNIX processes form tree hierarchy where parent creates children via fork(), with init (PID 1) as root of tree.

Tag: Normal

---

### Question 313
Domain: Operating Systems
Topic: Process Management
Subtopic: exec() System Call
Difficulty: Medium

Question: What does exec() system call do?
A) Creates new process
B) Replaces current process memory with new program
C) Terminates process
D) Suspends process

✔ Correct Answer: B

Reason: exec() family of calls replaces current process's memory space with new program while keeping same PID.

Tag: Past Paper

---

### Question 314
Domain: Operating Systems
Topic: Process Management
Subtopic: wait() System Call
Difficulty: Medium

Question: What does wait() system call do?
A) Creates process
B) Parent waits for child to terminate
C) Sleeps indefinitely
D) Terminates process

✔ Correct Answer: B

Reason: wait() suspends parent process until one of its children terminates, returning child's exit status.

Tag: Normal

---

### Question 315
Domain: Operating Systems
Topic: Process Management
Subtopic: Interprocess Communication
Difficulty: Easy

Question: What is IPC?
A) Internet Protocol Communication
B) Interprocess Communication - processes exchanging data
C) Internal Process Control
D) Integrated Program Compilation

✔ Correct Answer: B

Reason: IPC (Interprocess Communication) allows processes to exchange data and synchronize actions through various mechanisms.

Tag: Past Paper

---

### Question 316
Domain: Operating Systems
Topic: Process Management
Subtopic: IPC Models
Difficulty: Medium

Question: What are the two fundamental IPC models?
A) Fast and slow
B) Shared memory and message passing
C) Old and new
D) Simple and complex

✔ Correct Answer: B

Reason: IPC uses shared memory (processes share memory region) or message passing (processes exchange messages through kernel).

Tag: Past Paper

---

### Question 317
Domain: Operating Systems
Topic: Process Management
Subtopic: Shared Memory
Difficulty: Medium

Question: What is the main advantage of shared memory IPC?
A) Slower communication
B) Fast communication after setup
C) More secure
D) Simpler synchronization

✔ Correct Answer: B

Reason: Shared memory provides fast communication as processes directly access shared region without kernel intervention after initial setup.

Tag: Normal

---

### Question 318
Domain: Operating Systems
Topic: Process Management
Subtopic: Message Passing
Difficulty: Medium

Question: What operations are fundamental to message passing?
A) read() and write()
B) send() and receive()
C) push() and pop()
D) get() and put()

✔ Correct Answer: B

Reason: Message passing uses send() to transmit messages and receive() to accept messages, with kernel managing communication.

Tag: Normal

---

### Question 319
Domain: Operating Systems
Topic: Process Management
Subtopic: Pipes
Difficulty: Easy

Question: What is a pipe in UNIX?
A) Hardware component
B) Conduit for communication between processes
C) File type
D) Network protocol

✔ Correct Answer: B

Reason: Pipe is IPC mechanism providing unidirectional data flow between processes, commonly used for parent-child communication.

Tag: Normal

---

### Question 320
Domain: Operating Systems
Topic: Process Management
Subtopic: Named Pipes
Difficulty: Medium

Question: How do named pipes differ from ordinary pipes?
A) No difference
B) Named pipes persist and allow unrelated processes to communicate
C) Named pipes are slower
D) Named pipes are temporary

✔ Correct Answer: B

Reason: Named pipes (FIFOs) have filesystem name, persist beyond process lifetime, and allow communication between unrelated processes.

Tag: Normal

---

### Question 321
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Queues
Difficulty: Easy

Question: What is the ready queue?
A) Queue of terminated processes
B) Queue of processes ready to execute
C) Queue of blocked processes
D) Queue of new processes

✔ Correct Answer: B

Reason: Ready queue contains processes in main memory that are ready and waiting for CPU allocation.

Tag: Normal

---

### Question 322
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Queues
Difficulty: Easy

Question: What is the device queue?
A) Queue of ready processes
B) Queue of processes waiting for I/O device
C) Queue of terminated processes
D) CPU queue

✔ Correct Answer: B

Reason: Device queue contains processes waiting for specific I/O device to become available.

Tag: Normal

---

### Question 323
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Types
Difficulty: Medium

Question: What is long-term scheduling?
A) CPU scheduling
B) Job scheduling - selecting processes to load into memory
C) I/O scheduling
D) Thread scheduling

✔ Correct Answer: B

Reason: Long-term (job) scheduler selects processes from job pool to load into memory, controlling degree of multiprogramming.

Tag: Normal

---

### Question 324
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Types
Difficulty: Medium

Question: What is short-term scheduling?
A) Job scheduling
B) CPU scheduling - selecting process to execute next
C) Memory scheduling
D) Disk scheduling

✔ Correct Answer: B

Reason: Short-term (CPU) scheduler selects process from ready queue to execute next, invoked very frequently (milliseconds).

Tag: Past Paper

---

### Question 325
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Types
Difficulty: Hard

Question: What is medium-term scheduling?
A) CPU scheduling
B) Swapping processes in/out of memory
C) Job scheduling
D) Thread scheduling

✔ Correct Answer: B

Reason: Medium-term scheduler swaps processes between memory and disk to control degree of multiprogramming and memory usage.

Tag: Normal

---

### Question 326
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Process Behavior
Difficulty: Medium

Question: What is a CPU-bound process?
A) I/O intensive
B) Spends more time computing than I/O
C) Balanced I/O and CPU
D) No CPU usage

✔ Correct Answer: B

Reason: CPU-bound (compute-intensive) processes spend most time executing instructions with few I/O operations.

Tag: Normal

---

### Question 327
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Process Behavior
Difficulty: Medium

Question: What is an I/O-bound process?
A) CPU intensive
B) Spends more time on I/O than computing
C) Balanced I/O and CPU
D) No I/O usage

✔ Correct Answer: B

Reason: I/O-bound processes spend most time waiting for I/O operations with short CPU bursts.

Tag: Normal

---

### Question 328
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Gantt Chart
Difficulty: Easy

Question: What is a Gantt chart in scheduling?
A) Process hierarchy
B) Visual representation of process execution timeline
C) Memory map
D) Network diagram

✔ Correct Answer: B

Reason: Gantt chart visually represents when each process executes on CPU over time, useful for analyzing scheduling algorithms.

Tag: Normal

---

### Question 329
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Convoy Effect
Difficulty: Hard

Question: What causes the convoy effect?
A) Too many processes
B) Short processes waiting behind long process in FCFS
C) Priority inversion
D) Deadlock

✔ Correct Answer: B

Reason: Convoy effect occurs in FCFS when many short processes queue behind one long process, causing poor average waiting time.

Tag: Normal

---

### Question 330
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Response Time
Difficulty: Easy

Question: What is response time?
A) Total execution time
B) Time from request submission to first response
C) Waiting time
D) Turnaround time

✔ Correct Answer: B

Reason: Response time measures time from request submission until first response is produced, important for interactive systems.

Tag: Normal

---

### Question 331
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Throughput
Difficulty: Easy

Question: What is throughput in scheduling?
A) Data transfer rate
B) Number of processes completed per time unit
C) CPU speed
D) Memory bandwidth

✔ Correct Answer: B

Reason: Throughput measures number of processes completed per time unit, indicating system productivity.

Tag: Normal

---

### Question 332
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Waiting Time
Difficulty: Easy

Question: What is waiting time?
A) Execution time
B) Time process spends in ready queue
C) I/O time
D) Total time

✔ Correct Answer: B

Reason: Waiting time is sum of time periods process spends waiting in ready queue before getting CPU.

Tag: Past Paper

---

### Question 333
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Real-Time Scheduling
Difficulty: Hard

Question: What distinguishes hard real-time from soft real-time systems?
A) No difference
B) Hard has strict deadlines, soft allows occasional misses
C) Hard is slower
D) Soft is obsolete

✔ Correct Answer: B

Reason: Hard real-time requires guaranteed deadline meeting (failure catastrophic), soft real-time prefers meeting deadlines but tolerates occasional misses.

Tag: Normal

---

### Question 334
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Rate Monotonic Scheduling
Difficulty: Hard

Question: What is rate monotonic scheduling?
A) Random priority
B) Static priority based on period - shorter period gets higher priority
C) Dynamic priority
D) No priority

✔ Correct Answer: B

Reason: Rate monotonic scheduling assigns static priorities inversely proportional to task periods, optimal for fixed-priority preemptive scheduling.

Tag: Normal

---

### Question 335
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Earliest Deadline First
Difficulty: Hard

Question: What is EDF scheduling?
A) Static priority
B) Dynamic priority based on deadline - earlier deadline gets higher priority
C) FCFS variant
D) Round robin variant

✔ Correct Answer: B

Reason: EDF (Earliest Deadline First) dynamically assigns priorities based on deadlines, optimal for dynamic priority scheduling.

Tag: Normal

---

### Question 336
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread States
Difficulty: Easy

Question: Do threads have states like processes?
A) No states
B) Yes - new, ready, running, waiting, terminated
C) Only running state
D) Different states

✔ Correct Answer: B

Reason: Threads have same states as processes (new, ready, running, waiting, terminated) as they are schedulable entities.

Tag: Normal

---

### Question 337
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Cancellation
Difficulty: Medium

Question: What is thread cancellation?
A) Creating thread
B) Terminating thread before completion
C) Suspending thread
D) Joining thread

✔ Correct Answer: B

Reason: Thread cancellation terminates target thread before it completes, either asynchronously (immediate) or deferred (at cancellation point).

Tag: Normal

---

### Question 338
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread-Local Storage
Difficulty: Hard

Question: What is thread-local storage (TLS)?
A) Shared storage
B) Private data unique to each thread
C) Global storage
D) No storage

✔ Correct Answer: B

Reason: TLS provides each thread with its own copy of data, useful when threads need private versions of global variables.

Tag: Normal

---

### Question 339
Domain: Operating Systems
Topic: Thread Management
Subtopic: Scheduler Activations
Difficulty: Hard

Question: What are scheduler activations?
A) Process scheduling
B) Mechanism for kernel to notify user-level thread library
C) Thread creation
D) Thread termination

✔ Correct Answer: B

Reason: Scheduler activations provide upcalls from kernel to user-level thread library, combining benefits of user and kernel threads.

Tag: Normal

---

### Question 340
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Safety
Difficulty: Medium

Question: What makes a function thread-safe?
A) Fast execution
B) Correct behavior when called by multiple threads concurrently
C) Single-threaded only
D) No parameters

✔ Correct Answer: B

Reason: Thread-safe functions work correctly when called simultaneously by multiple threads, avoiding race conditions through proper synchronization.

Tag: Normal

---

### Question 341
Domain: Operating Systems
Topic: Thread Management
Subtopic: Reentrant Code
Difficulty: Hard

Question: What is reentrant code?
A) Code that loops
B) Code that can be interrupted and safely called again
C) Recursive code
D) Non-executable code

✔ Correct Answer: B

Reason: Reentrant code can be interrupted mid-execution and safely called again before previous invocation completes, using only local variables.

Tag: Normal

---

### Question 342
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Bounded Buffer Problem
Difficulty: Hard

Question: What is the bounded buffer problem?
A) Unlimited buffer
B) Producer-consumer with fixed-size buffer
C) No buffer
D) Infinite buffer

✔ Correct Answer: B

Reason: Bounded buffer problem involves producer filling and consumer emptying fixed-size buffer, requiring synchronization to prevent overflow/underflow.

Tag: Past Paper

---

### Question 343
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphore Implementation
Difficulty: Hard

Question: How can busy waiting be avoided in semaphore implementation?
A) Cannot be avoided
B) Block process and place in waiting queue
C) Use faster CPU
D) Ignore the problem

✔ Correct Answer: B

Reason: Instead of busy waiting, semaphore can block process and place it in waiting queue, waking it when semaphore becomes available.

Tag: Normal

---

### Question 344
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Priority Inversion
Difficulty: Hard

Question: What is priority inversion?
A) Normal priority scheduling
B) High-priority process waiting for low-priority process holding resource
C) Priority increase
D) No priorities

✔ Correct Answer: B

Reason: Priority inversion occurs when high-priority process must wait for low-priority process holding needed resource, potentially causing deadline misses.

Tag: Normal

---

### Question 345
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Priority Inheritance
Difficulty: Hard

Question: How does priority inheritance solve priority inversion?
A) Lowers high priority
B) Temporarily raises low-priority process to high priority
C) Removes priorities
D) No solution

✔ Correct Answer: B

Reason: Priority inheritance temporarily elevates priority of process holding resource to that of highest-priority waiting process.

Tag: Normal

---

### Question 346
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Transactional Memory
Difficulty: Hard

Question: What is transactional memory?
A) Memory type
B) Executing memory operations atomically as transaction
C) Disk storage
D) Cache memory

✔ Correct Answer: B

Reason: Transactional memory allows group of memory operations to execute atomically, simplifying concurrent programming by avoiding explicit locks.

Tag: Normal

---

### Question 347
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Lock-Free Programming
Difficulty: Hard

Question: What characterizes lock-free programming?
A) Uses many locks
B) Uses atomic operations without locks
C) No synchronization
D) Single-threaded

✔ Correct Answer: B

Reason: Lock-free programming uses atomic operations like CAS to achieve synchronization without locks, avoiding deadlock and improving scalability.

Tag: Normal

---

### Question 348
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Resource Allocation Graph
Difficulty: Medium

Question: What does a cycle in resource allocation graph indicate?
A) No deadlock
B) Possible deadlock (certain if single instance per type)
C) Normal operation
D) System error

✔ Correct Answer: B

Reason: Cycle in resource allocation graph indicates possible deadlock; if each resource type has single instance, cycle guarantees deadlock.

Tag: Past Paper

---

### Question 349
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Resource Allocation Graph
Difficulty: Hard

Question: What do edges represent in resource allocation graph?
A) Process relationships
B) Request edge (process to resource) and assignment edge (resource to process)
C) Time flow
D) Priority

✔ Correct Answer: B

Reason: Request edge points from process to resource (requesting), assignment edge points from resource to process (allocated).

Tag: Normal

---

### Question 350
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Banker's Algorithm
Difficulty: Hard

Question: What information does Banker's Algorithm require?
A) Only current allocation
B) Maximum need, current allocation, available resources
C) Only available resources
D) No information

✔ Correct Answer: B

Reason: Banker's Algorithm needs maximum resource needs of each process, current allocation, and currently available resources to determine safe states.

Tag: Normal

---

### Question 351
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Safety Algorithm
Difficulty: Hard

Question: What does the safety algorithm determine?
A) System speed
B) Whether system is in safe state
C) Process priority
D) Memory allocation

✔ Correct Answer: B

Reason: Safety algorithm checks if there exists a sequence of process execution where all can complete without deadlock.

Tag: Normal

---

### Question 352
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Resource Request Algorithm
Difficulty: Hard

Question: When does Banker's Algorithm grant a resource request?
A) Always
B) Only if granting leaves system in safe state
C) Never
D) Randomly

✔ Correct Answer: B

Reason: Banker's Algorithm grants request only if resulting state is safe, preventing potential deadlock.

Tag: Normal

---

### Question 353
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Ignorance
Difficulty: Medium

Question: What is the ostrich algorithm?
A) Deadlock prevention
B) Ignoring deadlock problem assuming it's rare
C) Deadlock detection
D) Deadlock avoidance

✔ Correct Answer: B

Reason: Ostrich algorithm ignores deadlock problem, used when deadlocks are rare and cost of prevention/avoidance exceeds cost of occasional restart.

Tag: Normal

---

### Question 354
Domain: Operating Systems
Topic: Memory Management
Subtopic: Base and Limit Registers
Difficulty: Medium

Question: What do base and limit registers provide?
A) No protection
B) Simple memory protection for processes
C) File protection
D) Network protection

✔ Correct Answer: B

Reason: Base register contains smallest legal physical address, limit register contains range size, protecting processes from accessing each other's memory.

Tag: Normal

---

### Question 355
Domain: Operating Systems
Topic: Memory Management
Subtopic: Relocation Register
Difficulty: Medium

Question: What is a relocation register?
A) Static register
B) Register added to logical address to get physical address
C) Limit register
D) No function

✔ Correct Answer: B

Reason: Relocation (base) register value is added to every logical address generated by process to produce physical address.

Tag: Normal

---

### Question 356
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Allocation
Difficulty: Easy

Question: What is the difference between static and dynamic memory allocation?
A) No difference
B) Static at compile time, dynamic at runtime
C) Static is faster
D) Dynamic is obsolete

✔ Correct Answer: B

Reason: Static allocation occurs at compile time with fixed sizes, dynamic allocation occurs at runtime with variable sizes.

Tag: Normal

---

### Question 357
Domain: Operating Systems
Topic: Memory Management
Subtopic: Heap vs Stack
Difficulty: Medium

Question: How does heap differ from stack?
A) No difference
B) Heap for dynamic allocation, stack for function calls
C) Heap is faster
D) Stack is larger

✔ Correct Answer: B

Reason: Heap provides dynamic memory allocation (malloc/new), stack manages function calls and local variables with automatic allocation/deallocation.

Tag: Past Paper

---

### Question 358
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Leak
Difficulty: Easy

Question: What is a memory leak?
A) Hardware failure
B) Allocated memory not freed, causing gradual memory exhaustion
C) Fast memory
D) Memory overflow

✔ Correct Answer: B

Reason: Memory leak occurs when program allocates memory but fails to free it, gradually consuming available memory.

Tag: Normal

---

### Question 359
Domain: Operating Systems
Topic: Memory Management
Subtopic: Garbage Collection
Difficulty: Medium

Question: What is garbage collection?
A) Disk cleanup
B) Automatic memory reclamation of unused objects
C) File deletion
D) Cache clearing

✔ Correct Answer: B

Reason: Garbage collection automatically identifies and reclaims memory occupied by objects no longer reachable by program.

Tag: Normal

---

### Question 360
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Table Entry
Difficulty: Medium

Question: What information does a page table entry typically contain?
A) Only frame number
B) Frame number, valid bit, protection bits, reference bit, dirty bit
C) Only valid bit
D) Process ID only

✔ Correct Answer: B

Reason: PTE contains frame number, valid bit (in memory?), protection bits (r/w/x), reference bit (accessed?), dirty/modified bit.

Tag: Normal

---

### Question 361
Domain: Operating Systems
Topic: Memory Management
Subtopic: Valid-Invalid Bit
Difficulty: Easy

Question: What does the valid bit in page table indicate?
A) Page size
B) Whether page is in physical memory
C) Page number
D) Process priority

✔ Correct Answer: B

Reason: Valid bit indicates if page is currently in physical memory (valid) or on disk (invalid), triggering page fault if invalid.

Tag: Normal

---

### Question 362
Domain: Operating Systems
Topic: Memory Management
Subtopic: Dirty Bit
Difficulty: Medium

Question: What is the purpose of the dirty (modified) bit?
A) Indicates page size
B) Indicates if page has been modified
C) Indicates page age
D) No purpose

✔ Correct Answer: B

Reason: Dirty bit indicates if page has been modified since loading; if set, page must be written back to disk when replaced.

Tag: Normal

---

### Question 363
Domain: Operating Systems
Topic: Memory Management
Subtopic: Reference Bit
Difficulty: Medium

Question: How is the reference bit used?
A) Not used
B) Track page access for replacement algorithms
C) Indicate page size
D) Store page number

✔ Correct Answer: B

Reason: Reference (accessed) bit is set when page is accessed, used by page replacement algorithms like second chance to approximate LRU.

Tag: Normal

---

### Question 364
Domain: Operating Systems
Topic: Memory Management
Subtopic: Copy-on-Write
Difficulty: Hard

Question: What is copy-on-write (COW)?
A) Immediate copying
B) Delay copying until write occurs
C) No copying
D) Copy everything

✔ Correct Answer: B

Reason: COW allows parent and child to share pages initially, copying only when either writes to shared page, improving fork() efficiency.

Tag: Normal

---

### Question 365
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Sharing
Difficulty: Hard

Question: What pages can be shared between processes?
A) All pages
B) Read-only pages like code and libraries
C) No pages
D) Only data pages

✔ Correct Answer: B

Reason: Read-only pages (code, shared libraries) can be shared between processes, reducing memory usage while maintaining isolation.

Tag: Normal

---

### Question 366
Domain: Operating Systems
Topic: Memory Management
Subtopic: Two-Level Paging
Difficulty: Hard

Question: Why use two-level paging?
A) Slower access
B) Avoid keeping entire page table in memory
C) More complexity
D) No benefit

✔ Correct Answer: B

Reason: Two-level paging divides page table into pages, keeping only active portions in memory, reducing memory overhead for large address spaces.

Tag: Normal

---

### Question 367
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Table Size
Difficulty: Hard

Question: For 32-bit address space with 4KB pages, how many page table entries?
A) 1024
B) 1,048,576 (2^20)
C) 4096
D) 65536

✔ Correct Answer: B

Reason: 32-bit address with 4KB (2^12) pages needs 2^20 entries (32-12=20 bits for page number), requiring significant memory.

Tag: Normal

---

### Question 368
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation with Paging
Difficulty: Hard

Question: What does segmentation with paging combine?
A) Nothing
B) Logical segmentation view with physical paging implementation
C) Two paging schemes
D) Two segmentation schemes

✔ Correct Answer: B

Reason: Combines segmentation's logical organization with paging's physical memory management, providing both programmer convenience and efficient memory use.

Tag: Normal

---

### Question 369
Domain: Operating Systems
Topic: Memory Management
Subtopic: Translation Process
Difficulty: Medium

Question: What is the order of address translation with paging?
A) Physical to logical
B) Logical page number → page table → physical frame number
C) No translation
D) Random translation

✔ Correct Answer: B

Reason: CPU generates logical address (page number + offset), page table maps page to frame, offset added to frame address for physical address.

Tag: Normal

---

### Question 370
Domain: Operating Systems
Topic: Memory Management
Subtopic: Effective Memory Access Time
Difficulty: Hard

Question: If memory access takes 100ns and TLB access takes 20ns with 80% hit ratio, what is effective access time?
A) 100ns
B) 140ns
C) 120ns
D) 200ns

✔ Correct Answer: B

Reason: EAT = 0.8(20+100) + 0.2(20+100+100) = 96 + 44 = 140ns. TLB hit: TLB+memory; TLB miss: TLB+page table+memory.

Tag: Past Paper

---

### Question 371
Domain: Operating Systems
Topic: Memory Management
Subtopic: Prepaging
Difficulty: Hard

Question: What is prepaging?
A) No paging
B) Loading pages before they're referenced
C) Delayed paging
D) Random paging

✔ Correct Answer: B

Reason: Prepaging attempts to load pages before they're referenced based on prediction, reducing page faults but may waste I/O if predictions wrong.

Tag: Normal

---

### Question 372
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Size Selection
Difficulty: Hard

Question: What is a tradeoff in selecting page size?
A) No tradeoff
B) Smaller pages reduce internal fragmentation but increase page table size
C) Larger is always better
D) Size doesn't matter

✔ Correct Answer: B

Reason: Small pages reduce internal fragmentation and improve locality but increase page table size and overhead; large pages have opposite effects.

Tag: Normal

---

### Question 373
Domain: Operating Systems
Topic: Memory Management
Subtopic: LFU Page Replacement
Difficulty: Hard

Question: What is LFU page replacement?
A) Most frequently used
B) Least frequently used page replaced
C) Random replacement
D) FIFO variant

✔ Correct Answer: B

Reason: LFU (Least Frequently Used) replaces page with lowest reference count, but may retain old pages no longer needed.

Tag: Normal

---

### Question 374
Domain: Operating Systems
Topic: Memory Management
Subtopic: MFU Page Replacement
Difficulty: Hard

Question: What is the logic behind MFU page replacement?
A) No logic
B) Page with highest count probably just brought in
C) Random selection
D) Oldest page

✔ Correct Answer: B

Reason: MFU (Most Frequently Used) assumes page with highest count was just brought in and won't be used soon, though rarely used in practice.

Tag: Normal

---

### Question 375
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Buffering
Difficulty: Hard

Question: What is page buffering?
A) No buffering
B) Maintaining pool of free frames for quick allocation
C) Disk buffering
D) Network buffering

✔ Correct Answer: B

Reason: Page buffering keeps pool of free frames and modified page list, allowing quick page fault handling and batch writing of dirty pages.

Tag: Normal

---

### Question 376
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Mounting
Difficulty: Medium

Question: What happens when a file system is mounted?
A) File system deleted
B) File system attached to directory tree at mount point
C) File system created
D) File system formatted

✔ Correct Answer: B

Reason: Mounting attaches file system to existing directory tree at specified mount point, making its contents accessible.

Tag: Normal

---

### Question 377
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Types
Difficulty: Easy

Question: Which is a common file system type?
A) TCP
B) ext4, NTFS, FAT32
C) HTTP
D) FTP

✔ Correct Answer: B

Reason: Common file systems include ext4 (Linux), NTFS (Windows), FAT32 (portable), each with different features and performance characteristics.

Tag: Normal

---

### Question 378
Domain: Operating Systems
Topic: File System Management
Subtopic: Metadata
Difficulty: Easy

Question: What is file metadata?
A) File content
B) Information about file (size, permissions, timestamps)
C) File name only
D) File type only

✔ Correct Answer: B

Reason: Metadata is data about data, including file attributes like size, owner, permissions, creation/modification times, location.

Tag: Normal

---

### Question 379
Domain: Operating Systems
Topic: File System Management
Subtopic: File Locking
Difficulty: Medium

Question: What is file locking?
A) Encrypting file
B) Preventing concurrent access conflicts
C) Deleting file
D) Compressing file

✔ Correct Answer: B

Reason: File locking prevents conflicts when multiple processes access same file, using shared locks (read) or exclusive locks (write).

Tag: Normal

---

### Question 380
Domain: Operating Systems
Topic: File System Management
Subtopic: Advisory vs Mandatory Locking
Difficulty: Hard

Question: How does advisory locking differ from mandatory locking?
A) No difference
B) Advisory is voluntary, mandatory is enforced by OS
C) Advisory is faster
D) Mandatory is obsolete

✔ Correct Answer: B

Reason: Advisory locking relies on processes cooperating to check locks; mandatory locking is enforced by OS, preventing access to locked files.

Tag: Normal

---

### Question 381
Domain: Operating Systems
Topic: File System Management
Subtopic: Consistency Checking
Difficulty: Medium

Question: What is file system consistency checking?
A) Checking file content
B) Verifying file system structure integrity
C) Checking file size
D) Checking file names

✔ Correct Answer: B

Reason: Consistency checking (fsck, chkdsk) verifies file system metadata integrity, detecting and repairing inconsistencies from crashes or errors.

Tag: Normal

---

### Question 382
Domain: Operating Systems
Topic: File System Management
Subtopic: Log-Structured File System
Difficulty: Hard

Question: What characterizes log-structured file systems?
A) Random writes
B) All writes appended to log sequentially
C) In-place updates
D) No structure

✔ Correct Answer: B

Reason: Log-structured file systems write all modifications sequentially to log, optimizing write performance and simplifying crash recovery.

Tag: Normal

---

### Question 383
Domain: Operating Systems
Topic: File System Management
Subtopic: Extent-Based Allocation
Difficulty: Hard

Question: What is extent-based allocation?
A) Single block allocation
B) Allocating contiguous blocks as single extent
C) Random allocation
D) No allocation

✔ Correct Answer: B

Reason: Extent is contiguous block of disk space; extent-based allocation reduces metadata overhead and improves sequential access performance.

Tag: Normal

---

### Question 384
Domain: Operating Systems
Topic: File System Management
Subtopic: B-Tree
Difficulty: Hard

Question: Why are B-trees used in file systems?
A) Simple structure
B) Efficient searching and balanced structure for large datasets
C) Small size
D) No reason

✔ Correct Answer: B

Reason: B-trees provide efficient searching, insertion, and deletion with balanced structure, ideal for indexing large file systems and databases.

Tag: Normal

---

### Question 385
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Partitioning
Difficulty: Easy

Question: What is disk partitioning?
A) Disk deletion
B) Dividing disk into separate logical sections
C) Disk formatting
D) Disk encryption

✔ Correct Answer: B

Reason: Partitioning divides physical disk into separate logical sections, each potentially with different file system or purpose.

Tag: Normal

---

### Question 386
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Swap Space
Difficulty: Medium

Question: What is swap space?
A) File storage
B) Disk area for swapping pages/processes
C) Cache
D) Boot area

✔ Correct Answer: B

Reason: Swap space is disk area used for swapping pages or entire processes between memory and disk in virtual memory systems.

Tag: Normal

---

### Question 387
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Defragmentation
Difficulty: Easy

Question: What is disk defragmentation?
A) Deleting files
B) Reorganizing files to be contiguous
C) Formatting disk
D) Partitioning disk

✔ Correct Answer: B

Reason: Defragmentation reorganizes file fragments to be contiguous, improving sequential access performance on traditional hard drives.

Tag: Normal

---

### Question 388
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID 10
Difficulty: Hard

Question: What does RAID 10 combine?
A) RAID 0 and 1
B) Mirroring and striping
C) RAID 2 and 3
D) No combination

✔ Correct Answer: B

Reason: RAID 10 (1+0) combines mirroring (RAID 1) and striping (RAID 0), providing both performance and redundancy.

Tag: Normal

---

### Question 389
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Hot Spare
Difficulty: Medium

Question: What is a hot spare in RAID?
A) Backup disk
B) Unused disk ready to replace failed disk automatically
C) Active disk
D) Slow disk

✔ Correct Answer: B

Reason: Hot spare is standby disk that automatically replaces failed disk in RAID array, beginning rebuild immediately without manual intervention.

Tag: Normal

---

### Question 390
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Mirroring
Difficulty: Easy

Question: What is disk mirroring?
A) Disk striping
B) Maintaining identical copy of data on two disks
C) Disk partitioning
D) Disk compression

✔ Correct Answer: B

Reason: Disk mirroring (RAID 1) maintains exact duplicate of data on second disk, providing fault tolerance and improved read performance.

Tag: Normal

---

### Question 391
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Polling
Difficulty: Easy

Question: What is polling in I/O?
A) Interrupt-driven
B) CPU repeatedly checking device status
C) DMA
D) No checking

✔ Correct Answer: B

Reason: Polling has CPU repeatedly check device status in loop until device is ready, simple but wastes CPU cycles.

Tag: Normal

---

### Question 392
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Interrupt Handling
Difficulty: Medium

Question: What happens during interrupt handling?
A) Nothing
B) Save state, execute handler, restore state
C) System crash
D) Ignore interrupt

✔ Correct Answer: B

Reason: Interrupt handling saves current execution state, executes interrupt service routine, then restores state to resume interrupted process.

Tag: Normal

---

### Question 393
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Interrupt Vector
Difficulty: Medium

Question: What is an interrupt vector?
A) Interrupt count
B) Table of addresses of interrupt service routines
C) Interrupt priority
D) No function

✔ Correct Answer: B

Reason: Interrupt vector table contains addresses of interrupt service routines, allowing quick dispatch to appropriate handler.

Tag: Normal

---

### Question 394
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Completion
Difficulty: Medium

Question: How does CPU know I/O operation completed?
A) Polling only
B) Device sends interrupt
C) Guessing
D) Timer

✔ Correct Answer: B

Reason: Device sends interrupt to CPU when I/O operation completes, allowing CPU to process results and continue.

Tag: Normal

---

### Question 395
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Character Devices
Difficulty: Easy

Question: What are character devices?
A) Block devices
B) Devices transferring data as stream of characters
C) Network devices
D) Storage devices

✔ Correct Answer: B

Reason: Character devices (keyboards, serial ports) transfer data as stream of characters without block structure or random access.

Tag: Normal

---

### Question 396
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Block Devices
Difficulty: Easy

Question: What are block devices?
A) Character devices
B) Devices transferring data in fixed-size blocks
C) Network devices
D) Input devices only

✔ Correct Answer: B

Reason: Block devices (disks, SSDs) transfer data in fixed-size blocks and support random access to any block.

Tag: Normal

---

### Question 397
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Matrix
Difficulty: Hard

Question: What is an access matrix?
A) Memory matrix
B) Matrix defining access rights of subjects to objects
C) Network matrix
D) No matrix

✔ Correct Answer: B

Reason: Access matrix is abstract model with rows (subjects/processes) and columns (objects/resources) defining access rights.

Tag: Normal

---

### Question 398
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Capability Lists
Difficulty: Hard

Question: What is a capability list?
A) Process list
B) List of objects and operations a subject can perform
C) File list
D) User list

✔ Correct Answer: B

Reason: Capability list associates with each subject a list of objects it can access and permitted operations, implementing access matrix by rows.

Tag: Normal

---

### Question 399
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control Lists
Difficulty: Medium

Question: How do ACLs implement access matrix?
A) By rows
B) By columns - each object has list of subjects and permissions
C) No implementation
D) Random implementation

✔ Correct Answer: B

Reason: ACLs implement access matrix by columns, associating with each object a list of subjects and their permitted operations.

Tag: Normal

---

### Question 400
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Policies
Difficulty: Medium

Question: What is a security policy?
A) Hardware specification
B) Statement of what is and is not allowed
C) Software license
D) Network protocol

✔ Correct Answer: B

Reason: Security policy defines rules and practices regulating how system manages, protects, and distributes sensitive information and resources.

Tag: Normal

---

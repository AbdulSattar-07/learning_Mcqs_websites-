# Operating Systems - MCQ Batch 01
## Questions 1-100

---

### Question 1
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Fundamentals
Difficulty: Easy

Question: What is the primary purpose of an operating system?
A) To compile programs
B) To manage computer hardware and software resources
C) To provide internet connectivity
D) To create documents

✔ Correct Answer: B

Reason: An operating system acts as an intermediary between users and computer hardware, managing resources like CPU, memory, and I/O devices efficiently.

Tag: Past Paper

---

### Question 2
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Functions
Difficulty: Easy

Question: Which of the following is NOT a function of an operating system?
A) Process management
B) Memory management
C) Virus creation
D) File management

✔ Correct Answer: C

Reason: Operating systems manage processes, memory, files, and I/O devices. Creating viruses is malicious activity, not an OS function.

Tag: Normal

---

### Question 3
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Types
Difficulty: Easy

Question: Which type of operating system allows multiple users to use the computer simultaneously?
A) Single-user OS
B) Multi-user OS
C) Real-time OS
D) Embedded OS

✔ Correct Answer: B

Reason: Multi-user operating systems like UNIX and Linux allow multiple users to access the system concurrently with proper resource allocation and security.

Tag: Normal

---

### Question 4
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Batch Systems
Difficulty: Medium

Question: In batch operating systems, what happens to jobs?
A) Executed immediately upon submission
B) Grouped and executed without user interaction
C) Require constant user intervention
D) Cannot be executed

✔ Correct Answer: B

Reason: Batch systems collect similar jobs into batches and execute them sequentially without user interaction, maximizing CPU utilization.

Tag: Past Paper

---

### Question 5
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Time-Sharing Systems
Difficulty: Medium

Question: What is the main advantage of time-sharing operating systems?
A) Faster execution of single programs
B) Multiple users can interact with the system simultaneously
C) Lower hardware requirements
D) No need for scheduling

✔ Correct Answer: B

Reason: Time-sharing systems use CPU scheduling and multiprogramming to provide each user with a small portion of time, creating the illusion of dedicated access.

Tag: Normal

---

### Question 6
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Real-Time Systems
Difficulty: Medium

Question: Which characteristic is essential for real-time operating systems?
A) Maximum throughput
B) Deterministic response time
C) User-friendly interface
D) Large storage capacity

✔ Correct Answer: B

Reason: Real-time systems must respond to inputs within a guaranteed time constraint, making deterministic timing critical for applications like medical devices and industrial control.

Tag: Normal

---

### Question 7
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Distributed Systems
Difficulty: Hard

Question: What is the primary goal of a distributed operating system?
A) Run on a single processor
B) Make multiple computers appear as a single system
C) Reduce network traffic
D) Eliminate the need for memory

✔ Correct Answer: B

Reason: Distributed OS coordinates multiple independent computers to work together, presenting users with a unified system while distributing computation and resources.

Tag: Normal

---

### Question 8
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls
Difficulty: Medium

Question: What is a system call?
A) A call between two users
B) An interface between a process and the operating system
C) A hardware interrupt
D) A network protocol

✔ Correct Answer: B

Reason: System calls provide a programmatic interface for processes to request services from the operating system kernel, such as file operations or process creation.

Tag: Past Paper

---

### Question 9
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Kernel
Difficulty: Easy

Question: What is the kernel in an operating system?
A) The user interface
B) The core component that manages system resources
C) An application program
D) A file system

✔ Correct Answer: B

Reason: The kernel is the central component of an OS that has complete control over system resources, managing hardware and providing essential services.

Tag: Normal

---

### Question 10
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Monolithic Kernel
Difficulty: Medium

Question: What characterizes a monolithic kernel?
A) All OS services run in user space
B) All OS services run in kernel space as a single program
C) Services are distributed across network
D) No services are provided

✔ Correct Answer: B

Reason: Monolithic kernels run all operating system services in kernel mode as a single large process, providing fast performance but less modularity.

Tag: Normal

---

### Question 11
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Microkernel
Difficulty: Hard

Question: What is the main advantage of a microkernel architecture?
A) Faster system calls
B) Better modularity and easier maintenance
C) Larger kernel size
D) No need for inter-process communication

✔ Correct Answer: B

Reason: Microkernels keep only essential services in kernel space, moving other services to user space, improving modularity, reliability, and ease of maintenance.

Tag: Normal

---

### Question 12
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Layered Approach
Difficulty: Medium

Question: In a layered operating system structure, which layer is at the bottom?
A) User interface
B) Hardware
C) File system
D) Application layer

✔ Correct Answer: B

Reason: Layered OS architecture is organized hierarchically with hardware at the bottom (Layer 0) and user interface at the top, each layer using services of lower layers.

Tag: Normal

---

### Question 13
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Concept
Difficulty: Easy

Question: What is a process?
A) A program stored on disk
B) A program in execution
C) A compiled program
D) A text file

✔ Correct Answer: B

Reason: A process is an active entity representing a program in execution, including program counter, registers, and memory contents, while a program is a passive entity.

Tag: Past Paper

---

### Question 14
Domain: Operating Systems
Topic: Process Management
Subtopic: Process States
Difficulty: Easy

Question: Which of the following is NOT a typical process state?
A) New
B) Running
C) Compiled
D) Waiting

✔ Correct Answer: C

Reason: Standard process states are New, Ready, Running, Waiting (Blocked), and Terminated. "Compiled" refers to program preparation, not process execution state.

Tag: Normal

---

### Question 15
Domain: Operating Systems
Topic: Process Management
Subtopic: Process State Transitions
Difficulty: Medium

Question: When does a process move from Running state to Waiting state?
A) When it completes execution
B) When it requests I/O or waits for an event
C) When it's created
D) When CPU is allocated to it

✔ Correct Answer: B

Reason: A process transitions to Waiting state when it cannot continue execution until an event occurs, such as I/O completion or resource availability.

Tag: Past Paper

---

### Question 16
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Control Block
Difficulty: Medium

Question: What information does a Process Control Block (PCB) contain?
A) Only the program code
B) Process state, program counter, CPU registers, and scheduling information
C) Only memory addresses
D) User interface data

✔ Correct Answer: B

Reason: PCB is a data structure containing all information about a process: state, program counter, registers, memory limits, open files, and scheduling data.

Tag: Normal

---

### Question 17
Domain: Operating Systems
Topic: Process Management
Subtopic: Context Switch
Difficulty: Medium

Question: What is a context switch?
A) Switching between user and kernel mode
B) Saving the state of one process and loading another
C) Changing the operating system
D) Switching between applications

✔ Correct Answer: B

Reason: Context switching involves saving the current process's state in its PCB and loading the saved state of another process, enabling multitasking.

Tag: Past Paper

---

### Question 18
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Creation
Difficulty: Easy

Question: In UNIX/Linux, which system call is used to create a new process?
A) exec()
B) fork()
C) wait()
D) exit()

✔ Correct Answer: B

Reason: fork() creates a new process by duplicating the calling process. The new process (child) is a copy of the parent with a different process ID.

Tag: Past Paper

---

### Question 19
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Termination
Difficulty: Easy

Question: Which system call is used to terminate a process in UNIX?
A) kill()
B) stop()
C) exit()
D) end()

✔ Correct Answer: C

Reason: exit() system call terminates the calling process, returning an exit status to the parent process and releasing allocated resources.

Tag: Normal

---

### Question 20
Domain: Operating Systems
Topic: Process Management
Subtopic: Parent-Child Relationship
Difficulty: Medium

Question: What happens when a parent process terminates before its child processes?
A) Child processes are automatically terminated
B) Child processes become orphan processes
C) Child processes cannot execute
D) System crashes

✔ Correct Answer: B

Reason: When a parent terminates before children, the children become orphans and are typically adopted by the init process (PID 1) in UNIX systems.

Tag: Normal

---

### Question 21
Domain: Operating Systems
Topic: Process Management
Subtopic: Zombie Process
Difficulty: Hard

Question: What is a zombie process?
A) A process that consumes too much CPU
B) A terminated process whose entry remains in process table
C) A process that cannot be killed
D) A suspended process

✔ Correct Answer: B

Reason: A zombie is a process that has completed execution but still has an entry in the process table, waiting for its parent to read its exit status.

Tag: Normal

---

### Question 22
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Criteria
Difficulty: Easy

Question: Which scheduling criterion measures the time from process submission to completion?
A) Waiting time
B) Response time
C) Turnaround time
D) Throughput

✔ Correct Answer: C

Reason: Turnaround time is the total time from process submission to completion, including waiting time, execution time, and I/O time.

Tag: Past Paper

---

### Question 23
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Criteria
Difficulty: Easy

Question: What does CPU utilization measure?
A) Number of processes completed
B) Percentage of time CPU is busy
C) Time process waits in ready queue
D) Time to first response

✔ Correct Answer: B

Reason: CPU utilization is the percentage of time the CPU is actively executing processes, ideally kept high (40-90%) for efficient system performance.

Tag: Normal

---

### Question 24
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: FCFS Scheduling
Difficulty: Easy

Question: What does FCFS stand for in CPU scheduling?
A) First Come First Served
B) Fast CPU First Scheduled
C) First Created First Started
D) Final Check First System

✔ Correct Answer: A

Reason: FCFS is the simplest scheduling algorithm where processes are executed in the order they arrive in the ready queue.

Tag: Past Paper

---

### Question 25
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: FCFS Scheduling
Difficulty: Medium

Question: What is the main disadvantage of FCFS scheduling?
A) Complex implementation
B) Convoy effect causing poor average waiting time
C) Starvation of processes
D) High context switch overhead

✔ Correct Answer: B

Reason: FCFS suffers from the convoy effect where short processes wait for long processes to complete, resulting in poor average waiting time.

Tag: Normal

---

### Question 26
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: SJF Scheduling
Difficulty: Medium

Question: What does SJF scheduling algorithm optimize?
A) CPU utilization
B) Average waiting time
C) Throughput
D) Response time

✔ Correct Answer: B

Reason: Shortest Job First (SJF) is provably optimal for minimizing average waiting time by executing shortest processes first.

Tag: Past Paper

---

### Question 27
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: SJF Scheduling
Difficulty: Hard

Question: What is the main problem with SJF scheduling?
A) High turnaround time
B) Difficulty in knowing future CPU burst time
C) Low CPU utilization
D) Too many context switches

✔ Correct Answer: B

Reason: SJF requires knowing the length of the next CPU burst in advance, which is impossible to predict accurately, though estimation techniques can be used.

Tag: Normal

---

### Question 28
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Priority Scheduling
Difficulty: Medium

Question: What problem can occur with priority scheduling?
A) Convoy effect
B) Starvation of low-priority processes
C) High turnaround time for all processes
D) Excessive context switching

✔ Correct Answer: B

Reason: Low-priority processes may never execute if high-priority processes keep arriving, causing indefinite blocking or starvation.

Tag: Past Paper

---

### Question 29
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Priority Scheduling
Difficulty: Hard

Question: What technique prevents starvation in priority scheduling?
A) Preemption
B) Aging
C) Time quantum
D) Context switching

✔ Correct Answer: B

Reason: Aging gradually increases the priority of waiting processes over time, ensuring that even low-priority processes eventually get CPU time.

Tag: Normal

---

### Question 30
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Round Robin Scheduling
Difficulty: Easy

Question: What is the time quantum in Round Robin scheduling?
A) Total execution time
B) Small fixed time slice allocated to each process
C) Waiting time
D) Turnaround time

✔ Correct Answer: B

Reason: Time quantum (time slice) is a small unit of time (typically 10-100ms) after which a running process is preempted and moved to the end of ready queue.

Tag: Past Paper

---

### Question 31
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Round Robin Scheduling
Difficulty: Medium

Question: What happens if the time quantum in Round Robin is too large?
A) Better response time
B) Degenerates to FCFS
C) Increased throughput
D) Reduced context switches

✔ Correct Answer: B

Reason: If time quantum is very large, processes complete within one quantum, making Round Robin behave like FCFS, losing its time-sharing benefits.

Tag: Normal

---

### Question 32
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Round Robin Scheduling
Difficulty: Medium

Question: What happens if the time quantum in Round Robin is too small?
A) Better average waiting time
B) Excessive context switching overhead
C) Improved CPU utilization
D) Reduced turnaround time

✔ Correct Answer: B

Reason: Very small time quantum causes frequent context switches, increasing overhead and reducing effective CPU utilization for actual process execution.

Tag: Normal

---

### Question 33
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multilevel Queue Scheduling
Difficulty: Hard

Question: In multilevel queue scheduling, how are processes assigned to queues?
A) Randomly
B) Based on process properties like priority or type
C) First come first served
D) By user choice only

✔ Correct Answer: B

Reason: Processes are permanently assigned to queues based on properties such as process type (system, interactive, batch), priority, or memory requirements.

Tag: Normal

---

### Question 34
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Multilevel Feedback Queue
Difficulty: Hard

Question: How does multilevel feedback queue differ from multilevel queue?
A) No difference
B) Processes can move between queues
C) Only one queue exists
D) No scheduling is performed

✔ Correct Answer: B

Reason: Multilevel feedback queue allows processes to move between queues based on their behavior and CPU burst characteristics, providing adaptive scheduling.

Tag: Normal

---

### Question 35
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Preemptive vs Non-Preemptive
Difficulty: Easy

Question: What is preemptive scheduling?
A) Process runs until completion
B) Process can be interrupted and moved to ready state
C) No scheduling occurs
D) Only I/O bound processes are scheduled

✔ Correct Answer: B

Reason: Preemptive scheduling allows the OS to interrupt a running process and allocate CPU to another process, enabling better responsiveness.

Tag: Past Paper

---

### Question 36
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Algorithms
Difficulty: Medium

Question: Which scheduling algorithm is non-preemptive?
A) Round Robin
B) FCFS
C) Shortest Remaining Time First
D) Priority with preemption

✔ Correct Answer: B

Reason: FCFS is non-preemptive; once a process starts execution, it runs to completion or until it blocks for I/O.

Tag: Normal

---

### Question 37
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Concept
Difficulty: Easy

Question: What is a thread?
A) A separate process
B) A lightweight process or basic unit of CPU utilization
C) A file system component
D) A memory management unit

✔ Correct Answer: B

Reason: A thread is the smallest unit of CPU utilization, consisting of thread ID, program counter, register set, and stack, sharing code and data with other threads.

Tag: Past Paper

---

### Question 38
Domain: Operating Systems
Topic: Thread Management
Subtopic: Benefits of Threads
Difficulty: Easy

Question: What is the main advantage of using threads over processes?
A) More memory usage
B) Lower overhead for creation and context switching
C) Better security
D) Simpler programming

✔ Correct Answer: B

Reason: Threads are lighter than processes, requiring less time and resources for creation, termination, and context switching since they share memory space.

Tag: Normal

---

### Question 39
Domain: Operating Systems
Topic: Thread Management
Subtopic: User Threads vs Kernel Threads
Difficulty: Medium

Question: What characterizes user-level threads?
A) Managed by the kernel
B) Managed by user-level thread library
C) Cannot be created
D) Require kernel mode execution

✔ Correct Answer: B

Reason: User-level threads are managed by user-space thread libraries without kernel intervention, providing fast thread operations but limited by kernel scheduling.

Tag: Normal

---

### Question 40
Domain: Operating Systems
Topic: Thread Management
Subtopic: User Threads vs Kernel Threads
Difficulty: Hard

Question: What is a disadvantage of user-level threads?
A) Slow context switching
B) If one thread blocks, entire process blocks
C) High memory overhead
D) Cannot share data

✔ Correct Answer: B

Reason: Since the kernel sees only the process, not individual user threads, a blocking system call by one thread blocks the entire process.

Tag: Normal

---

### Question 41
Domain: Operating Systems
Topic: Thread Management
Subtopic: Multithreading Models
Difficulty: Hard

Question: In the many-to-one multithreading model, what is the mapping?
A) One user thread to one kernel thread
B) Many user threads to one kernel thread
C) One user thread to many kernel threads
D) Many user threads to many kernel threads

✔ Correct Answer: B

Reason: Many-to-one model maps multiple user threads to a single kernel thread, limiting concurrency since only one thread can access kernel at a time.

Tag: Normal

---

### Question 42
Domain: Operating Systems
Topic: Thread Management
Subtopic: Multithreading Models
Difficulty: Hard

Question: What is the advantage of the one-to-one multithreading model?
A) Less overhead
B) Better concurrency and parallelism
C) Simpler implementation
D) Unlimited threads

✔ Correct Answer: B

Reason: One-to-one model maps each user thread to a kernel thread, providing better concurrency and allowing multiple threads to run in parallel on multiprocessors.

Tag: Normal

---

### Question 43
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Libraries
Difficulty: Easy

Question: Which of the following is a thread library?
A) NTFS
B) POSIX Pthreads
C) FAT32
D) TCP/IP

✔ Correct Answer: B

Reason: POSIX Pthreads is a standard thread library providing API for thread creation, synchronization, and management in UNIX-like systems.

Tag: Normal

---

### Question 44
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Race Condition
Difficulty: Medium

Question: What is a race condition?
A) Competition between processes for CPU
B) Situation where outcome depends on timing of uncontrollable events
C) Fast process execution
D) Scheduling algorithm

✔ Correct Answer: B

Reason: Race condition occurs when multiple processes access shared data concurrently and the outcome depends on the particular order of execution.

Tag: Past Paper

---

### Question 45
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Critical Section
Difficulty: Easy

Question: What is a critical section?
A) Important code segment
B) Code segment accessing shared resources
C) Error handling code
D) Initialization code

✔ Correct Answer: B

Reason: Critical section is a code segment where shared resources are accessed, requiring mutual exclusion to prevent race conditions.

Tag: Past Paper

---

### Question 46
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Critical Section Requirements
Difficulty: Medium

Question: Which is NOT a requirement for a critical section solution?
A) Mutual exclusion
B) Progress
C) Bounded waiting
D) Maximum CPU utilization

✔ Correct Answer: D

Reason: Critical section solutions must satisfy mutual exclusion, progress, and bounded waiting. CPU utilization is a performance metric, not a correctness requirement.

Tag: Normal

---

### Question 47
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Mutual Exclusion
Difficulty: Easy

Question: What does mutual exclusion ensure?
A) All processes execute simultaneously
B) Only one process executes in critical section at a time
C) Processes never wait
D) Maximum throughput

✔ Correct Answer: B

Reason: Mutual exclusion guarantees that when one process is executing in its critical section, no other process can execute in its critical section.

Tag: Past Paper

---

### Question 48
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Peterson's Solution
Difficulty: Hard

Question: How many processes does Peterson's solution handle?
A) One
B) Two
C) Unlimited
D) Three

✔ Correct Answer: B

Reason: Peterson's solution is a software-based mutual exclusion algorithm for two processes, using shared variables to coordinate critical section access.

Tag: Normal

---

### Question 49
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphores
Difficulty: Medium

Question: What is a semaphore?
A) A hardware device
B) A synchronization tool using integer variable
C) A scheduling algorithm
D) A memory management technique

✔ Correct Answer: B

Reason: A semaphore is an integer variable accessed through two atomic operations (wait/P and signal/V) used for process synchronization.

Tag: Past Paper

---

### Question 50
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Binary Semaphore
Difficulty: Easy

Question: What values can a binary semaphore take?
A) Any integer
B) 0 or 1
C) Negative integers
D) Floating point numbers

✔ Correct Answer: B

Reason: Binary semaphores (mutex locks) can only have values 0 or 1, used for mutual exclusion where 1 indicates available and 0 indicates unavailable.

Tag: Normal

---


### Question 51
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Counting Semaphore
Difficulty: Medium

Question: What is the range of values for a counting semaphore?
A) 0 to 1
B) Unrestricted integer domain
C) Only positive integers
D) Only negative integers

✔ Correct Answer: B

Reason: Counting semaphores can have any integer value, used to control access to resources with multiple instances, where value indicates available resources.

Tag: Normal

---

### Question 52
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphore Operations
Difficulty: Medium

Question: What does the wait() operation on a semaphore do?
A) Increments the semaphore value
B) Decrements the semaphore value and blocks if negative
C) Resets the semaphore
D) Deletes the semaphore

✔ Correct Answer: B

Reason: wait() (P operation) decrements the semaphore value. If the result is negative, the process is blocked until the semaphore becomes positive.

Tag: Past Paper

---

### Question 53
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Semaphore Operations
Difficulty: Medium

Question: What does the signal() operation on a semaphore do?
A) Decrements the semaphore value
B) Increments the semaphore value and wakes waiting process
C) Blocks the process
D) Terminates the process

✔ Correct Answer: B

Reason: signal() (V operation) increments the semaphore value. If processes are waiting, one is woken up to continue execution.

Tag: Normal

---

### Question 54
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Monitors
Difficulty: Hard

Question: What is a monitor in operating systems?
A) A display device
B) A high-level synchronization construct with mutual exclusion
C) A process scheduler
D) A memory manager

✔ Correct Answer: B

Reason: A monitor is a high-level synchronization construct that encapsulates shared data and procedures, providing automatic mutual exclusion for procedure calls.

Tag: Normal

---

### Question 55
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Classical Synchronization Problems
Difficulty: Hard

Question: In the Producer-Consumer problem, what does the buffer represent?
A) CPU cache
B) Shared memory region for data exchange
C) Process control block
D) File system

✔ Correct Answer: B

Reason: The buffer is a shared memory region where producers place items and consumers remove items, requiring synchronization to prevent race conditions.

Tag: Past Paper

---

### Question 56
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Readers-Writers Problem
Difficulty: Hard

Question: In the Readers-Writers problem, what is allowed?
A) Multiple writers simultaneously
B) Multiple readers simultaneously
C) One reader and one writer simultaneously
D) No concurrent access

✔ Correct Answer: B

Reason: Multiple readers can access shared data simultaneously since reading doesn't modify data, but writers require exclusive access.

Tag: Normal

---

### Question 57
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Dining Philosophers Problem
Difficulty: Hard

Question: What does the Dining Philosophers problem illustrate?
A) CPU scheduling
B) Deadlock and resource allocation issues
C) Memory management
D) File system design

✔ Correct Answer: B

Reason: The Dining Philosophers problem demonstrates challenges in allocating limited resources among multiple processes without deadlock or starvation.

Tag: Normal

---

### Question 58
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Concept
Difficulty: Easy

Question: What is a deadlock?
A) A fast process
B) A situation where processes wait indefinitely for resources
C) A scheduling algorithm
D) A memory allocation technique

✔ Correct Answer: B

Reason: Deadlock is a situation where a set of processes are blocked, each waiting for a resource held by another process in the set.

Tag: Past Paper

---

### Question 59
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Necessary Conditions
Difficulty: Medium

Question: How many necessary conditions must hold simultaneously for deadlock to occur?
A) Two
B) Three
C) Four
D) Five

✔ Correct Answer: C

Reason: Four conditions must hold simultaneously for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait.

Tag: Past Paper

---

### Question 60
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Mutual Exclusion
Difficulty: Easy

Question: What does the mutual exclusion condition for deadlock state?
A) Resources can be shared
B) At least one resource must be held in non-sharable mode
C) All resources are sharable
D) No resources are needed

✔ Correct Answer: B

Reason: Mutual exclusion means at least one resource must be non-sharable, where only one process can use it at a time.

Tag: Normal

---

### Question 61
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Hold and Wait
Difficulty: Medium

Question: What is the hold and wait condition?
A) Process releases all resources before requesting new ones
B) Process holds resources while waiting for additional resources
C) Process never holds resources
D) Process waits without holding resources

✔ Correct Answer: B

Reason: Hold and wait occurs when a process holding at least one resource is waiting to acquire additional resources held by other processes.

Tag: Normal

---

### Question 62
Domain: Operating Systems
Topic: Deadlocks
Subtopic: No Preemption
Difficulty: Medium

Question: What does the no preemption condition mean?
A) Resources can be forcibly taken
B) Resources cannot be forcibly removed from processes
C) All resources are preemptable
D) No resources exist

✔ Correct Answer: B

Reason: No preemption means resources cannot be forcibly taken from a process; they must be voluntarily released by the holding process.

Tag: Normal

---

### Question 63
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Circular Wait
Difficulty: Medium

Question: What is circular wait in deadlock?
A) Processes wait in a line
B) A circular chain of processes each waiting for a resource held by the next
C) Random waiting pattern
D) No waiting occurs

✔ Correct Answer: B

Reason: Circular wait exists when there's a circular chain of processes where each process waits for a resource held by the next process in the chain.

Tag: Past Paper

---

### Question 64
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: How can the hold and wait condition be prevented?
A) Allow preemption
B) Require processes to request all resources at once
C) Use circular wait
D) Ignore deadlocks

✔ Correct Answer: B

Reason: Hold and wait can be prevented by requiring processes to request all needed resources at once before execution, or release all before requesting new ones.

Tag: Normal

---

### Question 65
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Prevention
Difficulty: Hard

Question: How can circular wait be prevented?
A) Allow hold and wait
B) Impose total ordering on resource types
C) Remove mutual exclusion
D) Allow preemption randomly

✔ Correct Answer: B

Reason: Circular wait can be prevented by imposing a total ordering on resource types and requiring processes to request resources in increasing order.

Tag: Normal

---

### Question 66
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Avoidance
Difficulty: Hard

Question: What information does deadlock avoidance require?
A) Past resource usage
B) Future resource requests in advance
C) Current CPU utilization
D) Memory size

✔ Correct Answer: B

Reason: Deadlock avoidance requires advance information about maximum resource needs of each process to make safe allocation decisions.

Tag: Normal

---

### Question 67
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Banker's Algorithm
Difficulty: Hard

Question: What does the Banker's Algorithm ensure?
A) Maximum profit
B) System remains in safe state
C) Fastest execution
D) Minimum memory usage

✔ Correct Answer: B

Reason: Banker's Algorithm is a deadlock avoidance algorithm that ensures the system never enters an unsafe state by simulating resource allocation.

Tag: Past Paper

---

### Question 68
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Safe State
Difficulty: Medium

Question: What is a safe state?
A) No processes are running
B) System can allocate resources to processes in some order avoiding deadlock
C) All processes have completed
D) No resources are allocated

✔ Correct Answer: B

Reason: A safe state exists when there's a sequence of process execution that allows all processes to complete without deadlock.

Tag: Normal

---

### Question 69
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Unsafe State
Difficulty: Medium

Question: Does an unsafe state always lead to deadlock?
A) Yes, always
B) No, it may lead to deadlock
C) Never leads to deadlock
D) Only in single processor systems

✔ Correct Answer: B

Reason: An unsafe state doesn't guarantee deadlock but indicates the possibility of deadlock. The system may still complete successfully.

Tag: Normal

---

### Question 70
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Detection
Difficulty: Hard

Question: When is deadlock detection used?
A) To prevent deadlocks
B) When system allows deadlocks to occur and detects them
C) To avoid deadlocks
D) Never used

✔ Correct Answer: B

Reason: Deadlock detection allows deadlocks to occur, then uses algorithms to detect them by examining resource allocation graphs or matrices.

Tag: Normal

---

### Question 71
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Resource Allocation Graph
Difficulty: Hard

Question: In a resource allocation graph, what does a cycle indicate in a single-instance resource system?
A) No deadlock
B) Deadlock exists
C) Safe state
D) High CPU usage

✔ Correct Answer: B

Reason: In systems with single-instance resources, a cycle in the resource allocation graph is both necessary and sufficient for deadlock.

Tag: Normal

---

### Question 72
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Recovery
Difficulty: Medium

Question: What is one method of deadlock recovery?
A) Ignore the deadlock
B) Process termination
C) Prevent future deadlocks
D) Increase resources

✔ Correct Answer: B

Reason: Deadlock recovery can be achieved by terminating one or more processes in the deadlock cycle to break the circular wait.

Tag: Normal

---

### Question 73
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Recovery
Difficulty: Hard

Question: What is resource preemption in deadlock recovery?
A) Preventing resource allocation
B) Forcibly taking resources from processes
C) Deleting resources
D) Creating new resources

✔ Correct Answer: B

Reason: Resource preemption involves forcibly taking resources from deadlocked processes and giving them to others, requiring rollback and restart mechanisms.

Tag: Normal

---

### Question 74
Domain: Operating Systems
Topic: Memory Management
Subtopic: Address Binding
Difficulty: Medium

Question: When does compile-time address binding occur?
A) During program execution
B) When absolute code location is known at compile time
C) During loading
D) Never occurs

✔ Correct Answer: B

Reason: Compile-time binding generates absolute code when memory location is known in advance, requiring recompilation if starting location changes.

Tag: Normal

---

### Question 75
Domain: Operating Systems
Topic: Memory Management
Subtopic: Address Binding
Difficulty: Medium

Question: What is load-time address binding?
A) Binding during compilation
B) Binding when program is loaded into memory
C) Binding during execution
D) No binding occurs

✔ Correct Answer: B

Reason: Load-time binding generates relocatable code at compile time, with final binding to physical addresses occurring when the program is loaded.

Tag: Normal

---

### Question 76
Domain: Operating Systems
Topic: Memory Management
Subtopic: Logical vs Physical Address
Difficulty: Easy

Question: What is a logical address?
A) Physical memory location
B) Address generated by CPU during execution
C) Hard disk address
D) Network address

✔ Correct Answer: B

Reason: Logical (virtual) address is generated by the CPU and must be translated to physical address by the Memory Management Unit (MMU).

Tag: Past Paper

---

### Question 77
Domain: Operating Systems
Topic: Memory Management
Subtopic: MMU
Difficulty: Medium

Question: What is the function of the Memory Management Unit (MMU)?
A) Allocate memory
B) Translate logical addresses to physical addresses
C) Manage files
D) Schedule processes

✔ Correct Answer: B

Reason: MMU is a hardware device that translates logical addresses generated by CPU to physical addresses in main memory.

Tag: Normal

---

### Question 78
Domain: Operating Systems
Topic: Memory Management
Subtopic: Swapping
Difficulty: Easy

Question: What is swapping in memory management?
A) Exchanging data between processes
B) Moving processes between main memory and disk
C) Sorting memory contents
D) Deleting processes

✔ Correct Answer: B

Reason: Swapping temporarily moves a process from main memory to backing store (disk) and brings it back later, enabling multiprogramming with limited memory.

Tag: Past Paper

---

### Question 79
Domain: Operating Systems
Topic: Memory Management
Subtopic: Contiguous Allocation
Difficulty: Medium

Question: What is contiguous memory allocation?
A) Memory scattered across disk
B) Each process occupies a single contiguous section of memory
C) Memory shared among all processes
D) No memory allocation

✔ Correct Answer: B

Reason: Contiguous allocation assigns each process a single continuous block of memory, simple but can lead to fragmentation.

Tag: Normal

---

### Question 80
Domain: Operating Systems
Topic: Memory Management
Subtopic: Fixed Partitioning
Difficulty: Medium

Question: What is a disadvantage of fixed partitioning?
A) Complex implementation
B) Internal fragmentation
C) No fragmentation
D) Unlimited processes

✔ Correct Answer: B

Reason: Fixed partitioning divides memory into fixed-size partitions, causing internal fragmentation when process size is smaller than partition size.

Tag: Normal

---

### Question 81
Domain: Operating Systems
Topic: Memory Management
Subtopic: Dynamic Partitioning
Difficulty: Medium

Question: What problem does dynamic partitioning face?
A) Internal fragmentation
B) External fragmentation
C) No fragmentation
D) Too much memory

✔ Correct Answer: B

Reason: Dynamic partitioning allocates exactly the memory needed, avoiding internal fragmentation but causing external fragmentation as processes load and terminate.

Tag: Normal

---

### Question 82
Domain: Operating Systems
Topic: Memory Management
Subtopic: Fragmentation
Difficulty: Easy

Question: What is external fragmentation?
A) Wasted space within allocated memory
B) Free memory scattered in small blocks
C) No free memory
D) Too much free memory

✔ Correct Answer: B

Reason: External fragmentation occurs when free memory is broken into small scattered blocks, preventing allocation of large contiguous blocks.

Tag: Past Paper

---

### Question 83
Domain: Operating Systems
Topic: Memory Management
Subtopic: Fragmentation
Difficulty: Easy

Question: What is internal fragmentation?
A) Free memory between partitions
B) Wasted space within allocated memory partition
C) No wasted space
D) Memory on disk

✔ Correct Answer: B

Reason: Internal fragmentation is wasted space within an allocated memory partition when the allocated space is larger than requested.

Tag: Normal

---

### Question 84
Domain: Operating Systems
Topic: Memory Management
Subtopic: Compaction
Difficulty: Medium

Question: What is memory compaction?
A) Compressing memory contents
B) Moving processes to create one large free block
C) Deleting processes
D) Expanding memory

✔ Correct Answer: B

Reason: Compaction shuffles memory contents to place all free memory together in one large block, solving external fragmentation but requiring relocation.

Tag: Normal

---

### Question 85
Domain: Operating Systems
Topic: Memory Management
Subtopic: Paging
Difficulty: Medium

Question: What is paging?
A) Printing pages
B) Dividing memory into fixed-size pages
C) Sorting memory
D) Deleting memory

✔ Correct Answer: B

Reason: Paging divides physical memory into fixed-size blocks (frames) and logical memory into same-size blocks (pages), eliminating external fragmentation.

Tag: Past Paper

---

### Question 86
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Table
Difficulty: Medium

Question: What is the purpose of a page table?
A) Store process data
B) Map logical pages to physical frames
C) Schedule processes
D) Manage files

✔ Correct Answer: B

Reason: Page table maintains the mapping between logical page numbers and physical frame numbers for address translation.

Tag: Normal

---

### Question 87
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Size
Difficulty: Hard

Question: What is a disadvantage of large page size?
A) More page table entries
B) Increased internal fragmentation
C) Slower address translation
D) More external fragmentation

✔ Correct Answer: B

Reason: Larger pages increase internal fragmentation as the last page of a process may have significant unused space.

Tag: Normal

---

### Question 88
Domain: Operating Systems
Topic: Memory Management
Subtopic: TLB
Difficulty: Hard

Question: What is a Translation Lookaside Buffer (TLB)?
A) A disk cache
B) A fast cache for page table entries
C) A process queue
D) A file buffer

✔ Correct Answer: B

Reason: TLB is a small, fast hardware cache that stores recent page table entries, speeding up address translation by avoiding main memory access.

Tag: Normal

---

### Question 89
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation
Difficulty: Medium

Question: What is segmentation?
A) Fixed-size memory division
B) Variable-size logical memory division based on program structure
C) No memory division
D) Disk partitioning

✔ Correct Answer: B

Reason: Segmentation divides memory into variable-size segments based on logical program structure (code, data, stack), supporting programmer's view.

Tag: Normal

---

### Question 90
Domain: Operating Systems
Topic: Memory Management
Subtopic: Segmentation vs Paging
Difficulty: Hard

Question: What is a key difference between paging and segmentation?
A) Paging is visible to programmer
B) Paging uses fixed-size blocks, segmentation uses variable-size
C) Segmentation is faster
D) No difference

✔ Correct Answer: B

Reason: Paging uses fixed-size pages (invisible to programmer), while segmentation uses variable-size segments (visible to programmer, matching logical structure).

Tag: Normal

---

### Question 91
Domain: Operating Systems
Topic: Memory Management
Subtopic: Virtual Memory
Difficulty: Easy

Question: What is virtual memory?
A) Memory on disk only
B) Technique allowing execution of processes not completely in memory
C) Physical RAM
D) Cache memory

✔ Correct Answer: B

Reason: Virtual memory allows execution of processes larger than physical memory by keeping only needed parts in memory and rest on disk.

Tag: Past Paper

---

### Question 92
Domain: Operating Systems
Topic: Memory Management
Subtopic: Demand Paging
Difficulty: Medium

Question: What is demand paging?
A) Loading all pages at start
B) Loading pages only when needed
C) Never loading pages
D) Deleting pages

✔ Correct Answer: B

Reason: Demand paging loads pages into memory only when they are referenced, reducing initial load time and memory requirements.

Tag: Normal

---

### Question 93
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault
Difficulty: Easy

Question: What is a page fault?
A) Hardware error
B) Reference to a page not in memory
C) Disk failure
D) Network error

✔ Correct Answer: B

Reason: Page fault occurs when a process references a page not currently in physical memory, triggering the OS to load it from disk.

Tag: Past Paper

---

### Question 94
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Replacement
Difficulty: Medium

Question: When is page replacement needed?
A) When memory is empty
B) When memory is full and a new page must be loaded
C) During system boot
D) Never needed

✔ Correct Answer: B

Reason: Page replacement is needed when all frames are occupied and a page fault occurs, requiring selection of a victim page to replace.

Tag: Normal

---

### Question 95
Domain: Operating Systems
Topic: Memory Management
Subtopic: FIFO Page Replacement
Difficulty: Easy

Question: What does FIFO page replacement algorithm replace?
A) Most recently used page
B) Oldest page in memory
C) Largest page
D) Random page

✔ Correct Answer: B

Reason: FIFO (First-In-First-Out) replaces the oldest page in memory, simple to implement but may replace frequently used pages.

Tag: Normal

---

### Question 96
Domain: Operating Systems
Topic: Memory Management
Subtopic: Optimal Page Replacement
Difficulty: Hard

Question: What does the optimal page replacement algorithm replace?
A) Oldest page
B) Page that will not be used for longest time
C) Most recently used page
D) Random page

✔ Correct Answer: B

Reason: Optimal algorithm replaces the page that will not be used for the longest time in the future, minimizing page faults but requiring future knowledge.

Tag: Normal

---

### Question 97
Domain: Operating Systems
Topic: Memory Management
Subtopic: LRU Page Replacement
Difficulty: Medium

Question: What does LRU page replacement algorithm replace?
A) Oldest page
B) Page not used for longest time in past
C) Most recently used page
D) Random page

✔ Correct Answer: B

Reason: LRU (Least Recently Used) replaces the page that hasn't been used for the longest time, approximating optimal algorithm using past behavior.

Tag: Past Paper

---

### Question 98
Domain: Operating Systems
Topic: Memory Management
Subtopic: Thrashing
Difficulty: Hard

Question: What is thrashing?
A) Fast execution
B) Excessive paging activity degrading performance
C) Efficient memory usage
D) Process termination

✔ Correct Answer: B

Reason: Thrashing occurs when a process spends more time paging than executing, caused by insufficient frames allocated to processes.

Tag: Normal

---

### Question 99
Domain: Operating Systems
Topic: Memory Management
Subtopic: Working Set
Difficulty: Hard

Question: What is a working set?
A) Set of all pages
B) Set of pages actively used by process in recent time window
C) Set of free pages
D) Set of disk pages

✔ Correct Answer: B

Reason: Working set is the set of pages referenced by a process during a time window, used to determine minimum frames needed to prevent thrashing.

Tag: Normal

---

### Question 100
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Fault Frequency
Difficulty: Hard

Question: What does high page fault frequency indicate?
A) Efficient execution
B) Process needs more frames
C) Too much memory allocated
D) Fast CPU

✔ Correct Answer: B

Reason: High page fault frequency indicates the process doesn't have enough frames allocated, requiring more memory to reduce paging overhead.

Tag: Normal

---

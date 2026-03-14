# Operating Systems - MCQ Batch 08
## Questions 701-800

---

### Question 701
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Mobile Operating Systems
Difficulty: Medium

Question: What distinguishes mobile OS from desktop OS?
A) No difference
B) Power management, touch interface, app sandboxing
C) Slower performance
D) Less features

✔ Correct Answer: B

Reason: Mobile OS emphasize power efficiency, touch-optimized interfaces, app sandboxing for security, and resource constraints.

Tag: Normal

---

### Question 702
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Cloud Operating Systems
Difficulty: Hard

Question: What characterizes cloud operating systems?
A) Local only
B) Distributed resource management across data centers
C) Single machine
D) No networking

✔ Correct Answer: B

Reason: Cloud OS manage distributed resources across data centers, providing virtualization, orchestration, and scalability.

Tag: Normal

---

### Question 703
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: Microservices
Difficulty: Hard

Question: How do microservices relate to OS design?
A) No relation
B) Similar to microkernel - modular, independent services
C) Opposite approach
D) Same as monolithic

✔ Correct Answer: B

Reason: Microservices architecture mirrors microkernel philosophy: small, independent, communicating components with clear interfaces.

Tag: Normal

---

### Question 704
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Container Technology
Difficulty: Hard

Question: What are containers?
A) Virtual machines
B) Lightweight isolation using OS-level virtualization
C) Physical machines
D) No isolation

✔ Correct Answer: B

Reason: Containers provide lightweight isolation using OS kernel features (namespaces, cgroups), sharing kernel unlike VMs.

Tag: Normal

---

### Question 705
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Namespaces
Difficulty: Hard

Question: What do Linux namespaces provide?
A) No isolation
B) Process isolation for PIDs, network, mounts, etc.
C) Only PID isolation
D) Full virtualization

✔ Correct Answer: B

Reason: Namespaces isolate process views of system resources (PID, network, mount, IPC, user), enabling containerization.

Tag: Normal

---

### Question 706
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Control Groups
Difficulty: Hard

Question: What are cgroups in Linux?
A) Process groups
B) Resource limiting and accounting mechanism
C) User groups
D) No groups

✔ Correct Answer: B

Reason: Cgroups (control groups) limit, account for, and isolate resource usage (CPU, memory, I/O) of process groups.

Tag: Normal

---

### Question 707
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls Performance
Difficulty: Hard

Question: Why are system calls expensive?
A) Not expensive
B) Mode switch, context save/restore, parameter validation
C) Simple operations
D) No overhead

✔ Correct Answer: B

Reason: System calls require mode switch to kernel, saving/restoring context, parameter validation, and security checks.

Tag: Normal

---

### Question 708
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: vDSO
Difficulty: Hard

Question: What is vDSO in Linux?
A) Virtual device
B) Virtual shared library for fast system calls
C) Virtual disk
D) No function

✔ Correct Answer: B

Reason: vDSO (virtual dynamic shared object) maps kernel code into user space for fast system calls without mode switch.

Tag: Normal

---

### Question 709
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling Policies
Difficulty: Medium

Question: What is SCHED_BATCH in Linux?
A) Interactive scheduling
B) CPU-intensive batch processes with lower priority
C) Real-time scheduling
D) No scheduling

✔ Correct Answer: B

Reason: SCHED_BATCH is for CPU-intensive batch processes, scheduled less frequently than interactive processes.

Tag: Normal

---

### Question 710
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Scheduling Policies
Difficulty: Hard

Question: What is SCHED_IDLE in Linux?
A) High priority
B) Extremely low priority, runs only when nothing else
C) Normal priority
D) Real-time priority

✔ Correct Answer: B

Reason: SCHED_IDLE is for extremely low priority tasks, scheduled only when no other processes are runnable.

Tag: Normal

---

### Question 711
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Namespaces
Difficulty: Hard

Question: What does PID namespace provide?
A) Global PIDs
B) Isolated PID space, processes see different PIDs
C) No isolation
D) Single PID space

✔ Correct Answer: B

Reason: PID namespace provides isolated PID space; process can have different PIDs in different namespaces.

Tag: Normal

---

### Question 712
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Capabilities
Difficulty: Hard

Question: What are Linux capabilities?
A) No capabilities
B) Fine-grained privileges instead of all-or-nothing root
C) User permissions
D) File permissions

✔ Correct Answer: B

Reason: Capabilities divide root privileges into distinct units (CAP_NET_ADMIN, CAP_SYS_TIME), allowing fine-grained privilege assignment.

Tag: Normal

---

### Question 713
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Resource Limits
Difficulty: Medium

Question: What are ulimits?
A) No limits
B) Per-process resource limits (files, memory, CPU)
C) System limits
D) Network limits

✔ Correct Answer: B

Reason: Ulimits set per-process resource limits including open files, memory, CPU time, preventing resource exhaustion.

Tag: Normal

---

### Question 714
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Scheduling Latency
Difficulty: Hard

Question: What is scheduling latency?
A) Execution time
B) Time from process becoming runnable to actually running
C) Waiting time
D) Turnaround time

✔ Correct Answer: B

Reason: Scheduling latency is delay between process becoming runnable and being scheduled, affecting responsiveness.

Tag: Normal

---

### Question 715
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Preemption Latency
Difficulty: Hard

Question: What is preemption latency?
A) No latency
B) Time to preempt current process and switch to another
C) Execution time
D) Waiting time

✔ Correct Answer: B

Reason: Preemption latency is time required to interrupt current process and context switch to higher-priority process.

Tag: Normal

---

### Question 716
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Real-Time Constraints
Difficulty: Hard

Question: What is a deadline in real-time scheduling?
A) No constraint
B) Time by which task must complete
C) Start time
D) Arrival time

✔ Correct Answer: B

Reason: Deadline is absolute time by which task must complete; missing deadline may cause system failure in hard real-time.

Tag: Normal

---

### Question 717
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Real-Time Constraints
Difficulty: Hard

Question: What is a period in real-time scheduling?
A) Random interval
B) Time between successive task activations
C) Execution time
D) Deadline

✔ Correct Answer: B

Reason: Period is time interval between successive activations of periodic task, determining task frequency.

Tag: Normal

---

### Question 718
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: Schedulability Analysis
Difficulty: Hard

Question: What is schedulability analysis?
A) Random analysis
B) Determining if task set can meet all deadlines
C) Performance analysis
D) No analysis

✔ Correct Answer: B

Reason: Schedulability analysis determines whether given task set with specified timing constraints can be scheduled to meet all deadlines.

Tag: Normal

---

### Question 719
Domain: Operating Systems
Topic: CPU Scheduling
Subtopic: CPU Utilization Bound
Difficulty: Hard

Question: What is the utilization bound for Rate Monotonic scheduling?
A) 100%
B) n(2^(1/n) - 1), approaches 69% as n increases
C) 50%
D) No bound

✔ Correct Answer: B

Reason: Rate Monotonic has utilization bound of n(2^(1/n) - 1), approximately 69% for many tasks, ensuring schedulability.

Tag: Normal

---

### Question 720
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread-Specific Data
Difficulty: Hard

Question: What is thread-specific data (TSD)?
A) Shared data
B) Data unique to each thread
C) Global data
D) No data

✔ Correct Answer: B

Reason: TSD (thread-local storage) provides each thread with its own copy of data, avoiding synchronization for thread-private data.

Tag: Normal

---

### Question 721
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Priorities
Difficulty: Medium

Question: How do thread priorities affect scheduling?
A) No effect
B) Higher priority threads scheduled before lower priority
C) Random scheduling
D) All equal

✔ Correct Answer: B

Reason: Thread priorities influence scheduler decisions; higher priority threads typically get CPU before lower priority threads.

Tag: Normal

---

### Question 722
Domain: Operating Systems
Topic: Thread Management
Subtopic: Thread Signals
Difficulty: Hard

Question: How are signals handled in multithreaded programs?
A) All threads receive
B) Delivered to specific thread or all threads depending on signal
C) No signals
D) Random thread

✔ Correct Answer: B

Reason: Signals can be directed to specific thread (synchronous) or delivered to any thread (asynchronous), requiring careful handling.

Tag: Normal

---

### Question 723
Domain: Operating Systems
Topic: Thread Management
Subtopic: Fork in Multithreaded Programs
Difficulty: Hard

Question: What happens when multithreaded process calls fork()?
A) All threads copied
B) Only calling thread duplicated in child
C) No fork allowed
D) Random threads copied

✔ Correct Answer: B

Reason: fork() in multithreaded program typically duplicates only calling thread in child, avoiding complex state duplication.

Tag: Normal

---

### Question 724
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Lock Granularity
Difficulty: Hard

Question: What is fine-grained locking?
A) Single global lock
B) Many locks protecting small data portions
C) No locks
D) Coarse locks

✔ Correct Answer: B

Reason: Fine-grained locking uses many locks for small data portions, increasing concurrency but adding complexity.

Tag: Normal

---

### Question 725
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Lock Granularity
Difficulty: Hard

Question: What is coarse-grained locking?
A) Many small locks
B) Few locks protecting large data portions
C) No locks
D) Fine locks

✔ Correct Answer: B

Reason: Coarse-grained locking uses few locks for large data portions, simpler but reducing concurrency.

Tag: Normal

---

### Question 726
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Lock Contention
Difficulty: Medium

Question: What is lock contention?
A) No contention
B) Multiple threads competing for same lock
C) Single thread
D) No competition

✔ Correct Answer: B

Reason: Lock contention occurs when multiple threads compete for same lock, causing blocking and reducing parallelism.

Tag: Normal

---

### Question 727
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Lock-Free Data Structures
Difficulty: Hard

Question: What characterizes lock-free data structures?
A) Use locks
B) Use atomic operations, guarantee system-wide progress
C) No synchronization
D) Single-threaded

✔ Correct Answer: B

Reason: Lock-free structures use atomic operations ensuring at least one thread makes progress, avoiding deadlock and priority inversion.

Tag: Normal

---

### Question 728
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Wait-Free Data Structures
Difficulty: Hard

Question: What characterizes wait-free data structures?
A) May wait indefinitely
B) Every operation completes in bounded steps
C) Lock-based
D) No guarantees

✔ Correct Answer: B

Reason: Wait-free structures guarantee every thread completes operation in bounded steps, strongest progress guarantee.

Tag: Normal

---

### Question 729
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: RCU
Difficulty: Hard

Question: What is RCU (Read-Copy-Update)?
A) Write optimization
B) Synchronization allowing concurrent reads with updates
C) Lock mechanism
D) No synchronization

✔ Correct Answer: B

Reason: RCU allows multiple concurrent readers with writers creating new versions, deferring old version removal until safe.

Tag: Normal

---

### Question 730
Domain: Operating Systems
Topic: Concurrency & Synchronization
Subtopic: Seqlocks
Difficulty: Hard

Question: What are seqlocks?
A) Regular locks
B) Locks allowing readers to retry if writer active
C) No locks
D) Write locks only

✔ Correct Answer: B

Reason: Seqlocks use sequence counter; readers check counter before/after, retrying if changed, favoring writers over readers.

Tag: Normal

---

### Question 731
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Detection Frequency
Difficulty: Hard

Question: What determines optimal deadlock detection frequency?
A) Always maximum
B) Balance between overhead and detection delay
C) Never detect
D) Random frequency

✔ Correct Answer: B

Reason: Detection frequency balances CPU overhead of detection algorithm against delay in identifying and recovering from deadlocks.

Tag: Normal

---

### Question 732
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Deadlock Recovery Cost
Difficulty: Hard

Question: What factors affect deadlock recovery cost?
A) No factors
B) Number of processes terminated, work lost, restart overhead
C) Only time
D) Only memory

✔ Correct Answer: B

Reason: Recovery cost includes processes terminated, computation lost, checkpoint/restart overhead, and cascading effects.

Tag: Normal

---

### Question 733
Domain: Operating Systems
Topic: Deadlocks
Subtopic: Timeout-Based Deadlock
Difficulty: Medium

Question: How can timeouts help with deadlocks?
A) Cannot help
B) Process releases resources if cannot acquire within timeout
C) Prevent all deadlocks
D) No effect

✔ Correct Answer: B

Reason: Timeouts allow process to release held resources and retry if cannot acquire needed resources within time limit.

Tag: Normal

---

### Question 734
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Fragmentation
Difficulty: Medium

Question: Which causes more problems in practice?
A) Internal fragmentation
B) External fragmentation
C) Both equal
D) Neither

✔ Correct Answer: B

Reason: External fragmentation more problematic as it prevents allocation even with sufficient total free space; internal fragmentation wastes fixed amount.

Tag: Normal

---

### Question 735
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Allocation Performance
Difficulty: Hard

Question: What affects memory allocator performance?
A) Only speed
B) Speed, fragmentation, scalability, memory overhead
C) Only fragmentation
D) No factors

✔ Correct Answer: B

Reason: Allocator performance involves allocation/deallocation speed, fragmentation control, multithread scalability, and metadata overhead.

Tag: Normal

---

### Question 736
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Allocators
Difficulty: Hard

Question: What is jemalloc?
A) Simple allocator
B) Scalable memory allocator for multithreaded applications
C) Single-threaded allocator
D) No allocator

✔ Correct Answer: B

Reason: jemalloc is high-performance allocator designed for multithreaded applications, reducing contention and fragmentation.

Tag: Normal

---

### Question 737
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Allocators
Difficulty: Hard

Question: What is tcmalloc?
A) Slow allocator
B) Thread-caching malloc for improved performance
C) Single-threaded
D) No caching

✔ Correct Answer: B

Reason: tcmalloc (Thread-Caching Malloc) provides per-thread caches reducing lock contention in multithreaded programs.

Tag: Normal

---

### Question 738
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Replacement Algorithms
Difficulty: Hard

Question: What is the working set clock algorithm?
A) Simple FIFO
B) Combines working set and clock algorithms
C) Random replacement
D) No algorithm

✔ Correct Answer: B

Reason: Working set clock algorithm uses clock hand with working set information for efficient page replacement.

Tag: Normal

---

### Question 739
Domain: Operating Systems
Topic: Memory Management
Subtopic: Page Replacement Algorithms
Difficulty: Hard

Question: What is the WSClock algorithm advantage?
A) No advantages
B) Efficient working set approximation with low overhead
C) Slower
D) More complex only

✔ Correct Answer: B

Reason: WSClock efficiently approximates working set model with lower overhead than pure working set algorithm.

Tag: Normal

---

### Question 740
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Pressure
Difficulty: Medium

Question: What is memory pressure?
A) Physical pressure
B) System state when memory scarce
C) No pressure
D) Disk pressure

✔ Correct Answer: B

Reason: Memory pressure indicates system running low on available memory, triggering reclamation mechanisms.

Tag: Normal

---

### Question 741
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Reclamation
Difficulty: Hard

Question: What is kswapd in Linux?
A) User process
B) Kernel thread performing background page reclamation
C) Swap file
D) No function

✔ Correct Answer: B

Reason: kswapd is kernel thread that performs background page reclamation when memory pressure detected.

Tag: Normal

---

### Question 742
Domain: Operating Systems
Topic: Memory Management
Subtopic: Transparent Huge Pages
Difficulty: Hard

Question: What are transparent huge pages?
A) Small pages
B) Automatic huge page management without application changes
C) Manual pages
D) No pages

✔ Correct Answer: B

Reason: Transparent huge pages automatically use large pages when beneficial, improving TLB efficiency without application modification.

Tag: Normal

---

### Question 743
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Deduplication
Difficulty: Hard

Question: What is memory deduplication?
A) Duplication
B) Merging identical pages to save memory
C) No merging
D) Copying pages

✔ Correct Answer: B

Reason: Memory deduplication (KSM in Linux) identifies and merges identical pages, saving memory in virtualized environments.

Tag: Normal

---

### Question 744
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Ballooning
Difficulty: Hard

Question: What is memory ballooning in virtualization?
A) Inflating memory
B) Guest returns memory to host via balloon driver
C) No mechanism
D) Fixed memory

✔ Correct Answer: B

Reason: Memory ballooning allows hypervisor to reclaim memory from guest by inflating balloon driver, making guest free pages.

Tag: Normal

---

### Question 745
Domain: Operating Systems
Topic: Memory Management
Subtopic: NUMA Awareness
Difficulty: Hard

Question: Why is NUMA awareness important?
A) Not important
B) Optimize memory allocation for local node access
C) Random allocation
D) No optimization

✔ Correct Answer: B

Reason: NUMA-aware allocation places memory on same node as accessing CPU, reducing remote memory access latency.

Tag: Normal

---

### Question 746
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Snapshots
Difficulty: Hard

Question: What are file system snapshots?
A) Photos
B) Point-in-time read-only copy of file system
C) Backups
D) No copies

✔ Correct Answer: B

Reason: Snapshots create point-in-time view of file system, typically using copy-on-write for space efficiency.

Tag: Normal

---

### Question 747
Domain: Operating Systems
Topic: File System Management
Subtopic: Copy-on-Write File Systems
Difficulty: Hard

Question: What characterizes COW file systems?
A) In-place updates
B) Never overwrite data, write to new location
C) Random writes
D) No writes

✔ Correct Answer: B

Reason: COW file systems (ZFS, Btrfs) never overwrite data in place, writing modifications to new locations for consistency.

Tag: Normal

---

### Question 748
Domain: Operating Systems
Topic: File System Management
Subtopic: ZFS Features
Difficulty: Hard

Question: What features does ZFS provide?
A) Basic features
B) Pooled storage, snapshots, checksums, compression, RAID-Z
C) No features
D) Minimal features

✔ Correct Answer: B

Reason: ZFS provides integrated volume management, snapshots, end-to-end checksums, compression, and RAID-Z.

Tag: Normal

---

### Question 749
Domain: Operating Systems
Topic: File System Management
Subtopic: Btrfs Features
Difficulty: Hard

Question: What features does Btrfs provide?
A) Simple features
B) COW, snapshots, subvolumes, checksums, compression
C) No features
D) Minimal features

✔ Correct Answer: B

Reason: Btrfs provides copy-on-write, snapshots, subvolumes, checksums, compression, and online resizing.

Tag: Normal

---

### Question 750
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Checksums
Difficulty: Hard

Question: Why do modern file systems use checksums?
A) No reason
B) Detect silent data corruption
C) Increase speed
D) Reduce size

✔ Correct Answer: B

Reason: Checksums detect silent data corruption from disk errors, bit rot, or hardware failures, ensuring data integrity.

Tag: Normal

---

### Question 751
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Compression
Difficulty: Medium

Question: What is transparent file system compression?
A) Manual compression
B) Automatic compression/decompression by file system
C) No compression
D) Application compression

✔ Correct Answer: B

Reason: Transparent compression automatically compresses/decompresses data, saving space without application awareness.

Tag: Normal

---

### Question 752
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Encryption
Difficulty: Medium

Question: What is file system-level encryption?
A) No encryption
B) Transparent encryption of all file system data
C) File-by-file encryption
D) Application encryption

✔ Correct Answer: B

Reason: File system-level encryption transparently encrypts all data, protecting against physical theft and unauthorized access.

Tag: Normal

---

### Question 753
Domain: Operating Systems
Topic: File System Management
Subtopic: Deduplication
Difficulty: Hard

Question: What is file system deduplication?
A) Duplication
B) Eliminating duplicate data blocks to save space
C) No elimination
D) Copying data

✔ Correct Answer: B

Reason: Deduplication identifies and eliminates duplicate blocks, storing single copy with multiple references, saving space.

Tag: Normal

---

### Question 754
Domain: Operating Systems
Topic: File System Management
Subtopic: Reflink
Difficulty: Hard

Question: What is reflink in file systems?
A) Hard link
B) Copy-on-write file copy sharing blocks
C) Symbolic link
D) No link

✔ Correct Answer: B

Reason: Reflink creates file copy sharing blocks with original using COW, instant copy with space savings until modification.

Tag: Normal

---

### Question 755
Domain: Operating Systems
Topic: File System Management
Subtopic: File System Quotas
Difficulty: Medium

Question: What are file system quotas?
A) No limits
B) Limits on disk space and file count per user/group
C) Unlimited space
D) No tracking

✔ Correct Answer: B

Reason: Quotas limit disk space and inode usage per user or group, preventing resource monopolization.

Tag: Normal

---

### Question 756
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: I/O Schedulers
Difficulty: Hard

Question: What is the deadline I/O scheduler?
A) No deadlines
B) Guarantees request serviced within deadline
C) FIFO only
D) Random scheduling

✔ Correct Answer: B

Reason: Deadline scheduler maintains read/write deadlines, ensuring requests serviced within time limit to prevent starvation.

Tag: Normal

---

### Question 757
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: I/O Schedulers
Difficulty: Hard

Question: What is the CFQ I/O scheduler?
A) Random scheduling
B) Completely Fair Queuing - fair time slices per process
C) FIFO scheduling
D) No fairness

✔ Correct Answer: B

Reason: CFQ (Completely Fair Queuing) allocates fair time slices to each process's I/O queue, ensuring fairness.

Tag: Normal

---

### Question 758
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: I/O Schedulers
Difficulty: Hard

Question: What is the noop I/O scheduler?
A) Complex scheduler
B) Simple FIFO with merging only
C) Advanced scheduler
D) No scheduling

✔ Correct Answer: B

Reason: Noop scheduler performs minimal work (FIFO with request merging), suitable for SSDs and virtualized environments.

Tag: Normal

---

### Question 759
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: I/O Schedulers
Difficulty: Hard

Question: Why might SSDs use simpler I/O schedulers?
A) Need complex scheduling
B) No seek time, parallel access makes reordering less beneficial
C) Slower performance
D) No reason

✔ Correct Answer: B

Reason: SSDs lack mechanical seek time and support parallel operations, making complex reordering less beneficial than HDDs.

Tag: Normal

---

### Question 760
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Multiqueue Block Layer
Difficulty: Hard

Question: What is the multiqueue block layer?
A) Single queue
B) Multiple per-CPU queues for parallel I/O
C) No queues
D) Slow queuing

✔ Correct Answer: B

Reason: Multiqueue block layer uses per-CPU queues, reducing lock contention and improving scalability on multicore systems.

Tag: Normal

---

### Question 761
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: I/O Priorities
Difficulty: Medium

Question: What are I/O priorities?
A) No priorities
B) Assigning importance levels to I/O requests
C) All equal
D) Random priorities

✔ Correct Answer: B

Reason: I/O priorities allow assigning importance to processes' I/O requests, ensuring critical I/O gets preferential treatment.

Tag: Normal

---

### Question 762
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Encryption
Difficulty: Medium

Question: What is full disk encryption?
A) Partial encryption
B) Encrypting entire disk including OS
C) File-level encryption
D) No encryption

✔ Correct Answer: B

Reason: Full disk encryption encrypts entire disk including OS and swap, protecting against physical theft.

Tag: Normal

---

### Question 763
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Self-Encrypting Drives
Difficulty: Hard

Question: What are self-encrypting drives (SEDs)?
A) Software encryption
B) Hardware-based encryption in drive controller
C) No encryption
D) OS encryption

✔ Correct Answer: B

Reason: SEDs perform encryption/decryption in drive controller hardware, transparent to OS with better performance.

Tag: Normal

---

### Question 764
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Storage Tiering
Difficulty: Hard

Question: What is storage tiering?
A) Single tier
B) Automatically moving data between storage types by access frequency
C) No movement
D) Manual movement

✔ Correct Answer: B

Reason: Storage tiering automatically moves frequently accessed data to faster storage (SSD) and cold data to slower storage (HDD).

Tag: Normal

---

### Question 765
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Thin Provisioning
Difficulty: Hard

Question: What is thin provisioning?
A) Full allocation
B) Allocating storage on demand rather than upfront
C) No allocation
D) Fixed allocation

✔ Correct Answer: B

Reason: Thin provisioning allocates storage as needed rather than reserving full amount upfront, improving utilization.

Tag: Normal

---

### Question 766
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Virtualization
Difficulty: Hard

Question: What is I/O virtualization?
A) No virtualization
B) Sharing physical I/O devices among virtual machines
C) Single VM only
D) No sharing

✔ Correct Answer: B

Reason: I/O virtualization allows multiple VMs to share physical I/O devices efficiently through hypervisor mediation.

Tag: Normal

---

### Question 767
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: SR-IOV
Difficulty: Hard

Question: What is SR-IOV?
A) Software virtualization
B) Hardware I/O virtualization with virtual functions
C) No virtualization
D) CPU virtualization

✔ Correct Answer: B

Reason: SR-IOV (Single Root I/O Virtualization) allows PCIe device to present multiple virtual functions for direct VM access.

Tag: Normal

---

### Question 768
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Paravirtualized I/O
Difficulty: Hard

Question: What is paravirtualized I/O?
A) Full virtualization
B) Guest uses special drivers aware of virtualization
C) No virtualization
D) Hardware virtualization

✔ Correct Answer: B

Reason: Paravirtualized I/O uses guest drivers aware of virtualization (virtio), improving performance over emulation.

Tag: Normal

---

### Question 769
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Passthrough
Difficulty: Hard

Question: What is I/O passthrough?
A) Emulated I/O
B) Direct device access by VM bypassing hypervisor
C) Shared access
D) No access

✔ Correct Answer: B

Reason: I/O passthrough gives VM direct access to physical device, best performance but device dedicated to single VM.

Tag: Normal

---

### Question 770
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Interrupt Remapping
Difficulty: Hard

Question: What is interrupt remapping?
A) No remapping
B) Translating device interrupts for VMs
C) Blocking interrupts
D) Random interrupts

✔ Correct Answer: B

Reason: Interrupt remapping translates device interrupts to appropriate VM, enabling safe interrupt delivery in virtualized environments.

Tag: Normal

---

### Question 771
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Kernel Security
Difficulty: Hard

Question: What is kernel address space layout randomization (KASLR)?
A) Fixed addresses
B) Randomizing kernel memory addresses
C) No randomization
D) User space only

✔ Correct Answer: B

Reason: KASLR randomizes kernel memory layout, making kernel exploits harder by preventing attackers from knowing addresses.

Tag: Normal

---

### Question 772
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Kernel Security
Difficulty: Hard

Question: What is kernel page table isolation (KPTI)?
A) No isolation
B) Separating kernel and user page tables
C) Shared page tables
D) No page tables

✔ Correct Answer: B

Reason: KPTI separates kernel and user page tables, mitigating Meltdown vulnerability by preventing user access to kernel memory.

Tag: Normal

---

### Question 773
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Features
Difficulty: Hard

Question: What is SELinux?
A) Simple security
B) Mandatory access control security module
C) No security
D) Firewall

✔ Correct Answer: B

Reason: SELinux (Security-Enhanced Linux) implements mandatory access control, enforcing security policies beyond traditional permissions.

Tag: Normal

---

### Question 774
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Features
Difficulty: Hard

Question: What is AppArmor?
A) Application installer
B) Mandatory access control using profiles
C) No security
D) Antivirus

✔ Correct Answer: B

Reason: AppArmor provides MAC using per-program profiles defining allowed file access, capabilities, and network access.

Tag: Normal

---

### Question 775
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Seccomp
Difficulty: Hard

Question: What is seccomp?
A) No filtering
B) System call filtering for sandboxing
C) Compression
D) Encryption

✔ Correct Answer: B

Reason: Seccomp (secure computing mode) filters system calls, restricting process to subset of calls for sandboxing.

Tag: Normal

---

### Question 776
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Capabilities
Difficulty: Hard

Question: What is CAP_NET_ADMIN capability?
A) File access
B) Network administration operations
C) Process management
D) Memory access

✔ Correct Answer: B

Reason: CAP_NET_ADMIN allows network configuration operations (interface config, routing, firewall) without full root.

Tag: Normal

---

### Question 777
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Capabilities
Difficulty: Hard

Question: What is CAP_SYS_ADMIN capability?
A) Limited privilege
B) Wide range of administrative operations
C) No privileges
D) User operations

✔ Correct Answer: B

Reason: CAP_SYS_ADMIN grants wide range of administrative operations, often called "new root" due to broad scope.

Tag: Normal

---

### Question 778
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Audit System
Difficulty: Medium

Question: What is the Linux audit system?
A) No auditing
B) Recording security-relevant events for compliance
C) Performance monitoring
D) Debugging tool

✔ Correct Answer: B

Reason: Linux audit system records security-relevant events (file access, system calls, authentication) for compliance and forensics.

Tag: Normal

---

### Question 779
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Integrity Measurement
Difficulty: Hard

Question: What is IMA (Integrity Measurement Architecture)?
A) No measurement
B) Measuring and verifying file integrity
C) Performance measurement
D) Size measurement

✔ Correct Answer: B

Reason: IMA measures file integrity before execution, detecting unauthorized modifications and supporting trusted boot.

Tag: Normal

---

### Question 780
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Trusted Boot
Difficulty: Hard

Question: What is trusted boot?
A) Fast boot
B) Measuring boot components, recording in TPM
C) No measurement
D) Slow boot

✔ Correct Answer: B

Reason: Trusted boot measures each boot component, recording measurements in TPM for attestation, detecting tampering.

Tag: Normal

---

### Question 781
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Attestation
Difficulty: Hard

Question: What is remote attestation?
A) Local verification
B) Proving system state to remote party
C) No verification
D) Manual check

✔ Correct Answer: B

Reason: Remote attestation uses TPM measurements to prove system configuration to remote party, establishing trust.

Tag: Normal

---

### Question 782
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Kernel Hardening
Difficulty: Hard

Question: What is kernel hardening?
A) Making kernel softer
B) Applying security measures to reduce attack surface
C) No security
D) Removing features

✔ Correct Answer: B

Reason: Kernel hardening applies security measures (ASLR, stack protection, restricting features) to reduce vulnerability to attacks.

Tag: Normal

---

### Question 783
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Exploit Mitigation
Difficulty: Hard

Question: What is stack canary?
A) Bird
B) Value detecting stack buffer overflow
C) No protection
D) Heap protection

✔ Correct Answer: B

Reason: Stack canary is known value placed before return address; modification indicates buffer overflow attempt.

Tag: Normal

---

### Question 784
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Exploit Mitigation
Difficulty: Hard

Question: What is NX bit (No-Execute)?
A) Execute anywhere
B) Marking memory pages as non-executable
C) No protection
D) Execute only

✔ Correct Answer: B

Reason: NX bit marks memory pages as non-executable, preventing code execution from data pages (stack, heap).

Tag: Normal

---

### Question 785
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Vulnerability Classes
Difficulty: Medium

Question: What is a use-after-free vulnerability?
A) Memory leak
B) Accessing freed memory
C) Buffer overflow
D) Integer overflow

✔ Correct Answer: B

Reason: Use-after-free occurs when program accesses memory after freeing it, potentially executing attacker-controlled code.

Tag: Normal

---

### Question 786
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Vulnerability Classes
Difficulty: Medium

Question: What is a race condition vulnerability?
A) Fast execution
B) Exploiting timing between check and use
C) Slow execution
D) No timing issue

✔ Correct Answer: B

Reason: Race condition vulnerability exploits time-of-check to time-of-use (TOCTOU) gap, changing state between check and use.

Tag: Normal

---

### Question 787
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Privilege Escalation
Difficulty: Medium

Question: What is privilege escalation?
A) Reducing privileges
B) Gaining higher privileges than authorized
C) Normal operation
D) No change

✔ Correct Answer: B

Reason: Privilege escalation exploits vulnerabilities to gain elevated privileges, often from user to root/administrator.

Tag: Normal

---

### Question 788
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Updates
Difficulty: Easy

Question: Why are security updates important?
A) Not important
B) Patch vulnerabilities before exploitation
C) Add features only
D) Slow down system

✔ Correct Answer: B

Reason: Security updates patch discovered vulnerabilities, preventing exploitation by attackers who learn of flaws.

Tag: Normal

---

### Question 789
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Performance Metrics
Difficulty: Medium

Question: What is system load average?
A) CPU speed
B) Average number of processes in runnable/uninterruptible state
C) Memory usage
D) Disk usage

✔ Correct Answer: B

Reason: Load average measures average number of processes in runnable or uninterruptible wait state over time periods.

Tag: Normal

---

### Question 790
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Monitoring
Difficulty: Easy

Question: What does the top command show?
A) File listing
B) Real-time process and system resource usage
C) Network status
D) Disk space

✔ Correct Answer: B

Reason: top displays real-time view of running processes, CPU usage, memory usage, and system statistics.

Tag: Normal

---

### Question 791
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Monitoring
Difficulty: Medium

Question: What does vmstat report?
A) Only CPU
B) Virtual memory, processes, CPU, I/O statistics
C) Only memory
D) Only disk

✔ Correct Answer: B

Reason: vmstat reports virtual memory statistics including processes, memory, paging, I/O, and CPU activity.

Tag: Normal

---

### Question 792
Domain: Operating Systems
Topic: Introduction to Operating Systems
Subtopic: System Monitoring
Difficulty: Medium

Question: What does iostat report?
A) Only CPU
B) CPU and I/O statistics for devices
C) Only memory
D) Only network

✔ Correct Answer: B

Reason: iostat reports CPU utilization and I/O statistics for storage devices, identifying I/O bottlenecks.

Tag: Normal

---

### Question 793
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Initialization
Difficulty: Medium

Question: What is the init process?
A) Last process
B) First user-space process, parent of all processes
C) Random process
D) Kernel process

✔ Correct Answer: B

Reason: init (PID 1) is first user-space process started by kernel, ancestor of all other processes.

Tag: Normal

---

### Question 794
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Runlevels
Difficulty: Medium

Question: What are runlevels in SysV init?
A) CPU levels
B) System states defining which services run
C) Memory levels
D) No levels

✔ Correct Answer: B

Reason: Runlevels define system states (0=halt, 1=single-user, 3=multi-user, 5=graphical, 6=reboot) and active services.

Tag: Normal

---

### Question 795
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Systemd Units
Difficulty: Hard

Question: What are systemd units?
A) No units
B) Configuration files defining services, mounts, devices, etc.
C) Only services
D) Hardware units

✔ Correct Answer: B

Reason: Systemd units are configuration files defining system resources: services, sockets, devices, mounts, timers, etc.

Tag: Normal

---

### Question 796
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Service Management
Difficulty: Medium

Question: How does systemd improve on SysV init?
A) No improvement
B) Parallel startup, dependency management, socket activation
C) Slower startup
D) Less features

✔ Correct Answer: B

Reason: Systemd provides parallel service startup, explicit dependencies, socket activation, and better resource management.

Tag: Normal

---

### Question 797
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Tracing
Difficulty: Hard

Question: What is strace?
A) Stack trace
B) Tool tracing system calls and signals
C) String trace
D) No tracing

✔ Correct Answer: B

Reason: strace traces system calls made by process and signals received, useful for debugging and understanding behavior.

Tag: Normal

---

### Question 798
Domain: Operating Systems
Topic: Process Management
Subtopic: Process Debugging
Difficulty: Medium

Question: What is ptrace system call?
A) Print trace
B) Process tracing and debugging interface
C) Path trace
D) No function

✔ Correct Answer: B

Reason: ptrace allows process to observe and control execution of another process, foundation for debuggers.

Tag: Normal

---

### Question 799
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Profiling
Difficulty: Hard

Question: What is valgrind?
A) Validator
B) Memory debugging and profiling tool
C) Compiler
D) No tool

✔ Correct Answer: B

Reason: Valgrind detects memory leaks, invalid memory access, and provides profiling tools for performance analysis.

Tag: Normal

---

### Question 800
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory Analysis
Difficulty: Hard

Question: What does /proc/meminfo provide?
A) Process info
B) Detailed system memory statistics
C) CPU info
D) Disk info

✔ Correct Answer: B

Reason: /proc/meminfo provides detailed memory statistics including total, free, available, buffers, cached, and swap memory.

Tag: Normal

---

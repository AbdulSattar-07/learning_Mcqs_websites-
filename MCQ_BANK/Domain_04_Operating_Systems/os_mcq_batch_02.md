# Operating Systems - MCQ Batch 02
## Questions 101-200

---

### Question 101
Domain: Operating Systems
Topic: Memory Management
Subtopic: Belady's Anomaly
Difficulty: Hard

Question: What is Belady's Anomaly?
A) More frames always reduce page faults
B) Increasing frames can increase page faults with FIFO
C) LRU always performs better
D) No anomaly exists

✔ Correct Answer: B

Reason: Belady's Anomaly occurs with FIFO page replacement where increasing the number of frames can paradoxically increase page faults.

Tag: Normal

---

### Question 102
Domain: Operating Systems
Topic: Memory Management
Subtopic: Frame Allocation
Difficulty: Medium

Question: What is equal allocation of frames?
A) All processes get different frames
B) All processes get equal number of frames
C) No frames allocated
D) Random allocation

✔ Correct Answer: B

Reason: Equal allocation divides available frames equally among all processes, simple but doesn't consider process size or priority.

Tag: Normal

---

### Question 103
Domain: Operating Systems
Topic: Memory Management
Subtopic: Frame Allocation
Difficulty: Hard

Question: What is proportional allocation?
A) Equal frames to all
B) Frames allocated based on process size
C) Random allocation
D) No allocation

✔ Correct Answer: B

Reason: Proportional allocation assigns frames to processes based on their size, giving larger processes more frames.

Tag: Normal

---

### Question 104
Domain: Operating Systems
Topic: Memory Management
Subtopic: Global vs Local Replacement
Difficulty: Hard

Question: What is global page replacement?
A) Process selects from its own frames
B) Process can select from all frames
C) No replacement
D) Only system frames

✔ Correct Answer: B

Reason: Global replacement allows a process to select a replacement frame from the set of all frames, potentially taking frames from other processes.

Tag: Normal

---

### Question 105
Domain: Operating Systems
Topic: Memory Management
Subtopic: Memory-Mapped Files
Difficulty: Hard

Question: What is memory-mapped I/O?
A) Mapping memory to disk
B) Treating file I/O as memory access
C) Mapping I/O devices to memory addresses
D) No mapping

✔ Correct Answer: C

Reason: Memory-mapped I/O maps I/O device registers to memory addresses, allowing I/O operations using standard memory instructions.

Tag: Normal

---

### Question 106
Domain: Operating Systems
Topic: File System Management
Subtopic: File Concept
Difficulty: Easy

Question: What is a file?
A) A process
B) A named collection of related information
C) A memory location
D) A CPU register

✔ Correct Answer: B

Reason: A file is a named collection of related information stored on secondary storage, representing programs or data.

Tag: Past Paper

---

### Question 107
Domain: Operating Systems
Topic: File System Management
Subtopic: File Attributes
Difficulty: Easy

Question: Which is NOT typically a file attribute?
A) Name
B) Size
C) CPU speed
D) Creation time

✔ Correct Answer: C

Reason: File attributes include name, type, size, location, protection, timestamps. CPU speed is a system attribute, not a file attribute.

Tag: Normal

---

### Question 108
Domain: Operating Systems
Topic: File System Management
Subtopic: File Operations
Difficulty: Easy

Question: Which is a basic file operation?
A) Compile
B) Create
C) Execute
D) Debug

✔ Correct Answer: B

Reason: Basic file operations include create, delete, open, close, read, write, append, seek, and get/set attributes.

Tag: Normal

---

### Question 109
Domain: Operating Systems
Topic: File System Management
Subtopic: File Types
Difficulty: Easy

Question: What does a file extension typically indicate?
A) File size
B) File type or format
C) File owner
D) File location

✔ Correct Answer: B

Reason: File extensions (like .txt, .exe, .jpg) indicate the file type or format, helping the OS and applications handle the file appropriately.

Tag: Normal

---

### Question 110
Domain: Operating Systems
Topic: File System Management
Subtopic: File Access Methods
Difficulty: Medium

Question: What is sequential file access?
A) Random access to any record
B) Records accessed in order from beginning
C) No access
D) Parallel access

✔ Correct Answer: B

Reason: Sequential access processes records in order from beginning to end, suitable for tape drives and batch processing.

Tag: Past Paper

---

### Question 111
Domain: Operating Systems
Topic: File System Management
Subtopic: File Access Methods
Difficulty: Medium

Question: What is direct (random) file access?
A) Sequential access only
B) Access any record directly without reading previous records
C) No access allowed
D) Ordered access only

✔ Correct Answer: B

Reason: Direct access allows reading/writing records in any order without accessing previous records, using record numbers or keys.

Tag: Normal

---

### Question 112
Domain: Operating Systems
Topic: File System Management
Subtopic: Directory Structure
Difficulty: Easy

Question: What is a directory?
A) A file containing data
B) A container organizing files and subdirectories
C) A process
D) A memory location

✔ Correct Answer: B

Reason: A directory is a special file containing information about files and subdirectories, organizing the file system hierarchically.

Tag: Normal

---

### Question 113
Domain: Operating Systems
Topic: File System Management
Subtopic: Single-Level Directory
Difficulty: Easy

Question: What is the main limitation of single-level directory?
A) Too complex
B) Name collision when multiple users
C) Too much space
D) Too fast

✔ Correct Answer: B

Reason: Single-level directory has all files in one directory, causing naming conflicts when multiple users want same filename.

Tag: Normal

---

### Question 114
Domain: Operating Systems
Topic: File System Management
Subtopic: Two-Level Directory
Difficulty: Medium

Question: What does two-level directory structure provide?
A) One directory for all
B) Separate directory for each user
C) No directories
D) Random structure

✔ Correct Answer: B

Reason: Two-level directory gives each user a separate directory, solving name collision but limiting file organization within user space.

Tag: Normal

---

### Question 115
Domain: Operating Systems
Topic: File System Management
Subtopic: Tree-Structured Directory
Difficulty: Medium

Question: What advantage does tree-structured directory provide?
A) Flat structure
B) Hierarchical organization with subdirectories
C) No organization
D) Single level only

✔ Correct Answer: B

Reason: Tree-structured directories allow hierarchical organization with subdirectories, providing flexible file organization and grouping.

Tag: Past Paper

---

### Question 116
Domain: Operating Systems
Topic: File System Management
Subtopic: Path Names
Difficulty: Easy

Question: What is an absolute path?
A) Relative to current directory
B) Complete path from root directory
C) No path
D) Random path

✔ Correct Answer: B

Reason: Absolute path specifies location from root directory (e.g., /home/user/file.txt), providing complete unambiguous file location.

Tag: Normal

---

### Question 117
Domain: Operating Systems
Topic: File System Management
Subtopic: Path Names
Difficulty: Easy

Question: What is a relative path?
A) Path from root
B) Path from current working directory
C) No path
D) Absolute path

✔ Correct Answer: B

Reason: Relative path specifies location relative to current working directory (e.g., ../docs/file.txt), shorter but context-dependent.

Tag: Normal

---

### Question 118
Domain: Operating Systems
Topic: File System Management
Subtopic: File Sharing
Difficulty: Medium

Question: What is a hard link?
A) Network connection
B) Directory entry pointing to same inode
C) Symbolic reference
D) No link

✔ Correct Answer: B

Reason: Hard link is a directory entry that directly references the same inode as another file, creating multiple names for same file.

Tag: Normal

---

### Question 119
Domain: Operating Systems
Topic: File System Management
Subtopic: File Sharing
Difficulty: Medium

Question: What is a symbolic (soft) link?
A) Direct inode reference
B) Special file containing path to another file
C) No link
D) Hardware link

✔ Correct Answer: B

Reason: Symbolic link is a special file containing the pathname of another file, allowing links across file systems and to directories.

Tag: Normal

---

### Question 120
Domain: Operating Systems
Topic: File System Management
Subtopic: File Protection
Difficulty: Easy

Question: What are the three basic file access permissions in UNIX?
A) Create, Delete, Modify
B) Read, Write, Execute
C) Open, Close, Save
D) Copy, Move, Rename

✔ Correct Answer: B

Reason: UNIX file permissions are Read (r), Write (w), and Execute (x), applied to owner, group, and others.

Tag: Past Paper

---


### Question 121
Domain: Operating Systems
Topic: File System Management
Subtopic: Access Control List
Difficulty: Hard

Question: What is an Access Control List (ACL)?
A) List of files
B) List specifying permissions for each user/group
C) List of processes
D) List of directories

✔ Correct Answer: B

Reason: ACL provides fine-grained access control by specifying permissions for individual users and groups beyond basic owner/group/others model.

Tag: Normal

---

### Question 122
Domain: Operating Systems
Topic: File System Management
Subtopic: File Allocation Methods
Difficulty: Medium

Question: What is contiguous file allocation?
A) Files scattered across disk
B) Each file occupies consecutive disk blocks
C) Random allocation
D) No allocation

✔ Correct Answer: B

Reason: Contiguous allocation stores each file in consecutive disk blocks, providing fast sequential access but causing external fragmentation.

Tag: Past Paper

---

### Question 123
Domain: Operating Systems
Topic: File System Management
Subtopic: Contiguous Allocation
Difficulty: Medium

Question: What is the main disadvantage of contiguous allocation?
A) Slow access
B) External fragmentation and difficulty in file growth
C) Too much space
D) No disadvantages

✔ Correct Answer: B

Reason: Contiguous allocation suffers from external fragmentation and makes file growth difficult as contiguous space may not be available.

Tag: Normal

---

### Question 124
Domain: Operating Systems
Topic: File System Management
Subtopic: Linked Allocation
Difficulty: Medium

Question: How does linked allocation work?
A) Contiguous blocks
B) Each block contains pointer to next block
C) Random blocks
D) No blocks

✔ Correct Answer: B

Reason: Linked allocation stores files as linked list of disk blocks, each containing pointer to next block, eliminating external fragmentation.

Tag: Normal

---

### Question 125
Domain: Operating Systems
Topic: File System Management
Subtopic: Linked Allocation
Difficulty: Hard

Question: What is a disadvantage of linked allocation?
A) External fragmentation
B) No random access, pointer overhead
C) Too fast
D) No disadvantages

✔ Correct Answer: B

Reason: Linked allocation doesn't support efficient random access and wastes space for pointers in each block, though it eliminates external fragmentation.

Tag: Normal

---

### Question 126
Domain: Operating Systems
Topic: File System Management
Subtopic: Indexed Allocation
Difficulty: Hard

Question: What is indexed allocation?
A) No index used
B) Index block contains pointers to all file blocks
C) Sequential allocation
D) Random allocation

✔ Correct Answer: B

Reason: Indexed allocation uses an index block containing pointers to all blocks of a file, supporting random access without external fragmentation.

Tag: Past Paper

---

### Question 127
Domain: Operating Systems
Topic: File System Management
Subtopic: FAT
Difficulty: Medium

Question: What does FAT stand for?
A) Fast Access Table
B) File Allocation Table
C) File Access Type
D) Fast Allocation Technique

✔ Correct Answer: B

Reason: FAT (File Allocation Table) is a file system using a table to track cluster allocation, simple but limited in features and scalability.

Tag: Normal

---

### Question 128
Domain: Operating Systems
Topic: File System Management
Subtopic: Inode
Difficulty: Hard

Question: What is an inode in UNIX file systems?
A) A file name
B) Data structure containing file metadata and block pointers
C) A directory
D) A process

✔ Correct Answer: B

Reason: Inode (index node) stores file metadata (permissions, timestamps, size) and pointers to data blocks, separating file names from file data.

Tag: Normal

---

### Question 129
Domain: Operating Systems
Topic: File System Management
Subtopic: Free Space Management
Difficulty: Medium

Question: What is a bitmap for free space management?
A) Image file
B) Bit array where each bit represents block status
C) Text file
D) Process list

✔ Correct Answer: B

Reason: Bitmap uses one bit per block (0=free, 1=allocated), providing efficient space management and easy identification of free blocks.

Tag: Normal

---

### Question 130
Domain: Operating Systems
Topic: File System Management
Subtopic: Free Space Management
Difficulty: Medium

Question: What is a free list?
A) List of files
B) Linked list of free disk blocks
C) List of processes
D) List of users

✔ Correct Answer: B

Reason: Free list maintains a linked list of all free disk blocks, simple but requires traversal to find contiguous free space.

Tag: Normal

---

### Question 131
Domain: Operating Systems
Topic: File System Management
Subtopic: Journaling
Difficulty: Hard

Question: What is the purpose of journaling in file systems?
A) Keep diary
B) Log changes before committing for crash recovery
C) Increase speed
D) Reduce space

✔ Correct Answer: B

Reason: Journaling logs file system changes before committing them, enabling quick recovery and maintaining consistency after crashes.

Tag: Normal

---

### Question 132
Domain: Operating Systems
Topic: File System Management
Subtopic: Virtual File System
Difficulty: Hard

Question: What does VFS (Virtual File System) provide?
A) Virtual memory
B) Abstract interface for different file systems
C) Virtual processes
D) Virtual network

✔ Correct Answer: B

Reason: VFS provides an abstract interface allowing the OS to support multiple file system types transparently to applications.

Tag: Normal

---

### Question 133
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

Reason: A sector is the smallest addressable unit on a disk, typically 512 bytes or 4KB, forming the basic unit of disk I/O.

Tag: Normal

---

### Question 134
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

Reason: A track is a concentric circle on a disk platter where data is stored, with multiple tracks on each platter surface.

Tag: Normal

---

### Question 135
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Structure
Difficulty: Medium

Question: What is a cylinder in disk geometry?
A) Disk shape
B) Set of tracks at same position on all platters
C) Disk motor
D) Disk cache

✔ Correct Answer: B

Reason: A cylinder consists of all tracks at the same radial position across all disk platters, accessible without moving the read/write head.

Tag: Normal

---

### Question 136
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Scheduling
Difficulty: Easy

Question: What is disk scheduling?
A) Scheduling processes
B) Determining order of disk I/O requests
C) Scheduling memory
D) Scheduling network

✔ Correct Answer: B

Reason: Disk scheduling algorithms determine the order in which pending disk I/O requests are serviced to minimize seek time and improve performance.

Tag: Past Paper

---

### Question 137
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: FCFS Disk Scheduling
Difficulty: Easy

Question: What does FCFS disk scheduling do?
A) Serves requests in arrival order
B) Serves shortest seek first
C) Serves randomly
D) No scheduling

✔ Correct Answer: A

Reason: FCFS (First-Come-First-Served) services disk requests in the order they arrive, simple but may not minimize seek time.

Tag: Normal

---

### Question 138
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: SSTF Disk Scheduling
Difficulty: Medium

Question: What does SSTF stand for?
A) Shortest Seek Time First
B) Shortest Service Time First
C) Slowest Seek Time First
D) Standard Seek Time First

✔ Correct Answer: A

Reason: SSTF selects the request with minimum seek time from current head position, reducing average seek time but may cause starvation.

Tag: Past Paper

---

### Question 139
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

Reason: SCAN (elevator algorithm) moves the disk arm in one direction servicing requests until reaching the end, then reverses direction.

Tag: Normal

---

### Question 140
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: C-SCAN Disk Scheduling
Difficulty: Hard

Question: How does C-SCAN differ from SCAN?
A) Same algorithm
B) Returns to beginning without servicing on return trip
C) Slower
D) No difference

✔ Correct Answer: B

Reason: C-SCAN (Circular SCAN) services requests in one direction, then returns to the beginning without servicing, providing more uniform wait time.

Tag: Normal

---

### Question 141
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: LOOK Disk Scheduling
Difficulty: Hard

Question: How does LOOK differ from SCAN?
A) Same algorithm
B) Reverses direction at last request, not disk end
C) Faster
D) No difference

✔ Correct Answer: B

Reason: LOOK is like SCAN but reverses direction at the last request in that direction rather than going to the physical disk end.

Tag: Normal

---

### Question 142
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Formatting
Difficulty: Medium

Question: What is low-level formatting?
A) File system creation
B) Dividing disk into sectors with headers/trailers
C) Deleting files
D) Partitioning

✔ Correct Answer: B

Reason: Low-level (physical) formatting divides disk into sectors, writing headers, data areas, and trailers, typically done by manufacturer.

Tag: Normal

---

### Question 143
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Disk Formatting
Difficulty: Medium

Question: What is high-level formatting?
A) Physical formatting
B) Creating file system structures
C) Hardware formatting
D) No formatting

✔ Correct Answer: B

Reason: High-level (logical) formatting creates file system structures like boot blocks, free space management, and root directory.

Tag: Normal

---

### Question 144
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Boot Block
Difficulty: Medium

Question: What is stored in the boot block?
A) User files
B) Code to load and start operating system
C) Temporary data
D) Nothing

✔ Correct Answer: B

Reason: Boot block contains bootstrap loader code that initializes the system and loads the operating system kernel into memory.

Tag: Normal

---

### Question 145
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: Bad Blocks
Difficulty: Medium

Question: How are bad blocks handled?
A) Ignored
B) Marked and replaced with spare sectors
C) Deleted
D) Reformatted repeatedly

✔ Correct Answer: B

Reason: Bad blocks are detected, marked in a bad-block list, and logically replaced with spare sectors to maintain disk reliability.

Tag: Normal

---

### Question 146
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

Reason: RAID (Redundant Array of Independent Disks) combines multiple disks for improved performance, reliability, or both.

Tag: Past Paper

---

### Question 147
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

Reason: RAID 0 stripes data across multiple disks for improved performance but provides no redundancy; any disk failure loses all data.

Tag: Normal

---

### Question 148
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

Reason: RAID 1 mirrors data across two disks, providing full redundancy and fault tolerance but using 50% of capacity for redundancy.

Tag: Normal

---

### Question 149
Domain: Operating Systems
Topic: Secondary Storage Management
Subtopic: RAID Levels
Difficulty: Hard

Question: What does RAID 5 use for redundancy?
A) Mirroring
B) Distributed parity
C) No redundancy
D) Triple redundancy

✔ Correct Answer: B

Reason: RAID 5 uses distributed parity across all disks, allowing recovery from single disk failure while using less space than mirroring.

Tag: Normal

---

### Question 150
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

Reason: Device controller is hardware that manages I/O device operations, containing registers for communication with CPU and device-specific logic.

Tag: Normal

---


### Question 151
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

Reason: Device driver is software that provides a standard interface between the operating system and hardware devices, translating generic I/O commands to device-specific operations.

Tag: Normal

---

### Question 152
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

Reason: Programmed I/O has the CPU continuously check device status (polling) and transfer data, simple but wastes CPU cycles.

Tag: Normal

---

### Question 153
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Methods
Difficulty: Medium

Question: What is interrupt-driven I/O?
A) CPU polls continuously
B) Device signals CPU when ready via interrupt
C) No interrupts used
D) Manual I/O

✔ Correct Answer: B

Reason: Interrupt-driven I/O allows CPU to do other work while waiting; device sends interrupt when ready, improving CPU utilization.

Tag: Past Paper

---

### Question 154
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

Reason: DMA (Direct Memory Access) allows devices to transfer data directly to/from memory without CPU intervention, freeing CPU for other tasks.

Tag: Past Paper

---

### Question 155
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: DMA
Difficulty: Hard

Question: What is the role of DMA controller?
A) Control CPU
B) Manage data transfer between device and memory
C) Control processes
D) Manage files

✔ Correct Answer: B

Reason: DMA controller manages data transfer between I/O devices and memory independently, only interrupting CPU when transfer completes.

Tag: Normal

---

### Question 156
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

Reason: Buffering uses temporary storage to hold data during transfer between devices with different speeds, smoothing speed mismatches.

Tag: Normal

---

### Question 157
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Spooling
Difficulty: Medium

Question: What is spooling?
A) Printing directly
B) Queuing output for device that serves one request at a time
C) Deleting files
D) No queuing

✔ Correct Answer: B

Reason: Spooling (Simultaneous Peripheral Operations OnLine) queues jobs for devices like printers, allowing multiple processes to generate output concurrently.

Tag: Normal

---

### Question 158
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: I/O Scheduling
Difficulty: Hard

Question: Why is I/O scheduling needed?
A) Not needed
B) To order I/O requests for efficiency and fairness
C) To delete requests
D) To create requests

✔ Correct Answer: B

Reason: I/O scheduling orders pending I/O requests to improve system performance, reduce wait times, and ensure fairness among processes.

Tag: Normal

---

### Question 159
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Blocking I/O
Difficulty: Easy

Question: What happens in blocking I/O?
A) Process continues execution
B) Process suspended until I/O completes
C) I/O never completes
D) No suspension

✔ Correct Answer: B

Reason: Blocking (synchronous) I/O suspends the calling process until the I/O operation completes, simple but may waste CPU time.

Tag: Normal

---

### Question 160
Domain: Operating Systems
Topic: Input/Output Systems
Subtopic: Non-blocking I/O
Difficulty: Medium

Question: What characterizes non-blocking I/O?
A) Process waits for completion
B) Process continues execution, checks status later
C) I/O never happens
D) Immediate completion

✔ Correct Answer: B

Reason: Non-blocking (asynchronous) I/O returns immediately, allowing process to continue while I/O proceeds in background.

Tag: Normal

---

### Question 161
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

### Question 162
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

Reason: Authentication verifies the identity of a user or process, typically using passwords, biometrics, or tokens before granting access.

Tag: Normal

---

### Question 163
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

Reason: Authorization determines what resources and operations an authenticated user is permitted to access, enforcing access control policies.

Tag: Normal

---

### Question 164
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control
Difficulty: Medium

Question: What is the principle of least privilege?
A) Maximum access for all
B) Users get minimum permissions needed for tasks
C) No access control
D) Random permissions

✔ Correct Answer: B

Reason: Least privilege principle grants users only the minimum permissions necessary to perform their tasks, limiting potential damage from errors or attacks.

Tag: Normal

---

### Question 165
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control Models
Difficulty: Hard

Question: What is Discretionary Access Control (DAC)?
A) Mandatory control
B) Owner controls access to their resources
C) No control
D) System controls all

✔ Correct Answer: B

Reason: DAC allows resource owners to control access permissions, flexible but vulnerable to Trojan horses and user errors.

Tag: Normal

---

### Question 166
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control Models
Difficulty: Hard

Question: What is Mandatory Access Control (MAC)?
A) Owner controls access
B) System enforces access based on security labels
C) No control
D) User controls all

✔ Correct Answer: B

Reason: MAC enforces access control based on system-wide security policies and labels, more secure but less flexible than DAC.

Tag: Normal

---

### Question 167
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Access Control Models
Difficulty: Hard

Question: What is Role-Based Access Control (RBAC)?
A) User-based control
B) Access based on user roles in organization
C) No roles
D) Random access

✔ Correct Answer: B

Reason: RBAC assigns permissions to roles rather than individuals, simplifying administration and ensuring consistent access control.

Tag: Normal

---

### Question 168
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Passwords
Difficulty: Easy

Question: What makes a strong password?
A) Short and simple
B) Long with mix of characters, numbers, symbols
C) Common words
D) Username repeated

✔ Correct Answer: B

Reason: Strong passwords are long (12+ characters) with uppercase, lowercase, numbers, and symbols, avoiding dictionary words and personal information.

Tag: Normal

---

### Question 169
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Password Attacks
Difficulty: Medium

Question: What is a brute force password attack?
A) Physical attack
B) Trying all possible password combinations
C) Social engineering
D) Guessing once

✔ Correct Answer: B

Reason: Brute force systematically tries all possible password combinations until finding the correct one, time-consuming but eventually successful.

Tag: Normal

---

### Question 170
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Password Attacks
Difficulty: Medium

Question: What is a dictionary attack?
A) Random guessing
B) Trying common words and phrases from dictionary
C) Physical attack
D) No attack

✔ Correct Answer: B

Reason: Dictionary attacks try common words, phrases, and known passwords from precompiled lists, faster than brute force for weak passwords.

Tag: Normal

---

### Question 171
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Encryption
Difficulty: Medium

Question: What is encryption?
A) Deleting data
B) Converting data to unreadable form using algorithm
C) Compressing data
D) Copying data

✔ Correct Answer: B

Reason: Encryption transforms plaintext into ciphertext using cryptographic algorithms and keys, protecting confidentiality during storage and transmission.

Tag: Normal

---

### Question 172
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Malware
Difficulty: Easy

Question: What is malware?
A) Hardware failure
B) Malicious software designed to harm systems
C) Antivirus software
D) Operating system

✔ Correct Answer: B

Reason: Malware (malicious software) includes viruses, worms, trojans, ransomware, and spyware designed to damage, disrupt, or gain unauthorized access.

Tag: Normal

---

### Question 173
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Virus
Difficulty: Easy

Question: What is a computer virus?
A) Hardware disease
B) Malicious code that replicates by attaching to files
C) Network protocol
D) Antivirus

✔ Correct Answer: B

Reason: A virus is malicious code that replicates by inserting copies into other programs or files, requiring host program execution to spread.

Tag: Past Paper

---

### Question 174
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Worm
Difficulty: Medium

Question: How does a worm differ from a virus?
A) Same thing
B) Worm self-replicates without host program
C) Worm is slower
D) No difference

✔ Correct Answer: B

Reason: Worms are self-replicating malware that spread independently across networks without needing host programs, often exploiting vulnerabilities.

Tag: Normal

---

### Question 175
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Trojan Horse
Difficulty: Medium

Question: What is a Trojan horse?
A) Antivirus software
B) Malware disguised as legitimate software
C) Network device
D) Encryption method

✔ Correct Answer: B

Reason: Trojan horse appears legitimate but contains malicious code, doesn't self-replicate but tricks users into executing it.

Tag: Normal

---

### Question 176
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Ransomware
Difficulty: Medium

Question: What does ransomware do?
A) Protects files
B) Encrypts files and demands payment for decryption
C) Backs up files
D) Deletes viruses

✔ Correct Answer: B

Reason: Ransomware encrypts victim's files and demands payment (ransom) for the decryption key, causing data loss and financial damage.

Tag: Normal

---

### Question 177
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Firewall
Difficulty: Easy

Question: What is a firewall?
A) Physical wall
B) Security system controlling network traffic
C) Antivirus software
D) Backup system

✔ Correct Answer: B

Reason: Firewall monitors and controls incoming/outgoing network traffic based on security rules, protecting against unauthorized access.

Tag: Normal

---

### Question 178
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Intrusion Detection
Difficulty: Hard

Question: What does an Intrusion Detection System (IDS) do?
A) Prevents all attacks
B) Monitors and detects suspicious activities
C) Encrypts data
D) Backs up files

✔ Correct Answer: B

Reason: IDS monitors network/system activities for malicious activities or policy violations, alerting administrators but not blocking traffic.

Tag: Normal

---

### Question 179
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Intrusion Prevention
Difficulty: Hard

Question: How does IPS differ from IDS?
A) Same function
B) IPS actively blocks detected threats
C) IPS is slower
D) No difference

✔ Correct Answer: B

Reason: IPS (Intrusion Prevention System) not only detects but also actively blocks or prevents detected threats, providing active defense.

Tag: Normal

---

### Question 180
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Medium

Question: What is a denial of service (DoS) attack?
A) Stealing data
B) Overwhelming system to make it unavailable
C) Encrypting files
D) Installing software

✔ Correct Answer: B

Reason: DoS attack floods a system with traffic or requests to exhaust resources, making it unavailable to legitimate users.

Tag: Past Paper

---

### Question 181
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Hard

Question: What is a man-in-the-middle attack?
A) Physical attack
B) Intercepting communication between two parties
C) Password guessing
D) Virus infection

✔ Correct Answer: B

Reason: Man-in-the-middle attack intercepts and possibly alters communication between two parties who believe they're communicating directly.

Tag: Normal

---

### Question 182
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Attacks
Difficulty: Medium

Question: What is phishing?
A) Network protocol
B) Fraudulent attempt to obtain sensitive information
C) Encryption method
D) Backup technique

✔ Correct Answer: B

Reason: Phishing uses deceptive emails or websites to trick users into revealing sensitive information like passwords or credit card numbers.

Tag: Normal

---

### Question 183
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Buffer Overflow
Difficulty: Hard

Question: What is a buffer overflow attack?
A) Too much data storage
B) Writing data beyond buffer boundaries to execute malicious code
C) Network congestion
D) Disk full

✔ Correct Answer: B

Reason: Buffer overflow writes data beyond allocated buffer, potentially overwriting adjacent memory and executing malicious code.

Tag: Normal

---

### Question 184
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Mechanisms
Difficulty: Medium

Question: What is sandboxing?
A) Playing in sand
B) Isolating programs in restricted environment
C) Backing up data
D) Encrypting files

✔ Correct Answer: B

Reason: Sandboxing runs untrusted programs in isolated environment with limited access to system resources, containing potential damage.

Tag: Normal

---

### Question 185
Domain: Operating Systems
Topic: Protection & Security
Subtopic: Security Auditing
Difficulty: Medium

Question: What is security auditing?
A) Financial audit
B) Recording and reviewing security-relevant events
C) Deleting logs
D) Creating users

✔ Correct Answer: B

Reason: Security auditing records system activities and events for later review, helping detect security breaches and ensure compliance.

Tag: Normal

---

### Question 186
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls
Difficulty: Medium

Question: Which system call creates a new process in UNIX?
A) exec()
B) fork()
C) wait()
D) exit()

✔ Correct Answer: B

Reason: fork() creates a new process by duplicating the calling process, returning 0 to child and child's PID to parent.

Tag: Past Paper

---

### Question 187
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls
Difficulty: Hard

Question: What does the exec() family of system calls do?
A) Creates new process
B) Replaces current process image with new program
C) Terminates process
D) Waits for child

✔ Correct Answer: B

Reason: exec() replaces the current process's memory space with a new program, commonly used after fork() to run different program.

Tag: Normal

---

### Question 188
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Calls
Difficulty: Medium

Question: What does the wait() system call do?
A) Creates process
B) Parent waits for child process to terminate
C) Terminates process
D) Executes program

✔ Correct Answer: B

Reason: wait() suspends parent process until one of its child processes terminates, returning child's exit status.

Tag: Normal

---

### Question 189
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Kernel Modes
Difficulty: Easy

Question: What is user mode?
A) Kernel mode
B) Restricted mode with limited access to hardware
C) Full access mode
D) No mode

✔ Correct Answer: B

Reason: User mode is a restricted execution mode where applications run with limited privileges, unable to directly access hardware or critical system resources.

Tag: Normal

---

### Question 190
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Kernel Modes
Difficulty: Easy

Question: What is kernel mode?
A) User mode
B) Privileged mode with full hardware access
C) Restricted mode
D) No mode

✔ Correct Answer: B

Reason: Kernel mode (supervisor mode) allows unrestricted access to all hardware and system resources, used by OS kernel for critical operations.

Tag: Past Paper

---

### Question 191
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Mode Switching
Difficulty: Medium

Question: When does a mode switch from user to kernel occur?
A) Never
B) System call, interrupt, or exception
C) Random times
D) Only at boot

✔ Correct Answer: B

Reason: Mode switch to kernel occurs on system calls (explicit), interrupts (hardware events), or exceptions (errors), allowing OS to handle privileged operations.

Tag: Normal

---

### Question 192
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Virtual Machines
Difficulty: Hard

Question: What is a virtual machine?
A) Physical machine
B) Software emulation of complete computer system
C) Network device
D) Storage device

✔ Correct Answer: B

Reason: Virtual machine provides isolated environment emulating complete hardware, allowing multiple OS instances on single physical machine.

Tag: Normal

---

### Question 193
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Hypervisor
Difficulty: Hard

Question: What is a hypervisor?
A) User application
B) Software managing virtual machines
C) File system
D) Network protocol

✔ Correct Answer: B

Reason: Hypervisor (Virtual Machine Monitor) creates and manages virtual machines, allocating physical resources among VMs.

Tag: Normal

---

### Question 194
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Type 1 Hypervisor
Difficulty: Hard

Question: What characterizes a Type 1 hypervisor?
A) Runs on host OS
B) Runs directly on hardware (bare metal)
C) Runs in user space
D) No hardware access

✔ Correct Answer: B

Reason: Type 1 (bare-metal) hypervisor runs directly on hardware without host OS, providing better performance and isolation.

Tag: Normal

---

### Question 195
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Type 2 Hypervisor
Difficulty: Hard

Question: What characterizes a Type 2 hypervisor?
A) Runs on hardware directly
B) Runs on top of host operating system
C) No OS needed
D) Kernel-level only

✔ Correct Answer: B

Reason: Type 2 (hosted) hypervisor runs as application on host OS, easier to set up but with performance overhead.

Tag: Normal

---

### Question 196
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Containers
Difficulty: Hard

Question: How do containers differ from virtual machines?
A) Same thing
B) Containers share host OS kernel, VMs have separate OS
C) Containers are slower
D) No difference

✔ Correct Answer: B

Reason: Containers share host OS kernel and isolate applications, lighter than VMs which include full OS, but less isolated.

Tag: Normal

---

### Question 197
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: System Boot
Difficulty: Medium

Question: What is the boot process?
A) Shutting down
B) Loading OS into memory and starting execution
C) Installing OS
D) Updating OS

✔ Correct Answer: B

Reason: Boot process initializes hardware, loads bootloader, then loads OS kernel into memory and transfers control to it.

Tag: Normal

---

### Question 198
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: BIOS
Difficulty: Easy

Question: What does BIOS stand for?
A) Basic Input Output System
B) Binary Input Output System
C) Basic Internal Operating System
D) Binary Internal Operating System

✔ Correct Answer: A

Reason: BIOS (Basic Input/Output System) is firmware that initializes hardware during boot and provides runtime services for OS and programs.

Tag: Normal

---

### Question 199
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: UEFI
Difficulty: Medium

Question: What is UEFI?
A) Old BIOS version
B) Modern replacement for BIOS with enhanced features
C) Operating system
D) File system

✔ Correct Answer: B

Reason: UEFI (Unified Extensible Firmware Interface) replaces BIOS with modern features like secure boot, larger disk support, and faster boot times.

Tag: Normal

---

### Question 200
Domain: Operating Systems
Topic: Operating System Structures
Subtopic: Bootloader
Difficulty: Medium

Question: What is the role of a bootloader?
A) Load applications
B) Load operating system kernel into memory
C) Manage files
D) Schedule processes

✔ Correct Answer: B

Reason: Bootloader (like GRUB) loads OS kernel from disk into memory and transfers control to it, bridging firmware and OS.

Tag: Normal

---

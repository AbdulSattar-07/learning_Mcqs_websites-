# Computer Networks - MCQ Batch 06
## Questions 501-600

---

### Question 501
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Holddown Timer
Difficulty: Hard

Question: What is the purpose of holddown timer in distance vector routing?
A) Speed up convergence
B) Prevent accepting worse routes during convergence
C) Encrypt updates
D) Compress routing tables

✔ Correct Answer: B

Reason: Holddown timer prevents a router from accepting routes with worse metrics for a failed route during the convergence period, avoiding routing loops.

Tag: Normal

---

### Question 502
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Triggered Updates
Difficulty: Medium

Question: When are triggered updates sent in RIP?
A) Every 30 seconds
B) Immediately when topology changes
C) Every 60 seconds
D) Never

✔ Correct Answer: B

Reason: Triggered updates are sent immediately when a route metric changes, speeding up convergence instead of waiting for the regular update timer.

Tag: Normal

---

### Question 503
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Packet Types
Difficulty: Hard

Question: Which EIGRP packet type is used for route discovery?
A) Hello
B) Update
C) Query
D) Reply

✔ Correct Answer: C

Reason: Query packets are sent when a route is lost and no feasible successor exists, asking neighbors for alternative paths during route discovery.

Tag: Normal

---

### Question 504
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Hello Interval
Difficulty: Medium

Question: What is the default EIGRP hello interval on high-speed links?
A) 5 seconds
B) 10 seconds
C) 30 seconds
D) 60 seconds

✔ Correct Answer: A

Reason: EIGRP sends hello packets every 5 seconds on high-speed links (>1.544 Mbps) and 60 seconds on slow links. Hold time is 3x hello interval.

Tag: Normal

---

### Question 505
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Reliable Transport
Difficulty: Hard

Question: Which EIGRP packet types use reliable transport (RTP)?
A) Hello only
B) Update, Query, Reply
C) All packets
D) None

✔ Correct Answer: B

Reason: Update, Query, and Reply packets use RTP requiring acknowledgment. Hello and ACK packets use unreliable transport.

Tag: Normal

---

### Question 506
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Hello Interval
Difficulty: Medium

Question: What is the default OSPF hello interval on broadcast networks?
A) 5 seconds
B) 10 seconds
C) 30 seconds
D) 40 seconds

✔ Correct Answer: B

Reason: OSPF sends hellos every 10 seconds on broadcast/point-to-point networks and 30 seconds on NBMA networks. Dead interval is 4x hello.

Tag: Normal

---

### Question 507
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Adjacency
Difficulty: Hard

Question: What must match for OSPF routers to form adjacency?
A) Only router IDs
B) Area ID, hello/dead intervals, authentication, stub flag
C) Only IP addresses
D) Only subnet masks

✔ Correct Answer: B

Reason: OSPF adjacency requires matching area ID, hello/dead intervals, authentication, stub area flag, and MTU. Mismatches prevent adjacency formation.

Tag: Past Paper

---

### Question 508
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP K-values
Difficulty: Hard

Question: What must match for EIGRP routers to become neighbors?
A) Only AS number
B) AS number and K-values
C) Only router IDs
D) Only IP addresses

✔ Correct Answer: B

Reason: EIGRP neighbors must have matching AS numbers and K-values (metric weights). Mismatched K-values prevent neighbor relationships.

Tag: Normal

---

### Question 509
Domain: Computer Networks
Topic: Network Security
Subtopic: AAA
Difficulty: Medium

Question: What does AAA stand for in network security?
A) Access, Authorization, Accounting
B) Authentication, Authorization, Accounting
C) Authentication, Access, Auditing
D) Authorization, Access, Accounting

✔ Correct Answer: B

Reason: AAA stands for Authentication (verify identity), Authorization (grant permissions), and Accounting (track resource usage and activities).

Tag: Past Paper

---

### Question 510
Domain: Computer Networks
Topic: Network Security
Subtopic: 802.1X Components
Difficulty: Hard

Question: What are the three components in 802.1X authentication?
A) Client, Server, Database
B) Supplicant, Authenticator, Authentication Server
C) User, Switch, Router
D: Host, Gateway, Firewall

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: 802.1X uses Supplicant (client), Authenticator (switch/AP), and Authentication Server (RADIUS) for port-based network access control.

Tag: Normal

---

### Question 511
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EAP Methods
Difficulty: Hard

Question: Which EAP method uses TLS for mutual authentication?
A) EAP-MD5
B) EAP-TLS
C) EAP-PEAP
D) EAP-FAST

✔ Correct Answer: B

Reason: EAP-TLS uses TLS with certificates for mutual authentication (both client and server), providing strong security but requiring certificate management.

Tag: Normal

---

### Question 512
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PEAP
Difficulty: Hard

Question: What does PEAP (Protected EAP) provide?
A) Faster authentication
B: TLS tunnel protecting inner authentication
B) [Missing option - Please review]

C) No encryption
D) Simpler configuration

✔ Correct Answer: B

Reason: PEAP creates a TLS tunnel to protect the inner authentication method (like MS-CHAPv2), providing security without requiring client certificates.

Tag: Normal

---

### Question 513
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Campus Network
Difficulty: Medium

Question: What characterizes a campus network?
A) Single building only
B) Multiple buildings in limited geographic area
C) Global distribution
D) Wireless only

✔ Correct Answer: B

Reason: A campus network connects multiple buildings within a limited geographic area (university, corporate campus), typically owned by single organization.

Tag: Normal

---

### Question 514
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Enterprise Network
Difficulty: Easy

Question: What is an enterprise network?
A) Small home network
B: Organization's entire network infrastructure
B) [Missing option - Please review]

C) Public Internet
D) Single LAN

✔ Correct Answer: B

Reason: An enterprise network encompasses an organization's entire network infrastructure, including LANs, WANs, data centers, and remote sites.

Tag: Normal

---

### Question 515
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP Path Selection
Difficulty: Hard

Question: What is the first criterion in BGP path selection?
A) AS_PATH length
B) Highest weight (Cisco)
C) LOCAL_PREF
D: MED

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: BGP path selection follows a specific order. Cisco routers first check Weight (local to router), then LOCAL_PREF, then locally originated routes.

Tag: Normal

---

### Question 516
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP LOCAL_PREF
Difficulty: Hard

Question: What is the scope of BGP LOCAL_PREF attribute?
A) Global
B: Within the AS only
B) [Missing option - Please review]

C) Between two routers only
D) Across all ASes

✔ Correct Answer: B

Reason: LOCAL_PREF is used within an AS to influence outbound traffic path selection. It's not propagated to external BGP peers.

Tag: Normal

---

### Question 517
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP MED
Difficulty: Hard

Question: What does MED (Multi-Exit Discriminator) influence?
A) Outbound traffic
B) Inbound traffic from neighboring AS
C: Internal routing
C) [Missing option - Please review]

D) Multicast routing

✔ Correct Answer: B

Reason: MED is advertised to neighboring AS to influence how they send traffic into your AS when multiple entry points exist (lower MED is preferred).

Tag: Normal

---

### Question 518
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP AS_PATH Prepending
Difficulty: Hard

Question: Why would you prepend AS numbers to AS_PATH?
A) Increase security
B) Make path less preferred by increasing length
C) Faster routing
D: Better encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: AS_PATH prepending artificially lengthens the AS path to make it less preferred, influencing inbound traffic routing from other autonomous systems.

Tag: Normal

---

### Question 519
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP Communities
Difficulty: Hard

Question: What are BGP communities used for?
A) Social networking
B: Grouping routes for common policy application
B) [Missing option - Please review]

C) Encryption
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: BGP communities are tags attached to routes for grouping and applying common policies, simplifying route management across multiple routers.

Tag: Normal

---

### Question 520
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP Route Reflector
Difficulty: Hard

Question: What problem does BGP route reflector solve?
A: Slow convergence
B: Full mesh iBGP requirement
C: Security issues
D: Bandwidth limitations

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Route reflectors eliminate the need for full mesh iBGP by reflecting routes to clients, reducing the number of required iBGP sessions.

Tag: Normal

---

### Question 521
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP Confederation
Difficulty: Hard

Question: What is the purpose of BGP confederation?
A: Increase speed
B: Divide large AS into sub-ASes to reduce iBGP mesh
C: Encrypt BGP
D: Compress updates

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: BGP confederation divides a large AS into smaller sub-ASes, reducing iBGP full mesh requirements while appearing as single AS externally.

Tag: Normal

---

### Question 522
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Window Size
Difficulty: Medium

Question: What is the maximum TCP window size without window scaling?
A: 32 KB
B: 64 KB
C: 128 KB
D: 256 KB

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: The TCP window field is 16 bits, allowing maximum 65,535 bytes (64 KB). Window scaling option is needed for larger windows.

Tag: Normal

---

### Question 523
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Window Scaling Factor
Difficulty: Hard

Question: What is the maximum window scaling factor in TCP?
A: 8
B: 14
C: 16
D: 32

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: The window scale option uses 4 bits for shift count (0-14), allowing maximum window of 65535 × 2^14 = 1 GB.

Tag: Normal

---

### Question 524
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MSS
Difficulty: Medium

Question: What does MSS (Maximum Segment Size) specify?
A: Maximum packet size
B: Maximum TCP payload size
C: Maximum window size
D: Maximum frame size

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: MSS specifies the maximum amount of data in a TCP segment (excluding headers), typically 1460 bytes for Ethernet (1500 MTU - 20 IP - 20 TCP).

Tag: Past Paper

---

### Question 525
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MSS vs MTU
Difficulty: Medium

Question: How is MSS related to MTU?
A: MSS = MTU
B: MSS = MTU - IP header - TCP header
C: MSS > MTU
D: Unrelated

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: MSS = MTU - IP header (20) - TCP header (20). For 1500-byte MTU, MSS is typically 1460 bytes.

Tag: Normal

---

### Question 526
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Path MTU Discovery Issues
Difficulty: Hard

Question: What can cause PMTUD to fail?
A: Slow links
B: ICMP filtering by firewalls
C: High bandwidth
D: Low latency

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: PMTUD relies on ICMP "Fragmentation Needed" messages. If firewalls block ICMP, PMTUD fails, causing "black hole" where large packets are silently dropped.

Tag: Normal

---

### Question 527
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP MSS Clamping
Difficulty: Hard

Question: What is TCP MSS clamping used for?
A: Increase speed
B: Adjust MSS to prevent fragmentation
C: Encrypt TCP
D: Compress segments

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: MSS clamping modifies the MSS value in TCP SYN packets to prevent fragmentation, useful when PMTUD fails or in VPN/PPPoE scenarios.

Tag: Normal

---

### Question 528
Domain: Computer Networks
Topic: Network Protocols
Subtopic: GRE Overhead
Difficulty: Hard

Question: How much overhead does GRE add to packets?
A: 4 bytes
B: 20 bytes
C: 24 bytes (20 IP + 4 GRE)
D: 40 bytes

D) [Missing option - Please review]

✔ Correct Answer: C

Reason: GRE adds 24 bytes overhead: 20-byte IP header for tunnel and 4-byte GRE header (more with optional fields), reducing effective MTU.

Tag: Normal

---

### Question 529
Domain: Computer Networks
Topic: Network Protocols
Subtopic: IPSec Overhead
Difficulty: Hard

Question: Approximately how much overhead does IPSec ESP in tunnel mode add?
A: 10 bytes
B: 30 bytes
C: 50-60 bytes
D: 100 bytes

D) [Missing option - Please review]

✔ Correct Answer: C

Reason: IPSec ESP tunnel mode adds ~50-60 bytes: new IP header (20), ESP header (8), ESP trailer (2+padding), ESP auth (12), reducing effective MTU significantly.

Tag: Normal

---

### Question 530
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Offload
Difficulty: Hard

Question: What does TCP offload engine (TOE) do?
A: Disable TCP
B: Move TCP processing to network card
C: Encrypt TCP
D: Compress TCP

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: TOE offloads TCP/IP processing from CPU to the network interface card, reducing CPU usage and improving performance for high-throughput applications.

Tag: Normal

---

### Question 531
Domain: Computer Networks
Topic: Network Performance
Subtopic: RSS
Difficulty: Hard

Question: What does RSS (Receive Side Scaling) do?
A: Encrypt received packets
B: Distribute packet processing across multiple CPU cores
C: Compress received data
D: Filter received packets

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: RSS distributes network receive processing across multiple CPU cores using hash-based distribution, improving performance on multi-core systems.

Tag: Normal

---

### Question 532
Domain: Computer Networks
Topic: Network Performance
Subtopic: Interrupt Coalescing
Difficulty: Hard

Question: What is interrupt coalescing?
A: Combining packets
B: Batching interrupts to reduce CPU overhead
C: Encrypting interrupts
D: Blocking interrupts

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Interrupt coalescing batches multiple packet arrivals into single interrupt, reducing CPU overhead from interrupt handling at the cost of slight latency increase.

Tag: Normal

---

### Question 533
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Jumbo Frames Benefits
Difficulty: Medium

Question: What is the main benefit of jumbo frames?
A: Better security
B: Reduced overhead and CPU usage
C: Longer transmission distance
D: Better encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Jumbo frames reduce per-packet overhead (headers, interrupts, processing), improving throughput and reducing CPU usage for large data transfers.

Tag: Normal

---

### Question 534
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Jumbo Frames Requirement
Difficulty: Medium

Question: What is required for jumbo frames to work?
A: Only sender support
B: End-to-end support across all devices
C: Only receiver support
D: No special requirements

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: All devices in the path (NICs, switches, routers) must support jumbo frames. If any device doesn't support them, packets will be dropped or fragmented.

Tag: Normal

---

### Question 535
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Baby Giant Frames
Difficulty: Hard

Question: What are baby giant frames?
A: Small jumbo frames
B: Frames slightly larger than 1500 bytes for VLAN tags
C: Compressed frames
D: Encrypted frames

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Baby giant frames (1504-1522 bytes) accommodate VLAN tags (4 bytes) and QinQ (8 bytes) without being considered jumbo frames.

Tag: Normal

---

### Question 536
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Ethernet Frame Types
Difficulty: Medium

Question: Which Ethernet frame type is most commonly used today?
A: Ethernet II (DIX)
B: 802.3 with 802.2 LLC
C: 802.3 Raw
D: Token Ring

D) [Missing option - Please review]

✔ Correct Answer: A

Reason: Ethernet II (DIX) is the most common frame type, using a 2-byte EtherType field to identify the protocol (0x0800 for IPv4, 0x86DD for IPv6).

Tag: Normal

---

### Question 537
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ARP Timeout
Difficulty: Medium

Question: Why do ARP cache entries have timeouts?
A: Save memory
B: Ensure entries stay current and detect changes
C: Increase speed
D: Improve security

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: ARP cache timeouts (typically 2-20 minutes) ensure entries are refreshed, detecting when devices change IP addresses or are replaced.

Tag: Normal

---

### Question 538
Domain: Computer Networks
Topic: Network Security
Subtopic: MAC Spoofing
Difficulty: Medium

Question: What is MAC address spoofing?
A: Encrypting MAC addresses
B: Changing device's MAC address to impersonate another
C: Hiding MAC address
D: Compressing MAC addresses

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: MAC spoofing changes a device's MAC address to impersonate another device, bypassing MAC-based security controls or access restrictions.

Tag: Normal

---

### Question 539
Domain: Computer Networks
Topic: Network Security
Subtopic: CAM Table Overflow
Difficulty: Hard

Question: What is a CAM table overflow attack?
A: Overloading router
B: Flooding switch with fake MAC addresses to fill CAM table
C: DDoS attack
D: DNS attack

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: CAM table overflow floods a switch with fake MAC addresses, filling the CAM table and causing the switch to act like a hub, enabling sniffing.

Tag: Normal

---

### Question 540
Domain: Computer Networks
Topic: Network Security
Subtopic: Port Security Violation
Difficulty: Medium

Question: What happens in "shutdown" violation mode for port security?
A: Warning only
B: Port is disabled (err-disabled state)
C: Traffic is dropped silently
D: Nothing

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: In shutdown mode, the port enters err-disabled state when violation occurs, requiring manual intervention to re-enable, providing strongest security.

Tag: Normal

---

### Question 541
Domain: Computer Networks
Topic: Network Security
Subtopic: Port Security Modes
Difficulty: Hard

Question: In "restrict" violation mode, what happens?
A: Port shuts down
B: Violation packets dropped, SNMP trap sent, counter incremented
C: All traffic allowed
D: Port speed reduced

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Restrict mode drops violating packets, sends SNMP trap, and increments violation counter, but keeps port operational unlike shutdown mode.

Tag: Normal

---

### Question 542
Domain: Computer Networks
Topic: Network Security
Subtopic: Sticky MAC
Difficulty: Medium

Question: What does sticky MAC learning do in port security?
A: Makes MAC permanent
B: Dynamically learns and saves MAC addresses to config
C: Blocks all MACs
D: Encrypts MACs

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Sticky MAC learning dynamically learns MAC addresses and adds them to running configuration, combining convenience of dynamic learning with persistence.

Tag: Normal

---

### Question 543
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DTP Modes
Difficulty: Hard

Question: Which DTP mode actively attempts to form a trunk?
A: Access
B: Dynamic desirable
C: Dynamic auto
D: Trunk

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Dynamic desirable actively sends DTP frames to negotiate trunk. Dynamic auto waits for the other side to initiate. Trunk mode forces trunking.

Tag: Normal

---

### Question 544
Domain: Computer Networks
Topic: Network Protocols
Subtopic: VTP Modes
Difficulty: Hard

Question: Which VTP mode can create, modify, and delete VLANs?
A: Client
B: Server
C: Transparent
D: Off

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: VTP Server mode can create/modify/delete VLANs and propagate changes. Client mode receives updates, Transparent mode doesn't participate but forwards updates.

Tag: Normal

---

### Question 545
Domain: Computer Networks
Topic: Network Protocols
Subtopic: VTP Pruning
Difficulty: Hard

Question: What does VTP pruning do?
A: Deletes VLANs
B: Restricts flooded traffic to trunk links with active VLANs
C: Removes old entries
D: Compresses VTP messages

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: VTP pruning prevents unnecessary broadcast, multicast, and unknown unicast traffic from being sent over trunk links to switches without active ports in that VLAN.

Tag: Normal

---

### Question 546
Domain: Computer Networks
Topic: Network Protocols
Subtopic: VTP Version 3
Difficulty: Hard

Question: What feature does VTP version 3 add?
A: Faster updates
B: Extended VLAN support and authentication
C: Encryption
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: VTP v3 adds extended VLAN range support (1-4094), improved authentication, and protection against accidental database overwrites with primary server concept.

Tag: Normal

---

### Question 547
Domain: Computer Networks
Topic: Network Design
Subtopic: Broadcast Storm
Difficulty: Medium

Question: What causes a broadcast storm?
A: Too many users
B: Layer 2 loops causing infinite broadcast propagation
C: High bandwidth
D: Encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Broadcast storms occur when Layer 2 loops exist, causing broadcasts to circulate infinitely, consuming all bandwidth and overwhelming devices.

Tag: Past Paper

---

### Question 548
Domain: Computer Networks
Topic: Network Protocols
Subtopic: STP Convergence Time
Difficulty: Medium

Question: What is the typical convergence time for traditional STP (802.1D)?
A: 1-2 seconds
B: 5-10 seconds
C: 30-50 seconds
D: 2-3 minutes

✔ Correct Answer: C

Reason: Traditional STP takes 30-50 seconds to converge (20s listening + 15s learning + timers). RSTP reduces this to 1-2 seconds.

Tag: Normal

---

### Question 549
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RSTP Port States
Difficulty: Hard

Question: How many port states does RSTP have?
A: 3 (Discarding, Learning, Forwarding)
B: 5
C: 2
D: 4

D) [Missing option - Please review]

✔ Correct Answer: A

Reason: RSTP simplifies STP's 5 states to 3: Discarding (combines Disabled, Blocking, Listening), Learning, and Forwarding.

Tag: Normal

---

### Question 550
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RSTP Port Roles
Difficulty: Hard

Question: Which port role is unique to RSTP (not in STP)?
A: Root port
B: Designated port
C: Alternate port
D: Disabled port

D) [Missing option - Please review]

✔ Correct Answer: C

Reason: RSTP adds Alternate (backup path to root) and Backup (backup designated port) roles, enabling faster convergence by pre-identifying backup paths.

Tag: Normal

---

### Question 551
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RSTP Proposal/Agreement
Difficulty: Hard

Question: What does RSTP proposal/agreement mechanism provide?
A: Encryption
B: Rapid convergence without waiting timers
C: Load balancing
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: RSTP's proposal/agreement handshake allows rapid transition to forwarding state without waiting for timers, achieving sub-second convergence.

Tag: Normal

---

### Question 552
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MST Regions
Difficulty: Hard

Question: What must match for switches to be in the same MST region?
A: Only region name
B: Region name, revision number, and VLAN-to-instance mapping
C: Only VLAN configuration
D: Only priority

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: MST region membership requires matching region name, revision number, and identical VLAN-to-instance mapping across all switches.

Tag: Normal

---

### Question 553
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MST Instances
Difficulty: Hard

Question: How many MST instances can be configured?
A: 16
B: 64
C: 4096
D: 16 (0-15) plus IST

D) [Missing option - Please review]

✔ Correct Answer: D

Reason: MST supports 16 instances (0-15). Instance 0 is the IST (Internal Spanning Tree), and instances 1-15 can be configured for VLAN groups.

Tag: Normal

---

### Question 554
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EtherChannel Load Balancing
Difficulty: Medium

Question: Which method can EtherChannel use for load balancing?
A: Round robin only
B: Source/destination MAC, IP, or port hashing
C: Random selection
D: Bandwidth-based

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: EtherChannel uses hash-based load balancing on source/destination MAC, IP, or port numbers to distribute traffic across member links consistently.

Tag: Normal

---

### Question 555
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EtherChannel Requirements
Difficulty: Medium

Question: What must match for ports to form an EtherChannel?
A: Only speed
B: Speed, duplex, VLAN, and other configurations
C: Only VLAN
D: Nothing

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: EtherChannel members must have matching speed, duplex, VLAN configuration, and other settings. Mismatches prevent bundle formation.

Tag: Normal

---

### Question 556
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LACP Modes
Difficulty: Hard

Question: Which LACP mode actively initiates negotiation?
A: On
B: Active
C: Passive
D: Auto

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: LACP Active mode actively sends LACP packets to negotiate. Passive mode waits for the other side. At least one side must be Active.

Tag: Normal

---

### Question 557
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PAgP Modes
Difficulty: Hard

Question: Which PAgP mode actively initiates negotiation?
A: On
B: Desirable
C: Auto
D: Off

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: PAgP Desirable mode actively sends PAgP packets. Auto mode waits for the other side. At least one side must be Desirable.

Tag: Normal

---

### Question 558
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EtherChannel Guard
Difficulty: Hard

Question: What does EtherChannel guard prevent?
A: Port failures
B: Loops from EtherChannel misconfiguration
C: Bandwidth issues
D: Security breaches

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: EtherChannel guard detects misconfigurations where one side forms channel but other doesn't, preventing loops by disabling the port.

Tag: Normal

---

### Question 559
Domain: Computer Networks
Topic: Network Design
Subtopic: Uplink
Difficulty: Easy

Question: What is an uplink in network terminology?
A: Wireless connection
B: Connection from lower to higher layer in hierarchy
C: Backup link
D: Encrypted link

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: An uplink connects a device to a higher-level device in the network hierarchy, such as access switch to distribution switch.

Tag: Normal

---

### Question 560
Domain: Computer Networks
Topic: Network Design
Subtopic: Downlink
Difficulty: Easy

Question: What is a downlink?
A: Failed link
B: Connection from higher to lower layer in hierarchy
C: Slow link
D: Wireless link only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: A downlink connects from a higher-level device to a lower-level device, such as distribution switch to access switch or base station to mobile device.

Tag: Normal

---

### Question 561
Domain: Computer Networks
Topic: Network Protocols
Subtopic: UDLD
Difficulty: Hard

Question: What does UDLD (Unidirectional Link Detection) detect?
A: Slow links
B: Links where traffic flows only one direction
C: Encrypted links
D: Wireless links

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: UDLD detects unidirectional links where traffic flows only one way, which can cause loops and other issues. It disables affected ports.

Tag: Normal

---

### Question 562
Domain: Computer Networks
Topic: Network Protocols
Subtopic: UDLD Modes
Difficulty: Hard

Question: What does UDLD aggressive mode do?
A: Increases speed
B: Disables port on any UDLD failure including neighbor loss
C: Encrypts traffic
D: Increases bandwidth

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Aggressive mode disables ports not only for unidirectional links but also when UDLD neighbor information is lost, providing stronger protection.

Tag: Normal

---

### Question 563
Domain: Computer Networks
Topic: Network Performance
Subtopic: Micro-segmentation
Difficulty: Hard

Question: What is micro-segmentation in modern networks?
A: Creating tiny subnets
B: Isolating workloads with granular security policies
C: Physical cable segmentation
D: VLAN subdivision only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Micro-segmentation creates fine-grained security zones, isolating individual workloads or applications with specific policies, often using software-defined networking.

Tag: Normal

---

### Question 564
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Zero Trust
Difficulty: Medium

Question: What is the core principle of zero trust networking?
A: Trust all internal traffic
B: Never trust, always verify
C: Trust based on location
D: Trust based on device type

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Zero trust assumes no implicit trust based on network location, requiring verification for every access request regardless of source.

Tag: Normal

---

### Question 565
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LISP
Difficulty: Hard

Question: What does LISP (Locator/ID Separation Protocol) separate?
A: VLANs
B: Device identity from location
C: Data and control planes
D: IPv4 and IPv6

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: LISP separates endpoint identifiers (EIDs) from routing locators (RLOCs), improving scalability and mobility in large networks.

Tag: Normal

---

### Question 566
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Fabric
Difficulty: Hard

Question: What is a network fabric?
A: Physical cables
B: Unified network architecture with consistent policies
C: Wireless network
D: Backup network

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: A network fabric provides a unified, flat architecture with consistent policies and simplified management, often using technologies like VXLAN and EVPN.

Tag: Normal

---

### Question 567
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Leaf-Spine Benefits
Difficulty: Medium

Question: What is a key benefit of leaf-spine architecture?
A: Lower cost only
B: Predictable latency and high bandwidth
C: Simpler cabling only
D: Less equipment

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Leaf-spine provides predictable latency (maximum 2 hops) and high bisectional bandwidth through full mesh between layers, ideal for data centers.

Tag: Normal

---

### Question 568
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TRILL
Difficulty: Hard

Question: What does TRILL (Transparent Interconnection of Lots of Links) provide?
A: Encryption
B: Layer 2 multipathing using IS-IS
C: Faster switching
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: TRILL uses IS-IS routing at Layer 2 to enable multipathing and eliminate STP's single path limitation, improving bandwidth utilization.

Tag: Normal

---

### Question 569
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SPB
Difficulty: Hard

Question: What does SPB (Shortest Path Bridging) provide?
A: Longest path routing
B: Layer 2 multipathing alternative to STP
C: Layer 3 routing only
D: Encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: SPB (802.1aq) provides Layer 2 multipathing using IS-IS, similar to TRILL, eliminating STP limitations and enabling all paths to be used.

Tag: Normal

---

### Question 570
Domain: Computer Networks
Topic: Network Protocols
Subtopic: FabricPath
Difficulty: Hard

Question: What is Cisco FabricPath?
A: Physical cable type
B: Layer 2 multipathing technology
C: Routing protocol
D: Encryption method

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: FabricPath is Cisco's Layer 2 multipathing technology similar to TRILL, using IS-IS to enable all links in a network to forward traffic.

Tag: Normal

---

### Question 571
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Clos Network
Difficulty: Hard

Question: What is a Clos network topology?
A: Ring topology
B: Multi-stage switching fabric with multiple paths
C: Bus topology
D: Single path topology

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Clos topology is a multi-stage switching fabric providing multiple paths between endpoints, used in modern data center leaf-spine architectures.

Tag: Normal

---

### Question 572
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Fat Tree
Difficulty: Hard

Question: What characterizes a fat tree topology?
A: Single root
B: Increasing bandwidth toward root
C: Decreasing bandwidth toward root
D: Equal bandwidth everywhere

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Fat tree topology increases bandwidth toward the root by using more links or higher-speed links, preventing bottlenecks at higher levels.

Tag: Normal

---

### Question 573
Domain: Computer Networks
Topic: Network Performance
Subtopic: Elephant Flows
Difficulty: Hard

Question: What are elephant flows?
A: Small, short-lived flows
B: Large, long-lived flows consuming significant bandwidth
C: Multicast flows
D: Encrypted flows

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Elephant flows are large, long-duration flows that consume significant bandwidth, requiring special handling for load balancing and QoS.

Tag: Normal

---

### Question 574
Domain: Computer Networks
Topic: Network Performance
Subtopic: Mice Flows
Difficulty: Hard

Question: What characterizes mice flows?
A: Large size
B: Small, short-lived flows
C: Long duration
D: High bandwidth

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Mice flows are small, short-lived flows (like web requests) that are latency-sensitive. Most flows are mice, but elephants consume most bandwidth.

Tag: Normal

---

### Question 575
Domain: Computer Networks
Topic: Network Load Balancing
Subtopic: ECMP Hashing
Difficulty: Hard

Question: Why does ECMP use hashing for path selection?
A: Encryption
B: Ensure packets of same flow take same path
C: Random distribution
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: ECMP uses hash of packet headers to select path, ensuring all packets of a flow take the same path, preventing reordering.

Tag: Normal

---

### Question 576
Domain: Computer Networks
Topic: Network Load Balancing
Subtopic: Flow-based vs Packet-based
Difficulty: Hard

Question: What is the advantage of flow-based load balancing over packet-based?
A: Faster
B: Prevents packet reordering within flows
C: Better encryption
D: Lower latency

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Flow-based load balancing keeps all packets of a flow on the same path, preventing reordering. Packet-based can cause reordering but better load distribution.

Tag: Normal

---

### Question 577
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Anycast Gateway
Difficulty: Hard

Question: What is an anycast gateway in VXLAN?
A: Single gateway
B: Same gateway IP/MAC on multiple VTEPs
C: Random gateway
D: Backup gateway

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Anycast gateway configures the same gateway IP and MAC on multiple VTEPs, allowing hosts to use any VTEP as gateway, improving load distribution.

Tag: Normal

---

### Question 578
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Active-Active
Difficulty: Medium

Question: What is active-active configuration?
A: One active, one standby
B: Multiple devices actively forwarding traffic simultaneously
C: All devices standby
D: Sequential activation

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Active-active configuration has multiple devices simultaneously forwarding traffic, providing both load balancing and redundancy, unlike active-standby.

Tag: Normal

---

### Question 579
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Active-Standby
Difficulty: Easy

Question: In active-standby configuration, when does standby device activate?
A: Immediately
B: When active device fails
C: Never
D: Randomly

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: In active-standby, the standby device remains idle and takes over only when the active device fails, providing redundancy without load balancing.

Tag: Normal

---

### Question 580
Domain: Computer Networks
Topic: Network Protocols
Subtopic: FHRP Comparison
Difficulty: Medium

Question: Which FHRP provides load balancing by default?
A: HSRP
B: VRRP
C: GLBP
D: None

D) [Missing option - Please review]

✔ Correct Answer: C

Reason: GLBP provides load balancing by assigning different virtual MAC addresses to hosts, distributing traffic across multiple routers. HSRP/VRRP are active-standby.

Tag: Normal

---

### Question 581
Domain: Computer Networks
Topic: Network Security
Subtopic: General
Subtip: VLAN Security Best Practices
Difficulty: Medium

Question: Which is a VLAN security best practice?
A: Use VLAN 1 for all traffic
B: Change native VLAN from default and disable unused ports
C: Enable DTP on all ports
D: Use same VLAN for all devices

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Security best practices include changing native VLAN from default (1), disabling unused ports, disabling DTP, and using dedicated management VLAN.

Tag: Normal

---

### Question 582
Domain: Computer Networks
Topic: Network Security
Subtopic: Management VLAN
Difficulty: Medium

Question: Why use a separate management VLAN?
A: Faster management
B: Isolate management traffic for security
C: Reduce costs
D: Increase bandwidth

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Separate management VLAN isolates management traffic (SSH, SNMP, etc.) from user traffic, improving security and preventing unauthorized access.

Tag: Normal

---

### Question 583
Domain: Computer Networks
Topic: Network Security
Subtopic: Voice VLAN
Difficulty: Medium

Question: Why use a separate voice VLAN for IP phones?
A: Phones require it
B: QoS prioritization and security separation
C: Cost reduction
D: Faster calls

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Separate voice VLAN enables QoS prioritization for voice traffic, security separation from data, and simplified troubleshooting.

Tag: Normal

---

### Question 584
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LLDP-MED Voice VLAN
Difficulty: Hard

Question: How do IP phones discover voice VLAN?
A: Manual configuration
B: LLDP-MED or CDP from switch
C: DHCP
D: DNS

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Switches advertise voice VLAN information via LLDP-MED or CDP, allowing IP phones to automatically configure themselves for the correct VLAN.

Tag: Normal

---

### Question 585
Domain: Computer Networks
Topic: Network QoS
Subtopic: Trust Boundary
Difficulty: Medium

Question: What is a trust boundary in QoS?
A: Firewall location
B: Point where QoS markings are trusted or remarked
C: Network edge only
D: Router location

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Trust boundary defines where QoS markings are trusted. Typically at IP phones or servers; user devices are untrusted and traffic is remarked.

Tag: Normal

---

### Question 586
Domain: Computer Networks
Topic: Network QoS
Subtopic: Marking vs Classification
Difficulty: Medium

Question: What is the difference between classification and marking?
A: They are the same
B: Classification identifies traffic, marking sets QoS bits
C: Marking is faster
D: Classification is more secure

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Classification identifies traffic based on criteria (ACLs, NBAR), while marking sets QoS bits (DSCP, CoS) in packet headers for downstream QoS treatment.

Tag: Normal

---

### Question 587
Domain: Computer Networks
Topic: Network QoS
Subtopic: NBAR
Difficulty: Hard

Question: What does NBAR (Network-Based Application Recognition) do?
A: Encrypts applications
B: Classifies traffic by deep packet inspection
C: Blocks applications
D: Compresses traffic

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: NBAR performs deep packet inspection to classify applications beyond simple port/protocol matching, enabling application-aware QoS and policies.

Tag: Normal

---

### Question 588
Domain: Computer Networks
Topic: Network QoS
Subtopic: Queuing Disciplines
Difficulty: Medium

Question: Which queuing method serves all queues equally?
A: Priority queuing
B: Round robin
C: Weighted fair queuing
D: FIFO

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Round robin serves each queue in turn equally, providing fair distribution. WFQ uses weights, priority queuing favors high-priority queues.

Tag: Normal

---

### Question 589
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Ethernet Pause
Difficulty: Medium

Question: What is a limitation of 802.3x PAUSE frames?
A: Too slow
B: Pauses all traffic, not per-priority
C: Too complex
D: Requires expensive hardware

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Standard PAUSE frames stop all traffic on a link. PFC (Priority Flow Control) improves this by allowing per-priority class pausing.

Tag: Normal

---

### Question 590
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Cut-through Switching
Difficulty: Medium

Question: What is cut-through switching?
A: Cutting cables
B: Forwarding frame before fully received
C: Blocking traffic
D: Encrypting frames

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Cut-through switching forwards frames after reading destination MAC (first 6 bytes), reducing latency but not checking for errors.

Tag: Normal

---

### Question 591
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Store-and-Forward
Difficulty: Easy

Question: What does store-and-forward switching do?
A: Forwards immediately
B: Receives entire frame, checks errors, then forwards
C: Stores frames permanently
D: Forwards to all ports

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Store-and-forward receives the entire frame, checks FCS for errors, then forwards only error-free frames, providing reliability at cost of latency.

Tag: Past Paper

---

### Question 592
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Fragment-Free Switching
Difficulty: Hard

Question: What does fragment-free switching check?
A: Entire frame
B: First 64 bytes for collision fragments
C: Only destination MAC
D: Nothing

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Fragment-free switching reads first 64 bytes (minimum frame size) to filter collision fragments, balancing speed and error detection.

Tag: Normal

---

### Question 593
Domain: Computer Networks
Topic: Network Performance
Subtopic: Switching Latency
Difficulty: Medium

Question: Which switching method has the lowest latency?
A: Store-and-forward
B: Cut-through
C: Fragment-free
D: All equal

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Cut-through has lowest latency (microseconds) as it forwards after reading destination MAC. Store-and-forward has higher latency but better error handling.

Tag: Normal

---

### Question 594
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MAC Address Table
Difficulty: Easy

Question: How does a switch learn MAC addresses?
A: Manual configuration
B: Examining source MAC of received frames
C: DNS queries
D: DHCP

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Switches learn MAC addresses by examining the source MAC address of received frames and associating it with the ingress port.

Tag: Normal

---

### Question 595
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MAC Address Aging
Difficulty: Medium

Question: What is the typical MAC address table aging time?
A: 30 seconds
B: 5 minutes (300 seconds)
C: 1 hour
D: 24 hours

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Default MAC address aging time is typically 300 seconds (5 minutes). Entries are refreshed when traffic is seen from that MAC address.

Tag: Normal

---

### Question 596
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Unknown Unicast Flooding
Difficulty: Medium

Question: What does a switch do with a frame destined to an unknown MAC address?
A: Drops it
B: Floods it out all ports except ingress port
C: Sends to router
D: Buffers it

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: When destination MAC is not in the table, the switch floods the frame out all ports (except ingress) in the VLAN, similar to broadcast.

Tag: Normal

---

### Question 597
Domain: Computer Networks
Topic: Network Security
Subtopic: Unknown Unicast Flood Blocking
Difficulty: Hard

Question: Why would you block unknown unicast flooding?
A: Increase speed
B: Prevent CAM table overflow attacks
C: Reduce costs
D: Improve encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Blocking unknown unicast flooding on certain ports prevents attackers from exploiting CAM table overflow to sniff traffic through flooding.

Tag: Normal

---

### Question 598
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Multicast MAC Address
Difficulty: Hard

Question: How is a multicast MAC address identified?
A: First byte is FF
B: Least significant bit of first byte is 1
C: Last byte is FF
D: All bytes are same

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Multicast MAC addresses have the least significant bit of the first byte set to 1 (e.g., 01:00:5E:xx:xx:xx for IPv4 multicast).

Tag: Normal

---

### Question 599
Domain: Computer Networks
Topic: Network Protocols
Subtopic: IGMP Snooping
Difficulty: Hard

Question: What does IGMP snooping do?
A: Spies on users
B: Forwards multicast only to ports with interested receivers
C: Blocks all multicast
D: Encrypts multicast

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: IGMP snooping examines IGMP messages to learn which ports have multicast receivers, forwarding multicast only to those ports instead of flooding.

Tag: Normal

---

### Question 600
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MLD
Difficulty: Hard

Question: What is MLD in IPv6?
A: Multicast routing protocol
B: IPv6 equivalent of IGMP for multicast group management
C: Encryption protocol
D: Load balancing protocol

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: MLD (Multicast Listener Discovery) is the IPv6 equivalent of IGMP, managing multicast group memberships for IPv6 hosts.

Tag: Normal

---

# Computer Networks - MCQ Batch 05
## Questions 401-500

---

### Question 401
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HSRP Preempt
Difficulty: Hard

Question: What does HSRP preempt allow?
A) Faster routing
B) Higher priority router to reclaim active role
C) Load balancing
D) Encryption

✔ Correct Answer: B

Reason: Preempt allows a router with higher priority to take over the active role from a lower priority active router, ensuring optimal router is always active.

Tag: Normal

---

### Question 402
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HSRP Tracking
Difficulty: Hard

Question: What is interface tracking in HSRP?
A) Monitor bandwidth usage
B) Adjust priority based on interface status
C) Track MAC addresses
D) Monitor temperature

✔ Correct Answer: B

Reason: Interface tracking monitors specified interfaces and decrements HSRP priority if they fail, triggering failover to standby router.

Tag: Normal

---

### Question 403
Domain: Computer Networks
Topic: Network Design
Subtopic: Hierarchical Model
Difficulty: Medium

Question: What are the three layers in the hierarchical network design model?
A) Physical, Logical, Application
B) Core, Distribution, Access
C) Input, Processing, Output
D) Client, Server, Database

✔ Correct Answer: B

Reason: The hierarchical model consists of Core (high-speed backbone), Distribution (routing and policy), and Access (end-user connectivity) layers.

Tag: Past Paper

---

### Question 404
Domain: Computer Networks
Topic: Network Design
Subtopic: Core Layer
Difficulty: Medium

Question: What is the primary function of the core layer?
A) Connect end users
B) High-speed packet switching and routing
C) Apply security policies
D) Provide wireless access

✔ Correct Answer: B

Reason: The core layer provides high-speed, reliable packet switching and routing between distribution layer devices, focusing on speed and reliability.

Tag: Normal

---

### Question 405
Domain: Computer Networks
Topic: Network Design
Subtopic: Distribution Layer
Difficulty: Medium

Question: Which functions are typically performed at the distribution layer?
A) Only routing
B) Routing, filtering, and policy enforcement
C) Only switching
D) Only security

✔ Correct Answer: B

Reason: The distribution layer performs routing between VLANs, implements policies, filters traffic, and aggregates access layer connections.

Tag: Normal

---

### Question 406
Domain: Computer Networks
Topic: Network Design
Subtopic: Access Layer
Difficulty: Easy

Question: What is the primary function of the access layer?
A) High-speed routing
B) Provide network access to end devices
C) Internet connectivity
D) Backup services

✔ Correct Answer: B

Reason: The access layer (edge layer) provides network connectivity to end-user devices, implementing port security, VLANs, and PoE.

Tag: Normal

---

### Question 407
Domain: Computer Networks
Topic: Network Protocols
Subtopic: STP Cost
Difficulty: Hard

Question: What is the default STP cost for a 1 Gbps link?
A) 1
B) 4
C) 19
D) 100

✔ Correct Answer: B

Reason: Using the IEEE 802.1D-1998 standard, 1 Gbps link has cost 4. The formula is 1000 Mbps / link speed. Newer standards use different calculations.

Tag: Normal

---

### Question 408
Domain: Computer Networks
Topic: Network Protocols
Subtopic: STP Priority
Difficulty: Medium

Question: What is the default STP bridge priority?
A) 0
B) 32768
C) 65535
D) 100

✔ Correct Answer: B

Reason: The default STP bridge priority is 32768. Priority values must be multiples of 4096 in modern implementations.

Tag: Normal

---

### Question 409
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PVST+
Difficulty: Hard

Question: What does PVST+ provide?
A) Single STP instance for all VLANs
B) Separate STP instance per VLAN
C) No STP
D) Faster convergence only

✔ Correct Answer: B

Reason: PVST+ (Per-VLAN Spanning Tree Plus) runs a separate STP instance for each VLAN, allowing per-VLAN root bridges and load balancing.

Tag: Normal

---

### Question 410
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MST
Difficulty: Hard

Question: What advantage does MST have over PVST+?
A) Simpler configuration
B) Maps multiple VLANs to fewer STP instances
C) Faster
D) More secure

✔ Correct Answer: B

Reason: MST (Multiple Spanning Tree) maps multiple VLANs to a single STP instance, reducing CPU and memory overhead compared to PVST+'s per-VLAN instances.

Tag: Normal

---

### Question 411
Domain: Computer Networks
Topic: Network Performance
Subtopic: Serialization Delay
Difficulty: Hard

Question: What is serialization delay?
A) Time to route a packet
B) Time to put bits on the wire
C) Time for signal propagation
D) Time in queue

✔ Correct Answer: B

Reason: Serialization delay is the time required to transmit all bits of a packet onto the link, calculated as packet size divided by link bandwidth.

Tag: Normal

---

### Question 412
Domain: Computer Networks
Topic: Network Performance
Subtopic: Processing Delay
Difficulty: Medium

Question: What causes processing delay in routers?
A) Cable length
B) Time to examine header and determine output port
C) Bandwidth limitations
D) Encryption

✔ Correct Answer: B

Reason: Processing delay is the time routers take to examine packet headers, check for errors, and determine the appropriate output port.

Tag: Normal

---

### Question 413
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Proxy ARP
Difficulty: Hard

Question: What does Proxy ARP do?
A) Encrypts ARP
B) Router responds to ARP requests on behalf of other devices
C) Blocks ARP requests
D) Compresses ARP tables

✔ Correct Answer: B

Reason: Proxy ARP allows a router to respond to ARP requests on behalf of devices on another network, making remote devices appear local.

Tag: Normal

---

### Question 414
Domain: Computer Networks
Topic: Network Addressing
Subtopic: Classless Addressing
Difficulty: Medium

Question: What problem does CIDR solve?
A) Slow routing
B) IPv4 address exhaustion and routing table growth
C) Security issues
D) Bandwidth limitations

✔ Correct Answer: B

Reason: CIDR (Classless Inter-Domain Routing) eliminates class boundaries, allowing flexible address allocation and route aggregation, slowing IPv4 exhaustion.

Tag: Past Paper

---

### Question 415
Domain: Computer Networks
Topic: Network Addressing
Subtopic: Longest Prefix Match
Difficulty: Hard

Question: In routing, what is longest prefix matching?
A) Matching longest domain name
B) Selecting route with most specific (longest) subnet mask
C) Matching longest packet
D) Selecting fastest route

✔ Correct Answer: B

Reason: Longest prefix matching selects the routing entry with the most specific (longest) subnet mask that matches the destination, ensuring most accurate routing.

Tag: Normal

---

### Question 416
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ICMP Types
Difficulty: Medium

Question: Which ICMP message type is used by ping?
A) Type 0 and 8 (Echo Reply and Echo Request)
B) Type 3 (Destination Unreachable)
C) Type 11 (Time Exceeded)
D) Type 5 (Redirect)

✔ Correct Answer: A

Reason: Ping uses ICMP Echo Request (Type 8) and Echo Reply (Type 0) messages to test connectivity and measure round-trip time.

Tag: Normal

---

### Question 417
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ICMP Redirect
Difficulty: Hard

Question: When does a router send an ICMP Redirect message?
A) When destination is unreachable
B) When a better route exists on the same subnet
C) When TTL expires
D) On every packet

✔ Correct Answer: B

Reason: Routers send ICMP Redirect (Type 5) to inform hosts of a better route on the same subnet, optimizing the host's routing table.

Tag: Normal

---

### Question 418
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ICMP Destination Unreachable
Difficulty: Medium

Question: What does ICMP Destination Unreachable indicate?
A) Network congestion
B) Packet cannot be delivered for various reasons
C) Successful delivery
D) Encryption failure

✔ Correct Answer: B

Reason: ICMP Destination Unreachable (Type 3) has various codes indicating why a packet couldn't be delivered (network, host, port, protocol unreachable, etc.).

Tag: Normal

---

### Question 419
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ICMP Time Exceeded
Difficulty: Medium

Question: When is ICMP Time Exceeded sent?
A) When packet is too large
B) When TTL reaches zero
C) When bandwidth is exceeded
D) When port is closed

✔ Correct Answer: B

Reason: ICMP Time Exceeded (Type 11) is sent when a packet's TTL reaches zero, preventing infinite routing loops. Traceroute uses this mechanism.

Tag: Past Paper

---

### Question 420
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MTU Path Discovery
Difficulty: Hard

Question: Which ICMP message is used in Path MTU Discovery?
A) Echo Request
B) Destination Unreachable - Fragmentation Needed
C) Time Exceeded
D) Redirect

✔ Correct Answer: B

Reason: When a router receives a packet with DF bit set that's too large, it sends ICMP Destination Unreachable with "Fragmentation Needed" code and MTU size.

Tag: Normal

---

### Question 421
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Retransmission
Difficulty: Hard

Question: How is TCP retransmission timeout (RTO) calculated?
A) Fixed value
B) Based on measured RTT with variance
C) Random value
D) Based on bandwidth only

✔ Correct Answer: B

Reason: RTO is dynamically calculated based on smoothed RTT and RTT variance using exponential weighted moving average, adapting to network conditions.

Tag: Normal

---

### Question 422
Domain: Computer Networks
Topic: TCP Performance
Subtopic: Silly Window Syndrome
Difficulty: Hard

Question: What is silly window syndrome?
A) Large window sizes
B) Small segments reducing efficiency
C) Window size of zero
D) Infinite window size

✔ Correct Answer: B

Reason: Silly window syndrome occurs when small window sizes or small data chunks lead to transmission of many tiny segments, reducing efficiency.

Tag: Normal

---

### Question 423
Domain: Computer Networks
Topic: Network Protocols
Subtopic: VLAN Hopping
Difficulty: Hard

Question: What is VLAN hopping?
A) Switching between VLANs normally
B) Security attack to access unauthorized VLANs
C) Fast VLAN switching
D) VLAN backup method

✔ Correct Answer: B

Reason: VLAN hopping is an attack where an attacker sends packets to VLANs they shouldn't access, exploiting trunk configurations or double-tagging.

Tag: Normal

---

### Question 424
Domain: Computer Networks
Topic: Network Security
Subtopic: Double Tagging
Difficulty: Hard

Question: How does double tagging VLAN attack work?
A) Using two switches
B) Adding two VLAN tags to exploit native VLAN
C) Sending packets twice
D) Using two MAC addresses

✔ Correct Answer: B

Reason: Double tagging adds two 802.1Q tags. The first switch removes outer tag (native VLAN), and the inner tag directs packet to target VLAN on next switch.

Tag: Normal

---

### Question 425
Domain: Computer Networks
Topic: Network Security
Subtopic: Switch Spoofing
Difficulty: Hard

Question: What is switch spoofing in VLAN security?
A) Faking MAC address
B) Attacker negotiates trunk to access multiple VLANs
C) Spoofing IP address
D) Faking switch identity

✔ Correct Answer: B

Reason: Switch spoofing exploits DTP to negotiate a trunk link, allowing the attacker to send and receive traffic from multiple VLANs.

Tag: Normal

---

### Question 426
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Private VLAN
Difficulty: Hard

Question: What is the purpose of Private VLANs?
A) Encrypt VLAN traffic
B) Isolate devices within same VLAN
C) Increase VLAN speed
D) Reduce VLAN count

✔ Correct Answer: B

Reason: Private VLANs subdivide a VLAN into isolated ports that cannot communicate with each other, useful in hosting environments for customer isolation.

Tag: Normal

---

### Question 427
Domain: Computer Networks
Topic: Network Protocols
Subtopic: QinQ
Difficulty: Hard

Question: What does QinQ (802.1ad) provide?
A) Quality of Service
B) VLAN stacking (double tagging)
C) Faster switching
D) Encryption

✔ Correct Answer: B

Reason: QinQ allows VLAN tag stacking (double tagging) for service providers to tunnel customer VLANs through their network while maintaining separation.

Tag: Normal

---

### Question 428
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Ethernet Flow Control
Difficulty: Medium

Question: What mechanism does Ethernet use for flow control?
A) Sliding window
B) PAUSE frames (802.3x)
C) ACK packets
D) ICMP messages

✔ Correct Answer: B

Reason: Ethernet flow control uses PAUSE frames (IEEE 802.3x) to temporarily stop transmission when receiver buffer is full, preventing packet loss.

Tag: Normal

---

### Question 429
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PFC
Difficulty: Hard

Question: What does PFC (Priority Flow Control) improve over standard flow control?
A) Faster control
B) Per-priority class flow control
C) Better encryption
D) Lower latency

✔ Correct Answer: B

Reason: PFC (802.1Qbb) provides flow control on a per-priority basis, allowing pause of specific traffic classes without stopping all traffic.

Tag: Normal

---

### Question 430
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ETS
Difficulty: Hard

Question: What does ETS (Enhanced Transmission Selection) do?
A) Encrypts transmissions
B) Allocates bandwidth to different traffic classes
C) Selects fastest route
D) Compresses data

✔ Correct Answer: B

Reason: ETS (802.1Qaz) allocates bandwidth among different traffic classes, ensuring each class gets its guaranteed bandwidth share.

Tag: Normal

---

### Question 431
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DCB
Difficulty: Hard

Question: What is DCB (Data Center Bridging)?
A) Database connection
B) Set of enhancements for lossless Ethernet
C) Routing protocol
D) Security protocol

✔ Correct Answer: B

Reason: DCB is a set of IEEE standards (including PFC, ETS) that enhance Ethernet for data center use, providing lossless transport for storage traffic.

Tag: Normal

---

### Question 432
Domain: Computer Networks
Topic: Network Protocols
Subtopic: FCoE Requirements
Difficulty: Hard

Question: Why does FCoE require lossless Ethernet?
A) For speed
B) Fibre Channel expects no packet loss
C) For security
D) For simplicity

✔ Correct Answer: B

Reason: Fibre Channel protocol expects lossless transport. FCoE requires DCB features like PFC to provide lossless Ethernet for storage traffic.

Tag: Normal

---

### Question 433
Domain: Computer Networks
Topic: Network Protocols
Subtopic: iWARP
Difficulty: Hard

Question: What does iWARP provide?
A) Wireless access
B) RDMA over TCP/IP
C) Faster routing
D) Better encryption

✔ Correct Answer: B

Reason: iWARP provides RDMA (Remote Direct Memory Access) over TCP/IP, allowing direct memory access between computers without CPU involvement.

Tag: Normal

---

### Question 434
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RoCE
Difficulty: Hard

Question: What does RoCE stand for?
A) Router over Converged Ethernet
B) RDMA over Converged Ethernet
C) Routing over Cloud Ethernet
D) Remote over Centralized Ethernet

✔ Correct Answer: B

Reason: RoCE (RDMA over Converged Ethernet) provides RDMA over Ethernet, requiring lossless Ethernet (DCB) for reliable operation.

Tag: Normal

---

### Question 435
Domain: Computer Networks
Topic: Network Protocols
Subtopic: InfiniBand
Difficulty: Hard

Question: What is InfiniBand primarily used for?
A) Internet access
B) High-performance computing interconnects
C) Wireless communication
D) Email services

✔ Correct Answer: B

Reason: InfiniBand is a high-speed interconnect technology used in HPC clusters and data centers, providing very low latency and high bandwidth.

Tag: Normal

---

### Question 436
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Collapsed Core
Difficulty: Medium

Question: What is a collapsed core design?
A) Failed core layer
B) Combining core and distribution layers
C) Removing core layer entirely
D) Backup core design

✔ Correct Answer: B

Reason: Collapsed core combines core and distribution layers into a single layer, suitable for smaller networks where separate layers aren't needed.

Tag: Normal

---

### Question 437
Domain: Computer Networks
Topic: Network Design
Subtopic: Redundancy
Difficulty: Medium

Question: What is the purpose of redundant links in network design?
A) Increase speed only
B) Provide fault tolerance and high availability
C) Reduce costs
D) Simplify management

✔ Correct Answer: B

Reason: Redundant links provide alternative paths if primary links fail, ensuring network availability and fault tolerance, though requiring loop prevention mechanisms.

Tag: Normal

---

### Question 438
Domain: Computer Networks
Topic: Network Protocols
Subtopic: First Hop Redundancy
Difficulty: Medium

Question: What do HSRP, VRRP, and GLBP provide?
A) Routing between networks
B) Default gateway redundancy
C) VLAN management
D) Encryption

✔ Correct Answer: B

Reason: These First Hop Redundancy Protocols (FHRP) provide redundant default gateways, ensuring hosts can reach other networks even if one router fails.

Tag: Normal

---

### Question 439
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Gratuitous ARP Use Case
Difficulty: Hard

Question: When is gratuitous ARP commonly used?
A) Normal communication
B) During HSRP/VRRP failover to update MAC tables
C) For encryption
D) For compression

✔ Correct Answer: B

Reason: During FHRP failover, the new active router sends gratuitous ARP to update switches' MAC address tables, redirecting traffic to the new active router.

Tag: Normal

---

### Question 440
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Timestamp
Difficulty: Hard

Question: What does the TCP timestamp option enable?
A) Synchronize clocks
B) Better RTT measurement and PAWS
C) Encrypt timestamps
D) Compress headers

✔ Correct Answer: B

Reason: TCP timestamps enable more accurate RTT measurements and PAWS (Protection Against Wrapped Sequences) for high-speed networks.

Tag: Normal

---

### Question 441
Domain: Computer Networks
Topic: Network Performance
Subtopic: PAWS
Difficulty: Hard

Question: What problem does PAWS (Protection Against Wrapped Sequences) solve?
A) Packet loss
B) Sequence number wraparound in high-speed networks
C) Encryption issues
D) Routing loops

✔ Correct Answer: B

Reason: PAWS uses timestamps to detect old duplicate segments that might arrive after sequence numbers wrap around in high-bandwidth networks.

Tag: Normal

---

### Question 442
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ECN Bits
Difficulty: Hard

Question: How many bits are used for ECN in the IP header?
A) 1
B) 2
C) 4
D) 8

✔ Correct Answer: B

Reason: ECN uses 2 bits in the IP header (formerly part of ToS field) to signal congestion: ECT (ECN-Capable Transport) and CE (Congestion Experienced).

Tag: Normal

---

### Question 443
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DSCP
Difficulty: Hard

Question: How many bits does DSCP use in the IP header?
A) 3
B) 6
C) 8
D) 16

✔ Correct Answer: B

Reason: DSCP (Differentiated Services Code Point) uses 6 bits in the IP header for traffic classification, allowing 64 different traffic classes.

Tag: Normal

---

### Question 444
Domain: Computer Networks
Topic: Network QoS
Subtopic: CoS
Difficulty: Medium

Question: At which layer does CoS (Class of Service) operate?
A) Network Layer
B) Data Link Layer (Layer 2)
C) Transport Layer
D) Application Layer

✔ Correct Answer: B

Reason: CoS uses 3 bits in the 802.1Q VLAN tag (Layer 2) for QoS marking, while DSCP operates at Layer 3 in the IP header.

Tag: Normal

---

### Question 445
Domain: Computer Networks
Topic: Network QoS
Subtopic: Priority Queuing
Difficulty: Medium

Question: What is a disadvantage of strict priority queuing?
A) Too complex
B) Lower priority traffic can be starved
C) Too slow
D) Requires expensive hardware

✔ Correct Answer: B

Reason: Strict priority queuing always serves higher priority queues first, potentially starving lower priority traffic if high priority traffic is continuous.

Tag: Normal

---

### Question 446
Domain: Computer Networks
Topic: Network QoS
Subtopic: WFQ
Difficulty: Hard

Question: What does WFQ (Weighted Fair Queuing) provide?
A) Equal bandwidth to all flows
B) Bandwidth allocation proportional to weights
C) Priority to largest packets
D) Random packet selection

✔ Correct Answer: B

Reason: WFQ allocates bandwidth proportionally based on assigned weights, ensuring fair distribution while allowing prioritization of important traffic.

Tag: Normal

---

### Question 447
Domain: Computer Networks
Topic: Network QoS
Subtopic: CBWFQ
Difficulty: Hard

Question: What does CBWFQ add to WFQ?
A) Encryption
B) User-defined traffic classes with guaranteed bandwidth
C) Faster queuing
D) Compression

✔ Correct Answer: B

Reason: CBWFQ (Class-Based WFQ) allows administrators to define traffic classes and guarantee minimum bandwidth for each class, providing more control than WFQ.

Tag: Normal

---

### Question 448
Domain: Computer Networks
Topic: Network QoS
Subtopic: LLQ
Difficulty: Hard

Question: What does LLQ (Low Latency Queuing) combine?
A) WFQ and encryption
B) CBWFQ with strict priority queue
C) Two priority queues
D) WFQ and compression

✔ Correct Answer: B

Reason: LLQ combines CBWFQ with a strict priority queue for delay-sensitive traffic like VoIP, providing both guaranteed bandwidth and low latency.

Tag: Normal

---

### Question 449
Domain: Computer Networks
Topic: Network Protocols
Subtopic: WRED
Difficulty: Hard

Question: What does WRED (Weighted Random Early Detection) do?
A) Encrypts packets
B) Drops packets based on traffic class before buffer fills
C) Routes packets
D) Compresses packets

✔ Correct Answer: B

Reason: WRED proactively drops packets based on traffic class and queue depth before buffers fill, preventing tail drop and TCP global synchronization.

Tag: Normal

---

### Question 450
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Policing vs Shaping
Difficulty: Hard

Question: What happens to excess traffic in policing?
A) Buffered for later
B) Dropped or marked
C) Encrypted
D) Compressed

✔ Correct Answer: B

Reason: Policing drops or marks (remarking DSCP) packets exceeding the rate limit immediately, while shaping buffers them for later transmission.

Tag: Normal

---

### Question 451
Domain: Computer Networks
Topic: Network Performance
Subtopic: Token Bucket
Difficulty: Hard

Question: What does the token bucket algorithm control?
A) Token Ring networks
B) Traffic rate and burst size
C) Encryption keys
D) MAC addresses

✔ Correct Answer: B

Reason: Token bucket algorithm controls traffic rate by generating tokens at a fixed rate. Packets need tokens to be transmitted, controlling both average rate and burst size.

Tag: Normal

---

### Question 452
Domain: Computer Networks
Topic: Network Performance
Subtopic: Leaky Bucket
Difficulty: Hard

Question: How does leaky bucket differ from token bucket?
A) Leaky bucket is faster
B) Leaky bucket smooths traffic, token bucket allows bursts
C) Leaky bucket is more secure
D) They are identical

✔ Correct Answer: B

Reason: Leaky bucket outputs packets at a constant rate regardless of input rate (smoothing), while token bucket allows bursts up to bucket size.

Tag: Normal

---

### Question 453
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MPLS Labels
Difficulty: Hard

Question: How many bits is an MPLS label?
A) 8
B) 16
C) 20
D) 32

✔ Correct Answer: C

Reason: An MPLS label is 20 bits, part of a 32-bit label stack entry that also includes 3-bit EXP field, 1-bit bottom-of-stack, and 8-bit TTL.

Tag: Normal

---

### Question 454
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MPLS VPN
Difficulty: Hard

Question: What type of VPN does MPLS commonly provide?
A) Remote access VPN
B) Layer 3 VPN (MPLS L3VPN)
C) SSL VPN
D) PPTP VPN

✔ Correct Answer: B

Reason: MPLS L3VPN provides Layer 3 connectivity between customer sites, using VRF (Virtual Routing and Forwarding) to isolate customer routing tables.

Tag: Normal

---

### Question 455
Domain: Computer Networks
Topic: Network Protocols
Subtopic: VRF
Difficulty: Hard

Question: What does VRF (Virtual Routing and Forwarding) enable?
A) Faster routing
B) Multiple routing tables on single router
C) Encryption
D) Compression

✔ Correct Answer: B

Reason: VRF creates multiple virtual routers on a single physical router, each with its own routing table, enabling customer isolation in MPLS VPNs.

Tag: Normal

---

### Question 456
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MPLS TE
Difficulty: Hard

Question: What does MPLS Traffic Engineering enable?
A) Faster routing
B) Explicit path control and bandwidth reservation
C) Better encryption
D) Automatic failover only

✔ Correct Answer: B

Reason: MPLS TE allows explicit path selection and bandwidth reservation, optimizing network utilization and avoiding congested links.

Tag: Normal

---

### Question 457
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LDP
Difficulty: Hard

Question: What is LDP used for in MPLS?
A) Routing packets
B) Distributing label bindings
C) Encrypting labels
D) Compressing labels

✔ Correct Answer: B

Reason: LDP (Label Distribution Protocol) distributes label binding information between MPLS routers, establishing label-switched paths.

Tag: Normal

---

### Question 458
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RSVP-TE
Difficulty: Hard

Question: How does RSVP-TE differ from standard RSVP?
A) Faster
B) Adds traffic engineering extensions for MPLS
C) More secure
D) Simpler

✔ Correct Answer: B

Reason: RSVP-TE extends RSVP with traffic engineering capabilities for MPLS, enabling explicit path setup and bandwidth reservation.

Tag: Normal

---

### Question 459
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Segment Routing
Difficulty: Hard

Question: What is segment routing?
A) Traditional routing
B) Source-based routing using segment list
C) Multicast routing
D) Broadcast routing

✔ Correct Answer: B

Reason: Segment routing allows source nodes to specify the path through a list of segments (instructions), simplifying traffic engineering without per-flow state.

Tag: Normal

---

### Question 460
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SR-MPLS
Difficulty: Hard

Question: What does SR-MPLS use for segment identification?
A) IP addresses
B) MPLS labels
C) MAC addresses
D) Port numbers

✔ Correct Answer: B

Reason: SR-MPLS (Segment Routing with MPLS data plane) uses MPLS labels to represent segments, providing traffic engineering without complex signaling protocols.

Tag: Normal

---

### Question 461
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SRv6
Difficulty: Hard

Question: What does SRv6 use for segment identification?
A) MPLS labels
B) IPv6 addresses
C) MAC addresses
D) VLAN tags

✔ Correct Answer: B

Reason: SRv6 (Segment Routing over IPv6) uses IPv6 addresses to represent segments, encoding the segment list in the IPv6 extension header.

Tag: Normal

---

### Question 462
Domain: Computer Networks
Topic: Network Architecture
Subtopic: EVPN
Difficulty: Hard

Question: What does EVPN (Ethernet VPN) provide?
A) Email VPN
B) Layer 2 VPN services over MPLS or VXLAN
C) Web VPN
D) File transfer VPN

✔ Correct Answer: B

Reason: EVPN is a control plane technology for Layer 2 VPN services, using BGP to distribute MAC addresses and provide advanced features over MPLS or VXLAN.

Tag: Normal

---

### Question 463
Domain: Computer Networks
Topic: Network Architecture
Subtopic: VXLAN Overlay
Difficulty: Hard

Question: What is the VXLAN Network Identifier (VNI) size?
A) 12 bits
B) 16 bits
C) 24 bits
D) 32 bits

✔ Correct Answer: C

Reason: VNI is 24 bits, allowing up to 16 million virtual networks compared to VLAN's 12-bit limit of 4096 networks.

Tag: Normal

---

### Question 464
Domain: Computer Networks
Topic: Network Architecture
Subtopic: VTEP
Difficulty: Hard

Question: What does VTEP stand for in VXLAN?
A) Virtual Tunnel End Point
B) VLAN Tunnel Encryption Point
C) Virtual Transport Endpoint
D: VXLAN Tunnel Encryption Protocol

D) [Missing option - Please review]

✔ Correct Answer: A

Reason: VTEP (VXLAN Tunnel End Point) encapsulates and decapsulates VXLAN packets, acting as the entry and exit points for VXLAN tunnels.

Tag: Normal

---

### Question 465
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Underlay vs Overlay
Difficulty: Medium

Question: In network virtualization, what is the underlay network?
A) Virtual network
B) Physical network infrastructure
C) Application layer
D) Backup network

✔ Correct Answer: B

Reason: The underlay is the physical network infrastructure that carries overlay traffic. The overlay is the virtual network built on top.

Tag: Normal

---

### Question 466
Domain: Computer Networks
Topic: Network Protocols
Subtopic: GRE Tunnel
Difficulty: Hard

Question: What is a limitation of GRE tunnels?
A) Cannot tunnel multiple protocols
B) No encryption by default
C) Too slow
D) Limited distance

✔ Correct Answer: B

Reason: GRE provides tunneling but no encryption. For secure tunnels, GRE must be combined with IPSec (GRE over IPSec).

Tag: Normal

---

### Question 467
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DMVPN
Difficulty: Hard

Question: What does DMVPN provide?
A) Static VPN only
B) Dynamic mesh VPN with spoke-to-spoke tunnels
C) Encryption only
D) Routing only

✔ Correct Answer: B

Reason: DMVPN (Dynamic Multipoint VPN) creates dynamic IPSec tunnels between sites, allowing direct spoke-to-spoke communication without going through hub.

Tag: Normal

---

### Question 468
Domain: Computer Networks
Topic: Network Protocols
Subtopic: NHRP
Difficulty: Hard

Question: What protocol does DMVPN use for dynamic tunnel creation?
A) OSPF
B) NHRP (Next Hop Resolution Protocol)
C) BGP
D) RIP

✔ Correct Answer: B

Reason: DMVPN uses NHRP to dynamically discover the NBMA (Non-Broadcast Multiple Access) address of destination spokes, enabling direct tunnels.

Tag: Normal

---

### Question 469
Domain: Computer Networks
Topic: Network Architecture
Subtopic: SD-WAN
Difficulty: Hard

Question: What is a key benefit of SD-WAN?
A) Cheaper hardware only
B) Application-aware routing across multiple WAN links
C) Faster speeds only
D) Simpler cabling

✔ Correct Answer: B

Reason: SD-WAN provides intelligent, application-aware routing across multiple WAN connections (MPLS, Internet, LTE), optimizing performance and costs.

Tag: Normal

---

### Question 470
Domain: Computer Networks
Topic: Network Architecture
Subtopic: SD-WAN Features
Difficulty: Medium

Question: Which feature is commonly provided by SD-WAN?
A) Only encryption
B) Dynamic path selection based on application and link quality
C) Only cost reduction
D) Physical cable management

✔ Correct Answer: B

Reason: SD-WAN dynamically selects paths based on application requirements, link quality, and policies, providing better performance than traditional static routing.

Tag: Normal

---

### Question 471
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BFD
Difficulty: Hard

Question: What is BFD (Bidirectional Forwarding Detection) used for?
A) Encrypt bidirectional traffic
B) Fast failure detection between routers
C) Load balancing
D) Bandwidth measurement

✔ Correct Answer: B

Reason: BFD provides fast (sub-second) failure detection between adjacent routers, much faster than routing protocol hello mechanisms.

Tag: Normal

---

### Question 472
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BFD Benefits
Difficulty: Hard

Question: Why is BFD faster than routing protocol hellos?
A) Uses faster links
B) Lightweight protocol with frequent hellos
C) Uses hardware acceleration
D) Skips authentication

✔ Correct Answer: B

Reason: BFD is a lightweight protocol designed specifically for fast failure detection, sending frequent hellos (milliseconds) without the overhead of routing protocols.

Tag: Normal

---

### Question 473
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PBR Use Cases
Difficulty: Medium

Question: Which scenario is appropriate for policy-based routing?
A) All routing decisions
B) Route traffic based on source network or application
C) Only default routing
D) Multicast routing only

✔ Correct Answer: B

Reason: PBR is useful for routing based on source, application, or other criteria, such as directing guest traffic to Internet while employee traffic uses VPN.

Tag: Normal

---

### Question 474
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Route Maps
Difficulty: Hard

Question: What are route maps used for?
A) Display network topology
B) Complex routing policy and redistribution control
C) Encrypt routes
D) Compress routing tables

✔ Correct Answer: B

Reason: Route maps are powerful tools for implementing complex routing policies, controlling route redistribution, and manipulating routing attributes.

Tag: Normal

---

### Question 475
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Prefix Lists
Difficulty: Hard

Question: What are prefix lists used for?
A) List all prefixes
B) Filter routes based on network prefix
C) Encrypt prefixes
D) Compress prefixes

✔ Correct Answer: B

Reason: Prefix lists filter routing updates based on network prefixes and prefix lengths, more flexible and efficient than access lists for route filtering.

Tag: Normal

---

### Question 476
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Route Filtering
Difficulty: Medium

Question: Why would you filter routing updates?
A) Increase speed
B) Control routing information and prevent unwanted routes
C) Encrypt routes
D) Compress updates

✔ Correct Answer: B

Reason: Route filtering controls which routes are advertised or accepted, implementing routing policies, preventing routing loops, and optimizing routing tables.

Tag: Normal

---

### Question 477
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Route Summarization
Difficulty: Hard

Question: What is the benefit of route summarization?
A) More detailed routing
B) Smaller routing tables and reduced update traffic
C) Slower convergence
D) More complex configuration

✔ Correct Answer: B

Reason: Route summarization (aggregation) combines multiple routes into a single summary route, reducing routing table size, update traffic, and improving scalability.

Tag: Past Paper

---

### Question 478
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Default Route
Difficulty: Easy

Question: What does a default route (0.0.0.0/0) represent?
A) Local network only
B) Route for all destinations not in routing table
C) Loopback address
D) Broadcast address

✔ Correct Answer: B

Reason: A default route matches all destinations (0.0.0.0/0) and is used when no more specific route exists, typically pointing to the Internet gateway.

Tag: Normal

---

### Question 479
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Floating Static Route
Difficulty: Hard

Question: What is a floating static route?
A) Dynamic route
B) Backup static route with higher administrative distance
C) Fastest route
D) Encrypted route

✔ Correct Answer: B

Reason: A floating static route has higher AD than the primary route, remaining inactive until the primary route fails, providing backup connectivity.

Tag: Normal

---

### Question 480
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Null Route
Difficulty: Hard

Question: What is the purpose of a null route (route to null0)?
A) Backup route
B) Discard packets matching the route
C) Fastest route
D) Encrypted route

✔ Correct Answer: B

Reason: A null route (blackhole route) discards packets matching the route, useful for preventing routing loops or blocking unwanted traffic.

Tag: Normal

---

### Question 481
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Network Types
Difficulty: Hard

Question: What is the default OSPF network type for Ethernet interfaces?
A) Point-to-point
B) Broadcast
C) Non-broadcast
D) Point-to-multipoint

✔ Correct Answer: B

Reason: Ethernet interfaces default to broadcast network type in OSPF, electing DR/BDR. Point-to-point links don't need DR/BDR election.

Tag: Normal

---

### Question 482
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF DR/BDR
Difficulty: Hard

Question: Why are DR and BDR elected in OSPF broadcast networks?
A) Increase speed
B) Reduce LSA flooding and adjacencies
C) Provide encryption
D) Enable multicast

✔ Correct Answer: B

Reason: DR (Designated Router) and BDR (Backup DR) reduce the number of adjacencies and LSA flooding in broadcast networks, improving scalability.

Tag: Past Paper

---

### Question 483
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Priority
Difficulty: Medium

Question: What OSPF priority value prevents a router from becoming DR/BDR?
A) 0
B) 1
C) 255
D) -1

✔ Correct Answer: A

Reason: Setting OSPF priority to 0 prevents a router from participating in DR/BDR election, useful for routers that shouldn't take these roles.

Tag: Normal

---

### Question 484
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF LSA Types
Difficulty: Hard

Question: Which OSPF LSA type describes router links within an area?
A) Type 1 (Router LSA)
B) Type 2 (Network LSA)
C) Type 3 (Summary LSA)
D) Type 5 (External LSA)

✔ Correct Answer: A

Reason: Type 1 Router LSA describes a router's links within an area. Type 2 is from DR, Type 3 is inter-area routes, Type 5 is external routes.

Tag: Normal

---

### Question 485
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Stub Area
Difficulty: Hard

Question: What routes are NOT allowed in an OSPF stub area?
A) Intra-area routes
B) Type 5 external LSAs
C) Inter-area routes
D) Default routes

✔ Correct Answer: B

Reason: Stub areas don't accept Type 5 external LSAs, reducing routing table size. ABR injects a default route for external destinations.

Tag: Normal

---

### Question 486
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Totally Stubby Area
Difficulty: Hard

Question: What routes does a totally stubby area accept?
A) All routes
B) Only intra-area routes and default route
C) Only external routes
D) No routes

✔ Correct Answer: B

Reason: Totally stubby areas accept only intra-area routes and a default route from ABR, blocking both external (Type 5) and inter-area (Type 3) LSAs.

Tag: Normal

---

### Question 487
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF NSSA
Difficulty: Hard

Question: What does NSSA (Not-So-Stubby Area) allow that stub areas don't?
A) All external routes
B) Type 7 LSAs for limited external routes
C) Inter-area routes
D) Multicast routes

✔ Correct Answer: B

Reason: NSSA allows importing external routes as Type 7 LSAs (converted to Type 5 by ABR), useful when the area needs to redistribute some external routes.

Tag: Normal

---

### Question 488
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Virtual Link
Difficulty: Hard

Question: When is an OSPF virtual link needed?
A) Always
B) When an area cannot physically connect to Area 0
C) For faster routing
D) For encryption

✔ Correct Answer: B

Reason: Virtual links provide logical connectivity to Area 0 through a transit area when physical connection isn't possible, maintaining OSPF's backbone requirement.

Tag: Normal

---

### Question 489
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Metrics
Difficulty: Hard

Question: Which metrics does EIGRP use by default?
A) Hop count only
B) Bandwidth and delay
C) All five metrics
D) Cost only

✔ Correct Answer: B

Reason: EIGRP can use five metrics (bandwidth, delay, load, reliability, MTU) but by default uses only bandwidth and delay for metric calculation.

Tag: Normal

---

### Question 490
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP DUAL
Difficulty: Hard

Question: What does DUAL algorithm in EIGRP provide?
A) Encryption
B) Loop-free paths and fast convergence
C) Load balancing only
D) Compression

✔ Correct Answer: B

Reason: DUAL (Diffusing Update Algorithm) ensures loop-free paths at every instant and provides fast convergence using feasible successors.

Tag: Normal

---

### Question 491
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Feasible Successor
Difficulty: Hard

Question: What is a feasible successor in EIGRP?
A) Primary route
B) Backup route that meets feasibility condition
C) Failed route
D) Slowest route

✔ Correct Answer: B

Reason: A feasible successor is a backup route whose reported distance is less than the successor's feasible distance, guaranteed to be loop-free.

Tag: Normal

---

### Question 492
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Stuck in Active
Difficulty: Hard

Question: What causes "Stuck in Active" (SIA) in EIGRP?
A) Too much traffic
B) Query not replied within timeout
C) Encryption failure
D) Bandwidth limitation

✔ Correct Answer: B

Reason: SIA occurs when a router doesn't receive replies to its queries within the active timer (3 minutes default), potentially causing neighbor relationships to reset.

Tag: Normal

---

### Question 493
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Stub
Difficulty: Hard

Question: What is the purpose of EIGRP stub configuration?
A) Reduce router capabilities
B) Prevent queries to stub routers and improve stability
C) Disable EIGRP
D) Encrypt EIGRP updates

✔ Correct Answer: B

Reason: EIGRP stub routers don't receive queries, reducing query scope and preventing SIA conditions, useful for spoke routers in hub-and-spoke topologies.

Tag: Normal

---

### Question 494
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP Authentication
Difficulty: Medium

Question: Which authentication method does EIGRP support?
A) Plaintext only
B) MD5 and SHA
C) No authentication
D) Certificate-based only

✔ Correct Answer: B

Reason: EIGRP supports MD5 authentication (classic EIGRP) and SHA authentication (named mode EIGRP), preventing unauthorized routers from joining.

Tag: Normal

---

### Question 495
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Authentication
Difficulty: Medium

Question: Which authentication types does OSPF support?
A) None only
B) Plaintext, MD5, and SHA (OSPFv3)
C) Certificate only
D) Kerberos only

✔ Correct Answer: B

Reason: OSPF supports null (none), plaintext, and MD5 authentication. OSPFv3 adds IPSec and SHA support for stronger security.

Tag: Normal

---

### Question 496
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RIP Timers
Difficulty: Medium

Question: What is the default update timer for RIP?
A) 10 seconds
B) 30 seconds
C) 60 seconds
D) 90 seconds

✔ Correct Answer: B

Reason: RIP sends routing updates every 30 seconds by default. Invalid timer is 180 seconds, holddown is 180 seconds, flush is 240 seconds.

Tag: Normal

---

### Question 497
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RIP Hop Count
Difficulty: Easy

Question: What is the maximum hop count in RIP?
A) 10
B) 15
C) 20
D) 255

✔ Correct Answer: B

Reason: RIP has a maximum hop count of 15. A hop count of 16 is considered infinite (unreachable), limiting RIP to small networks.

Tag: Past Paper

---

### Question 498
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Split Horizon
Difficulty: Hard

Question: What does split horizon prevent in distance vector routing?
A) Fast convergence
B) Routing loops by not advertising routes back to source
C) Load balancing
D) Authentication

✔ Correct Answer: B

Reason: Split horizon prevents routing loops by not advertising routes back through the interface they were learned from, avoiding count-to-infinity problem.

Tag: Normal

---

### Question 499
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Route Poisoning
Difficulty: Hard

Question: What is route poisoning in distance vector protocols?
A) Deleting routes
B) Setting metric to infinity for failed routes
C) Encrypting routes
D) Compressing routes

✔ Correct Answer: B

Reason: Route poisoning sets a failed route's metric to infinity (16 in RIP) and advertises it, quickly informing neighbors of the failure.

Tag: Normal

---

### Question 500
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Poison Reverse
Difficulty: Hard

Question: How does poison reverse enhance split horizon?
A) It doesn't
B) Explicitly advertises poisoned routes back to source
C) Blocks all routes
D) Encrypts routes

✔ Correct Answer: B

Reason: Poison reverse explicitly advertises failed routes with infinite metric back to the source, overriding split horizon to speed up convergence.

Tag: Normal

---

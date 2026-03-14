# Computer Networks - MCQ Batch 04
## Questions 301-400

---

### Question 301
Domain: Computer Networks
Topic: Network Protocols
Subtopic: STUN
Difficulty: Hard

Question: What is STUN used for?
A) Encryption
B) NAT traversal for real-time communication
C) Routing
D) Load balancing

✔ Correct Answer: B

Reason: STUN (Session Traversal Utilities for NAT) helps clients discover their public IP address and port when behind NAT, enabling peer-to-peer communication.

Tag: Normal

---

### Question 302
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TURN
Difficulty: Hard

Question: When is TURN used instead of STUN?
A) Always
B) When direct peer-to-peer connection fails
C) For faster connections
D) For encryption

✔ Correct Answer: B

Reason: TURN (Traversal Using Relays around NAT) relays traffic when direct peer-to-peer connection is impossible due to restrictive NATs or firewalls.

Tag: Normal

---

### Question 303
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ICE
Difficulty: Hard

Question: What does ICE protocol do?
A) Encrypts data
B) Finds the best path for peer-to-peer connections
C) Cools network equipment
D) Compresses data

✔ Correct Answer: B

Reason: ICE (Interactive Connectivity Establishment) uses STUN and TURN to find the best path for peer-to-peer connections, trying direct, STUN, then TURN.

Tag: Normal

---

### Question 304
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Data Center
Difficulty: Medium

Question: What is a spine-leaf architecture in data centers?
A) Traditional hierarchical design
B) Two-tier architecture with full mesh between spine and leaf
C) Single-tier flat network
D) Ring topology

✔ Correct Answer: B

Reason: Spine-leaf is a two-tier architecture where every leaf switch connects to every spine switch, providing predictable latency and high bandwidth.

Tag: Normal

---

### Question 305
Domain: Computer Networks
Topic: Network Architecture
Subtopic: East-West Traffic
Difficulty: Medium

Question: What is east-west traffic in data centers?
A) Traffic between client and server
B) Traffic between servers within the data center
C) Traffic to the Internet
D) Backup traffic

✔ Correct Answer: B

Reason: East-west traffic flows between servers within the data center, increasingly dominant in modern applications with microservices and distributed architectures.

Tag: Normal

---

### Question 306
Domain: Computer Networks
Topic: Network Architecture
Subtopic: North-South Traffic
Difficulty: Easy

Question: North-south traffic refers to:
A) Traffic between servers
B) Traffic between data center and external clients
C) Internal backup traffic
D) Management traffic

✔ Correct Answer: B

Reason: North-south traffic flows between the data center and external clients/Internet, traditionally the dominant traffic pattern in client-server architectures.

Tag: Normal

---

### Question 307
Domain: Computer Networks
Topic: Network Protocols
Subtopic: VRRP vs HSRP
Difficulty: Hard

Question: What is a key difference between VRRP and HSRP?
A) VRRP is proprietary, HSRP is standard
B) VRRP is an open standard, HSRP is Cisco proprietary
C) VRRP is faster
D) VRRP works only on wireless

✔ Correct Answer: B

Reason: VRRP is an open standard (RFC 5798), while HSRP is Cisco proprietary. Both provide router redundancy but with different implementations.

Tag: Normal

---

### Question 308
Domain: Computer Networks
Topic: Network Performance
Subtopic: Packet Loss Recovery
Difficulty: Medium

Question: Which mechanism does TCP use to detect packet loss?
A) Parity check
B) Timeout and duplicate ACKs
C) CRC
D) Checksum only

✔ Correct Answer: B

Reason: TCP detects packet loss through retransmission timeout (RTO) when ACK doesn't arrive, or through three duplicate ACKs triggering fast retransmit.

Tag: Normal

---

### Question 309
Domain: Computer Networks
Topic: TCP Optimization
Subtopic: Nagle's Algorithm
Difficulty: Hard

Question: What is the purpose of Nagle's algorithm?
A) Faster routing
B) Reduce small packet overhead by buffering
C) Encrypt data
D) Detect errors

✔ Correct Answer: B

Reason: Nagle's algorithm reduces network congestion by buffering small packets and sending them together, reducing overhead from many tiny packets.

Tag: Normal

---

### Question 310
Domain: Computer Networks
Topic: TCP Optimization
Subtopic: Delayed ACK
Difficulty: Hard

Question: Why does TCP use delayed acknowledgments?
A) Increase security
B) Reduce number of ACK packets sent
C) Increase bandwidth
D) Detect errors better

✔ Correct Answer: B

Reason: Delayed ACK waits briefly before sending ACK, allowing it to piggyback on return data or acknowledge multiple segments with one ACK, reducing overhead.

Tag: Normal

---

### Question 311
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SACK
Difficulty: Hard

Question: What does SACK (Selective Acknowledgment) allow?
A) Acknowledge only lost packets
B) Acknowledge non-contiguous blocks of received data
C) Acknowledge all packets at once
D) Skip acknowledgments

✔ Correct Answer: B

Reason: SACK allows the receiver to acknowledge non-contiguous blocks of data, enabling the sender to retransmit only missing segments, improving efficiency.

Tag: Normal

---

### Question 312
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Window Scaling
Difficulty: Hard

Question: Why is TCP window scaling needed?
A) Reduce latency
B) Support window sizes larger than 64 KB
C) Improve security
D) Simplify configuration

✔ Correct Answer: B

Reason: The TCP window field is 16 bits (max 64 KB). Window scaling option allows larger windows needed for high bandwidth-delay product networks.

Tag: Normal

---

### Question 313
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Jumbo Frames
Difficulty: Medium

Question: What is a jumbo frame?
A) Standard 1500-byte frame
B) Ethernet frame larger than 1500 bytes
C) Compressed frame
D) Encrypted frame

✔ Correct Answer: B

Reason: Jumbo frames are Ethernet frames with payload larger than standard 1500 bytes (typically up to 9000 bytes), reducing overhead for large data transfers.

Tag: Normal

---

### Question 314
Domain: Computer Networks
Topic: Network Performance
Subtopic: Path MTU Discovery
Difficulty: Hard

Question: What is the purpose of Path MTU Discovery?
A) Find fastest route
B) Determine maximum packet size that can be sent without fragmentation
C) Discover all routers in path
D) Measure bandwidth

✔ Correct Answer: B

Reason: Path MTU Discovery determines the largest packet size that can traverse the path without fragmentation, optimizing performance and avoiding fragmentation overhead.

Tag: Normal

---

### Question 315
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PMTUD
Difficulty: Hard

Question: How does IPv4 PMTUD work?
A) Sends test packets of increasing size
B) Uses ICMP "Fragmentation Needed" messages
C) Queries each router
D) Uses DNS

✔ Correct Answer: B

Reason: IPv4 PMTUD sets the Don't Fragment bit and relies on ICMP "Fragmentation Needed" messages from routers to discover the path MTU.

Tag: Normal

---

### Question 316
Domain: Computer Networks
Topic: Network Security
Subtopic: IPSec Modes
Difficulty: Hard

Question: In IPSec transport mode, what is encrypted?
A) Entire IP packet
B) Only the payload
C) Only the header
D) Nothing

✔ Correct Answer: B

Reason: IPSec transport mode encrypts only the payload, leaving the original IP header intact. Tunnel mode encrypts the entire original packet.

Tag: Normal

---

### Question 317
Domain: Computer Networks
Topic: Network Security
Subtopic: IPSec Tunnel Mode
Difficulty: Hard

Question: What does IPSec tunnel mode do?
A) Encrypts only payload
B) Encrypts entire original packet and adds new IP header
C) Compresses data
D) Fragments packets

✔ Correct Answer: B

Reason: Tunnel mode encrypts the entire original IP packet and encapsulates it with a new IP header, commonly used for VPN connections.

Tag: Normal

---

### Question 318
Domain: Computer Networks
Topic: Network Security
Subtopic: IPSec Protocols
Difficulty: Hard

Question: Which IPSec protocol provides authentication but not encryption?
A) ESP
B) AH
C) IKE
D) L2TP

✔ Correct Answer: B

Reason: AH (Authentication Header) provides authentication and integrity but not encryption. ESP (Encapsulating Security Payload) provides both authentication and encryption.

Tag: Normal

---

### Question 319
Domain: Computer Networks
Topic: Network Security
Subtopic: IKE
Difficulty: Hard

Question: What is the role of IKE in IPSec?
A) Encrypt data
B) Establish and manage security associations
C) Route packets
D) Detect intrusions

✔ Correct Answer: B

Reason: IKE (Internet Key Exchange) negotiates and establishes IPSec security associations, managing keys and security parameters for secure communication.

Tag: Normal

---

### Question 320
Domain: Computer Networks
Topic: VPN Types
Subtopic: Site-to-Site
Difficulty: Medium

Question: What is a site-to-site VPN used for?
A) Individual remote access
B) Connecting entire networks securely
C) Web browsing only
D) Email access

✔ Correct Answer: B

Reason: Site-to-site VPN connects entire networks (like branch offices to headquarters), creating a secure tunnel between network gateways.

Tag: Normal

---

### Question 321
Domain: Computer Networks
Topic: VPN Types
Subtopic: Remote Access
Difficulty: Easy

Question: What is remote access VPN used for?
A) Connecting two offices
B) Individual users connecting to corporate network
C) Connecting servers
D) Backup purposes

✔ Correct Answer: B

Reason: Remote access VPN allows individual users to securely connect to a corporate network from remote locations over the Internet.

Tag: Normal

---

### Question 322
Domain: Computer Networks
Topic: Network Protocols
Subtopic: L2TP
Difficulty: Hard

Question: What does L2TP provide?
A) Encryption
B) Tunneling (no encryption by itself)
C) Routing
D) Load balancing

✔ Correct Answer: B

Reason: L2TP (Layer 2 Tunneling Protocol) provides tunneling but no encryption. It's typically combined with IPSec (L2TP/IPSec) for secure VPN connections.

Tag: Normal

---

### Question 323
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PPTP
Difficulty: Medium

Question: What is a major security weakness of PPTP?
A) Too slow
B) Weak encryption and known vulnerabilities
C) Too complex
D) Incompatible with most systems

✔ Correct Answer: B

Reason: PPTP (Point-to-Point Tunneling Protocol) has known security vulnerabilities and uses weak encryption (MS-CHAPv2), making it unsuitable for secure VPNs.

Tag: Normal

---

### Question 324
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OpenVPN
Difficulty: Medium

Question: Which library does OpenVPN use for encryption?
A) WinCrypt
B) OpenSSL
C) Java Crypto
D) .NET Crypto

✔ Correct Answer: B

Reason: OpenVPN uses the OpenSSL library for encryption, supporting various encryption algorithms and providing strong security for VPN connections.

Tag: Normal

---

### Question 325
Domain: Computer Networks
Topic: Network Protocols
Subtopic: WireGuard
Difficulty: Hard

Question: What is a key characteristic of WireGuard VPN?
A) Complex configuration
B) Simple, modern, and fast with minimal code
C) Proprietary protocol
D) Works only on Linux

✔ Correct Answer: B

Reason: WireGuard is a modern VPN protocol with minimal codebase, simple configuration, and high performance using state-of-the-art cryptography.

Tag: Normal

---

### Question 326
Domain: Computer Networks
Topic: Network Addressing
Subtopic: IPv6 Autoconfiguration
Difficulty: Medium

Question: What is SLAAC in IPv6?
A) Security protocol
B) Stateless Address Autoconfiguration
C) Routing protocol
D) Encryption method

✔ Correct Answer: B

Reason: SLAAC (Stateless Address Autoconfiguration) allows IPv6 hosts to automatically configure their addresses using router advertisements without a DHCP server.

Tag: Normal

---

### Question 327
Domain: Computer Networks
Topic: Network Addressing
Subtopic: EUI-64
Difficulty: Hard

Question: In IPv6 SLAAC, how is the interface identifier typically generated?
A) Random number
B) From MAC address using EUI-64 format
C) From IP address
D) Sequential numbering

✔ Correct Answer: B

Reason: EUI-64 format derives the 64-bit interface identifier from the 48-bit MAC address by inserting FFFE in the middle and flipping the 7th bit.

Tag: Normal

---

### Question 328
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DHCPv6
Difficulty: Medium

Question: How does DHCPv6 differ from DHCPv4?
A) Uses different port numbers
B) Can provide configuration without assigning addresses (stateless)
C) Faster
D) More secure

✔ Correct Answer: B

Reason: DHCPv6 can operate in stateless mode (providing configuration only) or stateful mode (assigning addresses), unlike DHCPv4 which always assigns addresses.

Tag: Normal

---

### Question 329
Domain: Computer Networks
Topic: Network Security
Subtopic: DNSSEC
Difficulty: Hard

Question: What does DNSSEC provide?
A) Faster DNS resolution
B) Authentication and integrity for DNS responses
C) DNS caching
D) Load balancing

✔ Correct Answer: B

Reason: DNSSEC (DNS Security Extensions) uses digital signatures to authenticate DNS responses, preventing DNS spoofing and cache poisoning attacks.

Tag: Normal

---

### Question 330
Domain: Computer Networks
Topic: Network Security
Subtopic: DNS over HTTPS
Difficulty: Medium

Question: What is the main benefit of DNS over HTTPS (DoH)?
A) Faster resolution
B) Encrypted DNS queries for privacy
C) Lower latency
D) Automatic caching

✔ Correct Answer: B

Reason: DoH encrypts DNS queries within HTTPS traffic, preventing eavesdropping and manipulation of DNS requests, improving privacy.

Tag: Normal

---

### Question 331
Domain: Computer Networks
Topic: Network Security
Subtopic: DNS over TLS
Difficulty: Medium

Question: Which port does DNS over TLS (DoT) use?
A) 53
B) 443
C) 853
D) 8853

✔ Correct Answer: C

Reason: DoT uses port 853 for encrypted DNS queries over TLS, while traditional DNS uses port 53 and DoH uses port 443 (HTTPS).

Tag: Normal

---

### Question 332
Domain: Computer Networks
Topic: Network Protocols
Subtopic: mDNS Port
Difficulty: Medium

Question: Which port does mDNS use?
A) 53
B) 5353
C) 5355
D) 8053

✔ Correct Answer: B

Reason: mDNS uses UDP port 5353 for multicast DNS queries on local networks, different from standard DNS port 53.

Tag: Normal

---

### Question 333
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LLMNR
Difficulty: Hard

Question: What is LLMNR used for in Windows networks?
A) File sharing
B: Local name resolution when DNS fails
B) [Missing option - Please review]

C) Printer discovery
D) User authentication

✔ Correct Answer: B

Reason: LLMNR (Link-Local Multicast Name Resolution) is a Windows protocol for name resolution on local networks when DNS is unavailable.

Tag: Normal

---

### Question 334
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Fast Open
Difficulty: Hard

Question: What does TCP Fast Open (TFO) optimize?
A) Data transfer speed
B) Connection establishment by sending data in SYN
C) Error detection
D) Congestion control

✔ Correct Answer: B

Reason: TFO allows data to be sent in the SYN packet during connection establishment, reducing latency by eliminating one round trip.

Tag: Normal

---

### Question 335
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Keepalive
Difficulty: Medium

Question: What is the purpose of TCP keepalive?
A) Maintain connection and detect dead peers
B) Increase speed
C) Encrypt data
D) Compress packets

✔ Correct Answer: A

Reason: TCP keepalive sends periodic probes to detect if the peer is still alive and maintain the connection, preventing timeout on idle connections.

Tag: Normal

---

### Question 336
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RTSP
Difficulty: Medium

Question: What is RTSP (Real Time Streaming Protocol) used for?
A) File transfer
B) Controlling streaming media servers
C) Email delivery
D) DNS resolution

✔ Correct Answer: B

Reason: RTSP is a network control protocol for controlling streaming media servers, providing VCR-like controls (play, pause, stop) for media streams.

Tag: Normal

---

### Question 337
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RTCP
Difficulty: Hard

Question: What is the relationship between RTP and RTCP?
A) They are the same
B) RTCP provides control and statistics for RTP sessions
C) RTCP replaces RTP
D) They are unrelated

✔ Correct Answer: B

Reason: RTCP (RTP Control Protocol) works with RTP to provide feedback on QoS, participant information, and session control for real-time streams.

Tag: Normal

---

### Question 338
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SDP
Difficulty: Hard

Question: What does SDP (Session Description Protocol) describe?
A) Routing paths
B) Multimedia session parameters
C) Security policies
D) Network topology

✔ Correct Answer: B

Reason: SDP describes multimedia session parameters like media types, formats, and transport addresses, used with protocols like SIP and RTSP.

Tag: Normal

---

### Question 339
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Service Mesh
Difficulty: Hard

Question: What is a service mesh in microservices architecture?
A) Physical network cables
B) Infrastructure layer handling service-to-service communication
C) Database cluster
D) Load balancer only

✔ Correct Answer: B

Reason: A service mesh is a dedicated infrastructure layer that handles service-to-service communication, providing features like load balancing, encryption, and observability.

Tag: Normal

---

### Question 340
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP Attributes
Difficulty: Hard

Question: Which BGP attribute is used to prevent routing loops?
A) Local Preference
B) AS_PATH
C) MED
D) Next Hop

✔ Correct Answer: B

Reason: AS_PATH lists all autonomous systems a route has traversed. BGP rejects routes containing its own AS number, preventing loops.

Tag: Normal

---

### Question 341
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP Types
Difficulty: Hard

Question: What is the difference between eBGP and iBGP?
A) eBGP is faster
B) eBGP runs between different AS, iBGP within same AS
C) eBGP is more secure
D) eBGP uses UDP

✔ Correct Answer: B

Reason: eBGP (External BGP) runs between different autonomous systems, while iBGP (Internal BGP) runs between routers within the same AS.

Tag: Normal

---

### Question 342
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Areas
Difficulty: Hard

Question: What is the purpose of OSPF areas?
A) Increase speed
B) Reduce routing table size and LSA flooding
C) Improve security
D) Enable wireless

✔ Correct Answer: B

Reason: OSPF areas create hierarchical routing domains, reducing routing table size and limiting LSA flooding, improving scalability in large networks.

Tag: Normal

---

### Question 343
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Backbone
Difficulty: Hard

Question: What is the area ID of the OSPF backbone area?
A) Area 0
B) Area 1
C) Area 255
D) Area 100

✔ Correct Answer: A

Reason: Area 0 (0.0.0.0) is the OSPF backbone area. All other areas must connect to the backbone, either directly or through virtual links.

Tag: Past Paper

---

### Question 344
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF Router Types
Difficulty: Hard

Question: What is an ABR in OSPF?
A) Autonomous Border Router
B) Area Border Router
C) Automatic Backup Router
D) Access Border Router

✔ Correct Answer: B

Reason: ABR (Area Border Router) connects multiple OSPF areas, maintaining separate link-state databases for each area and summarizing routes between areas.

Tag: Normal

---

### Question 345
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPF ASBR
Difficulty: Hard

Question: What does an ASBR do in OSPF?
A) Connects areas
B) Connects OSPF domain to external routing domains
C) Provides backup
D) Manages bandwidth

✔ Correct Answer: B

Reason: ASBR (Autonomous System Boundary Router) connects the OSPF routing domain to external routing domains, redistributing routes between different protocols.

Tag: Normal

---

### Question 346
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RIP Versions
Difficulty: Medium

Question: What improvement does RIPv2 have over RIPv1?
A) Unlimited hop count
B) Support for VLSM and authentication
C) Faster convergence
D) Uses link-state algorithm

✔ Correct Answer: B

Reason: RIPv2 added support for VLSM, CIDR, authentication, and multicast updates, while maintaining the 15-hop limit and distance vector algorithm.

Tag: Normal

---

### Question 347
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RIPng
Difficulty: Hard

Question: What is RIPng?
A) Next generation RIP for IPv4
B) RIP for IPv6
C) Faster version of RIP
D) Secure RIP

✔ Correct Answer: B

Reason: RIPng (RIP next generation) is the IPv6 version of RIP, using IPv6 for transport and supporting IPv6 routing.

Tag: Normal

---

### Question 348
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OSPFv3
Difficulty: Hard

Question: What is the main difference between OSPFv2 and OSPFv3?
A) OSPFv3 is faster
B) OSPFv3 supports IPv6
C) OSPFv3 has no areas
D) OSPFv3 uses distance vector

✔ Correct Answer: B

Reason: OSPFv3 is designed for IPv6 routing, though it can also support IPv4. It maintains OSPF's link-state algorithm and area concepts.

Tag: Normal

---

### Question 349
Domain: Computer Networks
Topic: Network Protocols
Subtopic: IS-IS
Difficulty: Hard

Question: At which layer does IS-IS operate?
A) Network Layer (IP)
B) Data Link Layer (directly over Layer 2)
C) Transport Layer
D) Application Layer

✔ Correct Answer: B

Reason: IS-IS (Intermediate System to Intermediate System) operates directly over Layer 2, making it protocol-independent and able to route both IP and other protocols.

Tag: Normal

---

### Question 350
Domain: Computer Networks
Topic: Multicast Routing
Subtopic: PIM Modes
Difficulty: Hard

Question: When is PIM Dense Mode appropriate?
A) Sparse receiver distribution
B) Dense receiver distribution with high bandwidth
C) Low bandwidth networks
D) Never recommended

✔ Correct Answer: B

Reason: PIM-DM is suitable when receivers are densely distributed and bandwidth is plentiful, as it floods traffic initially then prunes unnecessary branches.

Tag: Normal

---

### Question 351
Domain: Computer Networks
Topic: Multicast Routing
Subtopic: PIM-SM
Difficulty: Hard

Question: What does PIM Sparse Mode use for multicast distribution?
A) Flooding
B) Rendezvous Point (RP)
C) Broadcast
D) Unicast only

✔ Correct Answer: B

Reason: PIM-SM uses a Rendezvous Point where sources and receivers register, building distribution trees only where needed, efficient for sparse receiver distribution.

Tag: Normal

---

### Question 352
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MSDP
Difficulty: Hard

Question: What is MSDP used for?
A) Routing unicast traffic
B) Connecting multiple PIM-SM domains
C) DNS resolution
D) File transfer

✔ Correct Answer: B

Reason: MSDP (Multicast Source Discovery Protocol) allows multiple PIM-SM domains to share multicast source information, enabling inter-domain multicast.

Tag: Normal

---

### Question 353
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Slow Start
Difficulty: Hard

Question: What is the initial congestion window size in TCP slow start?
A) 1 MSS
B) 2 MSS
C) 4 MSS
D) 10 MSS

✔ Correct Answer: A

Reason: Traditionally, TCP slow start begins with cwnd = 1 MSS (Maximum Segment Size). Modern implementations may start with larger values (up to 10 MSS).

Tag: Normal

---

### Question 354
Domain: Computer Networks
Topic: TCP Congestion Control
Subtopic: Threshold
Difficulty: Hard

Question: What happens when TCP congestion window reaches the slow start threshold?
A) Connection closes
B) Switches from slow start to congestion avoidance
C) Resets to 1
D) Doubles faster

✔ Correct Answer: B

Reason: When cwnd reaches ssthresh, TCP switches from exponential growth (slow start) to linear growth (congestion avoidance) to prevent congestion.

Tag: Normal

---

### Question 355
Domain: Computer Networks
Topic: TCP Congestion Control
Subtopic: Fast Retransmit
Difficulty: Hard

Question: How many duplicate ACKs trigger TCP fast retransmit?
A) 1
B) 2
C) 3
D) 4

✔ Correct Answer: C

Reason: TCP fast retransmit is triggered by three duplicate ACKs, indicating packet loss without waiting for timeout, improving performance.

Tag: Past Paper

---

### Question 356
Domain: Computer Networks
Topic: TCP Congestion Control
Subtopic: Fast Recovery
Difficulty: Hard

Question: What does TCP fast recovery do after fast retransmit?
A) Reset cwnd to 1
B) Set cwnd to ssthresh and continue congestion avoidance
C) Close connection
D) Double cwnd

✔ Correct Answer: B

Reason: Fast recovery sets cwnd to ssthresh (instead of 1) after fast retransmit, avoiding slow start and maintaining higher throughput.

Tag: Normal

---

### Question 357
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ECMP
Difficulty: Hard

Question: What does ECMP (Equal-Cost Multi-Path) routing do?
A) Find single best path
B) Distribute traffic across multiple equal-cost paths
C) Encrypt routing updates
D) Compress routing tables

✔ Correct Answer: B

Reason: ECMP allows routers to distribute traffic across multiple paths with equal cost, improving bandwidth utilization and providing redundancy.

Tag: Normal

---

### Question 358
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Policy-Based Routing
Difficulty: Hard

Question: What does policy-based routing (PBR) allow?
A) Automatic routing only
B) Route packets based on criteria beyond destination address
C) Faster routing
D) Simpler configuration

✔ Correct Answer: B

Reason: PBR allows routing decisions based on source address, application, protocol, or other criteria, not just destination address, enabling flexible traffic engineering.

Tag: Normal

---

### Question 359
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Route Redistribution
Difficulty: Hard

Question: What is route redistribution?
A) Deleting routes
B) Sharing routes between different routing protocols
C) Backing up routes
D) Encrypting routes

✔ Correct Answer: B

Reason: Route redistribution allows routes learned by one routing protocol to be advertised into another protocol, enabling interoperability between different routing domains.

Tag: Normal

---

### Question 360
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Administrative Distance
Difficulty: Hard

Question: Which routing source has the lowest (most trusted) administrative distance?
A) RIP
B) OSPF
C) Directly connected
D) Static route

✔ Correct Answer: C

Reason: Directly connected interfaces have AD of 0 (most trusted), static routes have 1, EIGRP 90, OSPF 110, RIP 120. Lower AD is preferred.

Tag: Normal

---

### Question 361
Domain: Computer Networks
Topic: Network Security
Subtopic: ACL
Difficulty: Medium

Question: What is an Access Control List (ACL) used for?
A) Assign IP addresses
B) Filter traffic based on rules
C) Encrypt data
D) Compress packets

✔ Correct Answer: B

Reason: ACLs are sets of rules that filter network traffic based on criteria like source/destination IP, port, or protocol, controlling what traffic is allowed.

Tag: Past Paper

---

### Question 362
Domain: Computer Networks
Topic: Network Security
Subtopic: ACL Types
Difficulty: Hard

Question: What is the difference between standard and extended ACLs?
A) Standard is faster
B) Standard filters by source IP only, extended by multiple criteria
C) Standard is more secure
D) Extended is simpler

✔ Correct Answer: B

Reason: Standard ACLs filter based only on source IP address, while extended ACLs can filter by source/destination IP, protocol, port, and other criteria.

Tag: Normal

---

### Question 363
Domain: Computer Networks
Topic: Network Security
Subtopic: Stateful Firewall
Difficulty: Medium

Question: What does a stateful firewall track?
A) Only IP addresses
B) Connection state and context
C) Only port numbers
D) MAC addresses

✔ Correct Answer: B

Reason: Stateful firewalls track the state of connections, understanding the context of traffic and allowing return traffic for established connections automatically.

Tag: Normal

---

### Question 364
Domain: Computer Networks
Topic: Network Security
Subtopic: Stateless Firewall
Difficulty: Medium

Question: How does a stateless firewall make decisions?
A) Based on connection history
B) Based on individual packet headers only
C) Based on user identity
D) Based on time of day

✔ Correct Answer: B

Reason: Stateless firewalls examine each packet independently based on header information without tracking connection state, simpler but less intelligent than stateful.

Tag: Normal

---

### Question 365
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TACACS+
Difficulty: Hard

Question: How does TACACS+ differ from RADIUS?
A) TACACS+ is faster
B) TACACS+ separates AAA functions, RADIUS combines them
C) TACACS+ uses UDP
D) TACACS+ is open standard

✔ Correct Answer: B

Reason: TACACS+ separates Authentication, Authorization, and Accounting into distinct processes, while RADIUS combines authentication and authorization. TACACS+ uses TCP, RADIUS uses UDP.

Tag: Normal

---

### Question 366
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RADIUS vs TACACS+
Difficulty: Hard

Question: Which protocol does RADIUS use for transport?
A) TCP
B) UDP
C) SCTP
D) DCCP

✔ Correct Answer: B

Reason: RADIUS uses UDP (ports 1812 for authentication, 1813 for accounting), while TACACS+ uses TCP port 49 for more reliable communication.

Tag: Normal

---

### Question 367
Domain: Computer Networks
Topic: Network Management
Subtopic: NetFlow
Difficulty: Medium

Question: What information does NetFlow collect?
A) Only bandwidth usage
B) Traffic flow statistics and patterns
C) Only error rates
D) Only security events

✔ Correct Answer: B

Reason: NetFlow collects IP traffic flow information including source/destination, ports, protocols, and byte/packet counts, useful for monitoring and analysis.

Tag: Normal

---

### Question 368
Domain: Computer Networks
Topic: Network Management
Subtopic: sFlow
Difficulty: Hard

Question: How does sFlow differ from NetFlow?
A) sFlow is Cisco proprietary
B) sFlow uses packet sampling, NetFlow analyzes all flows
C) sFlow is slower
D) sFlow works only on wireless

✔ Correct Answer: B

Reason: sFlow uses statistical packet sampling for scalability, while NetFlow analyzes all flows. sFlow is also vendor-neutral and includes Layer 2 information.

Tag: Normal

---

### Question 369
Domain: Computer Networks
Topic: Network Management
Subtopic: IPFIX
Difficulty: Hard

Question: What is IPFIX?
A) IP security protocol
B) Standardized version of NetFlow
C) Routing protocol
D) Encryption method

✔ Correct Answer: B

Reason: IPFIX (IP Flow Information Export) is the IETF standard based on NetFlow v9, providing a standardized format for exporting flow information.

Tag: Normal

---

### Question 370
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LLDP-MED
Difficulty: Hard

Question: What does LLDP-MED add to standard LLDP?
A) Encryption
B) Extensions for VoIP and media endpoint devices
C) Faster discovery
D) Wireless support

✔ Correct Answer: B

Reason: LLDP-MED (Media Endpoint Discovery) extends LLDP with features for VoIP phones and media devices, including power, VLAN, and QoS configuration.

Tag: Normal

---

### Question 371
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PoE
Difficulty: Medium

Question: What does PoE (Power over Ethernet) provide?
A) Faster data transfer
B) Electrical power over Ethernet cables
C) Better security
D) Wireless connectivity

✔ Correct Answer: B

Reason: PoE delivers electrical power along with data over Ethernet cables, eliminating the need for separate power supplies for devices like IP phones and cameras.

Tag: Normal

---

### Question 372
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PoE Standards
Difficulty: Hard

Question: What is the maximum power delivery in IEEE 802.3af (PoE)?
A) 7.5 watts
B) 15.4 watts
C) 30 watts
D) 60 watts

✔ Correct Answer: B

Reason: 802.3af (PoE) provides up to 15.4W at the source. 802.3at (PoE+) provides 30W, and 802.3bt (PoE++) provides up to 60-100W.

Tag: Normal

---

### Question 373
Domain: Computer Networks
Topic: Network Design
Subtopic: Oversubscription
Difficulty: Hard

Question: What is oversubscription ratio in network design?
A) Number of users per switch
B) Ratio of downstream to upstream bandwidth
C) Error rate
D) Latency measurement

✔ Correct Answer: B

Reason: Oversubscription ratio compares total downstream bandwidth to upstream bandwidth. A 3:1 ratio means 3 Gbps downstream shares 1 Gbps upstream.

Tag: Normal

---

### Question 374
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BPDU
Difficulty: Hard

Question: What does BPDU stand for in STP?
A) Bridge Protocol Data Unit
B) Broadcast Protocol Data Unit
C) Border Protocol Data Unit
D) Backup Protocol Data Unit

✔ Correct Answer: A

Reason: BPDU (Bridge Protocol Data Unit) is a frame used by STP to exchange information between switches for detecting and preventing loops.

Tag: Normal

---

### Question 375
Domain: Computer Networks
Topic: Network Protocols
Subtopic: STP Port States
Difficulty: Hard

Question: How many port states does STP (802.1D) define?
A) 3
B) 4
C) 5
D) 6

✔ Correct Answer: C

Reason: STP defines 5 port states: Disabled, Blocking, Listening, Learning, and Forwarding. RSTP simplifies this to 3 states.

Tag: Normal

---

### Question 376
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Root Bridge
Difficulty: Hard

Question: In STP, how is the root bridge elected?
A) Random selection
B) Lowest bridge ID (priority + MAC address)
C) Highest IP address
D) First switch powered on

✔ Correct Answer: B

Reason: The switch with the lowest bridge ID becomes root bridge. Bridge ID combines priority (configurable) and MAC address.

Tag: Past Paper

---

### Question 377
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Port Roles
Difficulty: Hard

Question: In STP, what is a designated port?
A) Port connected to root bridge
B) Port with best path to root on a segment
C) Blocked port
D) Disabled port

✔ Correct Answer: B

Reason: The designated port is the port on a segment with the best path to the root bridge, responsible for forwarding traffic from that segment toward the root.

Tag: Normal

---

### Question 378
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BPDU Guard
Difficulty: Hard

Question: What does BPDU Guard do?
A) Encrypts BPDUs
B) Disables port if BPDU is received
C) Filters BPDUs
D) Compresses BPDUs

✔ Correct Answer: B

Reason: BPDU Guard is a security feature that disables a port if it receives a BPDU, protecting against unauthorized switches and STP manipulation.

Tag: Normal

---

### Question 379
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Root Guard
Difficulty: Hard

Question: What does Root Guard prevent?
A) Root bridge failure
B) Unauthorized switch from becoming root bridge
C) Port failures
D) VLAN conflicts

✔ Correct Answer: B

Reason: Root Guard prevents external switches from becoming the root bridge by blocking ports that receive superior BPDUs, maintaining intended network topology.

Tag: Normal

---

### Question 380
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Loop Guard
Difficulty: Hard

Question: What problem does Loop Guard address?
A) Routing loops
B) Unidirectional link failures causing loops
C) VLAN loops
D) IP conflicts

✔ Correct Answer: B

Reason: Loop Guard prevents loops caused by unidirectional link failures where BPDUs stop being received, moving ports to loop-inconsistent state instead of forwarding.

Tag: Normal

---

### Question 381
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PortFast
Difficulty: Medium

Question: What does PortFast do in STP?
A) Increases port speed
B) Bypasses listening and learning states for edge ports
C) Disables STP
D) Encrypts traffic

✔ Correct Answer: B

Reason: PortFast allows edge ports (connected to end devices) to transition directly to forwarding state, reducing connection time from 30-50 seconds to immediate.

Tag: Normal

---

### Question 382
Domain: Computer Networks
Topic: Network Protocols
Subtopic: UplinkFast
Difficulty: Hard

Question: What is UplinkFast used for?
A) Increase uplink speed
B) Fast convergence when direct link to root fails
C) Load balancing
D) Encryption

✔ Correct Answer: B

Reason: UplinkFast provides fast convergence (1-3 seconds) when a direct link to the root bridge fails by immediately activating a blocked port.

Tag: Normal

---

### Question 383
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BackboneFast
Difficulty: Hard

Question: What does BackboneFast optimize?
A) Backbone bandwidth
B) Convergence when indirect link fails
C) Security
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: BackboneFast reduces convergence time from 50 to 30 seconds when an indirect link fails by detecting inferior BPDUs and expiring max age timer early.

Tag: Normal

---

### Question 384
Domain: Computer Networks
Topic: VLAN
Subtopic: Trunk Ports
Difficulty: Medium

Question: What is a trunk port in VLAN configuration?
A) Port connected to router
B) Port carrying traffic for multiple VLANs
C) Blocked port
D) Management port

✔ Correct Answer: B

Reason: A trunk port carries traffic for multiple VLANs between switches, using VLAN tagging (802.1Q) to identify which VLAN each frame belongs to.

Tag: Past Paper

---

### Question 385
Domain: Computer Networks
Topic: VLAN
Subtopic: Access Port
Difficulty: Easy

Question: What is an access port in VLAN configuration?
A) Port for administrators only
B) Port belonging to single VLAN for end devices
C) Port for multiple VLANs
D) Disabled port

✔ Correct Answer: B

Reason: An access port belongs to a single VLAN and connects end devices. Frames on access ports are untagged.

Tag: Normal

---

### Question 386
Domain: Computer Networks
Topic: VLAN
Subtopic: Native VLAN
Difficulty: Hard

Question: What is the native VLAN on a trunk port?
A) VLAN 0
B) VLAN 1 (default)
C) VLAN 4095
D) No native VLAN exists

✔ Correct Answer: B

Reason: The native VLAN (default VLAN 1) carries untagged traffic on a trunk port. It's important to match native VLANs on both ends to avoid issues.

Tag: Normal

---

### Question 387
Domain: Computer Networks
Topic: VLAN
Subtopic: VTP
Difficulty: Hard

Question: What does VTP (VLAN Trunking Protocol) do?
A) Encrypt VLAN traffic
B) Propagate VLAN configuration across switches
C) Route between VLANs
D) Compress VLAN tags

✔ Correct Answer: B

Reason: VTP is a Cisco proprietary protocol that propagates VLAN configuration changes across switches in the same VTP domain, simplifying management.

Tag: Normal

---

### Question 388
Domain: Computer Networks
Topic: VLAN
Subtopic: Inter-VLAN Routing
Difficulty: Medium

Question: What is required for communication between different VLANs?
A) Nothing, they can communicate directly
B) Layer 3 device (router or Layer 3 switch)
C) Hub
D) Repeater

✔ Correct Answer: B

Reason: VLANs are separate broadcast domains. Communication between VLANs requires a Layer 3 device to route traffic between them.

Tag: Past Paper

---

### Question 389
Domain: Computer Networks
Topic: VLAN
Subtopic: Router on a Stick
Difficulty: Hard

Question: What is "router on a stick" configuration?
A) Physical router placement
B) Single router interface with subinterfaces for inter-VLAN routing
C) Redundant router setup
D) Wireless router configuration

✔ Correct Answer: B

Reason: Router on a stick uses a single physical interface with multiple subinterfaces (one per VLAN) connected to a trunk port for inter-VLAN routing.

Tag: Normal

---

### Question 390
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DTP
Difficulty: Hard

Question: What does DTP (Dynamic Trunking Protocol) negotiate?
A) IP addresses
B) Trunk formation between switches
C) Routing paths
D) Encryption keys

✔ Correct Answer: B

Reason: DTP is a Cisco proprietary protocol that automatically negotiates trunking between switches, though manual configuration is often preferred for security.

Tag: Normal

---

### Question 391
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PAGP vs LACP
Difficulty: Hard

Question: What is the main difference between PAgP and LACP?
A) PAgP is faster
B) PAgP is Cisco proprietary, LACP is standard
C) PAgP is more secure
D) PAgP uses different ports

✔ Correct Answer: B

Reason: PAgP (Port Aggregation Protocol) is Cisco proprietary for link aggregation, while LACP (802.3ad) is the IEEE standard, offering better interoperability.

Tag: Normal

---

### Question 392
Domain: Computer Networks
Topic: Network Performance
Subtopic: Microburst
Difficulty: Hard

Question: What is a microburst in networking?
A) Small packet
B) Short-duration traffic spike that can cause packet loss
C) Type of error
D) Encryption method

✔ Correct Answer: B

Reason: Microbursts are very short (milliseconds) traffic spikes that can overflow buffers and cause packet loss, difficult to detect with standard monitoring.

Tag: Normal

---

### Question 393
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LLDP vs CDP
Difficulty: Medium

Question: What advantage does LLDP have over CDP?
A) LLDP is faster
B) LLDP is vendor-neutral standard
C) LLDP is more secure
D) LLDP uses less bandwidth

✔ Correct Answer: B

Reason: LLDP is an IEEE standard (802.1AB) that works with all vendors, while CDP is Cisco proprietary and only works between Cisco devices.

Tag: Normal

---

### Question 394
Domain: Computer Networks
Topic: Network Security
Subtopic: DHCP Snooping
Difficulty: Hard

Question: What does DHCP snooping prevent?
A) DHCP server overload
B) Rogue DHCP servers and DHCP-based attacks
C) IP conflicts
D) Slow DHCP responses

✔ Correct Answer: B

Reason: DHCP snooping validates DHCP messages, building a binding table and preventing rogue DHCP servers and attacks like DHCP starvation.

Tag: Normal

---

### Question 395
Domain: Computer Networks
Topic: Network Security
Subtopic: DAI
Difficulty: Hard

Question: What does DAI (Dynamic ARP Inspection) prevent?
A) ARP cache overflow
B) ARP spoofing attacks
C) Slow ARP responses
D) ARP encryption

✔ Correct Answer: B

Reason: DAI validates ARP packets against DHCP snooping binding table, preventing ARP spoofing and man-in-the-middle attacks.

Tag: Normal

---

### Question 396
Domain: Computer Networks
Topic: Network Security
Subtopic: IP Source Guard
Difficulty: Hard

Question: What does IP Source Guard protect against?
A) DDoS attacks
B) IP spoofing by validating source IP
C) Port scanning
D) DNS attacks

✔ Correct Answer: B

Reason: IP Source Guard filters traffic based on DHCP snooping binding table, preventing IP spoofing by allowing only valid source IP addresses.

Tag: Normal

---

### Question 397
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Storm Control
Difficulty: Medium

Question: What does storm control prevent?
A) Weather-related outages
B) Broadcast, multicast, or unicast storms
C) Power surges
D) Temperature issues

✔ Correct Answer: B

Reason: Storm control monitors and limits broadcast, multicast, or unknown unicast traffic to prevent network storms that can overwhelm switches.

Tag: Normal

---

### Question 398
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Port Mirroring
Difficulty: Medium

Question: What is port mirroring (SPAN) used for?
A) Backup connections
B) Copying traffic to monitoring port for analysis
C) Load balancing
D) Encryption

✔ Correct Answer: B

Reason: Port mirroring (SPAN - Switched Port Analyzer) copies traffic from one or more ports to a monitoring port for analysis with tools like Wireshark.

Tag: Normal

---

### Question 399
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RSPAN
Difficulty: Hard

Question: How does RSPAN differ from local SPAN?
A) RSPAN is faster
B) RSPAN can mirror traffic across switches using VLAN
C) RSPAN is more secure
D) RSPAN uses different protocols

✔ Correct Answer: B

Reason: RSPAN (Remote SPAN) extends SPAN across multiple switches by using a dedicated RSPAN VLAN to carry mirrored traffic to a remote monitoring port.

Tag: Normal

---

### Question 400
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ERSPAN
Difficulty: Hard

Question: What advantage does ERSPAN have over RSPAN?
A) Lower cost
B) Can span across Layer 3 boundaries using GRE
C) Simpler configuration
D) Faster mirroring

✔ Correct Answer: B

Reason: ERSPAN (Encapsulated Remote SPAN) uses GRE encapsulation to mirror traffic across Layer 3 networks, not limited to Layer 2 like RSPAN.

Tag: Normal

---

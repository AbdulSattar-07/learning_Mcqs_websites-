# Computer Networks - MCQ Batch 02
## Questions 101-200

---

### Question 101
Domain: Computer Networks
Topic: Network Models
Subtopic: Hybrid Topology
Difficulty: Medium

Question: A network combining star and bus topologies is called:
A) Mesh topology
B) Hybrid topology
C) Tree topology
D) Ring topology

✔ Correct Answer: B

Reason: Hybrid topology combines two or more different topologies. A common example is combining star and bus topologies for larger networks.

Tag: Normal

---

### Question 102
Domain: Computer Networks
Topic: Collision Domain
Subtopic: Fundamentals
Difficulty: Medium

Question: How many collision domains exist in a network with 8 ports connected to a hub?
A) 1
B) 4
C) 8
D) 16

✔ Correct Answer: A

Reason: A hub creates a single collision domain for all connected devices because it broadcasts to all ports, causing potential collisions.

Tag: Past Paper

---

### Question 103
Domain: Computer Networks
Topic: Collision Domain
Subtopic: Switch vs Hub
Difficulty: Medium

Question: How many collision domains are created by an 8-port switch?
A) 1
B) 4
C) 8
D) 16

✔ Correct Answer: C

Reason: Each port on a switch creates its own collision domain, so an 8-port switch creates 8 separate collision domains, reducing collisions.

Tag: Normal

---

### Question 104
Domain: Computer Networks
Topic: Broadcast Domain
Subtopic: Fundamentals
Difficulty: Medium

Question: Which device can segment broadcast domains?
A) Hub
B) Switch
C) Router
D) Repeater

✔ Correct Answer: C

Reason: Routers segment broadcast domains by not forwarding broadcast traffic between networks. Switches and hubs forward broadcasts within their network.

Tag: Past Paper

---

### Question 105
Domain: Computer Networks
Topic: VLAN
Subtopic: Fundamentals
Difficulty: Medium

Question: What is the primary purpose of VLANs?
A) Increase bandwidth
B) Logically segment a network
C) Encrypt traffic
D) Compress data

✔ Correct Answer: B

Reason: VLANs (Virtual LANs) logically segment a physical network into multiple broadcast domains, improving security and network management.

Tag: Normal

---

### Question 106
Domain: Computer Networks
Topic: VLAN
Subtopic: Tagging
Difficulty: Hard

Question: Which IEEE standard defines VLAN tagging?
A) 802.3
B) 802.11
C) 802.1Q
D) 802.1X

✔ Correct Answer: C

Reason: IEEE 802.1Q is the standard for VLAN tagging on Ethernet networks, adding a 4-byte tag to frames to identify VLAN membership.

Tag: Normal

---

### Question 107
Domain: Computer Networks
Topic: Spanning Tree Protocol
Subtopic: Purpose
Difficulty: Hard

Question: What problem does Spanning Tree Protocol (STP) solve?
A) IP address conflicts
B) Routing loops
C) Layer 2 loops in switched networks
D) Bandwidth limitations

✔ Correct Answer: C

Reason: STP prevents Layer 2 loops in switched networks by blocking redundant paths while maintaining backup links for fault tolerance.

Tag: Normal

---

### Question 108
Domain: Computer Networks
Topic: ARP
Subtopic: Operation
Difficulty: Hard

Question: What type of message does a host send when it needs to find a MAC address?
A) ARP request (broadcast)
B) ARP request (unicast)
C) ARP reply (broadcast)
D) ARP reply (unicast)

✔ Correct Answer: A

Reason: ARP request is sent as a broadcast to all devices on the local network. The device with the matching IP responds with a unicast ARP reply containing its MAC address.

Tag: Past Paper

---

### Question 109
Domain: Computer Networks
Topic: RARP
Subtopic: Fundamentals
Difficulty: Medium

Question: What is the purpose of RARP (Reverse ARP)?
A) Find IP address from MAC address
B) Find MAC address from IP address
C) Find domain name from IP address
D) Find port number from IP address

✔ Correct Answer: A

Reason: RARP performs the reverse operation of ARP, allowing a device to discover its IP address when it only knows its MAC address (used by diskless workstations).

Tag: Normal

---

### Question 110
Domain: Computer Networks
Topic: Subnetting
Subtopic: Calculation
Difficulty: Hard

Question: How many subnets can be created from a Class C network using a /27 mask?
A) 2
B) 4
C) 8
D) 16

✔ Correct Answer: C

Reason: Class C default is /24. A /27 mask borrows 3 bits for subnetting (27-24=3). 2^3 = 8 subnets can be created.

Tag: Normal

---

### Question 111
Domain: Computer Networks
Topic: Subnetting
Subtopic: Private IP Ranges
Difficulty: Easy

Question: Which of the following is a private IP address range?
A) 172.16.0.0 - 172.31.255.255
B) 172.32.0.0 - 172.64.255.255
C) 192.169.0.0 - 192.169.255.255
D) 10.0.0.0 - 10.255.255.254

✔ Correct Answer: A

Reason: Private IP ranges are: 10.0.0.0/8, 172.16.0.0/12 (172.16-172.31), and 192.168.0.0/16. These are not routable on the public Internet.

Tag: Normal

---

### Question 112
Domain: Computer Networks
Topic: Network Security
Subtopic: Attack Types
Difficulty: Medium

Question: What type of attack floods a network with excessive traffic to make it unavailable?
A) Phishing
B) Man-in-the-middle
C) Denial of Service (DoS)
D) SQL injection

✔ Correct Answer: C

Reason: DoS attacks overwhelm a network, server, or service with excessive traffic, making it unavailable to legitimate users.

Tag: Past Paper

---

### Question 113
Domain: Computer Networks
Topic: Network Security
Subtopic: DDoS
Difficulty: Medium

Question: How does a DDoS attack differ from a DoS attack?
A) DDoS is less severe
B) DDoS uses multiple sources
C) DDoS targets only web servers
D) DDoS is easier to prevent

✔ Correct Answer: B

Reason: DDoS (Distributed Denial of Service) uses multiple compromised systems to launch the attack, making it harder to defend against than single-source DoS.

Tag: Normal

---

### Question 114
Domain: Computer Networks
Topic: Network Security
Subtopic: Man-in-the-Middle
Difficulty: Hard

Question: Which attack involves intercepting communication between two parties?
A) Spoofing
B) Man-in-the-middle
C) Replay attack
D) Brute force

✔ Correct Answer: B

Reason: Man-in-the-middle (MITM) attacks intercept and potentially alter communication between two parties who believe they're communicating directly.

Tag: Normal

---

### Question 115
Domain: Computer Networks
Topic: Network Security
Subtopic: Spoofing
Difficulty: Medium

Question: IP spoofing involves:
A) Stealing passwords
B) Forging source IP addresses
C) Encrypting packets
D) Blocking network traffic

✔ Correct Answer: B

Reason: IP spoofing is creating packets with a forged source IP address to hide the sender's identity or impersonate another system.

Tag: Normal

---

### Question 116
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SNMP
Difficulty: Medium

Question: What is SNMP used for?
A) Sending emails
B) Network management and monitoring
C) File transfer
D) Web browsing

✔ Correct Answer: B

Reason: SNMP (Simple Network Management Protocol) is used for monitoring and managing network devices, collecting information about network performance and status.

Tag: Past Paper

---

### Question 117
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Telnet
Difficulty: Easy

Question: What is the default port for Telnet?
A) 21
B) 22
C) 23
D) 25

✔ Correct Answer: C

Reason: Telnet uses port 23 for remote terminal access. However, it's insecure as data is sent in plaintext; SSH (port 22) is the secure alternative.

Tag: Normal

---

### Question 118
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SSH
Difficulty: Medium

Question: What advantage does SSH have over Telnet?
A) Faster connection
B) Encrypted communication
C) Simpler configuration
D) Lower bandwidth usage

✔ Correct Answer: B

Reason: SSH (Secure Shell) encrypts all communication including authentication credentials, while Telnet sends everything in plaintext.

Tag: Normal

---

### Question 119
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TFTP
Difficulty: Medium

Question: Which transport protocol does TFTP use?
A) TCP
B) UDP
C) SCTP
D) DCCP

✔ Correct Answer: B

Reason: TFTP (Trivial File Transfer Protocol) uses UDP port 69, making it simpler and faster than FTP but without reliability guarantees.

Tag: Normal

---

### Question 120
Domain: Computer Networks
Topic: Socket Programming
Subtopic: Fundamentals
Difficulty: Medium

Question: A socket is identified by:
A) IP address only
B) Port number only
C) IP address and port number
D) MAC address and port number

✔ Correct Answer: C

Reason: A socket is uniquely identified by the combination of IP address and port number, enabling multiple connections on a single host.

Tag: Past Paper

---

### Question 121
Domain: Computer Networks
Topic: Network Standards
Subtopic: IEEE 802
Difficulty: Easy

Question: Which IEEE standard defines Ethernet?
A) 802.3
B) 802.11
C) 802.15
D) 802.16

✔ Correct Answer: A

Reason: IEEE 802.3 defines Ethernet standards for wired LANs. 802.11 is Wi-Fi, 802.15 is Bluetooth/WPAN, 802.16 is WiMAX.

Tag: Past Paper

---

### Question 122
Domain: Computer Networks
Topic: Network Standards
Subtopic: IEEE 802.11
Difficulty: Easy

Question: Which IEEE standard defines wireless LAN (Wi-Fi)?
A) 802.3
B) 802.11
C) 802.15
D) 802.16

✔ Correct Answer: B

Reason: IEEE 802.11 is the standard for wireless LANs (Wi-Fi), with variants like 802.11a/b/g/n/ac/ax defining different speeds and frequencies.

Tag: Normal

---

### Question 123
Domain: Computer Networks
Topic: Network Standards
Subtopic: IEEE 802.15
Difficulty: Medium

Question: What technology does IEEE 802.15 standardize?
A) Ethernet
B) Wi-Fi
C) Bluetooth and WPAN
D) WiMAX

✔ Correct Answer: C

Reason: IEEE 802.15 defines standards for Wireless Personal Area Networks (WPAN), including Bluetooth and other short-range wireless technologies.

Tag: Normal

---

### Question 124
Domain: Computer Networks
Topic: Framing
Subtopic: Byte Stuffing
Difficulty: Hard

Question: Why is byte stuffing used in data link layer framing?
A) To compress data
B) To distinguish data from control characters
C) To encrypt frames
D) To increase transmission speed

✔ Correct Answer: B

Reason: Byte stuffing (character stuffing) adds escape characters before special flag bytes in data to distinguish them from frame delimiters.

Tag: Normal

---

### Question 125
Domain: Computer Networks
Topic: Framing
Subtopic: Bit Stuffing
Difficulty: Hard

Question: In bit stuffing, if the data contains five consecutive 1s, what is inserted?
A) A 0 bit
B) A 1 bit
C) Two 0 bits
D) Nothing

✔ Correct Answer: A

Reason: Bit stuffing inserts a 0 after five consecutive 1s to prevent confusion with the flag pattern (01111110), which marks frame boundaries.

Tag: Normal

---

### Question 126
Domain: Computer Networks
Topic: Network Delay
Subtopic: Components
Difficulty: Medium

Question: Which delay is caused by waiting in router queues?
A) Propagation delay
B) Transmission delay
C) Queuing delay
D) Processing delay

✔ Correct Answer: C

Reason: Queuing delay occurs when packets wait in router buffers before being processed, varying with network congestion levels.

Tag: Past Paper

---

### Question 127
Domain: Computer Networks
Topic: Network Delay
Subtopic: Transmission Delay
Difficulty: Hard

Question: Transmission delay depends on:
A) Distance between nodes
B) Packet size and link bandwidth
C) Router processing speed
D) Number of hops

✔ Correct Answer: B

Reason: Transmission delay = Packet size / Bandwidth. It's the time to push all bits of a packet onto the link.

Tag: Normal

---

### Question 128
Domain: Computer Networks
Topic: CDN
Subtopic: Fundamentals
Difficulty: Easy

Question: What does CDN stand for?
A) Central Data Network
B) Content Delivery Network
C) Computer Distribution Network
D) Cached Domain Network

✔ Correct Answer: B

Reason: CDN (Content Delivery Network) distributes content across geographically dispersed servers to reduce latency and improve load times for users.

Tag: Normal

---

### Question 129
Domain: Computer Networks
Topic: CDN
Subtopic: Benefits
Difficulty: Medium

Question: What is the main benefit of using a CDN?
A) Reduced hosting costs
B) Improved content delivery speed
C) Better SEO ranking
D) Automatic content updates

✔ Correct Answer: B

Reason: CDNs cache content on edge servers closer to users, significantly reducing latency and improving content delivery speed and user experience.

Tag: Normal

---

### Question 130
Domain: Computer Networks
Topic: Load Balancing
Subtopic: Fundamentals
Difficulty: Easy

Question: What is the purpose of load balancing?
A) Encrypt network traffic
B) Distribute traffic across multiple servers
C) Block malicious requests
D) Compress data packets

✔ Correct Answer: B

Reason: Load balancing distributes incoming network traffic across multiple servers to optimize resource utilization, maximize throughput, and ensure high availability.

Tag: Normal

---

### Question 131
Domain: Computer Networks
Topic: Load Balancing
Subtopic: Algorithms
Difficulty: Medium

Question: Which load balancing algorithm sends requests to servers in sequential order?
A) Random
B) Least connections
C) Round robin
D) IP hash

✔ Correct Answer: C

Reason: Round robin distributes requests sequentially to each server in turn, providing simple and fair distribution without considering server load.

Tag: Past Paper

---

### Question 132
Domain: Computer Networks
Topic: Proxy Server
Subtopic: Forward Proxy
Difficulty: Medium

Question: What is the primary function of a forward proxy?
A) Cache server responses
B) Act on behalf of clients to access servers
C) Load balance server requests
D) Encrypt all traffic

✔ Correct Answer: B

Reason: A forward proxy acts as an intermediary for clients, forwarding their requests to servers, providing anonymity, caching, and access control.

Tag: Normal

---

### Question 133
Domain: Computer Networks
Topic: Proxy Server
Subtopic: Reverse Proxy
Difficulty: Hard

Question: How does a reverse proxy differ from a forward proxy?
A) It's faster
B) It acts on behalf of servers, not clients
C) It only works with HTTPS
D) It doesn't cache content

✔ Correct Answer: B

Reason: A reverse proxy sits in front of servers and acts on their behalf, handling client requests, providing load balancing, caching, and security for backend servers.

Tag: Normal

---

### Question 134
Domain: Computer Networks
Topic: Network Troubleshooting
Subtopic: Ping
Difficulty: Easy

Question: What does a successful ping response indicate?
A) The target is reachable at network layer
B) All services on target are running
C) The target has no firewall
D) The connection is encrypted

✔ Correct Answer: A

Reason: A successful ping indicates network layer connectivity (Layer 3) to the target, but doesn't guarantee application-level services are functioning.

Tag: Normal

---

### Question 135
Domain: Computer Networks
Topic: Network Troubleshooting
Subtopic: Traceroute
Difficulty: Medium

Question: What information does traceroute provide?
A) Bandwidth between nodes
B) Path and hop-by-hop delays to destination
C) MAC addresses of routers
D) Encryption status of links

✔ Correct Answer: B

Reason: Traceroute shows the path packets take to reach a destination and the round-trip time to each hop, useful for identifying routing issues.

Tag: Past Paper

---

### Question 136
Domain: Computer Networks
Topic: Network Troubleshooting
Subtopic: Netstat
Difficulty: Medium

Question: What information does the netstat command display?
A) DNS records
B) Active network connections and listening ports
C) Wireless signal strength
D) Bandwidth usage

✔ Correct Answer: B

Reason: Netstat displays active TCP connections, listening ports, routing tables, and network interface statistics.

Tag: Normal

---

### Question 137
Domain: Computer Networks
Topic: Network Troubleshooting
Subtopic: Nslookup
Difficulty: Easy

Question: What is the purpose of the nslookup command?
A) Check network speed
B) Query DNS records
C) Test port connectivity
D) Monitor bandwidth

✔ Correct Answer: B

Reason: Nslookup queries DNS servers to obtain domain name or IP address mapping and other DNS records.

Tag: Normal

---

### Question 138
Domain: Computer Networks
Topic: Bandwidth Calculation
Subtopic: Nyquist Theorem
Difficulty: Hard

Question: According to Nyquist theorem, what is the maximum data rate for a noiseless channel with bandwidth 3000 Hz and 4 signal levels?
A) 6000 bps
B) 12000 bps
C) 24000 bps
D) 3000 bps

✔ Correct Answer: B

Reason: Nyquist rate = 2 × Bandwidth × log2(L), where L is signal levels. 2 × 3000 × log2(4) = 2 × 3000 × 2 = 12000 bps.

Tag: Normal

---

### Question 139
Domain: Computer Networks
Topic: Bandwidth Calculation
Subtopic: Shannon Capacity
Difficulty: Hard

Question: Shannon capacity theorem considers which factor that Nyquist doesn't?
A) Bandwidth
B) Signal levels
C) Noise
D) Frequency

✔ Correct Answer: C

Reason: Shannon capacity theorem accounts for noise (SNR - Signal-to-Noise Ratio) in the channel, while Nyquist assumes a noiseless channel.

Tag: Normal

---

### Question 140
Domain: Computer Networks
Topic: Network Protocols
Subtopic: NTP
Difficulty: Medium

Question: What is the purpose of NTP (Network Time Protocol)?
A) Transfer files
B) Synchronize clocks across network
C) Manage network topology
D) Allocate IP addresses

✔ Correct Answer: B

Reason: NTP synchronizes computer clocks across a network to a reference time source, crucial for distributed systems and security protocols.

Tag: Normal

---

### Question 141
Domain: Computer Networks
Topic: Network Address Translation
Subtopic: Types
Difficulty: Hard

Question: In which NAT type is the mapping between private and public addresses one-to-one and permanent?
A) Dynamic NAT
B) Static NAT
C) PAT
D) Overlapping NAT

✔ Correct Answer: B

Reason: Static NAT creates a permanent one-to-one mapping between a private IP and a public IP, useful for servers that need consistent external addresses.

Tag: Normal

---

### Question 142
Domain: Computer Networks
Topic: Fragmentation
Subtopic: IPv4
Difficulty: Hard

Question: What happens when an IP packet is larger than the MTU of a link?
A) Packet is dropped
B) Packet is compressed
C) Packet is fragmented
D) Packet is queued

✔ Correct Answer: C

Reason: When a packet exceeds the Maximum Transmission Unit (MTU), it's fragmented into smaller packets that fit the MTU, then reassembled at the destination.

Tag: Past Paper

---

### Question 143
Domain: Computer Networks
Topic: Fragmentation
Subtopic: MTU
Difficulty: Medium

Question: What is the typical MTU size for Ethernet?
A) 576 bytes
B) 1500 bytes
C) 9000 bytes
D) 65535 bytes

✔ Correct Answer: B

Reason: Standard Ethernet has an MTU of 1500 bytes. Jumbo frames can support up to 9000 bytes, but 1500 is the standard.

Tag: Normal

---

### Question 144
Domain: Computer Networks
Topic: Multicast
Subtopic: Addressing
Difficulty: Medium

Question: Which IP address class is reserved for multicast?
A) Class A
B) Class B
C) Class C
D) Class D

✔ Correct Answer: D

Reason: Class D addresses (224.0.0.0 to 239.255.255.255) are reserved for multicast, allowing one-to-many communication.

Tag: Past Paper

---

### Question 145
Domain: Computer Networks
Topic: Multicast
Subtopic: Protocols
Difficulty: Hard

Question: Which protocol is used for multicast group management?
A) ICMP
B) IGMP
C) SMTP
D) SNMP

✔ Correct Answer: B

Reason: IGMP (Internet Group Management Protocol) manages multicast group membership, allowing hosts to join or leave multicast groups.

Tag: Normal

---

### Question 146
Domain: Computer Networks
Topic: Unicast vs Multicast vs Broadcast
Subtopic: Comparison
Difficulty: Easy

Question: In unicast communication, data is sent to:
A) All devices on the network
B) A specific group of devices
C) A single specific device
D) Random devices

✔ Correct Answer: C

Reason: Unicast is one-to-one communication where data is sent from one sender to one specific receiver.

Tag: Normal

---

### Question 147
Domain: Computer Networks
Topic: Broadcast
Subtopic: Types
Difficulty: Medium

Question: What is the broadcast address for the network 192.168.1.0/24?
A) 192.168.1.0
B) 192.168.1.1
C) 192.168.1.254
D) 192.168.1.255

✔ Correct Answer: D

Reason: The broadcast address has all host bits set to 1. For 192.168.1.0/24, the broadcast address is 192.168.1.255.

Tag: Normal

---

### Question 148
Domain: Computer Networks
Topic: Network Segmentation
Subtopic: Benefits
Difficulty: Medium

Question: What is a primary benefit of network segmentation?
A) Increased bandwidth for all users
B) Improved security and reduced broadcast traffic
C) Elimination of all network devices
D) Automatic IP assignment

✔ Correct Answer: B

Reason: Network segmentation divides a network into smaller segments, improving security by isolating traffic and reducing broadcast domains.

Tag: Normal

---

### Question 149
Domain: Computer Networks
Topic: Repeater
Subtopic: Function
Difficulty: Easy

Question: What is the primary function of a repeater?
A) Filter packets
B) Amplify and regenerate signals
C) Route packets
D) Encrypt data

✔ Correct Answer: B

Reason: Repeaters operate at the Physical Layer to amplify and regenerate signals, extending the transmission distance without changing the data.

Tag: Normal

---

### Question 150
Domain: Computer Networks
Topic: Network Cabling
Subtopic: Crossover vs Straight
Difficulty: Medium

Question: When is a crossover cable used?
A) Connecting a computer to a switch
B) Connecting two computers directly
C) Connecting a router to a modem
D) Connecting a computer to a printer

✔ Correct Answer: B

Reason: Crossover cables connect similar devices (computer-to-computer, switch-to-switch) by crossing transmit and receive pairs. Straight-through cables connect different devices.

Tag: Past Paper

---

### Question 151
Domain: Computer Networks
Topic: Network Cabling
Subtopic: Cable Categories
Difficulty: Easy

Question: Which cable category supports Gigabit Ethernet?
A) Cat3
B) Cat5
C) Cat5e
D) Cat1

✔ Correct Answer: C

Reason: Cat5e (Category 5 enhanced) and higher categories support Gigabit Ethernet (1000 Mbps). Cat5 can support it but Cat5e is the standard.

Tag: Normal

---

### Question 152
Domain: Computer Networks
Topic: Modulation
Subtopic: Types
Difficulty: Medium

Question: Which modulation technique varies the amplitude of the carrier signal?
A) Frequency Modulation (FM)
B) Amplitude Modulation (AM)
C) Phase Modulation (PM)
D) Pulse Code Modulation (PCM)

✔ Correct Answer: B

Reason: Amplitude Modulation varies the amplitude of the carrier signal according to the information signal while keeping frequency constant.

Tag: Normal

---

### Question 153
Domain: Computer Networks
Topic: Modulation
Subtopic: Digital Modulation
Difficulty: Hard

Question: Which digital modulation technique is most resistant to noise?
A) ASK (Amplitude Shift Keying)
B) FSK (Frequency Shift Keying)
C) PSK (Phase Shift Keying)
D) All are equally resistant

✔ Correct Answer: B

Reason: FSK is more resistant to noise than ASK because frequency changes are less affected by amplitude variations caused by noise.

Tag: Normal

---

### Question 154
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Three-Tier
Difficulty: Medium

Question: In a three-tier network architecture, which layer connects to end users?
A) Core layer
B) Distribution layer
C) Access layer
D) Application layer

✔ Correct Answer: C

Reason: The access layer (edge layer) connects end-user devices to the network. Distribution layer aggregates access layers, core layer provides high-speed backbone.

Tag: Normal

---

### Question 155
Domain: Computer Networks
Topic: Bandwidth Utilization
Subtopic: Efficiency
Difficulty: Hard

Question: If a channel has 1 Mbps bandwidth and transmits 800 Kbps actual data, what is the efficiency?
A) 60%
B) 70%
C) 80%
D) 90%

✔ Correct Answer: C

Reason: Efficiency = (Actual throughput / Bandwidth) × 100 = (800/1000) × 100 = 80%. The remaining 20% is overhead.

Tag: Normal

---

### Question 156
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SMTP
Difficulty: Easy

Question: What is the default port number for SMTP?
A) 21
B) 25
C) 80
D) 110

✔ Correct Answer: B

Reason: SMTP (Simple Mail Transfer Protocol) uses port 25 for email transmission. Port 587 is used for SMTP with authentication (submission).

Tag: Past Paper

---

### Question 157
Domain: Computer Networks
Topic: Network Protocols
Subtopic: POP3
Difficulty: Easy

Question: What is the default port for POP3?
A) 25
B) 80
C) 110
D) 143

✔ Correct Answer: C

Reason: POP3 (Post Office Protocol version 3) uses port 110 for retrieving emails. Secure POP3 (POP3S) uses port 995.

Tag: Normal

---

### Question 158
Domain: Computer Networks
Topic: Network Protocols
Subtopic: IMAP
Difficulty: Medium

Question: Which port does IMAP use by default?
A) 110
B) 143
C) 993
D) 995

✔ Correct Answer: B

Reason: IMAP (Internet Message Access Protocol) uses port 143. Secure IMAP (IMAPS) uses port 993 with SSL/TLS encryption.

Tag: Normal

---

### Question 159
Domain: Computer Networks
Topic: Cookies
Subtopic: Web Technology
Difficulty: Easy

Question: What is the primary purpose of HTTP cookies?
A) Encrypt web traffic
B) Store stateful information on the client side
C) Compress web pages
D) Block advertisements

✔ Correct Answer: B

Reason: Cookies store small pieces of data on the client side to maintain state in the stateless HTTP protocol, enabling sessions, preferences, and tracking.

Tag: Normal

---

### Question 160
Domain: Computer Networks
Topic: Session Management
Subtopic: Stateless vs Stateful
Difficulty: Medium

Question: Which protocol is stateless?
A) FTP
B) HTTP
C) Telnet
D) SSH

✔ Correct Answer: B

Reason: HTTP is stateless, meaning each request is independent and the server doesn't retain information about previous requests. Cookies and sessions add state.

Tag: Past Paper

---

### Question 161
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LDAP
Difficulty: Medium

Question: What is LDAP primarily used for?
A) File transfer
B) Directory services and authentication
C) Email routing
D) Web browsing

✔ Correct Answer: B

Reason: LDAP (Lightweight Directory Access Protocol) is used for accessing and maintaining distributed directory information services, commonly for authentication.

Tag: Normal

---

### Question 162
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SIP
Difficulty: Hard

Question: Which protocol is used for initiating VoIP calls?
A) RTP
B) RTCP
C) SIP
D) H.323

✔ Correct Answer: C

Reason: SIP (Session Initiation Protocol) is used for signaling and controlling multimedia communication sessions like VoIP calls. RTP carries the actual voice data.

Tag: Normal

---

### Question 163
Domain: Computer Networks
Topic: Network Protocols
Subtopic: RTP
Difficulty: Hard

Question: What type of data does RTP (Real-time Transport Protocol) carry?
A) Email messages
B) Web pages
C) Audio and video streams
D) File transfers

✔ Correct Answer: C

Reason: RTP is designed for delivering audio and video over IP networks, providing timing information and sequence numbering for real-time data.

Tag: Normal

---

### Question 164
Domain: Computer Networks
Topic: Network Management
Subtopic: SNMP Components
Difficulty: Medium

Question: Which component in SNMP architecture stores management information?
A) SNMP manager
B) SNMP agent
C) MIB (Management Information Base)
D) SNMP trap

✔ Correct Answer: C

Reason: MIB is a database that stores management information about network devices. SNMP agents access MIB data, and managers query agents.

Tag: Normal

---

### Question 165
Domain: Computer Networks
Topic: Network Management
Subtopic: SNMP Operations
Difficulty: Hard

Question: Which SNMP operation is used by an agent to notify the manager of an event?
A) GET
B) SET
C) TRAP
D) RESPONSE

✔ Correct Answer: C

Reason: TRAP is an unsolicited message sent by an SNMP agent to the manager to report significant events or threshold violations.

Tag: Past Paper

---

### Question 166
Domain: Computer Networks
Topic: Wireless Security
Subtopic: WEP
Difficulty: Medium

Question: Why is WEP considered insecure?
A) It uses weak encryption algorithms
B) It has no encryption
C) It's too slow
D) It requires expensive hardware

✔ Correct Answer: A

Reason: WEP uses the RC4 encryption algorithm with weak key management, making it vulnerable to attacks. It can be cracked in minutes with modern tools.

Tag: Normal

---

### Question 167
Domain: Computer Networks
Topic: Wireless Security
Subtopic: WPA2
Difficulty: Medium

Question: Which encryption algorithm does WPA2 use?
A) DES
B) 3DES
C) AES
D) RC4

✔ Correct Answer: C

Reason: WPA2 uses AES (Advanced Encryption Standard) with CCMP, providing strong encryption for wireless networks, much more secure than WEP's RC4.

Tag: Normal

---

### Question 168
Domain: Computer Networks
Topic: Network Topology
Subtopic: Ring Topology
Difficulty: Medium

Question: What happens in a ring topology if one node fails?
A) Network continues normally
B) Only adjacent nodes are affected
C) Entire network can fail (without redundancy)
D) Network speed increases

✔ Correct Answer: C

Reason: In a single ring topology, if one node fails, the entire network can fail as the ring is broken. Dual ring topologies provide redundancy.

Tag: Normal

---

### Question 169
Domain: Computer Networks
Topic: Network Topology
Subtopic: Tree Topology
Difficulty: Medium

Question: Tree topology is a combination of which two topologies?
A) Star and Ring
B) Star and Bus
C) Bus and Ring
D) Mesh and Star

✔ Correct Answer: B

Reason: Tree topology (hierarchical topology) combines star and bus topologies, with multiple star networks connected via a bus backbone.

Tag: Normal

---

### Question 170
Domain: Computer Networks
Topic: Carrier Sense
Subtopic: CSMA
Difficulty: Hard

Question: In 1-persistent CSMA, what does a station do when it finds the channel busy?
A) Wait for a random time
B) Continuously sense until idle, then transmit immediately
C) Wait for a fixed time
D) Give up transmission

✔ Correct Answer: B

Reason: In 1-persistent CSMA, when the channel is busy, the station continuously senses and transmits immediately when idle (with probability 1).

Tag: Normal

---

### Question 171
Domain: Computer Networks
Topic: Carrier Sense
Subtopic: CSMA Variants
Difficulty: Hard

Question: In p-persistent CSMA, if the channel is idle, what does the station do?
A) Always transmit immediately
B) Transmit with probability p
C) Wait for acknowledgment
D) Sense again after random time

✔ Correct Answer: B

Reason: In p-persistent CSMA, when the channel is idle, the station transmits with probability p or defers with probability (1-p), reducing collision probability.

Tag: Normal

---

### Question 172
Domain: Computer Networks
Topic: Network Devices
Subtopic: Modem
Difficulty: Easy

Question: What does a modem do?
A) Amplifies signals
B) Modulates and demodulates signals
C) Routes packets
D) Filters traffic

✔ Correct Answer: B

Reason: A modem (modulator-demodulator) converts digital signals to analog for transmission and analog back to digital for reception.

Tag: Past Paper

---

### Question 173
Domain: Computer Networks
Topic: Network Devices
Subtopic: NIC
Difficulty: Easy

Question: What does NIC stand for?
A) Network Interface Card
B) Network Internet Connection
C) Node Interface Controller
D) Network Integrated Circuit

✔ Correct Answer: A

Reason: NIC (Network Interface Card) is a hardware component that connects a computer to a network, providing the physical interface and MAC address.

Tag: Normal

---

### Question 174
Domain: Computer Networks
Topic: Packet Structure
Subtopic: Header
Difficulty: Medium

Question: What information is typically NOT found in a packet header?
A) Source address
B) Destination address
C) Actual user data
D) Protocol type

✔ Correct Answer: C

Reason: Packet headers contain control information (addresses, protocol, sequence numbers, etc.). Actual user data is in the payload, not the header.

Tag: Normal

---

### Question 175
Domain: Computer Networks
Topic: Packet Structure
Subtopic: Encapsulation
Difficulty: Medium

Question: What is the process of adding headers to data as it moves down the OSI layers called?
A) Decapsulation
B) Encapsulation
C) Fragmentation
D) Segmentation

✔ Correct Answer: B

Reason: Encapsulation is the process of adding protocol headers at each layer as data moves down the OSI model. Decapsulation is the reverse process.

Tag: Past Paper

---

### Question 176
Domain: Computer Networks
Topic: Protocol Data Units
Subtopic: Terminology
Difficulty: Easy

Question: What is the PDU (Protocol Data Unit) at the Transport Layer called?
A) Bit
B) Frame
C) Packet
D) Segment

✔ Correct Answer: D

Reason: Transport Layer PDU is called a segment (TCP) or datagram (UDP). Network Layer uses packet, Data Link uses frame, Physical uses bit.

Tag: Past Paper

---

### Question 177
Domain: Computer Networks
Topic: Protocol Data Units
Subtopic: Data Link Layer
Difficulty: Easy

Question: What is the PDU at the Data Link Layer called?
A) Packet
B) Frame
C) Segment
D) Datagram

✔ Correct Answer: B

Reason: The Data Link Layer PDU is called a frame, which includes MAC addresses and error detection information.

Tag: Normal

---

### Question 178
Domain: Computer Networks
Topic: Network Security
Subtopic: IDS
Difficulty: Medium

Question: What does IDS stand for?
A) Internet Data Service
B) Intrusion Detection System
C) Internal Domain Server
D) Integrated Data Security

✔ Correct Answer: B

Reason: IDS (Intrusion Detection System) monitors network traffic for suspicious activity and potential threats, alerting administrators to security incidents.

Tag: Normal

---

### Question 179
Domain: Computer Networks
Topic: Network Security
Subtopic: IDS vs IPS
Difficulty: Hard

Question: How does IPS differ from IDS?
A) IPS is faster
B) IPS can actively block threats, IDS only detects
C) IPS is cheaper
D) IPS works only on wireless networks

✔ Correct Answer: B

Reason: IPS (Intrusion Prevention System) can actively block or prevent detected threats, while IDS only detects and alerts. IPS is inline, IDS is passive.

Tag: Normal

---

### Question 180
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BGP
Difficulty: Hard

Question: What type of routing protocol is BGP?
A) Distance vector
B) Link state
C) Path vector
D) Hybrid

✔ Correct Answer: C

Reason: BGP (Border Gateway Protocol) is a path vector protocol used for inter-domain routing on the Internet, maintaining path information to prevent loops.

Tag: Normal

---

### Question 181
Domain: Computer Networks
Topic: Network Protocols
Subtopic: EIGRP
Difficulty: Hard

Question: EIGRP is a routing protocol developed by which company?
A) Microsoft
B) Cisco
C) Juniper
D) IBM

✔ Correct Answer: B

Reason: EIGRP (Enhanced Interior Gateway Routing Protocol) is a Cisco proprietary advanced distance vector routing protocol, though later versions are open.

Tag: Normal

---

### Question 182
Domain: Computer Networks
Topic: Routing Metrics
Subtopic: Cost Calculation
Difficulty: Hard

Question: In OSPF, the cost of a link is typically based on:
A) Hop count
B) Bandwidth
C) Delay
D) Reliability

✔ Correct Answer: B

Reason: OSPF calculates link cost based on bandwidth using the formula: Cost = Reference bandwidth / Interface bandwidth. Higher bandwidth = lower cost.

Tag: Normal

---

### Question 183
Domain: Computer Networks
Topic: Network Address
Subtopic: Loopback
Difficulty: Easy

Question: Which address range is reserved for loopback?
A) 10.0.0.0/8
B) 127.0.0.0/8
C) 192.168.0.0/16
D) 169.254.0.0/16

✔ Correct Answer: B

Reason: The entire 127.0.0.0/8 range is reserved for loopback addresses, with 127.0.0.1 being the most commonly used.

Tag: Normal

---

### Question 184
Domain: Computer Networks
Topic: Network Address
Subtopic: APIPA
Difficulty: Medium

Question: What is the purpose of APIPA (169.254.0.0/16) addresses?
A) Public Internet routing
B) Automatic self-configuration when DHCP fails
C) Multicast communication
D) VPN tunneling

✔ Correct Answer: B

Reason: APIPA (Automatic Private IP Addressing) allows devices to self-assign an IP address in the 169.254.0.0/16 range when DHCP server is unavailable.

Tag: Normal

---

### Question 185
Domain: Computer Networks
Topic: DNS
Subtopic: Record Types
Difficulty: Medium

Question: Which DNS record type maps a domain name to an IPv4 address?
A) AAAA record
B) CNAME record
C) A record
D) MX record

✔ Correct Answer: C

Reason: A (Address) record maps a domain name to an IPv4 address. AAAA maps to IPv6, CNAME creates aliases, MX specifies mail servers.

Tag: Past Paper

---

### Question 186
Domain: Computer Networks
Topic: DNS
Subtopic: Record Types
Difficulty: Medium

Question: Which DNS record type is used for email server identification?
A) A record
B) CNAME record
C) MX record
D) PTR record

✔ Correct Answer: C

Reason: MX (Mail Exchange) records specify the mail servers responsible for accepting email for a domain, with priority values for multiple servers.

Tag: Normal

---

### Question 187
Domain: Computer Networks
Topic: DNS
Subtopic: Resolution
Difficulty: Hard

Question: In recursive DNS resolution, who performs the iterative queries?
A) Client
B) Local DNS server
C) Root DNS server
D) Authoritative DNS server

✔ Correct Answer: B

Reason: In recursive resolution, the local DNS server performs all iterative queries on behalf of the client, querying root, TLD, and authoritative servers.

Tag: Normal

---

### Question 188
Domain: Computer Networks
Topic: DHCP
Subtopic: Process
Difficulty: Hard

Question: What is the correct order of DHCP messages in the address assignment process?
A) DISCOVER, OFFER, REQUEST, ACK
B) REQUEST, OFFER, DISCOVER, ACK
C) OFFER, DISCOVER, ACK, REQUEST
D) DISCOVER, REQUEST, OFFER, ACK

✔ Correct Answer: A

Reason: DHCP uses DORA process: Client sends DISCOVER (broadcast), server sends OFFER, client sends REQUEST, server sends ACK confirming the lease.

Tag: Past Paper

---

### Question 189
Domain: Computer Networks
Topic: DHCP
Subtopic: Lease Time
Difficulty: Medium

Question: What happens when a DHCP lease expires?
A) The IP is immediately released
B) The client must request renewal or release the IP
C) The IP becomes permanent
D) The network stops working

✔ Correct Answer: B

Reason: When a DHCP lease expires, the client must renew the lease or release the IP address. Typically, clients attempt renewal at 50% of lease time.

Tag: Normal

---

### Question 190
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BOOTP
Difficulty: Hard

Question: How does BOOTP differ from DHCP?
A) BOOTP is faster
B) BOOTP uses static IP assignment, DHCP is dynamic
C) BOOTP is more secure
D) BOOTP works only on wireless

✔ Correct Answer: B

Reason: BOOTP (Bootstrap Protocol) uses static configuration tables for IP assignment, while DHCP provides dynamic allocation with lease management.

Tag: Normal

---

### Question 191
Domain: Computer Networks
Topic: Network Performance
Subtopic: RTT
Difficulty: Easy

Question: What does RTT stand for?
A) Real Time Transfer
B) Round Trip Time
C) Rapid Transmission Technology
D) Remote Terminal Transfer

✔ Correct Answer: B

Reason: RTT (Round Trip Time) is the time it takes for a signal to travel from source to destination and back, important for measuring network latency.

Tag: Normal

---

### Question 192
Domain: Computer Networks
Topic: TCP Features
Subtopic: Flow Control
Difficulty: Medium

Question: Which TCP mechanism prevents the sender from overwhelming the receiver?
A) Congestion control
B) Flow control (sliding window)
C) Error detection
D) Routing

✔ Correct Answer: B

Reason: TCP flow control uses a sliding window mechanism where the receiver advertises its buffer size, preventing the sender from overwhelming it.

Tag: Past Paper

---

### Question 193
Domain: Computer Networks
Topic: TCP Features
Subtopic: Acknowledgment
Difficulty: Hard

Question: What type of acknowledgment does TCP use?
A) Individual acknowledgment
B) Cumulative acknowledgment
C) Negative acknowledgment only
D) No acknowledgment

✔ Correct Answer: B

Reason: TCP uses cumulative acknowledgment where an ACK for sequence number n indicates all bytes up to n-1 have been received correctly.

Tag: Normal

---

### Question 194
Domain: Computer Networks
Topic: UDP Features
Subtopic: Header
Difficulty: Medium

Question: What is the size of a UDP header?
A) 8 bytes
B) 20 bytes
C) 32 bytes
D) 40 bytes

✔ Correct Answer: A

Reason: UDP header is only 8 bytes (source port, destination port, length, checksum), much simpler than TCP's 20-byte minimum header.

Tag: Normal

---

### Question 195
Domain: Computer Networks
Topic: Network Applications
Subtopic: Streaming
Difficulty: Medium

Question: Which protocol is better suited for video streaming?
A) TCP
B) UDP
C) ICMP
D) ARP

✔ Correct Answer: B

Reason: UDP is preferred for video streaming because it's faster and occasional packet loss is acceptable, whereas TCP's retransmissions would cause delays.

Tag: Normal

---

### Question 196
Domain: Computer Networks
Topic: Network Applications
Subtopic: Real-time Communication
Difficulty: Medium

Question: Why is UDP preferred over TCP for VoIP applications?
A) UDP is more reliable
B) UDP has lower latency
C) UDP provides better quality
D) UDP is more secure

✔ Correct Answer: B

Reason: UDP's lower latency and lack of retransmission make it ideal for real-time applications like VoIP where timely delivery is more important than perfect reliability.

Tag: Normal

---

### Question 197
Domain: Computer Networks
Topic: Network Layer
Subtopic: Fragmentation Offset
Difficulty: Hard

Question: In IPv4, the fragmentation offset field is measured in units of:
A) 1 byte
B) 4 bytes
C) 8 bytes
D) 16 bytes

✔ Correct Answer: C

Reason: The fragmentation offset field measures the offset in 8-byte units, allowing the receiver to correctly reassemble fragmented packets.

Tag: Normal

---

### Question 198
Domain: Computer Networks
Topic: Network Layer
Subtopic: IP Options
Difficulty: Hard

Question: Which IPv4 header field indicates the presence of options?
A) Version
B) IHL (Internet Header Length)
C) Type of Service
D) Protocol

✔ Correct Answer: B

Reason: IHL (Internet Header Length) specifies the header length in 32-bit words. If IHL > 5, options are present (minimum header is 20 bytes = 5 words).

Tag: Normal

---

### Question 199
Domain: Computer Networks
Topic: Wireless Standards
Subtopic: 802.11n
Difficulty: Medium

Question: What technology does 802.11n use to increase throughput?
A) Higher frequency only
B) MIMO (Multiple Input Multiple Output)
C) Better encryption
D) Longer range only

✔ Correct Answer: B

Reason: 802.11n uses MIMO technology with multiple antennas to transmit multiple data streams simultaneously, significantly increasing throughput.

Tag: Normal

---

### Question 200
Domain: Computer Networks
Topic: Wireless Standards
Subtopic: Frequency Bands
Difficulty: Easy

Question: Which frequency band has more channels available for Wi-Fi?
A) 2.4 GHz
B) 5 GHz
C) Both have equal channels
D) 900 MHz

✔ Correct Answer: B

Reason: The 5 GHz band has more non-overlapping channels (up to 24) compared to 2.4 GHz (3 non-overlapping channels), reducing interference.

Tag: Normal

---

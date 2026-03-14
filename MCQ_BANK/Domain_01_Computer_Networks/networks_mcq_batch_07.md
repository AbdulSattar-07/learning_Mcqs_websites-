# Computer Networks - MCQ Batch 07
## Questions 601-700

---

### Question 601
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MLD Snooping
Difficulty: Hard

Question: What is MLD snooping?
A) Security monitoring
B) IPv6 multicast optimization like IGMP snooping
C) Encryption method
D) Routing protocol

✔ Correct Answer: B

Reason: MLD snooping is the IPv6 equivalent of IGMP snooping, forwarding IPv6 multicast traffic only to ports with interested listeners.

Tag: Normal

---

### Question 602
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Multicast Address Mapping
Difficulty: Hard

Question: How many IP multicast addresses map to one Ethernet multicast MAC?
A) 1
B) 16
C) 32
D) 64

✔ Correct Answer: C

Reason: Only 23 bits of IP multicast address map to MAC (01:00:5E:0x:xx:xx), so 32 IP addresses (5 bits ambiguous) map to same MAC address.

Tag: Normal

---

### Question 603
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Converged Network
Difficulty: Medium

Question: What is a converged network?
A) Network with single protocol
B) Network carrying multiple traffic types (data, voice, video)
C) Wireless only network
D) Backup network

✔ Correct Answer: B

Reason: Converged networks carry multiple traffic types (data, voice, video, storage) over a single infrastructure, reducing costs and complexity.

Tag: Normal

---


### Question 604
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PoE Standards
Difficulty: Medium

Question: What is the maximum power delivery in PoE (802.3af)?
A) 7.5W
B) 15.4W
C) 30W
D) 60W

✔ Correct Answer: B

Reason: PoE (802.3af) delivers up to 15.4W at the source, with 12.95W available at the device after cable loss. PoE+ (802.3at) provides 30W.

Tag: Normal

---

### Question 605
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PoE Plus
Difficulty: Medium

Question: How much power does PoE+ (802.3at) provide?
A) 15.4W
B) 25.5W
C) 30W
D) 60W

✔ Correct Answer: C

Reason: PoE+ (802.3at) provides up to 30W at the source, with 25.5W available at the device, supporting higher-power devices like PTZ cameras.

Tag: Normal

---

### Question 606
Domain: Computer Networks
Topic: Network Protocols
Subtopic: UPoE
Difficulty: Hard

Question: What is UPoE (Universal PoE)?
A) Standard PoE
B) Cisco proprietary 60W PoE
C) Wireless PoE
D) Low-power PoE

✔ Correct Answer: B

Reason: UPoE is Cisco's proprietary standard delivering up to 60W, supporting high-power devices before 802.3bt standard was finalized.

Tag: Normal

---

### Question 607
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PoE 802.3bt
Difficulty: Hard

Question: What are the two types defined in 802.3bt?
A) Type 1 and 2
B) Type 3 (60W) and Type 4 (100W)
C) Type A and B
D) Class 1 and 2

✔ Correct Answer: B

Reason: 802.3bt defines Type 3 (up to 60W) and Type 4 (up to 100W), using all four pairs in the cable for power delivery.

Tag: Normal

---

### Question 608
Domain: Computer Networks
Topic: Network Design
Subtopic: PoE Planning
Difficulty: Medium

Question: What must be considered when planning PoE deployment?
A) Only device count
B) Total power budget of switch and per-port requirements
C) Only cable length
D) Only switch model

✔ Correct Answer: B

Reason: PoE planning requires calculating total power needs of all devices and ensuring switch power budget is sufficient, considering per-port and total limits.

Tag: Normal

---

### Question 609
Domain: Computer Networks
Topic: Network Protocols
Subtopic: LLDP-MED
Difficulty: Hard

Question: What does LLDP-MED add to standard LLDP?
A) Encryption
B) Extensions for VoIP and media endpoint devices
C) Faster discovery
D) Compression

✔ Correct Answer: B

Reason: LLDP-MED (Media Endpoint Discovery) extends LLDP with capabilities for VoIP phones, including VLAN assignment, PoE management, and QoS configuration.

Tag: Normal

---

### Question 610
Domain: Computer Networks
Topic: Network Security
Subtopic: BPDU Guard
Difficulty: Medium

Question: What does BPDU Guard do?
A) Protects BPDUs from corruption
B) Disables port if BPDU is received
C) Encrypts BPDUs
D) Compresses BPDUs

✔ Correct Answer: B

Reason: BPDU Guard disables ports (err-disabled) if BPDUs are received, protecting against unauthorized switches and STP manipulation on access ports.

Tag: Normal

---

### Question 611
Domain: Computer Networks
Topic: Network Security
Subtopic: Root Guard
Difficulty: Hard

Question: What does Root Guard prevent?
A) Root password attacks
B) Unauthorized switch from becoming root bridge
C) Root access
D) Root directory access

✔ Correct Answer: B

Reason: Root Guard prevents external switches from becoming the STP root bridge by blocking superior BPDUs on designated ports, maintaining intended topology.

Tag: Normal

---

### Question 612
Domain: Computer Networks
Topic: Network Security
Subtopic: Loop Guard
Difficulty: Hard

Question: What problem does Loop Guard address?
A) Physical loops
B) Unidirectional link failures causing loops
C) Routing loops
D) Application loops

✔ Correct Answer: B

Reason: Loop Guard prevents alternate or root ports from becoming designated ports due to loss of BPDUs (unidirectional failure), preventing loops.

Tag: Normal

---

### Question 613
Domain: Computer Networks
Topic: Network Protocols
Subtopic: PortFast
Difficulty: Medium

Question: What does PortFast do?
A) Increases port speed
B) Bypasses STP listening/learning states on access ports
C) Encrypts port traffic
D) Disables ports

✔ Correct Answer: B

Reason: PortFast allows access ports to transition immediately to forwarding state, reducing connection time for end devices that don't cause loops.

Tag: Normal

---

### Question 614
Domain: Computer Networks
Topic: Network Protocols
Subtopic: UplinkFast
Difficulty: Hard

Question: What is UplinkFast used for?
A) Increase uplink speed
B) Fast convergence when direct uplink fails
C) Encrypt uplinks
D) Load balance uplinks

✔ Correct Answer: B

Reason: UplinkFast provides fast convergence (1-3 seconds) when a direct uplink fails by immediately activating a blocked port, used on access layer switches.

Tag: Normal

---

### Question 615
Domain: Computer Networks
Topic: Network Protocols
Subtopic: BackboneFast
Difficulty: Hard

Question: What does BackboneFast optimize?
A) Backbone speed
B) Convergence for indirect link failures
C) Backbone security
D) Backbone capacity

✔ Correct Answer: B

Reason: BackboneFast reduces convergence time from 50 to 30 seconds for indirect link failures by detecting inferior BPDUs and expiring max age timer early.

Tag: Normal

---

### Question 616
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Stacking
Difficulty: Medium

Question: What is switch stacking?
A) Physical stacking only
B) Connecting switches to operate as single logical unit
C) Backup switches
D) Wireless connection

✔ Correct Answer: B

Reason: Switch stacking connects multiple physical switches through stack cables to operate as a single logical switch with unified management.

Tag: Normal

---

### Question 617
Domain: Computer Networks
Topic: Network Architecture
Subtopic: VSS
Difficulty: Hard

Question: What does VSS (Virtual Switching System) provide?
A) Virtual machines
B) Two physical switches operating as one logical switch
C) Software switches only
D) Wireless switching

✔ Correct Answer: B

Reason: VSS combines two physical switches into one logical switch with single management plane, providing redundancy and simplified management.

Tag: Normal

---

### Question 618
Domain: Computer Networks
Topic: Network Architecture
Subtopic: vPC
Difficulty: Hard

Question: What does vPC (Virtual Port Channel) enable?
A) Virtual ports only
B) Device to connect to two switches as single port channel
C) Wireless channels
D) Encrypted channels

✔ Correct Answer: B

Reason: vPC allows a device to form a port channel to two separate switches, providing redundancy without STP blocking while maintaining loop-free topology.

Tag: Normal

---

### Question 619
Domain: Computer Networks
Topic: Network Architecture
Subtopic: MLAG
Difficulty: Hard

Question: What is MLAG (Multi-Chassis Link Aggregation)?
A) Single switch feature
B) Link aggregation across multiple switches
C) Wireless aggregation
D) Bandwidth compression

✔ Correct Answer: B

Reason: MLAG allows link aggregation across multiple physical switches, providing redundancy and active-active links without STP blocking.

Tag: Normal

---

### Question 620
Domain: Computer Networks
Topic: Network Protocols
Subtopic: FHRP Load Balancing
Difficulty: Hard

Question: Which FHRP provides load balancing across multiple routers?
A) HSRP
B) VRRP
C) GLBP
D) None

✔ Correct Answer: C

Reason: GLBP (Gateway Load Balancing Protocol) provides both redundancy and load balancing by distributing traffic across multiple routers using virtual MAC addresses.

Tag: Normal

---

### Question 621
Domain: Computer Networks
Topic: Network Performance
Subtopic: Jitter
Difficulty: Easy

Question: What is jitter in network performance?
A) Packet loss
B) Variation in packet delay
C) Bandwidth fluctuation
D) Signal interference

✔ Correct Answer: B

Reason: Jitter is the variation in packet arrival times, critical for real-time applications like VoIP where consistent timing is important.

Tag: Past Paper

---

### Question 622
Domain: Computer Networks
Topic: Network Performance
Subtopic: Jitter Buffer
Difficulty: Medium

Question: What is the purpose of a jitter buffer?
A) Increase bandwidth
B) Smooth out delay variations in real-time streams
C) Encrypt packets
D) Compress audio

✔ Correct Answer: B

Reason: Jitter buffers temporarily store packets to smooth out delay variations, ensuring consistent playback in real-time applications like VoIP.

Tag: Normal

---

### Question 623
Domain: Computer Networks
Topic: VoIP
Subtopic: Codecs
Difficulty: Medium

Question: What does a codec do in VoIP?
A) Encrypt calls
B) Compress and decompress audio
C) Route calls
D) Authenticate users

✔ Correct Answer: B

Reason: Codecs (coder-decoder) compress audio for transmission and decompress for playback, balancing quality and bandwidth usage.

Tag: Normal

---

### Question 624
Domain: Computer Networks
Topic: VoIP
Subtopic: QoS Requirements
Difficulty: Medium

Question: What is the maximum acceptable latency for good VoIP quality?
A) 50ms
B) 150ms
C) 300ms
D) 500ms

✔ Correct Answer: B

Reason: VoIP requires latency under 150ms for good quality. Above 150ms, conversation quality degrades noticeably. Jitter should be under 30ms.

Tag: Normal

---

### Question 625
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SIP Components
Difficulty: Hard

Question: What is a SIP proxy server?
A) Web proxy
B) Intermediary routing SIP requests
C) DNS server
D) DHCP server

✔ Correct Answer: B

Reason: SIP proxy servers route SIP requests between user agents, providing call routing, load balancing, and policy enforcement in VoIP systems.

Tag: Normal

---

### Question 626
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SIP Registrar
Difficulty: Hard

Question: What does a SIP registrar do?
A) Register domain names
B) Accept REGISTER requests and maintain user location
C) Register IP addresses
D) Register MAC addresses

✔ Correct Answer: B

Reason: SIP registrar accepts REGISTER requests from user agents and maintains a database of user locations (IP addresses) for call routing.

Tag: Normal

---

### Question 627
Domain: Computer Networks
Topic: Network Protocols
Subtopic: H.323
Difficulty: Hard

Question: What is H.323?
A) Video codec
B) Suite of protocols for multimedia communication
C) Audio codec
D) Encryption standard

✔ Correct Answer: B

Reason: H.323 is an ITU standard suite of protocols for multimedia communication over packet networks, predating SIP but more complex.

Tag: Normal

---

### Question 628
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Unified Communications
Difficulty: Medium

Question: What does unified communications integrate?
A) Only voice and video
B) Voice, video, messaging, presence, collaboration
C) Only email and chat
D) Only phone systems

✔ Correct Answer: B

Reason: Unified communications integrates multiple communication methods (voice, video, IM, presence, email, conferencing) into a cohesive system.

Tag: Normal

---

### Question 629
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MGCP
Difficulty: Hard

Question: What is MGCP (Media Gateway Control Protocol)?
A) Peer-to-peer protocol
B) Centralized call control protocol
C) Routing protocol
D) Security protocol

✔ Correct Answer: B

Reason: MGCP uses centralized call control where a call agent controls media gateways, unlike SIP's distributed peer-to-peer model.

Tag: Normal

---

### Question 630
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Megaco/H.248
Difficulty: Hard

Question: What is the relationship between Megaco and H.248?
A) Different protocols
B) Same protocol with different names
C) Megaco replaced H.248
D) Unrelated

✔ Correct Answer: B

Reason: Megaco (IETF) and H.248 (ITU) are the same protocol with different names, used for controlling media gateways in VoIP networks.

Tag: Normal

---

### Question 631
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Network Slicing
Difficulty: Hard

Question: What is network slicing in 5G?
A) Physical network division
B) Creating multiple virtual networks on shared infrastructure
C) Bandwidth reduction
D) Security feature only

✔ Correct Answer: B

Reason: Network slicing creates multiple isolated virtual networks on shared physical infrastructure, each optimized for specific use cases (IoT, video, etc.).

Tag: Normal

---

### Question 632
Domain: Computer Networks
Topic: Mobile Networks
Subtopic: 5G Features
Difficulty: Medium

Question: What is a key feature of 5G compared to 4G?
A) Lower speed
B) Ultra-low latency (1ms)
C) Higher latency
D) Less bandwidth

✔ Correct Answer: B

Reason: 5G provides ultra-low latency (~1ms), massive device connectivity, and higher speeds (up to 20 Gbps) compared to 4G's ~50ms latency.

Tag: Normal

---

### Question 633
Domain: Computer Networks
Topic: Mobile Networks
Subtopic: Handover
Difficulty: Medium

Question: What is handover in mobile networks?
A) Transferring files
B) Transferring connection from one cell to another
C) Handing over control
D) Device replacement

✔ Correct Answer: B

Reason: Handover (handoff) transfers an active connection from one cell tower to another as a mobile device moves, maintaining connectivity.

Tag: Normal

---

### Question 634
Domain: Computer Networks
Topic: Mobile Networks
Subtopic: Roaming
Difficulty: Easy

Question: What is roaming in mobile networks?
A) Walking with phone
B) Using network outside home network area
C) Switching apps
D) Changing phone numbers

✔ Correct Answer: B

Reason: Roaming allows mobile devices to access services through a visited network when outside their home network's coverage area.

Tag: Normal

---

### Question 635
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Small Cell
Difficulty: Medium

Question: What is a small cell in mobile networks?
A) Small phone
B) Low-power cellular base station
C) Small antenna
D) Reduced coverage area only

✔ Correct Answer: B

Reason: Small cells are low-power cellular base stations covering small areas (10m-2km), used to increase capacity and coverage in dense areas.

Tag: Normal

---

### Question 636
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Femtocell
Difficulty: Medium

Question: What is a femtocell?
A) Large cell tower
B) Small cellular base station for home/office
C) Satellite station
D) Wireless router

✔ Correct Answer: B

Reason: Femtocells are very small cellular base stations for home or small office use, connecting to carrier network via broadband, improving indoor coverage.

Tag: Normal

---

### Question 637
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Picocell
Difficulty: Medium

Question: What is the typical coverage range of a picocell?
A) 10-200 meters
B) 1-2 km
C) 5-10 km
D) 20-50 km

✔ Correct Answer: A

Reason: Picocells cover small areas (10-200m), larger than femtocells but smaller than microcells, used in buildings, airports, and stadiums.

Tag: Normal

---

### Question 638
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Macrocell
Difficulty: Easy

Question: What is a macrocell?
A) Small indoor cell
B) Traditional large cell tower
C) Satellite cell
D) Underground cell

✔ Correct Answer: B

Reason: Macrocells are traditional large cellular base stations providing wide area coverage (up to 35km), forming the backbone of mobile networks.

Tag: Normal

---

### Question 639
Domain: Computer Networks
Topic: Network Architecture
Subtopic: HetNet
Difficulty: Hard

Question: What is a HetNet (Heterogeneous Network)?
A) Single cell type network
B) Network mixing macro, micro, pico, and femtocells
C) Wired network only
D) Satellite network

✔ Correct Answer: B

Reason: HetNet combines different cell types (macro, micro, pico, femto) in a coordinated deployment, optimizing coverage, capacity, and user experience.

Tag: Normal

---

### Question 640
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MIMO
Difficulty: Medium

Question: What does MIMO stand for?
A) Multiple Input Multiple Output
B) Managed Input Managed Output
C) Modular Input Modular Output
D) Maximum Input Maximum Output

✔ Correct Answer: A

Reason: MIMO uses multiple antennas at transmitter and receiver to improve communication performance through spatial multiplexing and diversity.

Tag: Normal

---

### Question 641
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Beamforming
Difficulty: Hard

Question: What is beamforming in wireless networks?
A) Creating physical beams
B) Focusing signal toward specific receiver
C) Blocking signals
D) Encrypting signals

✔ Correct Answer: B

Reason: Beamforming uses antenna arrays to focus wireless signals toward specific receivers, improving signal strength, range, and reducing interference.

Tag: Normal

---

### Question 642
Domain: Computer Networks
Topic: Network Protocols
Subtopic: MU-MIMO
Difficulty: Hard

Question: What does MU-MIMO enable?
A) Single user only
B) Simultaneous communication with multiple users
C) Faster single-user speed
D) Better encryption

✔ Correct Answer: B

Reason: MU-MIMO (Multi-User MIMO) allows an access point to communicate with multiple clients simultaneously using spatial multiplexing, improving efficiency.

Tag: Normal

---

### Question 643
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: Channel Width
Difficulty: Medium

Question: What is the standard channel width for 2.4 GHz Wi-Fi?
A) 10 MHz
B) 20 MHz
C) 40 MHz
D) 80 MHz

✔ Correct Answer: B

Reason: Standard 2.4 GHz Wi-Fi uses 20 MHz channels. 40 MHz channels are possible but cause more interference due to limited spectrum.

Tag: Normal

---

### Question 644
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: 5 GHz Channels
Difficulty: Medium

Question: What advantage does 5 GHz band have over 2.4 GHz?
A) Longer range
B) More non-overlapping channels
C) Better wall penetration
D) Lower cost

✔ Correct Answer: B

Reason: 5 GHz band has more spectrum and non-overlapping channels (up to 24), reducing interference, though with shorter range than 2.4 GHz.

Tag: Normal

---

### Question 645
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: DFS
Difficulty: Hard

Question: What is DFS (Dynamic Frequency Selection) in Wi-Fi?
A) Faster frequency switching
B) Avoiding radar interference on 5 GHz channels
C) Selecting best channel automatically
D) Frequency encryption

✔ Correct Answer: B

Reason: DFS is required on certain 5 GHz channels to detect and avoid radar systems, switching channels if radar is detected.

Tag: Normal

---


### Question 646
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: TPC
Difficulty: Hard

Question: What does TPC (Transmit Power Control) do?
A) Increase power always
B) Adjust transmit power to reduce interference
C) Disable transmission
D) Encrypt transmissions

✔ Correct Answer: B

Reason: TPC dynamically adjusts transmit power to minimum needed for reliable communication, reducing interference and power consumption.

Tag: Normal

---

### Question 647
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: Roaming Standards
Difficulty: Hard

Question: Which standard defines fast roaming for Wi-Fi?
A) 802.11r
B) 802.11k
C) 802.11v
D) 802.11w

✔ Correct Answer: A

Reason: 802.11r (Fast BSS Transition) reduces roaming time by pre-authenticating with target AP, critical for voice and video applications.

Tag: Normal

---

### Question 648
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: 802.11k
Difficulty: Hard

Question: What does 802.11k provide?
A) Security
B) Radio resource measurement for better roaming decisions
C) Faster speed
D) Longer range

✔ Correct Answer: B

Reason: 802.11k enables clients to gather information about neighboring APs, making better roaming decisions based on signal strength and load.

Tag: Normal

---

### Question 649
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: 802.11v
Difficulty: Hard

Question: What does 802.11v enable?
A) Video streaming
B) Network-assisted power management and roaming
C) Voice calls
D) Virtual networks

✔ Correct Answer: B

Reason: 802.11v allows network to influence client behavior for power management, load balancing, and roaming, improving overall network performance.

Tag: Normal

---

### Question 650
Domain: Computer Networks
Topic: Wireless Networks
Subtopic: 802.11w
Difficulty: Hard

Question: What does 802.11w protect?
A) Data frames
B) Management frames from spoofing/forgery
C) Control frames
D) All frames equally

✔ Correct Answer: B

Reason: 802.11w (Protected Management Frames) encrypts and authenticates management frames, preventing deauthentication attacks and other management frame exploits.

Tag: Normal

---

### Question 651
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Wireless Controller
Difficulty: Medium

Question: What is the purpose of a wireless LAN controller?
A) Control wired networks
B) Centrally manage multiple access points
C) Control internet access
D) Manage switches

✔ Correct Answer: B

Reason: WLAN controllers centrally manage, configure, and monitor multiple access points, simplifying management and enabling advanced features.

Tag: Normal

---

### Question 652
Domain: Computer Networks
Topic: Wireless Architecture
Subtopic: Autonomous AP
Difficulty: Medium

Question: What characterizes an autonomous access point?
A) Requires controller
B) Standalone with full configuration
C) Cannot work independently
D) Cloud-managed only

✔ Correct Answer: B

Reason: Autonomous APs operate independently with full configuration on each device, unlike lightweight APs that require a controller.

Tag: Normal

---

### Question 653
Domain: Computer Networks
Topic: Wireless Architecture
Subtopic: Lightweight AP
Difficulty: Medium

Question: What is a lightweight access point?
A) Low-weight hardware
B) AP requiring controller for configuration and management
C) Low-power AP
D) Portable AP

✔ Correct Answer: B

Reason: Lightweight APs (LAPs) depend on a wireless controller for configuration and management, with minimal local intelligence, simplifying deployment.

Tag: Normal

---

### Question 654
Domain: Computer Networks
Topic: Wireless Protocols
Subtopic: CAPWAP
Difficulty: Hard

Question: What does CAPWAP protocol do?
A) Encrypt wireless traffic
B) Encapsulate and tunnel traffic between AP and controller
C) Authenticate users
D) Assign channels

✔ Correct Answer: B

Reason: CAPWAP (Control And Provisioning of Wireless Access Points) tunnels traffic between lightweight APs and controllers, enabling centralized management.

Tag: Normal

---

### Question 655
Domain: Computer Networks
Topic: Wireless Protocols
Subtopic: LWAPP
Difficulty: Hard

Question: What is LWAPP?
A) Lightweight application
B) Cisco proprietary predecessor to CAPWAP
C) Linux wireless protocol
D) Low-power protocol

✔ Correct Answer: B

Reason: LWAPP (Lightweight Access Point Protocol) was Cisco's proprietary protocol for AP-controller communication, later standardized as CAPWAP.

Tag: Normal

---

### Question 656
Domain: Computer Networks
Topic: Network Security
Subtopic: WPA3 Features
Difficulty: Hard

Question: What security improvement does WPA3 provide over WPA2?
A) Faster encryption
B) Protection against offline dictionary attacks
C) Longer passwords only
D) No improvements

✔ Correct Answer: B

Reason: WPA3 uses SAE (Simultaneous Authentication of Equals) instead of PSK, protecting against offline dictionary attacks and providing forward secrecy.

Tag: Normal

---

### Question 657
Domain: Computer Networks
Topic: Network Security
Subtopic: SAE
Difficulty: Hard

Question: What does SAE (Simultaneous Authentication of Equals) provide?
A) Faster authentication
B) Secure password-based authentication resistant to offline attacks
C) No password needed
D) Biometric authentication

✔ Correct Answer: B

Reason: SAE (Dragonfly handshake) provides secure password-based authentication that's resistant to offline dictionary attacks, even with weak passwords.

Tag: Normal

---

### Question 658
Domain: Computer Networks
Topic: Network Protocols
Subtopic: OWE
Difficulty: Hard

Question: What does OWE (Opportunistic Wireless Encryption) provide?
A) Maximum security
B) Encryption for open networks without authentication
C) No encryption
D) Password-based encryption

✔ Correct Answer: B

Reason: OWE provides encryption for open Wi-Fi networks without requiring passwords, protecting against passive eavesdropping while maintaining ease of access.

Tag: Normal

---

### Question 659
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Mesh Networks
Difficulty: Medium

Question: What characterizes a wireless mesh network?
A) Single access point
B) APs interconnected wirelessly forming mesh
C) Wired connections only
D) Star topology only

✔ Correct Answer: B

Reason: Wireless mesh networks have APs that wirelessly interconnect, providing redundant paths and extending coverage without running cables to each AP.

Tag: Normal

---

### Question 660
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Mesh Protocols
Difficulty: Hard

Question: Which protocol is used for wireless mesh routing?
A) OSPF
B) HWMP (Hybrid Wireless Mesh Protocol)
C) RIP
D) BGP

✔ Correct Answer: B

Reason: HWMP, defined in 802.11s, combines proactive and reactive routing for wireless mesh networks, optimizing path selection.

Tag: Normal

---

### Question 661
Domain: Computer Networks
Topic: Network Protocols
Subtopic: CoS to DSCP Mapping
Difficulty: Hard

Question: How many CoS values can be mapped to DSCP?
A) 4
B) 8
C) 64
D) 256

✔ Correct Answer: B

Reason: CoS uses 3 bits (8 values: 0-7) in 802.1Q tag. These map to DSCP values for QoS across Layer 2/3 boundaries.

Tag: Normal

---

### Question 662
Domain: Computer Networks
Topic: Network QoS
Subtopic: Trust Boundary
Difficulty: Medium

Question: What is a QoS trust boundary?
A) Security perimeter
B) Point where QoS markings are trusted or remarked
C) Network edge only
D) Firewall location

✔ Correct Answer: B

Reason: Trust boundary defines where QoS markings are trusted. Typically at access layer, markings from end devices are remarked to prevent abuse.

Tag: Normal

---

### Question 663
Domain: Computer Networks
Topic: Network QoS
Subtopic: Classification
Difficulty: Medium

Question: Where should traffic classification ideally occur?
A) Core layer
B) As close to source as possible (access layer)
C) Distribution layer only
D) At destination

✔ Correct Answer: B

Reason: Traffic should be classified and marked as close to the source as possible, allowing consistent QoS treatment throughout the network.

Tag: Normal

---

### Question 664
Domain: Computer Networks
Topic: Network QoS
Subtopic: Marking
Difficulty: Medium

Question: What is the difference between classification and marking?
A) They are the same
B) Classification identifies traffic, marking sets QoS bits
C) Marking is faster
D) Classification is more secure

✔ Correct Answer: B

Reason: Classification identifies traffic types using various criteria (ACLs, NBAR), while marking sets QoS bits (CoS, DSCP) in packet headers.

Tag: Normal

---

### Question 665
Domain: Computer Networks
Topic: Network QoS
Subtopic: Policing vs Shaping
Difficulty: Hard

Question: Where is traffic policing typically applied?
A) Only at source
B) At network boundaries and ingress
C) Only at destination
D) Core only

✔ Correct Answer: B

Reason: Policing is typically applied at network boundaries and ingress points to enforce rate limits, while shaping is used at egress to smooth traffic.

Tag: Normal

---

### Question 666
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Congestion Window
Difficulty: Hard

Question: What limits the sending rate in TCP?
A) Only bandwidth
B) Minimum of congestion window and receiver window
C) Only receiver window
D) Only congestion window

✔ Correct Answer: B

Reason: TCP sending rate is limited by the minimum of congestion window (network capacity) and receiver window (receiver buffer), ensuring flow and congestion control.

Tag: Normal

---

### Question 667
Domain: Computer Networks
Topic: Network Performance
Subtopic: Bandwidth-Delay Product
Difficulty: Hard

Question: What does bandwidth-delay product represent?
A) Total bandwidth
B) Amount of data in flight on the network
C) Delay only
D) Packet loss rate

✔ Correct Answer: B

Reason: BDP = Bandwidth × RTT represents the amount of data that can be in transit, determining optimal TCP window size for full utilization.

Tag: Normal

---

### Question 668
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Throughput
Difficulty: Hard

Question: What primarily limits TCP throughput on high-latency links?
A) Bandwidth only
B) Window size and RTT
C) CPU speed
D) Encryption

✔ Correct Answer: B

Reason: On high-latency links, TCP throughput is limited by window size divided by RTT. Small windows on high-latency links prevent full bandwidth utilization.

Tag: Normal

---

### Question 669
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP Cubic
Difficulty: Hard

Question: What is TCP Cubic?
A) Encryption algorithm
B) Congestion control algorithm
C) Routing protocol
D) Security protocol

✔ Correct Answer: B

Reason: TCP Cubic is a congestion control algorithm optimized for high-bandwidth, high-latency networks, default in Linux, using cubic function for window growth.

Tag: Normal

---

### Question 670
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP BBR
Difficulty: Hard

Question: What does BBR (Bottleneck Bandwidth and RTT) optimize?
A) Security
B) Congestion control based on bottleneck bandwidth
C) Encryption speed
D) Routing

✔ Correct Answer: B

Reason: BBR is Google's congestion control algorithm that models network path to find optimal sending rate, improving performance especially on lossy networks.

Tag: Normal

---


### Question 671
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Content Caching
Difficulty: Medium

Question: Where is content caching most effective?
A) At origin server only
B) Close to end users (edge)
C) In core network only
D) At ISP only

✔ Correct Answer: B

Reason: Caching content close to end users (edge caching) reduces latency, bandwidth usage, and origin server load, improving user experience.

Tag: Normal

---

### Question 672
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP Caching
Difficulty: Medium

Question: Which HTTP header controls caching behavior?
A) Content-Type
B) Cache-Control
C) Accept
D) Host

✔ Correct Answer: B

Reason: Cache-Control header specifies caching directives (max-age, no-cache, no-store, public, private) controlling how responses are cached.

Tag: Normal

---

### Question 673
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ETag
Difficulty: Medium

Question: What is an ETag in HTTP?
A) Encryption tag
B) Identifier for specific version of resource
C) Error tag
D) Expiration tag

✔ Correct Answer: B

Reason: ETag is an identifier for a specific version of a resource, used for cache validation and conditional requests to check if content changed.

Tag: Normal

---

### Question 674
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP Status Codes
Difficulty: Easy

Question: What does HTTP status code 404 indicate?
A) Success
B) Not Found
C) Server Error
D) Redirect

✔ Correct Answer: B

Reason: 404 Not Found indicates the requested resource doesn't exist on the server. It's a client error (4xx) status code.

Tag: Past Paper

---

### Question 675
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP Status Codes
Difficulty: Medium

Question: What does HTTP status code 503 indicate?
A) Not Found
B) Forbidden
C) Service Unavailable
D) Bad Request

✔ Correct Answer: C

Reason: 503 Service Unavailable indicates the server is temporarily unable to handle requests, often due to overload or maintenance.

Tag: Normal

---

### Question 676
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP Methods
Difficulty: Easy

Question: Which HTTP method is idempotent?
A) POST
B) PUT
C) PATCH
D) All methods

✔ Correct Answer: B

Reason: PUT is idempotent (multiple identical requests have same effect as one). POST is not idempotent. GET, DELETE, PUT are idempotent.

Tag: Normal

---

### Question 677
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP/2 Server Push
Difficulty: Hard

Question: What does HTTP/2 server push allow?
A) Client pushing data
B) Server sending resources before client requests them
C) Faster uploads
D) Better encryption

✔ Correct Answer: B

Reason: Server push allows servers to proactively send resources (CSS, JS) to clients before they're requested, reducing page load time.

Tag: Normal

---

### Question 678
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP/2 Header Compression
Difficulty: Hard

Question: Which compression algorithm does HTTP/2 use for headers?
A) GZIP
B) HPACK
C) Deflate
D) Brotli

✔ Correct Answer: B

Reason: HTTP/2 uses HPACK for header compression, reducing overhead from redundant headers across multiple requests on same connection.

Tag: Normal

---

### Question 679
Domain: Computer Networks
Topic: Network Security
Subtopic: HSTS
Difficulty: Medium

Question: What does HSTS (HTTP Strict Transport Security) enforce?
A) HTTP only
B) HTTPS connections only
C) FTP connections
D) No encryption

✔ Correct Answer: B

Reason: HSTS forces browsers to use HTTPS for all connections to a domain, preventing protocol downgrade attacks and cookie hijacking.

Tag: Normal

---

### Question 680
Domain: Computer Networks
Topic: Network Security
Subtopic: Certificate Pinning
Difficulty: Hard

Question: What is certificate pinning?
A) Attaching certificates
B) Associating host with specific certificate or public key
C) Removing certificates
D) Encrypting certificates

✔ Correct Answer: B

Reason: Certificate pinning associates a host with expected certificate or public key, preventing MITM attacks using fraudulent certificates from compromised CAs.

Tag: Normal

---

### Question 681
Domain: Computer Networks
Topic: Network Security
Subtopic: OCSP
Difficulty: Hard

Question: What does OCSP (Online Certificate Status Protocol) check?
A) Certificate expiration only
B) Real-time certificate revocation status
C) Certificate creation date
D) Certificate owner

✔ Correct Answer: B

Reason: OCSP checks if a certificate has been revoked in real-time, providing more current information than CRL (Certificate Revocation List).

Tag: Normal

---

### Question 682
Domain: Computer Networks
Topic: Network Security
Subtopic: OCSP Stapling
Difficulty: Hard

Question: What problem does OCSP stapling solve?
A) Slow encryption
B) Privacy and performance issues of OCSP
C) Certificate storage
D) Key generation

✔ Correct Answer: B

Reason: OCSP stapling has the server obtain and cache OCSP responses, improving privacy (client doesn't contact CA) and performance (reduces requests).

Tag: Normal

---

### Question 683
Domain: Computer Networks
Topic: Network Protocols
Subtopic: mDNS
Difficulty: Medium

Question: What is mDNS (Multicast DNS) used for?
A) Internet DNS
B) Name resolution on local network without DNS server
C) Encrypted DNS
D) Faster DNS

✔ Correct Answer: B

Reason: mDNS enables name resolution on local networks without a DNS server, used by Apple Bonjour and other zero-configuration services.

Tag: Normal

---

### Question 684
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DNS-SD
Difficulty: Hard

Question: What does DNS-SD (DNS Service Discovery) enable?
A) Faster DNS
B) Discovering services on network using DNS records
C) Secure DNS
D) DNS caching

✔ Correct Answer: B

Reason: DNS-SD uses DNS records (PTR, SRV, TXT) to advertise and discover services on a network, working with mDNS for zero-configuration networking.

Tag: Normal

---

### Question 685
Domain: Computer Networks
Topic: Network Protocols
Subtopic: UPnP
Difficulty: Medium

Question: What does UPnP (Universal Plug and Play) enable?
A) USB devices
B) Automatic device discovery and configuration
C) Faster processing
D) Better graphics

✔ Correct Answer: B

Reason: UPnP enables devices to discover each other and establish network services automatically without manual configuration, though with security concerns.

Tag: Normal

---

### Question 686
Domain: Computer Networks
Topic: Network Security
Subtopic: UPnP Security
Difficulty: Medium

Question: What is a security concern with UPnP?
A) Too slow
B) Can be exploited to open firewall ports
C) Too complex
D) Requires passwords

✔ Correct Answer: B

Reason: UPnP allows devices to automatically configure port forwarding, which can be exploited by malware to open firewall ports without user knowledge.

Tag: Normal

---

### Question 687
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SSDP
Difficulty: Hard

Question: What protocol does UPnP use for device discovery?
A) ARP
B) SSDP (Simple Service Discovery Protocol)
C) DNS
D) DHCP

✔ Correct Answer: B

Reason: UPnP uses SSDP over UDP multicast for device discovery and advertisement, allowing devices to announce their presence and services.

Tag: Normal

---

### Question 688
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Anycast DNS
Difficulty: Hard

Question: How does anycast improve DNS performance?
A) Faster encryption
B) Routes queries to nearest DNS server
C) Caches more data
D) Uses more servers

✔ Correct Answer: B

Reason: Anycast DNS uses same IP address on multiple servers globally, routing queries to the nearest server based on routing metrics, reducing latency.

Tag: Normal

---

### Question 689
Domain: Computer Networks
Topic: Network Architecture
Subtopic: GeoDNS
Difficulty: Medium

Question: What does GeoDNS do?
A) Encrypt DNS
B) Return different IP addresses based on client location
C) Faster DNS resolution
D) Block DNS queries

✔ Correct Answer: B

Reason: GeoDNS returns different IP addresses based on the geographic location of the DNS query, directing users to nearest or most appropriate server.

Tag: Normal

---

### Question 690
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DNS Round Robin
Difficulty: Easy

Question: What does DNS round robin provide?
A) Security
B) Simple load distribution across multiple IPs
C) Faster resolution
D) Encryption

✔ Correct Answer: B

Reason: DNS round robin returns multiple A records in rotating order, providing basic load distribution, though without health checking or intelligence.

Tag: Normal

---

### Question 691
Domain: Computer Networks
Topic: Network Protocols
Subtopic: GSLB
Difficulty: Hard

Question: What does GSLB (Global Server Load Balancing) provide?
A) Local load balancing only
B) Intelligent traffic distribution across geographic locations
C) Faster routing
D) Better encryption

✔ Correct Answer: B

Reason: GSLB distributes traffic across geographically dispersed data centers based on health, proximity, and load, providing disaster recovery and optimization.

Tag: Normal

---

### Question 692
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Active-Active
Difficulty: Medium

Question: What characterizes an active-active configuration?
A) One active, one standby
B) All systems actively handling traffic simultaneously
C) Sequential activation
D) Random activation

✔ Correct Answer: B

Reason: Active-active configuration has all systems simultaneously handling traffic, maximizing resource utilization and providing load distribution.

Tag: Normal

---

### Question 693
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Active-Passive
Difficulty: Easy

Question: In active-passive configuration, when does the passive system activate?
A) Always active
B) When active system fails
C) Randomly
D) Never

✔ Correct Answer: B

Reason: In active-passive (active-standby), the passive system remains idle until the active system fails, then takes over to maintain service availability.

Tag: Normal

---

### Question 694
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Keepalive Mechanisms
Difficulty: Medium

Question: What is the purpose of application-level keepalives?
A) Increase speed
B) Detect connection failures and maintain sessions
C) Encrypt connections
D) Compress data

✔ Correct Answer: B

Reason: Application-level keepalives detect connection failures faster than TCP keepalive and maintain sessions through NAT/firewalls that timeout idle connections.

Tag: Normal

---

### Question 695
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Connection Pooling
Difficulty: Medium

Question: What benefit does connection pooling provide?
A) More connections
B) Reuses connections reducing overhead of creating new ones
C) Better security
D) Faster encryption

✔ Correct Answer: B

Reason: Connection pooling maintains a pool of reusable connections, avoiding the overhead of establishing new connections for each request, improving performance.

Tag: Normal

---

### Question 696
Domain: Computer Networks
Topic: Network Performance
Subtopic: HTTP Persistent Connections
Difficulty: Medium

Question: What is the advantage of HTTP persistent connections (keep-alive)?
A) Better security
B) Reuses TCP connection for multiple requests
C) Faster encryption
D) Larger files

✔ Correct Answer: B

Reason: Persistent connections reuse the same TCP connection for multiple HTTP requests, eliminating connection setup overhead and improving performance.

Tag: Normal

---

### Question 697
Domain: Computer Networks
Topic: Network Performance
Subtopic: HTTP Pipelining
Difficulty: Hard

Question: What does HTTP pipelining allow?
A) Parallel connections
B) Multiple requests without waiting for responses
C) Faster encryption
D) Better compression

✔ Correct Answer: B

Reason: HTTP pipelining allows sending multiple requests without waiting for responses, reducing latency. However, it has issues and is largely replaced by HTTP/2 multiplexing.

Tag: Normal

---

### Question 698
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Gateway
Difficulty: Medium

Question: What is the primary function of an API gateway?
A) Network routing
B) Single entry point managing API requests
C) DNS resolution
D) File storage

✔ Correct Answer: B

Reason: API gateway acts as a single entry point for API requests, providing routing, authentication, rate limiting, and protocol translation for backend services.

Tag: Normal

---

### Question 699
Domain: Computer Networks
Topic: Network Security
Subtopic: Rate Limiting
Difficulty: Medium

Question: What is the purpose of rate limiting?
A) Increase speed
B) Control request rate to prevent abuse and overload
C) Encrypt faster
D) Compress data

✔ Correct Answer: B

Reason: Rate limiting restricts the number of requests from a client in a time period, preventing abuse, DDoS attacks, and resource exhaustion.

Tag: Normal

---

### Question 700
Domain: Computer Networks
Topic: Network Security
Subtopic: Token Bucket Rate Limiting
Difficulty: Hard

Question: In token bucket rate limiting, what happens when bucket is empty?
A) Requests are queued
B) Requests are rejected or delayed
C) Bucket refills instantly
D) All requests allowed

✔ Correct Answer: B

Reason: When the token bucket is empty, requests are either rejected (hard limit) or delayed until tokens are available, enforcing the rate limit.

Tag: Normal

---

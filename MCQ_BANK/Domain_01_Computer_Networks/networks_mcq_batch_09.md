# Computer Networks - MCQ Batch 09
## Questions 801-900

---

### Question 801
Domain: Computer Networks
Topic: Network Architecture
Subtopic: CAP Theorem
Difficulty: Hard

Question: What does the CAP theorem state?
A: All three can be achieved
B: Only two of Consistency, Availability, Partition tolerance can be guaranteed
C: Only one can be achieved
D: None can be guaranteed

✔ Correct Answer: B

Reason: CAP theorem states distributed systems can guarantee only two of three: Consistency, Availability, and Partition tolerance. Network partitions force choice between C and A.

Tag: Past Paper

---

### Question 802
Domain: Computer Networks
Topic: Network Architecture
Subtopic: BASE
Difficulty: Hard

Question: What does BASE stand for in distributed systems?
A: Basic Available Soft-state Eventually consistent
B: Basically Available, Soft state, Eventually consistent
C: Best Available System Ever
D: Basic Architecture for System Engineering

✔ Correct Answer: B

Reason: BASE (Basically Available, Soft state, Eventually consistent) is an alternative to ACID, accepting eventual consistency for better availability and partition tolerance.

Tag: Normal

---

### Question 803
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Eventual Consistency
Difficulty: Medium

Question: What is eventual consistency?
A: Immediate consistency
B: System becomes consistent after some time without updates
C: Never consistent
D: Always consistent

✔ Correct Answer: B

Reason: Eventual consistency guarantees that if no new updates are made, all replicas will eventually converge to the same value, trading immediate consistency for availability.

Tag: Normal

---

### Question 804
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Strong Consistency
Difficulty: Medium

Question: What does strong consistency guarantee?
A: Eventual consistency
B: All reads return most recent write immediately
C: No consistency
D: Delayed consistency

✔ Correct Answer: B

Reason: Strong consistency ensures all reads return the most recent write immediately, providing linearizability but potentially sacrificing availability.

Tag: Normal

---

### Question 805
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Quorum
Difficulty: Hard

Question: What is a quorum in distributed systems?
A: Meeting
B: Minimum number of nodes that must agree for operation
C: All nodes
D: Single node

✔ Correct Answer: B

Reason: Quorum is the minimum number of nodes that must participate in an operation for it to succeed, balancing consistency and availability (typically N/2 + 1).

Tag: Normal

---


### Question 806
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Split Brain
Difficulty: Hard

Question: What is split brain in distributed systems?
A: Brain damage
B: Network partition causing multiple nodes to act as primary
C: Load balancing
D: Data replication

✔ Correct Answer: B

Reason: Split brain occurs when network partition causes multiple nodes to believe they're primary, potentially causing data inconsistency. Quorum prevents this.

Tag: Normal

---

### Question 807
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Consensus Algorithms
Difficulty: Hard

Question: What do consensus algorithms like Raft and Paxos achieve?
A: Faster processing
B: Agreement among distributed nodes despite failures
C: Better encryption
D: Load balancing

✔ Correct Answer: B

Reason: Consensus algorithms enable distributed nodes to agree on values despite failures and network issues, crucial for distributed coordination and consistency.

Tag: Normal

---

### Question 808
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Leader Election
Difficulty: Hard

Question: What is leader election in distributed systems?
A: Voting for leaders
B: Process to select one node as coordinator
C: User election
D: Random selection

✔ Correct Answer: B

Reason: Leader election selects one node as coordinator/leader to make decisions, preventing conflicts and ensuring consistency in distributed systems.

Tag: Normal

---

### Question 809
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Distributed Locks
Difficulty: Hard

Question: What are distributed locks used for?
A: Physical locks
B: Coordinating access to shared resources across nodes
C: Security locks
D: File locks only

✔ Correct Answer: B

Reason: Distributed locks coordinate access to shared resources across multiple nodes, preventing concurrent modifications and ensuring consistency.

Tag: Normal

---

### Question 810
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Idempotency
Difficulty: Medium

Question: What does idempotency mean?
A: Same operation multiple times has same effect as once
B: Operations always fail
C: Operations never repeat
D: Random results

✔ Correct Answer: A

Reason: Idempotent operations produce the same result whether executed once or multiple times, crucial for safe retries in distributed systems.

Tag: Normal

---

### Question 811
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Idempotency Keys
Difficulty: Hard

Question: What are idempotency keys used for?
A: Encryption
B: Ensuring duplicate requests are processed only once
C: Authentication
D: Routing

✔ Correct Answer: B

Reason: Idempotency keys uniquely identify requests, allowing servers to detect and ignore duplicate requests, ensuring operations execute only once.

Tag: Normal

---

### Question 812
Domain: Computer Networks
Topic: Network Performance
Subtopic: Cache Invalidation
Difficulty: Medium

Question: What is cache invalidation?
A: Invalid cache
B: Removing or updating stale cached data
C: Disabling cache
D: Cache encryption

✔ Correct Answer: B

Reason: Cache invalidation removes or updates cached data when the source data changes, ensuring cache consistency but adding complexity.

Tag: Normal

---

### Question 813
Domain: Computer Networks
Topic: Network Performance
Subtopic: Cache Strategies
Difficulty: Medium

Question: In write-through caching, when is cache updated?
A: Never
B: Simultaneously with database write
C: After database write
D: Before database write

✔ Correct Answer: B

Reason: Write-through updates cache and database simultaneously, ensuring consistency but with write latency. Write-back updates cache first, database later.

Tag: Normal

---

### Question 814
Domain: Computer Networks
Topic: Network Performance
Subtopic: Cache-Aside
Difficulty: Medium

Question: In cache-aside pattern, who manages the cache?
A: Database
B: Application code
C: Cache server automatically
D: Operating system

✔ Correct Answer: B

Reason: In cache-aside (lazy loading), application code explicitly manages cache: check cache, if miss, load from database and populate cache.

Tag: Normal

---

### Question 815
Domain: Computer Networks
Topic: Network Performance
Subtopic: Read-Through Cache
Difficulty: Medium

Question: How does read-through cache work?
A: Application manages cache
B: Cache automatically loads from database on miss
C: No automatic loading
D: Preloads everything

✔ Correct Answer: B

Reason: Read-through cache automatically loads data from database on cache miss, abstracting cache management from application code.

Tag: Normal

---

### Question 816
Domain: Computer Networks
Topic: Network Performance
Subtopic: Write-Behind Cache
Difficulty: Hard

Question: What is the risk of write-behind (write-back) caching?
A: Too slow
B: Data loss if cache fails before writing to database
C: Too fast
D: No risks

✔ Correct Answer: B

Reason: Write-behind updates cache immediately and database asynchronously. If cache fails before database write, data is lost, trading consistency for performance.

Tag: Normal

---

### Question 817
Domain: Computer Networks
Topic: Network Performance
Subtopic: Cache Eviction
Difficulty: Easy

Question: What is LRU cache eviction policy?
A: Least Recently Used items evicted first
B: Most recently used evicted
C: Random eviction
D: Largest items evicted

✔ Correct Answer: A

Reason: LRU (Least Recently Used) evicts items that haven't been accessed recently, assuming recently accessed items are more likely to be accessed again.

Tag: Normal

---

### Question 818
Domain: Computer Networks
Topic: Network Performance
Subtopic: Cache Eviction Policies
Difficulty: Medium

Question: Which cache eviction policy is simplest to implement?
A: LRU
B: LFU
C: FIFO
D: Random

✔ Correct Answer: C

Reason: FIFO (First In First Out) evicts oldest items regardless of usage, simplest to implement but may evict frequently used items.

Tag: Normal

---

### Question 819
Domain: Computer Networks
Topic: Network Performance
Subtopic: LFU
Difficulty: Medium

Question: What does LFU (Least Frequently Used) eviction track?
A: Recent access time
B: Access frequency count
C: Item size
D: Creation time

✔ Correct Answer: B

Reason: LFU tracks how often items are accessed, evicting least frequently used items, though it may retain old items that were once popular.

Tag: Normal

---

### Question 820
Domain: Computer Networks
Topic: Network Performance
Subtopic: Cache Stampede
Difficulty: Hard

Question: What is cache stampede?
A: Physical damage
B: Multiple requests simultaneously regenerating expired cache
C: Cache overflow
D: Cache deletion

✔ Correct Answer: B

Reason: Cache stampede occurs when many requests simultaneously try to regenerate an expired popular cache item, overwhelming the backend. Locking prevents this.

Tag: Normal

---

### Question 821
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Database Replication
Difficulty: Medium

Question: What is master-slave replication?
A: Equal nodes
B: One primary accepts writes, replicas handle reads
C: All nodes accept writes
D: No replication

✔ Correct Answer: B

Reason: Master-slave (primary-replica) replication has one primary accepting writes, replicating to read-only replicas, simple but primary is bottleneck.

Tag: Normal

---

### Question 822
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Multi-Master Replication
Difficulty: Hard

Question: What challenge does multi-master replication face?
A: Too simple
B: Conflict resolution when same data modified on different masters
C: Too slow
D: No challenges

✔ Correct Answer: B

Reason: Multi-master allows writes on multiple nodes, requiring conflict resolution strategies when same data is modified concurrently on different masters.

Tag: Normal

---

### Question 823
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Synchronous Replication
Difficulty: Medium

Question: What is the trade-off of synchronous replication?
A: No trade-offs
B: Strong consistency but higher latency
C: Fast but inconsistent
D: No consistency

✔ Correct Answer: B

Reason: Synchronous replication waits for replicas to confirm writes, ensuring consistency but increasing write latency. Asynchronous is faster but eventually consistent.

Tag: Normal

---

### Question 824
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Asynchronous Replication
Difficulty: Medium

Question: What is the main risk of asynchronous replication?
A: Too slow
B: Data loss if primary fails before replication
C: Too complex
D: No risks

✔ Correct Answer: B

Reason: Asynchronous replication doesn't wait for replica confirmation. If primary fails before replication completes, recent writes may be lost.

Tag: Normal

---

### Question 825
Domain: Computer Networks
Topic: Network Protocols
Subtopic: WebRTC
Difficulty: Medium

Question: What does WebRTC enable?
A: Web routing
B: Real-time communication in browsers without plugins
C: Web caching
D: Web security

✔ Correct Answer: B

Reason: WebRTC (Web Real-Time Communication) enables peer-to-peer audio, video, and data sharing directly in browsers without plugins or additional software.

Tag: Normal

---

### Question 826
Domain: Computer Networks
Topic: Network Protocols
Subtopic: WebRTC Signaling
Difficulty: Hard

Question: What is signaling in WebRTC?
A: Signal processing
B: Exchanging session information to establish connection
C: Audio signals
D: Network signals

✔ Correct Answer: B

Reason: Signaling exchanges session descriptions (SDP) and ICE candidates between peers to establish WebRTC connection, typically using WebSocket or HTTP.

Tag: Normal

---

### Question 827
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SDP Offer/Answer
Difficulty: Hard

Question: What information does SDP exchange in WebRTC?
A: Security data
B: Media capabilities, codecs, and connection information
C: User data
D: File data

✔ Correct Answer: B

Reason: SDP (Session Description Protocol) exchanges media capabilities, supported codecs, encryption keys, and network information for establishing media sessions.

Tag: Normal

---

### Question 828
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DTLS
Difficulty: Hard

Question: What is DTLS (Datagram TLS)?
A: Database TLS
B: TLS for UDP-based protocols
C: Faster TLS
D: Disabled TLS

✔ Correct Answer: B

Reason: DTLS provides TLS-like security for UDP-based protocols, used by WebRTC and other applications requiring encryption without TCP overhead.

Tag: Normal

---

### Question 829
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SRTP
Difficulty: Hard

Question: What does SRTP (Secure RTP) provide?
A: Faster RTP
B: Encryption and authentication for RTP streams
C: Better compression
D: Lower latency

✔ Correct Answer: B

Reason: SRTP provides encryption, authentication, and integrity for RTP streams, securing voice and video communication against eavesdropping and tampering.

Tag: Normal

---

### Question 830
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Peer-to-Peer
Difficulty: Easy

Question: What characterizes peer-to-peer (P2P) networks?
A: Central server required
B: Nodes act as both clients and servers
C: Hierarchical structure
D: Single point of control

✔ Correct Answer: B

Reason: P2P networks have nodes that act as both clients and servers, sharing resources directly without central coordination, providing scalability and resilience.

Tag: Normal

---

### Question 831
Domain: Computer Networks
Topic: Network Architecture
Subtopic: DHT
Difficulty: Hard

Question: What is DHT (Distributed Hash Table)?
A: Database hash
B: Decentralized key-value store across P2P network
C: Hash function
D: Encryption table

✔ Correct Answer: B

Reason: DHT distributes key-value storage across P2P network nodes, providing decentralized lookup service used in BitTorrent, IPFS, and blockchain.

Tag: Normal

---

### Question 832
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Chord Protocol
Difficulty: Hard

Question: What does Chord protocol provide?
A: Music protocol
B: Efficient DHT lookup in P2P networks
C: Encryption
D: Routing protocol

✔ Correct Answer: B

Reason: Chord is a DHT protocol providing efficient key lookup in P2P networks using consistent hashing and finger tables, achieving O(log N) lookup.

Tag: Normal

---

### Question 833
Domain: Computer Networks
Topic: Network Architecture
Subtopic: BitTorrent
Difficulty: Medium

Question: How does BitTorrent improve download speed?
A: Faster servers
B: Downloading from multiple peers simultaneously
C: Better compression
D: Larger files

✔ Correct Answer: B

Reason: BitTorrent downloads different pieces from multiple peers simultaneously, distributing load and often achieving faster speeds than single-source downloads.

Tag: Normal

---

### Question 834
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Blockchain
Difficulty: Medium

Question: What is a key characteristic of blockchain?
A: Centralized control
B: Immutable distributed ledger
C: Mutable database
D: Single point of failure

✔ Correct Answer: B

Reason: Blockchain is a distributed, immutable ledger where blocks are cryptographically linked, making historical data tamper-evident and providing decentralized trust.

Tag: Normal

---

### Question 835
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Consensus Mechanisms
Difficulty: Hard

Question: What is Proof of Work (PoW) in blockchain?
A: Work certificate
B: Computational puzzle solving for block validation
C: Identity proof
D: Signature verification

✔ Correct Answer: B

Reason: PoW requires solving computationally intensive puzzles to validate blocks, providing security through computational cost but consuming significant energy.

Tag: Normal

---

### Question 836
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Proof of Stake
Difficulty: Hard

Question: How does Proof of Stake differ from Proof of Work?
A: Same mechanism
B: Validators chosen based on stake, not computation
C: Faster always
D: Less secure

✔ Correct Answer: B

Reason: PoS selects validators based on their stake (holdings) rather than computational power, reducing energy consumption while maintaining security.

Tag: Normal

---

### Question 837
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Smart Contracts
Difficulty: Medium

Question: What are smart contracts?
A: Legal contracts
B: Self-executing code on blockchain
C: Paper contracts
D: Contract management software

✔ Correct Answer: B

Reason: Smart contracts are self-executing programs on blockchain that automatically enforce agreement terms when conditions are met, enabling trustless transactions.

Tag: Normal

---

### Question 838
Domain: Computer Networks
Topic: Network Architecture
Subtopic: IPFS
Difficulty: Hard

Question: What does IPFS (InterPlanetary File System) provide?
A: Space communication
B: Content-addressed distributed file system
C: Faster FTP
D: Encrypted storage

✔ Correct Answer: B

Reason: IPFS is a peer-to-peer distributed file system using content addressing (hash-based), providing decentralized, permanent, and censorship-resistant storage.

Tag: Normal

---

### Question 839
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Content Addressing
Difficulty: Hard

Question: How does content addressing differ from location addressing?
A: Same thing
B: Identifies content by hash, not location
C: Faster addressing
D: More secure always

✔ Correct Answer: B

Reason: Content addressing uses cryptographic hash of content as identifier, ensuring integrity and enabling deduplication, unlike location-based URLs.

Tag: Normal

---

### Question 840
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Multipath TCP
Difficulty: Hard

Question: What does Multipath TCP (MPTCP) enable?
A: Multiple protocols
B: Using multiple network paths simultaneously
C: Faster single path
D: Path encryption

✔ Correct Answer: B

Reason: MPTCP allows a TCP connection to use multiple network interfaces/paths simultaneously, improving throughput and resilience for mobile devices.

Tag: Normal

---

### Question 841
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP Hybla
Difficulty: Hard

Question: What does TCP Hybla optimize for?
A: LAN networks
B: High-latency satellite links
C: Low-latency networks
D: Wireless only

✔ Correct Answer: B

Reason: TCP Hybla is designed for high-latency satellite links, modifying congestion control to achieve fairness with terrestrial connections.

Tag: Normal

---

### Question 842
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP Vegas
Difficulty: Hard

Question: How does TCP Vegas detect congestion?
A: Packet loss only
B: Measuring RTT changes before loss occurs
C: Random detection
D: No detection

✔ Correct Answer: B

Reason: TCP Vegas proactively detects congestion by monitoring RTT changes, adjusting window before packet loss occurs, unlike loss-based algorithms.

Tag: Normal

---

### Question 843
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP Westwood
Difficulty: Hard

Question: What does TCP Westwood optimize for?
A: Wired networks only
B: Wireless and high-loss networks
C: Low-latency networks
D: Satellite only

✔ Correct Answer: B

Reason: TCP Westwood estimates bandwidth and adjusts congestion window based on ACK rate, performing better on wireless networks with random losses.

Tag: Normal

---

### Question 844
Domain: Computer Networks
Topic: Network Performance
Subtopic: Bandwidth Estimation
Difficulty: Hard

Question: What is packet pair technique used for?
A: Pairing packets
B: Estimating available bandwidth
C: Encryption
D: Compression

✔ Correct Answer: B

Reason: Packet pair sends two packets back-to-back, measuring arrival time difference to estimate available bandwidth on the path.

Tag: Normal

---

### Question 845
Domain: Computer Networks
Topic: Network Performance
Subtopic: Active Queue Management
Difficulty: Hard

Question: What is active queue management (AQM)?
A: Managing queues manually
B: Proactively dropping packets before buffer fills
C: Passive monitoring
D: Queue encryption

✔ Correct Answer: B

Reason: AQM algorithms (RED, CoDel) proactively drop or mark packets before buffers fill, controlling queue length and reducing latency.

Tag: Normal

---

### Question 846
Domain: Computer Networks
Topic: Network Performance
Subtopic: CoDel
Difficulty: Hard

Question: What does CoDel (Controlled Delay) target?
A: Maximum throughput
B: Keeping queuing delay below target
C: Zero delay
D: Maximum delay

✔ Correct Answer: B

Reason: CoDel targets keeping queuing delay below a threshold (typically 5ms), dropping packets when delay exceeds target, reducing bufferbloat.

Tag: Normal

---

### Question 847
Domain: Computer Networks
Topic: Network Performance
Subtopic: Bufferbloat
Difficulty: Medium

Question: What is bufferbloat?
A: Buffer overflow
B: Excessive buffering causing high latency
C: Buffer underflow
D: Buffer encryption

✔ Correct Answer: B

Reason: Bufferbloat occurs when excessive buffering in network devices causes high latency, particularly affecting real-time applications despite high throughput.

Tag: Normal

---

### Question 848
Domain: Computer Networks
Topic: Network Performance
Subtopic: FQ-CoDel
Difficulty: Hard

Question: What does FQ-CoDel combine?
A: Two encryption methods
B: Fair queuing with CoDel AQM
C: Two routing protocols
D: Two compression methods

✔ Correct Answer: B

Reason: FQ-CoDel combines fair queuing (separating flows) with CoDel (controlling delay), providing both fairness and low latency.

Tag: Normal

---

### Question 849
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ECN in TCP
Difficulty: Hard

Question: How does ECN help TCP?
A: Faster encryption
B: Signals congestion without dropping packets
C: Better routing
D: Compression

✔ Correct Answer: B

Reason: ECN allows routers to mark packets instead of dropping them to signal congestion, enabling TCP to reduce rate without packet loss.

Tag: Normal

---

### Question 850
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Anycast Routing
Difficulty: Hard

Question: How do routers handle anycast addresses?
A: Broadcast to all
B: Route to nearest instance based on routing metrics
C: Random selection
D: Round robin

✔ Correct Answer: B

Reason: Routers treat anycast addresses as unicast, routing to the nearest instance based on routing protocol metrics, providing automatic failover and load distribution.

Tag: Normal

---


### Question 851
Domain: Computer Networks
Topic: Network Security
Subtopic: TLS 1.3 Improvements
Difficulty: Hard

Question: What improvement does TLS 1.3 have over TLS 1.2?
A: Slower handshake
B: Faster handshake (1-RTT) and removed weak ciphers
C: More ciphers
D: No improvements

✔ Correct Answer: B

Reason: TLS 1.3 reduces handshake to 1-RTT (from 2-RTT), removes weak ciphers, and improves security and performance over TLS 1.2.

Tag: Normal

---

### Question 852
Domain: Computer Networks
Topic: Network Security
Subtopic: Perfect Forward Secrecy
Difficulty: Hard

Question: What does Perfect Forward Secrecy (PFS) ensure?
A: Perfect encryption
B: Session keys not compromised if long-term key is compromised
C: Faster encryption
D: No forward secrecy

✔ Correct Answer: B

Reason: PFS uses ephemeral keys for each session, ensuring past sessions remain secure even if long-term private key is later compromised.

Tag: Normal

---

### Question 853
Domain: Computer Networks
Topic: Network Security
Subtopic: Diffie-Hellman
Difficulty: Hard

Question: What does Diffie-Hellman enable?
A: Encryption
B: Secure key exchange over insecure channel
C: Authentication
D: Compression

✔ Correct Answer: B

Reason: Diffie-Hellman allows two parties to establish a shared secret over an insecure channel without transmitting the secret, used for key exchange.

Tag: Normal

---

### Question 854
Domain: Computer Networks
Topic: Network Security
Subtopic: Elliptic Curve Cryptography
Difficulty: Hard

Question: What advantage does ECC have over RSA?
A: Simpler
B: Same security with smaller key sizes
C: Faster always
D: Older technology

✔ Correct Answer: B

Reason: ECC provides equivalent security to RSA with much smaller key sizes (256-bit ECC ≈ 3072-bit RSA), reducing computational overhead.

Tag: Normal

---

### Question 855
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Versioning
Difficulty: Medium

Question: Why is API versioning important?
A: Version control
B: Maintain backward compatibility while evolving API
C: Faster APIs
D: Better security

✔ Correct Answer: B

Reason: API versioning allows introducing changes and new features while maintaining backward compatibility for existing clients, preventing breaking changes.

Tag: Normal

---

### Question 856
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Rate Limiting
Difficulty: Medium

Question: What HTTP status code indicates rate limit exceeded?
A: 403
B: 429 (Too Many Requests)
C: 503
D: 500

✔ Correct Answer: B

Reason: HTTP 429 (Too Many Requests) indicates the client has sent too many requests in a given time period, with Retry-After header suggesting when to retry.

Tag: Normal

---

### Question 857
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Throttling
Difficulty: Medium

Question: What is the difference between rate limiting and throttling?
A: Same thing
B: Rate limiting rejects, throttling delays requests
C: Throttling is faster
D: Rate limiting is newer

✔ Correct Answer: B

Reason: Rate limiting rejects requests exceeding limits, while throttling delays/queues them, allowing processing at controlled rate without rejection.

Tag: Normal

---

### Question 858
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Keys
Difficulty: Easy

Question: What is the primary purpose of API keys?
A: Encryption
B: Identify and authenticate API clients
C: Compression
D: Routing

✔ Correct Answer: B

Reason: API keys identify and authenticate clients, enabling access control, usage tracking, and rate limiting, though less secure than OAuth for user data.

Tag: Normal

---

### Question 859
Domain: Computer Networks
Topic: Network Security
Subtopic: OAuth 2.0
Difficulty: Medium

Question: What does OAuth 2.0 provide?
A: Password sharing
B: Delegated authorization without sharing credentials
C: Encryption
D: Faster authentication

✔ Correct Answer: B

Reason: OAuth 2.0 enables delegated authorization, allowing third-party applications to access resources without sharing user credentials.

Tag: Normal

---

### Question 860
Domain: Computer Networks
Topic: Network Security
Subtopic: OAuth Flows
Difficulty: Hard

Question: Which OAuth 2.0 flow is most secure for server-side applications?
A: Implicit flow
B: Authorization Code flow
C: Password flow
D: Client Credentials

✔ Correct Answer: B

Reason: Authorization Code flow is most secure for server-side apps, using authorization code exchange and client secret, preventing token exposure to browser.

Tag: Normal

---

### Question 861
Domain: Computer Networks
Topic: Network Security
Subtopic: JWT
Difficulty: Medium

Question: What is a JWT (JSON Web Token)?
A: Java Web Token
B: Self-contained token with encoded claims
C: JavaScript Token
D: JSON Transfer

✔ Correct Answer: B

Reason: JWT is a compact, self-contained token containing encoded claims (user info, permissions), signed to prevent tampering, used for stateless authentication.

Tag: Normal

---

### Question 862
Domain: Computer Networks
Topic: Network Security
Subtopic: JWT Structure
Difficulty: Hard

Question: What are the three parts of a JWT?
A: User, Password, Token
B: Header, Payload, Signature
C: Key, Value, Hash
D: Start, Middle, End

✔ Correct Answer: B

Reason: JWT consists of Header (algorithm, type), Payload (claims), and Signature (verification), separated by dots and Base64URL encoded.

Tag: Normal

---

### Question 863
Domain: Computer Networks
Topic: Network Security
Subtopic: Refresh Tokens
Difficulty: Medium

Question: What is the purpose of refresh tokens?
A: Refresh pages
B: Obtain new access tokens without re-authentication
C: Refresh cache
D: Refresh DNS

✔ Correct Answer: B

Reason: Refresh tokens are long-lived tokens used to obtain new short-lived access tokens without requiring user re-authentication, balancing security and UX.

Tag: Normal

---

### Question 864
Domain: Computer Networks
Topic: Network Security
Subtopic: Token Rotation
Difficulty: Hard

Question: What is refresh token rotation?
A: Rotating servers
B: Issuing new refresh token with each use
C: Rotating encryption
D: No rotation

✔ Correct Answer: B

Reason: Refresh token rotation issues a new refresh token each time it's used, invalidating the old one, limiting damage if a token is compromised.

Tag: Normal

---

### Question 865
Domain: Computer Networks
Topic: Network Security
Subtopic: PKCE
Difficulty: Hard

Question: What does PKCE (Proof Key for Code Exchange) prevent?
A: All attacks
B: Authorization code interception attacks
C: DDoS attacks
D: SQL injection

✔ Correct Answer: B

Reason: PKCE prevents authorization code interception attacks in OAuth, particularly important for mobile and single-page applications without client secrets.

Tag: Normal

---

### Question 866
Domain: Computer Networks
Topic: Network Architecture
Subtopic: OpenID Connect
Difficulty: Hard

Question: What does OpenID Connect add to OAuth 2.0?
A: Better authorization
B: Identity layer with ID tokens
C: Faster flow
D: More security

✔ Correct Answer: B

Reason: OpenID Connect adds an identity layer on top of OAuth 2.0, providing ID tokens with user information for authentication, not just authorization.

Tag: Normal

---

### Question 867
Domain: Computer Networks
Topic: Network Security
Subtopic: SAML
Difficulty: Medium

Question: What is SAML primarily used for?
A: Email authentication
B: Enterprise SSO (Single Sign-On)
C: API authentication
D: Database authentication

✔ Correct Answer: B

Reason: SAML (Security Assertion Markup Language) is an XML-based standard for enterprise SSO, exchanging authentication and authorization data between parties.

Tag: Normal

---

### Question 868
Domain: Computer Networks
Topic: Network Security
Subtopic: SSO
Difficulty: Easy

Question: What does SSO (Single Sign-On) enable?
A: Single password
B: One authentication for multiple applications
C: Single user
D: Single server

✔ Correct Answer: B

Reason: SSO allows users to authenticate once and access multiple applications without re-authenticating, improving user experience and security management.

Tag: Normal

---

### Question 869
Domain: Computer Networks
Topic: Network Security
Subtopic: Identity Provider
Difficulty: Medium

Question: What is an Identity Provider (IdP)?
A: ID card provider
B: Service that authenticates users and provides identity assertions
C: Database provider
D: Network provider

✔ Correct Answer: B

Reason: IdP authenticates users and provides identity assertions to service providers, centralizing authentication in SSO and federated identity systems.

Tag: Normal

---

### Question 870
Domain: Computer Networks
Topic: Network Security
Subtopic: Service Provider
Difficulty: Medium

Question: In SSO, what is a Service Provider (SP)?
A: Internet service provider
B: Application trusting IdP for authentication
C: Cloud provider
D: Network provider

✔ Correct Answer: B

Reason: Service Provider is an application that trusts the Identity Provider for user authentication, relying on IdP's assertions about user identity.

Tag: Normal

---

### Question 871
Domain: Computer Networks
Topic: Network Security
Subtopic: MFA
Difficulty: Easy

Question: What does MFA (Multi-Factor Authentication) require?
A: Single factor
B: Multiple independent authentication factors
C: Multiple passwords
D: Multiple users

✔ Correct Answer: B

Reason: MFA requires two or more independent factors (something you know, have, are) for authentication, significantly improving security over passwords alone.

Tag: Past Paper

---

### Question 872
Domain: Computer Networks
Topic: Network Security
Subtopic: TOTP
Difficulty: Medium

Question: What is TOTP (Time-based One-Time Password)?
A: Permanent password
B: Password generated based on current time
C: Random password
D: Encrypted password

✔ Correct Answer: B

Reason: TOTP generates one-time passwords based on current time and shared secret, changing every 30 seconds, used in authenticator apps for MFA.

Tag: Normal

---

### Question 873
Domain: Computer Networks
Topic: Network Security
Subtopic: HOTP
Difficulty: Hard

Question: How does HOTP differ from TOTP?
A: Same thing
B: Counter-based instead of time-based
C: Faster
D: More secure

✔ Correct Answer: B

Reason: HOTP (HMAC-based OTP) uses a counter instead of time, incrementing with each use, requiring synchronization between client and server.

Tag: Normal

---

### Question 874
Domain: Computer Networks
Topic: Network Security
Subtopic: WebAuthn
Difficulty: Hard

Question: What does WebAuthn enable?
A: Web authentication only
B: Passwordless authentication using biometrics or security keys
C: Password management
D: Web authorization

✔ Correct Answer: B

Reason: WebAuthn is a W3C standard enabling passwordless authentication using biometrics, security keys, or platform authenticators, improving security and UX.

Tag: Normal

---

### Question 875
Domain: Computer Networks
Topic: Network Security
Subtopic: FIDO2
Difficulty: Hard

Question: What does FIDO2 consist of?
A: Two passwords
B: WebAuthn and CTAP protocols
C: Two servers
D: Two networks

✔ Correct Answer: B

Reason: FIDO2 combines WebAuthn (browser API) and CTAP (Client to Authenticator Protocol) for passwordless authentication using external authenticators.

Tag: Normal

---


### Question 876
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Session Management
Difficulty: Medium

Question: What is session affinity (sticky sessions)?
A: Session encryption
B: Routing user requests to same backend server
C: Session timeout
D: Session replication

✔ Correct Answer: B

Reason: Session affinity ensures requests from same user go to same backend server, maintaining session state but reducing load balancing effectiveness.

Tag: Normal

---

### Question 877
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Stateless Sessions
Difficulty: Medium

Question: How do stateless sessions work?
A: No sessions
B: Session data stored in client (cookies, JWT)
C: Server stores everything
D: Database stores sessions

✔ Correct Answer: B

Reason: Stateless sessions store session data in client-side tokens (JWT, encrypted cookies), allowing any server to handle requests without server-side storage.

Tag: Normal

---

### Question 878
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Session Store
Difficulty: Medium

Question: What is a centralized session store?
A: Local storage
B: Shared storage (Redis, Memcached) for session data
C: No storage
D: Client storage

✔ Correct Answer: B

Reason: Centralized session stores (Redis, Memcached) allow any server to access session data, enabling load balancing without sticky sessions.

Tag: Normal

---

### Question 879
Domain: Computer Networks
Topic: Network Performance
Subtopic: Database Indexing
Difficulty: Easy

Question: What is the primary purpose of database indexes?
A: Store data
B: Speed up data retrieval
C: Encrypt data
D: Backup data

✔ Correct Answer: B

Reason: Indexes create data structures that speed up data retrieval at the cost of additional storage and slower writes, crucial for query performance.

Tag: Normal

---

### Question 880
Domain: Computer Networks
Topic: Network Performance
Subtopic: Query Optimization
Difficulty: Medium

Question: What is query optimization?
A: Making queries shorter
B: Finding most efficient execution plan for query
C: Caching queries
D: Encrypting queries

✔ Correct Answer: B

Reason: Query optimization analyzes queries and selects the most efficient execution plan considering indexes, statistics, and costs, improving performance.

Tag: Normal

---

### Question 881
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Materialized Views
Difficulty: Hard

Question: What are materialized views?
A: Virtual views
B: Precomputed query results stored physically
C: Regular views
D: Temporary views

✔ Correct Answer: B

Reason: Materialized views store precomputed query results physically, trading storage and freshness for faster query performance on complex aggregations.

Tag: Normal

---

### Question 882
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Database Partitioning
Difficulty: Medium

Question: What is vertical partitioning?
A: Horizontal split
B: Splitting table by columns
C: Splitting by rows
D: No splitting

✔ Correct Answer: B

Reason: Vertical partitioning splits tables by columns, storing different columns in different locations, useful when some columns are accessed more frequently.

Tag: Normal

---

### Question 883
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Horizontal Partitioning
Difficulty: Medium

Question: What is horizontal partitioning?
A: Splitting by columns
B: Splitting table by rows (sharding)
C: No splitting
D: Vertical split

✔ Correct Answer: B

Reason: Horizontal partitioning splits tables by rows, distributing data across multiple databases/tables based on partition key, enabling scaling.

Tag: Normal

---

### Question 884
Domain: Computer Networks
Topic: Network Performance
Subtopic: Connection Multiplexing
Difficulty: Hard

Question: What is connection multiplexing in HTTP/2?
A: Multiple connections
B: Multiple requests/responses over single connection
C: Single request only
D: No multiplexing

✔ Correct Answer: B

Reason: HTTP/2 multiplexing allows multiple concurrent requests and responses over a single TCP connection, eliminating head-of-line blocking at HTTP layer.

Tag: Normal

---

### Question 885
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Domain Sharding
Difficulty: Medium

Question: What was domain sharding used for in HTTP/1.1?
A: Database sharding
B: Overcome browser connection limits per domain
C: Security
D: Faster DNS

✔ Correct Answer: B

Reason: Domain sharding served resources from multiple domains to bypass browser's per-domain connection limit (6-8), less needed with HTTP/2 multiplexing.

Tag: Normal

---

### Question 886
Domain: Computer Networks
Topic: Network Performance
Subtopic: Lazy Loading
Difficulty: Easy

Question: What is lazy loading?
A: Slow loading
B: Loading resources only when needed
C: Loading everything upfront
D: No loading

✔ Correct Answer: B

Reason: Lazy loading defers loading of non-critical resources until they're needed (e.g., images below fold), improving initial page load time.

Tag: Normal

---

### Question 887
Domain: Computer Networks
Topic: Network Performance
Subtopic: Eager Loading
Difficulty: Medium

Question: When is eager loading preferred over lazy loading?
A: Always
B: When data is definitely needed and latency matters
C: Never
D: Random choice

✔ Correct Answer: B

Reason: Eager loading fetches related data upfront when it's definitely needed, avoiding N+1 queries and reducing latency from multiple round trips.

Tag: Normal

---

### Question 888
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Pagination
Difficulty: Easy

Question: What is the purpose of API pagination?
A: Page design
B: Limit response size by returning data in chunks
C: Faster responses
D: Better security

✔ Correct Answer: B

Reason: Pagination divides large result sets into manageable chunks (pages), reducing response size, memory usage, and improving performance.

Tag: Normal

---

### Question 889
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Cursor-Based Pagination
Difficulty: Hard

Question: What advantage does cursor-based pagination have over offset-based?
A: Simpler
B: Consistent results when data changes
C: Faster always
D: No advantages

✔ Correct Answer: B

Reason: Cursor-based pagination uses pointers to specific items, providing consistent results even when data changes, unlike offset which can skip/duplicate items.

Tag: Normal

---

### Question 890
Domain: Computer Networks
Topic: Network Architecture
Subtopic: GraphQL Pagination
Difficulty: Hard

Question: What pagination approach does GraphQL commonly use?
A: Offset-based only
B: Cursor-based (Relay-style connections)
C: No pagination
D: Page numbers only

✔ Correct Answer: B

Reason: GraphQL commonly uses cursor-based pagination with Relay-style connections, providing edges, nodes, and pageInfo for consistent navigation.

Tag: Normal

---

### Question 891
Domain: Computer Networks
Topic: Network Performance
Subtopic: Database Connection Limits
Difficulty: Medium

Question: Why limit database connections?
A: Save money
B: Prevent resource exhaustion on database server
C: Increase speed
D: Better security

✔ Correct Answer: B

Reason: Each connection consumes memory and resources. Limiting connections prevents database server resource exhaustion while connection pooling enables reuse.

Tag: Normal

---

### Question 892
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Circuit Breaker States
Difficulty: Hard

Question: What are the three states in circuit breaker pattern?
A: On, Off, Standby
B: Closed, Open, Half-Open
C: Active, Passive, Idle
D: Start, Stop, Pause

✔ Correct Answer: B

Reason: Circuit breaker has Closed (normal), Open (failing, requests rejected), and Half-Open (testing recovery) states, managing failure gracefully.

Tag: Normal

---

### Question 893
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Timeout Configuration
Difficulty: Medium

Question: What happens if timeouts are too short?
A: Better performance
B: False failures and unnecessary retries
C: Improved reliability
D: No issues

✔ Correct Answer: B

Reason: Too-short timeouts cause false failures, triggering unnecessary retries and potentially overwhelming services. Too-long timeouts delay failure detection.

Tag: Normal

---

### Question 894
Domain: Computer Networks
Topic: Network Performance
Subtopic: Tail Latency
Difficulty: Hard

Question: What is tail latency?
A: Average latency
B: Latency at high percentiles (p95, p99)
C: Minimum latency
D: Median latency

✔ Correct Answer: B

Reason: Tail latency measures latency at high percentiles (p95, p99), representing worst-case user experience, often much higher than average.

Tag: Normal

---

### Question 895
Domain: Computer Networks
Topic: Network Performance
Subtopic: Hedged Requests
Difficulty: Hard

Question: What are hedged requests?
A: Protected requests
B: Sending duplicate request if first is slow
C: Encrypted requests
D: Compressed requests

✔ Correct Answer: B

Reason: Hedged requests send duplicate request to another server if first doesn't respond quickly, reducing tail latency at cost of increased load.

Tag: Normal

---

### Question 896
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Backpressure
Difficulty: Hard

Question: What is backpressure in distributed systems?
A: Physical pressure
B: Downstream signaling upstream to slow down
C: Increased pressure
D: No pressure

✔ Correct Answer: B

Reason: Backpressure allows downstream components to signal upstream to slow down when overwhelmed, preventing buffer overflow and maintaining system stability.

Tag: Normal

---

### Question 897
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Reactive Streams
Difficulty: Hard

Question: What do reactive streams provide?
A: Fast streams
B: Asynchronous stream processing with backpressure
C: Synchronous streams
D: No streams

✔ Correct Answer: B

Reason: Reactive streams provide asynchronous, non-blocking stream processing with backpressure, enabling efficient handling of data flows without overwhelming consumers.

Tag: Normal

---

### Question 898
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Flow Control
Difficulty: Medium

Question: What is the purpose of flow control?
A: Control water flow
B: Prevent sender from overwhelming receiver
C: Increase speed
D: Encryption

✔ Correct Answer: B

Reason: Flow control prevents fast senders from overwhelming slow receivers by regulating transmission rate based on receiver capacity.

Tag: Normal

---

### Question 899
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Congestion Control
Difficulty: Medium

Question: How does congestion control differ from flow control?
A: Same thing
B: Congestion control considers network capacity, flow control receiver capacity
C: Congestion is faster
D: Flow control is newer

✔ Correct Answer: B

Reason: Flow control manages sender-receiver rate based on receiver capacity. Congestion control manages rate based on network capacity to prevent congestion.

Tag: Normal

---

### Question 900
Domain: Computer Networks
Topic: Network Performance
Subtopic: Network Capacity Planning
Difficulty: Medium

Question: What is capacity planning?
A: Planning storage
B: Forecasting resource needs for future growth
C: Current capacity only
D: Random planning

✔ Correct Answer: B

Reason: Capacity planning forecasts future resource requirements based on growth trends, ensuring infrastructure can handle expected load without over-provisioning.

Tag: Normal

---

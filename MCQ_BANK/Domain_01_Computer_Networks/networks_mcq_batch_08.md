# Computer Networks - MCQ Batch 08
## Questions 701-800

---

### Question 701
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Microservices Communication
Difficulty: Medium

Question: Which pattern is commonly used for asynchronous microservices communication?
A: Direct HTTP calls only
B: Message queues and event streaming
C: Shared database
D: File sharing

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Message queues (RabbitMQ, Kafka) and event streaming enable asynchronous, decoupled communication between microservices, improving scalability and resilience.

Tag: Normal

---

### Question 702
Domain: Computer Networks
Topic: Network Protocols
Subtopic: AMQP
Difficulty: Hard

Question: What does AMQP (Advanced Message Queuing Protocol) provide?
A: Email queuing
B: Reliable message queuing with routing and security
C: Web queuing
D: File queuing

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: AMQP is an open standard for message-oriented middleware, providing reliable queuing, routing, security, and interoperability between systems.

Tag: Normal

---

### Question 703
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Event-Driven Architecture
Difficulty: Medium

Question: What characterizes event-driven architecture?
A: Synchronous requests only
B: Components communicate through events
C: Polling-based only
D: Direct coupling

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Event-driven architecture has components that produce and consume events asynchronously, enabling loose coupling and scalability.

Tag: Normal

---

### Question 704
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Kafka
Difficulty: Hard

Question: What type of system is Apache Kafka?
A: Database
B: Distributed event streaming platform
C: Web server
D: Email server

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Kafka is a distributed event streaming platform for high-throughput, fault-tolerant publish-subscribe messaging and stream processing.

Tag: Normal

---

### Question 705
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Circuit Breaker Pattern
Difficulty: Hard

Question: What does the circuit breaker pattern prevent?
A: Electrical issues
B: Cascading failures in distributed systems
C: Network loops
D: Data corruption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Circuit breaker pattern prevents cascading failures by stopping requests to failing services, allowing them to recover and preventing resource exhaustion.

Tag: Normal

---

### Question 706
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Retry Logic
Difficulty: Medium

Question: What is exponential backoff in retry logic?
A: Linear retry intervals
B: Increasing retry intervals exponentially
C: Random retries
D: No retries

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Exponential backoff increases wait time between retries exponentially (1s, 2s, 4s, 8s), preventing overwhelming a recovering service.

Tag: Normal

---

### Question 707
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Bulkhead Pattern
Difficulty: Hard

Question: What does the bulkhead pattern do?
A: Increase speed
B: Isolate resources to prevent total system failure
C: Encrypt data
D: Compress data

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Bulkhead pattern isolates resources (thread pools, connections) for different components, preventing failure in one from exhausting resources for others.

Tag: Normal

---

### Question 708
Domain: Computer Networks
Topic: Network Performance
Subtopic: Connection Timeout
Difficulty: Medium

Question: What is connection timeout?
A: Time to transfer data
B: Maximum time to establish connection
C: Time to close connection
D: Idle timeout

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Connection timeout is the maximum time allowed to establish a connection. If exceeded, the connection attempt fails, preventing indefinite waiting.

Tag: Normal

---

### Question 709
Domain: Computer Networks
Topic: Network Performance
Subtopic: Read Timeout
Difficulty: Medium

Question: What is read timeout?
A: Time to connect
B: Maximum time waiting for data after connection established
C: Time to write data
D: DNS resolution time

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Read timeout is the maximum time to wait for data from the server after connection is established, preventing indefinite blocking on slow responses.

Tag: Normal

---

### Question 710
Domain: Computer Networks
Topic: Network Protocols
Subtopic: gRPC Streaming
Difficulty: Hard

Question: What types of streaming does gRPC support?
A: Unary only
B: Unary, server streaming, client streaming, bidirectional
C: Server streaming only
D: No streaming

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: gRPC supports unary (single request/response), server streaming, client streaming, and bidirectional streaming, providing flexible communication patterns.

Tag: Normal

---

### Question 711
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Protocol Buffers
Difficulty: Hard

Question: What is Protocol Buffers (protobuf)?
A: Network buffer
B: Binary serialization format
C: Encryption protocol
D: Routing protocol

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Protocol Buffers is Google's language-neutral, platform-neutral binary serialization format, more efficient than JSON/XML, used by gRPC.

Tag: Normal

---

### Question 712
Domain: Computer Networks
Topic: Network Protocols
Subtopic: GraphQL
Difficulty: Medium

Question: What advantage does GraphQL have over REST?
A: Faster always
B: Clients specify exactly what data they need
C: Better security
D: Simpler implementation

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: GraphQL allows clients to request exactly the data they need in a single query, avoiding over-fetching and under-fetching issues of REST.

Tag: Normal

---

### Question 713
Domain: Computer Networks
Topic: Network Architecture
Subtopic: BFF Pattern
Difficulty: Hard

Question: What does BFF (Backend for Frontend) pattern provide?
A: Best friend forever
B: Dedicated backend for each frontend type
C: Single backend for all
D: No backend

✔ Correct Answer: B

Reason: BFF pattern creates dedicated backend services for each frontend (web, mobile, IoT), optimizing API design for specific client needs.

Tag: Normal

---

### Question 714
Domain: Computer Networks
Topic: Network Security
Subtopic: CORS
Difficulty: Medium

Question: What does CORS (Cross-Origin Resource Sharing) control?
A: Core routing
B: Cross-domain HTTP requests from browsers
C: Encryption
D: Compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: CORS is a security mechanism that controls which domains can make cross-origin HTTP requests from browsers, preventing unauthorized access.

Tag: Normal

---

### Question 715
Domain: Computer Networks
Topic: Network Security
Subtopic: Same-Origin Policy
Difficulty: Medium

Question: What does the same-origin policy restrict?
A: Same domain access
B: Cross-origin document/script interactions
C: Same protocol only
D: Port access

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Same-origin policy restricts how documents or scripts from one origin can interact with resources from another origin, preventing malicious access.

Tag: Normal

---

### Question 716
Domain: Computer Networks
Topic: Network Security
Subtopic: CSP
Difficulty: Hard

Question: What does CSP (Content Security Policy) prevent?
A: Content theft
B: XSS and code injection attacks
C: DDoS attacks
D: Phishing

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: CSP is a security header that specifies approved sources for content, preventing XSS attacks by blocking unauthorized script execution.

Tag: Normal

---

### Question 717
Domain: Computer Networks
Topic: Network Security
Subtopic: XSS
Difficulty: Medium

Question: What is Cross-Site Scripting (XSS)?
A: Legitimate scripting
B: Injecting malicious scripts into web pages
C: Cross-platform development
D: Faster scripting

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: XSS attacks inject malicious scripts into web pages viewed by other users, potentially stealing cookies, session tokens, or sensitive information.

Tag: Past Paper

---

### Question 718
Domain: Computer Networks
Topic: Network Security
Subtopic: CSRF
Difficulty: Hard

Question: What does CSRF (Cross-Site Request Forgery) exploit?
A: SQL databases
B: User's authenticated session to perform unauthorized actions
C: DNS servers
D: Email servers

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: CSRF tricks authenticated users into executing unwanted actions by exploiting their existing session, requiring anti-CSRF tokens for prevention.

Tag: Normal

---

### Question 719
Domain: Computer Networks
Topic: Network Security
Subtopic: SQL Injection
Difficulty: Medium

Question: What does SQL injection attack target?
A: Network routers
B: Database queries through unsanitized input
C: Email servers
D: DNS servers

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: SQL injection exploits unsanitized user input in SQL queries, potentially allowing attackers to read, modify, or delete database data.

Tag: Normal

---

### Question 720
Domain: Computer Networks
Topic: Network Security
Subtopic: Input Validation
Difficulty: Easy

Question: Why is input validation important?
A: Faster processing
B: Prevent injection attacks and data corruption
C: Better UI
D: Reduced bandwidth

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Input validation ensures data meets expected format and constraints, preventing injection attacks, data corruption, and application errors.

Tag: Normal

---


### Question 721
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Reverse Proxy Benefits
Difficulty: Medium

Question: What security benefit does a reverse proxy provide?
A: Encrypts all data
B: Hides backend server details from clients
C: Blocks all attacks
D: Requires no configuration

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Reverse proxies hide backend server IP addresses and architecture from clients, providing security through obscurity and centralized security controls.

Tag: Normal

---

### Question 722
Domain: Computer Networks
Topic: Network Architecture
Subtopic: SSL Termination
Difficulty: Medium

Question: What is SSL termination at load balancer?
A: Ending SSL support
B: Decrypting SSL at load balancer, forwarding unencrypted to backend
C: Encrypting everything
D: Blocking SSL

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: SSL termination decrypts traffic at the load balancer, reducing CPU load on backend servers and enabling content-based routing.

Tag: Normal

---

### Question 723
Domain: Computer Networks
Topic: Network Architecture
Subtopic: SSL Passthrough
Difficulty: Medium

Question: How does SSL passthrough differ from SSL termination?
A: Faster
B: Encrypted traffic forwarded to backend without decryption
C: More secure always
D: Requires no certificates

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: SSL passthrough forwards encrypted traffic directly to backend servers without decryption, maintaining end-to-end encryption but limiting load balancer capabilities.

Tag: Normal

---

### Question 724
Domain: Computer Networks
Topic: Network Architecture
Subtopic: SSL Bridging
Difficulty: Hard

Question: What is SSL bridging?
A: Connecting SSL servers
B: Decrypt at load balancer, re-encrypt to backend
C: No encryption
D: Bridge SSL versions

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: SSL bridging decrypts traffic at load balancer for inspection/routing, then re-encrypts before forwarding to backend, balancing security and functionality.

Tag: Normal

---

### Question 725
Domain: Computer Networks
Topic: Network Protocols
Subtopic: SNI
Difficulty: Hard

Question: What does SNI (Server Name Indication) enable?
A: Faster DNS
B: Multiple SSL certificates on same IP address
C: Better encryption
D: Automatic certificates

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: SNI allows clients to specify hostname during SSL handshake, enabling servers to present correct certificate when hosting multiple SSL sites on one IP.

Tag: Normal

---

### Question 726
Domain: Computer Networks
Topic: Network Protocols
Subtopic: ALPN
Difficulty: Hard

Question: What does ALPN (Application-Layer Protocol Negotiation) do?
A: Negotiate IP addresses
B: Negotiate application protocol during TLS handshake
C: Negotiate encryption
D: Negotiate ports

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: ALPN negotiates application protocol (HTTP/1.1, HTTP/2, HTTP/3) during TLS handshake, eliminating additional round trips for protocol negotiation.

Tag: Normal

---

### Question 727
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Fast Retransmit
Difficulty: Hard

Question: Why is fast retransmit faster than timeout-based retransmission?
A: Uses faster network
B: Detects loss through duplicate ACKs without waiting for timeout
C: Skips retransmission
D: Uses compression

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Fast retransmit detects loss through three duplicate ACKs (typically ~RTT), much faster than waiting for RTO which can be seconds.

Tag: Normal

---

### Question 728
Domain: Computer Networks
Topic: Network Performance
Subtopic: TCP Spurious Retransmission
Difficulty: Hard

Question: What causes spurious retransmissions in TCP?
A: Packet corruption
B: Premature timeout when packet is delayed not lost
C: Intentional duplication
D: Encryption errors

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Spurious retransmissions occur when RTO expires but the original packet was only delayed, causing unnecessary retransmission and wasting bandwidth.

Tag: Normal

---

### Question 729
Domain: Computer Networks
Topic: Network Protocols
Subtopic: TCP Timestamps
Difficulty: Hard

Question: How do TCP timestamps help with spurious retransmissions?
A: Prevent them completely
B: Detect and ignore duplicate segments
C: Speed up retransmission
D: Encrypt timestamps

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: TCP timestamps help detect spurious retransmissions by identifying duplicate segments, allowing the receiver to ignore them and sender to adjust RTO.

Tag: Normal

---

### Question 730
Domain: Computer Networks
Topic: Network Performance
Subtopic: Head-of-Line Blocking
Difficulty: Hard

Question: What is head-of-line blocking in TCP?
A: Physical blocking
B: Lost packet blocks delivery of subsequent packets
C: Router blocking
D: Firewall blocking

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: TCP's ordered delivery means a lost packet blocks delivery of all subsequent packets until it's retransmitted, even if they arrived successfully.

Tag: Normal

---

### Question 731
Domain: Computer Networks
Topic: Network Protocols
Subtopic: QUIC Streams
Difficulty: Hard

Question: How does QUIC solve head-of-line blocking?
A: Faster retransmission
B: Independent streams within connection
C: No ordering
D: Multiple connections

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: QUIC multiplexes multiple independent streams within a connection. Loss in one stream doesn't block others, eliminating head-of-line blocking.

Tag: Normal

---

### Question 732
Domain: Computer Networks
Topic: Network Protocols
Subtopic: QUIC 0-RTT
Difficulty: Hard

Question: What does QUIC 0-RTT enable?
A: No encryption
B: Sending data in first packet without handshake
C: Slower connection
D: Better security

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: QUIC 0-RTT allows sending application data in the first packet using cached session information, eliminating connection establishment latency.

Tag: Normal

---

### Question 733
Domain: Computer Networks
Topic: Network Security
Subtopic: 0-RTT Replay
Difficulty: Hard

Question: What security risk does 0-RTT have?
A: No encryption
B: Vulnerable to replay attacks
C: Weak encryption
D: No authentication

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: 0-RTT data can be replayed by attackers. Applications must ensure 0-RTT requests are idempotent or implement replay protection.

Tag: Normal

---

### Question 734
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Sidecar Pattern
Difficulty: Hard

Question: What is the sidecar pattern in microservices?
A: Physical placement
B: Helper container deployed alongside main container
C: Backup service
D: Load balancer

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Sidecar pattern deploys a helper container alongside the main application container, handling cross-cutting concerns like logging, monitoring, or proxying.

Tag: Normal

---

### Question 735
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Ambassador Pattern
Difficulty: Hard

Question: What does the ambassador pattern do?
A: Diplomatic functions
B: Proxy for external service communication
C: Authentication only
D: Routing only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Ambassador pattern uses a proxy container to handle communication with external services, providing retry logic, circuit breaking, and monitoring.

Tag: Normal

---

### Question 736
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Adapter Pattern
Difficulty: Hard

Question: What is the adapter pattern in microservices?
A: Hardware adapter
B: Standardizes interface to heterogeneous services
C: Power adapter
D: Network adapter

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Adapter pattern provides a standardized interface to services with different interfaces, enabling consistent monitoring and management.

Tag: Normal

---

### Question 737
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: Observability
Difficulty: Medium

Question: What are the three pillars of observability?
A: Speed, Security, Scalability
B: Metrics, Logs, Traces
C: CPU, Memory, Disk
D: Latency, Throughput, Errors

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Observability relies on three pillars: Metrics (numerical measurements), Logs (event records), and Traces (request flows), providing system insights.

Tag: Normal

---

### Question 738
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: Distributed Tracing
Difficulty: Hard

Question: What does distributed tracing track?
A: Physical locations
B: Request flow across multiple services
C: User locations
D: Network cables

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Distributed tracing tracks requests as they flow through multiple microservices, identifying bottlenecks and failures in distributed systems.

Tag: Normal

---

### Question 739
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: APM
Difficulty: Medium

Question: What does APM (Application Performance Monitoring) focus on?
A: Network hardware only
B: Application performance and user experience
C: Power monitoring
D: Physical monitoring

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: APM monitors application performance, transaction times, error rates, and user experience, helping identify and resolve performance issues.

Tag: Normal

---

### Question 740
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: Synthetic Monitoring
Difficulty: Medium

Question: What is synthetic monitoring?
A: Monitoring fake systems
B: Simulated transactions to test availability and performance
C: Monitoring synthesis
D: Chemical monitoring

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Synthetic monitoring uses automated scripts to simulate user transactions, proactively detecting issues before real users are affected.

Tag: Normal

---

### Question 741
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: RUM
Difficulty: Medium

Question: What does RUM (Real User Monitoring) measure?
A: Simulated users
B: Actual user experience and performance
C: Robot users
D: Random users

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: RUM collects performance data from actual user interactions, providing real-world insights into user experience across different locations and conditions.

Tag: Normal

---

### Question 742
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Blue-Green Deployment
Difficulty: Medium

Question: What is blue-green deployment?
A: Color coding
B: Two identical environments for zero-downtime deployment
C: Network coloring
D: Cable coloring

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Blue-green deployment maintains two identical production environments, switching traffic between them for zero-downtime deployments and easy rollback.

Tag: Normal

---

### Question 743
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Canary Deployment
Difficulty: Medium

Question: What is canary deployment?
A: Bird monitoring
B: Gradual rollout to subset of users before full deployment
C: Instant deployment
D: Backup deployment

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Canary deployment releases new version to a small subset of users first, monitoring for issues before full rollout, reducing risk.

Tag: Normal

---

### Question 744
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Feature Flags
Difficulty: Medium

Question: What do feature flags enable?
A: Network flags
B: Toggle features without deploying new code
C: Security flags
D: Error flags

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Feature flags allow enabling/disabling features at runtime without code deployment, enabling A/B testing, gradual rollouts, and quick rollbacks.

Tag: Normal

---

### Question 745
Domain: Computer Networks
Topic: Network Architecture
Subtopic: A/B Testing
Difficulty: Easy

Question: What is A/B testing?
A: Testing two networks
B: Comparing two versions to determine which performs better
C: Alphabetical testing
D: Testing twice

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: A/B testing shows different versions to different user groups, comparing metrics to determine which version performs better for optimization.

Tag: Normal

---


### Question 746
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Chaos Engineering
Difficulty: Hard

Question: What is chaos engineering?
A: Creating chaos
B: Deliberately injecting failures to test resilience
C: Random testing
D: Disorganized development

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Chaos engineering deliberately introduces failures in production to test system resilience and identify weaknesses before real failures occur.

Tag: Normal

---

### Question 747
Domain: Computer Networks
Topic: Network Performance
Subtopic: Connection Draining
Difficulty: Medium

Question: What is connection draining during deployment?
A: Closing all connections
B: Allowing existing connections to complete before shutdown
C: Draining bandwidth
D: Removing connections

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Connection draining allows in-flight requests to complete before removing a server from rotation, preventing abrupt connection termination.

Tag: Normal

---

### Question 748
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Health Checks
Difficulty: Easy

Question: What is the purpose of health checks in load balancing?
A: Check user health
B: Verify backend servers are operational
C: Check network speed
D: Monitor bandwidth

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Health checks periodically verify backend servers are responding correctly, removing failed servers from rotation to ensure traffic goes to healthy servers.

Tag: Normal

---

### Question 749
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Graceful Degradation
Difficulty: Medium

Question: What is graceful degradation?
A: Slow failure
B: System continues with reduced functionality when components fail
C: Complete shutdown
D: No degradation

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Graceful degradation ensures systems continue operating with reduced functionality when components fail, rather than complete failure.

Tag: Normal

---

### Question 750
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Failover Time
Difficulty: Medium

Question: What is failover time?
A: Time to fail
B: Time to switch from failed to backup system
C: Time between failures
D: Failure duration

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Failover time is the duration required to detect failure and switch to backup system, critical for high-availability requirements.

Tag: Normal

---

### Question 751
Domain: Computer Networks
Topic: Network Performance
Subtopic: Time to First Byte
Difficulty: Medium

Question: What does TTFB (Time to First Byte) measure?
A: Total transfer time
B: Time from request to first byte of response
C: Time to last byte
D: Connection time only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: TTFB measures time from request initiation to receiving the first byte of response, indicating server processing time and network latency.

Tag: Normal

---

### Question 752
Domain: Computer Networks
Topic: Network Performance
Subtopic: Page Load Time
Difficulty: Easy

Question: What factors affect web page load time?
A: HTML size only
B: Network latency, server processing, resource size, rendering
C: Server location only
D: Browser only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Page load time is affected by network latency, DNS resolution, server processing, resource sizes, number of requests, and browser rendering.

Tag: Normal

---

### Question 753
Domain: Computer Networks
Topic: Network Optimization
Subtopic: Minification
Difficulty: Easy

Question: What is code minification?
A: Making code smaller in lines
B: Removing whitespace and comments to reduce file size
C: Encrypting code
D: Compressing images

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Minification removes unnecessary characters (whitespace, comments, long variable names) from code without changing functionality, reducing file size.

Tag: Normal

---

### Question 754
Domain: Computer Networks
Topic: Network Optimization
Subtopic: Bundling
Difficulty: Easy

Question: What is the purpose of bundling JavaScript/CSS files?
A: Better organization
B: Reduce number of HTTP requests
C: Improve security
D: Enable caching only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Bundling combines multiple files into one, reducing HTTP requests and connection overhead, though HTTP/2 multiplexing reduces this need.

Tag: Normal

---

### Question 755
Domain: Computer Networks
Topic: Network Optimization
Subtopic: Code Splitting
Difficulty: Medium

Question: What is code splitting in web applications?
A: Dividing developers
B: Loading only necessary code initially, lazy loading rest
C: Splitting across servers
D: Breaking code randomly

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Code splitting divides application into chunks, loading only essential code initially and lazy loading additional code as needed, improving initial load time.

Tag: Normal

---

### Question 756
Domain: Computer Networks
Topic: Network Optimization
Subtopic: Tree Shaking
Difficulty: Medium

Question: What is tree shaking in JavaScript?
A: Removing trees
B: Eliminating unused code from bundles
C: Organizing code
D: Testing code

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Tree shaking analyzes code to eliminate unused exports and imports, reducing bundle size by including only code that's actually used.

Tag: Normal

---

### Question 757
Domain: Computer Networks
Topic: Network Optimization
Subtopic: Image Optimization
Difficulty: Easy

Question: What is a key strategy for image optimization?
A: Using largest size
B: Responsive images and modern formats (WebP, AVIF)
C: Avoiding images
D: Using only PNG

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Image optimization includes using appropriate sizes, modern formats (WebP, AVIF), compression, and responsive images for different devices.

Tag: Normal

---

### Question 758
Domain: Computer Networks
Topic: Network Protocols
Subtopic: HTTP/2 Prioritization
Difficulty: Hard

Question: What does HTTP/2 stream prioritization enable?
A: Random ordering
B: Specifying importance of resources for optimal loading
C: Encryption priority
D: Server priority only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: HTTP/2 allows clients to specify stream priorities and dependencies, enabling browsers to request critical resources first for faster page rendering.

Tag: Normal

---

### Question 759
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Resource Hints
Difficulty: Medium

Question: What does the "preconnect" resource hint do?
A: Preload content
B: Establish connection before resource is needed
C: Prefetch DNS only
D: Cache resources

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Preconnect establishes early connection (DNS, TCP, TLS) to origin, reducing latency when the resource is actually requested.

Tag: Normal

---

### Question 760
Domain: Computer Networks
Topic: Network Protocols
Subtopic: DNS Prefetch
Difficulty: Easy

Question: What does DNS prefetch do?
A: Fetch all DNS records
B: Resolve domain names before they're needed
C: Cache DNS permanently
D: Block DNS

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: DNS prefetch resolves domain names in advance, reducing DNS lookup latency when resources from those domains are requested.

Tag: Normal

---

### Question 761
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Preload
Difficulty: Medium

Question: What does the "preload" resource hint do?
A: Load all resources
B: Fetch critical resources early in page load
C: Preload images only
D: Preload DNS

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Preload tells browsers to fetch critical resources early in the page load process, ensuring they're available when needed for rendering.

Tag: Normal

---

### Question 762
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Progressive Web Apps
Difficulty: Medium

Question: What is a key feature of Progressive Web Apps (PWA)?
A: Native apps only
B: Work offline using service workers
C: Require app store
D: iOS only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: PWAs use service workers to cache resources and work offline, providing app-like experience through web technologies without app store distribution.

Tag: Normal

---

### Question 763
Domain: Computer Networks
Topic: Network Protocols
Subtopic: Service Workers
Difficulty: Medium

Question: What can service workers do?
A: Manage employees
B: Intercept network requests and cache resources
C: Process payments
D: Manage databases

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Service workers are JavaScript running in background, intercepting network requests, caching resources, enabling offline functionality and push notifications.

Tag: Normal

---

### Question 764
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Edge Functions
Difficulty: Hard

Question: What are edge functions?
A: Functions at network edge devices
B: Serverless functions running at CDN edge locations
C: Router functions
D: Switch functions

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Edge functions are serverless functions deployed at CDN edge locations, enabling dynamic content generation and API responses close to users.

Tag: Normal

---

### Question 765
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Serverless Computing
Difficulty: Medium

Question: What characterizes serverless computing?
A: No servers exist
B: Auto-scaling, pay-per-execution, no server management
C: Dedicated servers
D: Manual scaling

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Serverless abstracts server management, automatically scaling and charging per execution, allowing developers to focus on code not infrastructure.

Tag: Normal

---

### Question 766
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Cold Start
Difficulty: Medium

Question: What is a cold start in serverless?
A: Starting in winter
B: Latency when function instance starts from scratch
C: Fast start
D: Warm start

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Cold start is the initialization latency when a new function instance starts, including loading code and dependencies, affecting first request performance.

Tag: Normal

---

### Question 767
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Function Warm-up
Difficulty: Medium

Question: What is function warm-up in serverless?
A: Heating servers
B: Keeping function instances alive to avoid cold starts
C: Faster execution
D: Better encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Warm-up strategies keep function instances alive or pre-initialize them, reducing cold start latency for time-sensitive applications.

Tag: Normal

---

### Question 768
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Container Orchestration
Difficulty: Medium

Question: What is container orchestration?
A: Music for containers
B: Automated deployment, scaling, and management of containers
C: Manual container management
D: Container storage

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Container orchestration platforms (Kubernetes, Docker Swarm) automate deployment, scaling, networking, and management of containerized applications.

Tag: Normal

---

### Question 769
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Kubernetes Service
Difficulty: Hard

Question: What does a Kubernetes Service provide?
A: Application service
B: Stable endpoint for accessing pods
C: Storage service
D: Security service

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Kubernetes Service provides a stable IP and DNS name for accessing a set of pods, abstracting pod IP changes and providing load balancing.

Tag: Normal

---

### Question 770
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Ingress Controller
Difficulty: Hard

Question: What does a Kubernetes Ingress controller do?
A: Control entry to building
B: Manage external access to services (HTTP/HTTPS routing)
C: Control egress only
D: Block all traffic

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Ingress controller manages external HTTP/HTTPS access to services, providing routing, SSL termination, and load balancing at application layer.

Tag: Normal

---


### Question 771
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Network Policies
Difficulty: Hard

Question: What do Kubernetes Network Policies control?
A: User policies
B: Pod-to-pod communication rules
C: Storage policies
D: Deployment policies

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Network Policies define rules for pod-to-pod communication, implementing micro-segmentation and security controls at the network layer.

Tag: Normal

---

### Question 772
Domain: Computer Networks
Topic: Network Architecture
Subtopic: CNI
Difficulty: Hard

Question: What does CNI (Container Network Interface) define?
A: Container naming
B: Standard for configuring container networking
C: Container images
D: Container storage

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: CNI is a specification and libraries for configuring network interfaces in containers, enabling different networking solutions in orchestration platforms.

Tag: Normal

---

### Question 773
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Overlay Networks
Difficulty: Hard

Question: What is an overlay network in containers?
A: Physical network layer
B: Virtual network built on top of existing network
C: Backup network
D: Wireless network

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Overlay networks create virtual networks on top of physical infrastructure, enabling container communication across hosts using encapsulation (VXLAN, etc.).

Tag: Normal

---

### Question 774
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Service Discovery
Difficulty: Medium

Question: What is service discovery in microservices?
A: Discovering new services
B: Automatically locating service instances
C: Manual configuration
D: DNS only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Service discovery automatically locates service instances in dynamic environments, using registries (Consul, etcd) or DNS for dynamic service location.

Tag: Normal

---

### Question 775
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Service Registry
Difficulty: Medium

Question: What does a service registry maintain?
A: User registrations
B: Database of available service instances and locations
C: Domain registrations
D: Certificate registry

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Service registry maintains a database of available service instances, their locations, and health status, enabling dynamic service discovery.

Tag: Normal

---

### Question 776
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Client-Side Discovery
Difficulty: Hard

Question: In client-side service discovery, who queries the registry?
A: Load balancer
B: Client directly
C: Server
D: Router

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: In client-side discovery, clients query the service registry directly and select an instance, giving clients control but adding complexity.

Tag: Normal

---

### Question 777
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Server-Side Discovery
Difficulty: Hard

Question: In server-side service discovery, what handles registry queries?
A: Client
B: Load balancer or router
C: Database
D: DNS only

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: In server-side discovery, clients request through a load balancer/router that queries the registry and routes to appropriate instance, simplifying clients.

Tag: Normal

---

### Question 778
Domain: Computer Networks
Topic: Network Protocols
Subtopic: gRPC Load Balancing
Difficulty: Hard

Question: Why is gRPC load balancing challenging?
A: Too fast
B: Uses long-lived HTTP/2 connections
C: Too slow
D: No load balancing support

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: gRPC uses long-lived HTTP/2 connections. Traditional L4 load balancers see one connection, requiring L7 load balancing or client-side load balancing.

Tag: Normal

---

### Question 779
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Sidecar Proxy
Difficulty: Hard

Question: What does a sidecar proxy in service mesh do?
A: Physical proxy
B: Intercepts all service traffic for observability and control
C: Backup proxy
D: DNS proxy

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Sidecar proxies intercept all inbound/outbound traffic for a service, providing observability, security, and traffic management without code changes.

Tag: Normal

---

### Question 780
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Control Plane vs Data Plane
Difficulty: Medium

Question: In service mesh, what does the control plane do?
A: Handle all traffic
B: Configure and manage data plane proxies
C: Store data
D: Process requests

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Control plane configures and manages sidecar proxies (data plane), providing policy, telemetry collection, and service discovery without handling actual traffic.

Tag: Normal

---

### Question 781
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Mutual TLS
Difficulty: Hard

Question: What does mutual TLS (mTLS) provide?
A: One-way authentication
B: Both client and server authenticate each other
C: No authentication
D: Faster TLS

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: mTLS requires both client and server to present certificates, providing mutual authentication and ensuring both parties are who they claim to be.

Tag: Normal

---

### Question 782
Domain: Computer Networks
Topic: Network Security
Subtopic: Zero Trust Architecture
Difficulty: Hard

Question: What does zero trust require for every request?
A: Trust internal network
B: Authentication and authorization
C: VPN connection
D: Physical access

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Zero trust requires explicit authentication and authorization for every request, regardless of network location, implementing "never trust, always verify."

Tag: Normal

---

### Question 783
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Traffic Splitting
Difficulty: Medium

Question: What is traffic splitting in service mesh?
A: Physical cable splitting
B: Routing percentage of traffic to different service versions
C: Bandwidth division
D: Packet fragmentation

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Traffic splitting routes a percentage of traffic to different service versions, enabling canary deployments, A/B testing, and gradual rollouts.

Tag: Normal

---

### Question 784
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Fault Injection
Difficulty: Hard

Question: What is fault injection in service mesh?
A: Creating real faults
B: Deliberately introducing delays or errors for testing
C: Fixing faults
D: Detecting faults

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Fault injection deliberately introduces delays, errors, or aborts to test service resilience and failure handling without affecting production systems.

Tag: Normal

---

### Question 785
Domain: Computer Networks
Topic: Network Performance
Subtopic: Request Timeout
Difficulty: Medium

Question: Why are request timeouts important?
A: Save time
B: Prevent indefinite waiting and resource exhaustion
C: Increase speed
D: Better encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Request timeouts prevent clients from waiting indefinitely for responses, freeing resources and allowing faster failure detection and recovery.

Tag: Normal

---

### Question 786
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Retry Budget
Difficulty: Hard

Question: What is a retry budget?
A: Financial budget
B: Limit on retry attempts to prevent retry storms
C: Unlimited retries
D: No retries

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Retry budget limits the percentage of requests that can be retried, preventing retry storms that can overwhelm recovering services.

Tag: Normal

---

### Question 787
Domain: Computer Networks
Topic: Network Performance
Subtopic: Deadline Propagation
Difficulty: Hard

Question: What is deadline propagation in distributed systems?
A: Project deadlines
B: Passing request deadline through service chain
C: Time synchronization
D: Timeout extension

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Deadline propagation passes request deadlines through the service call chain, allowing services to abort work that would exceed the deadline.

Tag: Normal

---

### Question 788
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Saga Pattern
Difficulty: Hard

Question: What does the saga pattern manage?
A: Stories
B: Distributed transactions across microservices
C: User sessions
D: File transfers

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Saga pattern manages distributed transactions as a sequence of local transactions with compensating actions for rollback, maintaining consistency without 2PC.

Tag: Normal

---

### Question 789
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Two-Phase Commit
Difficulty: Hard

Question: What is the main drawback of two-phase commit (2PC)?
A: Too fast
B: Blocking protocol with single point of failure
C: Too simple
D: No drawbacks

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: 2PC is a blocking protocol where participants wait for coordinator. If coordinator fails, participants remain blocked, making it unsuitable for microservices.

Tag: Normal

---

### Question 790
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Event Sourcing
Difficulty: Hard

Question: What is event sourcing?
A: Finding event sources
B: Storing state changes as sequence of events
C: Event logging only
D: Event deletion

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Event sourcing stores all state changes as a sequence of events, enabling audit trails, temporal queries, and rebuilding state from events.

Tag: Normal

---

### Question 791
Domain: Computer Networks
Topic: Network Architecture
Subtopic: CQRS
Difficulty: Hard

Question: What does CQRS (Command Query Responsibility Segregation) separate?
A: Commands and queries into different models
B: Servers and clients
C: Networks and storage
D: Users and admins

D) [Missing option - Please review]

✔ Correct Answer: A

Reason: CQRS separates read (query) and write (command) operations into different models, optimizing each independently for performance and scalability.

Tag: Normal

---

### Question 792
Domain: Computer Networks
Topic: Network Performance
Subtopic: Database Connection Pooling
Difficulty: Medium

Question: Why use database connection pooling?
A: More connections
B: Reuse connections avoiding expensive creation overhead
C: Better security
D: Faster queries

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Database connection pooling maintains reusable connections, avoiding the overhead of creating new connections for each request, improving performance.

Tag: Normal

---

### Question 793
Domain: Computer Networks
Topic: Network Performance
Subtopic: N+1 Query Problem
Difficulty: Hard

Question: What is the N+1 query problem?
A: Math problem
B: One query plus N additional queries in loop
C: Query optimization
D: Query caching

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: N+1 problem occurs when fetching a list (1 query) then fetching related data for each item (N queries), causing performance issues.

Tag: Normal

---

### Question 794
Domain: Computer Networks
Topic: Network Performance
Subtopic: Query Batching
Difficulty: Medium

Question: What is query batching?
A: Running queries in batches
B: Combining multiple queries into single request
C: Delaying queries
D: Caching queries

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Query batching combines multiple queries into a single request, reducing network round trips and improving performance, solving N+1 problems.

Tag: Normal

---

### Question 795
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Data Locality
Difficulty: Medium

Question: What is data locality in distributed systems?
A: Local storage only
B: Processing data close to where it's stored
C: Remote processing only
D: Cloud storage

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Data locality processes data close to where it's stored, reducing network transfer overhead and improving performance in distributed systems.

Tag: Normal

---

### Question 796
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Sharding
Difficulty: Medium

Question: What is database sharding?
A: Breaking databases
B: Horizontal partitioning across multiple databases
C: Vertical partitioning
D: Database backup

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Sharding horizontally partitions data across multiple database instances, distributing load and enabling scaling beyond single server capacity.

Tag: Normal

---

### Question 797
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Consistent Hashing
Difficulty: Hard

Question: What problem does consistent hashing solve?
A: Hash collisions
B: Minimizing remapping when nodes are added/removed
C: Faster hashing
D: Better encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Consistent hashing minimizes key remapping when nodes are added or removed, distributing load evenly while maintaining cache efficiency.

Tag: Normal

---

### Question 798
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Replication Lag
Difficulty: Medium

Question: What is replication lag?
A: Slow replication
B: Time delay between primary and replica data
C: Replication failure
D: Network lag

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Replication lag is the time delay between data written to primary and appearing on replicas, affecting read consistency in distributed databases.

Tag: Normal

---

### Question 799
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Read Replicas
Difficulty: Easy

Question: What is the purpose of read replicas?
A: Backup only
B: Scale read operations by distributing across multiple copies
C: Write scaling
D: Encryption

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Read replicas are copies of the database that handle read queries, distributing read load and improving performance without affecting the primary.

Tag: Normal

---

### Question 800
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Write Scaling
Difficulty: Hard

Question: Which technique helps scale write operations?
A: Read replicas
B: Sharding and partitioning
C: Caching
D: CDN

D) [Missing option - Please review]

✔ Correct Answer: B

Reason: Sharding and partitioning distribute write operations across multiple database instances, enabling write scaling beyond single server capacity.

Tag: Normal

---

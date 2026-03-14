# Computer Networks - MCQ Batch 10
## Questions 901-1000

---

### Question 901
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: SLA
Difficulty: Easy

Question: What does SLA stand for?
A: System Level Agreement
B: Service Level Agreement
C: Software License Agreement
D: Security Level Assessment

✔ Correct Answer: B

Reason: SLA (Service Level Agreement) defines expected service levels (uptime, performance, response time) and consequences if not met.

Tag: Normal

---

### Question 902
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: SLO
Difficulty: Medium

Question: What is an SLO (Service Level Objective)?
A: Same as SLA
B: Specific measurable target within SLA
C: Service location
D: Security objective

✔ Correct Answer: B

Reason: SLO is a specific measurable target (e.g., 99.9% uptime, <200ms latency) within an SLA, defining what success looks like.

Tag: Normal

---

### Question 903
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: SLI
Difficulty: Hard

Question: What is an SLI (Service Level Indicator)?
A: Service location
B: Quantitative measure of service level
C: Service list
D: Security indicator

✔ Correct Answer: B

Reason: SLI is a quantitative measurement (error rate, latency, throughput) used to evaluate if SLOs are being met, forming the basis for SLA compliance.

Tag: Normal

---

### Question 904
Domain: Computer Networks
Topic: Network Monitoring
Subtopic: Error Budget
Difficulty: Hard

Question: What is an error budget?
A: Budget for errors
B: Acceptable amount of downtime/errors based on SLO
C: Error count
D: Budget allocation

✔ Correct Answer: B

Reason: Error budget is the acceptable amount of downtime or errors (100% - SLO), balancing reliability and innovation velocity.

Tag: Normal

---

### Question 905
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Graceful Shutdown
Difficulty: Medium

Question: What is graceful shutdown?
A: Immediate shutdown
B: Completing in-flight requests before stopping
C: Forced shutdown
D: No shutdown

✔ Correct Answer: B

Reason: Graceful shutdown stops accepting new requests while completing existing ones, preventing abrupt connection termination and data loss.

Tag: Normal

---


### Question 906
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Rolling Deployment
Difficulty: Medium

Question: What is rolling deployment?
A: Random deployment
B: Gradually updating instances one or few at a time
C: Instant deployment
D: No deployment

✔ Correct Answer: B

Reason: Rolling deployment updates instances gradually in batches, maintaining service availability while deploying, allowing monitoring and rollback if issues arise.

Tag: Normal

---

### Question 907
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Immutable Infrastructure
Difficulty: Hard

Question: What is immutable infrastructure?
A: Infrastructure that changes
B: Servers replaced rather than updated
C: Permanent infrastructure
D: Unchangeable configuration

✔ Correct Answer: B

Reason: Immutable infrastructure replaces servers with new versions rather than updating them, ensuring consistency and simplifying rollback.

Tag: Normal

---

### Question 908
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Infrastructure as Code
Difficulty: Medium

Question: What is Infrastructure as Code (IaC)?
A: Coding infrastructure
B: Managing infrastructure through code and version control
C: Infrastructure documentation
D: Manual infrastructure

✔ Correct Answer: B

Reason: IaC manages infrastructure through machine-readable files under version control, enabling automation, consistency, and reproducibility.

Tag: Normal

---

### Question 909
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Configuration Drift
Difficulty: Medium

Question: What is configuration drift?
A: Intentional changes
B: Unintended divergence from desired configuration
C: Configuration backup
D: Configuration encryption

✔ Correct Answer: B

Reason: Configuration drift occurs when actual configuration diverges from intended state due to manual changes, causing inconsistencies and issues.

Tag: Normal

---

### Question 910
Domain: Computer Networks
Topic: Network Architecture
Subtopic: GitOps
Difficulty: Hard

Question: What is GitOps?
A: Git operations
B: Using Git as single source of truth for infrastructure
C: Git backup
D: Git security

✔ Correct Answer: B

Reason: GitOps uses Git repositories as single source of truth for infrastructure and application configuration, with automated deployment on Git changes.

Tag: Normal

---

### Question 911
Domain: Computer Networks
Topic: Network Security
Subtopic: Secrets Management
Difficulty: Medium

Question: Why use dedicated secrets management tools?
A: Faster access
B: Secure storage, rotation, and access control for credentials
C: Simpler code
D: Better documentation

✔ Correct Answer: B

Reason: Secrets management tools (Vault, AWS Secrets Manager) provide secure storage, automatic rotation, access control, and audit logging for sensitive credentials.

Tag: Normal

---

### Question 912
Domain: Computer Networks
Topic: Network Security
Subtopic: Encryption at Rest
Difficulty: Easy

Question: What is encryption at rest?
A: Encrypting moving data
B: Encrypting stored data
C: No encryption
D: Partial encryption

✔ Correct Answer: B

Reason: Encryption at rest protects stored data (databases, files, backups) from unauthorized access if storage media is compromised.

Tag: Normal

---

### Question 913
Domain: Computer Networks
Topic: Network Security
Subtopic: Encryption in Transit
Difficulty: Easy

Question: What is encryption in transit?
A: Encrypting stored data
B: Encrypting data during transmission
C: No encryption
D: Partial encryption

✔ Correct Answer: B

Reason: Encryption in transit protects data while being transmitted over networks using TLS/SSL, preventing eavesdropping and tampering.

Tag: Normal

---

### Question 914
Domain: Computer Networks
Topic: Network Security
Subtopic: Key Rotation
Difficulty: Medium

Question: What is key rotation?
A: Physical rotation
B: Periodically changing encryption keys
C: Key backup
D: Key deletion

✔ Correct Answer: B

Reason: Key rotation periodically changes encryption keys, limiting damage from key compromise and meeting compliance requirements.

Tag: Normal

---

### Question 915
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Multi-Tenancy
Difficulty: Medium

Question: What is multi-tenancy?
A: Multiple buildings
B: Multiple customers sharing same infrastructure with isolation
C: Single customer
D: Multiple applications

✔ Correct Answer: B

Reason: Multi-tenancy allows multiple customers (tenants) to share infrastructure while maintaining data isolation and security, improving resource utilization.

Tag: Normal

---

### Question 916
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Tenant Isolation
Difficulty: Hard

Question: What is tenant isolation?
A: Physical separation
B: Ensuring tenants cannot access each other's data
C: Network isolation only
D: No isolation

✔ Correct Answer: B

Reason: Tenant isolation ensures customers in multi-tenant systems cannot access each other's data through logical separation, security controls, and access policies.

Tag: Normal

---

### Question 917
Domain: Computer Networks
Topic: Network Performance
Subtopic: Noisy Neighbor
Difficulty: Medium

Question: What is the noisy neighbor problem?
A: Loud servers
B: One tenant consuming excessive resources affecting others
C: Network noise
D: Physical noise

✔ Correct Answer: B

Reason: Noisy neighbor occurs when one tenant's excessive resource usage degrades performance for other tenants in shared infrastructure.

Tag: Normal

---

### Question 918
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Resource Quotas
Difficulty: Easy

Question: What are resource quotas?
A: Price quotas
B: Limits on resource usage per tenant/user
C: Resource sharing
D: Resource backup

✔ Correct Answer: B

Reason: Resource quotas limit CPU, memory, storage, or API calls per tenant/user, preventing resource exhaustion and ensuring fair sharing.

Tag: Normal

---

### Question 919
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Horizontal Scaling
Difficulty: Easy

Question: What is horizontal scaling?
A: Vertical growth
B: Adding more instances/servers
C: Upgrading existing servers
D: Reducing servers

✔ Correct Answer: B

Reason: Horizontal scaling (scale out) adds more instances to distribute load, providing better fault tolerance than vertical scaling (upgrading single server).

Tag: Normal

---

### Question 920
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Vertical Scaling
Difficulty: Easy

Question: What is vertical scaling?
A: Adding more servers
B: Upgrading existing server resources (CPU, RAM)
C: Removing resources
D: Horizontal growth

✔ Correct Answer: B

Reason: Vertical scaling (scale up) increases resources of existing server, simpler but has limits and creates single point of failure.

Tag: Normal

---

### Question 921
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Auto-Scaling
Difficulty: Medium

Question: What triggers auto-scaling?
A: Manual intervention
B: Metrics like CPU, memory, request rate
C: Time only
D: Random triggers

✔ Correct Answer: B

Reason: Auto-scaling automatically adjusts instance count based on metrics (CPU, memory, request rate, custom metrics), optimizing cost and performance.

Tag: Normal

---

### Question 922
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Predictive Scaling
Difficulty: Hard

Question: What is predictive scaling?
A: Random scaling
B: Scaling based on predicted future load
C: Reactive scaling only
D: No scaling

✔ Correct Answer: B

Reason: Predictive scaling uses machine learning to forecast load and scale proactively, preventing performance degradation during traffic spikes.

Tag: Normal

---

### Question 923
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Scheduled Scaling
Difficulty: Easy

Question: When is scheduled scaling useful?
A: Random times
B: Predictable traffic patterns (business hours, events)
C: Never
D: Always

✔ Correct Answer: B

Reason: Scheduled scaling adjusts capacity based on time schedules for predictable patterns, like scaling up during business hours and down at night.

Tag: Normal

---

### Question 924
Domain: Computer Networks
Topic: Network Performance
Subtopic: Warm Pool
Difficulty: Hard

Question: What is a warm pool in auto-scaling?
A: Heated servers
B: Pre-initialized instances ready for quick activation
C: Active instances
D: Cold instances

✔ Correct Answer: B

Reason: Warm pools maintain pre-initialized instances that can be quickly activated, reducing scale-out time compared to starting from scratch.

Tag: Normal

---

### Question 925
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Stateful vs Stateless
Difficulty: Medium

Question: Why are stateless services easier to scale?
A: Faster processing
B: Any instance can handle any request
C: Better security
D: Lower cost

✔ Correct Answer: B

Reason: Stateless services don't maintain session state, allowing any instance to handle any request, simplifying load balancing and scaling.

Tag: Normal

---

### Question 926
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Sticky Sessions Impact
Difficulty: Medium

Question: What is a drawback of sticky sessions?
A: Better performance
B: Uneven load distribution and scaling complexity
C: Improved security
D: No drawbacks

✔ Correct Answer: B

Reason: Sticky sessions can cause uneven load distribution, complicate auto-scaling, and create issues during instance termination or failure.

Tag: Normal

---

### Question 927
Domain: Computer Networks
Topic: Network Performance
Subtopic: Request Coalescing
Difficulty: Hard

Question: What is request coalescing?
A: Combining requests
B: Merging duplicate concurrent requests into one
C: Splitting requests
D: Delaying requests

✔ Correct Answer: B

Reason: Request coalescing merges multiple concurrent identical requests into a single backend request, reducing load when many clients request same data simultaneously.

Tag: Normal

---

### Question 928
Domain: Computer Networks
Topic: Network Performance
Subtopic: Batch Processing
Difficulty: Easy

Question: When is batch processing preferred over real-time?
A: Always
B: For large volumes where latency is acceptable
C: Never
D: Random choice

✔ Correct Answer: B

Reason: Batch processing is efficient for large data volumes where immediate results aren't needed, trading latency for throughput and resource efficiency.

Tag: Normal

---

### Question 929
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Stream Processing
Difficulty: Medium

Question: What characterizes stream processing?
A: Batch processing
B: Processing data continuously as it arrives
C: Delayed processing
D: No processing

✔ Correct Answer: B

Reason: Stream processing handles data continuously as it arrives in real-time, enabling immediate insights and actions on streaming data.

Tag: Normal

---

### Question 930
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Lambda Architecture
Difficulty: Hard

Question: What does Lambda architecture combine?
A: Two databases
B: Batch and stream processing layers
C: Two networks
D: Two servers

✔ Correct Answer: B

Reason: Lambda architecture combines batch layer (comprehensive, accurate) and speed layer (real-time, approximate) to provide both accuracy and low latency.

Tag: Normal

---

### Question 931
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Kappa Architecture
Difficulty: Hard

Question: How does Kappa architecture differ from Lambda?
A: Same thing
B: Stream processing only, no separate batch layer
C: Batch only
D: No processing

✔ Correct Answer: B

Reason: Kappa architecture uses only stream processing, treating batch as replay of stream, simplifying architecture by eliminating separate batch layer.

Tag: Normal

---

### Question 932
Domain: Computer Networks
Topic: Network Performance
Subtopic: Data Pipeline
Difficulty: Medium

Question: What is a data pipeline?
A: Physical pipe
B: Series of processing steps for data transformation
C: Data storage
D: Data backup

✔ Correct Answer: B

Reason: Data pipeline is a series of processing steps that ingest, transform, and move data from sources to destinations, enabling analytics and insights.

Tag: Normal

---

### Question 933
Domain: Computer Networks
Topic: Network Architecture
Subtopic: ETL
Difficulty: Easy

Question: What does ETL stand for?
A: Encrypt, Transfer, Load
B: Extract, Transform, Load
C: Execute, Test, Launch
D: Export, Transfer, Link

✔ Correct Answer: B

Reason: ETL (Extract, Transform, Load) is a process for extracting data from sources, transforming it to desired format, and loading into destination.

Tag: Normal

---

### Question 934
Domain: Computer Networks
Topic: Network Architecture
Subtopic: ELT
Difficulty: Medium

Question: How does ELT differ from ETL?
A: Same thing
B: Loads raw data first, transforms in destination
C: Faster always
D: More secure

✔ Correct Answer: B

Reason: ELT loads raw data into destination (data lake/warehouse) first, then transforms using destination's processing power, leveraging modern scalable systems.

Tag: Normal

---

### Question 935
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Data Lake
Difficulty: Medium

Question: What is a data lake?
A: Water storage
B: Centralized repository for raw data in native format
C: Structured database only
D: Data backup

✔ Correct Answer: B

Reason: Data lake stores raw data in native format (structured, semi-structured, unstructured) at scale, enabling flexible analysis without predefined schema.

Tag: Normal

---

### Question 936
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Data Warehouse
Difficulty: Easy

Question: What is a data warehouse?
A: Physical warehouse
B: Centralized repository for structured, processed data
C: Raw data storage
D: Temporary storage

✔ Correct Answer: B

Reason: Data warehouse stores structured, processed data optimized for analysis and reporting, using predefined schemas and typically supporting SQL queries.

Tag: Normal

---

### Question 937
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Data Mart
Difficulty: Medium

Question: What is a data mart?
A: Data market
B: Subset of data warehouse for specific business area
C: Complete warehouse
D: Data backup

✔ Correct Answer: B

Reason: Data mart is a focused subset of data warehouse serving specific business unit or function, providing faster queries and simpler access.

Tag: Normal

---

### Question 938
Domain: Computer Networks
Topic: Network Performance
Subtopic: OLTP vs OLAP
Difficulty: Medium

Question: How does OLTP differ from OLAP?
A: Same thing
B: OLTP for transactions, OLAP for analytics
C: OLTP is newer
D: OLAP is faster

✔ Correct Answer: B

Reason: OLTP (Online Transaction Processing) optimizes for fast transactions and updates. OLAP (Online Analytical Processing) optimizes for complex queries and analysis.

Tag: Normal

---

### Question 939
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Star Schema
Difficulty: Hard

Question: What is star schema in data warehousing?
A: Star-shaped network
B: Fact table surrounded by dimension tables
C: Star topology
D: Encryption schema

✔ Correct Answer: B

Reason: Star schema has a central fact table with measurements connected to dimension tables with descriptive attributes, optimizing query performance.

Tag: Normal

---

### Question 940
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Snowflake Schema
Difficulty: Hard

Question: How does snowflake schema differ from star schema?
A: Same thing
B: Dimension tables are normalized into multiple tables
C: Simpler
D: Faster always

✔ Correct Answer: B

Reason: Snowflake schema normalizes dimension tables into multiple related tables, saving storage but requiring more joins, trading space for query complexity.

Tag: Normal

---

### Question 941
Domain: Computer Networks
Topic: Network Performance
Subtopic: Denormalization
Difficulty: Medium

Question: Why denormalize databases?
A: Save space
B: Improve read performance by reducing joins
C: Better security
D: Easier updates

✔ Correct Answer: B

Reason: Denormalization adds redundancy to reduce joins, improving read performance at the cost of storage and update complexity.

Tag: Normal

---

### Question 942
Domain: Computer Networks
Topic: Network Architecture
Subtopic: CQRS Benefits
Difficulty: Hard

Question: What benefit does CQRS provide?
A: Simpler code
B: Optimize read and write models independently
C: Faster always
D: Better security

✔ Correct Answer: B

Reason: CQRS allows optimizing read and write models separately, using different databases or schemas for each, improving performance and scalability.

Tag: Normal

---

### Question 943
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Event Store
Difficulty: Hard

Question: What is an event store?
A: Store events only
B: Database optimized for appending and reading events
C: Regular database
D: Cache

✔ Correct Answer: B

Reason: Event store is a database optimized for append-only event storage and sequential reading, used in event sourcing for storing state changes.

Tag: Normal

---

### Question 944
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Projection
Difficulty: Hard

Question: What is a projection in event sourcing?
A: Future prediction
B: Current state derived from event history
C: Data backup
D: Data encryption

✔ Correct Answer: B

Reason: Projection is a read model built by replaying events, representing current state or specific view of data derived from event history.

Tag: Normal

---

### Question 945
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Snapshot
Difficulty: Medium

Question: Why use snapshots in event sourcing?
A: Photography
B: Avoid replaying all events by storing periodic state
C: Backup only
D: Security

✔ Correct Answer: B

Reason: Snapshots store state at specific points, allowing rebuilding from snapshot plus recent events instead of replaying entire history, improving performance.

Tag: Normal

---

### Question 946
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Outbox Pattern
Difficulty: Hard

Question: What problem does the outbox pattern solve?
A: Email problems
B: Ensuring database changes and message publishing are atomic
C: Storage issues
D: Network issues

✔ Correct Answer: B

Reason: Outbox pattern stores messages in database as part of transaction, then publishes them, ensuring atomicity between database changes and messaging.

Tag: Normal

---

### Question 947
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Change Data Capture
Difficulty: Hard

Question: What is Change Data Capture (CDC)?
A: Capturing photos
B: Tracking and capturing database changes for replication
C: Change management
D: Data backup

✔ Correct Answer: B

Reason: CDC tracks database changes (inserts, updates, deletes) and captures them for replication, analytics, or event streaming without application changes.

Tag: Normal

---

### Question 948
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Webhook
Difficulty: Easy

Question: What is a webhook?
A: Web hook tool
B: HTTP callback for event notifications
C: Web security
D: Web storage

✔ Correct Answer: B

Reason: Webhooks are HTTP callbacks that notify applications of events by sending POST requests to configured URLs, enabling event-driven integrations.

Tag: Normal

---

### Question 949
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Polling vs Webhooks
Difficulty: Medium

Question: What advantage do webhooks have over polling?
A: Simpler
B: Real-time notifications without constant checking
C: More secure
D: Faster always

✔ Correct Answer: B

Reason: Webhooks push notifications immediately when events occur, eliminating polling overhead and latency, though requiring publicly accessible endpoints.

Tag: Normal

---

### Question 950
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Long Polling
Difficulty: Medium

Question: What is long polling?
A: Frequent polling
B: Server holds request until data available or timeout
C: Short polling
D: No polling

✔ Correct Answer: B

Reason: Long polling keeps connection open until server has data or timeout, reducing overhead compared to frequent polling while providing near-real-time updates.

Tag: Normal

---


### Question 951
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Server-Sent Events
Difficulty: Medium

Question: What does SSE (Server-Sent Events) provide?
A: Two-way communication
B: One-way server-to-client push over HTTP
C: Client-to-server only
D: No communication

✔ Correct Answer: B

Reason: SSE enables servers to push updates to clients over HTTP, simpler than WebSocket for one-way communication, with automatic reconnection.

Tag: Normal

---

### Question 952
Domain: Computer Networks
Topic: Network Architecture
Subtopic: WebSocket vs SSE
Difficulty: Medium

Question: When should you use WebSocket over SSE?
A: Never
B: When bidirectional communication is needed
C: Always
D: Random choice

✔ Correct Answer: B

Reason: WebSocket provides full-duplex bidirectional communication, while SSE is server-to-client only. Use WebSocket when clients need to send frequent updates.

Tag: Normal

---

### Question 953
Domain: Computer Networks
Topic: Network Performance
Subtopic: Compression
Difficulty: Easy

Question: What is the trade-off of data compression?
A: No trade-offs
B: Reduced bandwidth for increased CPU usage
C: Increased bandwidth
D: No CPU impact

✔ Correct Answer: B

Reason: Compression reduces bandwidth and transfer time but increases CPU usage for compression/decompression, beneficial when bandwidth is bottleneck.

Tag: Normal

---

### Question 954
Domain: Computer Networks
Topic: Network Performance
Subtopic: Gzip
Difficulty: Easy

Question: What types of content benefit most from gzip compression?
A: Images
B: Text-based content (HTML, CSS, JS, JSON)
C: Videos
D: Already compressed files

✔ Correct Answer: B

Reason: Text-based content compresses well with gzip (50-70% reduction), while images and videos are already compressed and benefit little.

Tag: Normal

---

### Question 955
Domain: Computer Networks
Topic: Network Performance
Subtopic: Brotli
Difficulty: Medium

Question: What advantage does Brotli have over gzip?
A: Faster compression
B: Better compression ratio
C: Simpler
D: Older technology

✔ Correct Answer: B

Reason: Brotli achieves 15-25% better compression than gzip for text content, though with slower compression, widely supported in modern browsers.

Tag: Normal

---

### Question 956
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Gateway Features
Difficulty: Medium

Question: What features do API gateways typically provide?
A: Routing only
B: Routing, authentication, rate limiting, transformation
C: Storage only
D: Encryption only

✔ Correct Answer: B

Reason: API gateways provide routing, authentication, rate limiting, request/response transformation, caching, and monitoring as a single entry point.

Tag: Normal

---

### Question 957
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Backend for Frontend
Difficulty: Hard

Question: Why use separate BFFs for mobile and web?
A: More servers
B: Optimize API for each client's specific needs
C: Better security
D: Faster always

✔ Correct Answer: B

Reason: Separate BFFs allow optimizing API responses for each client type's needs (mobile: less data, web: richer data), improving performance and UX.

Tag: Normal

---

### Question 958
Domain: Computer Networks
Topic: Network Performance
Subtopic: Response Compression
Difficulty: Medium

Question: When should you avoid compressing responses?
A: Always compress
B: For small responses or already compressed content
C: Never compress
D: Random decision

✔ Correct Answer: B

Reason: Compression overhead isn't worth it for small responses (<1KB) or already compressed content (images, videos), potentially increasing latency.

Tag: Normal

---

### Question 959
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Microservices Challenges
Difficulty: Medium

Question: What is a key challenge of microservices architecture?
A: Too simple
B: Distributed system complexity and debugging
C: Too fast
D: No challenges

✔ Correct Answer: B

Reason: Microservices introduce distributed system complexity: network latency, partial failures, distributed debugging, and eventual consistency challenges.

Tag: Normal

---

### Question 960
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Monolith vs Microservices
Difficulty: Medium

Question: What is an advantage of monolithic architecture?
A: Better scaling
B: Simpler development and debugging
C: More flexible
D: Better fault isolation

✔ Correct Answer: B

Reason: Monoliths are simpler to develop, test, and debug with straightforward deployment, though they sacrifice independent scaling and technology flexibility.

Tag: Normal

---

### Question 961
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Service Boundaries
Difficulty: Hard

Question: How should microservice boundaries be defined?
A: Random division
B: Around business capabilities or bounded contexts
C: By technology
D: By team size

✔ Correct Answer: B

Reason: Services should be bounded by business capabilities or domain-driven design bounded contexts, ensuring cohesion and loose coupling.

Tag: Normal

---

### Question 962
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Database per Service
Difficulty: Hard

Question: Why should each microservice have its own database?
A: More databases
B: Ensure loose coupling and independent scaling
C: Better security only
D: Easier management

✔ Correct Answer: B

Reason: Separate databases ensure services are loosely coupled, can scale independently, and choose appropriate database technology for their needs.

Tag: Normal

---

### Question 963
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Shared Database Anti-pattern
Difficulty: Hard

Question: Why is sharing a database between microservices problematic?
A: Too fast
B: Creates tight coupling and coordination overhead
C: Too simple
D: No problems

✔ Correct Answer: B

Reason: Shared databases create tight coupling, prevent independent deployment, cause coordination overhead for schema changes, and limit technology choices.

Tag: Normal

---

### Question 964
Domain: Computer Networks
Topic: Network Performance
Subtopic: Database Connection Pooling Size
Difficulty: Hard

Question: What happens if connection pool is too small?
A: Better performance
B: Requests wait for available connections
C: Faster queries
D: No impact

✔ Correct Answer: B

Reason: Too-small pools cause requests to wait for connections, increasing latency. Too-large pools waste resources and can overwhelm database.

Tag: Normal

---

### Question 965
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Strangler Fig Pattern
Difficulty: Hard

Question: What is the strangler fig pattern?
A: Plant pattern
B: Gradually replacing legacy system with new system
C: Instant replacement
D: No replacement

✔ Correct Answer: B

Reason: Strangler fig pattern gradually replaces legacy system by incrementally building new system around it, routing traffic progressively until legacy is retired.

Tag: Normal

---

### Question 966
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Anti-Corruption Layer
Difficulty: Hard

Question: What does an anti-corruption layer do?
A: Prevent corruption
B: Translate between different domain models
C: Encrypt data
D: Backup data

✔ Correct Answer: B

Reason: Anti-corruption layer translates between different domain models or legacy systems, preventing external models from corrupting internal domain design.

Tag: Normal

---

### Question 967
Domain: Computer Networks
Topic: Network Architecture
Subtopic: API Composition
Difficulty: Hard

Question: What is API composition pattern?
A: Writing APIs
B: Aggregating data from multiple services
C: Single API only
D: API deletion

✔ Correct Answer: B

Reason: API composition aggregates data from multiple services to fulfill a request, though it can cause performance issues with sequential calls.

Tag: Normal

---

### Question 968
Domain: Computer Networks
Topic: Network Performance
Subtopic: Parallel Requests
Difficulty: Medium

Question: What is the benefit of parallel API requests?
A: Sequential processing
B: Reduced total latency by concurrent execution
C: Increased latency
D: No benefit

✔ Correct Answer: B

Reason: Parallel requests execute concurrently, reducing total latency to the slowest request instead of sum of all requests, improving performance.

Tag: Normal

---

### Question 969
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Timeout Hierarchy
Difficulty: Hard

Question: How should timeouts be configured in service chains?
A: All equal
B: Each service timeout < upstream timeout
C: Random values
D: No timeouts

✔ Correct Answer: B

Reason: Each service's timeout should be less than its upstream caller's timeout, ensuring proper error propagation and preventing cascading timeouts.

Tag: Normal

---

### Question 970
Domain: Computer Networks
Topic: Network Performance
Subtopic: Request Deduplication
Difficulty: Hard

Question: What is request deduplication?
A: Removing duplicates from data
B: Detecting and handling duplicate requests
C: Deleting requests
D: Copying requests

✔ Correct Answer: B

Reason: Request deduplication detects duplicate requests (using idempotency keys) and returns cached response, preventing duplicate processing.

Tag: Normal

---

### Question 971
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Saga Compensation
Difficulty: Hard

Question: What are compensating transactions in saga pattern?
A: Payment compensation
B: Undo operations for rollback
C: Bonus transactions
D: Faster transactions

✔ Correct Answer: B

Reason: Compensating transactions undo effects of completed steps when saga fails, providing rollback mechanism in distributed transactions without 2PC.

Tag: Normal

---

### Question 972
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Choreography vs Orchestration
Difficulty: Hard

Question: How does choreography differ from orchestration in sagas?
A: Same thing
B: Choreography is decentralized, orchestration is centralized
C: Choreography is faster
D: Orchestration is simpler

✔ Correct Answer: B

Reason: Choreography has services react to events independently (decentralized), while orchestration uses central coordinator, trading complexity for control.

Tag: Normal

---

### Question 973
Domain: Computer Networks
Topic: Network Performance
Subtopic: Async Processing
Difficulty: Medium

Question: When should you use asynchronous processing?
A: Always
B: For long-running or non-critical operations
C: Never
D: Short operations only

✔ Correct Answer: B

Reason: Async processing is ideal for long-running operations (reports, emails) or non-critical tasks, improving responsiveness by not blocking user requests.

Tag: Normal

---

### Question 974
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Job Queue
Difficulty: Easy

Question: What is a job queue?
A: Employment queue
B: Queue for asynchronous task processing
C: Network queue
D: Print queue

✔ Correct Answer: B

Reason: Job queues store tasks for asynchronous processing by worker processes, enabling background processing and load distribution.

Tag: Normal

---

### Question 975
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Worker Processes
Difficulty: Easy

Question: What do worker processes do?
A: Manage workers
B: Process jobs from queue asynchronously
C: Handle HTTP requests
D: Store data

✔ Correct Answer: B

Reason: Worker processes consume jobs from queues and process them asynchronously, separating long-running tasks from request-response cycle.

Tag: Normal

---

### Question 976
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Dead Letter Queue
Difficulty: Hard

Question: What is a dead letter queue?
A: Mail queue
B: Queue for messages that failed processing
C: Deleted messages
D: Priority queue

✔ Correct Answer: B

Reason: Dead letter queue stores messages that failed processing after retry attempts, enabling investigation and manual handling without losing messages.

Tag: Normal

---

### Question 977
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Message Ordering
Difficulty: Hard

Question: What is required to guarantee message ordering?
A: Fast network
B: Single consumer or partition-based ordering
C: Multiple consumers
D: No requirements

✔ Correct Answer: B

Reason: Guaranteed ordering requires single consumer or partition-based ordering (messages with same key go to same partition/consumer), limiting parallelism.

Tag: Normal

---

### Question 978
Domain: Computer Networks
Topic: Network Architecture
Subtopic: At-Least-Once Delivery
Difficulty: Hard

Question: What does at-least-once delivery guarantee?
A: Exactly one delivery
B: Message delivered one or more times
C: No delivery
D: At most once

✔ Correct Answer: B

Reason: At-least-once delivery ensures messages are delivered but may be duplicated, requiring idempotent processing to handle duplicates correctly.

Tag: Normal

---

### Question 979
Domain: Computer Networks
Topic: Network Architecture
Subtopic: At-Most-Once Delivery
Difficulty: Hard

Question: What does at-most-once delivery guarantee?
A: Multiple deliveries
B: Message delivered zero or one time, no duplicates
C: Exactly once
D: At least once

✔ Correct Answer: B

Reason: At-most-once delivery ensures no duplicates but messages may be lost, suitable when occasional loss is acceptable but duplicates are problematic.

Tag: Normal

---

### Question 980
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Exactly-Once Delivery
Difficulty: Hard

Question: Why is exactly-once delivery difficult?
A: Too easy
B: Requires coordination between delivery and processing
C: Too fast
D: Not useful

✔ Correct Answer: B

Reason: Exactly-once requires atomic delivery and processing, difficult in distributed systems. Often achieved through idempotency with at-least-once delivery.

Tag: Normal

---

### Question 981
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Message Acknowledgment
Difficulty: Medium

Question: When should messages be acknowledged?
A: Immediately on receipt
B: After successful processing
C: Before processing
D: Never

✔ Correct Answer: B

Reason: Messages should be acknowledged after successful processing, not on receipt, ensuring messages aren't lost if processing fails.

Tag: Normal

---

### Question 982
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Prefetch Count
Difficulty: Hard

Question: What does prefetch count control in message queues?
A: Fetch speed
B: Number of unacknowledged messages consumer can have
C: Message size
D: Queue size

✔ Correct Answer: B

Reason: Prefetch count limits unacknowledged messages per consumer, balancing throughput (higher prefetch) and fair distribution (lower prefetch).

Tag: Normal

---

### Question 983
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Message TTL
Difficulty: Medium

Question: What is message TTL (Time To Live)?
A: Message lifetime
B: Maximum time message can stay in queue
C: Processing time
D: Delivery time

✔ Correct Answer: B

Reason: Message TTL defines maximum time a message can remain in queue before expiring, preventing processing of stale messages.

Tag: Normal

---

### Question 984
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Priority Queue
Difficulty: Easy

Question: What is a priority queue?
A: Fast queue
B: Queue where messages processed by priority
C: First-in-first-out
D: Random processing

✔ Correct Answer: B

Reason: Priority queues process higher-priority messages first, ensuring critical tasks are handled before less important ones.

Tag: Normal

---

### Question 985
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Fanout Exchange
Difficulty: Hard

Question: What does a fanout exchange do?
A: Fan cooling
B: Broadcasts messages to all bound queues
C: Routes to one queue
D: Drops messages

✔ Correct Answer: B

Reason: Fanout exchange broadcasts messages to all bound queues, ignoring routing keys, useful for pub-sub patterns where all subscribers receive messages.

Tag: Normal

---

### Question 986
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Topic Exchange
Difficulty: Hard

Question: What does a topic exchange use for routing?
A: Random routing
B: Pattern matching on routing keys
C: Round robin
D: No routing

✔ Correct Answer: B

Reason: Topic exchange routes messages based on pattern matching (wildcards) on routing keys, enabling flexible pub-sub with selective subscription.

Tag: Normal

---

### Question 987
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Direct Exchange
Difficulty: Medium

Question: How does a direct exchange route messages?
A: Random routing
B: Exact match on routing key
C: Pattern matching
D: Broadcast

✔ Correct Answer: B

Reason: Direct exchange routes messages to queues where binding key exactly matches routing key, providing simple point-to-point or multicast routing.

Tag: Normal

---

### Question 988
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Message Durability
Difficulty: Medium

Question: What does message durability ensure?
A: Message speed
B: Messages survive broker restart
C: Message encryption
D: Message compression

✔ Correct Answer: B

Reason: Durable messages are persisted to disk, surviving broker restarts, trading performance for reliability, critical for important messages.

Tag: Normal

---

### Question 989
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Transient Messages
Difficulty: Medium

Question: When are transient (non-durable) messages appropriate?
A: Critical data
B: High-throughput, loss-tolerant scenarios
C: Financial transactions
D: Never

✔ Correct Answer: B

Reason: Transient messages are faster but lost on broker restart, suitable for high-throughput scenarios where occasional loss is acceptable (metrics, logs).

Tag: Normal

---

### Question 990
Domain: Computer Networks
Topic: Network Performance
Subtopic: Message Batching
Difficulty: Medium

Question: What is message batching?
A: Processing one at a time
B: Grouping multiple messages for efficient processing
C: Delaying messages
D: Splitting messages

✔ Correct Answer: B

Reason: Message batching groups multiple messages for processing together, reducing overhead and improving throughput at cost of slight latency increase.

Tag: Normal

---

### Question 991
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Event Streaming
Difficulty: Medium

Question: How does event streaming differ from message queuing?
A: Same thing
B: Streaming retains events for replay, queuing deletes after consumption
C: Streaming is slower
D: Queuing is newer

✔ Correct Answer: B

Reason: Event streaming platforms (Kafka) retain events for configured time allowing replay, while message queues delete messages after consumption.

Tag: Normal

---

### Question 992
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Log Compaction
Difficulty: Hard

Question: What is log compaction in Kafka?
A: Compressing logs
B: Retaining only latest value per key
C: Deleting all logs
D: Encrypting logs

✔ Correct Answer: B

Reason: Log compaction retains only the latest value for each key, providing complete current state while discarding intermediate updates, useful for state stores.

Tag: Normal

---

### Question 993
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Consumer Groups
Difficulty: Hard

Question: What do consumer groups in Kafka enable?
A: Group chat
B: Parallel processing with load balancing
C: Sequential processing only
D: No grouping

✔ Correct Answer: B

Reason: Consumer groups allow multiple consumers to share partition consumption, enabling parallel processing and load balancing while maintaining ordering per partition.

Tag: Normal

---

### Question 994
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Partition Key
Difficulty: Hard

Question: What determines which partition a message goes to?
A: Random selection
B: Hash of partition key
C: Message size
D: Timestamp

✔ Correct Answer: B

Reason: Messages with same partition key go to same partition (via hash), ensuring ordering for related messages while enabling parallel processing across partitions.

Tag: Normal

---

### Question 995
Domain: Computer Networks
Topic: Network Performance
Subtopic: Replication Factor
Difficulty: Hard

Question: What does replication factor determine?
A: Replication speed
B: Number of copies of data maintained
C: Replication time
D: Replication cost

✔ Correct Answer: B

Reason: Replication factor specifies how many copies of data are maintained across nodes, balancing durability and availability against storage and performance costs.

Tag: Normal

---

### Question 996
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Leader-Follower Replication
Difficulty: Medium

Question: In leader-follower replication, what handles writes?
A: All nodes
B: Leader only
C: Followers only
D: Random node

✔ Correct Answer: B

Reason: Leader handles all writes and replicates to followers, which handle reads, providing consistency but making leader a potential bottleneck.

Tag: Normal

---

### Question 997
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Failover Process
Difficulty: Medium

Question: What happens during failover?
A: System fails
B: Backup system takes over from failed primary
C: System restarts
D: Nothing

✔ Correct Answer: B

Reason: Failover automatically switches from failed primary to backup system, maintaining service availability, requiring health monitoring and state synchronization.

Tag: Normal

---

### Question 998
Domain: Computer Networks
Topic: Network Architecture
Subtopic: Split-Brain Prevention
Difficulty: Hard

Question: How is split-brain prevented?
A: Physical separation
B: Quorum-based decisions
C: Faster networks
D: More nodes

✔ Correct Answer: B

Reason: Quorum requires majority agreement for operations, preventing split-brain where partitioned groups both act as primary, ensuring consistency.

Tag: Normal

---

### Question 999
Domain: Computer Networks
Topic: Network Performance
Subtopic: Performance Testing
Difficulty: Easy

Question: What is load testing?
A: Testing physical load
B: Testing system behavior under expected load
C: Testing maximum load only
D: No testing

✔ Correct Answer: B

Reason: Load testing evaluates system performance under expected normal and peak loads, identifying bottlenecks and ensuring SLOs are met.

Tag: Normal

---

### Question 1000
Domain: Computer Networks
Topic: Network Performance
Subtopic: Stress Testing
Difficulty: Medium

Question: What is the purpose of stress testing?
A: Test normal load
B: Find breaking point by exceeding expected load
C: Test minimum load
D: No purpose

✔ Correct Answer: B

Reason: Stress testing pushes system beyond expected limits to find breaking points, understand failure modes, and determine maximum capacity.

Tag: Normal

---

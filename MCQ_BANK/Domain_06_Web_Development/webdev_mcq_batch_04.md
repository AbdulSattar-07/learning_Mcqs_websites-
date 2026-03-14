# Web Development - MCQ Batch 04
## Questions 301-400

---

### Question 301
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Render Blocking Resources
Difficulty: Hard

Question: Render-blocking resources:
A) Speed up rendering
B) Prevent page from rendering until loaded
C) Have no effect
D) Only affect images

✔ Correct Answer: B

Reason: Render-blocking resources (CSS, synchronous JavaScript) prevent the browser from rendering the page until they're loaded.

Tag: Normal

---

### Question 302
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Async vs Defer
Difficulty: Hard

Question: The 'defer' attribute on script tags:
A) Deletes script
B) Downloads script in parallel, executes after HTML parsing
C) Blocks parsing
D) Removes script

✔ Correct Answer: B

Reason: defer downloads the script in parallel with HTML parsing and executes it after parsing completes, maintaining order.

Tag: Normal

---

### Question 303
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Async Attribute
Difficulty: Hard

Question: The 'async' attribute on script tags:
A) Blocks parsing
B) Downloads and executes script asynchronously
C) Removes script
D) Defers execution

✔ Correct Answer: B

Reason: async downloads the script in parallel and executes it as soon as it's available, potentially interrupting HTML parsing.

Tag: Normal

---

### Question 304
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Resource Hints
Difficulty: Hard

Question: <link rel="preload"> is used to:
A) Delete resources
B) Tell browser to download resource with high priority
C) Slow down loading
D) Remove links

✔ Correct Answer: B

Reason: preload tells the browser to download a resource with high priority because it will be needed soon.

Tag: Normal

---

### Question 305
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: DNS Prefetch
Difficulty: Medium

Question: <link rel="dns-prefetch"> does what?
A) Removes DNS
B) Resolves domain name before resource is requested
C) Blocks DNS
D) Creates DNS

✔ Correct Answer: B

Reason: dns-prefetch resolves the domain name in advance, reducing latency when the resource is actually requested.

Tag: Normal

---

### Question 306
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Service Workers
Difficulty: Hard

Question: Service Workers enable:
A) Server management
B) Offline functionality and background sync
C) Database management
D) CSS processing

✔ Correct Answer: B

Reason: Service Workers are scripts that run in the background, enabling offline functionality, push notifications, and background sync.

Tag: Normal

---

### Question 307
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Web Workers
Difficulty: Hard

Question: Web Workers:
A) Work on servers
B) Run JavaScript in background threads
C) Style pages
D) Handle routing

✔ Correct Answer: B

Reason: Web Workers run JavaScript in background threads, allowing heavy computations without blocking the main thread.

Tag: Normal

---

### Question 308
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Critical CSS
Difficulty: Hard

Question: Critical CSS refers to:
A) All CSS
B) Minimum CSS needed for above-the-fold content
C) Unused CSS
D) External CSS only

✔ Correct Answer: B

Reason: Critical CSS is the minimum CSS required to render above-the-fold content, inlined for faster initial render.

Tag: Normal

---

### Question 309
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Image Formats
Difficulty: Medium

Question: WebP format offers:
A) Larger file sizes
B) Better compression than JPEG/PNG
C) Worse quality
D) No transparency

✔ Correct Answer: B

Reason: WebP provides superior compression compared to JPEG and PNG, with support for transparency and animation.

Tag: Normal

---

### Question 310
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Responsive Images
Difficulty: Medium

Question: The srcset attribute:
A) Sets source code
B) Provides multiple image sources for different screen sizes
C) Removes images
D) Compresses images

✔ Correct Answer: B

Reason: srcset allows specifying multiple image sources for different screen sizes/resolutions, letting browser choose appropriate one.

Tag: Normal

---

### Question 311
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Assertion Testing
Difficulty: Medium

Question: In testing, an assertion:
A) Deletes code
B) Checks if condition is true
C) Creates bugs
D) Removes tests

✔ Correct Answer: B

Reason: An assertion is a statement that checks if a condition is true, failing the test if it's false.

Tag: Normal

---

### Question 312
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Mocking
Difficulty: Hard

Question: Mocking in testing:
A) Makes fun of code
B) Creates fake objects to simulate real ones
C) Deletes objects
D) Copies objects

✔ Correct Answer: B

Reason: Mocking creates fake objects that simulate the behavior of real objects for isolated testing.

Tag: Normal

---

### Question 313
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Test-Driven Development
Difficulty: Medium

Question: TDD cycle is:
A) Write code, then test
B) Red (fail), Green (pass), Refactor
C) Test only
D) Code only

✔ Correct Answer: B

Reason: TDD follows Red-Green-Refactor: write failing test, make it pass, then refactor code.

Tag: Past Paper

---

### Question 314
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Snapshot Testing
Difficulty: Hard

Question: Snapshot testing:
A) Takes photos
B) Compares component output to saved snapshot
C) Deletes snapshots
D) Creates videos

✔ Correct Answer: B

Reason: Snapshot testing captures the rendered output of a component and compares it to a saved reference snapshot.

Tag: Normal

---

### Question 315
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Code Coverage
Difficulty: Medium

Question: 100% code coverage means:
A) All code is perfect
B) All code lines are executed during tests
C) No bugs exist
D) Tests are complete

✔ Correct Answer: B

Reason: 100% code coverage means all lines of code are executed during tests, but doesn't guarantee bug-free code.

Tag: Normal

---

### Question 316
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Static Site Hosting
Difficulty: Easy

Question: Static sites contain:
A) Server-side code only
B) HTML, CSS, JavaScript without server processing
C) Databases only
D) Dynamic content only

✔ Correct Answer: B

Reason: Static sites consist of fixed HTML, CSS, and JavaScript files served directly without server-side processing.

Tag: Normal

---

### Question 317
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Server Types
Difficulty: Medium

Question: A VPS (Virtual Private Server) is:
A) Physical server
B) Virtualized server with dedicated resources
C) Shared hosting
D) No server

✔ Correct Answer: B

Reason: VPS is a virtualized server that provides dedicated resources within a shared physical server.

Tag: Normal

---

### Question 318
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Serverless Computing
Difficulty: Hard

Question: Serverless computing means:
A) No servers exist
B) Developer doesn't manage servers, cloud provider does
C) Free hosting
D) Slow performance

✔ Correct Answer: B

Reason: Serverless means developers don't manage servers; the cloud provider handles infrastructure, scaling automatically.

Tag: Normal

---

### Question 319
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Environment Variables
Difficulty: Medium

Question: .env files should be:
A) Committed to version control
B) Kept out of version control (gitignored)
C) Shared publicly
D) Deleted

✔ Correct Answer: B

Reason: .env files contain sensitive data and should be excluded from version control using .gitignore.

Tag: Normal

---

### Question 320
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: SSL Certificates
Difficulty: Medium

Question: SSL certificates:
A) Slow down websites
B) Encrypt data between client and server
C) Are optional
D) Only for emails

✔ Correct Answer: B

Reason: SSL/TLS certificates encrypt data transmitted between client and server, enabling HTTPS.

Tag: Past Paper

---

### Question 321
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: HTTP Status Code Categories
Difficulty: Medium

Question: 2xx status codes indicate:
A) Client errors
B) Successful responses
C) Server errors
D) Redirects

✔ Correct Answer: B

Reason: 2xx status codes (200-299) indicate successful responses.

Tag: Past Paper

---

### Question 322
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: HTTP Status Codes
Difficulty: Medium

Question: Status code 401 means:
A) Not Found
B) Unauthorized (authentication required)
C) Forbidden
D) Server Error

✔ Correct Answer: B

Reason: 401 Unauthorized indicates authentication is required and has failed or not been provided.

Tag: Past Paper

---

### Question 323
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: HTTP Status Codes
Difficulty: Medium

Question: Status code 403 means:
A) Not Found
B) Unauthorized
C) Forbidden (no permission)
D) Success

✔ Correct Answer: C

Reason: 403 Forbidden means the server understood the request but refuses to authorize it.

Tag: Past Paper

---

### Question 324
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: API Documentation
Difficulty: Medium

Question: Swagger/OpenAPI is used for:
A) Database design
B) API documentation and specification
C) Frontend design
D) Testing only

✔ Correct Answer: B

Reason: Swagger/OpenAPI is a specification for documenting RESTful APIs in a machine-readable format.

Tag: Normal

---

### Question 325
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: API Keys
Difficulty: Medium

Question: API keys should be:
A) Shared publicly
B) Kept secret and not exposed in client-side code
C) Hardcoded in frontend
D) Committed to Git

✔ Correct Answer: B

Reason: API keys are sensitive credentials that should be kept secret and stored securely, not exposed in client-side code.

Tag: Normal

---

### Question 326
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: JAMstack
Difficulty: Hard

Question: JAMstack stands for:
A) Java, API, Markup
B) JavaScript, APIs, Markup
C) JSON, API, Markup
D) Java, Angular, Markup

✔ Correct Answer: B

Reason: JAMstack stands for JavaScript, APIs, and Markup - a modern web development architecture.

Tag: Normal

---

### Question 327
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Static Site Generators
Difficulty: Medium

Question: Static site generators:
A) Generate dynamic content
B) Build static HTML pages from templates and content
C) Require databases
D) Need servers

✔ Correct Answer: B

Reason: Static site generators build static HTML pages from templates and content at build time.

Tag: Normal

---

### Question 328
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Headless CMS
Difficulty: Hard

Question: A headless CMS:
A) Has no interface
B) Provides content via API without frontend
C) Cannot manage content
D) Is slower

✔ Correct Answer: B

Reason: Headless CMS provides content through APIs without a coupled frontend, allowing flexible content delivery.

Tag: Normal

---

### Question 329
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Server-Side Rendering
Difficulty: Hard

Question: SSR (Server-Side Rendering):
A) Renders on client only
B) Renders pages on server before sending to client
C) Never renders
D) Renders after page load

✔ Correct Answer: B

Reason: SSR renders pages on the server and sends fully rendered HTML to the client, improving initial load and SEO.

Tag: Normal

---

### Question 330
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Client-Side Rendering
Difficulty: Medium

Question: CSR (Client-Side Rendering):
A) Renders on server
B) Renders content in browser using JavaScript
C) No rendering
D) Renders before download

✔ Correct Answer: B

Reason: CSR renders content in the browser using JavaScript after the initial HTML is loaded.

Tag: Normal

---

### Question 331
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Hydration
Difficulty: Hard

Question: Hydration in web development:
A) Adds water
B) Attaches event handlers to server-rendered HTML
C) Removes content
D) Compresses files

✔ Correct Answer: B

Reason: Hydration is the process of attaching event handlers and making server-rendered HTML interactive on the client.

Tag: Normal

---

### Question 332
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Incremental Static Regeneration
Difficulty: Hard

Question: ISR allows:
A) No updates
B) Updating static pages after build without rebuilding entire site
C) Only dynamic pages
D) No static pages

✔ Correct Answer: B

Reason: ISR (Incremental Static Regeneration) allows updating static pages after deployment without rebuilding the entire site.

Tag: Normal

---

### Question 333
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: HTML Entities
Difficulty: Medium

Question: &nbsp; represents:
A) New line
B) Non-breaking space
C) Tab
D) Paragraph

✔ Correct Answer: B

Reason: &nbsp; is an HTML entity representing a non-breaking space that prevents line breaks.

Tag: Normal

---

### Question 334
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: HTML Accessibility
Difficulty: Medium

Question: The 'alt' attribute on images:
A) Is optional
B) Provides alternative text for screen readers
C) Changes image
D) Adds effects

✔ Correct Answer: B

Reason: The alt attribute provides alternative text for images, crucial for accessibility and when images fail to load.

Tag: Past Paper

---

### Question 335
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: ARIA Attributes
Difficulty: Hard

Question: ARIA stands for:
A) Advanced Rich Internet Applications
B) Accessible Rich Internet Applications
C) Automated Rich Internet Applications
D) Active Rich Internet Applications

✔ Correct Answer: B

Reason: ARIA (Accessible Rich Internet Applications) provides attributes to make web content more accessible.

Tag: Normal

---

### Question 336
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: HTML Lang Attribute
Difficulty: Medium

Question: The lang attribute on <html> tag:
A) Sets programming language
B) Specifies page's natural language
C) Changes font
D) Sets timezone

✔ Correct Answer: B

Reason: The lang attribute specifies the natural language of the page content (e.g., lang="en" for English).

Tag: Normal

---

### Question 337
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: HTML Viewport
Difficulty: Medium

Question: <meta name="viewport"> is used for:
A) Creating views
B) Controlling page dimensions and scaling on mobile
C) Adding images
D) Setting colors

✔ Correct Answer: B

Reason: The viewport meta tag controls how the page is displayed on mobile devices, setting width and initial scale.

Tag: Normal

---

### Question 338
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: CSS Inheritance
Difficulty: Medium

Question: Which property is NOT inherited by default?
A) color
B) font-family
C) border
D) font-size

✔ Correct Answer: C

Reason: Border properties are not inherited; color and font properties typically are inherited by child elements.

Tag: Normal

---

### Question 339
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: CSS !important
Difficulty: Medium

Question: !important in CSS:
A) Is recommended for all styles
B) Overrides other declarations, should be used sparingly
C) Has no effect
D) Removes styles

✔ Correct Answer: B

Reason: !important gives a declaration the highest specificity, overriding other rules, but should be used sparingly.

Tag: Normal

---

### Question 340
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: CSS Attribute Selectors
Difficulty: Medium

Question: [type="text"] selector targets:
A) All elements
B) Elements with type attribute equal to "text"
C) Text content
D) Paragraphs

✔ Correct Answer: B

Reason: Attribute selectors target elements based on attribute values; [type="text"] selects elements with type="text".

Tag: Normal

---

### Question 341
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: CSS nth-child
Difficulty: Hard

Question: :nth-child(2n) selects:
A) First child
B) Every even child
C) Every odd child
D) Last child

✔ Correct Answer: B

Reason: :nth-child(2n) or :nth-child(even) selects every even-numbered child element.

Tag: Normal

---

### Question 342
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: CSS first-child
Difficulty: Medium

Question: :first-child pseudo-class selects:
A) First element on page
B) First child of its parent
C) All children
D) Last child

✔ Correct Answer: B

Reason: :first-child selects an element that is the first child of its parent.

Tag: Normal

---

### Question 343
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Container Queries
Difficulty: Hard

Question: Container queries allow:
A) Querying databases
B) Styling based on container size, not viewport
C) Creating containers
D) Removing containers

✔ Correct Answer: B

Reason: Container queries enable styling elements based on their container's size rather than the viewport size.

Tag: Normal

---

### Question 344
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Logical Properties
Difficulty: Hard

Question: margin-inline-start is equivalent to:
A) margin-top
B) margin-left in LTR, margin-right in RTL
C) margin-bottom
D) margin-right always

✔ Correct Answer: B

Reason: Logical properties adapt to writing direction; margin-inline-start is margin-left in LTR, margin-right in RTL.

Tag: Normal

---

### Question 345
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Scroll Snap
Difficulty: Hard

Question: scroll-snap-type enables:
A) Removing scrolling
B) Snapping scroll position to specific points
C) Infinite scrolling
D) Disabling scroll

✔ Correct Answer: B

Reason: scroll-snap-type creates scroll snapping behavior, making scroll positions snap to defined points.

Tag: Normal

---

### Question 346
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Custom Properties Scope
Difficulty: Hard

Question: CSS variables defined in :root are:
A) Local to root only
B) Global, available throughout document
C) Not accessible
D) Temporary

✔ Correct Answer: B

Reason: Variables defined in :root pseudo-class are global and accessible throughout the entire document.

Tag: Normal

---

### Question 347
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Strict Mode
Difficulty: Medium

Question: 'use strict' does what?
A) Makes code slower
B) Enables strict mode, catching common errors
C) Removes features
D) Disables JavaScript

✔ Correct Answer: B

Reason: 'use strict' enables strict mode, which catches common coding errors and prevents certain actions.

Tag: Past Paper

---

### Question 348
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: NaN
Difficulty: Medium

Question: How to check if a value is NaN?
A) value === NaN
B) Number.isNaN(value)
C) value == NaN
D) typeof value === "NaN"

✔ Correct Answer: B

Reason: Number.isNaN() is the reliable way to check for NaN; NaN === NaN returns false.

Tag: Normal

---

### Question 349
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Undefined vs Null
Difficulty: Medium

Question: undefined means:
A) Variable is null
B) Variable declared but not assigned value
C) Variable doesn't exist
D) Variable is false

✔ Correct Answer: B

Reason: undefined means a variable has been declared but hasn't been assigned a value yet.

Tag: Past Paper

---

### Question 350
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: typeof Operator
Difficulty: Medium

Question: typeof null returns:
A) "null"
B) "object"
C) "undefined"
D) "number"

✔ Correct Answer: B

Reason: typeof null returns "object" due to a historical JavaScript bug that was never fixed for compatibility.

Tag: Normal

---

### Question 351
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array isArray
Difficulty: Medium

Question: How to check if a variable is an array?
A) typeof arr === "array"
B) Array.isArray(arr)
C) arr instanceof Object
D) arr.isArray()

✔ Correct Answer: B

Reason: Array.isArray() is the reliable method to check if a value is an array.

Tag: Normal

---

### Question 352
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: String Template Literals
Difficulty: Easy

Question: Template literals allow:
A) Only strings
B) String interpolation and multi-line strings
C) Numbers only
D) No variables

✔ Correct Answer: B

Reason: Template literals (backticks) support string interpolation with ${} and multi-line strings.

Tag: Normal

---

### Question 353
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Object Property Shorthand
Difficulty: Medium

Question: In ES6, {name, age} is shorthand for:
A) {name: name, age: age}
B) {name: "name", age: "age"}
C) {0: name, 1: age}
D) Invalid syntax

✔ Correct Answer: A

Reason: ES6 property shorthand: {name, age} is equivalent to {name: name, age: age}.

Tag: Normal

---

### Question 354
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Object Computed Properties
Difficulty: Medium

Question: {[key]: value} syntax allows:
A) Fixed property names
B) Dynamic property names
C) No properties
D) Array creation

✔ Correct Answer: B

Reason: Computed property names use brackets to create properties with dynamic names based on variable values.

Tag: Normal

---

### Question 355
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: For...of Loop
Difficulty: Medium

Question: for...of loop iterates over:
A) Object properties
B) Iterable values (arrays, strings, etc.)
C) Numbers only
D) Nothing

✔ Correct Answer: B

Reason: for...of iterates over iterable objects (arrays, strings, Maps, Sets), accessing values directly.

Tag: Normal

---

### Question 356
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: For...in Loop
Difficulty: Medium

Question: for...in loop iterates over:
A) Array values
B) Object property names (keys)
C) Strings only
D) Numbers

✔ Correct Answer: B

Reason: for...in iterates over enumerable property names (keys) of an object.

Tag: Past Paper

---

### Question 357
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Spread
Difficulty: Medium

Question: [...arr1, ...arr2] does what?
A) Deletes arrays
B) Concatenates arrays into new array
C) Compares arrays
D) Removes duplicates

✔ Correct Answer: B

Reason: Spread operator concatenates arrays, creating a new array with elements from both.

Tag: Normal

---

### Question 358
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Object Spread
Difficulty: Medium

Question: {...obj1, ...obj2} does what?
A) Deletes objects
B) Merges objects, obj2 properties override obj1
C) Compares objects
D) Creates array

✔ Correct Answer: B

Reason: Object spread merges objects; properties from obj2 override those in obj1 if keys match.

Tag: Normal

---

### Question 359
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Short-circuit Evaluation
Difficulty: Hard

Question: In a && b, if a is falsy:
A) b is evaluated
B) b is not evaluated, returns a
C) Error occurs
D) Returns true

✔ Correct Answer: B

Reason: && short-circuits: if first operand is falsy, it returns that value without evaluating the second.

Tag: Normal

---

### Question 360
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Logical OR Assignment
Difficulty: Hard

Question: a ||= b is equivalent to:
A) a = a || b
B) a = b || a
C) a || b
D) a && b

✔ Correct Answer: A

Reason: Logical OR assignment (||=) assigns b to a only if a is falsy: a = a || b.

Tag: Normal

---

### Question 361
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Object.freeze
Difficulty: Hard

Question: Object.freeze() makes object:
A) Mutable
B) Immutable (cannot add, delete, or modify properties)
C) Faster
D) Slower

✔ Correct Answer: B

Reason: Object.freeze() makes an object immutable - properties cannot be added, deleted, or modified.

Tag: Normal

---

### Question 362
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Object.seal
Difficulty: Hard

Question: Object.seal() allows:
A) Adding new properties
B) Modifying existing properties but not adding/deleting
C) Deleting properties
D) Nothing

✔ Correct Answer: B

Reason: Object.seal() prevents adding or deleting properties but allows modifying existing ones.

Tag: Normal

---

### Question 363
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Object.assign
Difficulty: Medium

Question: Object.assign(target, source) does what?
A) Deletes objects
B) Copies properties from source to target
C) Compares objects
D) Creates array

✔ Correct Answer: B

Reason: Object.assign() copies enumerable properties from source object(s) to target object.

Tag: Normal

---

### Question 364
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Object.entries
Difficulty: Medium

Question: Object.entries() returns:
A) Object keys
B) Array of [key, value] pairs
C) Object values
D) Object length

✔ Correct Answer: B

Reason: Object.entries() returns an array of [key, value] pairs from the object.

Tag: Normal

---

### Question 365
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Object.fromEntries
Difficulty: Hard

Question: Object.fromEntries() does what?
A) Deletes entries
B) Converts array of [key, value] pairs to object
C) Creates array
D) Removes properties

✔ Correct Answer: B

Reason: Object.fromEntries() transforms an array of [key, value] pairs into an object.

Tag: Normal

---

### Question 366
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Array.from
Difficulty: Medium

Question: Array.from() can:
A) Delete arrays
B) Create array from array-like or iterable object
C) Only copy arrays
D) Remove elements

✔ Correct Answer: B

Reason: Array.from() creates a new array from an array-like or iterable object.

Tag: Normal

---

### Question 367
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Array.flat
Difficulty: Medium

Question: [1, [2, [3]]].flat(2) returns:
A) [1, 2, 3]
B) [1, [2, [3]]]
C) [1, 2, [3]]
D) Error

✔ Correct Answer: A

Reason: flat(2) flattens array up to 2 levels deep, resulting in [1, 2, 3].

Tag: Normal

---

### Question 368
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Array.flatMap
Difficulty: Hard

Question: flatMap() is equivalent to:
A) map() only
B) map() followed by flat(1)
C) filter() and map()
D) reduce()

✔ Correct Answer: B

Reason: flatMap() maps each element using a function, then flattens the result by one level.

Tag: Normal

---

### Question 369
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Array.at
Difficulty: Medium

Question: arr.at(-1) returns:
A) First element
B) Last element
C) Error
D) undefined

✔ Correct Answer: B

Reason: at() method accepts negative indices; at(-1) returns the last element.

Tag: Normal

---

### Question 370
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: String.padStart
Difficulty: Medium

Question: "5".padStart(3, "0") returns:
A) "500"
B) "005"
C) "050"
D) "5"

✔ Correct Answer: B

Reason: padStart() pads the string from the start to reach target length: "005".

Tag: Normal

---

### Question 371
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: String.repeat
Difficulty: Easy

Question: "ab".repeat(3) returns:
A) "ab3"
B) "ababab"
C) "aaa"
D) "bbb"

✔ Correct Answer: B

Reason: repeat() returns a new string with specified number of copies: "ababab".

Tag: Normal

---

### Question 372
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: String.startsWith
Difficulty: Easy

Question: "Hello".startsWith("He") returns:
A) false
B) true
C) "He"
D) Error

✔ Correct Answer: B

Reason: startsWith() checks if string starts with specified characters, returning true or false.

Tag: Normal

---

### Question 373
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Promise.allSettled
Difficulty: Hard

Question: Promise.allSettled() waits for:
A) First promise to settle
B) All promises to settle (resolve or reject)
C) All to resolve only
D) One to reject

✔ Correct Answer: B

Reason: Promise.allSettled() waits for all promises to settle, regardless of whether they resolve or reject.

Tag: Normal

---

### Question 374
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Promise.any
Difficulty: Hard

Question: Promise.any() resolves when:
A) All promises resolve
B) First promise resolves
C) All promises reject
D) Never

✔ Correct Answer: B

Reason: Promise.any() resolves as soon as any promise resolves, ignoring rejections unless all reject.

Tag: Normal

---

### Question 375
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Async Iteration
Difficulty: Hard

Question: for await...of is used for:
A) Synchronous iteration
B) Iterating over async iterables
C) Object iteration
D) Number iteration

✔ Correct Answer: B

Reason: for await...of iterates over async iterables, awaiting each promise in the sequence.

Tag: Normal

---

### Question 376
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React StrictMode
Difficulty: Medium

Question: React.StrictMode:
A) Enforces strict typing
B) Highlights potential problems in development
C) Improves performance
D) Is for production only

✔ Correct Answer: B

Reason: StrictMode is a development tool that highlights potential problems, running additional checks and warnings.

Tag: Normal

---

### Question 377
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Fragments
Difficulty: Medium

Question: React Fragments (<></>) allow:
A) Breaking components
B) Grouping children without adding extra DOM nodes
C) Creating fragments
D) Removing elements

✔ Correct Answer: B

Reason: Fragments let you group children without adding extra nodes to the DOM.

Tag: Normal

---

### Question 378
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React PropTypes
Difficulty: Medium

Question: PropTypes are used for:
A) Creating props
B) Type checking props in development
C) Styling props
D) Removing props

✔ Correct Answer: B

Reason: PropTypes provide runtime type checking for React props during development.

Tag: Normal

---

### Question 379
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React defaultProps
Difficulty: Medium

Question: defaultProps define:
A) Required props
B) Default values for props
C) Prop types
D) Prop names

✔ Correct Answer: B

Reason: defaultProps specify default values for props if they're not provided by the parent.

Tag: Normal

---

### Question 380
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Children Prop
Difficulty: Medium

Question: props.children contains:
A) Parent component
B) Content between component's opening and closing tags
C) Sibling components
D) Nothing

✔ Correct Answer: B

Reason: props.children contains the content passed between a component's opening and closing tags.

Tag: Normal

---

### Question 381
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Higher-Order Components
Difficulty: Hard

Question: A Higher-Order Component (HOC) is:
A) A component at top of tree
B) Function that takes component and returns enhanced component
C) A class component
D) A hook

✔ Correct Answer: B

Reason: HOC is a function that takes a component and returns a new component with additional props or behavior.

Tag: Normal

---

### Question 382
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Render Props
Difficulty: Hard

Question: Render props pattern:
A) Renders properties
B) Shares code using prop whose value is a function
C) Styles components
D) Removes props

✔ Correct Answer: B

Reason: Render props is a technique for sharing code between components using a prop whose value is a function.

Tag: Normal

---

### Question 383
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Controlled Components
Difficulty: Medium

Question: In controlled components:
A) Component controls itself
B) React state controls form element values
C) No control exists
D) Browser controls values

✔ Correct Answer: B

Reason: Controlled components have form element values controlled by React state, making React the "single source of truth".

Tag: Normal

---

### Question 384
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Uncontrolled Components
Difficulty: Medium

Question: Uncontrolled components:
A) Are controlled by React
B) Store form data in DOM, accessed via refs
C) Have no data
D) Cannot be used

✔ Correct Answer: B

Reason: Uncontrolled components store form data in the DOM itself, accessed using refs rather than state.

Tag: Normal

---

### Question 385
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Angular Two-Way Binding
Difficulty: Medium

Question: [(ngModel)] in Angular provides:
A) One-way binding
B) Two-way data binding
C) No binding
D) Event binding only

✔ Correct Answer: B

Reason: [(ngModel)] combines property binding and event binding to create two-way data binding.

Tag: Normal

---

### Question 386
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Angular Pipes
Difficulty: Medium

Question: Pipes in Angular:
A) Create pipelines
B) Transform data in templates
C) Handle routing
D) Manage state

✔ Correct Answer: B

Reason: Pipes transform displayed values in templates (e.g., date formatting, uppercase conversion).

Tag: Normal

---

### Question 387
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Vue Slots
Difficulty: Medium

Question: Slots in Vue allow:
A) Time slots
B) Parent to pass content to child component
C) Styling only
D) Routing

✔ Correct Answer: B

Reason: Slots are Vue's content distribution mechanism, allowing parent components to pass content to children.

Tag: Normal

---

### Question 388
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Vue Mixins
Difficulty: Hard

Question: Mixins in Vue:
A) Mix colors
B) Distribute reusable functionality across components
C) Create components
D) Handle routing

✔ Correct Answer: B

Reason: Mixins are a flexible way to distribute reusable functionality across Vue components.

Tag: Normal

---

### Question 389
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Vue Composition API
Difficulty: Hard

Question: Composition API in Vue 3:
A) Composes music
B) Organizes component logic by feature
C) Is for styling
D) Handles routing

✔ Correct Answer: B

Reason: Composition API allows organizing component logic by logical concerns rather than lifecycle hooks.

Tag: Normal

---

### Question 390
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: Request Methods Safety
Difficulty: Hard

Question: Safe HTTP methods:
A) Change server state
B) Don't modify server state (GET, HEAD, OPTIONS)
C) Are insecure
D) Require authentication

✔ Correct Answer: B

Reason: Safe methods (GET, HEAD, OPTIONS) are read-only and don't modify server state.

Tag: Past Paper

---

### Question 391
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: Content Negotiation
Difficulty: Hard

Question: Accept header in HTTP request:
A) Accepts all content
B) Specifies media types client can process
C) Rejects content
D) Sets cookies

✔ Correct Answer: B

Reason: Accept header tells the server which media types (content types) the client can understand.

Tag: Normal

---

### Question 392
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: ETag
Difficulty: Hard

Question: ETag header is used for:
A) Tagging errors
B) Cache validation and conditional requests
C) Authentication
D) Routing

✔ Correct Answer: B

Reason: ETag is an identifier for a specific version of a resource, used for cache validation.

Tag: Normal

---

### Question 393
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: HTTP Caching
Difficulty: Hard

Question: Cache-Control: no-cache means:
A) Don't cache at all
B) Cache but revalidate with server before using
C) Cache forever
D) Delete cache

✔ Correct Answer: B

Reason: no-cache means cache the response but revalidate with the server before using it.

Tag: Normal

---

### Question 394
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: HTTP Caching
Difficulty: Medium

Question: Cache-Control: max-age=3600 means:
A) Cache for 3600 seconds
B) Cache for 3600 minutes
C) Don't cache
D) Cache forever

✔ Correct Answer: A

Reason: max-age specifies the maximum time in seconds a resource is considered fresh.

Tag: Normal

---

### Question 395
Domain: Web Development
Topic: Server-Side Programming
Subtopic: RESTful API Design
Difficulty: Medium

Question: In REST, resource names should be:
A) Verbs
B) Nouns (plural)
C) Adjectives
D) Random

✔ Correct Answer: B

Reason: RESTful URLs should use nouns (preferably plural) to represent resources, not verbs.

Tag: Past Paper

---

### Question 396
Domain: Web Development
Topic: Server-Side Programming
Subtopic: API Versioning
Difficulty: Medium

Question: API versioning can be done via:
A) URL path (/v1/users)
B) Headers
C) Query parameters
D) All of the above

✔ Correct Answer: D

Reason: API versioning can be implemented through URL paths, headers, or query parameters.

Tag: Normal

---

### Question 397
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Webhook
Difficulty: Hard

Question: A webhook is:
A) Web hook for fishing
B) HTTP callback that sends data when event occurs
C) Database hook
D) CSS hook

✔ Correct Answer: B

Reason: Webhook is an HTTP callback that sends real-time data to a URL when a specific event occurs.

Tag: Normal

---

### Question 398
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Long Polling
Difficulty: Hard

Question: Long polling:
A) Polls quickly
B) Client requests, server holds connection until data available
C) Never polls
D) Polls once

✔ Correct Answer: B

Reason: Long polling keeps the connection open until the server has data to send, then immediately reconnects.

Tag: Normal

---

### Question 399
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Server-Sent Events
Difficulty: Hard

Question: Server-Sent Events (SSE):
A) Are bidirectional
B) Allow server to push updates to client over HTTP
C) Require WebSocket
D) Are client-initiated only

✔ Correct Answer: B

Reason: SSE allows servers to push real-time updates to clients over a single HTTP connection (unidirectional).

Tag: Normal

---

### Question 400
Domain: Web Development
Topic: Databases for Web Applications
Subtopic: Database Sharding
Difficulty: Hard

Question: Database sharding:
A) Breaks database
B) Partitions data across multiple databases
C) Deletes data
D) Backs up data

✔ Correct Answer: B

Reason: Sharding is a database partitioning technique that distributes data across multiple database instances.

Tag: Normal

---

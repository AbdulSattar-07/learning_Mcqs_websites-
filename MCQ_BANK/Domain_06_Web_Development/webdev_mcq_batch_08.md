# Web Development MCQ Bank - Batch 08

## Questions 701-800

---

### Question 701
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: RESTful API Design
Difficulty: Medium

Question: Which HTTP method should be used to partially update a resource in a RESTful API?
A) PUT
B) PATCH
C) POST
D) UPDATE

✔ Correct Answer: B
Reason: PATCH is used for partial updates, while PUT replaces the entire resource.
Tag: Normal

---

### Question 702
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Progressive Web Apps
Difficulty: Medium

Question: Which file is essential for creating a Progressive Web App (PWA)?
A) package.json
B) manifest.json
C) config.json
D) settings.json

✔ Correct Answer: B
Reason: manifest.json defines PWA metadata, icons, and behavior.
Tag: Normal

---

### Question 703
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Promises
Difficulty: Hard

Question: What will be the output of the following code?
```javascript
Promise.resolve(1)
  .then(x => x + 1)
  .then(x => { throw new Error('error') })
  .catch(() => 1)
  .then(x => x + 1)
  .then(x => console.log(x))
```
A) 2
B) 3
C) Error
D) undefined

✔ Correct Answer: A
Reason: The catch returns 1, then 1 + 1 = 2 is logged.
Tag: Normal

---

### Question 704
Domain: Web Development
Topic: Web Security
Subtopic: Authentication
Difficulty: Medium

Question: What is the main advantage of using JWT (JSON Web Tokens) for authentication?
A) Tokens are encrypted by default
B) Stateless authentication without server-side sessions
C) Tokens cannot be stolen
D) Automatic token refresh

✔ Correct Answer: B
Reason: JWT enables stateless authentication, reducing server memory usage.
Tag: Normal

---

### Question 705
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Box Model
Difficulty: Easy

Question: In the CSS box model, which property controls the space between the content and the border?
A) margin
B) padding
C) border-spacing
D) gap

✔ Correct Answer: B
Reason: Padding is the space between content and border; margin is outside the border.
Tag: Normal

---

### Question 706
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: HTTP Status Codes
Difficulty: Easy

Question: What does HTTP status code 404 indicate?
A) Server error
B) Resource not found
C) Unauthorized access
D) Bad request

✔ Correct Answer: B
Reason: 404 means the requested resource was not found on the server.
Tag: Past Paper

---

### Question 707
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: React Hooks
Difficulty: Medium

Question: Which React Hook should be used to perform side effects in functional components?
A) useState
B) useEffect
C) useContext
D) useReducer

✔ Correct Answer: B
Reason: useEffect is designed for side effects like data fetching, subscriptions, etc.
Tag: Normal

---

### Question 708
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Lazy Loading
Difficulty: Medium

Question: What is the primary benefit of lazy loading images on a webpage?
A) Better image quality
B) Reduced initial page load time
C) Improved SEO ranking
D) Enhanced security

✔ Correct Answer: B
Reason: Lazy loading defers loading of off-screen images, reducing initial load time.
Tag: Normal

---

### Question 709
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Semantic HTML
Difficulty: Easy

Question: Which HTML5 element should be used to define a navigation section?
A) <div>
B) <section>
C) <nav>
D) <menu>

✔ Correct Answer: C
Reason: <nav> is the semantic element specifically for navigation links.
Tag: Normal

---

### Question 710
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: What will the following code output?
```javascript
const arr = [1, 2, 3, 4, 5];
const result = arr.filter(x => x > 2).map(x => x * 2);
console.log(result);
```
A) [2, 4, 6, 8, 10]
B) [6, 8, 10]
C) [3, 4, 5]
D) [1, 2, 3, 4, 5]

✔ Correct Answer: B
Reason: filter gives [3, 4, 5], then map multiplies each by 2: [6, 8, 10].
Tag: Normal

---

### Question 711
Domain: Web Development
Topic: Web Security
Subtopic: CORS
Difficulty: Medium

Question: What does CORS stand for in web development?
A) Cross-Origin Resource Sharing
B) Client-Origin Request Security
C) Cross-Origin Request System
D) Client-Origin Resource Sharing

✔ Correct Answer: A
Reason: CORS is a mechanism that allows restricted resources to be requested from another domain.
Tag: Normal

---

### Question 712
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: Media Queries
Difficulty: Easy

Question: Which CSS feature is primarily used to create responsive designs?
A) Flexbox
B) Grid
C) Media queries
D) Transitions

✔ Correct Answer: C
Reason: Media queries allow CSS to adapt based on device characteristics like screen width.
Tag: Normal

---

### Question 713
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Node.js
Difficulty: Medium

Question: In Node.js, which module is used to create a web server?
A) fs
B) http
C) path
D) url

✔ Correct Answer: B
Reason: The http module provides functionality to create HTTP servers.
Tag: Normal

---

### Question 714
Domain: Web Development
Topic: Databases for Web Applications
Subtopic: SQL vs NoSQL
Difficulty: Medium

Question: Which database type is best suited for storing hierarchical or nested data structures?
A) Relational databases (SQL)
B) Document databases (NoSQL)
C) Graph databases
D) Key-value stores

✔ Correct Answer: B
Reason: Document databases like MongoDB handle nested/hierarchical data naturally.
Tag: Normal

---

### Question 715
Domain: Web Development
Topic: Web Architecture & Protocols
Subtopic: HTTP Methods
Difficulty: Easy

Question: Which HTTP method is idempotent and used to retrieve data?
A) POST
B) GET
C) PUT
D) DELETE

✔ Correct Answer: B
Reason: GET is idempotent (multiple identical requests have the same effect) and retrieves data.
Tag: Past Paper

---

### Question 716
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Closures
Difficulty: Hard

Question: What will be the output of the following code?
```javascript
function outer() {
  let count = 0;
  return function inner() {
    count++;
    return count;
  }
}
const counter = outer();
console.log(counter());
console.log(counter());
```
A) 0, 0
B) 1, 1
C) 1, 2
D) undefined, undefined

✔ Correct Answer: C
Reason: The inner function forms a closure, maintaining access to count across calls.
Tag: Normal

---

### Question 717
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Unit Testing
Difficulty: Medium

Question: Which JavaScript testing framework is commonly used with React applications?
A) Mocha
B) Jest
C) Jasmine
D) QUnit

✔ Correct Answer: B
Reason: Jest is the most popular testing framework for React, developed by Facebook.
Tag: Normal

---

### Question 718
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Virtual DOM
Difficulty: Medium

Question: What is the primary advantage of using a Virtual DOM in frameworks like React?
A) Smaller bundle size
B) Better SEO
C) Efficient DOM updates
D) Easier debugging

✔ Correct Answer: C
Reason: Virtual DOM minimizes actual DOM manipulations by batching and optimizing updates.
Tag: Normal

---

### Question 719
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Selectors
Difficulty: Easy

Question: Which CSS selector has the highest specificity?
A) Element selector
B) Class selector
C) ID selector
D) Universal selector

✔ Correct Answer: C
Reason: ID selectors have higher specificity than class or element selectors.
Tag: Normal

---

### Question 720
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: Fetch API
Difficulty: Medium

Question: What does the Fetch API return?
A) JSON object
B) Promise
C) XMLHttpRequest object
D) String

✔ Correct Answer: B
Reason: Fetch returns a Promise that resolves to the Response object.
Tag: Normal

---

### Question 721
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Web Components
Difficulty: Medium

Question: Which technology allows you to create reusable custom HTML elements?
A) React Components
B) Web Components
C) Angular Directives
D) Vue Components

✔ Correct Answer: B
Reason: Web Components are a native browser standard for creating custom, reusable elements.
Tag: Normal

---

### Question 722
Domain: Web Development
Topic: Web Security
Subtopic: XSS Prevention
Difficulty: Hard

Question: Which HTTP header helps prevent XSS attacks by controlling which scripts can execute?
A) X-Frame-Options
B) Content-Security-Policy
C) X-XSS-Protection
D) Strict-Transport-Security

✔ Correct Answer: B
Reason: Content-Security-Policy (CSP) defines approved sources of executable scripts.
Tag: Normal

---

### Question 723
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Async/Await
Difficulty: Medium

Question: What keyword must be used before a function to use await inside it?
A) promise
B) async
C) defer
D) await

✔ Correct Answer: B
Reason: Functions must be declared with async to use await for asynchronous operations.
Tag: Normal

---

### Question 724
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Forms
Difficulty: Easy

Question: Which HTML input type is used for email validation?
A) <input type="text">
B) <input type="email">
C) <input type="mail">
D) <input type="validate">

✔ Correct Answer: B
Reason: type="email" provides built-in email format validation.
Tag: Normal

---

### Question 725
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Cloud Platforms
Difficulty: Easy

Question: Which platform is specifically designed for deploying static websites and JAMstack applications?
A) Heroku
B) AWS EC2
C) Netlify
D) DigitalOcean

✔ Correct Answer: C
Reason: Netlify specializes in static site hosting and JAMstack deployments.
Tag: Normal

---

### Question 726
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: RESTful APIs
Difficulty: Medium

Question: In REST architecture, what does the term "stateless" mean?
A) The server doesn't store any data
B) Each request contains all necessary information
C) The client doesn't maintain state
D) No database is used

✔ Correct Answer: B
Reason: Stateless means each request must contain all information needed to process it.
Tag: Past Paper

---

### Question 727
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Event Loop
Difficulty: Hard

Question: What will be the output order of the following code?
```javascript
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
```
A) 1, 2, 3, 4
B) 1, 4, 2, 3
C) 1, 4, 3, 2
D) 1, 3, 4, 2

✔ Correct Answer: C
Reason: Synchronous code runs first (1, 4), then microtasks/Promises (3), then macrotasks/setTimeout (2).
Tag: Normal

---

### Question 728
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: Flexbox
Difficulty: Medium

Question: Which CSS property is used to change the direction of flex items?
A) flex-direction
B) flex-flow
C) flex-wrap
D) flex-order

✔ Correct Answer: A
Reason: flex-direction controls whether items flow in rows or columns.
Tag: Normal

---

### Question 729
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Caching
Difficulty: Medium

Question: Which HTTP header is used to control browser caching behavior?
A) Cache-Control
B) Expires
C) ETag
D) All of the above

✔ Correct Answer: D
Reason: All three headers can control caching, though Cache-Control is most modern.
Tag: Normal

---

### Question 730
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Express.js
Difficulty: Medium

Question: In Express.js, what is middleware?
A) A database connection layer
B) Functions that have access to request and response objects
C) A templating engine
D) A routing mechanism

✔ Correct Answer: B
Reason: Middleware functions process requests before they reach route handlers.
Tag: Normal

---

### Question 731
Domain: Web Development
Topic: Databases for Web Applications
Subtopic: MongoDB
Difficulty: Medium

Question: In MongoDB, what is a collection equivalent to in relational databases?
A) Database
B) Table
C) Row
D) Column

✔ Correct Answer: B
Reason: A collection in MongoDB is analogous to a table in SQL databases.
Tag: Normal

---

### Question 732
Domain: Web Development
Topic: Web Security
Subtopic: HTTPS
Difficulty: Easy

Question: What does HTTPS provide that HTTP does not?
A) Faster loading
B) Encryption and security
C) Better SEO only
D) Caching capabilities

✔ Correct Answer: B
Reason: HTTPS encrypts data transmission using SSL/TLS certificates.
Tag: Normal

---

### Question 733
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: State Management
Difficulty: Medium

Question: Which library is commonly used for state management in React applications?
A) Axios
B) Redux
C) Lodash
D) Moment.js

✔ Correct Answer: B
Reason: Redux is a popular state management library for React apps.
Tag: Normal

---

### Question 734
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Accessibility
Difficulty: Medium

Question: Which attribute is used to provide alternative text for images for screen readers?
A) title
B) alt
C) aria-label
D) description

✔ Correct Answer: B
Reason: The alt attribute provides text alternatives for images for accessibility.
Tag: Normal

---

### Question 735
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Positioning
Difficulty: Medium

Question: Which CSS position value removes an element from the normal document flow?
A) relative
B) static
C) absolute
D) sticky

✔ Correct Answer: C
Reason: position: absolute removes the element from normal flow and positions it relative to its positioned ancestor.
Tag: Normal

---

### Question 736
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Scope
Difficulty: Medium

Question: What is the scope of a variable declared with 'let' inside a block?
A) Global scope
B) Function scope
C) Block scope
D) Module scope

✔ Correct Answer: C
Reason: Variables declared with let have block scope, limited to the enclosing {}.
Tag: Normal

---

### Question 737
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: WebSockets
Difficulty: Medium

Question: What is the main advantage of WebSockets over HTTP polling?
A) Better security
B) Real-time bidirectional communication
C) Easier implementation
D) Better browser support

✔ Correct Answer: B
Reason: WebSockets enable full-duplex communication channels over a single TCP connection.
Tag: Normal

---

### Question 738
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Build Tools
Difficulty: Easy

Question: Which tool is commonly used for bundling JavaScript modules?
A) npm
B) Webpack
C) Babel
D) ESLint

✔ Correct Answer: B
Reason: Webpack is a module bundler that packages JavaScript files and assets.
Tag: Normal

---

### Question 739
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Browser DevTools
Difficulty: Easy

Question: Which browser DevTools tab is used to inspect and modify CSS styles?
A) Console
B) Network
C) Elements/Inspector
D) Sources

✔ Correct Answer: C
Reason: The Elements/Inspector tab shows HTML structure and allows CSS inspection.
Tag: Normal

---

### Question 740
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Destructuring
Difficulty: Medium

Question: What will be the output of the following code?
```javascript
const obj = { a: 1, b: 2, c: 3 };
const { a, ...rest } = obj;
console.log(rest);
```
A) { a: 1, b: 2, c: 3 }
B) { b: 2, c: 3 }
C) { a: 1 }
D) undefined

✔ Correct Answer: B
Reason: The rest operator collects remaining properties after destructuring 'a'.
Tag: Normal

---

### Question 741
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: Authentication vs Authorization
Difficulty: Medium

Question: What is the difference between authentication and authorization?
A) They are the same thing
B) Authentication verifies identity; authorization verifies permissions
C) Authorization verifies identity; authentication verifies permissions
D) Authentication is for APIs only

✔ Correct Answer: B
Reason: Authentication confirms who you are; authorization determines what you can access.
Tag: Past Paper

---

### Question 742
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Minification
Difficulty: Easy

Question: What is the purpose of minifying JavaScript and CSS files?
A) Improve code readability
B) Reduce file size for faster loading
C) Add comments
D) Fix syntax errors

✔ Correct Answer: B
Reason: Minification removes whitespace and comments to reduce file size.
Tag: Normal

---

### Question 743
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Meta Tags
Difficulty: Easy

Question: Which meta tag is used to make a website responsive on mobile devices?
A) <meta charset="UTF-8">
B) <meta name="viewport" content="width=device-width, initial-scale=1.0">
C) <meta name="description">
D) <meta http-equiv="refresh">

✔ Correct Answer: B
Reason: The viewport meta tag controls layout on mobile browsers.
Tag: Normal

---

### Question 744
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Grid
Difficulty: Medium

Question: Which CSS property defines the number of columns in a CSS Grid?
A) grid-columns
B) grid-template-columns
C) column-count
D) grid-column-gap

✔ Correct Answer: B
Reason: grid-template-columns defines the column structure of a grid container.
Tag: Normal

---

### Question 745
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Type Coercion
Difficulty: Hard

Question: What will be the output of the following code?
```javascript
console.log([] + []);
console.log([] + {});
console.log({} + []);
```
A) "", "[object Object]", "[object Object]"
B) "", "[object Object]", "0"
C) "undefined", "undefined", "undefined"
D) Error

✔ Correct Answer: A
Reason: Arrays and objects are coerced to strings: "" + "" = "", "" + "[object Object]", "[object Object]" + "".
Tag: Normal

---

### Question 746
Domain: Web Development
Topic: Web Security
Subtopic: SQL Injection
Difficulty: Medium

Question: Which practice best prevents SQL injection attacks?
A) Using client-side validation
B) Using parameterized queries/prepared statements
C) Encrypting the database
D) Using HTTPS

✔ Correct Answer: B
Reason: Parameterized queries separate SQL code from data, preventing injection.
Tag: Past Paper

---

### Question 747
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Session Management
Difficulty: Medium

Question: Where are session data typically stored on the server side?
A) Cookies
B) Local storage
C) Server memory or database
D) Browser cache

✔ Correct Answer: C
Reason: Session data is stored server-side in memory, files, or databases.
Tag: Normal

---

### Question 748
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Component Lifecycle
Difficulty: Medium

Question: In React, which lifecycle method is called after a component is rendered to the DOM?
A) componentWillMount
B) componentDidMount
C) componentWillUpdate
D) shouldComponentUpdate

✔ Correct Answer: B
Reason: componentDidMount runs after the component is inserted into the DOM.
Tag: Normal

---

### Question 749
Domain: Web Development
Topic: Web Architecture & Protocols
Subtopic: DNS
Difficulty: Easy

Question: What does DNS stand for?
A) Domain Name System
B) Dynamic Network Service
C) Data Name Server
D) Digital Network System

✔ Correct Answer: A
Reason: DNS translates domain names to IP addresses.
Tag: Normal

---

### Question 750
Domain: Web Development
Topic: Databases for Web Applications
Subtopic: Database Indexing
Difficulty: Medium

Question: What is the primary purpose of database indexing?
A) Encrypt data
B) Speed up query performance
C) Reduce storage space
D) Backup data

✔ Correct Answer: B
Reason: Indexes create data structures that improve query retrieval speed.
Tag: Normal

---

### Question 751
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Version Control
Difficulty: Easy

Question: Which command is used to create a new branch in Git?
A) git new branch
B) git branch <branch-name>
C) git create branch
D) git add branch

✔ Correct Answer: B
Reason: git branch <branch-name> creates a new branch in Git.
Tag: Normal

---

### Question 752
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Pseudo-classes
Difficulty: Medium

Question: Which CSS pseudo-class selects an element when the mouse hovers over it?
A) :active
B) :hover
C) :focus
D) :visited

✔ Correct Answer: B
Reason: :hover applies styles when the cursor is over an element.
Tag: Normal

---

### Question 753
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: Local Storage
Difficulty: Easy

Question: What is the maximum storage capacity of localStorage in most browsers?
A) 1 MB
B) 5 MB
C) 10 MB
D) Unlimited

✔ Correct Answer: B
Reason: Most browsers limit localStorage to approximately 5-10 MB, commonly 5 MB.
Tag: Normal

---

### Question 754
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Arrow Functions
Difficulty: Medium

Question: What is a key difference between arrow functions and regular functions?
A) Arrow functions are faster
B) Arrow functions don't have their own 'this' binding
C) Arrow functions can't take parameters
D) Arrow functions are always async

✔ Correct Answer: B
Reason: Arrow functions inherit 'this' from their enclosing scope.
Tag: Normal

---

### Question 755
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Error Handling
Difficulty: Medium

Question: Which JavaScript statement is used to handle exceptions?
A) if-else
B) switch-case
C) try-catch
D) throw-error

✔ Correct Answer: C
Reason: try-catch blocks handle runtime errors and exceptions.
Tag: Normal

---

### Question 756
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Variables
Difficulty: Medium

Question: How do you declare a CSS custom property (variable)?
A) $variable-name: value;
B) --variable-name: value;
C) @variable-name: value;
D) var-variable-name: value;

✔ Correct Answer: B
Reason: CSS variables are declared with -- prefix and used with var().
Tag: Normal

---

### Question 757
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: API Versioning
Difficulty: Medium

Question: Which is a common practice for API versioning?
A) /api/users
B) /api/v1/users
C) /users/api
D) /v1api/users

✔ Correct Answer: B
Reason: Including version number in URL path (e.g., /v1/) is a standard practice.
Tag: Normal

---

### Question 758
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Data Attributes
Difficulty: Medium

Question: What is the correct syntax for creating a custom data attribute in HTML?
A) custom-attribute="value"
B) data-attribute="value"
C) attr-attribute="value"
D) x-attribute="value"

✔ Correct Answer: B
Reason: Custom data attributes must start with 'data-' prefix.
Tag: Normal

---

### Question 759
Domain: Web Development
Topic: Web Security
Subtopic: CSRF Protection
Difficulty: Hard

Question: What is the purpose of CSRF tokens?
A) Encrypt user passwords
B) Prevent cross-site request forgery attacks
C) Speed up form submission
D) Validate email addresses

✔ Correct Answer: B
Reason: CSRF tokens verify that requests originate from legitimate users.
Tag: Normal

---

### Question 760
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Environment Variables
Difficulty: Easy

Question: Why should sensitive information like API keys be stored in environment variables?
A) Faster access
B) Security and configuration flexibility
C) Better performance
D) Easier debugging

✔ Correct Answer: B
Reason: Environment variables keep secrets out of code and allow environment-specific configs.
Tag: Normal

---

### Question 761
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Vue.js
Difficulty: Medium

Question: In Vue.js, which directive is used for two-way data binding?
A) v-bind
B) v-model
C) v-on
D) v-if

✔ Correct Answer: B
Reason: v-model creates two-way binding between form inputs and data.
Tag: Normal

---

### Question 762
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Content Delivery Network
Difficulty: Easy

Question: What is the primary benefit of using a CDN (Content Delivery Network)?
A) Better security
B) Faster content delivery through geographically distributed servers
C) Cheaper hosting
D) Automatic backups

✔ Correct Answer: B
Reason: CDNs serve content from servers closest to users, reducing latency.
Tag: Normal

---

### Question 763
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Hoisting
Difficulty: Hard

Question: What will be the output of the following code?
```javascript
console.log(x);
var x = 5;
console.log(x);
```
A) 5, 5
B) undefined, 5
C) Error, 5
D) 5, undefined

✔ Correct Answer: B
Reason: Variable declarations are hoisted but not initializations; x is undefined first, then 5.
Tag: Normal

---

### Question 764
Domain: Web Development
Topic: Databases for Web Applications
Subtopic: Transactions
Difficulty: Medium

Question: What does ACID stand for in database transactions?
A) Atomicity, Consistency, Isolation, Durability
B) Access, Control, Integration, Data
C) Automatic, Consistent, Isolated, Distributed
D) Authentication, Consistency, Integrity, Distribution

✔ Correct Answer: A
Reason: ACID properties ensure reliable database transaction processing.
Tag: Past Paper

---

### Question 765
Domain: Web Development
Topic: Web Architecture & Protocols
Subtopic: WebRTC
Difficulty: Medium

Question: What does WebRTC enable in web browsers?
A) Real-time peer-to-peer communication
B) Faster page loading
C) Better SEO
D) Database connections

✔ Correct Answer: A
Reason: WebRTC enables real-time audio, video, and data sharing between browsers.
Tag: Normal

---

### Question 766
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: Mobile-First Design
Difficulty: Medium

Question: What is the mobile-first approach in responsive design?
A) Designing only for mobile devices
B) Starting with mobile styles and adding complexity for larger screens
C) Testing on mobile devices first
D) Using mobile frameworks only

✔ Correct Answer: B
Reason: Mobile-first means designing for smallest screens first, then progressively enhancing.
Tag: Normal

---

### Question 767
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: CI/CD
Difficulty: Medium

Question: What does CI/CD stand for in software development?
A) Code Integration / Code Deployment
B) Continuous Integration / Continuous Deployment
C) Central Integration / Central Distribution
D) Compiled Integration / Compiled Delivery

✔ Correct Answer: B
Reason: CI/CD automates code integration, testing, and deployment processes.
Tag: Normal

---

### Question 768
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Canvas
Difficulty: Medium

Question: Which HTML5 element is used for drawing graphics via JavaScript?
A) <svg>
B) <canvas>
C) <graphics>
D) <draw>

✔ Correct Answer: B
Reason: The <canvas> element provides a drawing surface for JavaScript graphics.
Tag: Normal

---

### Question 769
Domain: Web Development
Topic: Web Security
Subtopic: Content Security Policy
Difficulty: Hard

Question: Which CSP directive controls which domains can load JavaScript?
A) script-src
B) default-src
C) connect-src
D) style-src

✔ Correct Answer: A
Reason: script-src specifies valid sources for JavaScript execution.
Tag: Normal

---

### Question 770
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Middleware
Difficulty: Medium

Question: What is the purpose of body-parser middleware in Express.js?
A) Compress response bodies
B) Parse incoming request bodies
C) Handle errors
D) Manage sessions

✔ Correct Answer: B
Reason: body-parser extracts and parses the body portion of incoming requests.
Tag: Normal

---

### Question 771
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Prototypes
Difficulty: Hard

Question: What will be the output of the following code?
```javascript
function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {
  return `Hello, ${this.name}`;
};
const john = new Person('John');
console.log(john.greet());
```
A) undefined
B) Hello, John
C) Error
D) Hello, undefined

✔ Correct Answer: B
Reason: The prototype method is accessible to instances created with the constructor.
Tag: Normal

---

### Question 772
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: GraphQL
Difficulty: Medium

Question: What is a key advantage of GraphQL over REST?
A) Better security
B) Clients can request exactly the data they need
C) Faster server processing
D) Easier to implement

✔ Correct Answer: B
Reason: GraphQL allows clients to specify exactly what data they need, avoiding over-fetching.
Tag: Normal

---

### Question 773
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Specificity
Difficulty: Medium

Question: Which CSS rule will be applied if multiple rules target the same element?
A) The first rule in the stylesheet
B) The last rule in the stylesheet
C) The rule with highest specificity
D) A random rule

✔ Correct Answer: C
Reason: CSS applies the rule with highest specificity; if equal, the last one wins.
Tag: Normal

---

### Question 774
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Docker
Difficulty: Medium

Question: What is the primary purpose of Docker in web development?
A) Version control
B) Containerization for consistent environments
C) Code compilation
D) Database management

✔ Correct Answer: B
Reason: Docker packages applications with dependencies into containers for consistency.
Tag: Normal

---

### Question 775
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Angular
Difficulty: Medium

Question: In Angular, what is a directive?
A) A routing configuration
B) A class that adds behavior to elements in the DOM
C) A service for HTTP requests
D) A database connection

✔ Correct Answer: B
Reason: Directives are classes that modify DOM element behavior or appearance.
Tag: Normal

---

### Question 776
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: Integration Testing
Difficulty: Medium

Question: What does integration testing verify?
A) Individual functions work correctly
B) Different modules work together correctly
C) User interface appearance
D) Code syntax

✔ Correct Answer: B
Reason: Integration testing checks that different parts of the system work together.
Tag: Normal

---

### Question 777
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Modules
Difficulty: Medium

Question: Which keyword is used to export a default value from an ES6 module?
A) export
B) export default
C) module.exports
D) return

✔ Correct Answer: B
Reason: export default exports a single default value from a module.
Tag: Normal

---

### Question 778
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: Rate Limiting
Difficulty: Medium

Question: Why is rate limiting important for APIs?
A) Improve performance
B) Prevent abuse and ensure fair usage
C) Reduce server costs
D) Improve SEO

✔ Correct Answer: B
Reason: Rate limiting prevents API abuse by limiting request frequency per client.
Tag: Normal

---

### Question 779
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Iframes
Difficulty: Easy

Question: What does the <iframe> element do?
A) Creates a form
B) Embeds another HTML page within the current page
C) Creates a frame border
D) Defines an image

✔ Correct Answer: B
Reason: <iframe> embeds external content or another webpage within the current page.
Tag: Normal

---

### Question 780
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Code Splitting
Difficulty: Medium

Question: What is code splitting in modern web applications?
A) Dividing code into multiple files manually
B) Breaking code into smaller bundles loaded on demand
C) Separating HTML, CSS, and JavaScript
D) Using multiple programming languages

✔ Correct Answer: B
Reason: Code splitting creates smaller bundles that load only when needed, improving performance.
Tag: Normal

---

### Question 781
Domain: Web Development
Topic: Databases for Web Applications
Subtopic: ORM
Difficulty: Medium

Question: What does ORM stand for in database management?
A) Object Relational Mapping
B) Online Resource Management
C) Operational Record Model
D) Object Resource Manager

✔ Correct Answer: A
Reason: ORM maps database tables to objects in programming languages.
Tag: Normal

---

### Question 782
Domain: Web Development
Topic: Web Security
Subtopic: Password Security
Difficulty: Medium

Question: Which hashing algorithm is recommended for storing passwords?
A) MD5
B) SHA-1
C) bcrypt
D) Base64

✔ Correct Answer: C
Reason: bcrypt is designed for password hashing with built-in salting and slow computation.
Tag: Past Paper

---

### Question 783
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Package Managers
Difficulty: Easy

Question: Which command installs all dependencies listed in package.json?
A) npm start
B) npm install
C) npm init
D) npm update

✔ Correct Answer: B
Reason: npm install reads package.json and installs all listed dependencies.
Tag: Normal

---

### Question 784
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Animations
Difficulty: Medium

Question: Which CSS property is used to define the duration of an animation?
A) animation-time
B) animation-duration
C) animation-speed
D) animation-length

✔ Correct Answer: B
Reason: animation-duration specifies how long an animation takes to complete.
Tag: Normal

---

### Question 785
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Template Literals
Difficulty: Easy

Question: Which character is used to create template literals in JavaScript?
A) Single quotes '
B) Double quotes "
C) Backticks `
D) Forward slash /

✔ Correct Answer: C
Reason: Template literals use backticks and support string interpolation with ${}.
Tag: Normal

---

### Question 786
Domain: Web Development
Topic: Web Architecture & Protocols
Subtopic: Load Balancing
Difficulty: Medium

Question: What is the primary purpose of load balancing?
A) Encrypt data
B) Distribute traffic across multiple servers
C) Cache static content
D) Compress files

✔ Correct Answer: B
Reason: Load balancers distribute incoming requests across multiple servers for better performance.
Tag: Normal

---

### Question 787
Domain: Web Development
Topic: Server-Side Programming
Subtopic: Templating Engines
Difficulty: Medium

Question: Which is a popular templating engine for Node.js?
A) React
B) EJS
C) Bootstrap
D) jQuery

✔ Correct Answer: B
Reason: EJS (Embedded JavaScript) is a templating engine for generating HTML with JavaScript.
Tag: Normal

---

### Question 788
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Transitions
Difficulty: Medium

Question: Which CSS property controls the speed curve of a transition?
A) transition-speed
B) transition-timing-function
C) transition-curve
D) transition-easing

✔ Correct Answer: B
Reason: transition-timing-function defines the acceleration curve (ease, linear, etc.).
Tag: Normal

---

### Question 789
Domain: Web Development
Topic: Frontend Frameworks & Libraries
Subtopic: Single Page Applications
Difficulty: Medium

Question: What is a key characteristic of Single Page Applications (SPAs)?
A) Multiple HTML pages
B) Dynamic content updates without full page reloads
C) No JavaScript required
D) Server-side rendering only

✔ Correct Answer: B
Reason: SPAs update content dynamically using JavaScript without reloading the entire page.
Tag: Normal

---

### Question 790
Domain: Web Development
Topic: Web APIs & Integration
Subtopic: AJAX
Difficulty: Easy

Question: What does AJAX stand for?
A) Asynchronous JavaScript and XML
B) Advanced JavaScript and XML
C) Automatic JavaScript and XML
D) Asynchronous Java and XML

✔ Correct Answer: A
Reason: AJAX enables asynchronous communication with servers without page reloads.
Tag: Normal

---

### Question 791
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Web Storage
Difficulty: Medium

Question: What is the main difference between localStorage and sessionStorage?
A) Storage capacity
B) Data persistence (localStorage persists, sessionStorage clears on tab close)
C) Security level
D) Browser support

✔ Correct Answer: B
Reason: localStorage persists until explicitly cleared; sessionStorage clears when the tab closes.
Tag: Normal

---

### Question 792
Domain: Web Development
Topic: Web Testing & Debugging
Subtopic: End-to-End Testing
Difficulty: Medium

Question: Which tool is commonly used for end-to-end testing of web applications?
A) Jest
B) Cypress
C) ESLint
D) Webpack

✔ Correct Answer: B
Reason: Cypress is a popular framework for automated end-to-end browser testing.
Tag: Normal

---

### Question 793
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Strict Mode
Difficulty: Medium

Question: How do you enable strict mode in JavaScript?
A) "use strict";
B) strict = true;
C) enable strict;
D) mode: strict;

✔ Correct Answer: A
Reason: "use strict"; at the beginning of a script or function enables strict mode.
Tag: Normal

---

### Question 794
Domain: Web Development
Topic: Backend Development Fundamentals
Subtopic: Microservices
Difficulty: Medium

Question: What is a key characteristic of microservices architecture?
A) Single large application
B) Independent, loosely coupled services
C) Monolithic database
D) Single programming language

✔ Correct Answer: B
Reason: Microservices break applications into independent services that can be developed and deployed separately.
Tag: Normal

---

### Question 795
Domain: Web Development
Topic: Web Security
Subtopic: Clickjacking
Difficulty: Medium

Question: Which HTTP header helps prevent clickjacking attacks?
A) Content-Security-Policy
B) X-Frame-Options
C) X-XSS-Protection
D) Access-Control-Allow-Origin

✔ Correct Answer: B
Reason: X-Frame-Options controls whether a page can be displayed in an iframe.
Tag: Normal

---

### Question 796
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Generators
Difficulty: Hard

Question: What does the yield keyword do in a generator function?
A) Stops the function permanently
B) Pauses execution and returns a value
C) Throws an error
D) Restarts the function

✔ Correct Answer: B
Reason: yield pauses generator execution and returns a value, resumable with next().
Tag: Normal

---

### Question 797
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Display Property
Difficulty: Easy

Question: Which CSS display value hides an element but maintains its space in the layout?
A) display: none;
B) visibility: hidden;
C) opacity: 0;
D) display: hidden;

✔ Correct Answer: B
Reason: visibility: hidden hides the element but keeps its layout space; display: none removes it entirely.
Tag: Normal

---

### Question 798
Domain: Web Development
Topic: Deployment & Hosting
Subtopic: Environment Configuration
Difficulty: Easy

Question: Which file is commonly used to store environment variables in Node.js projects?
A) config.js
B) .env
C) settings.json
D) environment.txt

✔ Correct Answer: B
Reason: .env files store environment-specific configuration variables.
Tag: Normal

---

### Question 799
Domain: Web Development
Topic: Web Performance & Optimization
Subtopic: Image Optimization
Difficulty: Medium

Question: Which modern image format provides better compression than JPEG and PNG?
A) GIF
B) BMP
C) WebP
D) TIFF

✔ Correct Answer: C
Reason: WebP provides superior compression and quality compared to JPEG and PNG.
Tag: Normal

---

### Question 800
Domain: Web Development
Topic: Modern Web Development Practices
Subtopic: Semantic Versioning
Difficulty: Medium

Question: In semantic versioning (e.g., 2.4.1), what does the middle number represent?
A) Major version
B) Minor version (new features, backward compatible)
C) Patch version
D) Build number

✔ Correct Answer: B
Reason: Format is MAJOR.MINOR.PATCH; minor version adds features without breaking changes.
Tag: Normal

---

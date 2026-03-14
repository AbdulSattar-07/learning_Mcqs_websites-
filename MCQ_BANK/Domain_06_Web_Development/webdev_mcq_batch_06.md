# Web Development - MCQ Batch 06
## Questions 501-600

---

### Question 501
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Code Output Prediction
Difficulty: Hard

Question: What is the output: console.log(!!"false");
A) false
B) true
C) "false"
D) Error

✔ Correct Answer: B

Reason: Non-empty strings are truthy. !"false" is false, !!"false" is true.

Tag: Normal

---

### Question 502
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Code Output Prediction
Difficulty: Hard

Question: What is the output: console.log(+"10");
A) "10"
B) 10
C) NaN
D) Error

✔ Correct Answer: B

Reason: Unary plus (+) converts string to number: +"10" becomes 10.

Tag: Normal

---

### Question 503
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Code Output Prediction
Difficulty: Medium

Question: What is the output: console.log([1] == [1]);
A) true
B) false
C) undefined
D) Error

✔ Correct Answer: B

Reason: Arrays are objects compared by reference, not value. Different array instances are not equal.

Tag: Normal

---

### Question 504
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Code Output Prediction
Difficulty: Hard

Question: What is the output: console.log(null == undefined);
A) false
B) true
C) null
D) undefined

✔ Correct Answer: B

Reason: null and undefined are loosely equal (==) but not strictly equal (===).

Tag: Normal

---

### Question 505
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Code Output Prediction
Difficulty: Hard

Question: What is the output: console.log(null === undefined);
A) true
B) false
C) null
D) undefined

✔ Correct Answer: B

Reason: Strict equality (===) checks type and value. null and undefined are different types.

Tag: Normal

---

### Question 506
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Specificity Calculation
Difficulty: Hard

Question: Which selector has higher specificity: #id .class or .class .class .class?
A) .class .class .class
B) #id .class
C) Equal
D) Cannot determine

✔ Correct Answer: B

Reason: ID selector (#id) has higher specificity (100) than any number of class selectors (10 each).

Tag: Normal

---

### Question 507
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Specificity Calculation
Difficulty: Hard

Question: Inline styles have specificity of:
A) 100
B) 1000
C) 10
D) Highest (except !important)

✔ Correct Answer: D

Reason: Inline styles have specificity of 1000, higher than any selector (except !important).

Tag: Normal

---

### Question 508
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Form Elements
Difficulty: Medium

Question: Which input type creates a slider?
A) <input type="slider">
B) <input type="range">
C) <input type="number">
D) <input type="scroll">

✔ Correct Answer: B

Reason: type="range" creates a slider control for selecting a numeric value.

Tag: Normal

---

### Question 509
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Form Elements
Difficulty: Medium

Question: Which input type creates a color picker?
A) <input type="color">
B) <input type="picker">
C) <input type="palette">
D) <input type="rgb">

✔ Correct Answer: A

Reason: type="color" creates a color picker interface in HTML5.

Tag: Normal

---

### Question 510
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Form Elements
Difficulty: Medium

Question: The 'autocomplete' attribute:
A) Completes forms automatically
B) Enables/disables browser autocomplete
C) Validates forms
D) Submits forms

✔ Correct Answer: B

Reason: autocomplete attribute controls whether browser should autocomplete form fields.

Tag: Normal

---

### Question 511
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [1,2,3].includes(2) returns:
A) 1
B) true
C) 2
D) false

✔ Correct Answer: B

Reason: includes() checks if array contains a value, returning true or false.

Tag: Normal

---

### Question 512
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [1,2,3].indexOf(2) returns:
A) 2
B) 1
C) true
D) -1

✔ Correct Answer: B

Reason: indexOf() returns the index of the first occurrence (2 is at index 1).

Tag: Normal

---

### Question 513
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [1,2,3].indexOf(5) returns:
A) 5
B) -1
C) undefined
D) null

✔ Correct Answer: B

Reason: indexOf() returns -1 when the element is not found in the array.

Tag: Normal

---

### Question 514
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [1,2,3].slice(1, 2) returns:
A) [1]
B) [2]
C) [1, 2]
D) [2, 3]

✔ Correct Answer: B

Reason: slice(1, 2) extracts from index 1 up to (but not including) index 2: [2].

Tag: Normal

---

### Question 515
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [1,2,3].splice(1, 1) returns and modifies:
A) Returns [2], array becomes [1, 3]
B) Returns [1], array unchanged
C) Returns [1, 2], array becomes [3]
D) Error

✔ Correct Answer: A

Reason: splice(1, 1) removes 1 element at index 1, returns [2], modifies original to [1, 3].

Tag: Normal

---

### Question 516
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [1,2,3].reverse() modifies:
A) Returns new array, original unchanged
B) Modifies original array and returns it
C) Returns reversed string
D) Does nothing

✔ Correct Answer: B

Reason: reverse() modifies the original array in place and returns the reversed array.

Tag: Normal

---

### Question 517
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Medium

Question: [3,1,2].sort() returns:
A) [3, 1, 2]
B) [1, 2, 3]
C) [1, 3, 2]
D) Error

✔ Correct Answer: B

Reason: sort() sorts array in place. Without comparator, converts to strings and sorts: [1, 2, 3].

Tag: Normal

---

### Question 518
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Array Methods
Difficulty: Hard

Question: [10, 5, 20].sort() returns:
A) [5, 10, 20]
B) [10, 20, 5]
C) [20, 10, 5]
D) [5, 20, 10]

✔ Correct Answer: B

Reason: Default sort converts to strings: "10", "20", "5". String sort gives [10, 20, 5].

Tag: Normal

---

### Question 519
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: String Methods
Difficulty: Medium

Question: "hello".charAt(1) returns:
A) "h"
B) "e"
C) 1
D) "l"

✔ Correct Answer: B

Reason: charAt(1) returns the character at index 1: "e".

Tag: Normal

---

### Question 520
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: String Methods
Difficulty: Medium

Question: "hello".substring(1, 3) returns:
A) "h"
B) "el"
C) "ell"
D) "llo"

✔ Correct Answer: B

Reason: substring(1, 3) extracts from index 1 up to (not including) 3: "el".

Tag: Normal

---

### Question 521
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: String Methods
Difficulty: Medium

Question: "hello".slice(-2) returns:
A) "he"
B) "lo"
C) "ll"
D) "o"

✔ Correct Answer: B

Reason: slice(-2) extracts last 2 characters: "lo".

Tag: Normal

---

### Question 522
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: String Methods
Difficulty: Medium

Question: "hello".replace("l", "L") returns:
A) "heLLo"
B) "heLlo"
C) "hello"
D) "HELLO"

✔ Correct Answer: B

Reason: replace() replaces only the first occurrence: "heLlo".

Tag: Normal

---

### Question 523
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: String Methods
Difficulty: Medium

Question: "hello".replaceAll("l", "L") returns:
A) "heLlo"
B) "heLLo"
C) "hello"
D) "HELLO"

✔ Correct Answer: B

Reason: replaceAll() replaces all occurrences: "heLLo".

Tag: Normal

---

### Question 524
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Display Property
Difficulty: Medium

Question: display: inline-block allows:
A) Block behavior only
B) Inline flow with block properties (width, height)
C) Inline behavior only
D) No styling

✔ Correct Answer: B

Reason: inline-block flows inline but accepts width, height, and vertical margins like block elements.

Tag: Normal

---

### Question 525
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Display Property
Difficulty: Medium

Question: display: inline elements:
A) Accept width and height
B) Don't accept width and height
C) Start on new line
D) Are invisible

✔ Correct Answer: B

Reason: Inline elements don't accept width/height properties; they size based on content.

Tag: Past Paper

---

### Question 526
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Display Property
Difficulty: Easy

Question: display: block elements:
A) Flow inline
B) Start on new line and take full width
C) Don't accept width
D) Are invisible

✔ Correct Answer: B

Reason: Block elements start on a new line and take up the full available width by default.

Tag: Past Paper

---

### Question 527
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Margin Collapse
Difficulty: Hard

Question: Vertical margins between adjacent block elements:
A) Add together
B) Collapse to the larger margin
C) Don't apply
D) Always equal

✔ Correct Answer: B

Reason: Vertical margins collapse, taking the larger of the two margins, not adding them.

Tag: Normal

---

### Question 528
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Box Sizing
Difficulty: Medium

Question: box-sizing: border-box includes:
A) Content only
B) Content, padding, and border in width/height
C) Margin in width/height
D) Nothing

✔ Correct Answer: B

Reason: border-box includes padding and border in the element's width/height (not margin).

Tag: Normal

---

### Question 529
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Box Sizing
Difficulty: Medium

Question: box-sizing: content-box (default) means:
A) Width/height includes padding and border
B) Width/height applies to content only
C) Width/height includes margin
D) No sizing

✔ Correct Answer: B

Reason: content-box (default) means width/height applies only to content; padding and border are added.

Tag: Normal

---

### Question 530
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Functions
Difficulty: Hard

Question: clamp(10px, 5vw, 50px) returns:
A) Always 10px
B) 5vw, but never less than 10px or more than 50px
C) Always 50px
D) Random value

✔ Correct Answer: B

Reason: clamp() returns the preferred value (5vw) constrained between min (10px) and max (50px).

Tag: Normal

---

### Question 531
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Functions
Difficulty: Medium

Question: min(50%, 300px) returns:
A) Always 50%
B) Whichever is smaller: 50% or 300px
C) Always 300px
D) Sum of both

✔ Correct Answer: B

Reason: min() returns the smallest value from the list.

Tag: Normal

---

### Question 532
Domain: Web Development
Topic: Advanced CSS & Responsive Design
Subtopic: CSS Functions
Difficulty: Medium

Question: max(50%, 300px) returns:
A) Whichever is larger: 50% or 300px
B) Always 50%
C) Always 300px
D) Sum of both

✔ Correct Answer: A

Reason: max() returns the largest value from the list.

Tag: Normal

---

### Question 533
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Comparison Operators
Difficulty: Medium

Question: "2" > "12" evaluates to:
A) false
B) true
C) Error
D) undefined

✔ Correct Answer: B

Reason: String comparison is lexicographic (character by character): "2" > "1" is true.

Tag: Normal

---

### Question 534
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Comparison Operators
Difficulty: Medium

Question: 2 > "12" evaluates to:
A) true
B) false
C) Error
D) undefined

✔ Correct Answer: B

Reason: "12" is coerced to number 12, so 2 > 12 is false.

Tag: Normal

---

### Question 535
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Logical Operators
Difficulty: Hard

Question: console.log(0 || 1 && 2) outputs:
A) 0
B) 2
C) 1
D) false

✔ Correct Answer: B

Reason: && has higher precedence: (1 && 2) = 2, then (0 || 2) = 2.

Tag: Normal

---

### Question 536
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Logical Operators
Difficulty: Hard

Question: console.log(false || true && false) outputs:
A) true
B) false
C) undefined
D) Error

✔ Correct Answer: B

Reason: && has higher precedence: (true && false) = false, then (false || false) = false.

Tag: Normal

---

### Question 537
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Meta Tags
Difficulty: Medium

Question: <meta charset="UTF-8"> specifies:
A) Page language
B) Character encoding
C) Page title
D) Keywords

✔ Correct Answer: B

Reason: charset attribute specifies the character encoding for the HTML document.

Tag: Normal

---

### Question 538
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Meta Tags
Difficulty: Medium

Question: <meta name="description"> is used for:
A) Page title
B) Page description for search engines
C) Keywords
D) Author name

✔ Correct Answer: B

Reason: Description meta tag provides a brief description of the page for search engines.

Tag: Normal

---

### Question 539
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Link Relations
Difficulty: Medium

Question: <link rel="icon"> specifies:
A) External link
B) Favicon for the page
C) Stylesheet
D) Script

✔ Correct Answer: B

Reason: rel="icon" specifies the favicon (icon) displayed in the browser tab.

Tag: Normal

---

### Question 540
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Script Loading
Difficulty: Medium

Question: <script defer> loads:
A) Immediately, blocking parsing
B) In parallel, executes after HTML parsing
C) Never
D) Before HTML

✔ Correct Answer: B

Reason: defer downloads script in parallel with parsing, executes after HTML is fully parsed.

Tag: Normal

---

### Question 541
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Script Loading
Difficulty: Medium

Question: <script async> loads:
A) After HTML parsing
B) In parallel, executes as soon as available
C) Never
D) Synchronously

✔ Correct Answer: B

Reason: async downloads in parallel and executes immediately when ready, potentially interrupting parsing.

Tag: Normal

---

### Question 542
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Text Properties
Difficulty: Easy

Question: text-decoration: underline adds:
A) Bold text
B) Underline to text
C) Italic text
D) Strike-through

✔ Correct Answer: B

Reason: text-decoration: underline adds an underline beneath the text.

Tag: Normal

---

### Question 543
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Text Properties
Difficulty: Easy

Question: text-transform: uppercase converts:
A) Text to lowercase
B) Text to uppercase
C) First letter to uppercase
D) No change

✔ Correct Answer: B

Reason: text-transform: uppercase converts all text to uppercase letters.

Tag: Normal

---

### Question 544
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Text Properties
Difficulty: Medium

Question: text-transform: capitalize converts:
A) All text to uppercase
B) First letter of each word to uppercase
C) All text to lowercase
D) No change

✔ Correct Answer: B

Reason: capitalize converts the first letter of each word to uppercase.

Tag: Normal

---

### Question 545
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Text Properties
Difficulty: Medium

Question: white-space: nowrap prevents:
A) All whitespace
B) Text from wrapping to new line
C) Spaces between words
D) Text display

✔ Correct Answer: B

Reason: white-space: nowrap prevents text from wrapping to a new line.

Tag: Normal

---

### Question 546
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Text Properties
Difficulty: Medium

Question: text-overflow: ellipsis requires:
A) No other properties
B) overflow: hidden and white-space: nowrap
C) Only overflow: hidden
D) Only white-space: nowrap

✔ Correct Answer: B

Reason: text-overflow: ellipsis requires both overflow: hidden and white-space: nowrap to work.

Tag: Normal

---

### Question 547
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Number Methods
Difficulty: Medium

Question: Number.isInteger(5.0) returns:
A) false
B) true
C) undefined
D) Error

✔ Correct Answer: B

Reason: 5.0 is an integer (5), so Number.isInteger() returns true.

Tag: Normal

---

### Question 548
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Number Methods
Difficulty: Medium

Question: Number.isNaN("NaN") returns:
A) true
B) false
C) undefined
D) Error

✔ Correct Answer: B

Reason: Number.isNaN() checks if value is actually NaN. String "NaN" is not NaN, returns false.

Tag: Normal

---

### Question 549
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Number Methods
Difficulty: Medium

Question: parseFloat("10.5px") returns:
A) NaN
B) 10.5
C) "10.5"
D) 10

✔ Correct Answer: B

Reason: parseFloat() parses string until it encounters non-numeric character: 10.5.

Tag: Normal

---

### Question 550
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Number Methods
Difficulty: Medium

Question: parseInt("10.9") returns:
A) 10.9
B) 10
C) 11
D) NaN

✔ Correct Answer: B

Reason: parseInt() parses integer part only, ignoring decimal: 10.

Tag: Normal

---

### Question 551
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Easy

Question: Math.ceil(4.3) returns:
A) 4
B) 5
C) 4.3
D) 4.5

✔ Correct Answer: B

Reason: Math.ceil() rounds up to the nearest integer: 5.

Tag: Normal

---

### Question 552
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Easy

Question: Math.round(4.5) returns:
A) 4
B) 5
C) 4.5
D) Error

✔ Correct Answer: B

Reason: Math.round() rounds to nearest integer. 4.5 rounds up to 5.

Tag: Normal

---

### Question 553
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Medium

Question: Math.max(1, 5, 3) returns:
A) 1
B) 5
C) 3
D) 9

✔ Correct Answer: B

Reason: Math.max() returns the largest number from the arguments: 5.

Tag: Normal

---

### Question 554
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Medium

Question: Math.min(1, 5, 3) returns:
A) 1
B) 5
C) 3
D) -1

✔ Correct Answer: A

Reason: Math.min() returns the smallest number from the arguments: 1.

Tag: Normal

---

### Question 555
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Medium

Question: Math.abs(-5) returns:
A) -5
B) 5
C) 0
D) Error

✔ Correct Answer: B

Reason: Math.abs() returns the absolute (positive) value: 5.

Tag: Normal

---

### Question 556
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Medium

Question: Math.pow(2, 3) returns:
A) 5
B) 8
C) 6
D) 9

✔ Correct Answer: B

Reason: Math.pow(2, 3) calculates 2^3 = 8.

Tag: Normal

---

### Question 557
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Math Object
Difficulty: Medium

Question: Math.sqrt(16) returns:
A) 8
B) 4
C) 256
D) 2

✔ Correct Answer: B

Reason: Math.sqrt() returns the square root: √16 = 4.

Tag: Normal

---

### Question 558
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Background Properties
Difficulty: Medium

Question: background-repeat: no-repeat does what?
A) Repeats background
B) Displays background once without repeating
C) Removes background
D) Tiles background

✔ Correct Answer: B

Reason: no-repeat displays the background image once without repeating it.

Tag: Normal

---

### Question 559
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Background Properties
Difficulty: Medium

Question: background-position: center centers:
A) Text
B) Background image
C) Element
D) Border

✔ Correct Answer: B

Reason: background-position: center centers the background image within the element.

Tag: Normal

---

### Question 560
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Background Properties
Difficulty: Medium

Question: background-attachment: fixed makes background:
A) Move with scroll
B) Stay fixed relative to viewport
C) Disappear
D) Repeat

✔ Correct Answer: B

Reason: fixed makes the background stay in place relative to the viewport when scrolling.

Tag: Normal

---

### Question 561
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: List Properties
Difficulty: Easy

Question: list-style-type: none removes:
A) List items
B) List markers (bullets/numbers)
C) List padding
D) Entire list

✔ Correct Answer: B

Reason: list-style-type: none removes the markers (bullets or numbers) from list items.

Tag: Normal

---

### Question 562
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: List Properties
Difficulty: Medium

Question: list-style-position: inside places markers:
A) Outside content flow
B) Inside content flow
C) Above list
D) Below list

✔ Correct Answer: B

Reason: inside places list markers inside the content flow, affecting text wrapping.

Tag: Normal

---

### Question 563
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Date Methods
Difficulty: Medium

Question: new Date().getFullYear() returns:
A) Month
B) Current year (4 digits)
C) Day
D) Time

✔ Correct Answer: B

Reason: getFullYear() returns the 4-digit year (e.g., 2024).

Tag: Normal

---

### Question 564
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Date Methods
Difficulty: Medium

Question: new Date().getMonth() returns:
A) Month name
B) Month number (0-11)
C) Month number (1-12)
D) Year

✔ Correct Answer: B

Reason: getMonth() returns month as number from 0 (January) to 11 (December).

Tag: Normal

---

### Question 565
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Date Methods
Difficulty: Medium

Question: new Date().getDate() returns:
A) Full date
B) Day of month (1-31)
C) Day of week
D) Month

✔ Correct Answer: B

Reason: getDate() returns the day of the month (1-31).

Tag: Normal

---

### Question 566
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Date Methods
Difficulty: Medium

Question: new Date().getDay() returns:
A) Day of month
B) Day of week (0-6, Sunday=0)
C) Day name
D) Date string

✔ Correct Answer: B

Reason: getDay() returns day of week as number: 0 (Sunday) to 6 (Saturday).

Tag: Normal

---

### Question 567
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Set Methods
Difficulty: Medium

Question: new Set([1,2,2,3]).size returns:
A) 4
B) 3
C) 2
D) undefined

✔ Correct Answer: B

Reason: Set stores unique values only. [1,2,2,3] becomes {1,2,3}, size is 3.

Tag: Normal

---

### Question 568
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Set Methods
Difficulty: Medium

Question: set.has(value) does what?
A) Adds value
B) Checks if value exists in set
C) Removes value
D) Clears set

✔ Correct Answer: B

Reason: has() checks if a value exists in the set, returning true or false.

Tag: Normal

---

### Question 569
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Set Methods
Difficulty: Medium

Question: set.add(value) does what?
A) Removes value
B) Adds value to set
C) Checks value
D) Clears set

✔ Correct Answer: B

Reason: add() adds a new value to the set (if not already present).

Tag: Normal

---

### Question 570
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Map Methods
Difficulty: Medium

Question: map.set(key, value) does what?
A) Gets value
B) Sets key-value pair
C) Deletes key
D) Clears map

✔ Correct Answer: B

Reason: set() adds or updates a key-value pair in the map.

Tag: Normal

---

### Question 571
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Map Methods
Difficulty: Medium

Question: map.get(key) does what?
A) Sets value
B) Returns value associated with key
C) Deletes key
D) Checks if key exists

✔ Correct Answer: B

Reason: get() returns the value associated with the specified key.

Tag: Normal

---

### Question 572
Domain: Web Development
Topic: Advanced JavaScript
Subtopic: Map Methods
Difficulty: Medium

Question: map.has(key) does what?
A) Gets value
B) Checks if key exists in map
C) Adds key
D) Deletes key

✔ Correct Answer: B

Reason: has() checks if a key exists in the map, returning true or false.

Tag: Normal

---

### Question 573
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Transition Properties
Difficulty: Medium

Question: transition: all 0.3s ease applies to:
A) One property
B) All animatable properties
C) No properties
D) Only colors

✔ Correct Answer: B

Reason: 'all' keyword applies transition to all animatable properties.

Tag: Normal

---

### Question 574
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Transition Properties
Difficulty: Medium

Question: transition-timing-function: ease provides:
A) Linear transition
B) Slow start, fast middle, slow end
C) Fast start, slow end
D) Instant transition

✔ Correct Answer: B

Reason: ease timing function starts slow, speeds up in middle, slows down at end.

Tag: Normal

---

### Question 575
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Transition Properties
Difficulty: Medium

Question: transition-delay: 1s does what?
A) Speeds up transition
B) Delays transition start by 1 second
C) Makes transition last 1 second
D) Removes transition

✔ Correct Answer: B

Reason: transition-delay specifies how long to wait before starting the transition.

Tag: Normal

---

### Question 576
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Animation Properties
Difficulty: Medium

Question: animation-iteration-count: infinite makes animation:
A) Run once
B) Run continuously
C) Never run
D) Run twice

✔ Correct Answer: B

Reason: infinite makes the animation repeat continuously without stopping.

Tag: Normal

---

### Question 577
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Animation Properties
Difficulty: Medium

Question: animation-direction: alternate does what?
A) Plays forward only
B) Alternates between forward and backward
C) Plays backward only
D) Stops animation

✔ Correct Answer: B

Reason: alternate makes animation play forward, then backward, alternating each iteration.

Tag: Normal

---

### Question 578
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Animation Properties
Difficulty: Medium

Question: animation-fill-mode: forwards keeps:
A) Initial state
B) Final state after animation ends
C) No state
D) Middle state

✔ Correct Answer: B

Reason: forwards retains the final keyframe styles after the animation completes.

Tag: Normal

---

### Question 579
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Table Elements
Difficulty: Medium

Question: <thead> element contains:
A) Table footer
B) Table header rows
C) Table body
D) Table caption

✔ Correct Answer: B

Reason: <thead> groups header content (column headings) in a table.

Tag: Normal

---

### Question 580
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Table Elements
Difficulty: Medium

Question: <tbody> element contains:
A) Table header
B) Table body content (data rows)
C) Table footer
D) Table caption

✔ Correct Answer: B

Reason: <tbody> groups the body content (main data rows) in a table.

Tag: Normal

---

### Question 581
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Table Elements
Difficulty: Medium

Question: colspan attribute:
A) Spans multiple rows
B) Spans multiple columns
C) Sets column width
D) Removes columns

✔ Correct Answer: B

Reason: colspan makes a cell span across multiple columns.

Tag: Normal

---

### Question 582
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Table Elements
Difficulty: Medium

Question: rowspan attribute:
A) Spans multiple columns
B) Spans multiple rows
C) Sets row height
D) Removes rows

✔ Correct Answer: B

Reason: rowspan makes a cell span across multiple rows.

Tag: Normal

---

### Question 583
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Boolean Conversion
Difficulty: Medium

Question: Boolean("") returns:
A) true
B) false
C) ""
D) undefined

✔ Correct Answer: B

Reason: Empty string is falsy, so Boolean("") returns false.

Tag: Normal

---

### Question 584
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Boolean Conversion
Difficulty: Medium

Question: Boolean("0") returns:
A) false
B) true
C) 0
D) undefined

✔ Correct Answer: B

Reason: Non-empty strings are truthy, even "0". Boolean("0") returns true.

Tag: Normal

---

### Question 585
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Boolean Conversion
Difficulty: Medium

Question: Boolean([]) returns:
A) false
B) true
C) []
D) undefined

✔ Correct Answer: B

Reason: Empty arrays are truthy objects. Boolean([]) returns true.

Tag: Normal

---

### Question 586
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Boolean Conversion
Difficulty: Medium

Question: Boolean({}) returns:
A) false
B) true
C) {}
D) undefined

✔ Correct Answer: B

Reason: Empty objects are truthy. Boolean({}) returns true.

Tag: Normal

---

### Question 587
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Flexbox Alignment
Difficulty: Medium

Question: align-items: center in flexbox:
A) Aligns along main axis
B) Aligns along cross axis
C) Does nothing
D) Removes items

✔ Correct Answer: B

Reason: align-items aligns flex items along the cross axis (perpendicular to main axis).

Tag: Normal

---

### Question 588
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Flexbox Alignment
Difficulty: Medium

Question: align-self allows:
A) Aligning all items
B) Overriding align-items for individual item
C) Aligning container
D) Nothing

✔ Correct Answer: B

Reason: align-self allows individual flex items to override the align-items value.

Tag: Normal

---

### Question 589
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Flexbox Properties
Difficulty: Medium

Question: flex-grow: 1 makes item:
A) Shrink
B) Grow to fill available space
C) Stay fixed
D) Disappear

✔ Correct Answer: B

Reason: flex-grow defines the ability for a flex item to grow if necessary.

Tag: Normal

---

### Question 590
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Flexbox Properties
Difficulty: Medium

Question: flex-shrink: 0 prevents item from:
A) Growing
B) Shrinking
C) Displaying
D) Moving

✔ Correct Answer: B

Reason: flex-shrink: 0 prevents the flex item from shrinking if necessary.

Tag: Normal

---

### Question 591
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Flexbox Properties
Difficulty: Medium

Question: flex-basis sets:
A) Flex direction
B) Initial size of flex item before growing/shrinking
C) Flex wrap
D) Alignment

✔ Correct Answer: B

Reason: flex-basis defines the initial main size of a flex item before space distribution.

Tag: Normal

---

### Question 592
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Grid Properties
Difficulty: Hard

Question: grid-column: 1 / 3 makes item span:
A) 1 column
B) 2 columns (from line 1 to 3)
C) 3 columns
D) All columns

✔ Correct Answer: B

Reason: Grid lines are numbered; 1 / 3 spans from line 1 to line 3 (2 columns).

Tag: Normal

---

### Question 593
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Grid Properties
Difficulty: Hard

Question: grid-row: 1 / span 2 makes item:
A) Span 1 row
B) Span 2 rows starting from row 1
C) Span all rows
D) Disappear

✔ Correct Answer: B

Reason: span 2 makes the item span 2 rows starting from the specified line.

Tag: Normal

---

### Question 594
Domain: Web Development
Topic: CSS Fundamentals
Subtopic: Grid Properties
Difficulty: Medium

Question: gap: 10px in grid creates:
A) No space
B) 10px space between grid items
C) 10px padding
D) 10px margin

✔ Correct Answer: B

Reason: gap (or grid-gap) creates spacing between grid rows and columns.

Tag: Normal

---

### Question 595
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Variable Scope
Difficulty: Hard

Question: Variables declared with var are:
A) Block-scoped
B) Function-scoped
C) Global only
D) Not scoped

✔ Correct Answer: B

Reason: var is function-scoped (or globally scoped if outside function), not block-scoped.

Tag: Past Paper

---

### Question 596
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Variable Scope
Difficulty: Medium

Question: Variables declared with let are:
A) Function-scoped
B) Block-scoped
C) Global only
D) Not scoped

✔ Correct Answer: B

Reason: let and const are block-scoped, limited to the block they're declared in.

Tag: Past Paper

---

### Question 597
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Variable Scope
Difficulty: Medium

Question: const variables:
A) Can be reassigned
B) Cannot be reassigned
C) Are not scoped
D) Are function-scoped

✔ Correct Answer: B

Reason: const creates a read-only reference; the variable cannot be reassigned.

Tag: Past Paper

---

### Question 598
Domain: Web Development
Topic: JavaScript Fundamentals
Subtopic: Variable Scope
Difficulty: Hard

Question: const obj = {a: 1}; obj.a = 2; is:
A) Error
B) Valid (object properties can be modified)
C) Invalid syntax
D) Undefined behavior

✔ Correct Answer: B

Reason: const prevents reassignment of the variable, but object properties can still be modified.

Tag: Normal

---

### Question 599
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Accessibility
Difficulty: Medium

Question: role="button" attribute:
A) Creates button
B) Indicates element acts as button for screen readers
C) Styles element
D) Removes element

✔ Correct Answer: B

Reason: ARIA role attribute indicates the element's purpose to assistive technologies.

Tag: Normal

---

### Question 600
Domain: Web Development
Topic: HTML Fundamentals
Subtopic: Accessibility
Difficulty: Medium

Question: aria-label attribute:
A) Creates label element
B) Provides accessible label for screen readers
C) Styles label
D) Removes label

✔ Correct Answer: B

Reason: aria-label provides an accessible label for elements when visible label isn't present.

Tag: Normal

---

# JavaScript Questions

### Q. Explain how `this` works in JavaScript.

### A.
`this` is the JavaScript context object in which the current code is executing. In most cases, the value of `this` is determined by how a function is called.

* Global context: In the global execution context (outside of any function), `this` refers to the global object whether in strict mode or not.


* Function context: Inside a function, the value of `this` depends on how the function is called.

  - Where a function uses the `this` keyword in its body, its value can be bound to a particular object in the call using the  `Function.prototype.call()` or  `Function.prototype.apply()` methods

  ```javascript
  // An object can be passed as the first argument to call or apply and this will be bound to it.
  var obj = { a: 'Custom' };

  // This property is set on the global object
  var a = 'Global';

  function whatsThis() {
    return this.a;  // The value of this is dependent on how the function is called
  }

  whatsThis();          // 'Global'
  whatsThis.call(obj);  // 'Custom'
  whatsThis.apply(obj); // 'Custom'
  ```

  - Where the value of `this` is not set by the call, `this` will default to the global object, which is window in a browser.(Global in Node.js)
  - In strict mode, however, the value of `this` remains at whatever it was set to when entering the execution context

  ```javascript
  // strict mode
  function f2() {
    'use strict'; // see strict mode
    return this;
  }

  f2() === undefined; // true, because f2 was called directly and not as a method or property of an object (e.g. window.f2())
  ```

  - ES5 `Function.prototype.bind()` method: Creates a new function with the same body and scope, permanently bound to the first argument of bind. Bind only works once.
  - Arrow function: In arrow functions, `this` retains the value of the enclosing lexical context's `this`. No matter what, arrow functions' `this` is set to what it was when it was created.


* As an object method
  - When a function is called as a method of an object, its `this` is set to the object the method is called on.
  - The `this` binding is only affected by the most immediate member reference.

  ```javascript
  var o = {prop: 37};

  function independent() {
    return this.prop;
  }

  o.f = independent;

  console.log(o.f()); // 37

  o.b = {g: independent, prop: 42};
  console.log(o.b.g()); // 42
  ```


* As a constructor
  - When a function is used as a constructor (with the new keyword), its `this` is bound to the new object being constructed.


* As a DOM event handler
  - When a function is used as an event handler, its this is set to the element the event fired from.


* In an inline event handler
  - When the code is called from an inline on-event handler, its `this` is set to the DOM element on which the listener is placed


### Q. Can you explain what `Function.call` and `Function.apply` do? What's the notable difference between the two?

### A.
Both are used to set the value of this explicitly. While `call` takes a list of arguments in comma separated format, `apply` takes an array with list of arguments. (a for array, c for comma.)


### Q. Explain `Function.prototype.bind`.

### A.
Function.prototype.bind is used to set this explicitly. It returns a function with given this context that can be called later. Creates a new function with the same body and scope, permanently bound to the first argument of bind. Bind only works once.


### Q. Explain how prototypal inheritance works.

### A.
In JavaScript, objects have a special hidden property `[[Prototype]]` (as named in the specification), that is either null or references another object. That object is called "a prototype". When trying to access a property of an object, the property will not only be sought on the object but on the prototype of the object, the prototype of the prototype, and so on until either a property with a matching name is found or the end of the prototype chain is reached(null).


### Q. What's the difference between a variable that is: `null`, `undefined` or undeclared?
* How would you go about checking for any of these states?

### A.
Undeclared is any variable that has not been declared yet. Console throws an error for this. Undefined is a declared variable that has no assigned value, yet. `null` is a special value which represents "nothing", "empty" or "value unknown".
The meaning of `undefined` is "value is not assigned".
```javascript
let a;        // undefined
let b = null; // null
c             // undeclared
typeof(b)     // object. It is an officially recognized error in typeof, kept for compatibility.
```


### Q. What is a closure, and how/why would you use one?

### A.

```javascript
function makeAdder(x) {
  return function(y) {
    return x + y;
  };
}

var add5 = makeAdder(5);
var add10 = makeAdder(10);

console.log(add5(2));  // 7
console.log(add10(2)); // 12
```

A closure is the combination of a function and the lexical environment within which that function was declared. This environment consists of any local variables that were in-scope at the time the closure was created. Closures are useful because they let you associate some data (the lexical environment) with a function that operates on that data.

In the above example we use our function factory to create two new functions — one that adds 5 to its argument, and one that adds 10. `add5` and `add10` are both closures. They share the same function body definition, but store different lexical environments. In `add5`'s lexical environment, `x` is 5, while in the lexical environment for `add10`, `x` is 10.

Use cases:
  - You can use a closure anywhere that **you might normally use an object with only a single method.** ex) event handler
  - [Emulating private methods with closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures#Emulating_private_methods_with_closures)


### Q. Explain event delegation.

### A.
Attaching event listeners to parent node, instead of every child, present or newly created, is event delegation. It makes use of event bubbling, where the event on a child bubbles up to the parent. So instead of adding an event listener to a child, and adding one every time a new child is added, we add the listener on parent.


### Q. Describe event bubbling.

### A.
When an event happens on an element, it first runs the handlers on it, then on its parent, then all the way up on other ancestors. Almost all events bubble. For instance, a focus event does not bubble. There are other examples too. The most deeply nested element that caused the event is called a target element, accessible as `event.target`.

A bubbling event goes from the target element straight up. Normally it goes upwards till <html>, and then to document object, and some events even reach window, calling all handlers on the path.

But any handler may decide that the event has been fully processed and stop the bubbling.

The method for it is `event.stopPropagation()`.


### Q. Describe event capturing.

### A.
The standard DOM Events describes 3 phases of event propagation:

1. Capturing phase – the event goes down to the element.
2. Target phase – the event reached the target element.
3. Bubbling phase – the event bubbles up from the element.

The capturing phase is rarely used. Normally it is invisible to us. Handlers added using `on<event>`-property or using HTML attributes or using `addEventListener(event, handler)` don't know anything about capturing, they only run on the 2nd and 3rd phases. To catch an event on the capturing phase, we need to set the 3rd argument of `addEventListener` to `true`.


### Q. What's the difference between host objects and native objects?

### A.
Host — objects provided by environment like window, document by browser. Native — object in an ECMAScript implementation whose semantics are fully defined by this specification rather than by the host environment. Eg. Array, String etc.


### Q. What's the difference between feature detection, feature inference, and using the UA string?

### A.
Feature detection checks a feature for existence, e.g.:

```javascript
if (window.XMLHttpRequest) {
    new XMLHttpRequest();
}
```

Feature inference checks for a feature just like feature detection, but uses another function because it assumes it will also exist, e.g.:

```javascript
if (document.getElementsByTagName) {
    element = document.getElementById(id);
}
```

Checking the UA string is an old practice and should not be used anymore. You keep changing the UA checks and never benefit from newly implemented features, e.g.:

```javascript
if (navigator.userAgent.indexOf("MSIE 7") > -1){
    //do something
}
```


### Q. What's the difference between an "attribute" and a "property"?

### A.
When writing HTML source code, you can define attributes on your HTML elements. Then, once the browser parses your code, a corresponding DOM node will be created. This node is an object, and therefore it has properties. Attributes are defined by HTML. Properties are defined by DOM. Some HTML attributes have 1:1 mapping onto properties. id is one example of such. Some do not


### Q. What language constructions do you use for iterating over object properties and array items?

### A.
for loop, for..in, for each..in, map, reduce etc


### Q. Explain the differences on the usage of `foo` between `function foo() {}` and `var foo = function() {}`

### A.
First one is declaration defined at parse time while the other is expression defined at run time. Function declarations load before any code is executed. Function expressions load only when the interpreter reaches that line of code.

* Can you describe the main difference between the `Array.forEach()` loop and `Array.map()` methods and why you would pick one versus the other?


### Q. Explain "hoisting".

### A.
Variable declarations (and declarations in general) are processed before any code is executed, declaring a variable anywhere in the code is equivalent to declaring it at the top. All variable declarations are hoisted (lifted and declared) to the top of the function, if defined in a function, or the top of the global context, if outside a function. It is important to know that only variable declarations are hoisted to the top, not variable initialization or assignments (when the variable is assigned a value).


### Q. What is the difference between `==` and `===`?

### A.
When comparing values of different types, JavaScript converts the values to numbers. For example, string '01' becomes a number 1. For boolean values, true becomes 1 and false becomes 0. A strict equality operator `===` checks the equality without type conversion.


### Q. Why is it called a Ternary operator, what does the word "Ternary" indicate?

### A.
"Ternary" means operands with three(n-ary) param. This is a one-line shorthand for an if-then statement. It is called a ternary operator or a conditional operator.


### Q. What tools and techniques do you use debugging JavaScript code?

### A.
Web/Browser console using `console.log`. Developer Tools.


### Q. Explain the difference between: `function Person(){}`, `var person = Person()`, and `var person = new Person()`?

### A.
`function Person() {}`: This defined a function. The convention is that if a function name starts with a capital letter then that function defines a constructor (similar to a class in other languages).

`var person = new Person()`:
1. `new` creates a new object.
2. The newly created object has it's prototype set to whatever the Person's prototype is right now.
3. Finally the constructor function is called (the body of Person) with any references to `this` replaced with the object created in step 1.

`var person = Person()`: Everything is ruined
1. Step 1 (the plain old empty JS object) doesn't happen.
2. Step 2 (setting the prototype) doesn't happen.
3. Step 3 (constructor with this set) tries to happen. It really does it's very best. Since there's no new object to set this to, JS does the next best thing and uses the default this, the window.

It's possible that the Person constructor was written to avoid just this pitfall. It would look something like this:

```javascript
function Person(name) {
  if (this instanceof Person) {
    this.name = name;
  } else {
    return new Person(name);
  }
}
Person.prototype.introduce = function() {
  console.log("Hi, my name is " + this.name);
}
```


### Q. What is strict mode? What are some of the advantages/disadvantages of using it?

### A.
Strict Mode is a new feature in ECMAScript 5 that allows you to place a program, or a function, in a "strict" operating context. This strict context prevents certain actions from being taken and throws more exceptions (generally providing the user with more information and a tapered-down coding experience).

Pros:
It catches some common coding bloopers, throwing exceptions.
It prevents, or throws errors, when relatively “unsafe” actions are taken (such as gaining access to the global object).
It disables features that are confusing or poorly thought out.

Cons:
Browsers not supporting strict mode will run strict mode code with different behavior from browsers that do, so don’t rely on strict mode.


### Q. What are the differences between variables created using `let`, `var` or `const`?

### A.
`var`:
* Scope: `var` declarations are globally scoped or function/locally scoped
* `var` variables can be re-declared and updated. That means that we can do this within the same scope and won't get an error. This can cause some issues.

```javascript
var greeter = "hey hi";
var times = 4;

if (times > 3) {
  var greeter = "say Hello instead";
}

console.log(greeter) //"say Hello instead"
```

* Hoisting of `var`: Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their scope before code execution.

```javascript
console.log (greeter);
var greeter = "say hello"

// it is interpreted as this
var greeter;
console.log(greeter); //greeter is undefined
greeter = "say hello"
```

`let`:
* Scope: `let` is block scoped. A block is chunk of code bounded by {}.
* `let` can be updated but not re-declared.
* Hoisting of `let`: Just like `var`, `let` declarations are hoisted to the top. Unlike `var` which is initialized as undefined, the `let` keyword is not initialized. So if you try to use a `let` variable before declaration, you'll get a Reference Error.

`const`:
* Scope: `const` is block scoped.
* `const` cannot be updated or re-declared.
* Hoisting of `const`: Just like `let`, `const` declarations are hoisted to the top but are not initialized.


### Q. What's a typical use case for anonymous functions?

### A.
Since Anonymous Functions are function expressions rather than the regular function declaration which are statements. Function expressions are more flexible. We can assign functions to variables, object properties, pass them as arguments to other functions, and even write a simple one line code enclosed in an anonymous functions.


### Q. Explain the difference between mutable and immutable objects.
* How can you achieve immutability in your own code?

### A.

* What is an example of an immutable object in JavaScript?
  - Mutable is a type of variable that can be changed. In JavaScript, only objects and arrays are mutable, not primitive values.
  - A mutable object is an object whose state can be modified after it is created. Immutables are the objects whose state cannot be changed once the object is created.
  - String and Numbers are Immutable. (You can make a variable name point to a new value, but the previous value is still held in memory. Hence the need for garbage collection.)
* What are the pros and cons of immutability?
  - Immutability: You are always creating a copy of the old data structure and applying the changes to the copy instead of changing the original data structure.
  - pros: Simpler Programming
    - Persistence: You have access to the older versions of your data structure until you use garbage collection method to get rid of it
    - Easier to Debug: Since immutability stresses removing all side-effects and using pure functions, this allows programmers to focus on one function that may have created the bug instead of following this chain of references to see what function possibly mutated our original data structure.
    - Easier Deep Value Comparisons: Since you’re always creating new copies of the old data structure in memory, you can just compare the memory locations of the data structures to see if their values are the same or not.
    - Concurrency: Immutability makes it easier to manage concurrency (without locks or snapshots).
  - cons: It makes some operations harder
    - Modifying state in large objects quickly,
    - Making copies and keeping them takes SPACE.
    - keeping a running state, etc.


### Q. What is the definition of a higher-order function?

### A.
A higher-order function is a function that can take another function as an argument, or that returns a function as a result.

ex) callback functions: Since JavaScript is single-threaded, meaning that only one operation happens at a time, each operation that’s going to happen is queued along this single thread. The strategy of passing in a function to be executed after the rest of the parent function’s operations are complete is one of the basic characteristics of languages that support higher-order functions. It allows for asynchronous behavior, so a script can continue executing while waiting for a result.


### Q. Can you give an example of a curry function and why this syntax offers an advantage?

### A.
currying is the technique of translating the evaluation of a function that takes multiple arguments into evaluating a sequence of functions, each with a single argument. For example, a function that takes two arguments, one from X and one from Y, and produces outputs in Z, by currying is translated into a function that takes a single argument from X and produces as outputs functions from Y to Z. Currying is related to, but not the same as, partial application.

```javascript
const sum = x => y => x + y;
sum (2)(1);   // returns the number 3
sum (2);      // returns a function y => 2 + y
```

Curried functions are great to improve code reusability and functional composition.

* Partial application
  - A partial application is a function which has been applied to some, but not yet all of its arguments. In other words, it’s a function which has some arguments fixed inside its closure scope.
  - Partial applications can take as many or as few arguments a time as desired. Curried functions on the other hand always return a unary function.
  - All curried functions return partial applications, but not all partial applications are the result of curried functions.

#### 6 fundamental terms in functional JavaScript

Lambda => Arrow function
* The term lambda originates from lambda calculus, a formal system of mathematical logic. Lambda calculus is of course Turing complete and as such it represents a universal model of computation able to build any Turing machine.

First-class function
* A first-class citizen (also type, object, entity, or value) in a given programming language is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, modified, and assigned to a variable

Higher-order function
* Higher-order function is a function that accepts other function as an argument or returns a function as a return value.
* First-order function is a function that doesn’t accept other function as an argument and doesn’t return a function as its return value.

Unary function
* Unary function (i.e. monadic) is a function that accepts exactly one argument.

Pure Function
* A pure function is a function where the return value is only determined by its arguments without any side effects. That means that if you give a pure function the same argument a hundred times in a hundred different places of your whole application, the function will always return the same value. No external states will be changed or read by the pure function.
* Examples
  - `array.prototype.push()`: Push function is impure itself and it alters the array it is called on and as such produces a side effect.
  - `array.prototype.concat()`: Concat on the other hand takes the array and concatenates it with the other array producing a whole new array without side effects.
* Pure functions are important as they simplify unit testing (no side effects and no need for dependency injection), they avoid tight coupling and by removing side effects, they make your application harder to break.


### Q. Imperative versus declarative code… what’s the difference?

### A.

Imperative paradigm
* Procedural and object-oriented programming belong under imperative paradigm (C, C++, C#, PHP, Java and of course Assembly).
* Code focuses on creating statements that **change program states** by creating algorithms that tell the computer **how to do things**. It closely relates to how hardware works.
* Typically your code will make use of *conditinal statements, loops and class inheritence*.


Declarative paradigm
* Logic, functional and domain-specific languages belong under declarative paradigms and they are not always Turing-complete (they are not always universal programming languages). (HTML, XML, CSS, SQL, Prolog, Haskell, F# and Lisp)
* Declarative code focuses on building logic of software without actually describing its flow. You are saying **what** without adding **how**.
* You create **expressions instead of statements** and evaluate functions.


### Q. Why you might want to create static class members?

### A.

The `static` keyword defines a static method for a class. Static methods aren't called on instances of the class. Instead, they're called on the class itself. These are often utility functions, such as functions to create or clone objects. It is common to use static methods as an alternative constructor.


### Q. Explain the difference between synchronous and asynchronous functions.

### A.
Synchronous way: It waits for each operation to complete, after that only it executes the next operation.
Asynchronous way: It never waits for each operation to complete, rather it executes all operations in the first  only. The result of each operation will be handled once the result is available.


### Q. What is event loop?
* What is the difference between call stack and task queue?

### A.
JavaScript has a concurrency model based on an "event loop". The event loop got its name because of how it's usually implemented, which usually resembles:

```javascript
while (queue.waitForMessage()) {
  queue.processNextMessage();
}
```

`queue.waitForMessage()` waits synchronously for a message to arrive if there is none currently. The loop gives priority to the call stack, and it first processes everything it finds in the call stack, and once there’s nothing in there, it goes to pick up things in the message queue.

* Run-to-completion
  - Each message is processed completely before any other message is processed.
  - A downside of this model is that if a message takes too long to complete, the web application is unable to process user interactions like click or scroll.


* Adding messages
  - In web browsers, messages are added anytime an event occurs and there is an event listener attached to it. If there is no listener, the event is lost.
  - The function `setTimeout` is called with 2 arguments: a message to add to the queue, and a time value (optional; defaults to 0). The time value represents the (minimum) delay after which the message will actually be pushed into the queue. If there are messages, the `setTimeout` message will have to wait for other messages to be processed.


* Zero delays
  - Zero delay doesn't actually mean the call back will fire-off after zero milliseconds. The execution depends on the number of waiting tasks in the queue.


* Never blocking
  - A very interesting property of the event loop model is that JavaScript, unlike a lot of other languages, never blocks. Handling I/O is typically performed via events and callbacks, so when the application is waiting for an IndexedDB query to return or an XHR request to return, it can still process other things like user input.


* Structure
  - Stack: Function calls form a stack of frames.
  - Heap: Objects are allocated in a heap which is just a name to denote a large mostly unstructured region of memory.
  -  Queue:
    - A JavaScript runtime uses a message queue, which is a list of messages to be processed. Each message has an associated function which gets called in order to handle the message.
    - At some point during the event loop, the runtime starts handling the messages on the queue, starting with the oldest one. To do so, the message is removed from the queue and its corresponding function is called with the message as an input parameter. As always, calling a function creates a new stack frame for that function's use.
    - The processing of functions continues until the stack is once again empty; then the event loop will process the next message in the queue (if there is one).










### Unsolved
* What are the differences between ES6 class and ES5 function constructors?
* Can you offer a use case for the new arrow `=>` function syntax? How does this new syntax differ from other functions?
* What advantage is there for using the arrow syntax for a method in a constructor?
* Can you give an example for destructuring an object or an array?
* Can you give an example of generating a string with ES6 Template Literals?
* What are the benefits of using `spread syntax` and how is it different from `rest syntax`?
* How can you share code between files?


* What are the pros and cons of extending built-in JavaScript objects?
* Explain the same-origin policy with regards to JavaScript.
* What are some of the advantages/disadvantages of writing JavaScript code in a language that compiles to JavaScript?

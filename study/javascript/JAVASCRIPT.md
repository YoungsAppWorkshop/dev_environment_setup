# Udacity: Object-Oriented JavaScript


## Lesson 1. Scope
### Lexical Scope
* The regions in source code where you can refer to a variable by name without getting access errors.
* After defining a variable in a lexical scope, you may make reference to that variable from anywhere else in that lexical scope.
* In simple programs with no functions at all, there's only one lexical scope, global scope.
* A new lexical scope is created every time you type out a function definition. You can access variables from broader lexical scopes containing the inner lexical scope, but variables defined in inner scopes cannot be referred to from outside of the scope.
* Notes:
  - In JavaScript, braces in if-else statements, for/while-loop do not create new scopes.
  - Variables declared without `var` keyword are defined in the global scope.


### Execution Contexts (In-Memory Scope)
* When a program runs, it builds up storage systems for holding the variables and their values. These in-memory scope structures are called execution contexts.
* Execution contexts are build as the code runs, not as it's typed.
* Execution contexts rule which variables a program has access to at different points during the execution.
* In-Memory scopes look similar to In-Memory objects, but they're completely separate by the interpreter.


## Lesson 2. Closures
* A closure is any function that somehow remains available after those outer scopes have returned


## Lesson 3. The `this` keyword
* Generally, `this` isn't bound to
  - the object created by the literal `this` appears within
  - the function object `this` appears within
  - 'a new instance of' the function `this` appears within (generally)
  - an object that happens to have that function as a property
  - an 'execution context' or 'scope' of that function call


* Generally, `this` is bound to
  - The object found to the left of the dot where the containing function is called. (90%)
  - The value that appears on the left of that dot will automatically be given the name `this` inside of that function invocation.
  - If there's no dot, `this` is bound to the global object.


## Lesson 4. Prototype Chains

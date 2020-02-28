# Coding Questions

## Study Later

Question: How would you make this work?

```js
add(2, 5); // 7
add(2)(5); // 7
```

Question: What is the value of `foo.x`?

```js
var foo = {n: 1};
var bar = foo;
foo.x = foo = {n: 2};
```

Answer: [Stack Over Flow](https://stackoverflow.com/questions/34933210/why-is-the-value-of-foo-x-undefined-in-foo-x-foo-n-2/34933473)


Question: What does the following code print?

```js
console.log('one');
setTimeout(function() {
  console.log('two');
}, 0);
Promise.resolve().then(function() {
  console.log('three');
})
console.log('four');
```

Question: What is the difference between these four promises?

```js
doSomething().then(function () {
  return doSomethingElse();
});

doSomething().then(function () {
  doSomethingElse();
});

doSomething().then(doSomethingElse());

doSomething().then(doSomethingElse);
```


## Problem Solved

Question: What is the value of `foo`?

```js
var foo = 10 + '20';
```

Question: What will be the output of the code below?

```js
console.log(0.1 + 0.2 == 0.3);
```

Question: What value is returned from the following statement?

```js
"i'm a lasagna hog".split("").reverse().join("");
```

Question: What is the value of `window.foo`?

```js
( window.foo || ( window.foo = "bar" ) );
```

Question: What is the outcome of the two alerts below?

```js
var foo = "Hello";
(function() {
  var bar = " World";
  alert(foo + bar);
})();
alert(foo + bar);
```

Question: What is the value of `foo.length`?

```js
var foo = [];
foo.push(1);
foo.push(2);
```

# Building Enterprise JavaScript Applications

Li, Daniel.
Building Enterprise JavaScript Applications: Learn to build and deploy robust JavaScript applications using Cucumber, Mocha, Jenkins, Docker, and Kubernetes.
Packt Publishing. Kindle Edition.

## Chapter 2. The State of JavaScript

### Evolution of the web application

#### Client-Server model

Browsers would send a request to one of Example Corp's servers, which retrieves the resource requested, and sends it back to the client. The browser then parses the HTML, retrieves all the files the web page depends on, such as CSS, JavaScript, and media files, and renders it onto the page.

In this model, most of the processing is handled server-side; the client's role is limited to simple and superficial uses. This model was popular in the 1990s and 2000s, when web browsers were not very powerful.

#### Just-in-time (JIT) compilers

Between 2008 and 2009, Mozilla, the company behind Firefox, slowly introduced TraceMonkey, the first Just-in-time (JIT) compiler for JavaScript. Similarly, the V8 JavaScript Engine, which powers Chrome and Safari, and Chakra, which powers Internet Explorer and Edge, also included a JIT compiler.

Traditionally, the JavaScript engine uses an interpreter, which translates the JavaScript source code into machine code that your computer can run.

The JIT compiler improved the performance of the engine by identifying blocks of code that are frequently run, compiling them, and adding them to a cache.

#### Single page applications (SPAs)

Because of this increased performance, developers can now build feature-rich JavaScript applications that run on the browser. Google was the first major company to take advantage of this, when they released the first client-side web application framework—Angular - on 20 October 2010.

The SPA model has many benefits over the client-server model:

- It frees up the server to handle more requests, as requests are simpler to process.
- It allows the UI of the app to respond more quickly to user interaction because the UI does not need to wait for the server to respond before updating itself.

#### Server-side rendering (SSR)

- Reduces the time-to-first-render (TTFR) and improving the user experience.
- Ensures Search Engine Optimization (SEO) performance.

### Benefits of Node.js

- Context switching
- Shared code

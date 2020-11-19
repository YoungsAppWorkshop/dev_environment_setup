# The Complete Node.js Developer Course (2nd Edition)

* Title: The Complete Node.js Developer Course (2nd Edition)
* Author: Andrew Mead, Rob Percival
* Platform: [Udemy.com](https://www.udemy.com/)
* Description: Learn Node.js by building real-world applications with Node, Express, MongoDB, Mocha, and more!

## Section 2. Getting Setup

* Node.js Installation
  * [Node.js Official Homepage](https://nodejs.org/en/)
  * HomeBrew
  * NVM(Node Version Manager): [GitHub](https://github.com/creationix/nvm)
  * [NVM Tutorial](https://nodesource.com/blog/installing-node-js-tutorial-using-nvm-on-mac-os-x-and-ubuntu/)
* Uninstall Node.js Completely: [StackOverFlow](https://stackoverflow.com/questions/11177954/how-do-i-completely-uninstall-node-js-and-reinstall-from-beginning-mac-os-x)
* Why Should I Use Node?
  * [Blocking IO vs Non-Blocking IO](https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/)
  * [The Node.js Event Loop, Timers, and process.nextTick()](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/)

## Section 3. Node.js Fundamentals(Note App)

* Node.js APIs List: [Node.js v10.5.0 Documentation](https://nodejs.org/api/)
* Initializing NPM: `npm init`
* Restarting App automatically: [nodemon](https://www.npmjs.com/package/nodemon)

### Debugging Node.js applications

* Command Line tools
  * `node inspect APP.JS`
  * `nodemon inspect APP.JS`
    * list(10): Show next 10 lines
    * n: next
    * c: continue
    * repl: repl mode
    * `debugger;`

* Debugging via Chrome Dev Tools
  * `node --inspect-brk APP.JS`
  * `nodemon --inspect-brk APP.JS`
  * In Chrome, `chrome://inspect/`

### Section 5. Web Servers and Application Deployment

* Rendering Templates with Data
  * [Handlebars](http://handlebarsjs.com/) templating engine: [NPM repo](https://www.npmjs.com/package/hbs)

* Nodemon to watch extensions: `nodemon APP.JS -e js,hbs`

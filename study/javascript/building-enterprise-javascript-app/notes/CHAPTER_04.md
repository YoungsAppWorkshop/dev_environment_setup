# Building Enterprise JavaScript Applications

Li, Daniel.
Building Enterprise JavaScript Applications: Learn to build and deploy robust JavaScript applications using Cucumber, Mocha, Jenkins, Docker, and Kubernetes.
Packt Publishing. Kindle Edition.

## Chapter 4. Setting Up Development Tools

### What is Node.js

Traditionally, JavaScript is interpreted by a JavaScript engine that converts JavaScript code into more optimized, machine-executable code, which then gets executed. The engine interprets the JavaScript code at the time it is run.

This is unlike compiled languages such as C#, which must first be compiled into an **intermediate language (IL)**, where this IL is then executed by the **common language runtime (CLR)**, software similar in function to the JavaScript engine.

Different browsers use different JavaScript engines:

- Chrome uses V8
- Firefox uses SpiderMonkey
- WebKit browsers such as Safari use JavaScriptCore
- Microsoft Edge uses Chakra

**Node.js uses V8** as its JavaScript engine and adds C++ bindings that allow it to access operating system resources, such as files and networking.

Many people incorrectly call the JavaScript engine the JavaScript runtime. JavaScript in the browser and Node.js both use the same V8 engine, but run in different runtime environments. For example, *the browser runtime environment provides the window global object, which is not available in the Node.js runtime.*

### Modules

Let's remind ourselves why modular design is important. Without it, the following apply:

- Logic from one business domain can easily be interwoven with that of another
- When debugging, it's hard to identify where the bug is
- There'll likely be duplicate code

Writing modular code means the following:

- Separation of concerns: Modules are logical separations of domains
- Code reusability: Each module should have a very specific purpose. It should be granular.
- Each module provides an API for other modules to interact with

#### The dawn of modules

- Package managers: `npm`, `Bower`, and `yarn`
- Standards in defining JavaScript modules: `CommonJS`, `AMD`, `UMD`, and `ES6 modules`
- Tools to enable them to work on browsers: `RequireJS`, `Browserify`, `Webpack`, `Rollup`, and `SystemJS`

#### The birth of Node.js modules

In Node.js, modules are written in the **CommonJS** format, which provides two global objects, `require` and `exports`, that developers can use to keep their modules encapsulated.

You can export multiple constructs from a single module by adding them as properties to the exports object. *Constructs that are not exported are not available outside the module* because Node.js wraps its modules inside a **module wrapper**, which is simply a function that contains the module code. Note that this is a feature of Node.js, not CommonJS.

#### Standardizing module formats

Since CommonJS, multiple module formats have emerged for client-side applications, such as AMD and UMD.

Eventually, the task of unifying JavaScript module formats was taken on by the **Ecma International**, which standardized modules in the ECMAScript 2015 (ES6) version of JavaScript. This module format uses two keywords: `import` and `export`. ES6 modules are **static**, *meaning they cannot be changed at runtime.*

Node.js and popular browsers are quickly adding support for ECMAScript 2015 features, but currently none of them fully support modules.

Luckily, there are tools that can convert ECMAScript 2015 modules into the universally supported CommonJS format. The most popular are **Babel** and **Traceur**. In this book, we will use **Babel** *because it is the de facto standard.*

### Installing Node

#### Using nvm to install Node

```bash
nvm ls-remote
nvm install 6.11.1
nvm install lts/boron
```

#### Documenting Node versions

We should document which version of Node we are running our API server with. To do this with `nvm`, we simply have to define a `.nvmrc` file in the root directory of our project. Then, any developers working on the API will be able to use the right Node version by running `nvm use`.

```bash
echo "8.11.4" > .nvmrc
```

### Using yarn instead of npm

[yarn](https://yarnpkg.com/en/) uses the same [npm registry](https://www.npmjs.com/) as the npm CLI. Since they both just install packages inside `node_modules` directories and write to `package.json`, you can use npm and yarn interchangeably. The differences are in their methods for resolving and downloading dependencies.

#### Package version locking

When we specify our dependencies inside our package.json file, we can use symbols to indicate a range of acceptable versions. For example, `>version` means the installed version must be greater than a certain version, `~version` means approximately equivalent (which means it can be up to the next minor version), and `^version` means compatible (which usually means the highest version without a change in the major version).

`yarn`, by default, creates a **lock file**, `yarn.lock`. The lock file ensures that the exact version of every package is recorded, so that everyone who installs using the lock file will have exactly the same version of every package.

`npm`, on the other hand, only made its lock files as defaults in version 5.0.0 with `package-lock.json`.

#### Getting familiar with the yarn CLI

- `yarn licenses ls`: Prints out, on the console, a list of packages, their URLs and their licenses
- `yarn licenses generate-disclaimer`: Generates a text file containing the licenses of all the dependencies
- `yarn why`: Generates a dependency graph to figure out why a package was downloade
- `yarn upgrade-interactive`: Provides an interactive wizard that allows you to selectively upgrade outdated packages

### Transpiling ES6 with Babel

#### `@babel/cli`

The Babel CLI is the most common (and easiest) way to run Babel. It gives you an executable (babel) which you can use on the terminal to transpile files and directories. It is available on npmjs.com, and so we can install it using yarn:

```bash
# Install @babel/cli as a development dependency
$ yarn add @babel/cli --dev
# transpile a single file
$ babel example.js -o compiled.js
# transpile an entire directory
$ babel src -d build
```

#### `@babel/register`

The `@babel/cli` package allows you to transpile source code ahead of time. On the other hand, `@babel/register` transpiles it at runtime. `@babel/register` *is useful during testing*, as it allows you to write ESNext inside your tests, as they will be transpiled down before the tests are run.

#### `@babel/node`

While the `@babel/register` hook can integrate with other tools such as `mocha` and `nyc` and acts as a middle step, `@babel/node` is a stand-in replacement for node and supports ESNext syntax:

```bash
# install @babel/node
$ yarn add @babel/node --dev
 # instead of this
$ node main.js
 # you'd run
$ babel-node main.js
```

It is provided for convenience, to help you get started. **It's not meant to be used in production** since, like `@babel/register`, it transpiles the source code at runtime, which is highly inefficient.

#### `@babel/core`

`@babel/cli`, `@babel/register`, `@babel/node`, and several other packages all depend on `@babel/core`, which as its name implies contains the core logic behind Babel. In addition, the `@babel/core` package exposes API methods that you can use inside your code:

```js
import * as babel from '@babel/core';
var result = babel.transform("code();", options);
result.code;
result.map;
result.ast;
```

#### `@babel/polyfill`

Babel transpiles the new syntax down to older versions of ECMAScript. To use the polyfill, you must first **install it as a dependency (not a development dependency)**:

```bash
$ yarn add @babel/polyfill
```

#### Using Babel CLI to transpile our code

`npx` allows you to run binaries install locally (within your project's node_modules directory, as opposed to globally) using a very tidy syntax. Instead of typing `./node_modules/.bin/babel index.js -o compile.js`, you can shorten it to `npx babel index.js -o compile.js`.

##### Plugins and presets

Plugins tell Babel how to transform your code, and presets are predefined groups of plugins. For example, there's the `react` preset, which includes the `transform-react-jsx` plugin (among others) to allow Babel to understand JSX.

To use a plugin or preset, you can install it as a development dependency, and specify it in the `.babelrc`.

```bash
$ yarn add @babel/preset-es2017 @babel/plugin-syntax-object-rest-spread --dev
```

```json
// .babelrc
{
  "presets": ["@babel/es2017"],
  "plugins": ["@babel/syntax-object-rest-spread"]
}
```

##### The `env` preset

Babel provides the env preset, which is available as the `@babel/preset-env` package. This preset will use [the kangax ECMAScript compatibility tables](kangax.github.io/compat-table/) to determine which features are unsupported by your environment, and download the appropriate Babel plugins.

```bash
$ yarn add @babel/preset-env --dev
```

```json
// .babelrc
{
  "presets": [
    ["@babel/env", {
      "targets": {
        "node": "current"
      }
    }]
  ]
}
```

##### Separating source and distribution code

```bash
$ rm -rf dist/ && npx babel src -d dist
$ node dist/index.js
```

##### Importing the Babel polyfill

Lastly, inside the src/index.js file, import the polyfill at the top of the file:

```js
import "@babel/polyfill";
...
```

This will allow us to use new JavaScript APIs, such as `fetch`.

### Consolidating commands with npm scripts

In your `package.json` file, add a new build sub-property to the scripts property, and set it to a string representing the command we want to run:

```json
"scripts": {
  "build": "rm -rf dist/ && babel src -d dist",
  "serve": "yarn run build && node dist/index.js",
  "test": "echo \"Error: no test specified\" && exit 1"
}
```

#### Ensuring cross-platform compatibility

To ensure our npm script will work everywhere, we can use a Node package called [rimraf](https://www.npmjs.com/package/rimraf).

```bash
$ yarn add rimraf --dev
```

In your `package.json` file:

```json
"scripts": {
  "build": "rimraf dist/ && babel src -d dist",
  "serve": "yarn run build && node dist/index.js",
  "test": "echo \"Error: no test specified\" && exit 1"
}
```

### Automating development using nodemon

First, let's install `nodemon`:

```bash
$ yarn add nodemon --dev
```

Next, add a watch script that uses nodemon instead of node:

```json
"scripts": {
  "build": "rimraf dist && babel src -d dist",
  "serve": "yarn run build && node dist/index.js",
  "test": "echo \"Error: no test specified\" && exit 1",
  "watch": "nodemon -w src --exec yarn run serve"
},
```

### Linting with ESLint

ESLint is an open source linter for JavaScript. To use it, you would first document your rules inside a configuration file named `.eslintrc`. It is designed to be pluggable, which means developers can override the default rules and compose their own set of code style rules. Any violations can also be given a severity level of warning or error.

It also provides useful features such as the `--init` flag, which initiates a wizard to help you compose your configuration file, as well as the `--fix` flag, which automatically fixes any violations that do not require human intervention.

#### Installing ESLint

Let's install ESLint and run its initiation wizard:

```bash
$ yarn add eslint --dev
$ npx eslint --init
```

#### Linting our code

Now, let's run eslint on our src/index.js to discover problems with our code:

```bash
$ npx eslint src/index.js
```

#### Adding lint script to package.json

Just as we did with the build, serve, and watch npm scripts, we can add a fix and lint script into our `package.json`:

```json
"scripts": {
    ...
    "fix": "eslint src --fix",
    "lint": "eslint,
```

#### Installing the ESLint extension

There are a lot more integrations available for editors and build tools; you can find a comprehensive list at [Eslint document](https://eslint.org/docs/user-guide/integrations).

#### Adding pre-commit hooks

We can implement Git hooks, which are programs that are triggerred to run at defined points in Git's execution.

By default, Git hooks are stored inside the `.git/hooks` directory. If you look inside the directory, you'll find many sample hooks with the `.sample` file extension. The one we are interested in is the pre-commit hook, which is executed after the git commit command is issued, but before the actual commit is made.

Hooks are written as a shell script. However, if writing shell scripts manually sounds like too much work for you, there's a tool called Husky, which hugely simplifies the process for us. Let's install it:

```bash
$ yarn add husky --dev
```

Husky will insert its own Git hooks into our project. In these hooks, it will check our package.json for scripts with special names and run them. For instance, our `pre-commit` hook will check for a script named `precommit`.

```json
"scripts": {
    ...
    "precommit": "yarn run lint",
    ...
```

### Committing our code into Git

#### Using `.gitignore` to ignore files

Go to [Gitignore GitHub repo](https://github.com/github/gitignore/blob/master/Node.gitignore) and replace our `.gitignore` file with the content of the `Node.gitignore` file.

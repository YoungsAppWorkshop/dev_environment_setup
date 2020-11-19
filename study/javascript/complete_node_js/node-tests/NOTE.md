* To install dev dependency, `npm i mocha@3.0.0 --save-dev`

* In package.json, add this line to automatically test
```
"scripts": {
  "test": "mocha **/*.test.js",
  "test-watch": "nodemon --exec \"npm test\""
},
```

* Run `npm run test-watch`

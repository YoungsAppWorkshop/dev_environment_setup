# Advanced React & Redux Lecture Note

## Section 2. Testing

- What do we test?
  1. Look at each individual part of your application
  2. Imagine telling a friend 'heres what this piece of code does'
  3. Write a test to verify each part does what you expect

- Enzyme API
  - Static: Render the given component and return plain HTML
  - Shallow: Render *just* the given component and none of its children
  - Full DOM: Render the component and all of its children & let us modify it afterwards

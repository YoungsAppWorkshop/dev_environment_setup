// let square = x => x * x;
// console.log(square(9));

let user = {
  name: 'Andrew',
  sayHi: () => {
    // this, arguments keyword in arrow function are not bound.
    console.log(`Hi. I'm ${this.name}.`);
    console.log(arguments);
  },
  sayHiAlt () {
    // Regular functions
    console.log(`Hi. I'm ${this.name}.`);
    console.log(arguments);
  }
}

user.sayHi(1, 2, 3);
user.sayHiAlt(1, 2, 3);

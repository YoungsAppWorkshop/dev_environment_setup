# MobX Quick Start Guide

## Preface

**Observer** : Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Chapter 1. Introduction to State Management

The topics covered in this chapter are as follows:

- What is the client state?
- The side effect model
- A speed tour of MobX

### 1-1. The client state

It is the data that takes on a pivotal role in describing the UI. Handling the structure and managing the changes that can happen to this data is what we commonly refer to as state management. **State management** is the act of defining the shape of data and the operations that are used to manipulate it. In the context of the UI, it is called *client-side state management*.

There is an interesting equation that captures this relationship between UI and state:

> UI = f(state)

In the context of React, the preceding equation can be written as follows:

> VirtualDOM = fn(props, state)

The only difference here is that `fn` takes two inputs, `props` and `state`, which is the prescribed contract of a React component.

### 1-2. Handling changes in state

Actions:

- User operations, which results in a change in state
- Actions are the commands that you invoke as a result of various input-events that are fired
- Actions cause a change in the state, which is then reflected back on the UI

The triad of State, UI, and Actions:

- **Action** changes **State**
- **State** modifies **UI**
- **UI** fires **Action**

**UI** does not change the state directly, but instead does it via a message-passing system by firing **actions**. The **action** encapsulates the parameters that are required to cause the appropriate change in **state**. When the **State** changes, it notifies all of its *observers (subscribers)* of the change. The **UI** is also one of the most important subscribers that is notified. *This system of data flow from the State into the UI is always **uni-directional***.

### 1-3. The side effect model

**Single Responsibility Principle (SRP)**:

- A class or a module should have only one reason to change.

If we start handling additional operations in the UI, it would have more than one reason to change. For example:

- Downloading data from a server
- Persisting data back on the server
- Running a timer and doing something periodically
- Executing some validation logic when some state changes

**Side Effects**:

We want to retain the purity of the data flow triad, handle ancillary operations such as the ones mentioned in the preceding list, and not add extra responsibilities to the UI. To balance all of these forces, we need to think about the ancillary operations as something external to the data flow triad. We call these **side effects**.

Side effects are *a result of some **state-change*** and are *invoked by responding to the notifications coming from the state*. Just like the UI, there is a handler, which we can call the **side effect handler**, that observes (subscribes to) the state change notifications. When a matching state change happens, the corresponding side effect is invoked:

- **State** notifies **Side Effect Handlers**
- **Side Effect Handlers** produces **Side Effects**
- **Side Effects** fires **Action**
- **Action** changes **State**

So, it's not just the UI that can cause state changes, but also ***external operations** (via side effects) that can affect a state change*.

### 1-4. A speed tour of MobX

MobX is a reactive state management library that makes it easy to adopt the side effect model.

**An observable state**:

MobX provides a core building block, called the observable, that represents the reactive state of your application. *Any JavaScript object* can be used to create an observable.

**Observers**:

MobX gives you three different kinds of observers, each tailor-made for the use cases you will encounter in your application. The core observers are `autorun`, `reaction`, and `when`.

**Actions**:

The state should not be changed directly and instead should be done via actions. MobX `action` API encapsulates the mutation:

```js
import { observable, autorun, action } from 'mobx';

let cart = observable({
  itemCount: 0,
  modified: new Date(),
});

autorun(() => {
  console.log(`The Cart contains ${cart.itemCount} item(s).`);
});

const incrementCount = action(() => {
  cart.itemCount++;
});

incrementCount();
```

Internally, `action` is doing much more than being a simple wrapper. *It ensures that all notifications for state changes are fired*, but only ***after** the completion of the action function*.

> In the MobX literature, **side effects** are also called **reactions**. Unlike actions that cause state changes, reactions are the ones responding to state changes.

- **Observables** capture the **state** of your application.
- **Observers**(also called reactions) include both the **side effect handlers** as well as the **UI**.
- The **actions** cause a change in the **observable state**

### 1-5. MobX versus Redux

In principle, MobX and Redux accomplish the same goal of providing a uni-directional data flow. The store is the central actor that manages all state changes and notifies the UI and other observers of the change in state.

The mechanism to achieve that is quite different between MobX and Redux. Redux relies on **immutable** state snapshots and *reference-comparisons between two state snapshots to check for changes*. In contrast, MobX thrives on **mutable** state and *uses a granular notification system to track state changes*.

## Chapter 2. Observables, Actions, and Reactions

### 2-1. Observables

Observables are entities that can be observed. They keep track of changes happening to their values and notify all the observers. An observer can observe one or more observables and get notified when any of them change value.

*Observable objects only track the properties provided in the initial value* given to `observable()` or `observable.object()`. This means if you add new properties later, they will not become observable automatically. *If you do need dynamic tracking of properties, you should consider using observable maps*.

#### `observable()`

- The `observable()` function automatically converts an object, an array, or a map into an observable entity.
- This automatic conversion is not applied for other types of data:
  - JavaScript primitives (number, string, boolean, null, undefined)
  - Functions
  - Class-instances (objects with prototypes)

Observables that wrap primitives, functions, or class-instances are called **boxed observables**. We have to use the `get()` and `set()` methods of a boxed observable instead of directly reading or assigning to it.

```js
const count = observable.box(20);
// Get the count
console.log(`Count is ${count.get()}`);
// Change count
count.set(22);
```

Besides objects and singular values, you can also create observables out of arrays and maps:

- Objects: `observable.object({ })`
- Arrays: `observable.array([ ])`
- Maps: `observable.map(value)`
- Primitives, functions, class-instances: `observable.box(value)`

#### Observable arrays

Using `observable.array()` is very similar to using an `observable()`. You pass an array as initial value or start with an empty array.

The observable array is not a real JavaScript array, even though it has the same API as a JS Array. When you are passing this array to other libraries or APIs, you can convert it into a JS Array by calling `toJS()`.

```js
import { observable, toJS } from 'mobx';

const items = observable.array(); // Start with empty array
console.log(items.length); // Prints: 0

items.push({
  name: 'hats', quantity: 40,
});

// Add one in the front
items.unshift({ name: 'Ribbons', quantity: 2 });

// Add at the back
items.push({ name: 'balloons', quantity: 1 });

const plainArray = toJS(items);

console.log(plainArray);
```

#### Observable maps

The observable map instance shares the same API as a regular ES6 Map. *Observable maps are great for tracking dynamic changes to the keys and values. This is in stark contrast to observable objects, which do not track properties that are added after creation.*

```js
import { observable } from 'mobx'

// Create an Observable Map
const twitterUserMap = observable.map()
console.log(twitterUserMap.size) // Prints: 0

// Add keys
twitterUserMap.set('pavanpodila', 'Pavan Podila')
twitterUserMap.set('mweststrate', 'Michel Weststrate')

console.log(twitterUserMap.get('pavanpodila')) // Prints: Pavan Podila
console.log(twitterUserMap.has('mweststrate')) // Prints: Michel Weststrate

twitterUserMap.forEach((value, key) => console.log(`${key}: ${value}`))
// Prints:
// pavanpodila: Pavan Podila
// mweststrate: Michel Weststrate
```

#### A note on observability

MobX applies **deep observability** when creating an observable. This means *MobX will automatically observe every property, at every level, in the object-tree, array, or map*. It also tracks additions or removals in the cases of arrays and maps. This behavior works well for most scenarios but could be excessive in some cases. There are special decorators that you can apply to control this observability.

You can change this behavior at the time of creating the observable. Instead of using `observable()`, you can use the sibling APIs (`observable.object()`, `observable.array()`, `observable.map()`) to create the observable. Each of these takes an extra argument for setting options on the observable instance.

```js
observable.object(value, decorators, { deep: false });
observable.map(values, { deep: false });
observable.array(values, { deep: false });
```

#### The computed observable

An observable that derives its value from other observables.

```js
import { observable } from 'mobx'

const cart = observable.object({
  items: [],
  modified: new Date(),

  get description() {
    switch (this.items.length) {
      case 0:
        return 'There are no items in the cart'
      case 1:
        return 'There is one item in the cart'
      default:
        return `There are ${this.items.length} items in the cart`
    }
  }
})

cart.items.push("banana", "apple")

console.log(cart.description) // There are 2 items in the cart
```

#### Better syntax with decorators

*The decorator syntax is only available for **classes*** and can be used for class declarations, properties and methods.

```js
class Cart {
  @observable.shallow items = [];
  @observable modified = new Date();

  @computed get description() {
    switch (this.items.length) {
      case 0:
        return 'There are no items in the cart';
      case 1:
        return 'There is one item in the cart';
      default:
        return `There are ${this.items.length} items in the cart`;
    }
  }
}
```

The default `@observable` decorator does deep observation on all the properties of the value. It is actually a shorthand for using `@observable.deep`. Similarly, we have the `@observable.shallow` decorator, which is a rough equivalent of setting the `{ deep: false }` option on the `observable`.

It works for **objects**, **arrays**, and **maps**.

### 2-2. Actions

Actions introduce *vocabulary* into the UI and give declarative names to the operations that mutate the state. MobX embraces this idea completely and makes actions a *first-class* concept. To create an action, we simply wrap the mutating function inside the `action()` API.

```js
import { observable, action } from 'mobx'

const cart = observable({
  items: [],
  modified: new Date()
})

// Create the actions
const addItem = action((name, quantity) => {
  const item = cart.items.find(x => x.name === name)
  if (item) {
    item.quantity += 1
  } else {
    cart.items.push({ name, quantity })
  }
  cart.modified = new Date()
})

const removeItem = action(name => {
  const item = cart.items.find(x => x.name === name)
  if (item) {
    item.quantity -= 1
    if (item.quantity <= 0) {
      cart.items.remove(item)
    }
    cart.modified = new Date()
  }
})

// Invoke actions
addItem('balloons', 2)
addItem('paint', 2)
removeItem('paint')
```

Besides improving the readability of the code, *actions also boost performance of MobX*. By default, when you modify an observable, MobX will immediately fire a notification for the change. *If you are modifying a bunch of observables together, you would rather fire the change notifications after all of them are modified*. These are, in essence, the core responsibilities of an `action()`.

#### Enforcing the use of actions

It should come as no surprise that MobX strongly recommends using actions for modifying observables. In fact, this can be made mandatory by configuring MobX to always enforce this policy, also called the strict mode. The `configure()` function can be used to set the enforceActions option to `observed`.

```js
import { observable, configure } from 'mobx';

configure({
  enforceActions: "observed", // "never", "observed", "always"
});

const cart = observable({
  items: [],
  modified: new Date()
})

// Modifying outside of an action
cart.items.push({ name: 'test', quantity: 1 });
cart.modified = new Date();
```

#### Decorating actions


```js
import { observable, action } from 'mobx'

class Cart {
  @observable modified = new Date()
  @observable.shallow items = []

  @action
  addItem(name, quantity) {
    this.items.push({ name, quantity })
    this.modified = new Date()
  }

  @action.bound
  removeItem(name) {
    const item = this.items.find(x => x.name === name)
    if (item) {
      item.quantity -= 1
      if (item.quantity <= 0) {
        this.items.remove(item)
      }
    }
  }
}
```

In the preceding snippet, we used `@action.bound` for the `removeItem()` action. This is a special form that pre-binds the instance of the class to the method. This means you can pass around the reference to `removeItem()` and be assured that the this value always points to the instance of the Cart.

### 2-3. Reactions

Reactions can really change the world for your app. They are the ***side-effect** causing behaviors* that react to the changes in observables.

#### `autorun()`

`autorun()` is a long-running side-effect that takes in a function (effect-function) as its argument. The effect-function function is where you apply all your side-effects. Now, these side-effects may depend on one or more observables.

```js
import { observable, action, autorun } from 'mobx'

class Cart {
  @observable modified = new Date()
  @observable.shallow items = []
  cancelAutorun = null

  constructor() {
    this.cancelAutorun = autorun(() => {
      console.log(`Items in Cart: ${this.items.length}`)
    })
  }

  @action
  addItem(name, quantity) {
    this.items.push({ name, quantity })
    this.modified = new Date()
  }
}

const cart = new Cart()         // Prints: Items in Cart: 0
cart.addItem('Power Cable', 1)  // Prints: Items in Cart: 1
cart.cancelAutorun()
cart.addItem('Shoes', 1)        // No prints

```

It runs immediately and also on every change to the dependent observables. The return-value of `autorun()` is a function that is in fact a disposer-function. By calling it, you can cancel the `autorun()` side-effect.

#### `reactions()`

`reaction()` is similar to `autorun()` but waits for a change in the observables before executing the effect-function. `reaction()` in fact takes two arguments, which are as follows:

- `reaction(tracker-function, effect-function): disposer-function`
- `tracker-function: () => data`
- `effect-function: (data) => {}`

`tracker-function` is where all the observables are tracked. Any time the tracked observables change, it will re-execute. It is supposed to return a value that is used to compare it to the previous run of `tracker-function`. If these return-values differ, the `effect-function` is executed.

By breaking up the activity of a reaction into a change-detecting function (*tracker function*) and the *effect function*, `reaction()` gives us more fine-grained control over when a side-effect should be caused.

Just like `autorun()`, you also get a disposer function as the return-value of `reaction()`.

```js
import { observable, action, reaction } from 'mobx'

class Cart {
  @observable modified = new Date()
  @observable items = []
  cancelPriceTracker = null

  trackPriceChangeForItem(name) {
    if (this.cancelPriceTracker) {
      this.cancelPriceTracker()
    }
    // 1. Reaction to track price changes
    this.cancelPriceTracker = reaction(
      () => {
        const item = this.items.find(x => x.name === name)
        return item ? item.price : null
      },
      price => {
        console.log(`Price changed for ${name}: ${price !== null ? price : 0}`)
      }
    )
  }

  @action
  addItem(name, price) {
    this.items.push({ name, price })
    this.modified = new Date()
  }

  @action
  changePrice(name, price) {
    const item = this.items.find(x => x.name === name)
    if (item) {
      item.price = price
    }
  }
}

const cart = new Cart()
cart.addItem('Shoes', 20)

// 2. Now track price for "Shoes"
cart.trackPriceChangeForItem('Shoes')

// 3. Change the price
cart.changePrice('Shoes', 100)  // Price changed for Shoes: 100
cart.changePrice('Shoes', 50)   // Price changed for Shoes: 50
```

##### A reactive UI

In the MobX world, this UI is also reactive, in the sense that it reacts to the changes in data and automatically re-renders itself.

MobX provides a companion library called `mobx-react` that has bindings to React. By using a decorator function (`observer()`) from `mobx-react`, you can transform a react component to observe the observables used in the `render()` function.

When they change, a re-render of the react component is triggered. Internally, `observer()` creates a wrapper component that uses a plain `reaction()` to watch the observables and re-render as a side-effect.

```js
import { observer } from 'mobx-react'
import { observable } from 'mobx'
import ReactDOM from 'react-dom'
import React from 'react'

const item = observable.box(30)

// 1. Create the component with observer
const ItemComponent = observer(() => {
  // 2. Read an observable: item
  return <h1>Current Item Value = {item.get()}</h1>
})
ReactDOM.render(<ItemComponent />, document.getElementById('root'))

// 3. Update item
setTimeout(() => item.set(50), 2000)
```

#### `when()`

As the name suggests, `when()` only executes the effect-function when a condition is met and automatically disposes the side-effect after that. Thus, `when()` is a one-time side-effect compared to `autorun()` and `reaction()`, which are long-running.

`when()` takes two arguments, which are as follows:

- `when(predicate-function, effect-function): disposer-function`
- `predicate-function: () => boolean, effect-function: () => {}`

The predicate function is expected to return a Boolean value. When it becomes `true`, the effect function is executed, and the `when()` is automatically disposed. Note that when() also gives you back a disposer function that you can call to prematurely cancel the side-effect.

```js
import { observable, action, when } from 'mobx'

class Inventory {
  @observable items = []
  cancelTracker = null

  trackAvailability(name) {
    // 1. Establish the tracker with when
    this.cancelTracker = when(
      () => {
        const item = this.items.find(x => x.name === name)
        return item ? item.quantity > 0 : false
      },
      () => {
        console.log(`${name} is now available`)
      }
    )
  }

  @action
  addItem(name, quantity) {
    const item = this.items.find(x => x.name === name)
    if (item) {
      item.quantity += quantity
    } else {
      this.items.push({ name, quantity })
    }
  }
}

const inventory = new Inventory()
inventory.addItem('Shoes', 0)
inventory.trackAvailability('Shoes')

// 2. Add two pairs
inventory.addItem('Shoes', 2)   // Shoes is now available

// 3. Add one more pair
inventory.addItem('Shoes', 1)
```

##### `when()` with a promise

```js
class Inventory {
  /* ... */
  async trackAvailability(name) {
    // 1. Wait for availability
    await when(() => {
      const item = this.items.find(x => x.name === name)
      return item ? item.quantity > 0 : false
    })
    // 2. Execute side-effect
    console.log(`${name} is now available`)
  }
  /* ... */
}
```

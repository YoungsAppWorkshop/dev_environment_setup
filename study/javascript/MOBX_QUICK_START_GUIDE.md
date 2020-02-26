# MobX Quick Start Guide

## Preface

**Observer** : Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Introduction to State Management

The topics covered in this chapter are as follows:

- What is the client state?
- The side effect model
- A speed tour of MobX

### The client state

It is the data that takes on a pivotal role in describing the UI. Handling the structure and managing the changes that can happen to this data is what we commonly refer to as state management. **State management** is the act of defining the shape of data and the operations that are used to manipulate it. In the context of the UI, it is called *client-side state management*.

There is an interesting equation that captures this relationship between UI and state:

> UI = f(state)

In the context of React, the preceding equation can be written as follows:

> VirtualDOM = f(props, state)

The only difference here is that fn takes two inputs, props and state, which is the prescribed contract of a React component.

### Handling changes in state

Actions:

- User operations, which results in a change in state
- Actions are the commands that you invoke as a result of various input-events that are fired
- Actions cause a change in the state, which is then reflected back on the UI

The triad of State, UI, and Actions:

- **Action** changes **State**
- **State** modifies **UI**
- **UI** fires **Action**

**UI** does not change the state directly, but instead does it via a message-passing system by firing **actions**. The **action** encapsulates the parameters that are required to cause the appropriate change in **state**. When the **State** changes, it notifies all of its *observers (subscribers)* of the change. The **UI** is also one of the most important subscribers that is notified. *This system of data flow from the State into the UI is always **uni-directional***.

### The side effect model

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

### A speed tour of MobX

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

### MobX versus Redux

In principle, MobX and Redux accomplish the same goal of providing a uni-directional data flow. The store is the central actor that manages all state changes and notifies the UI and other observers of the change in state.

The mechanism to achieve that is quite different between MobX and Redux. Redux relies on **immutable** state snapshots and *reference-comparisons between two state snapshots to check for changes*. In contrast, MobX thrives on **mutable** state and *uses a granular notification system to track state changes*.

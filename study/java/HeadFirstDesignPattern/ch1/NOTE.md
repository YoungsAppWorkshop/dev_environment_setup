# Chapter 1. Intro to Design Patterns: Welcome to Design Patterns

Someone has already solved your problems.
Instead of code reuse, with patterns you get experience reuse.

## The Problem

A great use of inheritance for the purpose of reuse hasn’t turned out so well when it comes to maintenance. *A localized update to the code caused a nonlocal side effect* (flying rubber ducks)!

```java
class Duck {
  quack()
  swim()
  display()
  fly()
}

class MallardDuck extends Duck {
  display() {
    // looks like a mallard
  }
}

class RedheadDuck extends Duck {
  display() {
    // looks like a redhead
  }
}

// Oops!! A flying rubber duck!!
class RubberDuck extends Duck {
  quack() {
    // overridden to squeak
  }
  display() {
    // looks like a rubber duck
  }
}
```

## Trials and Errors

We know that *not all of the subclasses should have flying or quacking behavior, so **inheritance isn’t the right** answer.*

```java
interface Flyable {
  fly()
}

interface Quackable {
  quack()
}

class Duck {
  swim()
  display()
}

class MallardDuck extends Duck implements Flyable, Quackable {
  display() {}
  fly() {}
  quack() {}
}

class RedheadDuck extends Duck implements Flyable, Quackable {
  display() {}
  fly() {}
  quack() {}
}

class RubberDuck extends Duck implements Quackable {
  display() {}
  quack() {}
}

class DecoyDuck extends Duck {
  display() {}
}
```

But *while having the subclasses implement Flyable and/or Quackable solves part of the problem* (no inappropriately flying rubber ducks), **it completely destroys code reuse** for those behaviors, so it just creates a different maintenance nightmare.

## The Solution

### Design Principle

> Identify the aspects of your application that vary and separate them from what stays the same.

Take what varies and **encapsulate** it so it won’t affect the rest of your code.

> Program to an interface, not an implementation.

The Duck behaviors will live in a separate class a class that implements a particular behavior interface.

```java
interface FlyBehavior {
  fly()
}

class FlyWithWings {
  fly() {
    // implements duck flying
  }
}

class FlyNoWay {
  fly() {
    // do nothing, can't fly
  }
}
```

*"Program to an interface"* really means ***"Program to a supertype."***

And we could rephrase “program to a supertype” as “the declared type of the variables should be a supertype, *usually an abstract class or interface, so that the objects assigned to those variables can be of any concrete implementation of the supertype,* which means the class declaring them doesn’t have to know about the actual object types!”

```java
// Programming to an implementation would be:
Dog d = new Dog();
d.bark();

// Programming to an interface/supertype would be:
Animal animal = new Dog();
animal.makeSound();

// Even better, rather than hardcoding the instantiation of
// the subtype (like new Dog()) into the code,
// assign the concrete implementation object at runtime:
a = getAnimal();
a.makeSound();
```

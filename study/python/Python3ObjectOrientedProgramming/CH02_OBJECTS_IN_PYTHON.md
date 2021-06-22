# Chapter 2. Objects in Python

After completing this chapter, we will understand:

- How to create classes and instantiate objects in Python
- How to add attributes and behaviors to Python objects
- How to organize classes into packages and modules
- How to suggest people don't clobber our data

## Creating Python classes

Define Class:

```python
class MyFirstClass:
    pass
```

The class name must follow standard Python variable naming rules:

- It must start with a letter or underscore
- It can only be comprised of letters, underscores, or numbers
- The Python style guide **PEP8** recommends that classes should be named using *CamelCase* notation

> Run the code and then drop to the interactive interpreter: `python -i first_class.py`

Instantiate an Object:

```python
a = MyFirstClass()
```

## Adding attributes

What do we have to do to assign an attribute to a given object? It turns out that *we don't have to do anything special in the class definition*. We can set arbitrary attributes on an instantiated object using the dot notation:

```python
class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p1.y = 4
```

## Making it do something

The one difference between methods and normal functions is that all methods have one required argument. This argument is conventionally named `self`. The `self` argument to a method is simply a reference to the object that the method is being invoked on.



```python
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset()
```

When we call the `p.reset()` method, we do not have to pass the `self` argument into it.

```python
p = Point()
Point.reset(p)
print(p.x, p.y)
```

However, the method really is just a function that happens to be on a class. Instead of calling the method on the object, we can invoke the function on the class, explicitly passing our object as the `self` argument.

## Initializing the object

Most object-oriented programming languages have the concept of a constructor, a special method that creates and initializes the object when it is created. **Python is a little different. It has a constructor and an initializer.** *The constructor function is rarely used unless you're doing something exotic.*

```python
class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)
```

The constructor function is called `__new__` as opposed to `__init__`, and accepts exactly one argument; the class that is being constructed (it is called before the object is constructed, so there is no `self` argument). It also has to return the newly created object. This has interesting possibilities when it comes to the complicated art of metaprogramming, but is not very useful in day-to-day programming. In practice, you will rarely, if ever, need to use `__new__` and `__init__` will be sufficient.

## Explaining yourself - `docstrings`

Docstrings are simply Python strings enclosed with apostrophe (`'`) or quote (`"`) characters. Often, docstrings are quite long and span multiple lines (the style guide suggests that the line length should not exceed 80 characters), which can be formatted as multi-line strings, enclosed in matching triple apostrophe (`'''`) or triple quote (`"""`) characters.

Try typing or loading (`python -i filename.py`) this file into the interactive interpreter. Then, enter `help(Point)` at the Python prompt. You should see nicely formatted documentation for the class.

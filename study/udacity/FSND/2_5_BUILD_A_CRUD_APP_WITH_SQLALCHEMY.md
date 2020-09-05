# Lesson 2-5. Build a CRUD App with SQLAlchemy

## Model View Controller (MVC)

**Takeaways**:

- MVC stands for Model-View-Controller, a common pattern for architecting web applications
- Describes the 3 layers of the application we are developing

![img-01](./imgs/img-2-5-1.png)

**Layers**:

- **Models** manage data and business logic for us. What happens inside models and database, capturing logical relationships and properties across the web app objects
- **Views** handles display and representation logic. What the user sees (HTML, CSS, JS from the user's perspective)
- **Controllers**: routes commands to the models and views, containing control logic. Control how commands are sent to models and views, and how models and views wound up interacting with each other.

## Handling User Input

**Takeaways**:

- Creating, updating, and deleting information from a database requires handling user input on what is being created/updated/deleted. This will be the focus of the rest of this series.

![img-02](./imgs/img-2-5-2.png)

**MVC Development**: How we'd add Create To-Do item functionality

- **On the view**: implement an HTML form
- **On the controller**: retrieve the user's input, and manipulate models
- **On the models**: create a record in our database, and return the newly created to-do item to the controller
- **On the controller**: take the newly created to-do item, and decide how to update the view with it.

**What we'll learn in order**:

1. **How we accept and get user data** in the context of a Flask app
2. **Send data in controllers** using database sessions in a controller
3. **Manipulating models** adding records in SQLAlchemy Models
4. **Direct how the view should update** within the controller and views

## Getting User Data in Flask

There are 3 methods of getting user data from a view to a controller.

- URL query parameters
- Forms
- JSON

![img-03](./imgs/img-2-5-3.png)

### URL query parameters

URL query parameters are listed as key-value pairs at the end of a URL, preceding a "?" question mark. E.g. `www.example.com/hello?my_key=my_value`.

### Form data

`request.form.get('<name>')` reads the value from a form input control (text input, number input, password input, etc) by the ***name*** attribute on the input HTML element.

**Note**: defaults

`request.args.get`, `request.form.get` both accept an optional second parameter, e.g. `request.args.get('foo', 'my default')`, set to a default value, in case the result is empty.

The way form data traverses from the client to server differs based on whether we are using a GET or a POST method on the form.

#### The POST submission

- On submit, we send off an HTTP POST request to the route with a request body
- The request body stringifies the key-value pairs of fields from the form (as part of the ***name*** attribute) along with their values.

#### The GET submission

- Sends off a GET request with URL query parameters that appends the form data to the URL.
- Ideal for smaller form submissions.

POSTs are ideal for longer form submissions, since URL query parameters can only be so long compared to request bodies (max 2048 characters). Moreover, forms can only send POST and GET requests, and nothing else.

### JSON

`request.data` retrieves JSON as a string. Then we'd take that string and turn it into python constructs by calling `json.loads` on the `request.data` string to turn it into lists and dictionaries in Python.

## Using sessions in controllers

Commits can succeed or fail. On fail, we want to rollback the session to avoid potential implicit commits done by the database on closing a connection. Good practice is to close connections at the end of every session used in a controller, to return the connection back to the connection pool.

### Pattern (try-except-finally)

```python
import sys

try:
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
except:
    db.session.rollback()
    error=True
    print(sys.exc_info())
finally:
    db.session.close()
```

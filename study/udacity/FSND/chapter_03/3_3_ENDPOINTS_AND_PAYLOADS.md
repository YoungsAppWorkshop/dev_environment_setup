# Lesson 3-3. Endpoints and Payloads

## Organizing API endpoints

Principles

- Should be intuitive
- Organize by resource
  - Use nouns in the path, not verbs
  - The method used will determine the operation taken
  - **GOOD**: `https://example.com/posts`
  - **BAD**: `https://example.com/get_posts`
- Keep a consistent scheme
  - Plural nouns for collections
  - Use parameters to specify a specific item
  - **GOOD**:
    - `https://example.com/entrees`
    - `https://example.com/entrees/5`
  - **BAD**:
    - `https://example.com/entree`
    - `https://example.com/entree_five`
- Don’t make them too complex or lengthy
  - No longer than `collection/item/collection`
  - **GOOD**: `https://example.com/entrees/5/reviews`
  - **BAD**: `https://example.com/entrees/5/customers/4/reviews`

## CORS: Cross-Origin Resource Sharing

*The same-origin policy* is a concept of web security that allows scripts in Webpage 1 to access data from Webpage 2 only if they share the same domain. This means that the above error will be raised in the following cases:

- Different domains
- Different subdomains (`example.com` and `api.example.com`)
- Different ports (`example.com` and `example.com:1234`)
- Different protocols (`http://example.com` and `https://example.com`)

This policy is there to protect you and your users. For instance, attackers may embed malicious scripts in advertisements. This policy prevents those scripts from successfully making requests to your bank's website as you access the website hosting the advertisement.

If you're sending any requests beyond very simple `GET` or `POST` requests, then before your actual request is sent, the browser sends a preflight `OPTIONS` request to the server. If **CORS** is not enabled, then the browser will not respond properly and the actual request will not be sent.

### CORS headers

| Header | Description |
| --- | --- |
| `Access-Control-Allow-Origin` | What client domains can access its resources. For any domain use `*` |
| `Access-Control-Allow-Credentials` | Only if using ***cookies*** for authentication - in which case its value must be `true` |
| `Access-Control-Allow-Methods` | List of HTTP request types allowed |
| `Access-Control-Allow-Headers` | List of http request header values the server will allow, particularly useful if you use any custom headers |

## Flask-CORS

### Installation

In order to install Flask-CORS simply run

```python
pip3 install -U flask-cors
```

### Initialization

Once Flask-CORS is installed, you simply import the CORS function and call it with your app instance as a parameter. This will intialize Flask-CORS will all default options.

```python
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)
```

### Resource-Specific Usage

There are multiple options you can use to specify your Flask-CORS behavior. One typical one is resources, which contains a dictionary whose keys are regular expressions and values are dictionary or kwargs

```python
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
```

### Route-Specific Usage

If you need to enable CORS on a given route, like those non-simple requests, you can use `@cross_origin()` to enable it.

```python
@app.route("/hello")
@cross_origin()
def get_greeting():
    return jsonify({'message':'Hello, World!'})
```

## Flask Route Decorator

### Variable Rules

In our endpoint naming scheme we follow `collection/item/collection`. In order to handle that variable item. In order to handle that variability in Flask, you add a `<variable_name>` within the path argument of the `@app.route` decorator, which is then passed to the function as a keyword argument variable_name.

You can also specify the type of the argument by using `<converter:variable_name>` syntax.

```python
@app.route('/entrees/<int:entree_id>')
def retrieve_entree(entree_id):
    return 'Entree %d' % entree_id
```

### HTTP Methods

By default, the `@app.route` decorator answers only `GET` requests. In order to enable more requests types, pass the method parameter to the decorate including a list of string methods.

```python
@app.route('/hello', methods=['GET', 'POST'])
def greeting():
    if request.method == 'POST':
        return create_greeting()
    else:
        return send_greeting()
```

`OPTIONS` requests are automatically implemented and `HEAD` is also automatically implemented if `GET` is present.

## Pagination in Flask

### Query Parameters

The below examples show the format of query parameters. When writing query parameters convention dictates that:

- A question mark precedes the query parameters
- Parameters are in key=value pairs with an equal sign in between the key and value
- Sets of parameters are separated by an ampersand

```bash
www.example.com/entrees?page=1
www.example.com/entrees?page=1&allergens=peanut
```

### Request Arguments

In flask, when a request is received with query params the route in the `@app.route` decorator remains the same and the request object arguments contains the parameter. You access it as shown below. `request.args` is a Python dictionary so we use the get method to access the value and provide a default value, in this case `1`.

```python
@app.route('/entrees', methods=['GET'])
  def get_entrees():
    page = request.args.get('page', 1, type=int)
```

## Error Handling

When you use the abort method, the default response is not digestible for the client or user.

```python
abort(404)
```

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

In addition, we want to ensure all of our server responses have consistent formatting and that we provide adequate information to the client regarding the error. The `@app.errorhandler` decorator allows you to specify the behavior for expected errors. When using this decorator take into consideration:

- passing the status code or Python error as an argument to the decorator
- logical naming of the function handler
- consistent formatting and messaging of the JSON object response

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not found"
    }), 404
```

# ------------------------------------------------
# ----------------Python JSON---------------------
# ------------------------------------------------

#  If you have a JSON string, you can parse it by using the json.loads() method.

# ex1 - Convert from JSON to Python:
    import json

    # some JSON:
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

# ex 2 - Convert from Python to JSON:

    import json

    # a Python object (dict):
    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)

# ex 3 - Convert Python objects into JSON strings, and print the values:
    import json

    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("apple", "bananas")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))

# ex 4 - Convert a Python object containing all the legal data types:
    import json

    x = {
      "name": "John",
      "age": 30,
      "married": True,
      "divorced": False,
      "children": ("Ann","Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
      ]
    }

    print(json.dumps(x))

# -------------------- Format the Result ----------------------------

# ex 5 - Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

# ex 6 - Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

# -------------------- Order the Result ----------------------------

# ex 7 - Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)


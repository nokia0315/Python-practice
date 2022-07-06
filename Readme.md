# Awesome-name

To do lists

## Description

I make a simple webapp to practice to programming.

## Reference

https://www.youtube.com/watch?v=jP7p2okKdJA&t=304s

## Development Environment

- OS:Windows
- Lng:HTML,CSS,Python,SQL
- Framework:Flask
- IDE:VScode

## Installing

- Install and update using pip:

```
pip install Flask
```

- Virtual env:

```
pip install virtualenv
```

- SQL:

```
pip install flask flask-sqlalchemy
```

## A Simple Example

```
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
python app.py
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

## Reference links

- Install flask:https://shigeblog221.com/python-flask1/

-Virtual env:https://qiita.com/psychoroid/items/6646d45d6a019f5cf16f

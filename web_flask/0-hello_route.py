#!/usr/bin/python3
"""Start a Flask web application
"""

from flask import Flask

app = Flask(__name__)

# Define the route for root
@app.route('/', strict_slashes=False)

def hello_hbnb():
    """ Disply Hello HBNB! """
    return "Hello HBNB!"

if __name__ == "__main__":
    # Start Flask serevr
    # lIsten on on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)

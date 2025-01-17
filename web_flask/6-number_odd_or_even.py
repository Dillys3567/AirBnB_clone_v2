#!/usr/bin/python
"""Start a flask application
"""

from flask import Flask, request, render_template

app = Flask(__name__)

#Define route for root
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' """
    return "Hello HBNB!"

#Define route for /bhnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' """
    return "HBNB"

# Define route for 'c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Display c followed by text"""
    # Replace underscores with spaces in text
    format_text =  text.replace('_', ' ')
    return "C {}".format(format_text)

#Define route for '/python(<text>)'
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """Display python followed by text and replace underscores
    with slashes in text
    """
    format_text = text.replace('_', ' ')
    return "Python {}".format(format_text)

# Define the route for /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display n if it is an intger"""
    return "{} is a number".format(n)

# Definfe route for'/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Dispaly html page if only <n> is an integer. """
    return render_template("5-number.html", n=n)

# Define the route for '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display HTML page if n is an integer
    """
    if isinstance(n, int):
        # Determine if n is odd or even
        even_or_odd = "even" if n % 2 == 0 else "odd"
        # Render the template and pass n to template
        return render_template('6-number_odd_or_even.html',
                n=n, even_or_odd=even_or_odd)
    else:
        # If n is not int return error
        return "Invalid input. Please provide an integer."


if __name__ == "__main__":
    # Start flask server
    app.run(host='0.0.0.0', port=5000)

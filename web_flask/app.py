#!/usr/bin/python3
"""Start a Flak application
The application listens on 0.0.0.0, port 5000.
Routes: Displays "Hello HBNB
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if <n> is an integer.

    States whether <n> is odd or even in the body.
    """
    return render_template("number_odd_or_even.html", n=n)

@app.teardown_appcontext
def handle_teardown(self):
    """method to handle teardown"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """method to render states"""
    states = storage.all('State').values()
    return render_template("states_list.html", states=states)

@app.route('/cities_by_states', strict_slashes=False)
def city_state_list():
    """
        method to render states from storage
    """
    states = storage.all('State').values()
    return render_template("cities_by_states.html", states=states)

@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("states.html", state=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("states.html", state=state)
    return render_template("states.html")

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("hbnb_filters.html",
                           states=states, amenities=amenities)

@app.route("/hugebnb", strict_slashes=False)
def hugebnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("hugebnb.html",
                           states=states, amenities=amenities, places=places)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

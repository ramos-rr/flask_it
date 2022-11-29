# Class 2 - Route creation and configuration
from flask import Flask


app = Flask(__name__)


# Normal Route
@app.route("/")
def index():
    return "Index"


# ADD A URL RULE - Call a function outside a route!
def test1():
    return "<p>testing 1</p>"
app.add_url_rule("/test1", "test1", test1)


def test2():
    return "<h1>testing 2</h1>"
app.add_url_rule("/test2", "test2", test2)



if __name__ == '__main__':
    # SET DEBUG ON to authomatically refresh the server whenever you make modifications
    # INFORM A PORT as you wish
    app.run(debug=True, port=2000)

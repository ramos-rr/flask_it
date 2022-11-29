# Class 7 - Requery objects
from flask import Flask, request, jsonify
app = Flask(__name__)


# Let's see which parameter we are getting from the browser
@app.route('/', methods=["GET", "POST"])
def index():
    print(request.method)
    print(request.args)
    print(request.query_string)
    return jsonify(request.args)


if __name__ == '__main__':
    app.run(debug=True, port=7000)
    # enter the following url = "http://127.0.0.1:7000?name=Testin123"

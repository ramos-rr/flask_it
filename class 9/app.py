# Class 9 - Templates
from flask import Flask, request, render_template, abort

app = Flask(__name__)


# We'll use Jinga2 template models
# Create a folder to house templates
# See also comentaries and instructions in the HTML file "model.html"
@app.route('/')
def index():
    x = 20
    y = 10
    fruits = ["apple", "melon", "strawbery", "orange"]
    query = request.args.to_dict()
    return render_template('model.html', x=x, y=y, fruits=fruits, query=query)


if __name__ == '__main__':
    app.run(debug=True, port=9000)

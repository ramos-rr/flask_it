# Class 1 - Installing Flask
from flask import Flask

# CREATE YOUR APP - Name whatever you want
app = Flask(__name__)


# CREATE A ROUTE - Flask will assume a route as soon as you use a DECORATOR "@<app_name>.route"
@app.route('/')
def index():
    return "Index"


@app.route('/test')
def test():
    return "Test"


if __name__ == '__main__':
    app.run()

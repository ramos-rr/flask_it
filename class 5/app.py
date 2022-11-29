# Class 5 - WEB Static files
from flask import Flask


# Inform in APP definition the static files' directory location
app = Flask(__name__, static_folder='static')


# NOTE THAT NO ROUTE IS NEEDED TO RUN THIS

if __name__ == '__main__':
    app.run(debug=True, port=5000)

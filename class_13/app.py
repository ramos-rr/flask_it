# Class 13 - File Upload
# USE SEND_FILE FUNCTION to help return a file as response
from flask import Flask, render_template, request, send_file

# IMPORT THE FOLLOW LIBRARY TO HELP TRANSFORM FILE FROM BINARY TO ITS NORMAL STATE
from werkzeug.utils import secure_filename

# Let's define the right folder to storage uploded files
import os


app = Flask(__name__, template_folder='templates', static_folder='static')

# USE OS.PATH.JOIN(<param1>, <param2>) to avoid "\" or "/", so it will be flexible to all operational systems
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Code
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=["POST"])
def upload():
    file = request.files["image"]  # "image" is the name given in html to the upload box
    save_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file_name = secure_filename(file.filename)
    file.save(save_path)
    return render_template('upload.html', file_name=file_name)


@app.route("/get_file/<file_name>")
def get_file(file_name):
    file = os.path.join(UPLOAD_FOLDER, file_name)
    return send_file(file, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, port=13000)

from flask import Flask, request, render_template, redirect, url_for
import csv
import os

PICTURE_FOLDER = os.path.join('static', 'picture_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)

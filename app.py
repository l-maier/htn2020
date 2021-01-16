from flask import Flask, request, render_template, redirect, url_for
import json
import os

from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

#PICTURE_FOLDER = os.path.join('static', 'picture_photo')

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

@app.route('/')
def home():
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)

from flask import Flask, request, render_template, redirect, url_for
import json
import os
from linkedinScraper import LinkedinScraper

app = Flask(__name__)

scrapp = LinkedinScraper()

@app.route('/')
def home():  
    return render_template("index.html")

@app.route('/go', methods=["POST"])
def letsgo():
    url_input = request.form.get('url')
    scrapp.scrap(url_input)
    about = scrapp.getAbout()
    return about

if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)
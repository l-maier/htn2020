from flask import Flask, request, render_template, redirect, url_for
import json
import os
from linkedinScraper import LinkedinScraper

app = Flask(__name__)


@app.route('/')
def home():  
    return render_template("index.html")

@app.route('/go', methods=["POST"])

def letsgo():
    usr_email = request.form.get('email')
    usr_password = request.form.get('password')
    url_input = request.form.get('url')
    scrapp = LinkedinScraper(usr_email,usr_password)
    scrapp.scrap(url_input)

    about = scrapp.getAbout()
    edu = scrapp.getEducation()
    job = scrapp.getCompany()
    title = scrapp.getTitle()

    if about != '':
        return render_template('questions.html', question='huh some smug question', yes='yes', no='no')
    else:
        pass
        return 'yya'

if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)
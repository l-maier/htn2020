from flask import Flask, request, render_template, redirect, url_for
import json
import os
from linkedinScraper import LinkedinScraper

app = Flask(__name__)
state = -1
has_question = {}
question = {}
yes_answer = {}
no_answer = {}

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

    about = scrapp.getAbout() # state 0
    edu = scrapp.getEducation() # state 1
    job = scrapp.getCompany() # state 2
    title = scrapp.getTitle() # state 3

    if about != '':
        has_question[0] = True
        question[0] = 'about'
        yes_answer[0] = 'yes'
        no_answer[0] = 'no'
    else:
        has_question[0] = False
    
    if edu != '':
        has_question[1] = True
        question[1] = 'edu'
        yes_answer[1] = 'yes'
        no_answer[1] = 'no'
    else:
        has_question[1] = False

    if job != '':
        has_question[2] = True
        question[2] = 'about'
        yes_answer[2] = 'yes'
        no_answer[2] = 'no'
    else:
        has_question[2] = False

    if title != '':
        has_question[3] = True
        question[3] = 'about'
        yes_answer[3] = 'yes'
        no_answer[3] = 'no'
    else:
        has_question[3] = False
    
    state = -1
    question[-1] = 'Are you ready?'
    yes_answer[-1] = 'Yes...'
    no_answer[-1] = 'No but do I have a choice?'
    return render_template('questions.html', question=question[state], yes=yes_answer[state], no=[state])


@app.route('/huh', methods=["POST"])
def questions():
    """
    if request.form['answer'] == yes_answer[state]:
        return 'wow yes'
    if request.form['answer'] == no_answer[state]:
        return 'wow no'
    return 'huh ?'
    """
    state = state + 1
    while state < 4 and has_question[state] == False:
        state = state + 1

    if state < 4:
        return render_template('questions.html', question=question[state], yes=yes_answer[state], no=[state])
    else:
        return render_template('ending.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)
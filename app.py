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

    about = scrapp.getAbout()
    edu = scrapp.getEducation()
    job = scrapp.getCompany()
    title = scrapp.getTitle()

    if about != '':
        has_question[0] = True
        question[0] = ''
        yes_answer[0] = ''
        no_answer[0] = ''
    else:
        has_question[0] = False
    
    if edu != '':
        has_question[1] = True
        ## copy paste this for everything
    else:
        has_question[1] = False
    
    state = -1
    question[-1] = 'Are you ready?'
    yes_answer[-1] = 'Yes...'
    no_answer[-1] = 'No but do I have a choice?'
    return render_template('questions.html', question=question[state], yes=yes_answer[state], no=[state])


@app.route('/huh', methods=["POST"])
def question():
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
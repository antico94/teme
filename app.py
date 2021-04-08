import data

import dotenv
from flask import Flask, render_template, request, redirect, url_for, make_response, session, escape
from data_manager import *

dotenv.load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    if 'email' in session:
        return render_template('index.html', is_logged_in=True, email=escape(session['email']))
    else:
        return render_template('index.html', is_logged_in=False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # hashed_password=hash_password(password)
        if get_password_for_user(email) != None:
            db_password = get_password_for_user(email)['password']
        else:
            return render_template("login.html", is_not_matching=True)
        is_matching = verify_password(password, db_password)
        if is_matching:
            session['email'] = email
            session['question_id'] = 0
            session['correct_results'] = 0
            return redirect(url_for('index'))
        else:
            return render_template("login.html", is_not_matching=True)
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = hash_password(password)
        if get_email(email) != None:
            return render_template('register.html', existance=True)
        else:
            add_user(email, hashed_password)
            return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    session.pop('question_id', None)
    session.pop('correct_results', None)
    return redirect(url_for('index'))


@app.route('/test')
def test():
    if 'email' in session:
        answer = request.cookies.get('question_answer')
        if session['question_id'] !=0:
            compared_question= get_next_question(session['question_id']-1)
            if answer == compared_question['answer']:
                session['correct_results'] += 1
        if session['question_id'] == get_number_of_questions()['count']:
            return redirect(url_for('result'))
        question = get_next_question(session['question_id'])
        return render_template('test.html', question=question)
    else:
        return redirect(url_for('index'))


@app.route('/result')
def result():
    number_of_questions = get_number_of_questions()['count']
    return render_template('result.html', correct_answer=session['correct_results'],
                           number_of_questions=number_of_questions)

@app.route('/set-cookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user_answer = request.form['answer']
        session['question_id'] += 1
        redirect_to_index = redirect(url_for('test'))
        response = make_response(redirect_to_index)
        response.set_cookie('question_answer', value=user_answer)
        return response


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'redis'

    app.run(debug=True)

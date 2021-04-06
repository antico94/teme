import data

import dotenv
from flask import Flask, render_template, request, redirect, url_for
from data_manager import *


dotenv.load_dotenv()
app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for("login"))


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)

# -*- coding: utf-8-*-
from flask import render_template
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Godkin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)


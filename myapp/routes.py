# -*- coding: utf-8-*-
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"


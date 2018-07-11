# -*- coding: utf-8-*-
from myapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Godkin'}
    return '''
<html>
    <head>
        <title>Home Page - My Flask App</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

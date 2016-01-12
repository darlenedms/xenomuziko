# -*- coding: utf-8 -*-

from bottle import Bottle, template, request

app = Bottle()


@app.get('/')
def index():
    return template('index')


@app.post('/result')
def result():
    username = request.forms.get('username')
    return template('result', username=username)


@app.error(404)
def error404(error):
    return template('404')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

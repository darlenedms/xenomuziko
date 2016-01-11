# -*- coding: utf-8 -*-

from bottle import Bottle, template

app = Bottle()


@app.get('/')
def index():
    return template('index')


@app.error(404)
def error404(error):
    return template('404')


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

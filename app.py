# -*- coding: utf-8 -*-

from bottle import Bottle

app = Bottle()


@app.get('/')
def index():
    return 'Hello World!'


@app.error(404)
def error404(error):
    return 'Nothing here, sorry'


if __name__ == '__main__':
    app.run(host='localhost', port=8080)

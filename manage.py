#! /usr/bin/env python3
from flask import FLask
app = Flask(__name__)
app.debug = True

from flask_script import Manager

manager = Manager(app)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

if __name__ == '__main__':
    manage.run()

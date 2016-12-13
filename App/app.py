from flask import FLask
app = Flask(__name__)
app.debug = True

from flask_script import Manager

manager = Manager(app)

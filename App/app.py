#-------------------- Flask --------------------#
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
app.debug = True

manager = Manager(app)
#-------------------- Bootstrap --------------------#
from flask_bootstrap import Bootstrap
app.config['BOOTSTRAP_SERVE_LOCAL']=True
Bootstrap(app)


#-------------------- SQLAlchemy --------------------#
from flask_sqlalchemy import SQLAlchemy
import os.path

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p
        )
    )

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('/myApp.db'))

db = SQLAlchemy(app)

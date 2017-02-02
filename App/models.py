from .app import db
from sqlalchemy import text
from flask_login import UserMixin

class Author(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    nameA    = db.Column(db.String(100))

class Player(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    nameP    = db.Column(db.String(100))

class Genre(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    nameG    = db.Column(db.String(100))

class User(db.Model, UserMixin):
    id      = db.Column(db.Integer, primary_key = True)
    username    = db.Column(db.String(100))
    password    = db.Column(db.String(100))
    imgProfil   = db.Column(db.String(100))
    typeUSer = db.Column(db.String(100))

    def get_id(self):
        return self.id

class Appartient(db.Model):
    id      = db.Column(db.Integer, primary_key = True)

    album_id = db.Column(db.Integer, db.ForeignKey("album.id"))
    album = db.relationship("Album", backref = db.backref("appartient", lazy ="dynamic"))

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre", backref = db.backref("appartient", lazy ="dynamic"))

class Listen(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id      = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref = db.backref("listen", lazy ="dynamic"))

    album_id      = db.Column(db.Integer, db.ForeignKey("album.id"))
    album = db.relationship("Album", backref = db.backref("listen", lazy ="dynamic"))

class Album(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    title       = db.Column(db.String(100))
    img         = db.Column(db.String(100))
    year        = db.Column(db.String(100))

    author_id   = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", backref = db.backref("album", lazy ="dynamic"))


    player_id  = db.Column(db.Integer, db.ForeignKey("player.id"))
    player = db.relationship("Player", backref = db.backref("album", lazy ="dynamic"))



def get_UserData(name):
    return User.query.filter_by(username=name).first()

def get_ListenAlbumUSer(name):
    result = db.engine.execute('select img from Album natural join Listen natural join User where username ="'+name+'"')
    names = []
    for row in result:
        names.append(row)
    return names
def get_Albums():
    return Album.query.all()

def get_Genre():
    return Genre.query.all()

def get_AlbumsByYear(y):
    return Album.query.filter_by(year=y).all()

def get_AlbumsByGenre(genre):
    #sql = text('select * from Album natural join Appartient natural join Genre where nameG = (1)', genre)
    #print(sql)
    result = db.engine.execute('select title,img from Album natural join Appartient natural join Genre where nameG ="'+genre+'"')
    names = []
    for row in result:
        names.append(row)
    return names

def get_AlbumsByGenreByYear(genre, year):
    #sql = text('select * from Album natural join Appartient natural join Genre where nameG = (1)', genre)
    #print(sql)
    result = db.engine.execute('select title,img from Album natural join Appartient natural join Genre where nameG ="'+genre+'" and year ="'+year+'"')
    names = []
    for row in result:
        names.append(row)
    return names


from .app import login_manager

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

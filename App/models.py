from .app import db
from sqlalchemy import text

class Author(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    nameA    = db.Column(db.String(100))

class Player(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    nameP    = db.Column(db.String(100))

class Genre(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    nameG    = db.Column(db.String(100))

class User(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    login    = db.Column(db.String(100))
    password    = db.Column(db.String(100))
    typeUSer = db.Column(db.String(100))

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




def get_Albums():
    return Album.query.all()

def get_AlbumsByGenre(genre):
    #sql = text('select * from Album natural join Appartient natural join Genre where nameG = (1)', genre)
    #print(sql)
    result = db.engine.execute('select title,img from Album natural join Appartient natural join Genre where nameG ="'+genre+'"')
    names = []
    for row in result:
        names.append(row)
    return names

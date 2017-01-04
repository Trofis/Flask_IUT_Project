from .app import db

class Individu(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(100))

class Genre(db.Model):
    id      = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(100))

class Music(db.Model):
    id          = db.Column(db.Integer, primary_key = True)
    title       = db.Column(db.String(100))
    img         = db.Column(db.String(100))
    year        = db.Column(db.String(100))
    author_id   = db.Column(db.Integer, db.ForeignKey("Individu.id"))
    players_id  = db.Column(db.Integer, db.ForeignKey("Individu.id"))
    genre       = [db.Column(db.Integer, db.ForeignKey("Genre.id"))]

db.session.add(Individu)
db.session.add(Genre)
db.session.add(Music)
db.session.commit()


def get_Albums():
    return Music.query.all()

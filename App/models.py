from .app import db

class Author(db.Model):
    __tablename__ = 'author'
    id      = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(100))

class Player(db.Model):
    __tablename__ = 'player'
    id      = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(100))

class Genre(db.Model):
    __tablename__ = 'genre'
    id      = db.Column(db.Integer, primary_key = True)
    name    = db.Column(db.String(100))

class User(db.Model):
    __tablename__ = 'user'
    id      = db.Column(db.Integer, primary_key = True)
    login    = db.Column(db.String(100))
    password    = db.Column(db.String(100))

class Appartient(db.Model):
    __tablename__ = 'appartient'
    id      = db.Column(db.Integer, primary_key = True)

    music_id = db.Column(db.Integer, db.ForeignKey("music.id"))
    music = db.relationship("Music", foreign_keys=[music_id])

    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre", foreign_keys=[genre_id])

class Listen(db.Model):
    __tablename__ = 'listen'
    id = db.Column(db.Integer, primary_key = True)
    user_id      = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", foreign_keys=[user_id])

    music_id      = db.Column(db.Integer, db.ForeignKey("music.id"))
    music = db.relationship("Music", foreign_keys=[music_id])

class Music(db.Model):
    __tablename__ = 'music'
    id          = db.Column(db.Integer, primary_key = True)
    title       = db.Column(db.String(100))
    img         = db.Column(db.String(100))
    year        = db.Column(db.String(100))

    author_id   = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", foreign_keys=[author_id])


    player_id  = db.Column(db.Integer, db.ForeignKey("player.id"))
    player = db.relationship("Player", foreign_keys=[player_id])









def get_Albums():
    return Music.query.all()

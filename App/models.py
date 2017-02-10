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


def get_Player():
    return Player.query.all()

def get_Author():
    return Author.query.all()

def get_Compo(title):
    try:
        resultIdCompo = db.engine.execute('select author_id from Album where title="'+title+'"').first();
        print(resultIdCompo)
        resultNameCompo = db.engine.execute('select nameA from Author where id="'+str(resultIdCompo[0])+'"').first();
        result = resultNameCompo[0]
        return result
    except Exception as e:
        return None
def ifAlbumExist(title, compo, art):
    if (Album.query.filter_by(title=title,author_id=compo, player_id=art).first() != None):
        return True
    return False

def insertAlbum(gen, title, year, compo, art):
    from sqlalchemy.sql.expression import func
    id = db.session.query(func.max(Album.id))[0][0] + 1
    o = Album(id = id, title = title, year = year, author_id=compo, player_id=art)
    a = Appartient(album_id=id, genre_id=gen)
    db.session.add(o)
    db.session.add(a)

    db.session.commit()
def deleteAlbum(idAlb):
    Appartient.query.filter_by(album_id=idAlb).delete()
    Listen.query.filter_by(album_id=idAlb).delete()
    Album.query.filter_by(id=idAlb).delete()
    db.session.commit()
def get_Artiste(title):
    try:
        resultId = db.engine.execute('select player_id from Album where title="'+title+'"').first();
        resultName = db.engine.execute('select nameP from Player where id="'+str(resultId[0])+'"').first();
        result = resultName[0]
        return result
    except Exception as e:
        return None


def get_genreAlb(title):
    resultArt = db.engine.execute('select nameG from Album natural join Appartient natural join Genre where title="'+title+'"');
    result = []
    for row in resultArt:
        result.append(row[0])
    return result
def setLike(idAlb, idUSer):
    o = Listen(
        user_id = idUSer,
        album_id = idAlb
    )
    if (len(Listen.query.filter_by(user_id=idUSer, album_id=idAlb).all()) == 0):
        db.session.add(o)
        db.session.commit()


def get_AlbumsDataByUsername(name):
    return Album.query.filter_by(title=name).first()

def get_UserData(name):
    return User.query.filter_by(username=name).first()

def get_ListenAlbumUSer(username):
    idUser = get_UserData(username).id
    resultListen = db.engine.execute('select album_id from Listen where user_id="'+str(idUser)+'"');
    result = []
    i= 0
    for elem in resultListen:
        q = db.engine.execute('select img from Album where id ="'+str(elem[0])+'"')
        for row in q:
            result.append(row)
    names = []
    for row in result:
        names.append(row[0])
    print(names)
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
    result = db.engine.execute('select album_id from Appartient natural join Genre where nameG="'+genre+'"')
    alb = []
    for idAlb in result:
        alb.append(db.engine.execute('select title,img from Album where id ="'+str(idAlb[0])+'"'));
    albResult = []
    for row in alb:
        for r in row:
            albResult.append(r)
    return albResult

def get_AlbumsByGenreByYear(genre, year):
    #sql = text('select * from Album natural join Appartient natural join Genre where nameG = (1)', genre)
    #print(sql)
    result = db.engine.execute('select album_id from Appartient natural join Genre where nameG="'+genre+'"')
    alb = []
    for idAlb in result:
        alb.append(db.engine.execute('select title,img from Album where year ="'+str(year)+'"  and id ="'+str(idAlb[0])+'"'));
    albResult = []
    for row in alb:
        for r in row:
            albResult.append(r)
    return albResult


from .app import login_manager

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

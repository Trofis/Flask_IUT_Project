from .app import manager, db

@manager.command
def loaddb(filename):
    "parameters : filename"
    db.create_all()


    import yaml
    albums = yaml.load(open(filename))

    from .models import Album, Author, Genre, Player, Appartient


    author = {}
    player = {}
    gender = {}
    for m in albums:
        a = m["by"]
        p = m["parent"]
        g = m["genre"]
        if a not in author:
            o = Author(nameA=a)
            db.session.add(o)
            author[a] = o

        if p not in player:
            o = Player(nameP=p)
            db.session.add(o)
            player[p] = o

        for genre in g:
            if genre not in gender:
                o = Genre(nameG=genre)
                db.session.add(o)
                gender[genre] = o
        db.session.commit()

    for m in albums:
        a = author[m["by"]]
        p = player[m["parent"]]
        lg = m["genre"]
        mus = Album(  title = m["title"],
                    img = m["img"],
                    year = m["releaseYear"],
                    author_id = a.id,
                    player_id = p.id
                    )
        for g in lg:
            og = gender[g]
            o = Appartient(
                album_id = mus.id,
                genre_id = og.id
            )
            db.session.add(o)
        db.session.add(mus)
    db.session.commit()



@manager.command
def addUser(_login, _password, _type):
    "parameters : login, password, type"
    from .models import User
    user = User(login=_login, password=_password,typeUSer = _type )
    db.session.add(user)
    db.session.commit()

@manager.command
def addGenreOrAuthorOrPlayer(name, typeCom):
    "parameters : name, type"
    from .models import Genre, Author, Player
    if typeCom == "Player":
        o = Player(name = name)
    if typeCom == "Author":
        o = Author(name = name)
    if typeCom == "Genre":
        o = Genre(name = name)
    db.session.add(o)
    db.session.commit()

@manager.command
def addListenForOneUser(id_User, id_Album):
    "parameters : id_User, id_Albums"
    from .models import Album, Player, Author, Genre, Appartient
    a = Appartient.query.filter_by(user_id = id_User, album_id= id_Album)
    if a is None:
        o = Appartient(user_id = id_User, album_id= id_Album)
        db.session.add(o)
        db.session.commit()


@manager.command
def addAlbum(_author_id, _player_id, _genre, _titre, _image, _year ):
    "parameters : _author_id, _player_id, _genre, _titre,_image, _year "
    from .models import Album, Player, Author, Genre, Appartient
    p = Player.query.filter_by(id = _player_id)
    a = Author.query.filter_by(id = _author_id)
    if p is not None and a is not None:
        alb = Album(title=_titre, img=_image, year = _year, author_id = _author_id, player_id= _player_id)
        for g in _genre:
            g_query = Genre.query.filter_by(name = _genre)
            if g_query is None:
                app = Appartient(alb.id, g_query.id)
            else:
                go = Genre(name = _genre)
                app = Appartient(album_id = alb.id, genre_id= go.id)
                db.session.add(go)
            db.session.add(app)
            db.session.commit()

        db.session.add(alb)
        db.session.commit()
    else:
        print("Author or Player does not exist")

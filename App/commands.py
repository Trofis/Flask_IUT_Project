from .app import manager, db

@manager.command
def loaddb(filename):

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
            o = Author(name=a)
            db.session.add(o)
            author[a] = o

        if p not in player:
            o = Player(name=p)
            db.session.add(o)
            player[p] = o

        for genre in g:
            if genre not in gender:
                o = Genre(name=genre)
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
    from .models import User
    user = User(login=_login, password=_password,typeUSer = _type )
    db.session.add(user)
    db.session.commit()

@manager.command
def addAlbum(_author_id, _player_id, _genre, _titre, _image, _year ):
    from .models import Album, Player, Author, Genre, Appartient
    p = Player.query.filter(Player.id = _player_id)
    a = Author.query.filter(Author.id = _author_id)
    if p not null and a not null:
        alb = Album(title=_titre, img=_image, year = _year, author_id = _author_id, player_id= _player_id)
        for g in _genre:

        db.session.add(user)
        db.session.commit()
    else:
        print("Author or Player does not exist")

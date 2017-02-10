from .app import app, db
from flask import render_template, request
from .models import *

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        idAlb = request.values["albumId"]
        idUser = request.values["userId"]
        setLike(idAlb, idUser)
    return render_template(
        "home.html",
        title = "Home",
        Albums = get_Albums(),
        basealb=get_Albums())

@app.route("/profil")
def profil():
    if current_user.is_authenticated:
        user = get_UserData(current_user.username)
        listen = get_ListenAlbumUSer(current_user.username)
        for elem in listen:
            print(elem)
        return render_template("profil.html", Pseudo = user.username, imgprofil= user.imgProfil, lImg = listen, basealb=get_Albums())

@app.route("/album/<string:title>")
def albumpage(title):
    album = get_AlbumsDataByUsername(title)
    compo = get_Compo(title)
    artiste =get_Artiste(title)

    genre =get_genreAlb(title)
    return render_template("albumpage.html", albumInfo=album, basealb=get_Albums(), compo= compo, artiste=artiste, genre=genre )

@app.route("/addAlbum", methods=["POST", "GET"])
def addAlbum():
    if current_user.is_authenticated and current_user.typeUSer == "admin":
        lGenre = get_Genre()
        lCompo = get_Author()
        lArt = get_Player()
        if request.method == "GET":
            return render_template("addAlbum.html", title="AddAlbum", basealb=get_Albums(), genre=lGenre, artiste=lArt, compositeur=lCompo, error="")

        else:
            gen = request.values["genre"]
            title = request.values["title"]
            year = request.values["year"]
            compo = request.values["compositeur"]
            art = request.values["artiste"]

            if (ifAlbumExist(title, compo, art)):
                return render_template("addAlbum.html", title="AddAlbum", basealb=get_Albums(), error = "Album already in base", genre=lGenre, artiste=lArt, compositeur=lCompo)
            else:
                insertAlbum(gen, title, year, compo, art)
                return redirect("/")




@app.route("/album/album/<string:title>")
def albumpageCorrect(title):
    album = get_AlbumsDataByUsername(title)
    compo = get_Compo(title)
    artiste =get_Artiste(title)
    print(compo)
    genre =get_genreAlb(title)
    return redirect(url_for("albumpage", title=title))
@app.route("/SearchAlbum", methods=["POST", "GET"])
def searchAlb():
    gen = ""
    g = False
    y = False
    if request.method == "POST":
        typeR="POST"
        alb = []

        fil = request.form.getlist("filter")

        if (request.form.getlist("albumId")):
            idAlb = request.values["albumId"]
            idUser = request.values["userId"]
            setLike(idAlb, idUser)

        if request.form.getlist('filter'):

            if ("genre" in request.form["filter"] and "year" in request.form.getlist("filter")):
                opt = request.form['genre']
                yea = request.form['year']
                y = True
                g = True
                if (opt is not None):
                    alb = get_AlbumsByGenreByYear(opt, yea)
                    gen = opt


            elif ("genre" in request.form["filter"]):
                g = True
                opt = request.form['genre']
                if (opt is not None):
                    alb = get_AlbumsByGenre(opt)
                    print(alb)

                    gen = opt
            elif ("year" in request.form["filter"]):
                y = True
                yea = request.form['year']
                alb = get_AlbumsByYear(yea)

    else:
        typeR="GET"
        alb = get_Albums()
        fil = []
    year = [str(2017-i) for i in range(0,40)]

    return render_template(
        "SearchAlbum.html",
        title = "SearchAlbum",
        Albums = alb,
        genreAct = gen,
        genre= get_Genre(),
        years= year,
        typeR=typeR,
        genreI=g,
        yearI=y,
        basealb=get_Albums())


#---------------------------LoginForm-----------------------------#
from wtforms import PasswordField, StringField, HiddenField
from .models import User
from hashlib import sha256
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    def get_authenticated_user(self):
        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

class SignUpForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    confirmPassword = PasswordField("ConfirmPassword")

    def get_authenticated_user(self):
        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            if (self.password.data.encode() == self.confirmPassword.data.encode()):
                m = sha256()
                m.update(self.password.data.encode())
                passwd = m.hexdigest()
                u = User(username=self.username.data, password=passwd, typeUSer= "client")
                db.session.add(u)
                db.session.commit()
                return u
        return None

from flask_login import login_user, current_user, logout_user
from flask import request, redirect, url_for

@app.route("/signin", methods=("GET", "POST"))
def signin():
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template(
        "signin.html",
        title = "SignIn",
        form = f,
        basealb=get_Albums())




@app.route("/signout", methods=("GET", "POST"))
def signout():
    f = SignUpForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template(
        "signout.html",
        title = "SignOut",
        form = f,
        basealb=get_Albums())

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

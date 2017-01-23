from .app import app
from flask import render_template, request
from .models import get_Albums, get_AlbumsByGenre

@app.route("/")
def home():
    return render_template(
        "home.html",
        title = "Patronat & Mendes Musics",
        Albums = get_Albums())


@app.route("/signin")
def signin():
    return render_template(
        "signin.html",
        title = "SignIn")


@app.route("/SearchAlbum", methods=["POST", "GET"])
def searchAlb():
    if request.method == "POST":
        opt = request.form['genre']
        if (opt is not None):
            alb = get_AlbumsByGenre(opt)
        else:
            alb =[]
    else:
        alb = get_Albums()
    print(alb)
    return render_template(
        "SearchAlbum.html",
        title = "SearchAlbum",
        Albums = alb)

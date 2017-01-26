from .app import app
from flask import render_template, request
from .models import get_Albums, get_AlbumsByGenre, get_Genre, get_AlbumsByGenreByYear, get_AlbumsByYear

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
    gen = ""
    g = False
    y = False
    if request.method == "POST":
        typeR="POST"
        alb = []
        fil = request.form.getlist("filter")

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
    print(request.form.getlist("filter"))

    return render_template(
        "SearchAlbum.html",
        title = "SearchAlbum",
        Albums = alb,
        genreAct = gen,
        genre= get_Genre(),
        years= year,
        typeR=typeR,
        genreI=g,
        yearI=y)

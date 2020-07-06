from app import app, db
from app.forms import AddFilmForm, RemoveFilmForm, ImportDataForm, ClearDataForm
from app.models import Film
from flask import render_template, flash, redirect, url_for
from datetime import datetime
import requests
import random
import re

@app.route('/')
@app.route('/index')
def index():
    films = Film.query.all()
    return render_template("index.html", films=films)

@app.route('/add_film', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        film = Film(title=form.title.data, year=form.year.data, runtime=form.runtime.data,\
        plot=form.plot.data, releasedate=form.releasedate.data, director=form.director.data,
        actors=form.actors.data)
        db.session.add(film)
        db.session.commit()
        flash("{} ({}) has been added to the database!".format(form.title.data, form.year.data))
        return redirect(url_for('index'))
    return render_template("add_film.html", form=form)

@app.route('/remove_film', methods=['GET', 'POST', 'DELETE'])
def remove_film():
    form = RemoveFilmForm()
    if form.validate_on_submit():
        title = form.title.data
        films = Film.query.all()
        titles = []
        # we're first just going to check that the film actually exists
        for film in films:
            # if it does, continue as planned
            if film.title == title:
                film = Film.query.filter_by(title=title).first() # arbitrarily remove the first film
                db.session.delete(film)
                db.session.commit()
                flash("{} has been removed from the database!".format(form.title.data))
                return redirect(url_for('index'))
        # if not, try again
        flash("That film doesn't exist.")
        return redirect(url_for('remove_film'))
    return render_template("remove_film.html", form=form)

@app.route('/import_films', methods=['GET', 'POST'])
def import_films():
    form = ImportDataForm()
    if form.validate_on_submit():
        # we need our API key to access the data
        api = open("apikey.txt", "r")
        apikey = api.read()
        # now we want to import some random films
        for i in range(30):
            # first we need to generate a random but valid IMDb film id
            id = "tt"+str(random.randrange(6))+str(random.randrange(10))+str(random.randrange(10))\
            +str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))
            # then we can build a URL from that id and my apikey
            url = "http://www.omdbapi.com/?i="+id+"&type=movie"+"&apikey="+apikey
            # then we need to request that film from the open IMDb and convert it to a nice format
            filmData = requests.get(url).json()
            # then we check it's worked
            if filmData["Response"] == "True" and not "Episode" in filmData["Title"]:
                # if it has, we need to coerce the values we want into the right format then make a Film object
                s = filmData["Runtime"]
                runningtime = re.sub("[^0-9]", "", s)

                if runningtime == "":
                    runningtime = 0
                else:
                    runningtime = int(runningtime)

                if filmData["Year"] == "":
                    filmyear = 0
                else:
                    if "–" in filmData["Year"]:
                        temp = filmData["Year"]
                        filmyear = int(temp[0:4])
                    else:
                        filmyear = int(filmData["Year"])


                if filmData["Released"] == "" or filmData["Released"] == "N/A":
                    date = "01 Jan 2100"
                    filmreleased = datetime.strptime(date, "%d %b %Y")
                else:
                    filmreleased = datetime.strptime(filmData["Released"], "%d %b %Y")

                if filmData["Plot"] == "N/A":
                    filmplot = "No description is available for this film."
                else:
                    filmplot = filmData["Plot"]

                film = Film(title=filmData["Title"], year=filmyear, runtime=runningtime,\
                plot=filmplot, releasedate=filmreleased, director=filmData["Director"],\
                actors=filmData["Actors"])
                # then we want to add this object to the database
                db.session.add(film)
            db.session.commit()
        flash("The new films have been imported!")
        return redirect(url_for('index'))
    return render_template("import_films.html", form=form)

@app.route('/delete_all_films', methods=['GET', 'POST', 'DELETE'])
def delete_all_films():
    form = ClearDataForm()
    if form.validate_on_submit():
        films = Film.query.all()
        for film in films:
            db.session.delete(film)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("delete_all_films.html", form=form)

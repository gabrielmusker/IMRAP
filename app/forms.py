from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange
from app import db
from app.models import Film

class AddFilmForm(FlaskForm):
    title = StringField("Film Title", validators=[DataRequired()])
    year = IntegerField("Year Released", validators=[DataRequired("This must be a valid year."), \
    NumberRange(min=1878)]) # year first film was released

    runtime = IntegerField("Running Time (in minutes)", validators=[DataRequired("This must be a positive integer."), \
    NumberRange(min=0, max=14400)]) # running time of longest ever film - 240 hours!

    plot = StringField("Synopsis")
    releasedate = DateField("Date of release (dd-mm-yyyy)", validators=[DataRequired()], format="%d-%m-%Y")
    director = StringField("Director", validators=[DataRequired()])
    actors = StringField("Actors", validators=[DataRequired()])

    submit = SubmitField("Add Film")

class RemoveFilmForm(FlaskForm):
    title = StringField("Film Title", validators=[DataRequired()])
    submit = SubmitField("Remove Film")

class ImportDataForm(FlaskForm):
    submit = SubmitField("Import Some Random Films from IMDB")

class ClearDataForm(FlaskForm):
    submit = SubmitField("Clear all films from the database.")

from app import db

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True) # since film titles may not be unique
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    plot = db.Column(db.String)
    releasedate = db.Column(db.DateTime)
    director = db.Column(db.String)
    actors = db.Column(db.String)

    def __repr__(self):
        return '<Film {} ({})>'.format(self.title, self.year)

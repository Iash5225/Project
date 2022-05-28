from flask_login import UserMixin
from sqlalchemy import ForeignKey
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    highscore = db.Column(db.Integer)
    lastplayed = db.Column(db.Date)
    
    
class Scores(db.Model):
    score_log_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey(User.id))
    score = db.Column(db.Integer)
    date = db.Column(db.Date)


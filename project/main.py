import imp
from select import select
from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from .models import User, Scores
from . import db
from sqlalchemy import desc, select

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/game')
@login_required
def game():
    leaderboard = db.session.execute(select(User.name, User.highscore)
                                     .order_by(User.highscore, User.name)
                                     .limit(10))
    leaderboard_names = []
    leaderboard_scores = []
    for row in leaderboard:
        leaderboard_names.append(row.name)
        leaderboard_scores.append(row.highscore)
        
    return render_template('game.html',
                           name = current_user.name,
                           lb_names = leaderboard_names,
                           lb_scores = leaderboard_scores)

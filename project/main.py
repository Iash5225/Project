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
    
    # get user's score history from db to render personal stats
    user_score_history = db.session.execute(select(Scores.score)
                                            .filter_by(Scores.userid == current_user.userid)
                                            .order_by(Scores.date))
    
    user_scores = [row.score for row in user_score_history]
    
    # get leaderboard from db to render leaderboard
    leaderboard = db.session.execute(select(User.name, User.highscore)
                                     .order_by(User.highscore, User.name)
                                     .limit(10))
    
    leaderboard_names = [row.name for row in leaderboard]
    leaderboard_scores = [row.highscore for row in leaderboard]
        
    return render_template('game.html',
                           name = current_user.name,
                           lb_names = leaderboard_names,
                           lb_scores = leaderboard_scores,
                           stats = user_scores)

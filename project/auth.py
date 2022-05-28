from datetime import date
from flask import Blueprint, render_template, redirect, session, url_for, request, flash, Response
from sqlalchemy import Date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Scores, User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.game'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), highscore=0)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/delete')
@login_required
def delete(): 
    user = User.query.get(current_user.id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('auth.signup'))


@auth.route('/submit', methods=['POST', 'GET'])
@login_required
def submit():
    cur_score = int(request.form.get('score'))
    cur_date = date.today()  
    user: User = User.query.get(current_user.id)
    
    # Have they already played today?
    if (user.lastplayed == cur_date):
        return redirect(url_for('main.index'))
    
    # Log their score
    new_score = Scores(userid=user.id, score=cur_score, date=cur_date)
    db.session.add(new_score)
    
    print(user, "submitted a score of", cur_score, "on", cur_date)
    
    # Was it a personal highscore?
    if not user.highscore or user.highscore < cur_score:
        user.highscore = cur_score
    
    user.lastplayed = cur_date;

    db.session.commit()
    
    return redirect(url_for('main.index'))
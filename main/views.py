import datetime
import json
from flask import Blueprint, request
from flask import Flask, render_template, request, redirect, flash, url_for
from stepler import db, User
from flask_login import login_user, current_user, logout_user, login_required


main_page = Blueprint('main_page', __name__)


@main_page.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))


@main_page.route('/index.html')
@main_page.route('/')
@login_required
def index():
    return render_template('index.html', title='Stepler', name=current_user.username)


@main_page.record
def record(state):
    db = state.app.config.get('SQLALCHEMY_DATABASE_URI')

    if db is None:
        raise Exception("This blueprint expects you to provide database access through orders.db")


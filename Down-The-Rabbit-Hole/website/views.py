from flask import Blueprint, jsonify, render_template, flash, request
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def landing():
    return render_template("landing.html")

@views.route('/message')
@login_required
def see_message():
    return render_template("message.html")

@views.route('/options', methods=['GET', 'POST'])
@login_required
def theme_options():
    return render_template("options.html")

@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    return render_template("history.html")

@views.route('/art', methods=['GET', 'POST'])
@login_required
def art():
    return render_template("art.html")

@views.route('/music', methods=['GET', 'POST'])
@login_required
def music():
    return render_template("music.html")

@views.route('/tech', methods=['GET', 'POST'])
@login_required
def tech():
    return render_template("tech.html")

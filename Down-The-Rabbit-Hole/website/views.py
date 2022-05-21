from flask import Blueprint, jsonify, render_template, flash, request, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("landing.html")

@views.route('/message')
def see_message():
    return render_template("message.html")

@views.route('/options', methods=['GET', 'POST'])
def theme_options():
    return render_template("options.html")

@views.route('/history', methods=['GET', 'POST'])
def history():
    return render_template("history.html")

@views.route('/art', methods=['GET', 'POST'])
def art():
    return render_template("art.html")

@views.route('/music', methods=['GET', 'POST'])
def music():
    return render_template("music.html")

@views.route('/tech', methods=['GET', 'POST'])
def tech():
    return render_template("tech.html")

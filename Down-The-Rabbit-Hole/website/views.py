from flask import Blueprint, jsonify, render_template, flash, request, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template("landing.html")

@views.route('/options', methods=['GET', 'POST'])
def theme_options():
    return render_template("options.html")